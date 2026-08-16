# REPORT — FP-0002 V9-07A01 Program Auto-Source and Comfort Gallery Fix

**Date:** 2026-07-23  
**Status:** PASS (local validation) — operator review pending  
**Release class:** post–Stable v1 correction wave (does **not** replace Stable v1 freeze)  
**Commit / push / freeze:** none

---

## 1. Status

| Gate | Result |
|------|--------|
| Overall | **PASS** |
| Operator review | pending |
| DB content writes (lasting) | **0** |
| Reversible validation writes | temporary title/desc probe on #1054 — restored |
| Cache | `wp_cache_flush()` once after delivery |
| Commit / push / freeze | **none** |

---

## 2. Pre-Change Backup

- **Path:** `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-07a01-before-program-auto-source-comfort-gallery-fix-20260723-214353`
- **DB dump:** `db/mars_wp_fp0002.sql` (SHA256 `43E5A754…`, ~6.5 MB)
- **Validation:** `BACKUP-OK.txt`, `BACKUP-INFO.md`, `hashes.csv`, `operator-change-manifest.csv`
- **Scope:** exact theme/plugin/ACF candidates + DB (not a Stable freeze)

---

## 3. Latest Operator Changes Canonized

| Check | Result |
|-------|--------|
| Theme source↔runtime | **MATCH** (only runtime-only `sergey-shpigovsky-interview.mp4.BROKEN-MPEGTS.bak`) |
| Plugin | **MATCH** |
| Operator CSS/HTML promote | **none required** |
| Unresolved drift | bak file only (ignored) |

---

## 4. Program Content Model Audit

| Item | Value |
|------|-------|
| Parent | `#13` `/o-centre/programma-lecheniya/` |
| Children | `#1053` genotipirovanie; `#1054` prostranstvo-vosstanovleniya; `#1055` psihokorrektsiya; `#1056` kinezioterapiya |
| Order | `menu_order ASC`, then `ID ASC` |
| Previous ownership | hardcoded slug/title map + O-centre `about_program_items` + service `programme_items` |

**Stale sources found**

1. `program-direction-helpers.php` definitions keyed by old slug `neyropsihologicheskaya-korrektsiya` + hardcoded titles  
2. O-centre ACF repeater `about_program_items` titles  
3. Service ACF repeater `programme_items_*_title` on many service posts (read by subdivision/leaf templates)

---

## 5. Renamed Page Repair

| Field | Value |
|-------|-------|
| Page ID | **1054** |
| Old title / slug | Нейропсихологическая коррекция / `neyropsihologicheskaya-korrektsiya` |
| Current title / slug | **Пространство восстановления** / `prostranstvo-vosstanovleniya` |
| Mini-description | child ACF `treatment_program_short_description` |
| Routes corrected | `/`, `/o-centre/`, `/uslugi/`, `/uslugi/zavisimosti/`, service program/approach blocks |

Old slug URL now correctly **404**. Child permalinks **200**.

---

## 6. O-centre Admin Ownership

| Item | Action |
|------|--------|
| Duplicate card fields | `about_program_items` (title/image) |
| Hidden | wrapper `fp02-acf-legacy-retired` + message note |
| Retained page fields | `about_program_heading`, `lead`, `intro`, `intro2` |
| Dormant metadata | existing `about_program_items_*` postmeta **not deleted** |
| Final card source | live children of #13 |

Service `programme_items` admin fields were **not** restructured (E62C Service ACF boundary). Frontend **stopped reading** them for program cards; postmeta remain dormant.

---

## 7. Program Auto-Source Implementation

- **Helper:** `inc/program-direction-helpers.php`
- **Title:** `get_the_title( $child )`
- **Permalink:** `get_permalink( $child )`
- **Mini-description:** `get_field( 'treatment_program_short_description', $child_id )`
- **Ordering:** `menu_order ASC`, `ID ASC`
- **Visual meta only:** marker/image assets keyed by page ID (1053–1056)
- **Fallback:** empty list if no published children (no stale title array)

Also wired:

- `institutional-helpers.php` → always auto-source items  
- `service/program.php` + `service/approach.php` → auto-source  
- `service-helpers.php` fallbacks → auto-source  

---

## 8. Program Validation

| Check | Result |
|-------|--------|
| Routes | old title/slug **absent** on Home / O-centre / Услуги / Зависимости |
| Edit propagation | temp title+desc on #1054 appeared on Home (+ desc) and all title routes; restored |
| Child links | four children **200**; old slug **404** |
| Viewports | gallery screenshots 1440 + 480; program HTML independent of viewport |

---

## 9. Comfort Gallery Root Cause

| Item | Finding |
|------|---------|
| Affected | `/uslugi/`, `/uslugi/zavisimosti/` |
| Working comparison | Home / O-centre already enqueued Fancybox |
| DOM | E59 structure OK: decor outside `.comfort__gallery`; 6 clickable items |
| Root cause | **Fancybox vendor not enqueued** on hub/subdivision/leaf (only Swiper) while `v9-shell.js` init silently no-ops without `window.Fancybox` |
| Console | no JS exceptions after fix |

---

## 10. Comfort Gallery Fix

| File | Change |
|------|--------|
| `inc/fancybox-vendors.php` | **new** shared idempotent Fancybox enqueue helper |
| `services-hub-vendors.php` | call helper |
| `service-subdivision-vendors.php` | call helper |
| `alcohol-direct-v9-vendors.php` | call helper |
| `functions.php` | require fancybox helper |
| `assets/js/v9-shell.js` | bind `.comfort__gallery [data-fancybox]`; idempotent boot; keep O-centre infrastructure bind |

Decor remains outside gallery (E59-FIX01 preserved).

---

## 11. Gallery Validation

| Route | Clickable | Open | Nav | Close | Escape | Mobile open | Overflow | Errors |
|-------|-----------|------|-----|-------|--------|-------------|----------|--------|
| `/uslugi/` | 6 | PASS | PASS | PASS | PASS | PASS | 0 | 0 |
| `/uslugi/zavisimosti/` | 6 | PASS | PASS | PASS | PASS | PASS | 0 | 0 |
| `/` (smoke) | 6 | PASS | PASS | PASS* | PASS* | PASS | 0 | 0 |
| opium individual service | 6 | PASS | — | PASS | PASS | — | 0 | 0 |

\*Home close/escape confirmed via close-probe selectors (`[data-fancybox-close]` / Escape).

Note: alcohol leaf `#74` currently has **no Comfort markup** (content toggle) — not a JS regression.

---

## 12. Database Changes

| Write | Detail |
|-------|--------|
| Lasting content | **0** |
| Validation | temporary `#1054` title/desc update → restored |
| Cache | `wp_cache_flush()` |
| Legacy postmeta | retained (`about_program_items`, `programme_items`) |

---

## 13. Exact Files Changed

### Source (`WORDPRESS/`)

- `theme/shpigovsky/inc/program-direction-helpers.php`
- `theme/shpigovsky/inc/institutional-helpers.php`
- `theme/shpigovsky/inc/service-helpers.php`
- `theme/shpigovsky/inc/institutional-about-v9-content.php`
- `theme/shpigovsky/inc/fancybox-vendors.php` (**new**)
- `theme/shpigovsky/inc/services-hub-vendors.php`
- `theme/shpigovsky/inc/service-subdivision-vendors.php`
- `theme/shpigovsky/inc/alcohol-direct-v9-vendors.php`
- `theme/shpigovsky/functions.php`
- `theme/shpigovsky/assets/js/v9-shell.js`
- `theme/shpigovsky/template-parts/service/program.php`
- `theme/shpigovsky/template-parts/service/approach.php`
- `plugins/shpigovsky-core/src/Fields/FieldGroups.php`
- `acf-json/group_fp02_page_ocentre_hub.json`

### Runtime

Exact copies of the above under `wp-content/themes/shpigovsky/`, `plugins/shpigovsky-core/`, `wp-content/acf-json/`.

### Reports / evidence / docs

- this report  
- `REPORTS/evidence/v9-07a01-program-auto-source-comfort-gallery-fix/`  
- `PROJECT-STATUS.md`  
- `DOCS/TREATMENT-PROGRAM-AUTO-SOURCE-OWNERSHIP-v1.md`  
- Forge Phase 3 backlog lesson  

---

## 14. Source-to-Runtime Delivery

All listed files: **source SHA256 == runtime SHA256** (see evidence `source-runtime-hashes-after.csv`). Exact-file only; operator CSS preserved; no broad sync.

---

## 15. Regression

HTTP smoke matrix: expected statuses; PHP noise **0**; old program title **absent**; Search/404/Blog/Reviews/Contacts **200/404** as expected. Shared shell (header/footer/phone/lifebuoy) untouched in this wave.

---

## 16. Risks and Tails

1. **Legacy O-centre / service programme postmeta** still in DB — dormant; do not mass-delete without charter.  
2. **New Program children** auto-appear; visual marker/image requires adding page-ID visual meta (or later ACF icon field).  
3. **Fancybox lifecycle** still page-scoped enqueue — any new template reusing Comfort must call `shpigovsky_enqueue_fancybox_vendor()`.  
4. **Stable v1 freeze unchanged** — this is a correction wave, not a new freeze.  
5. Optional later: hide/retire service `programme_items` in admin (out of E62C-hidden-group scope this wave).  
6. Temp Playwright `node_modules` may remain under runtime project root if install left packages — not part of delivery; do not commit.

---

## 17. Git Status

- **no commit**
- **no push**
- **no freeze**
- foreign WIP untouched

---

## 18. Operator Review

### Frontend

- http://shpigovsky.test/  
- http://shpigovsky.test/o-centre/  
- http://shpigovsky.test/uslugi/  
- http://shpigovsky.test/uslugi/zavisimosti/  
- http://shpigovsky.test/o-centre/programma-lecheniya/prostranstvo-vosstanovleniya/  
- Comfort open/nav/close on `/uslugi/` and `/uslugi/zavisimosti/`  
- One individual service with Comfort (e.g. opium leaf)

### Admin

- Edit child #1054 (title / slug / Мини-описание) — cards should follow  
- O-centre page editor: program directions note visible; legacy repeater hidden  
- Do not expect Service `programme_items` to drive frontend cards anymore
