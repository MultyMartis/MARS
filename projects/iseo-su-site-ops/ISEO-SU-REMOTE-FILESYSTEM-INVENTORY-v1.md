# ISEO-SU REMOTE FILESYSTEM INVENTORY v1

**Programme:** ISEO-SU-SITE-OPS  
**Origin:** PHASE 2B  
**Updated:** 2026-07-24 architecture knowledge capture  
**Protocol:** SFTP read-only  
**Docroot (sanitized):** `/home/[REDACTED]/[REDACTED]/i-seo.su/public_html`

No secret file contents.

---

## 1. Roots

| Role | Path |
|------|------|
| Docroot / WP root | `…/i-seo.su/public_html` |
| Theme | `wp-content/themes/iseoblog/` |
| Plugins | `wp-content/plugins/` |
| Shared assets | `css/`, `js/`, `img/`, `fonts/`, `libs/`, `favicon/`, `video/` |
| Marketing | root `*.html`, `services/`, `cases/` |
| Apps | `report-hub/`, `reports/` |

## 2. Top-level dirs

`cases/`, `css/`, `docs/`, `favicon/`, `fonts/`, `img/`, `js/`, `libs/`, `report-hub/`, `reports/`, `services/`, `video/`, `wp-admin/`, `wp-content/`, `wp-includes/`

## 3. WordPress trees

| Path | Notes |
|------|-------|
| `wp-config.php` | present (secrets excluded) |
| `wp-content/themes/iseoblog/` | sole theme; home/blog/tariff/offer templates |
| `wp-content/plugins/metacode-wpilot/` | active RC6 |
| `wp-content/plugins/.mars-rollback-metacode-wpilot-rc5-phase6c-r/` | retained rollback sibling |
| `wp-content/plugins/advanced-custom-fields-pro-main/` | ACF PRO |
| `wp-content/uploads/` | 2025/, 2026/, sass/, wpo/ |
| `wp-content/debug.log` | present — do not publish |

## 4. Custom handlers / tools

Root `*__FORM.php`; copies under `services/{seo,adv,audit,development,serm,ai-optimization}/`; `js/common.js`; `varvara-new.php`; `report-hub/`.

## 5. Build sources on server

`package.json` / `gulpfile` / `src` / `scss` / root `composer.json` / `.git` — **absent**.

## 6. Routing file

`.htaccess`: HTTPS, Bytespider block, www→apex, HTML-as-PHP, WordPress rewrite.

## 7. Authority

For ownership interpretation use the architecture knowledge package — this inventory is a filesystem index, not the task router.

---

*Remote filesystem inventory v1 · updated 2026-07-24.*
