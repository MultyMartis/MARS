# METALLKA — Page Inventory v1

**Programme:** METALLKA-RU-SITE-OPS  
**Status:** POPULATED — Phase 2B  
**Date:** 2026-07-26  
**Note:** Practical inventory (not every historical DB revision). All inspected pages use template `default` + `_wpb_vc_js_status=true` unless noted.

---

## Published pages (core set)

| ID | Slug | URL | Parent | Status | Builder class | vc_row | vc_raw_html | cf7 in content | Notes |
|----|------|-----|--------|--------|---------------|--------|-------------|----------------|-------|
| 2 | home | `/` | 0 | publish | WPBakery | 2 | 2 | 0 | Front page |
| 41 | contacts | `/contacts/` | 0 | publish | WPBakery | 2 | 2 | 1 | Forms + map shortcodes likely |
| 52 | about | `/about/` | 0 | publish | WPBakery | 1 | **0** | 0 | Simple `vc_column_text` body |
| 77 | services | `/services/` | 0 | publish | WPBakery meta | 0 | 0 | 0 | Nearly empty content (hub) |
| 86 | remont-otverstij | `/services/remont-otverstij/` | 77 | publish | WPBakery complex | 12 | **7** | 1 | High `vc_raw_html` |
| 87 | tokarnye-raboty | `/services/tokarnye-raboty/` | 77 | publish | WPBakery complex | 11 | **7** | 1 | High `vc_raw_html` |
| 88 | frezernye-raboty | `/services/frezernye-raboty/` | 77 | publish | WPBakery complex | 11 | **7** | 1 | High `vc_raw_html` |
| 58 | requisites | `/requisites/` | 0 | publish | WPBakery | 1 | 1 | 0 | |
| 56 | mentions | `/about/mentions/` | 52 | publish | WPBakery | 1 | 0 | 0 | Has `dt_*` shortcode |
| 67 | gallery | `/about/gallery/` | 52 | publish | WPBakery meta | 0 | 0 | 0 | Empty-ish content |
| 27 | blog | `/blog/` | 0 | publish | WPBakery meta | 0 | 0 | 0 | Posts index page |
| 3 | privacy-policy | `/privacy-policy/` | 0 | publish | WPBakery text | 1 | **0** | 0 | Legal text in `vc_column_text` |
| 30 | user-agreement | `/user-agreement/` | 0 | publish | WPBakery | 1 | 0 | 0 | |
| 31 | cookie-files-policy | `/cookie-files-policy/` | 0 | publish | WPBakery text | 1 | **0** | 0 | Single text block |
| 353 | consent-personal-data | `/consent-personal-data/` | 0 | publish | WPBakery | 1 | 0 | 0 | |

## Non-public / other

| ID | Slug | Status | Notes |
|----|------|--------|-------|
| 235 | izgotovlenie-metallokonstrukcij | draft | Under services parent |
| 64 | portfolio | pending | |

---

## Representative classifications

### Low-complexity text pages (preferred write candidates later)

- **52 About** — one `vc_row` → `vc_column` → `vc_column_text` only; no `vc_raw_html`; no CF7  
- **31 Cookie policy** — same pattern  
- **3 Privacy policy** — `vc_column_text` with page-specific VC CSS attribute; no `vc_raw_html`

### High-complexity commercial pages

- **86 / 87 / 88** — many rows, multiple `vc_raw_html`, The7 `dt_*` elements, embedded CF7  

### Global / shared content (not page-local alone)

- Shortcoder: `footer_contacts` (50), `yandex_map` (48), `safe_mail-client` (45)  
- Popup Maker popup 83  
- Child footer legal links hard-coded in `sidebar-footer.php`

---

## Sitemap

- `https://metallka.ru/sitemap_index.xml` (Rank Math style)  
- Submaps: `post-sitemap.xml`, `page-sitemap.xml`, `category-sitemap.xml`

---

*Page Inventory v1 · do not save pages during discovery.*
