# REPORT — FP-0002 V9-06E62D Program Mini-Descriptions and 404 Figma Correction

**Date:** 2026-07-17  
**Runtime:** `http://shpigovsky.test/`  
**Database:** `mars_wp_fp0002`  
**Evidence:** `REPORTS/evidence/v9-06e62d-program-mini-descriptions-404-figma-correction/`  
**Backup:** `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e62d-before-program-mini-descriptions-404-figma-correction-20260717-170730`

---

## 1. Status

| Item | Result |
|------|--------|
| Overall | **PASS** (local validation) |
| Operator review | **pending** |
| DB writes | **yes** (seed + reversible edit/empty tests; final texts restored) |
| Commit / push / freeze | **no** |

---

## 2. Pre-Change Backup

| Item | Value |
|------|-------|
| Path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e62d-before-program-mini-descriptions-404-figma-correction-20260717-170730` |
| DB dump | `db/mars_wp_fp0002.sql` — 6 727 573 bytes — SHA256 `4E3625FD076BBB8FFCD043EE68B89056CD55B64EA941A22204503D4859EA519C` |
| Validation | **PASS** (`CREATE TABLE` + `INSERT`; `--no-tablespaces`; `BACKUP-OK.txt`) |
| Hashes / manifest | `hashes.csv`, `operator-change-manifest.csv`, `BACKUP-INFO.md` |

---

## 3. Latest Operator Changes Canonized

| Item | Detail |
|------|--------|
| Pre-wave theme/plugin drift | **0** (source = runtime for product files) |
| `v9-style.css` | MATCH `18114D3C…` — **no promote** (already canon from E62C) |
| Templates / HTML | **0** HTML drift |
| Plugin | **0** drift |
| ACF JSON | 8 pre-existing source-only groups **not** broad-synced; new group delivered exactly |
| Protected | breadcrumbs, lifebuoy, nav, CTA markup, operator CSS — untouched |

---

## 4. Treatment Program Content Model

| Item | Value |
|------|-------|
| Parent | Page **#13** «Программа лечения» — `/o-centre/programma-lecheniya/` |
| Children | **#1053** genotipirovanie; **#1054** neyropsihologicheskaya-korrektsiya; **#1055** psihokorrektsiya; **#1056** kinezioterapiya |
| Home path | `front-page.php` → `template-parts/home/rehabilitation-program.php` → `shpigovsky_get_program_direction_items('home')` |
| Previous text source | Hardcoded `text` keys in `inc/program-direction-helpers.php` |
| Other uses of direction map | Services hub / service / about blocks use `variant=service` (title/image/URL only; no Home body text) |

Matrix: `evidence/.../program-child-page-matrix.csv`

---

## 5. Mini-Description ACF

| Item | Value |
|------|-------|
| Group | `group_fp02_treatment_program_child` — «Программа лечения — карточка» |
| Field key | `field_fp02_treatment_program_short_description` |
| Name / label | `treatment_program_short_description` / **Мини-описание** |
| Type | textarea, 4 rows, `new_lines` empty (no auto `<p>`) |
| Instructions | «Краткий текст для карточки направления в блоке программы лечения на Главной странице.» |
| Location | `page_parent == 13` (dynamic children of Treatment Program parent) |
| Admin check | HAS_GROUP on #1053–1056; NO_GROUP on #13/#11/#20/#4/#74 |
| Ownership | Page-owned ACF on Treatment Program children — not Home repeater |

---

## 6. Text Migration

| Child ID | Title | Old hardcoded | Previous field | Seeded/final | Result |
|----------|-------|---------------|----------------|--------------|--------|
| 1053 | Генотипирование | helpers.php `text` | empty | same as hardcoded | SEEDED |
| 1054 | Нейропсихологическая коррекция | helpers.php `text` | empty | same as hardcoded | SEEDED |
| 1055 | Психокоррекция | helpers.php `text` | empty | same as hardcoded | SEEDED |
| 1056 | Кинезиотерапия | helpers.php `text` | empty | same as hardcoded | SEEDED |

Hardcoded `text` keys **removed** from permanent definitions after seed. Edit-test on #1053 changed only its Home card; empty field → empty card text; accepted text restored.

---

## 7. Home Integration

| Item | Detail |
|------|--------|
| Helper | `shpigovsky_get_treatment_program_short_description( $page_id )` via `get_field` / postmeta |
| Template | `.home-rehabilitation-program__direction-text` still `wp_kses_post( $direction['text'] )` — no new `<p>` wrappers; classes preserved |
| Ordering / URLs / titles | Unchanged (slug map + resolved permalinks) |
| Fallback | Empty ACF → empty text (no permanent hardcoded array) |
| Viewports | Home screenshots 1440/1024/480/370 captured under `evidence/.../home/` |

---

## 8. 404 Figma Measurements

Authority PNG: desktop **1437×1900**, mobile **380×1734**, bg **`#DBE5F1`**, text **`#475371`**.

| Property | Figma desktop | Desktop before | Desktop final | Figma mobile | Mobile before | Mobile final |
|----------|---------------|----------------|---------------|--------------|---------------|--------------|
| Title size | ≈32px | clamp→36px | **32px / 40px / 600** | ≈22–24px (2 lines) | clamp | **22px / 30px** |
| Title color | #475371 | inherited | **#475371** | #475371 | inherited | #475371 |
| Lead size | ≈20px | clamp→24px | **20px / 28px** | ≈15–16px | clamp | **15px / 22px** |
| Title→lead gap | ≈68px | 16px | **48px** | ≈28px | 16px | 24px |
| Logo width | 246px | ≤220 | **246px** | ≈168 | ≤220 | **168px** |
| Button | ≈262×53 | min 240 | **262×53** | ≈148×36 | min 180 | **148×36** |
| Visual radius | PNG cutout | CSS 28px | **0 (PNG owns shape)** | PNG | 20px | **0** |
| Title top @1440 | ≈292 | — | **291** | — | — | — |
| Visual top @1440 | ≈820 | — | **821** | — | — | — |

Full matrix: `evidence/.../404-measurement-matrix.csv`  
Computed: `404-before-computed.json`, `404-after-computed.json`

---

## 9. 404 Visual Corrections

| Area | Change |
|------|--------|
| Typography | Exact Inter sizes/weights/line-heights; color `#475371`; global `h1` leak blocked |
| Spacing | Increased vertical rhythm toward Figma bands (not clamp approximations) |
| Graphic | Removed CSS `border-radius` so PNG cutout + `#dbe5f1` fringe blend; no re-crop required (content fills canvas; fringe is intentional match to page bg) |
| Button | Desktop 262×53; mobile short label path preserved |
| Breakpoints | 1024 / 767 / 480 local rules |
| Files | `assets/css/fp02-404.css` only (404.php markup unchanged) |

---

## 10. 404 Validation

| Check | Result |
|-------|--------|
| Comparison boards | Figma refs + `before/` + `after/` screenshots |
| Routes | `/this-page-definitely-does-not-exist-e62d/`, invalid service URL, invalid blog URL → **HTTP 404** |
| Robots | `noindex, nofollow` |
| Canonical | none to unrelated page |
| PHP warnings | 0 |
| JS errors | 0 |
| Overflow | 0 on probed viewports |

---

## 11. Database Changes

| Item | Detail |
|------|--------|
| Writes | postmeta `treatment_program_short_description` + `_treatment_program_short_description` on **1053–1056** |
| Edit test | #1053 temporary string → Home only that card → restored |
| Empty test | #1053 cleared → empty card → restored |
| Idempotency | 4/4 present; non-empty preserved |
| Unrelated writes | **0** for this meta key outside 1053–1056 |

Log: `evidence/.../db-write-log.md`

---

## 12. Exact Files Changed

### Canonical source
- `WORDPRESS/plugins/shpigovsky-core/src/Fields/FieldGroups.php`
- `WORDPRESS/acf-json/group_fp02_treatment_program_child.json` *(new)*
- `WORDPRESS/theme/shpigovsky/inc/program-direction-helpers.php`
- `WORDPRESS/theme/shpigovsky/assets/css/fp02-404.css`
- `WORDPRESS/theme/shpigovsky/template-parts/home/rehabilitation-program.php` *(comment only)*

### Runtime
Exact copies of the same paths under `wp-content/themes/shpigovsky/`, `plugins/shpigovsky-core/`, `acf-json/`.

### Reports / evidence
- `REPORTS/REPORT-FP-0002-V9-06E62D-program-mini-descriptions-404-figma-correction.md`
- `REPORTS/evidence/v9-06e62d-program-mini-descriptions-404-figma-correction/**`
- `PROJECT-STATUS.md`, `WORDPRESS/SOURCE-AUTHORITY.md`

---

## 13. Source-to-Runtime Delivery

| Item | Result |
|------|--------|
| Method | Exact-file copy only (**no** broad sync) |
| Match | **6/6** scoped product hashes MATCH (`source-runtime-hashes.csv`) |
| Operator CSS | Preserved (`18114D3C…`) |

---

## 14. Regression

| Route | HTTP | Notes |
|-------|------|-------|
| `/` | 200 | Home direction texts from ACF |
| `/uslugi/` | 200 | |
| `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | 200 | (typo slug in one probe matrix row used `noj` → 404; correct `noy` = 200) |
| `/o-centre/` | 200 | |
| Program children ×4 | 200 | |
| `/kontakty/`, `/blog/`, `/otzyvy/` | 200 | |
| 404 probes ×3 | 404 | |
| Shared shell | preserved | header / floating header / breadcrumbs / lifebuoy / footer |
| Errors / overflow | 0 / 0 | |

---

## 15. Risks and SAFE UNKNOWN

- **Location rule** `page_parent == 13` assumes parent ID stability; new children under #13 auto-receive the field (maintenance-friendly).
- **Figma PNG measurement tolerance** ~±4–8px on AA text bands; computed tops match within 1–2px at 1440.
- **404 graphic crop:** no lossless re-crop performed — PNG fringe matches page bg; CSS radius removed instead.
- **Empty mini-descriptions:** render empty card text (intentional).

---

## 16. Remaining Project Tails

- Operator visual review (Home cards + 404)
- Demo Blog/Reviews cleanup decision
- Out-of-scope source-only ACF groups (still not synced)
- Final freeze / commit / push

---

## 17. Git Status

- **no commit**
- **no push**
- Exact FP-0002 scope only
- Foreign WIP untouched

---

## 18. Operator Review Pages

### Frontend
- `http://shpigovsky.test/` — Home program direction cards
- `http://shpigovsky.test/o-centre/programma-lecheniya/genotipirovanie/`
- `http://shpigovsky.test/o-centre/programma-lecheniya/neyropsihologicheskaya-korrektsiya/`
- `http://shpigovsky.test/o-centre/programma-lecheniya/psihokorrektsiya/`
- `http://shpigovsky.test/o-centre/programma-lecheniya/kinezioterapiya/`
- `http://shpigovsky.test/this-page-definitely-does-not-exist-e62d/` — 404 @ 1440 / 1024 / 480 / 370

### Admin
- Edit pages **#1053–#1056** — field **Мини-описание**
- Confirm absent on Home (#4), O-centre (#11), Program parent (#13), Contacts (#20), Service (#74)
