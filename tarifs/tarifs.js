/* CoproSens price estimator. Prices are set in euros (VAT not applicable, art. 293 B CGI) and shown
   in the visitor's currency through an indicative conversion at a fixed ECB reference rate.
   Texts: French below (FR). Translated pages load /tarifs/l10n.js first, which sets
   window.PRICING_L10N with the same keys; figures never depend on the language. */
(function () {
  "use strict";
  var DAY = 550, PILOT = 2500, PILOT_FOUNDER = 1750, DASH = 750, LICENCE_MONTH = 7.8, FOUNDER_MAX = 32;
  var FR = {
    locale: "fr-FR",
    tiers: ["Petite copropriété (jusqu’à 32 lots)", "Copropriété moyenne (33 à 100 lots)", "Grande copropriété (101 à 200 lots)"],
    huge: "Très grande copropriété (plus de 200 lots) : devis personnalisé",
    quote: "Devis personnalisé",
    founder: " · offre clients fondateurs",
    included: "Inclus",
    notChosen: "Non retenu",
    notChosenF: "Non retenue",
    fx: "Conversion indicative de nos prix en euros, au cours de référence BCE du {date} (1 € = {rate}). Le devis écrit confirme le montant et la devise.",
    fxDate: "26/10/2026"
  };
  // ECB euro reference rates, 26 Oct 2026. Update by hand (and FX_DATE texts) when refreshing.
  var FX = { EUR: 1, USD: 1.1188, GBP: 0.8382, BRL: 6.2523, MXN: 20.8271, CAD: 1.5695, CHF: 0.9243 };
  // Rounding step for converted price points (whole amounts) per currency.
  var STEP = { EUR: 1, USD: 10, GBP: 10, BRL: 50, MXN: 100, CAD: 10, CHF: 10 };
  var REGION = { US: "USD", GB: "GBP", BR: "BRL", MX: "MXN", CA: "CAD", CH: "CHF" };
  // Eurozone (and euro-using microstates): euros on every language page.
  "AT BE BG HR CY EE FI FR DE GR IE IT LV LT LU MT NL PT SK SI ES AD MC SM VA ME XK".split(" ").forEach(function (c) { REGION[c] = "EUR"; });
  // Rest of Latin America: US dollars, the usual business reference currency there.
  "AR BO CL CO CR CU DO EC SV GT HN NI PA PY PE PR UY VE".split(" ").forEach(function (c) { REGION[c] = "USD"; });
  var PAGE_DEFAULT = { fr: "EUR", en: "USD", pt: "BRL", es: "EUR" };
  var S = FR, L = window.PRICING_L10N;
  if (L) { S = {}; Object.keys(FR).forEach(function (k) { S[k] = k in L ? L[k] : FR[k]; }); }
  // Tiers by number of main lots (housing, shops, offices).
  var TIERS = [
    { max: 32,  label: S.tiers[0], setup: 3 * DAY, maint: 175 },
    { max: 100, label: S.tiers[1], setup: 5 * DAY, maint: 350 },
    { max: 200, label: S.tiers[2], setup: 8 * DAY, maint: 550 }
  ];
  var $ = function (id) { return document.getElementById(id); };
  var cur = "EUR", fmt, fmt2;
  function setCur(c) {
    cur = FX[c] ? c : "EUR";
    fmt = new Intl.NumberFormat(S.locale, { style: "currency", currency: cur, currencyDisplay: "narrowSymbol", maximumFractionDigits: 0 });
    fmt2 = new Intl.NumberFormat(S.locale, { style: "currency", currency: cur, currencyDisplay: "narrowSymbol", minimumFractionDigits: 2, maximumFractionDigits: 2 });
    var usOutsideEn = cur === "USD" && S.locale.slice(0, 2) !== "en";
    if (cur === "MXN" || cur === "CAD" || usOutsideEn) { // "$" alone is ambiguous (pesos, CA$, US$)
      var pre = cur === "MXN" ? "MX$" : cur === "CAD" ? "CA$" : "US$";
      fmt = { format: (function (f) { return function (v) { return f.format(v).replace("$", pre); }; })(fmt) };
      fmt2 = { format: (function (f) { return function (v) { return f.format(v).replace("$", pre); }; })(fmt2) };
    }
  }
  // Convert a euro price point. Day-based amounts are converted per day, so "3 days" stays 3 x the day rate.
  function conv(eur) {
    if (cur === "EUR") return eur;
    var r = FX[cur], st = STEP[cur];
    if (eur < 50) return Math.round(eur * r * 100) / 100;
    if (eur !== DAY && eur % DAY === 0) return (eur / DAY) * conv(DAY);
    return Math.round(eur * r / st) * st;
  }
  function num(id, min, max) {
    var v = parseInt($(id).value, 10);
    if (isNaN(v)) v = min;
    return Math.min(max, Math.max(min, v));
  }
  function set(id, text) { $(id).textContent = text; }

  // Rate grid and hint: rewrite euro amounts found in text nodes (any locale format).
  var MONEY = /(€\u00a0?|€ )?(\d{1,3}(?:[ .,\u00a0\u202f]\d{3})+|\d+)(?:[.,](\d{2}))?(?:\u00a0?€| €)?/g;
  var gridNodes = [];
  (function collect() {
    var root = $("grid"); if (!root) return;
    var w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT), n;
    while ((n = w.nextNode())) if (n.nodeValue.indexOf("€") >= 0) gridNodes.push({ node: n, orig: n.nodeValue });
  })();
  function renderGrid() {
    gridNodes.forEach(function (g) {
      g.node.nodeValue = cur === "EUR" ? g.orig : g.orig.replace(MONEY, function (m, pre, int, dec) {
        if (m.indexOf("€") < 0) return m;
        var eur = parseInt(int.replace(/[^\d]/g, ""), 10) + (dec ? parseInt(dec, 10) / 100 : 0);
        var v = conv(eur);
        return (v % 1 ? fmt2 : fmt).format(v);
      });
    });
    var fx = $("k-fx");
    if (cur === "EUR") { fx.hidden = true; }
    else {
      fx.hidden = false;
      fx.textContent = S.fx.replace("{date}", S.fxDate).replace("{rate}", new Intl.NumberFormat(S.locale, { maximumFractionDigits: 4 }).format(FX[cur]) + " " + cur);
    }
  }

  function compute() {
    renderGrid();
    var lots = num("f-lots", 1, 2000), cs = num("f-cs", 1, 30), days = num("f-days", 0, 60);
    var founderOk = lots <= FOUNDER_MAX;
    var founderBox = $("f-founder");
    founderBox.disabled = !founderOk;
    if (!founderOk) founderBox.checked = false;
    $("founder-line").classList.toggle("disabled", !founderOk);
    var founder = founderBox.checked, dashOn = $("f-dash").checked || founder, maintOn = $("f-maint").checked;
    if (founder) $("f-dash").checked = true;

    var tier = null;
    for (var i = 0; i < TIERS.length; i++) { if (lots <= TIERS[i].max) { tier = TIERS[i]; break; } }
    var rows = ["k-pilot", "k-setup", "k-dash", "k-lic", "k-y1", "k-y1m", "k-y2m", "k-maint"];
    if (!tier) {
      set("k-tier", S.huge);
      rows.forEach(function (r) { set(r, S.quote); });
      $("k-quote").hidden = false;
      return;
    }
    $("k-quote").hidden = true;
    var pilot = conv(founder ? PILOT_FOUNDER : PILOT);
    var setup = conv(tier.setup) + days * conv(DAY);
    var dash = dashOn ? (founder ? 0 : conv(DASH)) : 0;
    var lic = Math.round(cs * conv(LICENCE_MONTH) * 12 * 100) / 100;
    var y1 = pilot + setup + dash + lic;
    set("k-tier", tier.label + (founder ? S.founder : ""));
    set("k-pilot", fmt.format(pilot));
    set("k-setup", fmt.format(setup));
    set("k-dash", dashOn ? (founder ? S.included : fmt.format(dash)) : S.notChosen);
    set("k-lic", fmt2.format(lic));
    set("k-y1", fmt2.format(y1));
    set("k-y1m", fmt2.format(y1 / lots / 12));
    set("k-y2m", fmt2.format(lic / lots / 12));
    set("k-maint", maintOn ? fmt.format(conv(tier.maint)) + " · " + fmt2.format(conv(tier.maint) / lots) : S.notChosenF);
    $("row-maint").classList.toggle("muted-row", !maintOn);
  }

  var pageLang = (document.documentElement.lang || "fr").slice(0, 2), saved = null;
  try { saved = localStorage.getItem("hda-cur"); } catch (e) {}
  var region = ((navigator.language || "").split("-")[1] || "").toUpperCase();
  var q0 = new URLSearchParams(location.search).get("cur");
  var start = (q0 && FX[q0.toUpperCase()] && q0.toUpperCase()) || (saved && FX[saved] && saved) || REGION[region] || PAGE_DEFAULT[pageLang] || "EUR";
  setCur(start); $("f-cur").value = cur;
  $("f-cur").addEventListener("change", function () {
    setCur(this.value);
    try { localStorage.setItem("hda-cur", cur); } catch (e) {}
    compute();
  });
  ["f-lots", "f-cs", "f-days", "f-dash", "f-maint", "f-founder"].forEach(function (id) {
    $(id).addEventListener("input", compute);
    $(id).addEventListener("change", compute);
  });
  $("k-print").addEventListener("click", function () { window.print(); });
  var q = new URLSearchParams(location.search);
  if (q.get("lots")) $("f-lots").value = q.get("lots");
  compute();
})();
