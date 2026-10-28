/**
 * Public, non-secret configuration for the project request page.
 * Route: GET /api/config
 * Env: TURNSTILE_SITEKEY (public site key of the Turnstile widget)
 */
export async function onRequestGet({ env }) {
  return new Response(JSON.stringify({ turnstileSitekey: env.TURNSTILE_SITEKEY || null }), {
    headers: { "Content-Type": "application/json; charset=utf-8", "Cache-Control": "public, max-age=300" },
  });
}
