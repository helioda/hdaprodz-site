/* CoproSens price estimator. All figures in euros, VAT not applicable (art. 293 B CGI).
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
    notChosenF: "Non retenue"
  };
  var S = FR, L = window.PRICING_L10N;
  if (L) { S = {}; Object.keys(FR).forEach(function (k) { S[k] = k in L ? L[k] : FR[k]; }); }
  // Tiers by number of main lots (housing, shops, offices).
  var TIERS = [
    { max: 32,  label: S.tiers[0], setup: 3 * DAY, maint: 175 },
    { max: 100, label: S.tiers[1], setup: 5 * DAY, maint: 350 },
    { max: 200, label: S.tiers[2], setup: 8 * DAY, maint: 550 }
  ];
  var $ = function (id) { return document.getElementById(id); };
  var fmt = new Intl.NumberFormat(S.locale, { style: "currency", currency: "EUR", maximumFractionDigits: 0 });
  var fmt2 = new Intl.NumberFormat(S.locale, { style: "currency", currency: "EUR", minimumFractionDigits: 2, maximumFractionDigits: 2 });
  function num(id, min, max) {
    var v = parseInt($(id).value, 10);
    if (isNaN(v)) v = min;
    return Math.min(max, Math.max(min, v));
  }
  function set(id, text) { $(id).textContent = text; }

  function compute() {
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
    var pilot = founder ? PILOT_FOUNDER : PILOT;
    var setup = tier.setup + days * DAY;
    var dash = dashOn ? (founder ? 0 : DASH) : 0;
    var lic = cs * LICENCE_MONTH * 12;
    var y1 = pilot + setup + dash + lic;
    set("k-tier", tier.label + (founder ? S.founder : ""));
    set("k-pilot", fmt.format(pilot));
    set("k-setup", fmt.format(setup));
    set("k-dash", dashOn ? (founder ? S.included : fmt.format(DASH)) : S.notChosen);
    set("k-lic", fmt2.format(lic));
    set("k-y1", fmt2.format(y1));
    set("k-y1m", fmt2.format(y1 / lots / 12));
    set("k-y2m", fmt2.format(lic / lots / 12));
    set("k-maint", maintOn ? fmt.format(tier.maint) + " · " + fmt2.format(tier.maint / lots) : S.notChosenF);
    $("row-maint").classList.toggle("muted-row", !maintOn);
  }

  ["f-lots", "f-cs", "f-days", "f-dash", "f-maint", "f-founder"].forEach(function (id) {
    $(id).addEventListener("input", compute);
    $(id).addEventListener("change", compute);
  });
  $("k-print").addEventListener("click", function () { window.print(); });
  var q = new URLSearchParams(location.search);
  if (q.get("lots")) $("f-lots").value = q.get("lots");
  compute();
})();
