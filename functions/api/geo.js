/**
 * Visitor's country as seen by Cloudflare, used by the price estimator to pick a currency.
 * Route: GET /api/geo  ->  {"country":"BR"}
 */
export async function onRequestGet({ request }) {
  const country = (request.cf && request.cf.country) || null;
  return new Response(JSON.stringify({ country }), {
    headers: { "Content-Type": "application/json; charset=utf-8", "Cache-Control": "private, no-store" },
  });
}
