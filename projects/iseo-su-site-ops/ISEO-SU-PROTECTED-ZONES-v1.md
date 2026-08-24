# ISEO-SU PROTECTED ZONES v1

**Programme:** ISEO-SU-SITE-OPS  
**Updated:** 2026-08-24 Metrika visitor IP param addon + local-only HMAC secret authority  
**Policy:** Default **protect-all** until an exact task charter names paths/surfaces. **Protected means inspect, diff, back up, change intentionally, validate, and preserve rollback; it does not mean “never touch.”**

No secrets stored here.

---

## 1. Global default

| Zone | Protection |
|------|------------|
| All production files under docroot | **PROTECTED** by default |
| Any write / upload / chmod / rename / delete | **FORBIDDEN** without A7 charter + backup proof |
| Database | **PROTECTED** — no phpMyAdmin, no direct DB |
| WordPress settings saves | **PROTECTED** |
| Accepted manual runtime edits | **PROTECTED FROM BLIND OVERWRITE** — fetch runtime, bounded diff, promote accepted state to canonical source first |

---

## 2. Critical protected zones (architecture-evidenced)

| Zone | Examples | Why |
|------|----------|-----|
| Config secrets | `wp-config.php` | DB credentials, salts |
| Routing | `.htaccess` | HTTPS, www, HTML-as-PHP, WP rewrite |
| Database | Beget MySQL | content/leads integrity |
| Forms / mail | all 12 root `*__FORM.php`, service delegates, `iseo-form-security.php`, `iseo-form-config.php`, `iseo-form-token.php`, `.iseo-form-runtime/`, and production-local `iseo-form-secrets.local.php` | lead loss / PII; shared server validation + anti-spam + recipient authority; canonical mirror `production-source/forms/` |
| Form recipient routing | `iseo-form-config.php` | production recipient must remain `nikel007i33@yandex.ru` only; `test_mode=false`; acceptance-only `im.work@mail.ru`, typo `im.work@nail.ru`, inactive comment `chrra@yandex.ru` are not active recipients |
| Shared JS | `js/common.js` | forms + calculator + tariffs; includes honeypot/token inject + Metrika visitor IP loader hook — reconcile with `production-source/js/common.js` |
| Existing Metrika | counter initialization/options for **54287016** | normal Metrika/Webvisor/goals must not be changed by addon work |
| Metrika visitor IP addon | `metrika-visitor-ip-config.php`, `metrika-visitor-ip.php`, `js/metrika-visitor-ip.js` | analytics-only `ipaddress`; current switch true/ON; false disables addon only; no auto-ban; mirror `production-source/metrika-ip/` |
| Shared CSS | `css/main.css`, `css/media.css` | sitewide marketing look; **`css/main.css` operator manual glossary tuning plus glossary-scoped mobile overflow block; canonical SHA `4a1202b6…`; reconcile before automation overwrite** |
| SEO calculator / tariffs | `/tariff-calc`, ACF calculator groups, `tarif-calc.php`, handlers | revenue tool |
| Web-KP / offers | `/offers`, CPT `offer`, `single-offer.php`, ACF «Предложения» | private commercial proposals |
| Glossary (public + drafts) | CPT `glossary`, `/glossary/`, `archive-glossary.php`, `single-glossary.php`, `template-parts/content-glossary-page-scene.php`, `template-parts/content-topbar.php` (menu link), `inc/glossary-*.php`, non-eligible drafts | do not publish MERGED/DEFERRED/EXCLUDED; hero is services `page_scene` copy without rates; manual CSS authority in `production-source/css/main.css`; exposure/rollback via launch + final baseline docs |
| Sitemaps / robots | `/sitemap.xml`, `/sitemap-static.xml`, `/wp-sitemap.xml`, `robots.txt`, owning WP hooks/settings | current root advertises 404 children; target two-child root index and robots-only-root policy are OPEN, not deployed; preserve working static/WP surfaces |
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

Completed form harden charter (`ISEO-SU-SITE-OPS-FORMS-ANTISPAM-AND-VALIDATION-01`) mutated only named form/security/JS/mail-config surfaces. Further form/mail edits still require a **new** exact charter + scoped backups.

## 3a. Form security note

Do not disable server validation, `contact_company_url` honeypot, ≈3s HMAC timing token, ≈3/5m/form/IP and ≈10/h/IP limits, or ≈10m duplicate protection without charter. Do not enable `test_mode` in lasting production. CAPTCHA is not part of the accepted baseline. Active HMAC secret material must remain local-only and out of tracked source.

## 3b. Runtime/source promotion note

Operator manual runtime edits are valid evidence. Before automation overwrites forms, CSS, JS, theme, Metrika addon, sitemap, or robots:

1. fetch the exact current runtime artifact;
2. diff against the canonical MARS mirror/procedure;
3. preserve accepted operator changes;
4. promote the reconciled state into MARS source;
5. only then deploy the next bounded change.



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
| Glossary publish / exposure / menu / hero / title | Final baseline is complete; **further changes require a new exact charter** |
| Forms / mail | **FORBIDDEN** |
| Metrika counter / visitor-IP addon | **FORBIDDEN** except exact addon/counter charter; soft kill must preserve normal Metrika |
| Sitemaps / robots | **FORBIDDEN** until exact implementation charter; target remains open |
| `.htaccess` / `wp-config.php` | **FORBIDDEN** |
| Bridge / writes / REST | **FORBIDDEN** until GATE 6D+ |

---

*Protected zones v1 · current-state reconciliation 2026-08-24.*
