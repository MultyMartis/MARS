# REPORT — FP-0002 V9-06E59-FIX01 Comfort Gallery, Contacts ACF and Footer Hover

**Date:** 2026-07-17  
**Runtime:** `http://shpigovsky.test/`  
**Database:** `mars_wp_fp0002`  
**Evidence:** `REPORTS/evidence/v9-06e59-fix01-comfort-contacts-footer-corrections/`

---

## 1. Status

| Item | Result |
|------|--------|
| Overall | **PASS** |
| Operator review | **pending** |
| DB writes | **0** |
| Commit / push / freeze | **no** |

---

## 2. Pre-Change Backup

| Item | Value |
|------|-------|
| Path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e59-fix01-before-comfort-contacts-footer-corrections-20260717-013408` |
| DB dump | `db/mars_wp_fp0002.sql` — 4 063 340 bytes — SHA256 `05B23BE442DE33B3090267E001CC0A922FD13A47C5C59C91C0899BF955980A95` |
| Validation | **PASS** (MySQL dump header + CREATE TABLE present; `BACKUP-OK.txt`) |
| Hashes | `hashes.csv`, `operator-change-manifest.csv` |

---

## 3. Latest Operator Changes Canonized

| Item | Result |
|------|--------|
| Preflight theme source↔runtime | **MATCH** (651/651 product files) |
| Plugin product tree | **MATCH** |
| Operator CSS `v9-style.css` | already identical source/runtime (`1AA1AAC8…` pre-wave) — **no promote needed** |
| Unresolved product drift | none for theme/plugin; unrelated ACF JSON drift outside Contacts left untouched |

---

## 4. Comfort Decor Separation

| Item | Detail |
|------|--------|
| Previous DOM | `.comfort__gallery` > `.comfort__gallery-item.comfort__gallery-item_decor` + photo items |
| New DOM | `.comfort__gallery-stage` > `.comfort__gallery-decor` + `.comfort__gallery` (real items only; `display: contents`) |
| Real gallery item count | **6** (was 7 grid children including decor) |
| Fancybox `data-fancybox="comfort"` | **6** (decor excluded) |
| Legacy class `comfort__gallery-item_decor` | **0** on frontend |
| JS | Fancybox binds only `[data-fancybox="comfort"]` — unchanged; decor has no fancybox |
| Visual grid | Stage owns 3-column grid; decor remains first cell; photos keep wide spans |
| Routes with Comfort section | `/`, `/uslugi/`, `/uslugi/zavisimosti/`, alcohol + narcotic service leaves |
| `/o-centre/` | infrastructure g5 uses same stage/decor pattern (not `section.comfort`) |

---

## 5. Contacts ACF Usage Audit

| field key | field name | label | status | code references | DB values | action |
|-----------|------------|-------|--------|-----------------|-----------|--------|
| `field_fp02_contacts_address` | `contacts_address` | Address | OBSOLETE | static fallback only | retained dormant | **removed** |
| `field_fp02_contacts_map_url` | `contacts_map_url` | Map URL | OBSOLETE | unused template render | empty / absent | **removed** |
| `field_fp02_contacts_blocks` | `contacts_blocks` | Contact blocks | OBSOLETE | legacy fallback when locations empty | 2 rows dormant | **removed** |
| (children) | `title` / `text` | Заголовок / Текст | OBSOLETE | parent only | dormant | **removed** |
| `field_fp02_contacts_phones` | `contacts_phones` | Phones | ACTIVE | primary phone | 1 row | **retained** |
| `field_fp02_contacts_messengers` | `contacts_messengers` | Messengers | ACTIVE | messenger row | empty → site social | **retained** |
| `field_fp02_contacts_locations` | `contacts_locations` | Адреса и карты | ACTIVE | location cards + maps | **2 rows** | **retained** |
| `field_fp02_contacts_form_intro` | `contacts_form_intro` | Form intro | ACTIVE | intro copy | populated | **retained** |

Runtime `acf_get_fields('group_fp02_page_contacts')` returns exactly 4 fields (phones, messengers, locations, form_intro).

---

## 6. Contacts Cleanup

| Item | Result |
|------|--------|
| Fields removed from PHP + ACF JSON | `contacts_address`, `contacts_map_url`, `contacts_blocks` (+ children) |
| Fallbacks removed | `contacts_blocks` merge path in `shpigovsky_get_contacts_locations()` |
| Fields retained | phones, messengers, locations, form_intro |
| Legacy DB values | **retained** (no postmeta deletion) |
| Current repeater | `contacts_locations` = 2 rows with Yandex embeds |
| Frontend `/kontakty/` | 2 location articles; 2 constructor maps; 0 static map images |

Optional tail (not performed): delete dormant postmeta / DB `acf-field` posts under group `#101`.

---

## 7. Footer Hover/Focus

| Item | Value |
|------|-------|
| Previous | `color: inherit; opacity: 0.85; outline: 2px solid currentColor; outline-offset: 2px;` |
| Final | `color: var(--color-accent-hover);` only |
| Computed intent | accent hover color; no opacity; no outline |
| Routes checked | `/`, `/uslugi/`, `/o-centre/`, `/kontakty/` |

---

## 8. Future Site Settings Audit Registered

| Item | Value |
|------|--------|
| Task name | `FP-0002 — Site Settings Admin Information Architecture Audit and Russian UX Rebuild` |
| Where | `DOCS/FUTURE-TASK-SITE-SETTINGS-ADMIN-IA-AUDIT-AND-RU-UX-REBUILD-v1.md` + PROJECT-STATUS |
| Implementation | **none** in FIX01 |

---

## 9. Database Changes

| Item | Result |
|------|--------|
| Exact writes | **0** |
| Unrelated writes | **0** |
| Dormant legacy values | `contacts_blocks*`, `contacts_address` postmeta retained on page `#20` |

---

## 10. Exact Files Changed

**Canonical source + runtime (8 delivered):**

- `theme/shpigovsky/assets/css/v9-style.css`
- `theme/shpigovsky/template-parts/home/comfort.php`
- `theme/shpigovsky/template-parts/institutional/infrastructure-narrative.php`
- `theme/shpigovsky/inc/reusable-blocks-helpers.php`
- `theme/shpigovsky/inc/contacts-helpers.php`
- `plugins/shpigovsky-core/src/Fields/FieldGroups.php`
- `plugins/shpigovsky-core/src/Fields/RepeaterValidation.php`
- `acf-json/group_fp02_page_contacts.json`

**Reports/documentation:**

- `REPORTS/REPORT-FP-0002-V9-06E59-FIX01-comfort-contacts-footer-corrections.md`
- `REPORTS/evidence/v9-06e59-fix01-comfort-contacts-footer-corrections/*`
- `PROJECT-STATUS.md`
- `WORDPRESS/SOURCE-AUTHORITY.md`
- `DOCS/FUTURE-TASK-SITE-SETTINGS-ADMIN-IA-AUDIT-AND-RU-UX-REBUILD-v1.md`

---

## 11. Source-to-Runtime Delivery

See `evidence/.../delivery-hashes.csv` — **8/8 MATCH**.

No broad theme/plugin sync. Operator CSS/HTML preserved (additive Comfort stage + footer rule only on CSS).

Post-wave CSS hash prefix: `361CB364…`

---

## 12. Validation

| Area | Result |
|------|--------|
| Comfort decor outside gallery | PASS |
| Real item count 6 / fancybox 6 | PASS |
| Contacts locations + maps | PASS |
| Footer hover rule exact | PASS |
| HTTP 200 sampled routes | PASS |
| PHP warnings in HTML | 0 |
| Legacy decor class | 0 |

Viewports 1440 / 1024 / 480 / 370: structural DOM validated; operator visual sign-off pending.

---

## 13. Regression

Sampled routes HTTP 200: Home, Services hub, O-centre, Contacts, section Зависимости, 2 individual services, Blog, Blog single.

Comfort present where expected; Contacts maps intact; footer links intact; no CSS mass rewrite beyond scoped rules.

---

## 14. Risks and Tails

- Dormant legacy Contacts postmeta and DB `acf-field` posts under group `#101` (local PHP SoT overrides admin field list).
- Future Site Settings IA audit registered, not executed.
- Comfort stage uses `display: contents` — visual parity with prior 3-column composition; if a future browser quirk appears, reposition CSS without re-entering gallery item semantics.
- Operator visual confirmation still required for Comfort/Footer.

---

## 15. Git Status

- **no commit**
- **no push**
- Exact FP-0002 scope only
- Foreign WIP untouched

---

## 16. Operator Review Pages

1. Home — Comfort gallery + footer «Услуги» / «О центре» hover  
2. `/uslugi/` — Comfort + footer  
3. `/uslugi/zavisimosti/` — Comfort  
4. One individual service with Comfort (e.g. alcohol)  
5. `/o-centre/` — infrastructure gallery decor  
6. `/kontakty/` — both maps/addresses  
7. wp-admin → Pages → Контакты `#20` — confirm only phones / messengers / Адреса и карты / form intro (no Address / Map URL / Contact blocks)  
8. Footer hover on `/o-centre/` and `/kontakty/`
