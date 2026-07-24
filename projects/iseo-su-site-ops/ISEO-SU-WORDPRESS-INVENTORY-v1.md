# ISEO-SU WORDPRESS INVENTORY v1

**Programme:** ISEO-SU-SITE-OPS  
**Origin:** PHASE 2B  
**Updated:** 2026-07-24 architecture knowledge capture  
**Methods:** public REST + Playwright Admin read-only + SFTP  

No usernames, passwords, tokens, or DB secrets.

---

## 1. Core

| Field | Value |
|-------|-------|
| WordPress | **7.0.2** |
| PHP runtime | **SAFE UNKNOWN** (Site Health scrape inconclusive) |
| Multisite | No |
| Table prefix | `wp_` |
| WP_DEBUG | `true` (metadata) |
| Site title | INTLSEO Studio |
| URL / Home | `https://i-seo.su` |

## 2. Reading / front

| Field | Value |
|-------|-------|
| `show_on_front` | `page` |
| Front page | 1732 `glavnaya` / `page-home.php` / `/` |
| `page_for_posts` | not set |
| Blog page | 1730 `blog` / `page-blog.php` / `/blog` |
| Tariff page | 1734 `tariff-calc` / `page-tariffcalc.php` |
| Offers page | 1377 `offers` / default template |
| Permalink | `/blog/%postname%.html` |

## 3. Theme

| Field | Value |
|-------|-------|
| Theme | `iseoblog` only |
| Child | No |

## 4. Plugins — active / inactive (Admin confirmed)

**Active:** ACF PRO, Auto Version, Cyr-To-Lat, Disable Gutenberg, Duplicate Page, FeedbackWP Rate My Post, Jetpack, MetaCODE WPilot, Post View Count, Simple User Avatar, Yoast SEO.

**Inactive:** Akismet, Hello Dolly, No Category Base (WPML), WP-Optimize.

## 5. CPT / taxonomies

| Kind | Items |
|------|-------|
| CPT | `offer` (public, has_archive, Admin UI; REST type not public) |
| Taxonomies | category, post_tag, nav_menu, …

## 6. ACF

| Group ID | Title |
|----------|-------|
| 19 | Записи |
| 1761 | Настройки калькулятора |
| 1742 | Настройки каналов и тарифов |
| 1382 | Предложения |

`acf-json`: not found. Options page registration in theme: not found.

## 7. Menus

Primary location `menu-1`; menu name «Меню 1». Theme topbar also hardcodes links.

## 8. WPilot

Active RC6; bridge/writes off; token local-only; public namespace `wpilot/v1` registered; REST not invoked in this task.

## 9. Detail authority

[ISEO-SU-WORDPRESS-OBJECT-AND-TEMPLATE-MAP-v1.md](ISEO-SU-WORDPRESS-OBJECT-AND-TEMPLATE-MAP-v1.md)

---

*WordPress inventory v1 · updated 2026-07-24.*
