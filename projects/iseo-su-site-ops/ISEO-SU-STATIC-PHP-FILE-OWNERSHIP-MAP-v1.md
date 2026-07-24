# ISEO-SU STATIC PHP FILE OWNERSHIP MAP v1

**Programme:** ISEO-SU-SITE-OPS  
**Date:** 2026-07-24  

## Active root marketing HTML

| File | Public URL | Reachable | Class | Edit rule |
|------|------------|-----------|-------|-----------|
| `about.html` | `/about.html` | yes 200 | STATIC_HARDCODED | SFTP |
| `services.html` | `/services.html` | yes 200 (intermittent 500 once) | STATIC_HARDCODED | SFTP + re-validate |
| `contacts.html` | `/contacts.html` | yes | STATIC_HARDCODED | SFTP |
| `cases.html` | `/cases.html` | yes | STATIC_HARDCODED | SFTP |
| `reviews.html` | `/reviews.html` | yes | STATIC_HARDCODED | SFTP |
| `partners.html` | `/partners.html` | yes | STATIC_HARDCODED | SFTP |
| `bonuses.html` | `/bonuses.html` | yes | STATIC_HARDCODED | SFTP |
| `career.html` | `/career.html` | yes | STATIC_HARDCODED | SFTP |
| `guarantees.html` | `/guarantees.html` | yes | STATIC_HARDCODED | SFTP |
| `privacy-policy.html` | `/privacy-policy.html` | yes | STATIC_HARDCODED | SFTP |
| `user-agreement.html` | `/user-agreement.html` | yes | STATIC_HARDCODED | SFTP |
| `cookie-files-policy.html` | `/cookie-files-policy.html` | yes | STATIC_HARDCODED | SFTP |

## Legacy / parallel / special root HTML

| File | Role | Class | Edit rule |
|------|------|-------|-----------|
| `home.html` | Parallel homepage | LEGACY_OR_PARALLEL | Do not treat as live `/` |
| `blog.html` | Parallel blog mock | LEGACY_OR_PARALLEL | Do not treat as `/blog` |
| `blog-article.html` | Article mock | LEGACY_OR_PARALLEL | Avoid |
| `index.html_` | Renamed former index | LEGACY | Do not revive casually |
| `readme.html` | WP readme | leave | ignore |
| `google061534338ccd37c3.html` | Search verification | protect | do not delete |
| `yandex_2446617d33da4cfb.html` | Search verification | protect | do not delete |

## PHP handlers (mail)

| File | Purpose | Public | Edit rule |
|------|---------|--------|-----------|
| `calc__FORM.php` | SEO calculator lead | POST target | **PROTECTED** |
| `tariff_1__FORM.php` … `tariff_4__FORM.php` | Tariff leads | POST | **PROTECTED** |
| `callback__FORM.php` | Callback | POST | **PROTECTED** |
| `page__FORM.php` | Page form | POST | **PROTECTED** |
| `audit__FORM.php` | Audit form | POST | **PROTECTED** |
| `bonus__FORM.php` | Bonus | POST | **PROTECTED** |
| `career__FORM.php` | Career | POST | **PROTECTED** |
| `partners__FORM.php` | Partners | POST | **PROTECTED** |
| `review__FORM.php` | Review | POST | **PROTECTED** |

**Copies:** identical filename sets under `services/seo|adv|audit|development|serm|ai-optimization/`. Drift risk **HIGH**.

## Other PHP

| File | Role | Class |
|------|------|-------|
| `index.php` | WP bootstrap | WORDPRESS core path |
| `varvara-new.php` | VVR-Searcher | STATIC_HARDCODED / tool |
| `wp-config.php` | WP config | **PROTECTED** — never casual |

## Shared includes

Marketing HTML generally **does not** PHP-include shared partials (no `include` found in sampled about/contacts/home). Chrome is **duplicated markup**. Theme WP surfaces use `get_header` / `get_template_part`.

## Directories

| Dir | Ownership |
|-----|-----------|
| `services/` | STATIC_HARDCODED tree |
| `cases/` | STATIC_HARDCODED tree |
| `css/`, `js/`, `libs/`, `img/`, `fonts/`, `favicon/` | SHARED assets |
| `report-hub/`, `reports/` | EXTERNAL_SIBLING / artifacts |
| `docs/`, `video/` | static assets |
| `wp-admin/`, `wp-includes/`, `wp-content/` | WordPress |

## Public reachability rule

Physical file presence ⇒ Apache serves file (HTML may run as PHP). Absence ⇒ WordPress rewrite.

---

*Static PHP file ownership map v1 · 2026-07-24.*
