# METALLKA — Protected Zones v1

**Programme:** METALLKA-RU-SITE-OPS  
**Status:** UPDATED after Phase 2B mapping  
**Date:** 2026-07-26  
**Site:** `metallka.ru`  
**Discovery status:** **PERFORMED** (read-only)

---

## Classification rule

```text
MAPPED ≠ WRITE AUTHORIZED
```

Surfaces may be **MAPPED** with known owner while remaining **PROTECTED** until an exact HITL write charter names the object, rollback, and acceptance criteria.

---

## Zone table

| # | Surface | Posture | Owner (if mapped) | Notes |
|---|---------|---------|-------------------|-------|
| 1 | `wp-config.php` | **PROTECTED** | WORDPRESS CORE / hosting | Never dump secrets |
| 2 | `.htaccess` / server configuration | **PROTECTED** | WORDPRESS CORE (+ hosting) | Standard WP rewrite mapped |
| 3 | Parent The7 theme | **PROTECTED** | THE7 vendor | Do not edit parent |
| 4 | Child theme | **PROTECTED** / **MAPPED** | CHILD THEME FILE | functions/style/footer/sidebar-footer known |
| 5 | `functions.php` (child) | **PROTECTED** / **MAPPED** | CHILD THEME FILE | |
| 6 | Theme template overrides | **PROTECTED** / **MAPPED** | CHILD THEME FILE | footer + sidebar-footer |
| 7 | The7 Theme Options | **PROTECTED** / **MAPPED** | THE7 THEME OPTION (`the7dtchild`) | |
| 8 | The7 postmeta | **PROTECTED** / **MAPPED** | THE7 POST META | Present on many pages |
| 9 | Header | **PROTECTED** / **MAPPED** | THE7 THEME OPTION + menus | |
| 10 | Footer | **PROTECTED** / **MAPPED** | THE7 + CHILD THEME FILE + Shortcoder | |
| 11 | Menus | **PROTECTED** / **MAPPED** | WORDPRESS CORE menus / The7 locations | |
| 12 | Forms | **PROTECTED** / **MAPPED** | PLUGIN (CF7+) | |
| 13 | SMTP | **PROTECTED** | UNKNOWN / hosting mail | No SMTP plugin |
| 14 | Custom plugins | **PROTECTED** / **MAPPED** | PLUGIN (`css-versioning`, etc.) | |
| 15 | MU plugins | **N/A** | — | None present |
| 16 | Code Snippets | **N/A** | — | None present |
| 17 | ACF schema | **N/A** | — | ACF absent |
| 18 | ACF options | **N/A** | — | |
| 19 | `vc_raw_html` | **PROTECTED** / **MAPPED** | WPBAKERY | Confirmed on key pages |
| 20 | Unknown WPBakery / custom shortcodes | **PROTECTED** / **PARTIAL** | MIXED | `dt_*`, Ultimate, Shortcoder |
| 21 | WPBakery global templates | **PROTECTED** | UNKNOWN residual | Not fully inventorying VC templates library |
| 22 | Reusable / global blocks | **PROTECTED** / **MAPPED** | PLUGIN Shortcoder + Popup Maker | |
| 23 | Redirects | **PROTECTED** | `.htaccess` standard only mapped | |
| 24 | SEO global settings | **PROTECTED** / **MAPPED** | PLUGIN Rank Math | |
| 25 | Cron | **PROTECTED** | Hosting / WP | User crontab empty |
| 26 | External APIs / webhooks | **PROTECTED** | PARTIAL | |
| 27 | Analytics injection | **PROTECTED** / **PARTIAL** | Clearfy options exist; home HTML needles 0 | |
| 28 | DB schema | **PROTECTED** | WORDPRESS CORE | |
| 29 | Users / auth | **PROTECTED** | WORDPRESS CORE | 2 administrators |
| 30 | Production media deletion | **PROTECTED** | — | |
| 31 | Cache / optimization configuration | **PROTECTED** / **MAPPED** | Clearfy + The7 CSS | No purge without charter |

### Lowest-risk future write class (still chartered)

| Surface | Posture |
|---------|---------|
| Page **52** About — single non-global `vc_column_text` | **MAPPED** candidate for Phase 3A charter — **NOT** authorized now |

---

*Protected Zones v1 · mapped where evidenced · writes still denied by default.*
