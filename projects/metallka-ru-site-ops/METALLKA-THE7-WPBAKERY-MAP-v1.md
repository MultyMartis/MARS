# METALLKA — The7 / WPBakery Map v1

**Programme:** METALLKA-RU-SITE-OPS  
**Status:** POPULATED — Phase 2B  
**Date:** 2026-07-26

---

## Stack versions

| Component | Version / path |
|-----------|----------------|
| The7 parent | `dt-the7` **11.6.0.1** |
| Child | `dt-the7-child` / header name `the7dtchild` **1.0.0** |
| WPBakery | `js_composer` **6.10.0** |
| Ultimate Addons | 3.19.14 |
| RevSlider | 6.6.7 |

---

## Which pages use WPBakery?

**All inspected published pages** carry `_wpb_vc_js_status=true` and template `default`.

Ordinary block/classic editor-only pages were **not** found in the core commercial/legal set.

### `vc_raw_html` present

| Page | Count (approx) |
|------|----------------|
| home (2) | 2 |
| contacts (41) | 2 |
| requisites (58) | 1 |
| service pages 86/87/88 | **7 each** |

### No `vc_raw_html` (text-oriented)

About (52), privacy (3), cookie (31), consent (353), user-agreement (30), mentions (56) — among inspected set.

### The7 shortcodes (`dt_*`)

Present on service pages and mentions; not on the simple about/legal text pages inspected.

### Custom / nested shortcodes

- CF7 `[contact-form-7 ...]` on contacts + service pages  
- Shortcoder snippets referenced from layouts/widgets  
- Ultimate / RevSlider generators present site-wide as plugins

---

## Ownership map (evidence-based)

| Surface | Owner class | Evidence |
|---------|-------------|----------|
| Header / main nav placement | **THE7 THEME OPTION** (+ WP menus) | The7 locations `primary`/`mobile`; options blob `the7dtchild` (956 keys); no child `header.php` override |
| Mobile navigation | **THE7 THEME OPTION** + menu `mobilnoe-menju` @ `mobile` | Menu locations list |
| Footer chrome | **THE7 THEME OPTION** + **CHILD THEME FILE** | Child `footer.php`, `sidebar-footer.php` overrides; legal notice HTML in child sidebar-footer |
| Logo | **THE7 THEME OPTION** (expected) | Options present; no child logo PHP — treat as Theme Options until a write charter inspects UI |
| Page layout shell | **THE7 THEME OPTION** / templates | Standard The7 wrappers in child footer |
| Sidebars / footer widgets | **THE7 THEME OPTION** + widgets | `presscore_*` widget options; `footer_widgetarea_id` via theme config |
| Global typography / colors | **THE7 THEME OPTION** | Generated `uploads/the7-css/*` |
| The7 Theme Options | **THE7 THEME OPTION** | Option `the7dtchild` |
| Page-specific The7 meta | **THE7 POST META** | `_dt_*` / related keys present on multiple pages |
| Page body composition | **WPBAKERY** | `post_content` shortcodes + `_wpb_vc_js_status` |
| Custom CSS (child) | **CHILD THEME FILE** | `dt-the7-child/style.css` (`WSP Fixes`) |
| WP Customizer additional CSS | Empty / none returned | WP-CLI `wp_get_custom_css` empty |
| Reusable HTML snippets | **PLUGIN** (Shortcoder) | CPT shortcoder posts |
| Popups | **PLUGIN** (Popup Maker) | CPT popup |
| Forms | **PLUGIN** (CF7) | CPT `wpcf7_contact_form` |

---

## Safe admin-owned vs protected

| Surface | Posture |
|---------|---------|
| Single-page `vc_column_text` on non-global legal/about pages | **MAPPED** — still requires exact write charter; lowest-risk class |
| `vc_raw_html` blocks | **PROTECTED** |
| Header / footer / Theme Options / menus / forms | **PROTECTED** |
| Child theme PHP/CSS | **PROTECTED** |
| Service landing WPBakery graphs | **PROTECTED** (complexity + raw HTML + forms) |

---

*The7 / WPBakery Map v1 · ownership by evidence, not analogy.*
