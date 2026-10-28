/* CoproSens price estimator — English, Brazilian Portuguese and Spanish texts.
   Loaded by /en/pricing/, /pt/precos/ and /es/precios/ before tarifs.js.
   Prices stay in euros in every language; only the display format changes. */
(function () {
  "use strict";
  var D = {
    en: {
      locale: "en-US",
      tiers: ["Small building (up to 32 units)", "Medium building (33 to 100 units)", "Large building (101 to 200 units)"],
      huge: "Very large building (over 200 units): tailored quote",
      quote: "Tailored quote",
      founder: " · founding client offer",
      included: "Included",
      notChosen: "Not selected",
      notChosenF: "Not selected"
    },
    pt: {
      locale: "pt-BR",
      tiers: ["Condomínio pequeno (até 32 unidades)", "Condomínio médio (33 a 100 unidades)", "Condomínio grande (101 a 200 unidades)"],
      huge: "Condomínio muito grande (mais de 200 unidades): orçamento personalizado",
      quote: "Orçamento personalizado",
      founder: " · oferta clientes fundadores",
      included: "Incluído",
      notChosen: "Não incluído",
      notChosenF: "Não incluída"
    },
    es: {
      locale: "es-ES",
      tiers: ["Comunidad pequeña (hasta 32 viviendas)", "Comunidad mediana (de 33 a 100 viviendas)", "Comunidad grande (de 101 a 200 viviendas)"],
      huge: "Comunidad muy grande (más de 200 viviendas): presupuesto personalizado",
      quote: "Presupuesto personalizado",
      founder: " · oferta clientes fundadores",
      included: "Incluido",
      notChosen: "No incluido",
      notChosenF: "No incluido"
    }
  };
  window.PRICING_L10N = D[(document.documentElement.lang || "").slice(0, 2)];
})();
