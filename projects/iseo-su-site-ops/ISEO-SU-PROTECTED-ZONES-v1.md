# ISEO-SU PROTECTED ZONES v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** PHASE 2B · **updated PHASE 4B**  
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

Nothing is allowlisted for mutation after Phase 2B / 4B.

Future allowlists must be **exact paths** in a task charter.

---

## 4. WPilot-specific boundaries (Phase 4B)

Even after a future authorized WPilot install, the following remain **out of WPilot mutation scope** unless a separate proven charter says otherwise:

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

WPilot MVP mutation surface (when later enabled): **WordPress `page` `post_content` only**, with plugin backup/rollback — still subordinate to full Beget backup policy.

Plugin filesystem path (future): `wp-content/plugins/metacode-wpilot/` — protect against wrong-folder deletes; emergency rollback may rename/delete **only** that exact folder under charter.

---

## 5. phpMyAdmin metadata

URL `https://mayday.beget.com/phpMyAdmin/` is **metadata only**. Opening it is outside this programme until a DB charter exists.

---

*Protected zones v1 · updated Phase 4B 2026-07-24.*
