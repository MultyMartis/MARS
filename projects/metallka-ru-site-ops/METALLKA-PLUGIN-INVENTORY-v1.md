# METALLKA — Plugin Inventory v1

**Programme:** METALLKA-RU-SITE-OPS  
**Status:** POPULATED — Phase 2B  
**Date:** 2026-07-26  
**Source:** SSH WP-CLI `plugin list` + filesystem `wp-content/plugins`

---

## Active plugins

| Slug / directory | Version | Role class | Notes |
|------------------|---------|------------|-------|
| `js_composer` | **6.10.0** | Page builder (WPBakery) | Update available → 8.7.4 (do **not** update in this phase) |
| `Ultimate_VC_Addons` | 3.19.14 | WPBakery addons | |
| `revslider` | **6.6.7** | Sliders | |
| `contact-form-7` | 6.1.4 | Forms | |
| `contact-form-7-honeypot` | 3.4.0 | Form spam protection | |
| `contact-form-cfdb7` | 1.3.5 | Form submissions DB storage | |
| `popup-maker` | 1.21.5 | Popups | At least popup ID 83 |
| `seo-by-rank-math` | 1.0.263 | SEO | |
| `clearfy` | 2.4.1 | Optimization / hardening / analytics helpers | Active; many `wbcr_clearfy_*` options |
| `media-file-renamer` | 6.2.0 | Media SEO rename | |
| `shortcoder` | 6.5.1 | Reusable shortcodes | IDs 45, 48, 50 |
| `duplicate-page` | 4.5.6 | Admin utility | |
| `duplicate-menu` | 0.2.3 | Admin utility | |
| `classic-widgets` | 0.3 | Widgets compatibility | |
| `advanced-database-cleaner` | 4.0.6 | DB maintenance | |
| `css-versioning` | 1.1 | Asset cache-bust helper | Custom/small |
| `underconstruction` | 1.22 | Maintenance plugin | **Active** but public site returns 200 — display likely off |

---

## Inactive (material)

| Slug | Version | Notes |
|------|---------|-------|
| `fast-velocity-minify` | 3.5.4 | Inactive; leftover cache under `wp-content/cache/fvm` |
| `seo-by-rank-math-pro` | 3.0.32.1 | Inactive |

---

## MU plugins / drop-ins

| Item | Status |
|------|--------|
| MU plugins directory | **NOT PRESENT** / empty (`NO_MU`) |
| `advanced-cache.php` | **NO** |
| `object-cache.php` | **NO** |
| Other drop-ins | Only default `wp-content/index.php` |

---

## Not present (explicit)

| Class | Status |
|-------|--------|
| ACF / ACF PRO / ACF Extended | **NOT PRESENT** |
| Code Snippets plugin | **NOT PRESENT** |
| Dedicated SMTP plugin | **NOT PRESENT** |
| Wordfence / Sucuri / similar security suite | **NOT PRESENT** as dedicated dirs |
| WPilot / metacode-wpilot | **NOT PRESENT** |

---

## WPilot presence check

| Check | Result |
|-------|--------|
| WP Admin / plugin list name | Absent |
| Plugin directory | Absent (`find` / `ls` no `*wpilot*`) |
| `wpilot_options` | **ABSENT** |
| WPilot DB tables | None matched |
| REST namespace `wpilot/v1` | **Not** in public `/wp-json/` namespaces |
| Ghost / duplicate dirs | **None found** |

---

## Custom / small plugins

- `css-versioning` — present, active, version 1.1  
- Child-theme JS mask helpers are **theme**, not plugins  

---

*Plugin Inventory v1 · read-only · no activation changes.*
