/* Project request page: validation, Turnstile and submission. */
(function () {
  "use strict";

  var LANG = (document.documentElement.lang || "fr").slice(0, 2).toLowerCase();
  var MAIL = '<a href="mailto:h@hdaprodz.com?subject=Projet%20musical%20HDA%20Productions">h@hdaprodz.com</a>';
  var I18N = {
    fr: {
      ok: "Merci, votre demande a bien été envoyée. Référence : <strong>{ref}</strong>. Vous recevrez une réponse par e-mail.",
      validation: "Certains champs sont à compléter ou à corriger.",
      captcha: "La vérification anti-robot a échoué. Merci de réessayer.",
      timing: "Le formulaire a été envoyé trop vite ou a expiré. Rechargez la page et réessayez.",
      unavailable: "Le formulaire n’est pas disponible pour le moment.",
      generic: "L’envoi n’a pas abouti. Réessayez dans quelques minutes.",
      wait: "Merci de patienter pendant la vérification anti-robot, puis réessayez.",
      sending: "Envoi en cours…", submit: "Envoyer ma demande ↗",
      fallback: " Vous pouvez aussi écrire à " + MAIL + ".",
      fields: {
        name: "Indiquez votre nom (2 caractères minimum).",
        email: "Indiquez une adresse e-mail valide.",
        phone: "Ce numéro ne semble pas valide.",
        projectType: "Choisissez un type de projet.",
        description: "Décrivez votre projet en quelques phrases (20 caractères minimum).",
        timeline: "Choisissez un délai dans la liste.",
        budget: "Choisissez un budget dans la liste.",
        consent: "Cochez cette case pour que nous puissions traiter votre demande."
      },
      turnstile: "fr"
    },
    en: {
      ok: "Thank you, your request has been sent. Reference: <strong>{ref}</strong>. You will receive a reply by e-mail.",
      validation: "Some fields need to be completed or corrected.",
      captcha: "The anti-bot check failed. Please try again.",
      timing: "The form was sent too quickly or has expired. Reload the page and try again.",
      unavailable: "The form is not available at the moment.",
      generic: "Your request could not be sent. Please try again in a few minutes.",
      wait: "Please wait for the anti-bot check to finish, then try again.",
      sending: "Sending…", submit: "Send my request ↗",
      fallback: " You can also write to " + MAIL + ".",
      fields: {
        name: "Enter your name (at least 2 characters).",
        email: "Enter a valid e-mail address.",
        phone: "This number doesn’t look valid.",
        projectType: "Choose a project type.",
        description: "Describe your project in a few sentences (at least 20 characters).",
        timeline: "Choose a timeframe from the list.",
        budget: "Choose a budget from the list.",
        consent: "Tick this box so we can process your request."
      },
      turnstile: "en"
    },
    pt: {
      ok: "Obrigado, sua solicitação foi enviada. Referência: <strong>{ref}</strong>. Você receberá uma resposta por e-mail.",
      validation: "Alguns campos precisam ser preenchidos ou corrigidos.",
      captcha: "A verificação anti-robô falhou. Tente novamente.",
      timing: "O formulário foi enviado rápido demais ou expirou. Recarregue a página e tente novamente.",
      unavailable: "O formulário não está disponível no momento.",
      generic: "Não foi possível enviar. Tente novamente em alguns minutos.",
      wait: "Aguarde a verificação anti-robô terminar e tente novamente.",
      sending: "Enviando…", submit: "Enviar minha solicitação ↗",
      fallback: " Você também pode escrever para " + MAIL + ".",
      fields: {
        name: "Informe seu nome (mínimo de 2 caracteres).",
        email: "Informe um endereço de e-mail válido.",
        phone: "Este número não parece válido.",
        projectType: "Escolha um tipo de projeto.",
        description: "Descreva seu projeto em algumas frases (mínimo de 20 caracteres).",
        timeline: "Escolha um prazo da lista.",
        budget: "Escolha um orçamento da lista.",
        consent: "Marque esta caixa para que possamos tratar sua solicitação."
      },
      turnstile: "pt-br"
    },
    es: {
      ok: "Gracias, su solicitud se ha enviado. Referencia: <strong>{ref}</strong>. Recibirá una respuesta por correo electrónico.",
      validation: "Algunos campos deben completarse o corregirse.",
      captcha: "La verificación antirrobot ha fallado. Inténtelo de nuevo.",
      timing: "El formulario se envió demasiado rápido o ha caducado. Recargue la página e inténtelo de nuevo.",
      unavailable: "El formulario no está disponible en este momento.",
      generic: "No se ha podido enviar. Inténtelo de nuevo en unos minutos.",
      wait: "Espere a que termine la verificación antirrobot e inténtelo de nuevo.",
      sending: "Enviando…", submit: "Enviar mi solicitud ↗",
      fallback: " También puede escribir a " + MAIL + ".",
      fields: {
        name: "Indique su nombre (mínimo 2 caracteres).",
        email: "Indique una dirección de correo electrónico válida.",
        phone: "Este número no parece válido.",
        projectType: "Elija un tipo de proyecto.",
        description: "Describa su proyecto en unas frases (mínimo 20 caracteres).",
        timeline: "Elija un plazo de la lista.",
        budget: "Elija un presupuesto de la lista.",
        consent: "Marque esta casilla para que podamos tramitar su solicitud."
      },
      turnstile: "es"
    }
  };
  var T = I18N[LANG] || I18N.fr;
  var MESSAGES = {
    ok: function (ref) { return T.ok.replace("{ref}", ref); },
    validation: T.validation, captcha: T.captcha, timing: T.timing,
    unavailable: T.unavailable, generic: T.generic
  };
  var FALLBACK = T.fallback;
  var FIELD_ERRORS = T.fields;

  var form, statusBox, submitBtn, widgetId = null, token = "";

  function $(sel, root) { return (root || document).querySelector(sel); }

  function showStatus(kind, html) {
    statusBox.className = "p-status " + kind;
    statusBox.innerHTML = html;
    statusBox.hidden = false;
    statusBox.focus();
  }

  function clearErrors() {
    form.querySelectorAll(".p-error").forEach(function (el) { el.remove(); });
    form.querySelectorAll("[aria-invalid]").forEach(function (el) { el.removeAttribute("aria-invalid"); el.removeAttribute("aria-describedby"); });
  }

  function markError(name) {
    var field = form.elements[name];
    if (!field || !FIELD_ERRORS[name]) return;
    var id = "err-" + name;
    var msg = document.createElement("span");
    msg.className = "p-error";
    msg.id = id;
    msg.textContent = FIELD_ERRORS[name];
    field.setAttribute("aria-invalid", "true");
    field.setAttribute("aria-describedby", id);
    var label = field.closest("label");
    if (name === "consent") label.insertAdjacentElement("afterend", msg);
    else label.appendChild(msg);
  }

  function localErrors() {
    var errs = [];
    ["name", "email", "phone", "projectType", "description"].forEach(function (n) {
      var f = form.elements[n];
      f.value = f.value.trim();
      if (!f.checkValidity()) errs.push(n);
    });
    if (!form.elements.consent.checked) errs.push("consent");
    return errs;
  }

  function resetTurnstile() {
    token = "";
    if (window.turnstile && widgetId !== null) window.turnstile.reset(widgetId);
  }

  function loadTurnstile(sitekey) {
    window.onHdaTurnstile = function () {
      widgetId = window.turnstile.render("#turnstile", {
        sitekey: sitekey,
        language: T.turnstile,
        theme: "dark",
        callback: function (t) { token = t; },
        "expired-callback": function () { token = ""; },
        "error-callback": function () { token = ""; }
      });
    };
    var s = document.createElement("script");
    s.src = "https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit&onload=onHdaTurnstile";
    s.async = true;
    s.defer = true;
    document.head.appendChild(s);
  }

  function init() {
    form = $("#formulaire");
    statusBox = $("#status");
    submitBtn = $("#submit");
    form.elements.started.value = String(Date.now());

    var desc = form.elements.description, count = $("#count");
    desc.addEventListener("input", function () { count.textContent = desc.value.length; });

    // Result of a plain (no-JS) post, if any.
    var q = new URLSearchParams(location.search);
    if (q.get("statut") === "ok" && q.get("ref")) showStatus("ok", MESSAGES.ok(q.get("ref").replace(/[^A-Z0-9-]/gi, "")));
    else if (q.get("statut") === "erreur") showStatus("err", MESSAGES.generic + FALLBACK);

    fetch("/api/config", { headers: { Accept: "application/json" } })
      .then(function (r) { if (!r.ok) throw new Error(); return r.json(); })
      .then(function (cfg) {
        if (!cfg.turnstileSitekey) throw new Error();
        loadTurnstile(cfg.turnstileSitekey);
      })
      .catch(function () {
        submitBtn.disabled = true;
        showStatus("err", MESSAGES.unavailable + FALLBACK);
      });

    form.addEventListener("submit", onSubmit);
  }

  function onSubmit(e) {
    e.preventDefault();
    clearErrors();
    var errs = localErrors();
    if (errs.length) {
      errs.forEach(markError);
      showStatus("err", MESSAGES.validation);
      return;
    }
    if (!token) {
      showStatus("err", T.wait);
      return;
    }

    var data = {};
    new FormData(form).forEach(function (v, k) { data[k] = v; });
    data.consent = form.elements.consent.checked;
    data["cf-turnstile-response"] = token;

    submitBtn.disabled = true;
    submitBtn.textContent = T.sending;

    fetch("/api/contact", {
      method: "POST",
      headers: { "Content-Type": "application/json", Accept: "application/json" },
      body: JSON.stringify(data)
    })
      .then(function (r) { return r.json().catch(function () { return { ok: false, code: "send" }; }); })
      .then(function (res) {
        if (res.ok) {
          form.reset();
          $("#count").textContent = "0";
          form.querySelectorAll("fieldset, .p-consent, .p-turnstile, .p-actions").forEach(function (el) { el.hidden = true; });
          showStatus("ok", MESSAGES.ok(String(res.ref || "").replace(/[^A-Z0-9-]/gi, "")));
          return;
        }
        if (res.code === "validation" && res.fields) res.fields.forEach(markError);
        var msg = MESSAGES[res.code] || MESSAGES.generic;
        showStatus("err", msg + (res.code === "validation" ? "" : FALLBACK));
        resetTurnstile();
      })
      .catch(function () {
        showStatus("err", MESSAGES.generic + FALLBACK);
        resetTurnstile();
      })
      .finally(function () {
        submitBtn.disabled = false;
        submitBtn.textContent = T.submit;
      });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
