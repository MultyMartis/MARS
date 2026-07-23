# ISEO-SU WORDPRESS INVENTORY v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** PHASE 2B  
**Date:** 2026-07-24  
**Methods:** SFTP filesystem + public REST API (`/wp-json/`). WordPress Admin UI via non-browser HTTP client was blocked by a JS challenge shell.

No usernames, passwords, tokens, or DB secrets.

---

## 1. Core

| Field | Value | Evidence |
|-------|-------|----------|
| WordPress | **7.0.2** | `wp-includes/version.php`; `/blog/` meta generator |
| Required PHP (core) | **≥ 7.4** | `version.php` `$required_php_version` |
| PHP runtime (host) | **SAFE UNKNOWN** | Site Health Admin UI inaccessible via HTTP client |
| Multisite | No | `wp-config` metadata |
| Table prefix | `wp_` | `wp-config` metadata only |
| WP_DEBUG | `true` | `wp-config` metadata |
| Site title (REST) | INTLSEO Studio | `/wp-json/` |
| URL / Home | `https://i-seo.su` | REST |

---

## 2. Reading / front settings

| Field | Value |
|-------|-------|
| `show_on_front` | `page` |
| Front page | id **1732**, slug `glavnaya`, title «Главная», template **`page-home.php`**, link `https://i-seo.su/` |
| `page_for_posts` | `0` (not set) |
| Blog WP page | id **1730**, slug `blog`, template **`page-blog.php`**, link `https://i-seo.su/blog` |
| Tariff calc page | id **1734**, slug `tariff-calc`, template **`page-tariffcalc.php`** |
| Offers page | id **1377**, slug `offers`, link `https://i-seo.su/offers` |

Public REST returned **4** pages total in the unauthenticated pages collection (may omit private/draft).

---

## 3. Active theme / child

| Field | Value |
|-------|-------|
| Theme directory | `iseoblog` |
| Child theme | **No** |
| Parent | n/a |
| Other themes on disk | **None** |
| Builder (WPBakery/The7) | **Not found** |

---

## 4. Plugins (filesystem)

| Entry | Plugin name | Version |
|-------|-------------|---------|
| advanced-custom-fields-pro-main | Advanced Custom Fields PRO | 6.3.10 |
| wordpress-seo | Yoast SEO | 28.0 |
| jetpack | Jetpack | 14.8 |
| wp-optimize | WP-Optimize | 4.5.5 |
| akismet | Akismet Anti-spam | 5.3.6 |
| cyr2lat | Cyr-To-Lat | 6.3.0 |
| disable-gutenberg | Disable Gutenberg | 3.2.2 |
| duplicate-page | Duplicate Page | 4.5.4 |
| rate-my-post | FeedbackWP - Rate My Post | 4.3.0 |
| wp-simple-post-view | Post View Count | 2.0.2 |
| simple-user-avatar | Simple User Avatar | 4.7 |
| no-category-base-wpml | No Category Base (WPML) | 1.5.4 |
| wordpress-plugin-autoVersion-master | Auto Version | 1.1.0 |
| hello.php | Hello Dolly | 1.7.2 |

**MU-plugins:** none listed.

**Active state:** exact on/off matrix **SAFE UNKNOWN** (Admin plugins screen not readable via HTTP client).  
**Live REST namespaces observed:** `yoast/v1`, multiple `jetpack/*` (+ boost/my-jetpack) — strong evidence Yoast + Jetpack are operational.

---

## 5. CPT / taxonomies

| Kind | Items |
|------|-------|
| Theme-registered CPT | `offer` (`single-offer.php`) |
| REST public types | `post`, `page`, `attachment`, `nav_menu_item`, block/template types |
| Taxonomies | `category`, `post_tag`, `nav_menu`, `wp_pattern_category` |

Note: `offer` did not appear in the public `wp/v2/types` map during this audit (may be non-public REST or differently exposed) — filesystem registration still confirmed.

---

## 6. ACF

| Field | Value |
|-------|-------|
| ACF PRO on disk | Yes 6.3.10 |
| acf-json | **Not found** |
| Field groups / options | **SAFE UNKNOWN** (Admin UI gap) |

---

## 7. Menus / widgets

| Field | Value |
|-------|-------|
| Menus | **SAFE UNKNOWN** (Admin UI gap; REST menu item type exists) |
| Widgets | **SAFE UNKNOWN** |

---

## 8. Blog settings

| Field | Value |
|-------|-------|
| Blog archive UI | `/blog/` WordPress-rendered |
| Categories | REST list collected (counts available in scratch evidence; not all reprinted) |
| Permalink style | postname-like public URLs (example from REST post links) |

---

## 9. Cache / security / mail components

| Component | Presence |
|-----------|----------|
| Yoast SEO | Present (REST + files) |
| Jetpack | Present (REST + files) |
| WP-Optimize | Present on disk (cache/clean/compress) |
| Akismet | Present on disk |
| Dedicated SMTP plugin | **Not identified** by name |
| WAF notes | `wp-content/jetpack-waf/` directory present |

---

## 10. WPilot

| Field | Value |
|-------|-------|
| Present on disk | **No** |
| Present in REST namespaces | **No** |
| Token | **Not created** |

---

## 11. Admin UI access note

Non-browser HTTP requests to `/wp-admin/*` after credentialed login attempt returned a minimal HTML+script challenge (~273 bytes) without `#adminmenu`.  

**Implication:** Admin-only screens (exact plugin actives, Site Health PHP version, menus, ACF UI) require operator browser HITL or a future Browser Workstation charter.

Dedicated MARS WordPress administrator account: **configured locally** (`wordpress_dedicated_mars_account: yes`) — username not recorded here.

---

*WordPress inventory v1 · 2026-07-24 · no secrets.*
