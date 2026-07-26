# METALLKA — WP Entity Map v1

**Programme:** METALLKA-RU-SITE-OPS  
**Status:** POPULATED — Phase 2B  
**Date:** 2026-07-26

Connects public URL → WordPress object → template → builder → ownership → dependencies.

---

## Front & commercial

| URL | WP object | Template | Builder | Theme/meta ownership | Dependencies |
|-----|-----------|----------|---------|----------------------|--------------|
| `/` | page **2** `home` | default | WPBakery | The7 page meta + Theme Options chrome | RevSlider / Ultimate possible; `vc_raw_html`×2 |
| `/services/` | page **77** | default | WPBakery meta (empty body) | The7 | Children 86–88 |
| `/services/remont-otverstij/` | page **86** | default | WPBakery complex | The7 meta + WPBakery | CF7; `dt_*`; `vc_raw_html`×7 |
| `/services/tokarnye-raboty/` | page **87** | default | WPBakery complex | same | same |
| `/services/frezernye-raboty/` | page **88** | default | WPBakery complex | same | same |
| `/about/` | page **52** | default | WPBakery simple text | The7 meta + WPBakery text | None form |
| `/about/mentions/` | page **56** | default | WPBakery | The7 + `dt_*` | |
| `/about/gallery/` | page **67** | default | WPBakery meta | The7 | Empty-ish |
| `/contacts/` | page **41** | default | WPBakery | The7 + WPBakery | CF7; Shortcoder map/mail; `vc_raw_html` |
| `/requisites/` | page **58** | default | WPBakery | The7 + WPBakery | `vc_raw_html` |
| `/blog/` | page **27** | default | WPBakery meta | The7 | Posts loop |

## Legal

| URL | WP object | Builder | Notes |
|-----|-----------|---------|-------|
| `/privacy-policy/` | page **3** | WPBakery `vc_column_text` | Linked from child footer |
| `/user-agreement/` | page **30** | WPBakery | Footer legal |
| `/cookie-files-policy/` | page **31** | WPBakery text | Footer legal |
| `/consent-personal-data/` | page **353** | WPBakery | Footer legal |

## Global entities

| Entity | Type | IDs / names | Used by |
|--------|------|-------------|---------|
| Primary menu | nav_menu | term 2 `glavnoe-menju` @ `primary` | Header |
| Mobile menu | nav_menu | term 6 `mobilnoe-menju` @ `mobile` | Mobile header |
| Footer menu | nav_menu | term 5 (no location assigned) | Possibly widgets / unused location |
| CF7 forms | `wpcf7_contact_form` | 80, 81, 101, 290, 291, 292 | Contacts / services / popups |
| Shortcoder | `shortcoder` | 45 mail, 48 map, 50 footer contacts | Footer / contacts |
| Popup | `popup` | 83 | CTA call request |

---

*WP Entity Map v1.*
