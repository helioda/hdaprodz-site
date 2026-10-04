// Website assistant: Copilot Studio web chat in a panel.
// The iframe is created only when the visitor opens the panel, so nothing is
// loaded from Microsoft (and no conversation or credit is used) before that.
(function () {
  var SRC = "https://copilotstudio.microsoft.com/environments/bb2bce61-d4d6-eef1-aecc-de974fa7f543/bots/cr371_AssistantHDASolutions/webchat?__version__=2";
  var PRIVACY = "projet.html#assistant";

  function el(tag, attrs, html) {
    var e = document.createElement(tag);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (html) e.innerHTML = html;
    return e;
  }

  function init() {
    var btn = el("button", { type: "button", "class": "hda-chat-btn", "aria-expanded": "false", "aria-controls": "hda-chat-panel" },
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg><span>Une question ? Assistant IA</span>');
    var panel = el("div", { id: "hda-chat-panel", "class": "hda-chat-panel", role: "dialog", "aria-label": "Assistant IA HDA Solutions", hidden: "" });
    var head = el("div", { "class": "hda-chat-head" }, "<span>Assistant IA · HDA Solutions</span>");
    var close = el("button", { type: "button", "class": "hda-chat-close", "aria-label": "Fermer l’assistant" }, "×");
    head.appendChild(close);
    var note = el("p", { "class": "hda-chat-note" },
      'Réponses générées par IA, à vérifier. Ne partagez pas de données sensibles. <a href="' + PRIVACY + '">Confidentialité</a>');
    panel.appendChild(head);
    panel.appendChild(note);
    document.body.appendChild(btn);
    document.body.appendChild(panel);

    var frame = null;
    function open() {
      if (!frame) {
        frame = el("iframe", { "class": "hda-chat-frame", src: SRC, title: "Assistant IA HDA Solutions", allow: "clipboard-write" });
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
