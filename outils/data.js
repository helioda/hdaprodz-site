/* Fictitious demo copropriété: Résidence Le Clos des Mésanges (same data as demo.hdaprodz.com).
   42 lots, 10 000 tantièmes généraux. Budget prévisionnel 2026: 156 500 €; fonds de travaux 5 %. */
(function () {
  "use strict";
  var T = [194,244,314,239,189,254,189,254,299,259,179,245,194,248,308,243,198,238,188,253,303,253,
           183,258,178,248,308,248,193,243,198,238,303,253,188,253,183,258,293,248,193,248];
  function type(t) { return t < 200 ? "T2" : t < 280 ? "T3" : "T4"; }
  var base = { T2: [38, 880], T3: [52, 1180], T4: [66, 1470] }; // m³ eau froide, unités répartiteurs
  var lots = T.map(function (t, i) {
    var n = i + 1, ty = type(t);
    var v = ((n * 37) % 11) - 5;                       // deterministic variation -5..+5
    return {
      id: n,
      label: "Lot " + (n < 10 ? "0" + n : n),
      owner: "Copropriétaire du lot " + (n < 10 ? "0" + n : n),
      type: ty,
      tantiemes: t,
      etage: n <= 6 ? 0 : Math.ceil((n - 6) / 6),        // lots 1-6 au rez-de-chaussée
      eau: base[ty][0] + v,                               // relevé compteur individuel (m³)
      chauffage: base[ty][1] + v * 25                     // unités des répartiteurs
    };
  });
  window.COPRO = {
    nom: "Résidence Le Clos des Mésanges",
    adresse: "12 allée des Mésanges, 91300 Massy (adresse fictive)",
    syndic: "Cabinet Démo Gestion (fictif)",
    totalTantiemes: 10000,
    lots: lots,
    budget: { generales: 98000, ascenseur: 8500, eau: 18000, chauffage: 32000 },
    fondsTravauxPct: 5,
    chauffageConsoPct: 70
  };
})();
