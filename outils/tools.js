/* CoproSens — outils du syndic (démonstration).
   1. Répartition et appels de fonds (tantièmes, charges spéciales, consommations individuelles)
   2. Documents d'AG : ordre du jour, convocation, formulaire de vote, projet de procès-verbal
   All calculations are deterministic (no AI): exact to the cent, totals always balance. */
(function () {
  "use strict";
  var C = window.COPRO, lots = C.lots;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var eur = new Intl.NumberFormat("fr-FR", { style: "currency", currency: "EUR" });
  var num = new Intl.NumberFormat("fr-FR");
  var esc = function (s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); };
  var fmtDate = function (d) { return d ? new Date(d + "T12:00:00").toLocaleDateString("fr-FR", { weekday: "long", day: "numeric", month: "long", year: "numeric" }) : "…"; };

  /* ---------- Tabs ---------- */
  $$(".tab").forEach(function (b) {
    b.addEventListener("click", function () {
      $$(".tab").forEach(function (x) { x.setAttribute("aria-selected", x === b ? "true" : "false"); });
      $$(".panel").forEach(function (p) { p.hidden = p.id !== b.getAttribute("aria-controls"); });
    });
  });

  /* ---------- Exact split: largest-remainder rounding to the cent ---------- */
  function split(totalEuros, weights) {
    var cents = Math.round(totalEuros * 100), sum = weights.reduce(function (a, b) { return a + b; }, 0);
    if (!sum) return weights.map(function () { return 0; });
    var raw = weights.map(function (w) { return cents * w / sum; });
    var floor = raw.map(Math.floor), rest = cents - floor.reduce(function (a, b) { return a + b; }, 0);
    raw.map(function (r, i) { return [r - floor[i], i]; }).sort(function (a, b) { return b[0] - a[0] || a[1] - b[1]; })
      .slice(0, rest).forEach(function (x) { floor[x[1]]++; });
    return floor.map(function (c) { return c / 100; });
  }

  /* ---------- 1. Appels de fonds ---------- */
  var B = C.budget;
  $("#b-gen").value = B.generales; $("#b-asc").value = B.ascenseur; $("#b-eau").value = B.eau; $("#b-ch").value = B.chauffage;
  $("#p-ft").value = C.fondsTravauxPct; $("#p-ch").value = C.chauffageConsoPct;

  var lastRows = [];
  function compute() {
    var g = +$("#b-gen").value || 0, a = +$("#b-asc").value || 0, e = +$("#b-eau").value || 0, h = +$("#b-ch").value || 0;
    var ftPct = +$("#p-ft").value || 0, chPct = Math.min(100, Math.max(0, +$("#p-ch").value || 0));
    var budget = g + a + e + h, ft = Math.round(budget * ftPct) / 100;
    var tant = lots.map(function (l) { return l.tantiemes; });
    var sGen = split(g, tant);
    var simple = $("#m-simple").checked;
    $("#p-ch").disabled = simple;
    var sAsc = simple ? split(a, tant) : split(a, lots.map(function (l) { return l.etage > 0 ? l.tantiemes : 0; }));
    var sEau = simple ? split(e, tant) : split(e, lots.map(function (l) { return l.eau; }));
    var hConso = simple ? 0 : Math.round(h * chPct) / 100, hFixe = Math.round((h - hConso) * 100) / 100;
    var sChC = simple ? lots.map(function () { return 0; }) : split(hConso, lots.map(function (l) { return l.chauffage; })), sChF = split(hFixe, tant);
    var sFt = split(ft, tant);
    lastRows = lots.map(function (l, i) {
      var annual = sGen[i] + sAsc[i] + sEau[i] + sChC[i] + sChF[i] + sFt[i];
      return { l: l, gen: sGen[i], asc: sAsc[i], eau: sEau[i], ch: sChC[i] + sChF[i], ft: sFt[i], an: annual };
    });
    var q = split(budget + ft, lastRows.map(function (r) { return r.an; }));
    lastRows.forEach(function (r, i) { r.an = q[i]; r.tri = Math.round(q[i] / 4 * 100) / 100; });

    var tot = function (k) { return lastRows.reduce(function (s, r) { return s + Math.round(r[k] * 100); }, 0) / 100; };
    $("#k-budget").textContent = eur.format(budget);
    $("#k-ft").textContent = eur.format(ft);
    $("#k-total").textContent = eur.format(budget + ft);
    $("#k-check").textContent = Math.abs(tot("an") - (budget + ft)) < 0.005 ? "Totaux équilibrés au centime ✓" : "Écart de " + eur.format(tot("an") - (budget + ft));

    $("#calc-body").innerHTML = lastRows.map(function (r) {
      return "<tr><th scope='row'>" + r.l.label + "<small>" + r.l.type + (r.l.etage ? " · étage " + r.l.etage : " · RDC") + "</small></th><td>" + r.l.tantiemes +
        "</td><td>" + eur.format(r.gen) + "</td><td>" + eur.format(r.asc) + "</td><td>" + eur.format(r.eau) + "<small>" + r.l.eau + " m³</small></td><td>" +
        eur.format(r.ch) + "<small>" + num.format(r.l.chauffage) + " unités</small></td><td>" + eur.format(r.ft) + "</td><td class='strong'>" + eur.format(r.an) + "</td><td class='strong accent'>" + eur.format(r.tri) + "</td></tr>";
    }).join("");
    $("#calc-foot").innerHTML = "<tr><th>Total</th><td>" + num.format(C.totalTantiemes) + "</td><td>" + eur.format(tot("gen")) + "</td><td>" + eur.format(tot("asc")) +
      "</td><td>" + eur.format(tot("eau")) + "</td><td>" + eur.format(tot("ch")) + "</td><td>" + eur.format(tot("ft")) + "</td><td>" + eur.format(tot("an")) + "</td><td>" + eur.format(tot("tri")) + "</td></tr>";
  }
  $$("#calc-form input").forEach(function (i) { i.addEventListener("input", compute); });
  compute();

  function download(name, mime, content) {
    var a = document.createElement("a");
    a.href = URL.createObjectURL(new Blob([content], { type: mime }));
    a.download = name; document.body.appendChild(a); a.click();
    setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 500);
  }
  $("#calc-csv").addEventListener("click", function () {
    var head = ["Lot", "Type", "Étage", "Tantièmes", "Charges générales", "Ascenseur", "Eau (m³)", "Eau (€)", "Chauffage (unités)", "Chauffage (€)", "Fonds de travaux", "Total annuel", "Appel trimestriel"];
    var f = function (x) { return x.toFixed(2).replace(".", ","); };
    var rows = lastRows.map(function (r) { return [r.l.label, r.l.type, r.l.etage, r.l.tantiemes, f(r.gen), f(r.asc), r.l.eau, f(r.eau), r.l.chauffage, f(r.ch), f(r.ft), f(r.an), f(r.tri)].join(";"); });
    download("appels-de-fonds-clos-des-mesanges.csv", "text/csv;charset=utf-8", "﻿" + head.join(";") + "\n" + rows.join("\n"));
  });
  $("#calc-print").addEventListener("click", function () { window.print(); });

  /* ---------- 2. Documents d'AG ---------- */
  var MAJ = {
    "24": "Article 24 : majorité des voix exprimées des copropriétaires présents, représentés ou ayant voté par correspondance",
    "25": "Article 25 : majorité des voix de tous les copropriétaires",
    "26": "Article 26 : majorité des membres du syndicat représentant au moins les deux tiers des voix"
  };
  var resolutions = [
    { t: "Élection du président de séance", m: "24" },
    { t: "Élection du secrétaire de séance", m: "24" },
    { t: "Élection du ou des scrutateurs", m: "24" },
    { t: "Approbation des comptes de l’exercice 2026", m: "24" },
    { t: "Quitus au syndic pour sa gestion de l’exercice 2026", m: "24" },
    { t: "Vote du budget prévisionnel de l’exercice 2027 (156 500 €)", m: "24" },
    { t: "Montant de la cotisation annuelle au fonds de travaux (5 % du budget prévisionnel)", m: "25" },
    { t: "Travaux de réfection de l’étanchéité de la toiture-terrasse : choix de l’entreprise sur la base de deux devis", m: "24" },
    { t: "Désignation du syndic et approbation de son contrat", m: "25" }
  ];
  var votes = {}; // index -> { contre:[lotIds], abst:[lotIds] }
  var absents = [11, 27, 33, 40];
  var today = new Date(); today.setHours(12);
  var iso = function (d) { return d.toISOString().slice(0, 10); };
  var ag = new Date(today); ag.setDate(ag.getDate() + 35);
  $("#ag-date").value = iso(ag); $("#ag-envoi").value = iso(today);
  $("#ag-heure").value = "18:30"; $("#ag-lieu").value = "Salle polyvalente, 12 allée des Mésanges, Massy (adresse fictive)";
  $("#ag-visio").checked = true;

  function renderResolutions() {
    $("#res-list").innerHTML = resolutions.map(function (r, i) {
      return "<li><input aria-label='Intitulé de la résolution " + (i + 1) + "' data-i='" + i + "' class='res-t' value=\"" + esc(r.t) + "\"><select aria-label='Majorité' data-i='" + i + "' class='res-m'>" +
        ["24", "25", "26"].map(function (m) { return "<option value='" + m + "'" + (r.m === m ? " selected" : "") + ">Art. " + m + "</option>"; }).join("") +
        "</select><button type='button' class='mini' data-del='" + i + "' aria-label='Supprimer'>✕</button></li>";
    }).join("");
    $$(".res-t").forEach(function (x) { x.addEventListener("input", function () { resolutions[+x.dataset.i].t = x.value; refresh(); }); });
    $$(".res-m").forEach(function (x) { x.addEventListener("change", function () { resolutions[+x.dataset.i].m = x.value; refresh(); }); });
    $$("[data-del]").forEach(function (x) { x.addEventListener("click", function () { resolutions.splice(+x.dataset.del, 1); votes = {}; renderResolutions(); refresh(); }); });
  }
  $("#res-add").addEventListener("click", function () { resolutions.push({ t: "Nouvelle résolution", m: "24" }); renderResolutions(); refresh(); });
  ["#ag-date", "#ag-envoi", "#ag-heure", "#ag-lieu", "#ag-visio"].forEach(function (s) { $(s).addEventListener("input", refresh); });

  // Default demo votes so the PV is meaningful
  function demoVotes() {
    votes = {};
    resolutions.forEach(function (r, i) {
      var c = [], a = [];
      if (/Quitus/.test(r.t)) { c = [7, 19]; a = [24]; }
      if (/étanchéité/.test(r.t)) { c = [3, 9, 15, 21]; a = [2, 30]; }
      if (/fonds de travaux/.test(r.t)) { c = [5, 25]; }
      if (/syndic et approbation/.test(r.t)) { c = [8, 14, 36]; a = [1]; }
      votes[i] = { contre: c, abst: a };
    });
  }
  demoVotes();

  function tally(i) {
    var v = votes[i] || { contre: [], abst: [] }, sum = function (ids) { return ids.reduce(function (s, id) { return s + lots[id - 1].tantiemes; }, 0); };
    var presentIds = lots.map(function (l) { return l.id; }).filter(function (id) { return absents.indexOf(id) < 0; });
    var contre = v.contre.filter(function (id) { return presentIds.indexOf(id) >= 0; }), abst = v.abst.filter(function (id) { return presentIds.indexOf(id) >= 0 && contre.indexOf(id) < 0; });
    var pour = presentIds.filter(function (id) { return contre.indexOf(id) < 0 && abst.indexOf(id) < 0; });
    return { pour: pour, contre: contre, abst: abst, vPour: sum(pour), vContre: sum(contre), vAbst: sum(abst), vAbs: sum(absents), nbMembres: lots.length };
  }
  function decide(r, x) {
    var T = C.totalTantiemes;
    if (r.m === "24") return x.vPour > x.vContre ? ["Adoptée", "art. 24"] : ["Rejetée", "art. 24"];
    if (r.m === "25") {
      if (x.vPour > T / 2) return ["Adoptée", "art. 25"];
      if (x.vPour * 3 >= T) return [x.vPour > x.vContre ? "Adoptée au second vote" : "Rejetée au second vote", "art. 25 non atteint, au moins un tiers des voix : second vote immédiat à l’art. 24 (art. 25-1)"];
      return ["Rejetée", "art. 25"];
    }
    var ok = x.pour.length > x.nbMembres / 2 && x.vPour * 3 >= T * 2;
    return ok ? ["Adoptée", "art. 26"] : ["Rejetée", "art. 26 (vérifier la passerelle de l’art. 26-1)"];
  }

  function renderVotes() {
    $("#vote-list").innerHTML = resolutions.map(function (r, i) {
      var x = tally(i), d = decide(r, x), v = votes[i] || { contre: [], abst: [] };
      return "<details class='vote'><summary><span>" + (i + 1) + ". " + esc(r.t) + "</span><b class='" + (/Adoptée/.test(d[0]) ? "ok" : "ko") + "'>" + d[0] + "</b></summary>" +
        "<p class='hint'>Pour " + num.format(x.vPour) + " · Contre " + num.format(x.vContre) + " · Abstention " + num.format(x.vAbst) + " (en tantièmes). " + esc(d[1]) + ".</p>" +
        "<label>Lots votant contre <input data-k='contre' data-i='" + i + "' class='vote-in' value='" + v.contre.join(", ") + "' placeholder='ex. 3, 9, 15'></label>" +
        "<label>Lots s’abstenant <input data-k='abst' data-i='" + i + "' class='vote-in' value='" + v.abst.join(", ") + "' placeholder='ex. 2'></label></details>";
    }).join("");
    $$(".vote-in").forEach(function (x) {
      x.addEventListener("change", function () {
        var ids = x.value.split(/[^0-9]+/).map(Number).filter(function (n) { return n >= 1 && n <= lots.length; });
        votes[+x.dataset.i] = votes[+x.dataset.i] || { contre: [], abst: [] }; votes[+x.dataset.i][x.dataset.k] = ids; refresh();
      });
    });
  }
  $("#ag-absents").value = absents.join(", ");
  $("#ag-absents").addEventListener("change", function () {
    absents = $("#ag-absents").value.split(/[^0-9]+/).map(Number).filter(function (n) { return n >= 1 && n <= lots.length; }); refresh();
  });

  function docOrdre() {
    return "<h2>Ordre du jour</h2><p>Assemblée générale ordinaire du syndicat des copropriétaires de la " + C.nom + "</p><ol>" +
      resolutions.map(function (r) { return "<li>" + esc(r.t) + " <em>(" + MAJ[r.m].split(" :")[0] + ")</em></li>"; }).join("") + "</ol>";
  }
  function docConvocation() {
    var envoi = $("#ag-envoi").value, date = $("#ag-date").value;
    var delai = envoi && date ? Math.round((new Date(date) - new Date(envoi)) / 864e5) : 0;
    var warn = delai < 21 ? "<p class='warn'>⚠ Délai insuffisant : " + delai + " jours entre l’envoi et l’assemblée. La convocation doit être notifiée au moins 21 jours avant l’assemblée.</p>" : "";
    return warn + "<p class='right'>" + C.syndic + "<br>Massy, le " + fmtDate(envoi) + "</p>" +
      "<p><b>Objet : convocation à l’assemblée générale ordinaire</b><br>Syndicat des copropriétaires de la " + C.nom + ", " + C.adresse + "</p>" +
      "<p>Madame, Monsieur,</p><p>Vous êtes convoqué(e) à l’assemblée générale ordinaire des copropriétaires qui se tiendra le <b>" + fmtDate(date) + " à " + esc($("#ag-heure").value) + "</b>, " + esc($("#ag-lieu").value) + ".</p>" +
      ($("#ag-visio").checked ? "<p>Vous pourrez également participer par visioconférence ; les modalités de connexion vous seront communiquées avec la présente convocation.</p>" : "") +
      "<p>L’assemblée délibérera sur l’ordre du jour suivant ; les projets de résolution et la majorité requise pour chacune figurent ci-dessous.</p><ol>" +
      resolutions.map(function (r) { return "<li><b>" + esc(r.t) + "</b><br><small>Majorité requise : " + MAJ[r.m] + ".</small></li>"; }).join("") + "</ol>" +
      "<p>Vous pouvez voter par correspondance à l’aide du formulaire joint, à retourner au syndic au moins trois jours francs avant l’assemblée, ou vous faire représenter en donnant pouvoir à un mandataire de votre choix.</p>" +
      "<p>Les pièces justificatives des charges peuvent être consultées selon les modalités suivantes : sur rendez-vous au cabinet du syndic, aux jours et heures précisés ci-dessous.</p>" +
      "<p><b>Documents joints :</b> comptes de l’exercice et annexes comptables ; budget prévisionnel ; projets de résolution ; devis et contrats soumis au vote ; projet de contrat de syndic et sa fiche d’information ; formulaire de vote par correspondance.</p>" +
      "<p><b>Mode d’envoi :</b> lettre recommandée avec accusé de réception, lettre recommandée électronique ou remise contre émargement.</p>" +
      "<p>Veuillez agréer, Madame, Monsieur, l’expression de nos salutations distinguées.</p><p>Le syndic, " + C.syndic + "</p>";
  }
  function docVote() {
    return "<h2>Formulaire de vote par correspondance</h2><p>Assemblée générale du " + fmtDate($("#ag-date").value) + ". Copropriétaire : ……………… Lot(s) : ……… Tantièmes : ………</p>" +
      "<table class='doc-table'><thead><tr><th>Résolution</th><th>Majorité</th><th>Pour</th><th>Contre</th><th>Abstention</th></tr></thead><tbody>" +
      resolutions.map(function (r, i) { return "<tr><td>" + (i + 1) + ". " + esc(r.t) + "</td><td>Art. " + r.m + "</td><td>☐</td><td>☐</td><td>☐</td></tr>"; }).join("") +
      "</tbody></table><p><small>À retourner au syndic au moins trois jours francs avant l’assemblée. Date et signature : ………………</small></p>";
  }
  function names(ids) { return ids.length ? ids.map(function (id) { return lots[id - 1].owner + " (" + lots[id - 1].tantiemes + ")"; }).join(", ") : "aucun"; }
  function docPV() {
    var presentT = C.totalTantiemes - tally(0).vAbs;
    return "<h2>Projet de procès-verbal de l’assemblée générale ordinaire</h2><p>Syndicat des copropriétaires de la " + C.nom + ". Assemblée tenue le " + fmtDate($("#ag-date").value) + " à " + esc($("#ag-heure").value) + ".</p>" +
      "<p>Copropriétaires présents, représentés ou ayant voté par correspondance : " + (lots.length - absents.length) + " sur " + lots.length + ", représentant " + num.format(presentT) + " / " + num.format(C.totalTantiemes) + " tantièmes. Copropriétaires défaillants : " + names(absents) + ". La feuille de présence est annexée au présent procès-verbal.</p>" +
      resolutions.map(function (r, i) {
        var x = tally(i), d = decide(r, x);
        return "<h3>Résolution n° " + (i + 1) + " : " + esc(r.t) + "</h3><p>Majorité requise : " + MAJ[r.m] + ".</p>" +
          "<p>Votes pour : " + num.format(x.vPour) + " tantièmes. Votes contre : " + num.format(x.vContre) + " tantièmes. Abstentions : " + num.format(x.vAbst) + " tantièmes.</p>" +
          "<p><b>Résolution " + d[0].toLowerCase() + "</b> (" + esc(d[1]) + ").</p>" +
          "<p>Copropriétaires opposants : " + names(x.contre) + ". Copropriétaires s’étant abstenus : " + names(x.abst) + ".</p>";
      }).join("") +
      "<p>Le président de séance, le secrétaire et le ou les scrutateurs : signatures.</p>" +
      "<p class='note'>Notification aux copropriétaires opposants et défaillants : les actions en contestation des décisions doivent être introduites dans un délai de deux mois à compter de la notification du procès-verbal (article 42, alinéa 2, de la loi du 10 juillet 1965), dont le texte est reproduit dans la notification.</p>";
  }
  var DOCS = { ordre: ["Ordre du jour", docOrdre], convocation: ["Convocation", docConvocation], vote: ["Formulaire de vote par correspondance", docVote], pv: ["Projet de procès-verbal", docPV] };
  var current = "convocation";
  $$(".doc-tab").forEach(function (b) {
    b.addEventListener("click", function () { current = b.dataset.doc; $$(".doc-tab").forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); }); refresh(); });
  });
  function refresh() {
    renderVotes();
    $("#doc-view").innerHTML = "<div class='stamp'>Projet généré par CoproSens · à valider par le syndic avant tout envoi</div>" + DOCS[current][1]();
  }
  $("#doc-word").addEventListener("click", function () {
    var html = "<html xmlns:o='urn:schemas-microsoft-com:office:office' xmlns:w='urn:schemas-microsoft-com:office:word'><head><meta charset='utf-8'><title>" + DOCS[current][0] + "</title>" +
      "<style>body{font-family:Calibri,Arial,sans-serif;font-size:11pt;line-height:1.4}h2{color:#0e7c86}table{border-collapse:collapse;width:100%}td,th{border:1px solid #999;padding:4px}.warn{color:#b91c1c}.right{text-align:right}.stamp{color:#92400e}</style></head><body>" +
      $("#doc-view").innerHTML + "</body></html>";
    download(DOCS[current][0].toLowerCase().replace(/[^a-z0-9]+/gi, "-") + ".doc", "application/msword", "﻿" + html);
  });
  $("#doc-print").addEventListener("click", function () { document.body.classList.add("print-doc"); window.print(); setTimeout(function () { document.body.classList.remove("print-doc"); }, 500); });
  $("#doc-send").addEventListener("click", function () {
    $("#send-msg").hidden = false;
  });
  renderResolutions(); refresh();
})();
