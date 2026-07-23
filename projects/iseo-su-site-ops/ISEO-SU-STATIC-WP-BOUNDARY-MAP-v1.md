# ISEO-SU STATIC / WORDPRESS BOUNDARY MAP v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** PHASE 2B  
**Date:** 2026-07-24  

Classification vocabulary:

- **WORDPRESS_OWNED**
- **STATIC_FILE_OWNED** (includes PHP-capable `.html` on this host)
- **SHARED_BUT_WORDPRESS_RENDERED**
- **SHARED_BUT_STATIC_RENDERED**
- **EXTERNAL_TOOL**
- **SAFE_UNKNOWN**

---

## Route / component map

| Route / component | Classification | Notes |
|-------------------|----------------|-------|
| `https://i-seo.su/` | SHARED_BUT_WORDPRESS_RENDERED | WP page `glavnaya` + template `page-home.php` hardcoded static-like HTML + `/css` `/js` |
| `/home.html` | STATIC_FILE_OWNED | Parallel physical file; drift risk vs `/` |
| `/blog/`, `/blog` | WORDPRESS_OWNED | Generator WordPress 7.0.2; theme assets |
| `/blog.html` | STATIC_FILE_OWNED | Parallel file; not live blog renderer |
| `/tariff-calc` | WORDPRESS_OWNED | WP page + `page-tariffcalc.php` |
| `/offers` | WORDPRESS_OWNED | WP page; related CPT `offer` |
| `/offer/*` (robots disallow) | WORDPRESS_OWNED (likely) | CPT singles via `single-offer.php` |
| Root marketing `*.html` (`about`, `contacts`, `services`, …) | STATIC_FILE_OWNED | Physical files; PHP-capable via AddType |
| `/services/**/*.html` | STATIC_FILE_OWNED | Large service tree |
| `/cases/**/*.html` | STATIC_FILE_OWNED | Case studies |
| `/report-hub/**` | EXTERNAL_TOOL / STATIC_FILE_OWNED | Separate report HTML app |
| `/reports/**` | STATIC_FILE_OWNED | Report HTML artifacts |
| Shared `css/`, `js/`, `libs/`, `img/`, `fonts/` | SHARED_BUT_STATIC_RENDERED | Consumed by static pages and WP templates that hardcode paths |
| Theme `header.php` / `footer.php` / template-parts chrome | WORDPRESS_OWNED | Used by WP-rendered templates that call them |
| SEO calculator UI on marketing pages | SHARED_BUT_STATIC_RENDERED | `js/common.js` + page markup |
| SEO calculator on WP tariff page / theme parts | SHARED_BUT_WORDPRESS_RENDERED | Theme template-parts + WP page |
| `calc__FORM.php` / `tariff_*__FORM.php` / other `*__FORM.php` | STATIC_FILE_OWNED | PHP mail handlers (not WP forms) |
| `wp-admin/`, REST authenticated admin | WORDPRESS_OWNED | Admin UI challenge for non-browser clients |
| Web-KP tool | SAFE_UNKNOWN | No dedicated route found; candidates: `/offers` + CPT `offer` |
| `varvara-new.php` | SAFE_UNKNOWN | Custom PHP |
| `sitemap-static.xml` | STATIC_FILE_OWNED | Static URL inventory |
| `sitemap.xml` | SAFE_UNKNOWN | May be WP/Yoast or static — not fully classified |

---

## Ownership rules of thumb

1. If a physical file exists at the request path → static/PHP file wins (Apache + WP `!-f`).
2. If no file/dir → WordPress front controller.
3. `.html` may execute PHP includes — do not assume “pure static”.
4. Do not edit theme chrome assuming it updates all marketing HTML (and vice versa).

---

*Boundary map v1 · 2026-07-24.*
