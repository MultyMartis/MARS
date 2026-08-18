# ISEO-SU PROTECTED ZONES v1

**Programme:** ISEO-SU-SITE-OPS  
**Updated:** 2026-07-24 architecture knowledge capture  
**Policy:** Default **protect-all** until an exact task charter names paths/surfaces.

No secrets stored here.

---

## 1. Global default

| Zone | Protection |
|------|------------|
| All production files under docroot | **PROTECTED** by default |
| Any write / upload / chmod / rename / delete | **FORBIDDEN** without A7 charter + backup proof |
| Database | **PROTECTED** — no phpMyAdmin, no direct DB |
| WordPress settings saves | **PROTECTED** |

---

## 2. Critical protected zones (architecture-evidenced)

| Zone | Examples | Why |
|------|----------|-----|
| Config secrets | `wp-config.php` | DB credentials, salts |
| Routing | `.htaccess` | HTTPS, www, HTML-as-PHP, WP rewrite |
| Database | Beget MySQL | content/leads integrity |
| Forms / mail | all `*__FORM.php` + service copies | lead loss / PII |
| Shared JS | `js/common.js` | forms + calculator + tariffs |
| Shared CSS | `css/main.css`, `css/media.css` | sitewide marketing look; **`css/main.css` operator manual glossary tuning promoted to `production-source/css/main.css` — reconcile before automation overwrite** |
| SEO calculator / tariffs | `/tariff-calc`, ACF calculator groups, `tarif-calc.php`, handlers | revenue tool |
| Web-KP / offers | `/offers`, CPT `offer`, `single-offer.php`, ACF «Предложения» | private commercial proposals |
| Glossary (public + drafts) | CPT `glossary`, `/glossary/`, `archive-glossary.php`, `single-glossary.php`, `template-parts/content-glossary-page-scene.php`, `template-parts/content-topbar.php` (menu link), `inc/glossary-*.php`, non-eligible drafts | do not publish MERGED/DEFERRED/EXCLUDED; hero is services `page_scene` copy without rates; manual CSS authority in `production-source/css/main.css`; exposure/rollback via launch + final baseline docs |
| Global header/footer | static HTML chrome + theme topbar/footer parts | dual-channel breakage |
| Homepage template | `page-home.php` (+ parallel `home.html`) | primary acquisition surface |
| Analytics / verification | `google*.html`, `yandex_*.html`, injected scripts | SEO/property proof |
| Cache / security plugins | Jetpack, WP-Optimize (inactive), Akismet (inactive), Jetpack WAF dir | false smoke / lockouts |
| WordPress core | `wp-admin/`, `wp-includes/` | core integrity |
| Plugins / themes outside charter | all plugin dirs; `iseoblog` unless named | compatibility |
| Uploads / media | `wp-content/uploads/` | media + possible sensitive files |
| Logs | `wp-content/debug.log` | may contain sensitive data |
| Report Hub | `report-hub/` | sibling operational surface |
| Local secrets / token | `X:\AI MARS\local\sites\iseo-su-production\`, `X:\AI MARS\local\tokens\wpilot-prod-iseo-su.token` | credentials |
| WPilot rollback dir | `.mars-rollback-metacode-wpilot-rc5-phase6c-r/` | emergency evidence; not activatable plugin |

---

## 3. Allow posture (historical completed charters only)

Completed allowlists remain limited to prior WPilot install/activation/RC6/token phases.  
**This architecture capture authorized documentation only — no production mutation.**

Bridge enable, writes, REST smoke, and content edits remain **FORBIDDEN** without a **separate** exact charter + fresh Beget backup.

---

## 4. WPilot mutation boundaries

Even with WPilot active (RC6 safe defaults + local token):

| Surface | Rule |
|---------|------|
| Static HTML / `home.html` | **FORBIDDEN** via WPilot |
| Shared css/js | **FORBIDDEN** |
| Calculator / tariff handlers / theme calculator | **FORBIDDEN** |
| Theme templates | **FORBIDDEN** |
| ACF field data | **FORBIDDEN** (not WPilot MVP) |
| CPT `offer` / KP | **FORBIDDEN** until charter |
| Glossary publish / exposure gate / menu link | **FORBIDDEN** until separate publication charter |
| Forms / mail | **FORBIDDEN** |
| `.htaccess` / `wp-config.php` | **FORBIDDEN** |
| Bridge / writes / REST | **FORBIDDEN** until GATE 6D+ |

---

*Protected zones v1 · updated glossary final integration closeout 2026-08-18.*
