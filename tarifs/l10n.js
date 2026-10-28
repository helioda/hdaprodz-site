/* CoproSens price estimator — English, Brazilian Portuguese and Spanish texts.
   Loaded by /en/pricing/, /pt/precos/ and /es/precios/ before tarifs.js.
   Prices are set in euros; tarifs.js converts them to the chosen currency (indicative). */
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
      fx: "Indicative conversion of our euro prices at the ECB reference rate of {date} (€1 = {rate}). Your written quote confirms the amount and currency.",
      fxDate: "26 Oct 2026",
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
      fx: "Conversão indicativa dos nossos preços em euros, à taxa de referência do BCE de {date} (1 € = {rate}). O orçamento por escrito confirma o valor e a moeda.",
      fxDate: "26/10/2026",
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
      fx: "Conversión orientativa de nuestros precios en euros, al tipo de referencia del BCE del {date} (1 € = {rate}). El presupuesto por escrito confirma el importe y la moneda.",
      fxDate: "26/10/2026",
      notChosenF: "No incluido"
    }
  };
  window.PRICING_L10N = D[(document.documentElement.lang || "").slice(0, 2)];
})();
