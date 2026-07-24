# ISEO-SU PROTECTED ZONES v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** PHASE 2B · updated through PHASE 6C RETRY (token local-only)  
**Date:** 2026-07-24  
**Policy:** Although future work may eventually cover the whole site, **initial default is protect-all** until an exact task charter names paths/surfaces.

No secrets stored here.

---

## 1. Global default

| Zone | Protection |
|------|------------|
| All production files under docroot | **PROTECTED** by default |
| Any write / upload / chmod / rename / delete | **FORBIDDEN** without A7 charter + backup proof |
| Database | **PROTECTED** — no phpMyAdmin, no direct DB, no credential copying |
| WordPress settings saves | **PROTECTED** |

---

## 2. Critical protected zones

| Zone | Examples | Why |
|------|----------|-----|
| Config secrets | `wp-config.php` | DB credentials, salts |
| Database | Beget MySQL / phpMyAdmin | Lead/content integrity |
| Forms / mail | `*__FORM.php`, form endpoints in `js/common.js` | Lead loss / spam / PII |
| SMTP / mail path | handlers + any mail plugins | Silent delivery failure |
| SEO calculator | calculator markup, `calc__FORM.php`, theme calc parts | Revenue tool |
| Web-KP / offers candidates | `/offers`, CPT `offer`, related templates | Business proposals |
| Shared header/footer | static HTML chrome; theme `header.php`/`footer.php`/topbar/footer parts | Sitewide breakage |
| Routing | `.htaccess` | HTTPS, rewrites, HTML-as-PHP |
| Cache / security | WP-Optimize, Jetpack, Jetpack WAF dir, Akismet | False smoke / lockouts |
| WordPress core | `wp-admin/`, `wp-includes/` | Core integrity |
| Plugins / themes outside exact task | all plugin dirs; `iseoblog` unless named | Compatibility |
| Static pages outside exact task | `services/`, `cases/`, root HTML | Content regression |
| Logs | `wp-content/debug.log` | May contain sensitive data |
| Uploads | `wp-content/uploads/` | Media + possible sensitive exports |
| Report Hub | `report-hub/` | Separate operational surface |
| Local secrets | `X:\AI MARS\local\sites\iseo-su-production\` | Credentials |

---

## 3. Initial allow posture

**Phase 6A exact allow (completed):** creation of inactive  
`wp-content/plugins/metacode-wpilot/**` only under the Phase 6A install-only charter.

**Phase 6B exact allow (completed):** WordPress Admin activation of **MetaCODE WPilot only**, with read-only verification of safe defaults. No token, bridge, write, REST smoke, or settings saves.

**Phase 6C attempted (blocked on RC5):** Generate-token click with bridge/DEV/writes left **off**. Plugin refused. No token file created.

**Phase 6C-R exact allow (completed):** SFTP in-place update of `wp-content/plugins/metacode-wpilot/**` from accepted RC5 to accepted RC6 only; creation of bounded sibling rollback dir `.mars-rollback-metacode-wpilot-rc5-phase6c-r/`. No token, bridge, write, REST, or settings saves.

**Phase 6C RETRY exact allow (completed):** WordPress Admin generate-token **once** under RC6 with bridge/writes/`dev_confirmed` left **off**; persist plaintext only to `X:\AI MARS\local\tokens\wpilot-prod-iseo-su.token`; update ignored site-profile path/status metadata only. No bridge enable, no writes enable, no REST.

Nothing else is allowlisted for mutation. Bridge enable, writes, REST smoke, and other paths remain **FORBIDDEN** without a **separate** exact charter.

---

## 4. WPilot-specific boundaries (Phase 4B / 6A / 6B / 6C-R)

Even with WPilot **active (RC6 safe defaults)**, the following remain **out of WPilot mutation scope** unless a separate proven charter says otherwise:

| Surface | Rule |
|---------|------|
| Static HTML trees / `home.html` | **FORBIDDEN** via WPilot |
| Shared `css/` / `js/` | **FORBIDDEN** via WPilot |
| Calculator / tariff PHP handlers / `/tariff-calc` | **FORBIDDEN** via WPilot |
| Theme templates (`iseoblog`, `page-home.php`, etc.) | **FORBIDDEN** via WPilot |
| ACF options / field data APIs | **FORBIDDEN** (not implemented in WPilot) |
| CPT `offer` / unresolved web-KP files | **FORBIDDEN** until ownership + charter |
| Forms / mail | **FORBIDDEN** |
| `.htaccess` / `wp-config.php` | **FORBIDDEN** |
| Cache purge via WPilot | **NOT AVAILABLE** — do not invent |
| WPilot write routes | **FORBIDDEN** until GATE 6E+ charter |
| Bridge enable / write enable / REST smoke | **FORBIDDEN** until GATE 6D+ charter |
| Token generate | **DONE (6C RETRY)** — further rotate/revoke needs charter |

WPilot MVP mutation surface (when later enabled): **WordPress `page` `post_content` only**, with plugin backup/rollback — still subordinate to full Beget backup policy.

Plugin filesystem path (present, **active RC6**, safe defaults + token present): `wp-content/plugins/metacode-wpilot/` — protect against wrong-folder deletes; emergency rollback may restore from `.mars-rollback-metacode-wpilot-rc5-phase6c-r/` or deactivate/rename **only** the exact active folder under charter. Do **not** enable bridge/writes or call REST without GATE 6D+ charter. Treat the rollback sibling as temporary evidence — not an activatable plugin; cleanup requires operator gate. Local token file under `X:\AI MARS\local\tokens\` is protected secret storage (Git-ignored).

---

## 5. phpMyAdmin metadata

URL `https://mayday.beget.com/phpMyAdmin/` is **metadata only**. Opening it is outside this programme until a DB charter exists.

---

*Protected zones v1 · updated Phase 6C RETRY 2026-07-24.*
