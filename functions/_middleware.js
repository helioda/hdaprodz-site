/**
 * Language routing for the home page.
 * - First visit to "/" without a remembered choice: send the visitor to the home page in
 *   their browser language (Accept-Language), else their country's language, else English
 *   for languages we don't offer. French visitors stay on "/".
 * - A home page reached from our own site (language menu, logo) counts as a choice and is
 *   remembered for a year in the "hda-lang" cookie.
 * - Search engines and link previews are never redirected, so every version stays indexed.
 * Runs only on "/", "/en/", "/pt/", "/es/" and /api/* (see _routes.json).
 */
const HOMES = { "/": "fr", "/en/": "en", "/pt/": "pt", "/es/": "es" };
const PATH = { fr: "/", en: "/en/", pt: "/pt/", es: "/es/" };
const COUNTRY = {};
"FR BE LU MC".split(" ").forEach((c) => (COUNTRY[c] = "fr"));
"BR PT AO MZ CV GW ST TL".split(" ").forEach((c) => (COUNTRY[c] = "pt"));
"ES MX AR CO CL PE VE EC GT CU BO DO HN PY SV NI CR PA UY PR GQ".split(" ").forEach((c) => (COUNTRY[c] = "es"));
const BOT = /bot|crawl|spider|slurp|preview|facebookexternalhit|embedly|whatsapp|telegram|discord|linkedin|skype|lighthouse/i;

function fromAcceptLanguage(h) {
  return (h || "")
    .split(",")
    .map((p) => { const [tag, ...prm] = p.trim().split(";"); const q = prm.find((x) => x.trim().startsWith("q=")); return { l: tag.toLowerCase().slice(0, 2), q: q ? parseFloat(q.split("=")[1]) || 0 : 1 }; })
    .filter((x) => x.l && x.q > 0)
    .sort((a, b) => b.q - a.q)
    .map((x) => x.l)
    .find((l) => l in PATH);
}

export async function onRequest(ctx) {
  const { request, next } = ctx;
  const url = new URL(request.url);
  const lang = HOMES[url.pathname];
  if (!lang || request.method !== "GET") return next();

  const ref = request.headers.get("Referer") || "";
  let sameSite = false;
  try { sameSite = new URL(ref).host === url.host; } catch (e) {}

  if (sameSite || url.searchParams.has("lang")) {
    const res = await next();
    const out = new Response(res.body, res);
    out.headers.append("Set-Cookie", `hda-lang=${lang}; Path=/; Max-Age=31536000; SameSite=Lax; Secure`);
    return out;
  }

  if (lang === "fr" && !BOT.test(request.headers.get("User-Agent") || "")) {
    const cookie = (request.headers.get("Cookie") || "").match(/(?:^|;\s*)hda-lang=(fr|en|pt|es)/);
    const want = cookie ? cookie[1]
      : fromAcceptLanguage(request.headers.get("Accept-Language")) || COUNTRY[(request.cf && request.cf.country) || ""] || "en";
    if (want !== "fr") {
      return new Response(null, {
        status: 302,
        headers: { Location: PATH[want] + url.search, Vary: "Accept-Language, Cookie", "Cache-Control": "private, no-store" },
      });
    }
  }
  const res = await next();
  const out = new Response(res.body, res);
  out.headers.set("Vary", "Accept-Language, Cookie");
  return out;
}
