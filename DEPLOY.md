# HDA Solutions site: project request form on Cloudflare Pages

## What changed in the repository

| File | Purpose |
|---|---|
| `projet.html` | New "Demande de projet" page: form + privacy notice (FR) |
| `assets/site.css` | Site styles, extracted from `index.html` (same rules) |
| `assets/projet.css`, `assets/projet.js` | Form styling, validation, Turnstile, submission |
| `functions/api/contact.js` | Server code: checks the request, then emails it via Microsoft Graph |
| `functions/api/config.js` | Gives the page the public Turnstile site key |
| `_headers`, `_routes.json` | Security headers; only `/api/*` runs server code |
| `index.html` | Buttons now open `projet.html`; privacy text updated |

No secret is stored in the code. All secrets live in Cloudflare's encrypted settings.

**Order matters:** the live site keeps working on GitHub Pages until step 8. Until then, the new page shows "formulaire indisponible" plus the e-mail link, so nothing breaks.

---

## 1. Push the files to GitHub

1. Copy the contents of this package into your local repository (`D:\Claude\GitHub`), replacing `index.html`.
2. In Visual Studio: **Git Changes** → commit message `Add project request form (Cloudflare Pages)` → **Commit All** → **Push**.

- **Rollback:** revert the commit in Git Changes (History → Revert) and push.

## 2. Create the Cloudflare Pages project

1. Create a free account at `dash.cloudflare.com` (use `h@hdaprodz.com`).
2. **Workers & Pages → Create → Pages → Connect to Git**, authorize GitHub, select `helioda/hdaprodz-site`.
3. Build settings: **Framework preset: None**, **Build command: empty**, **Build output directory: `/`** (check the field's wording in the UI; the site has no build step).
4. Note the project address, e.g. `hdaprodz-site.pages.dev`.

## 3. Create the Turnstile widget (anti-bot, free)

1. Cloudflare dashboard → **Turnstile → Add widget**.
2. Hostnames: `www.hdaprodz.com` and your `*.pages.dev` project address.
3. Mode: **Managed**. Keep the **site key** (public) and **secret key** (private) open for step 6.

## 4. Register the sending app in Microsoft Entra

1. `entra.microsoft.com` → **Applications → App registrations → New registration**.
   - Name: `HDA website contact form` · Accounts in this organizational directory only · no redirect URI.
2. Note the **Application (client) ID** and **Directory (tenant) ID**.
3. **Certificates & secrets → Certificates → Upload certificate** → `hda-contact-form.cer`. (Client secrets are blocked by the tenant policy; a certificate is the supported, stronger alternative.) It expires on 3 Oct 2028: put that date in your calendar.
4. **Do not** add `Mail.Send` under API permissions. That would let the app send as *any* mailbox. Step 5 grants it for one mailbox only.
5. Go to **Enterprise applications** → open `HDA website contact form` → note its **Application ID** and **Object ID** (these are the ones Exchange needs).

- **Rollback:** delete the app registration.

## 5. Allow the app to send from h@hdaprodz.com only (Exchange Online, App RBAC)

PowerShell (as administrator), one block at a time:

```powershell
Install-Module ExchangeOnlineManagement -Scope CurrentUser
Connect-ExchangeOnline -UserPrincipalName h@hdaprodz.com

New-ServicePrincipal -AppId <Application ID> -ObjectId <Object ID> -DisplayName "HDA website contact form"
New-ManagementScope -Name "HDA site sender" -RecipientRestrictionFilter "PrimarySmtpAddress -eq 'h@hdaprodz.com'"
New-ManagementRoleAssignment -App <Object ID> -Role "Application Mail.Send" -CustomResourceScope "HDA site sender"

Test-ServicePrincipalAuthorization -Identity <Object ID> -Resource h@hdaprodz.com | Format-Table
```

**Stop criterion:** the test shows `Application Mail.Send` with **InScope = True**. If `New-ManagementScope` rejects the filter, stop and send me the error.

Permission changes can take 30 minutes to 2 hours to apply.

- **Rollback:** `Get-ManagementRoleAssignment -RoleAssignee <Object ID> | Remove-ManagementRoleAssignment`, then `Remove-ManagementScope "HDA site sender"` and `Remove-ServicePrincipal -Identity <Object ID>`.

## 6. Enter the settings in Cloudflare

Pages project → **Settings → Variables and Secrets** → Production:

| Name | Value | Type |
|---|---|---|
| `TURNSTILE_SITEKEY` | Turnstile site key | Text |
| `TURNSTILE_SECRET` | Turnstile secret key | **Secret** |
| `M365_TENANT_ID` | Directory (tenant) ID | Text |
| `M365_CLIENT_ID` | Application (client) ID | Text |
| `M365_CERT_PRIVATE_KEY` | Full contents of `hda-contact-form-private-key.pem` | **Secret** |
| `M365_CERT_THUMBPRINT` | `UolvkwFCNj9ubOz7eK8ZEXJlP0JFqICe4YGso21Gaxk` | Text |
| `MAIL_FROM` | `h@hdaprodz.com` | Text |
| `MAIL_TO` | `h@hdaprodz.com` | Text |

Then **Deployments → latest → Retry deployment** so the values apply. Never paste the secrets into a chat. Delete the private key file from your PC once it is saved in Cloudflare.

## 7. Test on the `.pages.dev` address

1. Open `https://<project>.pages.dev/projet.html`, fill the form, send.
2. **Stop criterion:** the page shows a reference `HDA-YYYYMMDD-XXXXX`, and the e-mail arrives in `h@hdaprodz.com`; **Reply** goes to the address typed in the form.
3. If it fails: Pages project → **Functions → Real-time logs**, submit again, and send me the red line (`token 401`, `sendMail 403`…).

## 8. Move www.hdaprodz.com to Cloudflare

1. Pages project → **Custom domains → Set up a domain** → `www.hdaprodz.com` → Continue. Do this **before** the DNS change (Cloudflare documents a 522 error otherwise).
2. STRATO DNS: edit the `www` CNAME from `helioda.github.io` to `<project>.pages.dev`. Do not touch the apex, MX, SPF or autodiscover records.
3. If certificate issuance stalls: check for CAA records on `hdaprodz.com` that exclude Cloudflare's certificate authorities.

**Stop criterion:** `https://www.hdaprodz.com` loads with a valid certificate and `https://www.hdaprodz.com/api/config` returns your site key.

- **Rollback:** set the `www` CNAME back to `helioda.github.io`. GitHub Pages is still configured.

## 9. Clean up (after a few days without issues)

- GitHub → repository **Settings → Pages** → disable, so there is one live copy only. Keep the `CNAME` file; it's harmless on Cloudflare.

---

## Costs

- Cloudflare Pages + Functions: free plan. Static files are unlimited; Functions share the 100,000 requests/day Workers free quota.
- Turnstile: free plan, unlimited challenges.
- Microsoft Graph mail: included in your Microsoft 365 mailbox.

## Not verified yet

- The exact label of the "Build output directory" field in today's Cloudflare UI (step 2).
- That `PrimarySmtpAddress` is accepted in the management-scope filter (step 5): the test cmdlet confirms it.
- App-only sending with **no** Entra `Mail.Send` permission, relying on App RBAC alone (step 5). Step 7's test is the proof.
