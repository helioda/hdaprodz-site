/* Project request page: validation, Turnstile and submission. */
(function () {
  "use strict";

  var MESSAGES = {
    ok: function (ref) {
      return "Merci, votre demande a bien été envoyée. Référence : <strong>" + ref + "</strong>. Vous recevrez une réponse par e-mail.";
    },
    validation: "Certains champs sont à compléter ou à corriger.",
    captcha: "La vérification anti-robot a échoué. Merci de réessayer.",
    timing: "Le formulaire a été envoyé trop vite ou a expiré. Rechargez la page et réessayez.",
    unavailable: "Le formulaire n’est pas disponible pour le moment.",
    generic: "L’envoi n’a pas abouti. Réessayez dans quelques minutes."
  };
  var FALLBACK = ' Vous pouvez aussi écrire à <a href="mailto:h@hdaprodz.com?subject=Projet%20HDA%20Solutions">h@hdaprodz.com</a>.';
  var FIELD_ERRORS = {
    name: "Indiquez votre nom (2 caractères minimum).",
    email: "Indiquez une adresse e-mail valide.",
    phone: "Ce numéro ne semble pas valide.",
    projectType: "Choisissez un type de projet.",
    description: "Décrivez votre projet en quelques phrases (20 caractères minimum).",
    timeline: "Choisissez un délai dans la liste.",
    budget: "Choisissez un budget dans la liste.",
    consent: "Cochez cette case pour que nous puissions traiter votre demande."
  };

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
        language: "fr",
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
      showStatus("err", "Merci de patienter pendant la vérification anti-robot, puis réessayez.");
      return;
    }

    var data = {};
    new FormData(form).forEach(function (v, k) { data[k] = v; });
    data.consent = form.elements.consent.checked;
    data["cf-turnstile-response"] = token;

    submitBtn.disabled = true;
    submitBtn.textContent = "Envoi en cours…";

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
        submitBtn.textContent = "Envoyer ma demande ↗";
      });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
