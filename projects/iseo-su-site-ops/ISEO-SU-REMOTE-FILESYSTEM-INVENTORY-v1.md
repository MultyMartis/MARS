# ISEO-SU REMOTE FILESYSTEM INVENTORY v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** PHASE 2B read-only SFTP inventory  
**Date:** 2026-07-24  
**Protocol:** SFTP (port 22)  
**Docroot (sanitized):** `/home/[REDACTED]/[REDACTED]/i-seo.su/public_html`

No secret file contents. Account path segments redacted.

---

## 1. Roots

| Role | Sanitized path / relative |
|------|---------------------------|
| Hosting home (redacted) | `/home/[REDACTED]/[REDACTED]/` |
| Site folder | `…/i-seo.su/` |
| **Docroot / WordPress root** | `…/i-seo.su/public_html` |
| WordPress core | `wp-admin/`, `wp-includes/`, `wp-content/` |
| Static marketing roots | docroot `*.html`, `services/`, `cases/` |
| Shared assets | `css/`, `js/`, `img/`, `fonts/`, `libs/`, `favicon/`, `video/` |
| Custom apps | `report-hub/`, `reports/` |
| Docs/PDFs | `docs/` |

---

## 2. Docroot top-level directories

`cases/`, `css/`, `docs/`, `favicon/`, `fonts/`, `img/`, `js/`, `libs/`, `report-hub/`, `reports/`, `services/`, `video/`, `wp-admin/`, `wp-content/`, `wp-includes/`

---

## 3. WordPress trees

| Path | Classification |
|------|----------------|
| `wp-config.php` | WordPress config (**secrets excluded from evidence**) |
| `wp-admin/` | WordPress core admin |
| `wp-includes/` | WordPress core |
| `wp-content/themes/iseoblog/` | Active custom theme candidate (sole theme) |
| `wp-content/plugins/` | Plugin inventory (see WordPress inventory doc) |
| `wp-content/mu-plugins/` | Empty / absent listing |
| `wp-content/uploads/` | Uploads (`2025/`, `2026/`, `sass/`, `wpo/`) |
| `wp-content/debug.log` | Present — **protected / do not publish** |
| `wp-content/upgrade/`, `upgrade-temp-backup/` | Core/plugin upgrade artifacts |

---

## 4. Themes

| Theme dir | Notes |
|-----------|-------|
| `iseoblog` | Only theme directory; custom templates for home/blog/tariff-calc/offer; template-parts for tariffs/calculator/footer/topbar |

---

## 5. Custom plugins (filesystem entries)

`advanced-custom-fields-pro-main`, `akismet`, `cyr2lat`, `disable-gutenberg`, `duplicate-page`, `jetpack`, `no-category-base-wpml`, `rate-my-post`, `simple-user-avatar`, `wordpress-plugin-autoVersion-master`, `wordpress-seo`, `wp-optimize`, `wp-simple-post-view`, plus `hello.php`.

**WPilot:** not present.

---

## 6. Custom tools / handlers

| Relative path pattern | Classification |
|----------------------|----------------|
| `calc__FORM.php` | SEO calculator mail/handler |
| `tariff_1__FORM.php` … `tariff_4__FORM.php` | Tariff lead handlers |
| `callback__FORM.php`, `audit__FORM.php`, `page__FORM.php`, … | Lead forms |
| `services/**/ *__FORM.php` | Per-section handler copies |
| `js/common.js` | Front-end calculator/tariffs/forms |
| `report-hub/*.html` | Report Hub static app |
| `varvara-new.php` | Custom PHP page (purpose SAFE UNKNOWN) |

---

## 7. Build / source candidates

| Candidate | Present in docroot? |
|-----------|---------------------|
| `package.json` | **No** |
| `gulpfile.*` | **No** |
| `src/` | **No** |
| `scss/` | **No** |
| `.git/` | **No** |
| `composer.json` (root) | **No** |

Production appears to be a **deployed runtime tree**, not a Node build workspace.

---

## 8. Rewrite / server config files

| File | Role |
|------|------|
| `.htaccess` | HTTPS, www redirect, UA block, HTML-as-PHP, WordPress rewrite |
| nginx configs | **Not visible** in docroot listing |

---

## 9. Protected zones (filesystem)

Treat as protected by default:

- `wp-config.php`
- `wp-content/debug.log`
- entire `wp-admin/`, `wp-includes/`
- `wp-content/plugins/`, `wp-content/themes/` outside exact future task scope
- all `*__FORM.php` handlers
- `.htaccess`
- `wp-content/uploads/` (except explicitly chartered media)
- database (not on filesystem as dump in this audit)

---

## 10. Excluded sensitive files (not copied / not quoted)

- `wp-config.php` secret defines (DB_*, keys, salts)
- Form handler recipient emails
- Any credentials under local `secrets.local.md`
- Full `debug.log`

---

*Remote filesystem inventory v1 · sanitized · 2026-07-24.*
