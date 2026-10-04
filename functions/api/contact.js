/**
 * HDA Solutions — project request form handler (Cloudflare Pages Function).
 * Route: POST /api/contact
 *
 * Flow: validate input → honeypot + timing check → Cloudflare Turnstile check
 *       → send the request by email through Microsoft Graph (app-only,
 *         scoped in Exchange Online to the single sending mailbox).
 *
 * Required environment variables (Cloudflare Pages → Settings → Variables and Secrets):
 *   TURNSTILE_SECRET   (secret)  Turnstile widget secret key
 *   M365_TENANT_ID              Microsoft Entra tenant ID
 *   M365_CLIENT_ID              App registration (client) ID
 *   M365_CLIENT_SECRET (secret)  App registration client secret
 *   MAIL_FROM                   Mailbox the app sends from, e.g. h@hdaprodz.com
 *   MAIL_TO                     Mailbox that receives requests (can equal MAIL_FROM)
 */

const LIMITS = {
  name: 100,
  company: 120,
  email: 254,
  phone: 40,
  projectType: 60,
  description: 5000,
  timeline: 60,
  budget: 60,
  source: 120,
};

const PROJECT_TYPES = [
  "Agent ou copilote IA",
  "Automatisation de processus",
  "Accès aux documents et à la connaissance",
  "Production musicale ou audio",
  "Autre",
];
const TIMELINES = ["Dès que possible", "Dans 1 à 3 mois", "Dans 3 à 6 mois", "Plus tard / à définir"];
const BUDGETS = ["Moins de 2 000 €", "2 000 – 5 000 €", "5 000 – 15 000 €", "Plus de 15 000 €", "À définir ensemble"];

const MIN_FILL_MS = 3000; // a human needs more than 3 s to fill the form
const MAX_FILL_MS = 24 * 60 * 60 * 1000;

export async function onRequestPost(context) {
  const { request, env } = context;
  const wantsJson = (request.headers.get("Accept") || "").includes("application/json");

  try {
    const missing = ["TURNSTILE_SECRET", "M365_TENANT_ID", "M365_CLIENT_ID", "M365_CLIENT_SECRET", "MAIL_FROM", "MAIL_TO"]
      .filter((k) => !env[k]);
    if (missing.length) {
      console.error("Missing configuration:", missing.join(", "));
      return reply(wantsJson, 500, "config");
    }

    const data = await readBody(request);
    if (!data) return reply(wantsJson, 400, "invalid");

    // Honeypot: real visitors never see or fill this field.
    if (clean(data.website)) return reply(wantsJson, 200, "ok", fakeRef());

    // Timing check: rejects instant bot submissions.
    const started = Number(data.started);
    const elapsed = Date.now() - started;
    if (!Number.isFinite(started) || elapsed < MIN_FILL_MS || elapsed > MAX_FILL_MS) {
      return reply(wantsJson, 400, "timing");
    }

    const form = {
      name: clean(data.name, LIMITS.name),
      company: clean(data.company, LIMITS.company),
      email: clean(data.email, LIMITS.email).toLowerCase(),
      phone: clean(data.phone, LIMITS.phone),
      projectType: clean(data.projectType, LIMITS.projectType),
      description: clean(data.description, LIMITS.description, true),
      timeline: clean(data.timeline, LIMITS.timeline),
      budget: clean(data.budget, LIMITS.budget),
      source: clean(data.source, LIMITS.source),
      consent: data.consent === "on" || data.consent === "true" || data.consent === true,
    };

    const errors = validate(form);
    if (errors.length) return reply(wantsJson, 422, "validation", null, errors);

    const ip = request.headers.get("CF-Connecting-IP") || "";
    const human = await verifyTurnstile(env.TURNSTILE_SECRET, data["cf-turnstile-response"], ip);
    if (!human) return reply(wantsJson, 403, "captcha");

    const ref = makeRef();
    await sendMail(env, form, ref);
    return reply(wantsJson, 200, "ok", ref);
  } catch (err) {
    console.error("Contact form error:", err && err.message ? err.message : err);
    return reply(wantsJson, 502, "send");
  }
}

// Any other method on this route.
export async function onRequest() {
  return new Response("Method Not Allowed", { status: 405, headers: { Allow: "POST" } });
}

/* ---------- input ---------- */

async function readBody(request) {
  const type = request.headers.get("Content-Type") || "";
  const length = Number(request.headers.get("Content-Length") || 0);
  if (length > 32 * 1024) return null;
  try {
    if (type.includes("application/json")) return await request.json();
    if (type.includes("application/x-www-form-urlencoded") || type.includes("multipart/form-data")) {
      return Object.fromEntries(await request.formData());
    }
  } catch {
    return null;
  }
  return null;
}

function clean(value, max = 200, multiline = false) {
  if (typeof value !== "string") return "";
  let v = value.normalize("NFC").replace(/[\u0000-\u0008\u000B\u000C\u000E-\u001F\u007F]/g, "");
  v = multiline ? v.replace(/\r\n?/g, "\n").replace(/\n{4,}/g, "\n\n\n") : v.replace(/\s+/g, " ");
  return v.trim().slice(0, max);
}

function validate(f) {
  const errors = [];
  if (f.name.length < 2) errors.push("name");
  if (!/^[^\s@<>()",;:]+@[^\s@<>()",;:]+\.[a-z]{2,}$/i.test(f.email)) errors.push("email");
  if (f.phone && !/^[+()\d\s.\-]{6,40}$/.test(f.phone)) errors.push("phone");
  if (!PROJECT_TYPES.includes(f.projectType)) errors.push("projectType");
  if (f.description.length < 20) errors.push("description");
  if (f.timeline && !TIMELINES.includes(f.timeline)) errors.push("timeline");
  if (f.budget && !BUDGETS.includes(f.budget)) errors.push("budget");
  if (!f.consent) errors.push("consent");
  return errors;
}

/* ---------- Turnstile ---------- */

async function verifyTurnstile(secret, token, ip) {
  if (typeof token !== "string" || !token || token.length > 2048) return false;
  const body = new FormData();
  body.append("secret", secret);
  body.append("response", token);
  if (ip) body.append("remoteip", ip);
  const res = await fetch("https://challenges.cloudflare.com/turnstile/v0/siteverify", { method: "POST", body });
  if (!res.ok) return false;
  const out = await res.json();
  return out.success === true;
}

/* ---------- Microsoft Graph ---------- */

async function getGraphToken(env) {
  const body = new URLSearchParams({
    client_id: env.M365_CLIENT_ID,
    client_secret: env.M365_CLIENT_SECRET,
    scope: "https://graph.microsoft.com/.default",
    grant_type: "client_credentials",
  });
  const res = await fetch(`https://login.microsoftonline.com/${encodeURIComponent(env.M365_TENANT_ID)}/oauth2/v2.0/token`, {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body,
  });
  if (!res.ok) throw new Error(`token ${res.status}: ${(await res.text()).slice(0, 300)}`);
  const json = await res.json();
  return json.access_token;
}

async function sendMail(env, f, ref) {
  const token = await getGraphToken(env);
  const subject = `[Demande de projet ${ref}] ${f.projectType} — ${f.name}${f.company ? ` (${f.company})` : ""}`;

  const rows = [
    ["Référence", ref],
    ["Nom", f.name],
    ["Entreprise", f.company || "—"],
    ["E-mail", f.email],
    ["Téléphone", f.phone || "—"],
    ["Type de projet", f.projectType],
    ["Délai souhaité", f.timeline || "—"],
    ["Budget indicatif", f.budget || "—"],
    ["Source", f.source || "—"],
    ["Reçu le", new Date().toLocaleString("fr-FR", { timeZone: "Europe/Paris" })],
  ];

  const html = `<div style="font-family:Arial,Helvetica,sans-serif;font-size:14px;color:#132a29">
<h2 style="margin:0 0 12px">Nouvelle demande de projet</h2>
<table style="border-collapse:collapse;margin-bottom:16px">${rows
    .map(([k, v]) => `<tr><td style="padding:4px 14px 4px 0;color:#5b6b6a;vertical-align:top">${esc(k)}</td><td style="padding:4px 0"><strong>${esc(v)}</strong></td></tr>`)
    .join("")}</table>
<h3 style="margin:0 0 6px">Description du projet</h3>
<div style="white-space:pre-wrap;border-left:3px solid #86e8ff;padding:8px 12px;background:#f5f7fb">${esc(f.description)}</div>
<p style="color:#5b6b6a;font-size:12px;margin-top:16px">Envoyé depuis le formulaire www.hdaprodz.com. Répondre à ce message écrit directement au demandeur.</p>
</div>`;

  const message = {
    subject,
    body: { contentType: "HTML", content: html },
    toRecipients: [{ emailAddress: { address: env.MAIL_TO } }],
    replyTo: [{ emailAddress: { address: f.email, name: f.name } }],
  };

  const res = await fetch(`https://graph.microsoft.com/v1.0/users/${encodeURIComponent(env.MAIL_FROM)}/sendMail`, {
    method: "POST",
    headers: { Authorization: `Bearer ${token}`, "Content-Type": "application/json" },
    body: JSON.stringify({ message, saveToSentItems: true }),
  });
  if (res.status !== 202) throw new Error(`sendMail ${res.status}: ${(await res.text()).slice(0, 300)}`);
}

/* ---------- output ---------- */

function reply(wantsJson, status, code, ref = null, fields = []) {
  if (wantsJson) {
    return new Response(JSON.stringify({ ok: code === "ok", code, ref, fields }), {
      status,
      headers: { "Content-Type": "application/json; charset=utf-8", "Cache-Control": "no-store" },
    });
  }
  // Without JavaScript: plain form post → redirect back to the page with a status.
  const params = new URLSearchParams({ statut: code === "ok" ? "ok" : "erreur" });
  if (ref) params.set("ref", ref);
  return new Response(null, { status: 303, headers: { Location: `/projet.html?${params}#formulaire` } });
}

function makeRef() {
  const d = new Date();
  const ymd = d.toISOString().slice(0, 10).replace(/-/g, "");
  const rand = crypto.getRandomValues(new Uint32Array(1))[0].toString(36).toUpperCase().padStart(5, "0").slice(-5);
  return `HDA-${ymd}-${rand}`;
}

function fakeRef() {
  return makeRef();
}

function esc(s) {
  return String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]);
}
