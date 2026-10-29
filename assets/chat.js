// Website assistant: Copilot Studio web chat in a panel.
// The iframe is created only when the visitor opens the panel, so nothing is
// loaded from Microsoft (and no conversation or credit is used) before that.
(function () {
  var SRC = "https://copilotstudio.microsoft.com/environments/bb2bce61-d4d6-eef1-aecc-de974fa7f543/bots/cr371_AssistantHDASolutions/webchat?__version__=2";
  var ENV = "https://bb2bce61d4d6eef1aeccde974fa7f5.43.environment.api.powerplatform.com/powervirtualagents/";
  var TOKEN = ENV + "botsbyschema/cr371_AssistantHDASolutions/directline/token?api-version=2022-03-01-preview";
  var REGION = ENV + "regionalchannelsettings?api-version=2022-03-01-preview";
  var WEBCHAT = "https://cdn.botframework.com/botframework-webchat/4.18.0/webchat.js";
  var LOCALES = { fr: "fr-FR", en: "en-US", pt: "pt-BR", es: "es-ES" };
  var LANG = (document.documentElement.lang || "fr").slice(0, 2).toLowerCase();
  var I18N = {
    fr: { btn: "Une question ? Assistant IA", title: "Assistant IA · HDA Solutions", close: "Fermer l’assistant",
          note: "Réponses générées par IA, à vérifier. Ne partagez pas de données sensibles.", privacy: "Confidentialité", href: "/projet.html#assistant" },
    en: { btn: "Questions? AI assistant", title: "AI assistant · HDA Solutions", close: "Close the assistant",
          note: "AI-generated answers, please check them. Don’t share sensitive data.", privacy: "Privacy", href: "/en/project.html#assistant" },
    pt: { btn: "Dúvidas? Assistente de IA", title: "Assistente de IA · HDA Solutions", close: "Fechar o assistente",
          note: "Respostas geradas por IA, confira-as. Não compartilhe dados sensíveis.", privacy: "Privacidade", href: "/pt/projeto.html#assistant" },
    es: { btn: "¿Preguntas? Asistente de IA", title: "Asistente de IA · HDA Solutions", close: "Cerrar el asistente",
          note: "Respuestas generadas por IA, compruébelas. No comparta datos sensibles.", privacy: "Privacidad", href: "/es/proyecto.html#assistant" }
  };
  var T = I18N[LANG] || I18N.fr;

  function el(tag, attrs, html) {
    var e = document.createElement(tag);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (html) e.innerHTML = html;
    return e;
  }

  function init() {
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
    // Icon only while the hero is visible; full label once the visitor scrolls past it.
    var hero = document.querySelector(".hero");
    if (hero && "IntersectionObserver" in window) {
      btn.setAttribute("title", T.btn);
      new IntersectionObserver(function (es) {
        btn.classList.toggle("is-compact", es[0].isIntersecting);
      }, { threshold: 0.25 }).observe(hero);
    }
    document.body.appendChild(panel);

    var frame = null;
    // Web Chat in the page language; the hosted iframe ignores the locale,
    // so it is only the fallback if the script or the token fails.
    function fallback() {
      if (frame) frame.remove();
      frame = el("iframe", { "class": "hda-chat-frame", src: SRC, title: T.title, allow: "clipboard-write" });
      panel.insertBefore(frame, note);
    }
    function loadScript(src) {
      return new Promise(function (ok, ko) {
        if (window.WebChat) return ok();
        var s = el("script", { src: src, crossorigin: "anonymous" });
        s.onload = ok; s.onerror = ko; document.head.appendChild(s);
      });
    }
    function start() {
      var locale = LOCALES[LANG] || "fr-FR";
      frame = el("div", { "class": "hda-chat-frame hda-chat-live", role: "region", "aria-label": T.title });
      panel.insertBefore(frame, note);
      Promise.all([
        loadScript(WEBCHAT),
        fetch(TOKEN).then(function (r) { if (!r.ok) throw r; return r.json(); }),
        fetch(REGION).then(function (r) { return r.ok ? r.json() : {}; }).catch(function () { return {}; })
      ]).then(function (res) {
        var dl = res[2] && res[2].channelUrlsById && res[2].channelUrlsById.directline;
        var opts = { token: res[1].token };
        if (dl) opts.domain = new URL("v3/directline", dl).toString();
        var store = window.WebChat.createStore({}, function (api) {
          return function (next) { return function (action) {
            if (action.type === "DIRECT_LINE/CONNECT_FULFILLED") {
              api.dispatch({ type: "DIRECT_LINE/POST_ACTIVITY", meta: { method: "keyboard" },
                payload: { activity: { type: "event", name: "startConversation", locale: locale, channelData: { postBack: true } } } });
            }
            return next(action);
          }; };
        });
        window.WebChat.renderWebChat({
          directLine: window.WebChat.createDirectLine(opts), store: store, locale: locale,
          styleOptions: { hideUploadButton: true, backgroundColor: "#ffffff", accent: "#0e8a94",
            bubbleBorderRadius: 10, bubbleFromUserBorderRadius: 10, bubbleFromUserBackground: "#e6f7f8",
            primaryFont: "Arial, Helvetica, sans-serif" }
        }, frame);
      }).catch(fallback);
    }
    function open() {
      if (!frame) start();
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
