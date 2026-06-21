# M9 PHASE 3 SAFETY CHECK

**Program:** BZPM M9 Filter Profile System — Phase 3  
**Environment:** TEST ONLY — https://zpm.new-site.space/  
**Execution UTC:** 2026-06-15  
**Rollback source:** `SITE-002-STABLE-M8.3-BEFORE-M9-20260615-0159`  
**Phase 1 / 2 reference:** `SITE-002-M9-PHASE1-TABLES.md`, `SITE-002-M9-PHASE2-SINKS.md`

---

## Category Scope

| Action | category_id | Branch |
| --- | ---: | --- |
| **Implement profile** | 322 | Подтоварники и подставки (11 active SKU) |
| **Implement profile** | 207 | Зонты вытяжные (23 active SKU) |
| **Implement profile** | 326 | Тележки сервировочные (3 active SKU — dims-only) |
| **Document only** | 83 | Полки (0 active SKU) |
| **Document only** | 86 | Стеллажи (0 active SKU) |
| **Document only** | 85 | Тележки (0 active SKU) |
| **Preserved** | 301, 80 | Phase 1 / 2 profiles — unchanged files |

---

## Active Categories

| category_id | Active SKU (M8.1) | Profile file | Tier summary |
| --- | ---: | --- | --- |
| 322 | 11 | `322_podtovarniki.php` | PRIMARY: 51, 20 · SECONDARY: 22, 33, 21, 38, 26, 31, 115, 30, 24, 19 |
| 207 | 23 | `207_zonty.php` | PRIMARY: 21 · SECONDARY: 34 (branch exception) |
| 326 | 3 | `326_telezhki.php` | PRIMARY attrs: none (dims + commerce only) |

Physical dims (L/W/H) and price/availability remain controller-level PRIMARY on all profile PLPs.

---

## Empty Categories

| category_id | Name | Active SKU | Decision |
| --- | --- | ---: | --- |
| 83 | Полки | 0 | **Deferred** — spec-only planned profile in M9 architecture; activate on first SKU import |
| 86 | Стеллажи | 0 | **Deferred** — spec-only planned profile; activate on first SKU import |
| 85 | Тележки | 0 | **Deferred** — inherit root / legacy pool until populated |

No profile PHP files created for empty branches.

---

## Visible Attributes

### 322 — PRIMARY (sidebar, immediate)

| ID / source | Attribute |
| --- | --- |
| commerce | Цена, Наличие |
| oc_product | Длина, Ширина, Высота |
| 51 | Конструкция полки |
| 20 | Макс. нагрузка (до, кг) |

### 207 — PRIMARY

| ID / source | Attribute |
| --- | --- |
| commerce | Цена, Наличие |
| oc_product | Длина, Ширина, Высота |
| 21 | Конструкция |

### 326 — PRIMARY

| ID / source | Attribute |
| --- | --- |
| commerce | Цена, Наличие |
| oc_product | Длина, Ширина, Высота |

---

## Secondary Attributes

### 322 — «Дополнительные параметры» (collapsed)

22 Материал столешницы · 33 Тип опоры · 21 Конструкция · 38 Количество · 26 Ножки · 31 Регулируемость опоры · 115 Усиление · 30 Размер секции · 24 Назначение секции · 19 Количество уровней направляющих

### 207 — «Дополнительные параметры»

34 Страна производства (branch-only exception to global TECHNICAL hide)

### 326

None — insufficient SKU count; attr 42 Стандарт remains HIDDEN (global + branch).

---

## Hidden Attributes

**Global** (`global_hidden.php`): unchanged — TEST, SERVICE, packaging, TECHNICAL 12/13/27/36/34/42, dead defs.

**Branch-specific hidden:**

| Profile | IDs hidden |
| --- | --- |
| 322 | 23, 28, 29, 47, 112, 25, 18 + global |
| 207 | 12, 23, 28, 29, 51, 112, 115, 20, 22, 25 + global (except 34 via allowlist override) |
| 326 | 42 + global + all undiscovered attrs |

**Resolver note:** `isHiddenAttribute()` updated so branch PRIMARY/SECONDARY allowlist overrides global hidden (INH-04) — required for attr 34 on zonty only.

---

## Files To Modify

| Path | Action |
| --- | --- |
| `system/library/zpm/filter_profiles/322_podtovarniki.php` | **NEW** |
| `system/library/zpm/filter_profiles/207_zonty.php` | **NEW** |
| `system/library/zpm/filter_profiles/326_telezhki.php` | **NEW** |
| `system/library/zpm/filter_profile_resolver.php` | **MODIFIED** — register 207, 322, 326; allowlist override |
| `system/library/zpm/filter_profiles/global_hidden.php` | unchanged (redeploy) |
| `system/library/zpm/filter_profiles/301_stoly.php` | unchanged (redeploy) |
| `system/library/zpm/filter_profiles/80_moechnye_vanny.php` | unchanged (redeploy) |
| `catalog/model/catalog/product.php` | unchanged (redeploy) |
| `catalog/controller/product/category.php` | unchanged (redeploy) |
| `catalog/view/theme/default/template/sections/filterssidebar.twig` | unchanged (redeploy) |

Local patch: `projects/ocpilot/sites/site-002/m9-phase3-remaining-work/patch/`

---

## Rollback Method

1. Restore pre-Phase-3 resolver from `m9-phase3-remaining-work/backups/pre-m9-phase3-system__library__zpm__filter_profile_resolver.php` (Phase 2 resolver).
2. Delete on TEST host: `322_podtovarniki.php`, `207_zonty.php`, `326_telezhki.php`.
3. Clear `system/storage/cache/template/*` and `cache.category.attributes.*`.
4. Re-run M9 Phase 2 QA (`m9-phase2-qa.py`) — expect 7/7 pass.

**Full rollback to M8.3:** `SITE-002-STABLE-M8.3-BEFORE-M9-20260615-0159` baseline + remove all M9 library files.

---

## Risk Gate

| Risk | Assessment |
| --- | --- |
| Cross-contamination 301/80 vs new profiles | **LOW** — separate branch roots; regression QA included |
| Global hidden override for 34 | **LOW** — scoped to zonty allowlist only |
| Empty category accidental profile | **NONE** — 83/86/85 excluded |
| Resolver regression | **LOW** — single method change; Phase 1/2 files byte-identical |

**Risk gate:** **PASS** — proceed with TEST deploy.
