// Website assistant: Copilot Studio web chat in a panel.
// The iframe is created only when the visitor opens the panel, so nothing is
// loaded from Microsoft (and no conversation or credit is used) before that.
(function () {
  // Set SRC to the public web chat URL of the music agent (Copilot Studio). Empty = no button.
  var SRC = "";
  var LANG = (document.documentElement.lang || "fr").slice(0, 2).toLowerCase();
  var I18N = {
    fr: { btn: "Une question ? Assistant IA", title: "Assistant IA · HDA Productions", close: "Fermer l’assistant",
          note: "Réponses générées par IA, à vérifier. Ne partagez pas de données sensibles.", privacy: "Confidentialité", href: "/contact.html#assistant" },
    en: { btn: "Questions? AI assistant", title: "AI assistant · HDA Productions", close: "Close the assistant",
          note: "AI-generated answers, please check them. Don’t share sensitive data.", privacy: "Privacy", href: "/en/contact.html#assistant" },
    pt: { btn: "Dúvidas? Assistente de IA", title: "Assistente de IA · HDA Productions", close: "Fechar o assistente",
          note: "Respostas geradas por IA, confira-as. Não compartilhe dados sensíveis.", privacy: "Privacidade", href: "/pt/contato.html#assistant" },
    es: { btn: "¿Preguntas? Asistente de IA", title: "Asistente de IA · HDA Productions", close: "Cerrar el asistente",
          note: "Respuestas generadas por IA, compruébelas. No comparta datos sensibles.", privacy: "Privacidad", href: "/es/contacto.html#assistant" }
  };
  var T = I18N[LANG] || I18N.fr;

  function el(tag, attrs, html) {
    var e = document.createElement(tag);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (html) e.innerHTML = html;
    return e;
  }

  function init() {
    if (!SRC) return;
    var btn = el("button", { type: "button", "class": "hda-chat-btn", "aria-expanded": "false", "aria-controls": "hda-chat-panel" },
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg><span>' + T.btn + '</span>');
    var panel = el("div", { id: "hda-chat-panel", "class": "hda-chat-panel", role: "dialog", "aria-label": T.title, hidden: "" });
    var head = el("div", { "class": "hda-chat-head" }, "<span>" + T.title + "</span>");
    var close = el("button", { type: "button", "class": "hda-chat-close", "aria-label": T.close }, "×");
    head.appendChild(close);
    var note = el("p", { "class": "hda-chat-note" },
      T.note + ' <a href="' + T.href + '">' + T.privacy + '</a>');
    panel.appendChild(head);
    panel.appendChild(note);
    document.body.appendChild(btn);
    document.body.appendChild(panel);

    var frame = null;
    function open() {
      if (!frame) {
        frame = el("iframe", { "class": "hda-chat-frame", src: SRC, title: T.title, allow: "clipboard-write" });
        panel.insertBefore(frame, note);
      }
      panel.hidden = false;
      btn.setAttribute("aria-expanded", "true");
      close.focus();
    }
    function hide() {
      panel.hidden = true;
      btn.setAttribute("aria-expanded", "false");
      btn.focus();
    }
    btn.addEventListener("click", open);
    close.addEventListener("click", hide);
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && !panel.hidden) hide();
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
