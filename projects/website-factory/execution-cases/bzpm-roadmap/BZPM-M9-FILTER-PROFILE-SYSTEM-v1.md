# BZPM M9 — Filter Profile System Architecture v1

**Program:** BZPM Product Roadmap  
**Milestone:** M9 Filter Profile System  
**Environment:** https://zpm.new-site.space/ (TEST)  
**Specification UTC:** 2026-06-15  
**Mode:** Architecture only — no DB, code, deploy, or storefront changes  
**Authority:** `BZPM-PRODUCT-ROADMAP-v1.md` (ROAD-003, ROAD-004) · `BZPM-M8.1-ATTRIBUTE-INVENTORY-v1.md` · `BZPM-M8.2-CLEANUP-SPECIFICATION-v1.md` · `SITE-002-M8.3-WAVE1-TEST-CLEANUP.md` · `SITE-002-M8.3-WAVE2-TEST-CLEANUP.md` · `.recovery-temp/bzpm-m8.1-audit.json`

---

# REPORT — BZPM M9 Filter Profile System Architecture

## Executive Summary

**Проблема (подтверждено M8.1):** PLP строит `filter_groups` динамически через `getAttributesByCategory()` — любой заполненный атрибут активных SKU в поддереве категории попадает в sidebar. Это даёт **единый глобальный пул** (~15–20 атрибутов на Столах до M8.3), включая упаковку, SERVICE и нерелевантные для ветки поля.

**Цель M9:** перейти от **Global Filter** к **Category Filter Profiles** — для каждой ветки Нейтрального оборудования явно заданы: какие фильтры показывать, их tier (PRIMARY / SECONDARY / HIDDEN), группа, порядок и правила наследования.

**Текущее состояние post-M8.3 (TEST):**

| Слой | Статус |
| --- | --- |
| M8.3 Wave 1 | TEST attrs удалены; product 3071 inactive; **608** active SKU под Neutral 79 |
| M8.3 Wave 2 | Interim `AttributeFilterVisibility` — глобальный HIDE packaging (44–46, 52–57) + SERVICE (43, 48, 58) |
| M9 profiles | **Не реализованы** — Wave 2 = мост, не профили |
| TECHNICAL noise | IDs 12, 27, 34, 36, 42 **ещё в фильтре** — входят в M9 global HIDDEN |
| Native `oc_filter` | **0** rows — профили строятся на `oc_attribute` + `oc_product` dims |

**Объём M9 v1:** Launch Mode scope = **Нейтральное оборудование** (`category_id` **79**), **7 целевых веток** по заданию + root profile. Полки/Стеллажи/Тележки (85) — **0 active SKU**; профили spec-only до наполнения.

**Связь с roadmap:** M9 = ROAD-003 + ROAD-004. Группы фильтров (ROAD-006) и Primary vs Additional (ROAD-007) — **конфигурируются в профиле**, UI-рендер групп = M11. Dynamic visibility (ROAD-005) = M10; M9 задаёт **статический allowlist** и контракт для runtime rules.

---

## Category Profile Map

Источник: M8.1 Category Attribute Matrix (audit UTC 2026-06-14), post-Wave 1 active count **608** (was 609).  
Критерий «используется»: non-empty text на **≥1 active SKU** в поддереве ветки; commercial attrs — фокус задания.

### Сводная карта веток

| Category | category_id | Active SKU | Parent | Profile status |
| --- | ---: | ---: | ---: | --- |
| **Нейтральное оборудование** | 79 | 608 | — | Root profile (inheritance base) |
| **Моечные ванны** | 80 | 152 | 79 | **Populated** — full profile |
| **Столы** | 301 | 420 | 79 | **Populated** — full profile + subcategory overrides |
| **Зонты вытяжные** | 207 | 23 | 79 | **Populated** — minimal profile |
| **Подтоварники и подставки** | 322 | 11 | 79 | **Populated** — compact profile |
| **Тележки сервировочные** | 326 | 3 | 79 | **Sparse** — dims-only + REVIEW |
| **Тележки** | 85 | 0 | 79 | **Empty** — inherit root; defer attrs |
| **Полки** | 83 | 0 | 79 | **Empty** — planned profile (pattern from Столы) |
| **Стеллажи** | 86 | 0 | 79 | **Empty** — planned profile (pattern from Столы) |
| Столы производственные | 87 | 0 | 79 | Sibling of 301, not child — **REVIEW** taxonomy |
| Подтоварники | 82 | 0 | 79 | Empty parent; active SKUs under **322** |

**Примечание по taxonomy:** «Столы» (`301`) — PLP hub с вложенной иерархией (серии → линейки, напр. `/stoly/stoly-serii-premium/stoly-premium-600/`). Категория «Столы с бортом» **не зафиксирована в M8.1 audit** — используется ниже как **пример subcategory override** (ROAD-004), не как существующий `category_id`.

---

### 1. Моечные ванны (`80`, 152 SKU)

**Commercial attributes actually used in branch:**

| ID | Attribute | Branch fill | Class |
| ---: | --- | ---: | --- |
| — | Длина / Ширина / Высота / Масса (`oc_product`) | 152 | COMMERCIAL (physical) |
| 29 | Размер раковины (ДхШхВ, мм) | 147 | COMMERCIAL |
| 23 | Мойка | 149 | COMMERCIAL |
| 28 | Отверстие под смеситель | 149 | COMMERCIAL |
| 25 | Наличие борта | 149 | COMMERCIAL |
| 33 | Тип опоры | 149 | COMMERCIAL |
| 21 | Конструкция | 149 | COMMERCIAL |
| 26 | Ножки | 148 | COMMERCIAL |
| 18 | Высота борта (мм) | 140 | COMMERCIAL |
| 31 | Регулируемость опоры по высоте (max мм) | 114 | COMMERCIAL |
| 47 | Конструкция борта | 108 | COMMERCIAL |
| 22 | Материал столешницы | 104 | COMMERCIAL |
| 17 | В комплекте | 44 | COMMERCIAL |

**Filled but HIDDEN (profile excludes from filter):** 44–46, 52–54, 56, 43, 48, 12, 34, 42 (packaging/SERVICE/TECHNICAL per M8.2).

**Not used in branch (≥3 threshold):** sink-irrelevant table attrs (51, 112, 115, 20) — **не появляются** при корректном subtree scope.

---

### 2. Столы (`301`, 420 SKU)

**Commercial attributes actually used in branch:**

| ID | Attribute | Branch fill | Class |
| ---: | --- | ---: | --- |
| — | Длина / Ширина / Высота / Масса (`oc_product`) | 420 | COMMERCIAL |
| 22 | Материал столешницы | 420 | COMMERCIAL |
| 51 | Конструкция полки | 420 | COMMERCIAL |
| 21 | Конструкция | 420 | COMMERCIAL |
| 26 | Ножки | 420 | COMMERCIAL |
| 25 | Наличие борта | 420 | COMMERCIAL |
| 33 | Тип опоры | 420 | COMMERCIAL |
| 31 | Регулируемость опоры по высоте (max мм) | 420 | COMMERCIAL |
| 20 | Макс. нагрузка (до, кг) | 419 | COMMERCIAL |
| 115 | Усиление | 377 | COMMERCIAL |
| 112 | Материал полки | 377 | COMMERCIAL |
| 18 | Высота борта (мм) | 240 | COMMERCIAL |
| 47 | Конструкция борта | 44 | COMMERCIAL |
| 23 | Мойка | 43 | COMMERCIAL |
| 29 | Размер раковины (ДхШхВ, мм) | 43 | COMMERCIAL |
| 28 | Отверстие под смеситель | 43 | COMMERCIAL |

**Cross-family noise (reason for profile):** attrs 23/28/29 — **43 SKU** (combined table+sink SKUs). M9 profile for pure table lines should **HIDE** sink cluster unless subcategory override.

---

### 3. Тележки (`85`, 0 SKU) + Тележки сервировочные (`326`, 3 SKU)

**Тележки (85):** no active products — profile inherits root physical dims only.

**Тележки сервировочные (326):**

| ID | Attribute | Branch fill |
| ---: | --- | ---: |
| — | L/W/H/weight | 3 |
| 42 | Стандарт | 3 (TECHNICAL) |

**Policy:** until **N ≥ 20** active SKU — profile = **dims + price + availability** only; attr 42 = SECONDARY or HIDDEN until operator promotes.

---

### 4. Подтоварники и подставки (`322`, 11 SKU)

| ID | Attribute | Branch fill |
| ---: | --- | ---: |
| — | L/W/H/weight | 11 |
| 51 | Конструкция полки | 11 |
| 22 | Материал столешницы | 11 |
| 33 | Тип опоры | 11 |
| 21 | Конструкция | 11 |
| 31 | Регулируемость опоры | 11 |
| 26 | Ножки | 11 |
| 38 | Количество | 11 |
| 20 | Макс. нагрузка (до, кг) | 8 |
| 115 | Усиление | 8 |
| 30 | Размер секции | 3 (REVIEW) |
| 19 | Количество уровней направляющих | 3 (REVIEW) |
| 24 | Назначение секции | 3 (REVIEW) |

---

### 5. Полки (`83`, 0 SKU)

**No branch fill in M8.1.** Planned commercial set (from global fill + M8.2 pattern):

| ID | Attribute | Global fill | Planned role |
| ---: | --- | ---: | --- |
| — | L/W/H/weight | — | PRIMARY when populated |
| 51 | Конструкция полки | 435 | PRIMARY |
| 112 | Материал полки | 377 | PRIMARY |
| 114 | Количество полок (шт) | 1 | REVIEW → PRIMARY when N grows |
| 113 | Шаг регулировки полки (мм) | 1 | REVIEW |
| 20 | Макс. нагрузка | 427 global | SECONDARY |
| 21, 33, 26, 31 | Universal construction | high global | SECONDARY |

**Status:** spec-only; activate on first SKU import.

---

### 6. Стеллажи (`86`, 0 SKU)

**Planned profile** (load-critical shelving):

| ID | Attribute | Planned tier |
| ---: | --- | --- |
| — | L/W/H/weight | PRIMARY |
| 51 | Конструкция полки | PRIMARY |
| 112 | Материал полки | PRIMARY |
| 20 | Макс. нагрузка (до, кг) | PRIMARY |
| 114 | Количество полок (шт) | REVIEW → PRIMARY |
| 115 | Усиление | SECONDARY |
| 113 | Шаг регулировки полки (мм) | REVIEW |

---

### 7. Зонты вытяжные (`207`, 23 SKU)

| ID | Attribute | Branch fill |
| ---: | --- | ---: |
| — | L/W/H/weight | 23 |
| 21 | Конструкция | 19 |
| 34 | Страна производства | 22 (TECHNICAL) |
| 12 | Габариты нетто (мм) | 22 (TECHNICAL) |

**Minimal profile:** dims + Конструкция; Страна — единственная ветка где origin может быть SECONDARY (M8.2).

---

## Attribute Classification

Для каждой populated ветки — tier + reason. **HIDDEN** = never in filter sidebar (PDP STORE_ONLY per M8.2).  
Global HIDDEN применяется ко **всем** neutral profiles.

### Global HIDDEN (all profiles under 79)

| IDs / source | Reason |
| --- | --- |
| 16, 105–111 | TEST — deleted Wave 1; guard in profile |
| 43, 48, 58, 102 | SERVICE — ops text; Wave 2 interim hide |
| 44–46, 52–57 | Packaging — logistics; Wave 2 interim hide |
| 12, 13, 27, 36 | TECHNICAL logistics/engineering |
| 14, 15, 32, 55, 103, 104 | Dead / duplicate defs |
| Native `oc_filter` | Unused (0 rows) |

**Post-Wave 2 note:** packaging/SERVICE скрыты **глобально в коде**, не по профилю. M9 Phase 1 должен **поглотить** этот список в root profile `hidden_global[]` и deprecate hardcoded list.

---

### Моечные ванны (`80`) — classification

| Tier | Attribute (ID) | Reason |
| --- | --- | --- |
| **PRIMARY** | Длина, Ширина, Высота, Масса | Buyer-first sizing; 152/152 branch fill on dims |
| **PRIMARY** | Размер раковины (29) | Core sink dimension; 147 SKU — main decision axis |
| **PRIMARY** | Мойка (23) | Universal in branch (149/152) |
| **PRIMARY** | Наличие борта (25) | Yes/no commercial gate (149/152) |
| **SECONDARY** | Отверстие под смеситель (28) | Secondary install decision; high fill |
| **SECONDARY** | Конструкция борта (47) | Detail after bort yes/no |
| **SECONDARY** | Высота борта (18) | Numeric detail for bort variants |
| **SECONDARY** | Тип опоры (33), Ножки (26), Конструкция (21) | Construction family |
| **SECONDARY** | Регулируемость опоры (31) | Adjustability — not first click |
| **SECONDARY** | Материал столешницы (22) | 104 SKU — relevant but not sink-specific primary |
| **SECONDARY** | В комплекте (17) | Kit contents — 44 SKU |
| **HIDDEN** | All global HIDDEN + table-only attrs (51, 112, 115, 20) | Wrong product family for sink PLP |

---

### Столы (`301`) — classification

| Tier | Attribute (ID) | Reason |
| --- | --- | --- |
| **PRIMARY** | Длина, Ширина, Высота, Масса | Universal table sizing |
| **PRIMARY** | Материал столешницы (22) | Top commercial axis (420/420) |
| **PRIMARY** | Конструкция полки (51) | Shelf type — core table variant |
| **PRIMARY** | Макс. нагрузка (20) | Load rating — B2B decision (419/420) |
| **SECONDARY** | Материал полки (112), Усиление (115) | Shelf/load details |
| **SECONDARY** | Тип опоры (33), Ножки (26), Конструкция (21) | Construction |
| **SECONDARY** | Наличие борта (25) | 420 SKU but often default; promote in bort subcats |
| **SECONDARY** | Регулируемость опоры (31) | Adjustability |
| **SECONDARY** | Высота борта (18), Конструкция борта (47) | Bort subset (240 / 44 SKU) |
| **HIDDEN** | Мойка (23), Отверстие (28), Размер раковины (29) | Sink cluster — 43 SKU on combined SKUs; hide on default table profile |
| **HIDDEN** | Стандарт (42), Страна (34), Габариты нетто (12) | TECHNICAL — M9 global hide |
| **HIDDEN** | All global HIDDEN | Packaging/SERVICE/TEST |

**Subcategory override example (planned, ROAD-004):** leaf «Столы с бортом» → promote 25, 18, 47 to **PRIMARY**; keep sink cluster **HIDDEN**.

---

### Подтоварники и подставки (`322`)

| Tier | Attribute (ID) | Reason |
| --- | --- | --- |
| **PRIMARY** | L/W/H/weight | Size + footprint |
| **PRIMARY** | Конструкция полки (51) | Core shelf construction |
| **PRIMARY** | Макс. нагрузка (20) | Load-critical (8/11 but commercial key) |
| **SECONDARY** | Материал столешницы (22), Тип опоры (33), Конструкция (21) | Materials/support |
| **SECONDARY** | Количество (38), Ножки (26), Регулируемость (31) | Secondary specs |
| **SECONDARY** | Усиление (115) | 8 SKU — REVIEW promote when stable |
| **REVIEW→SECONDARY** | Размер секции (30), Назначение секции (24), Кол-во уровней (19) | 3 SKU each — show only if dynamic rules pass (M10) |
| **HIDDEN** | Sink/table-only attrs (23, 28, 29, 47), global HIDDEN | Irrelevant |

---

### Зонты вытяжные (`207`)

| Tier | Attribute (ID) | Reason |
| --- | --- | --- |
| **PRIMARY** | L/W/H/weight | Hood sizing |
| **PRIMARY** | Конструкция (21) | 19/23 — main variant axis |
| **SECONDARY** | Страна производства (34) | Only branch where origin may surface (22/23) |
| **HIDDEN** | Габариты нетто (12) | Duplicates product dims |
| **HIDDEN** | All table/sink/shelf attrs + global HIDDEN | Wrong family |

---

### Тележки сервировочные (`326`)

| Tier | Attribute (ID) | Reason |
| --- | --- | --- |
| **PRIMARY** | L/W/H/weight | Only reliable filters at N=3 |
| **REVIEW** | Стандарт (42) | TECHNICAL; defer until N≥20 |
| **HIDDEN** | All other attrs | Insufficient data; prevent noise |

---

### Полки (`83`) / Стеллажи (`86`) — planned

| Tier | Полки | Стеллажи |
| --- | --- | --- |
| **PRIMARY** | L/W/H/weight, Конструкция полки (51), Материал полки (112) | L/W/H/weight, 51, 112, Макс. нагрузка (20) |
| **SECONDARY** | Макс. нагрузка (20), Конструкция (21), Тип опоры (33) | Усиление (115), 114, 113 (REVIEW) |
| **HIDDEN** | Global + sink/table-only | Global + sink/table-only |

---

## Filter Groups System

Группы — **универсальная таксономия UI** (ROAD-006). Членство задаётся в профиле; рендер accordion/sections = M11.  
Построено из M8.1 registry + M8.2 Core Commercial Set — **не assumed**.

### Canonical filter groups (Neutral Equipment)

| Group ID | Label (RU) | Members | Evidence |
| --- | --- | --- | --- |
| `price_availability` | **Цена и наличие** | Price range, toggles (in stock / on order / …) | Existing PLP commerce controls; not attributes |
| `dimensions` | **Размеры** | `oc_product.length`, `width`, `height`, `weight`; attr **29** (Размер раковины) *sink branches only* | M8.1 universal dims 586/609; 29 = sink primary |
| `construction` | **Конструкция** | 21, 25, 26, 33, 31, 47, 51, 115, 19, 114, 113 | M8.2 Tier 2–3 construction cluster |
| `materials` | **Материалы** | 22, 112, 110 (REVIEW) | Table/shelf materials — high fill |
| `operation` | **Эксплуатация и сантехника** | 23, 28, 18, 20, 17, 38, 49 | Branch-specific: sink (23,28), load (20), kits (17,38) |
| `additional` | **Дополнительные параметры** | REVIEW attrs (19, 24, 30, 50, 110, 113, 114); 34 (зонты only); 42 if ever promoted | Low-fill / branch-specific |
| `hidden` | *(not rendered)* | Global HIDDEN set | M8.2 Hidden Attribute Set |

### Group assignment by category (summary)

| Category | price_availability | dimensions | construction | materials | operation | additional |
| --- | --- | --- | --- | --- | --- | --- |
| Моечные ванны | ✓ | ✓ + **29** | 25,47,18,33,26,21,31 | 22 | 23,28,17 | 49 |
| Столы | ✓ | ✓ | 25,26,33,31,21,51,115,47,18 | 22,112 | 20 | — |
| Подтоварники | ✓ | ✓ | 51,21,33,26,31,115 | 22 | 20,38 | 19,24,30 |
| Зонты | ✓ | ✓ | 21 | — | — | 34 |
| Тележки серв. | ✓ | ✓ | — | — | — | 42 (REVIEW) |
| Полки / Стеллажи | ✓ | ✓ | 51,21,33,114,113 | 112 | 20,115 | — |

**Rule:** attribute appears in **at most one group** per profile. Tier (PRIMARY/SECONDARY) is orthogonal to group.

---

## Profile Inheritance Model

### Category tree reality (TEST, documented)

```
Нейтральное оборудование (79)          ← ROOT PROFILE
├── Моечные ванны (80)                 ← BRANCH PROFILE (override root)
├── Столы (301)                        ← BRANCH PROFILE
│   ├── Столы серии ПРЕМИУМ (…)        ← SUBCATEGORY OVERRIDE (nested PLP)
│   ├── Столы ПРЕМИУМ-600 (leaf)        ← SUBCATEGORY OVERRIDE (optional)
│   └── … (series / line categories)
├── Зонты вытяжные (207)
├── Подтоварники и подставки (322)
├── Тележки сервировочные (326)
├── Тележки (85) — empty
├── Полки (83) — empty
├── Стеллажи (86) — empty
└── Столы производственные (87) — empty sibling (taxonomy REVIEW)
```

**SAFE UNKNOWN:** полный `oc_category` export с `parent_id` для всех nested table categories не в M8.1 JSON — inheritance для leaf categories опирается на M7.1 URL evidence (`/stoly/stoly-serii-premium/stoly-premium-600/`).

### Inheritance rules

| Rule ID | Behavior |
| --- | --- |
| **INH-01** | **Root profile (79)** defines: `hidden_global[]`, default groups, default tier for universal attrs (21, 33, 26, 25, 31), physical dims PRIMARY |
| **INH-02** | **Branch profile** (direct child of 79): **extends** root; may `add`, `override_tier`, `override_group`, `exclude` attrs |
| **INH-03** | **Subcategory profile** (depth ≥2 under branch): **inherits branch**; override wins on conflict (ROAD-004) |
| **INH-04** | **Merge semantics:** `effective = root ⊕ branch ⊕ subcategory` where ⊕ = child overrides parent for same attr key |
| **INH-05** | **HIDDEN is absolute:** if any level marks attr HIDDEN, it never surfaces (unless explicit `force_show` flag — **not in v1**) |
| **INH-06** | **Empty branch:** no branch file → inherit root only + category-scoped dynamic discovery disabled |
| **INH-07** | **Subtree scope:** profile resolves on **current PLP `category_id`**; product set = active SKUs in category subtree (existing `category_path` join) |

### Example inheritance chain (conceptual — ROAD-004)

| Level | category | Override |
| --- | --- | --- |
| Root | Нейтральное оборудование (79) | hidden_global; universal SECONDARY for 21,33,26 |
| Branch | Столы (301) | PRIMARY: 22,51,20; HIDDEN: 23,28,29 |
| Subcategory | Столы с бортом *(planned)* | PRIMARY: 25,18,47; keep sink HIDDEN |
| Leaf | Столы ПРЕМИУМ-600 *(exists)* | Inherit branch unless leaf-specific JSON |

### Profile resolution algorithm (design)

```
1. Load profile chain: [root_id=79, …ancestors…, current_category_id]
2. Merge attribute tiers + groups bottom-up (child wins)
3. Apply hidden_global + merged HIDDEN set → filter allowlist
4. Intersect with M10 dynamic visibility (future) on current result set
5. Sort by: group order → tier (PRIMARY first) → profile sort_index
6. Emit filter_groups[] to filterssidebar.twig
```

### Config storage (design — no implementation)

| Option | Recommendation |
| --- | --- |
| Format | JSON or PHP array under `system/library/zpm/filter_profiles/` |
| Key | `category_id` + optional `profile_version` |
| Fallback | Root 79 if no file |
| Admin UI | **Out of M9 scope** — manual JSON v1; admin editor = future |

---

## Dynamic Visibility Rules

M9 defines **static profile**; M10 implements **runtime rules**. M9 must expose hook contract.

### Rule types (priority order)

| Priority | Rule ID | Condition | Action | M10 owner |
| ---: | --- | --- | --- | --- |
| 1 | **DV-01 Profile HIDDEN** | Attr in profile `hidden` or `hidden_global` | Never render | M9 |
| 2 | **DV-02 Zero products in result set** | After category + active filters, **0 SKUs** have non-empty value for attr | Hide filter control | M10 |
| 3 | **DV-03 Single value only** | Exactly **1 distinct value** across current result set (and no range semantics) | Hide filter (no choice) | M10 |
| 4 | **DV-04 Single value post-filter** | User applied filters → attr has ≤1 value in narrowed set | Hide or disable | M10 |
| 5 | **DV-05 Empty attribute** | No non-empty values in subtree for attr | Hide | M10 |
| 6 | **DV-06 Low-fill REVIEW** | Attr tier=REVIEW and fill count **< threshold** (default **3** SKU in subtree) | Hide unless operator promoted | M9 config + M10 |
| 7 | **DV-07 Physical range collapse** | min=max for L/W/H/weight on result set | Hide range slider | M10 |
| 8 | **DV-08 Cross-family guard** | Attr not in profile allowlist | Hide (replaces raw `getAttributesByCategory` discovery) | M9 |

### Exact logic — DV-03 (single value)

```
INPUT:  category_id, current_filter_state, attribute_id
SET:    products = active SKUs in category subtree matching current_filter_state
VALUES: distinct non-empty normalized values of attribute_id across products
IF     count(VALUES) <= 1 AND attribute is NOT range-type:
       HIDE filter
ELSE   SHOW (subject to tier/group)
```

**Range-type exception:** `oc_product` L/W/H/weight always show if `max > min` on result set (DV-07 inverse).

### Exact logic — DV-02 (empty result set)

```
IF applying any value of attribute_id would yield 0 products
   AND no products in current set carry that attr:
   HIDE
```

**Note:** distinguish «attr absent on all SKUs» (DV-05) vs «attr present but all same» (DV-03).

### M9 vs M10 boundary

| Concern | M9 | M10 |
| --- | --- | --- |
| Category relevance | Profile allowlist | — |
| Packaging/SERVICE/TEST | HIDDEN in profile | — |
| Single-value hide | Contract only | Implementation |
| Filter count after user selection | — | Live recalc |
| Cache | Profile static — cache by category_id | Invalidate on filter state (AJAX) or page load |

---

## Primary vs Additional Filters

**Goal:** reduce filter panel height (Category Audit V1: «sidebar-фильтр чрезмерно длинный»).  
Tier mapping to UI (ROAD-007 — render in M11):

| Tier | UI behavior | Collapsed by default |
| --- | --- | --- |
| **PRIMARY** | Visible immediately in sidebar (desktop) / top of mobile panel | No |
| **SECONDARY** | Inside group; group may be collapsed | Group: optional |
| **ADDITIONAL** | Single accordion «Дополнительные параметры» at bottom | **Yes** |
| **HIDDEN** | Not rendered | — |

### Default PRIMARY set (Neutral root)

| Filter | Reason |
| --- | --- |
| Price + availability | Commerce baseline |
| Длина, Ширина, Высота | Highest cross-category fill (586/609) |
| Масса | 531/609 — load hint |

Branch **adds** PRIMARY per classification tables above.

### Collapse policy by category

| Category | PRIMARY (immediate) | ADDITIONAL (collapsed section) |
| --- | --- | --- |
| Моечные ванны | Price, dims, 29, 23, 25 | 28, 47, 18, 33, 26, 21, 31, 22, 17 |
| Столы | Price, dims, 22, 51, 20 | 112, 115, 33, 26, 21, 25, 31, 18, 47 |
| Подтоварники | Price, dims, 51, 20 | 22, 33, 21, 38, 26, 31, REVIEW attrs |
| Зонты | Price, dims, 21 | 34 |
| Тележки серв. | Price, dims only | — (42 hidden until N≥20) |

### Mobile parity

- PRIMARY: visible before scroll in filter overlay
- ADDITIONAL: one `<details>` / accordion «Ещё параметры» — matches УЗНМ simplified pattern direction (FIM-W3Y-001)

---

## Benchmark References

Reference-only (ROAD-008, D-03: **no direct copy**). Patterns inform M9/M11 design.

| Benchmark | Registry | Relevant pattern | M9 application |
| --- | --- | --- | --- |
| **УЗНМ** | COMP-BZPM-007 | Simplified filter UI — fewer groups, cleaner panel (FIM-W3Y-001) | PRIMARY-only default; collapse SECONDARY; limit groups to 4–5 visible |
| **КЛЕН** | COMP-BZPM-012 | View switchers (FIM-W3Y-003) | Out of M9 scope (M11/M12); filter panel unchanged |
| **Юниторг** | CAN-EXP-005 | Dual-column cards (FIM-W3Y-002) | Listing layout — not filter; dims PRIMARY align with dense cards |
| **Trapeza** | COMP-BZPM-011 | High information density — attrs on listing (FIM-W3Y-004) | Informs which attrs are PRIMARY (load, material, dims); not filter count inflation |
| **Kobor / Комплекс Трейд** | CAN-EXP-003/004 | Operator attention; no formal filter tag | No M9 inference — SAFE UNKNOWN |

**Operator intent synthesis:** УЗНМ → **reduce vertical noise** (Primary vs Additional). Trapeza → **keep decision attrs visible** (correct PRIMARY tier). Юниторг/КЛЕН → card/layout, deferred.

**Post-Wave 2 BZPM state vs benchmarks:** after packaging hide, Столы PLP shows commercial core (QA: Конструкция, Тип опоры, Материал столешницы, Макс. нагрузка) — closer to УЗНМ, but still **flat list** without groups/collapse (M11).

---

## Implementation Strategy

Lowest-risk sequence. Each phase = TEST deploy + QA gate. **No production** until operator sign-off.

### Phase 1 — Foundation (schema + root profile + replace interim hide)

| Step | Deliverable | Risk |
| ---: | --- | --- |
| 1.1 | Profile schema v1 (`profile_id`, `inherits`, `attributes{tier, group, sort}`) | Low |
| 1.2 | Root profile `79` with `hidden_global[]` = M8.2 hidden + Wave 2 packaging/SERVICE | Low |
| 1.3 | Refactor `getAttributesByCategory()` → `FilterProfileResolver::resolve($category_id)` | Medium |
| 1.4 | Deprecate hardcoded `AttributeFilterVisibility` lists — data moves to profile | Medium |
| 1.5 | Hide TECHNICAL 12, 27, 34, 36, 42 via root profile | Low |
| 1.6 | QA: Столы + Моечные ванны — no packaging/SERVICE/TECHNICAL; commercial intact | — |

**Exit gate:** PLP behavior ≥ Wave 2 parity + TECHNICAL hidden.

### Phase 2 — Branch profiles (populated categories)

| Step | Deliverable | Risk |
| ---: | --- | --- |
| 2.1 | Profile `80` Моечные ванны — sink PRIMARY set; hide table attrs | Low |
| 2.2 | Profile `301` Столы — table PRIMARY; hide sink cluster 23/28/29 | Medium |
| 2.3 | Profile `322` Подтоварники, `207` Зонты, `326` Тележки серв. | Low |
| 2.4 | Spec-only profiles `83` Полки, `86` Стеллажи (ready for import) | Low |
| 2.5 | QA matrix: all 7 target categories + regression PDP specs block | — |

**Exit gate:** each branch shows **only** profile allowlist attrs; no cross-family noise (Столы ≠ sink attrs).

### Phase 3 — Subcategory overrides + M10 hooks + M11 prep

| Step | Deliverable | Risk |
| ---: | --- | --- |
| 3.1 | Subcategory override mechanism (ROAD-004) — e.g. table bort lines | Medium |
| 3.2 | `dynamic_visibility` hook stubs (DV-02…DV-07) — no-op or log-only until M10 | Low |
| 3.3 | Export group + tier metadata to template for M11 accordion | Low |
| 3.4 | M8.3 Wave 3 dead-def DELETE — profile guard for removed IDs | Low |
| 3.5 | Operator review: promote REVIEW attrs 19,24,30,114 per branch fill | Low |

**Exit gate:** inheritance chain verified on nested Столы PLP; M10 charter approved.

### Dependency graph

```
M8.3 Wave 1 (done) → M8.3 Wave 2 (done) → M9 Phase 1 → Phase 2 → Phase 3
                                                    ↘ M10 (dynamic rules)
                                                    ↘ M11 (groups UI + collapse)
```

---

## Risks

| ID | Risk | Severity | Mitigation |
| --- | --- | --- | --- |
| RSK-M9-01 | **Profile drift from live data** — new attrs auto-surface via old dynamic logic | High | Phase 1 removes discovery-first; allowlist-only |
| RSK-M9-02 | **Incomplete category tree** for subcategory overrides | Medium | Phase 3 after PMA export of full `oc_category`; inherit branch until then |
| RSK-M9-03 | **Combined SKUs** (table+sink on Столы) — hiding 23/28/29 may confuse if user expects | Medium | Subcategory overrides; DV-02 shows if fill in subtree |
| RSK-M9-04 | **Empty branches** (Полки, Стеллажи, Тележки 85) — profile without QA data | Low | Spec-only; inherit root; activate on import |
| RSK-M9-05 | **4 unknown attribute IDs** (60 vs 56 in DB) | Medium | Classify before Phase 1 deploy; default HIDDEN |
| RSK-M9-06 | **Cache staleness** (`cache.category.attributes.*`) | High | Flush pattern from Wave 1 on every profile deploy |
| RSK-M9-07 | **Wave 2 interim code** conflicts with profile resolver | Medium | Phase 1.4 explicit deprecation + single code path |
| RSK-M9-08 | **M10 scope creep into M9** | Medium | Static allowlist in M9; runtime rules stub only |
| RSK-M9-09 | **Столы производственные (87)** vs **Столы (301)** taxonomy ambiguity | Medium | Operator taxonomy REVIEW; W1B name-match vs ID |
| RSK-M9-10 | **Benchmark over-fit** — copying УЗНМ filter set literally | Low | ROAD-008 reference-only; data-driven tiers from M8.1 |

---

## Recommended First Implementation Phase

**Start with Phase 1 + Phase 2.2 (Столы only)** as first deploy slice:

| Rationale | Evidence |
| --- | --- |
| Highest SKU volume | 420/608 active under Столы (301) |
| Highest historical noise | 6 packaging attrs × 420 SKU + SERVICE 43 (M8.1) |
| Wave 2 QA baseline | Commercial filters verified on `path=301` |
| Clear win | Hide sink attrs 23/28/29 on default table profile — immediate relevance gain |
| Rollback | Pre-Wave-2 `product.php` backup exists |

**First TEST deploy checklist:**

1. Root profile `79` — absorb Wave 2 hidden set + TECHNICAL 12,42,34,27,36  
2. Branch profile `301` — PRIMARY: dims, 22, 51, 20; HIDDEN: 23, 28, 29  
3. Single resolver path; remove duplicate hide lists  
4. Cache flush + QA-02 pattern from Wave 2 (Столы PLP)  
5. **Stop** — do not deploy other branches until Столы signed off  

**Second slice:** `80` Моечные ванны (152 SKU, distinct sink profile — validates cross-family separation).

---

## Profile Schema v1 (reference)

```json
{
  "profile_id": 301,
  "profile_key": "stoly",
  "inherits": 79,
  "label": "Столы",
  "groups_order": ["price_availability", "dimensions", "materials", "construction", "operation", "additional"],
  "attributes": {
    "oc_product.length":  { "tier": "PRIMARY",   "group": "dimensions",   "sort": 10 },
    "oc_product.width":   { "tier": "PRIMARY",   "group": "dimensions",   "sort": 20 },
    "oc_product.height":  { "tier": "PRIMARY",   "group": "dimensions",   "sort": 30 },
    "oc_product.weight":  { "tier": "PRIMARY",   "group": "dimensions",   "sort": 40 },
    "22": { "tier": "PRIMARY",   "group": "materials",    "sort": 10 },
    "51": { "tier": "PRIMARY",   "group": "construction", "sort": 10 },
    "20": { "tier": "PRIMARY",   "group": "operation",    "sort": 10 },
    "112": { "tier": "SECONDARY", "group": "materials",    "sort": 20 },
    "115": { "tier": "SECONDARY", "group": "construction", "sort": 20 },
    "23": { "tier": "HIDDEN",    "group": "hidden",       "sort": 0, "reason": "sink cluster — wrong family" },
    "28": { "tier": "HIDDEN",    "group": "hidden",       "sort": 0 },
    "29": { "tier": "HIDDEN",    "group": "hidden",       "sort": 0 }
  },
  "hidden_global_ref": true
}
```

*Schema illustration only — not deployed.*

---

## Evidence & limitations

| Item | Source |
| --- | --- |
| Attribute registry + category matrix | `BZPM-M8.1-ATTRIBUTE-INVENTORY-v1.md`, `.recovery-temp/bzpm-m8.1-audit.json` |
| DELETE/HIDE/KEEP actions | `BZPM-M8.2-CLEANUP-SPECIFICATION-v1.md` |
| TEST cleanup state | `SITE-002-M8.3-WAVE1-TEST-CLEANUP.md` |
| Packaging/SERVICE interim hide | `SITE-002-M8.3-WAVE2-TEST-CLEANUP.md`, `attribute_filter_visibility.php` |
| Strategic decisions | `BZPM-PRODUCT-ROADMAP-v1.md` ROAD-003…007 |
| Benchmark observations | `BZPM-OPERATOR-INSIGHTS-v1.md` FIM-W3Y-001…004 |
| Nested Столы URLs | `SITE-002-M7.1-TEST-DEPLOYMENT.md` |

## UNKNOWN / SECURITY RISK

- **UNKNOWN:** Full `oc_category` parent chain for all table subcategories (beyond URL samples) — subcategory override IDs not enumerated.
- **UNKNOWN:** Category «Столы с бортом» — example only; no `category_id` in repo evidence.
- **UNKNOWN:** Live post-Wave-2 SKU counts — M8.1 baseline (608 active after Wave 1) used.
- **UNKNOWN:** 4 attribute definition IDs missing from M8.1 export — classify before profile `hidden_global` finalized.
- **SECURITY RISK:** None — architecture document only; no credentials, no deploy.

---

*M9 Filter Profile System Architecture v1 — documentation only. No implementation performed. No commit authorized.*
