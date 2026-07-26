# METALLKA — Site Passport v1

**Programme:** METALLKA-RU-SITE-OPS  
**Status:** POPULATED — Phase 2B production read-only discovery  
**Date:** 2026-07-26  
**Site:** `https://metallka.ru/`  
**Environment:** PRODUCTION  
**Discovery:** COMPLETE (Beget panel UI PARTIAL — panel credentials not filled in local secrets)

---

## 1. Identity

| Field | Value | Evidence class |
|-------|-------|----------------|
| Domain (canonical) | `metallka.ru` (apex) | Public HTTP |
| WWW behavior | `https://www.metallka.ru/` → 301 → `https://metallka.ru/` | Public HTTP |
| HTTP → HTTPS | `http://metallka.ru/` → 301 → HTTPS apex | Public HTTP |
| Site URL | `https://metallka.ru` | WP-CLI `siteurl` |
| Home URL | `https://metallka.ru` | WP-CLI `home` |
| Front page | Page ID **2** (`home`) | WP-CLI `page_on_front` |
| Show on front | `page` | WP-CLI |
| Language | `ru_RU` | WP-CLI `WPLANG` |
| Timezone | GMT offset **+3** (empty `timezone_string`) | WP-CLI |
| Multisite | **NO** | WP-CLI |
| Permalink | `/%postname%/` | WP-CLI |
| WP_DEBUG | `false` | WP-CLI / wp-config flag grep |
| DB table prefix | `wp_` | WP-CLI (sanitized) |

---

## 2. Hosting / runtime

| Field | Value | Evidence class |
|-------|-------|----------------|
| Provider | **Beget** | Operator intake + kernel `beget-acl` + path shape |
| Docroot (sanitized) | `/home/[REDACTED]/[REDACTED]/metallka.ru/public_html` | SSH |
| Webserver | `nginx-reuseport/1.21.1` | Public `Server` header |
| PHP (HTTP runtime) | **8.3.20** | Public `X-Powered-By` |
| PHP (WP-CLI binary) | **7.4.33** (`/usr/local/php/cgi/7.4/bin/php`) | SSH `wp --info` |
| PHP (default shell `php -v`) | **5.6.40** | SSH — **not** visitor runtime |
| WP-CLI | Present, **2.9.0** | SSH |
| SSL | HTTPS serves 200 on apex | Public HTTP |
| Staging | **NONE** (operator confirmed) | Intake |
| Cron (user crontab) | Empty / none visible | SSH `crontab -l` |
| CDN / Cloudflare | **Not evidenced** (no CF-Ray / Via) | Public headers |

---

## 3. WordPress core

| Field | Value |
|-------|-------|
| WordPress | **7.0.2** |
| Install path | Docroot (standard root install) |
| `wp-content` | `.../public_html/wp-content` |
| Admin users (count/roles only) | 2 users with `administrator` role class |
| Discovery admin channel | SSH + WP-CLI (read-only); WP Admin credentials present locally but browser admin UI not required for this wave |

---

## 4. Theme stack

| Field | Value |
|-------|-------|
| Active stylesheet | `dt-the7-child` (`the7dtchild` header name) **1.0.0** |
| Active / parent template | `dt-the7` (**The7 11.6.0.1**) |
| Child directory | `wp-content/themes/dt-the7-child/` |
| Parent directory | `wp-content/themes/dt-the7/` |
| Inactive | `twentytwentyfive` 1.0 |
| The7 options blob | WP option `the7dtchild` — **array, 956 keys** |
| Generated CSS | `wp-content/uploads/the7-css/` (`custom.css`, `media.css`, …) |

---

## 5. Builder / SEO / forms (summary)

| Layer | Reality |
|-------|---------|
| WPBakery | **Active** `js_composer` **6.10.0** — pages use `_wpb_vc_js_status=true` |
| Ultimate Addons | Active `Ultimate_VC_Addons` 3.19.14 |
| Slider Revolution | Active `revslider` **6.6.7** |
| Forms | Contact Form 7 + Honeypot + CFDB7 |
| SEO | Rank Math active; Rank Math Pro inactive |
| Optimization | Clearfy active; Fast Velocity Minify **inactive** (cache dirs remain) |
| ACF | **NOT PRESENT** |
| WPilot | **ABSENT** (no plugin dir, no `wpilot_options`, no tables, no REST ns) |

---

## 6. Source authority

| Class | Status |
|-------|--------|
| External Git / archive | **NONE KNOWN** (operator) |
| Production `.git` | **NO_GIT** |
| Filesystem code authority | **PROVISIONAL SOURCE AUTHORITY** (production runtime) |
| DB / admin-authored content | Authoritative for page `post_content`, menus, CF7, Shortcoder, Popup Maker, The7 options |
| Developer markers | Child `style.css` comment `/*WSP Fixes*/`; child `functions.php` comment references WSP |

---

## 7. Backup / restore (summary)

Operator-attested Beget backup + restore **AVAILABLE**. Panel credentials **not** filled in local secrets → panel UI not inspected this wave. See `METALLKA-BACKUP-ROLLBACK-MODEL-v1.md`.

---

## 8. Evidence locus

Sanitized bulk evidence: `X:\AI MARS STORAGE\wpilot\evidence\metallka-ru-site-ops\phase-2b-discovery\`

---

*Site Passport v1 · Phase 2B · secrets never included.*
