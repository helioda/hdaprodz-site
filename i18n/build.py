#!/usr/bin/env python3
"""Generate the English, Portuguese and Spanish pages of the music site from the French source.

French is the source of truth: edit index.html / contact.html, then run
    python3 i18n/build.py
and commit the regenerated en/, pt/ and es/ folders. The script stops with an
error if a French text has no translation, so nothing is published half-translated.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from strings import PAGES, TEXT  # noqa: E402

HOME = {"fr": "/", "en": "/en/", "pt": "/pt/", "es": "/es/"}
FORM = {"fr": "/contact.html", "en": "/en/contact.html", "pt": "/pt/contato.html", "es": "/es/contacto.html"}
HTML_LANG = {"en": "en", "pt": "pt-BR", "es": "es"}
SWITCH_LABEL = {"en": "Language", "pt": "Idioma", "es": "Idioma"}
NAMES = {"fr": "Français", "en": "English", "pt": "Português", "es": "Español"}
TRANSLATED_ATTRS = ("alt", "aria-label", "title", "content")


def switcher(urls, lang):
    links = "".join(
        f'<a href="{u}" hreflang="{l}" lang="{l}" title="{NAMES[l]}"{" aria-current=\"true\"" if l == lang else ""}>{l.upper()}</a>'
        for l, u in urls.items()
    )
    return f'<!--lang--><span class="lang-switch" aria-label="{SWITCH_LABEL[lang]}">{links}</span><!--/lang-->'


def build(src_name, lang):
    page = PAGES[src_name]
    out_name = page["out"][lang]
    t = open(os.path.join(ROOT, src_name), encoding="utf-8").read()
    urls = HOME if src_name == "index.html" else FORM

    # The brand name is never translated.

    # 1. Text between tags and selected attributes, exact segment matches only.
    missing = []
    for fr, tr in TEXT[src_name].items():
        target = tr[lang]
        pat_text = re.compile(r">(\s*)" + re.escape(fr) + r"(\s*)<")
        pat_attr = re.compile(r'((?:' + "|".join(TRANSLATED_ATTRS) + r')=")' + re.escape(fr) + '"')
        n1 = len(pat_text.findall(t))
        n2 = len(pat_attr.findall(t))
        if n1 + n2 == 0:
            missing.append(fr)
            continue
        t = pat_text.sub(lambda m: ">" + m.group(1) + target + m.group(2) + "<", t)
        t = pat_attr.sub(lambda m: m.group(1) + target + '"', t)
    if missing:
        sys.exit(f"[{lang}] {src_name}: French text not found (source changed?):\n  " + "\n  ".join(missing))


    # 2. Structure: language, links, asset paths, switcher, form language.
    t = t.replace('<html lang="fr">', f'<html lang="{HTML_LANG[lang]}">', 1)
    t = re.sub(r"<!--lang-->.*?<!--/lang-->", lambda m: switcher(urls, lang), t, count=1, flags=re.S)
    t = re.sub(r'(href|src|poster)="(assets|media)/', r'\1="/\2/', t)
    t = t.replace('href="contact.html', f'href="{FORM[lang]}')
    t = t.replace('href="index.html#', f'href="{HOME[lang]}#')
    t = t.replace('href="index.html"', f'href="{HOME[lang]}"')
    t = t.replace('class="brand" href="#"', f'class="brand" href="{HOME[lang]}"')
    subj = {"en": "Music%20project", "pt": "Projeto%20musical", "es": "Proyecto%20musical"}[lang]
    t = t.replace("subject=Projet%20musical%20HDA%20Productions", f"subject={subj}%20HDA%20Productions")
    t = t.replace('<input type="hidden" name="lang" value="fr">', f'<input type="hidden" name="lang" value="{lang}">')

    # 3. Safety net: no French words that should have been translated.
    body = re.sub(r"<style>.*?</style>|<option value=\"[^\"]*\"|<link[^>]*>|<!--lang-->.*?<!--/lang-->", "", t, flags=re.S)
    for word in page["must_not_remain"]:
        if word in body:
            sys.exit(f"[{lang}] {out_name}: French text still present: {word!r}")

    out_path = os.path.join(ROOT, lang, out_name)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    open(out_path, "w", encoding="utf-8").write(t)
    return out_path


if __name__ == "__main__":
    for src in PAGES:
        for lang in ("en", "pt", "es"):
            print("wrote", os.path.relpath(build(src, lang), ROOT))
