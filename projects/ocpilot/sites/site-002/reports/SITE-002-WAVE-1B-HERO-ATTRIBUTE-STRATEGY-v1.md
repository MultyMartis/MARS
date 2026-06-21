# SITE-002-WAVE-1B-HERO-ATTRIBUTE-STRATEGY-v1

**Site ID:** SITE-002 (ЗПМ)  
**Environment:** TEST — https://zpm.new-site.space/  
**Run:** Wave 1B — Hero Attribute Discovery  
**Date:** 2026-06-09  
**Mode:** Read-only — no storefront, DB, FTP, or admin changes  
**Evidence (local, not in repo):**  
`C:\AI MARS\.recovery-temp\site-002-w1b-db-final.json`,  
`site-002-w1b-families.json`,  
`site-002-w1b-hero-layout.json`,  
`site-002-w1b-stoly-rest.json`,  
`site-002-w1b-final2.json`

---

# REPORT — WAVE 1B HERO ATTRIBUTE DISCOVERY

## Executive summary

| Finding | Verdict |
|---------|---------|
| `SUPER_ATTS` = IDs **12, 13, 15** | **Only ID 12 has data (8.9% catalog); 13 and 15 are empty** |
| Hero today (W1A.2 pilot стол) | **4 dimension rows** from `oc_product` L/W/H/weight — SUPER_ATTS not rendered on pilot SKU |
| Catalog attribute fill | **Strong** for neutral-equipment attrs (87–98%); **weak** for SUPER_ATTS and packaging duplicates |
| Thermal / cold families on TEST | **0 active SKUs** — family-specific hero rules **cannot be validated from live data** |
| Layout ratio @ 1440px | **Within target** for Media and Buy Box; Content **~2 pp below** target band |

**Recommendation headline:** Keep universal **L/W/H/weight** in Hero; **replace** global `SUPER_ATTS` with **family-specific attribute ID lists** keyed by category path; do **not** expand IDs 13/15 until CMS fill exists.

---

## Task 1 — SUPER_ATTS inventory

**Source:** `config.php` via FTP (read-only) + `polygonws_zpm` DB.

```php
define('SUPER_ATTS', array(12,13,15));
```

**Mechanism (documented architecture):** `catalog/controller/product/product.php` builds `$data['super_atts']` from `oc_product` dimensions first, then appends attributes whose `attribute_id` is in `SUPER_ATTS`.

| ID | Attribute | Group | Example value | Coverage % (609 active SKUs) | Classification |
|----|-----------|-------|---------------|----------------------------|----------------|
| **12** | Габариты нетто (мм) | Габариты | `1000х1000х400` | **8.9%** (54 SKUs) | **AVOID** (duplicates L/W/H on most SKUs) |
| **13** | Габариты брутто (мм) | Габариты | — | **0%** | **AVOID** |
| **15** | Гарантия | Общие | — | **0%** | **AVOID** |

**Notes**

- On W1A.2 pilot PDP (`СП-П-18/6`), Hero shows **only** controller-injected dimensions (Длина/Ширина/Высота/Масса from `oc_product`); none of 12/13/15 appear because they are empty on that SKU.
- ID 12 overlaps semantically with L/W/H already surfaced from product fields → low incremental value.

---

## Task 2 — Attribute landscape

### Catalog scale (2026-06-09, TEST DB)

| Metric | Value |
|--------|------:|
| Active products (`status=1`) | **609** |
| Total products (incl. inactive) | 3 134 |
| Attribute definitions | **60** |
| Attribute groups (with attrs) | **4** registered in use |
| `oc_product_attribute` rows | ~10 175 |

### Attribute groups

| Group | Attributes in group |
|-------|--------------------:|
| Другое | 37 |
| Нейтральное оборудование | 13 |
| Общие | 8 |
| Габариты | 2 |

**SAFE UNKNOWN:** Separate attribute groups for «Тепловое» / «Холодильное» equipment are **not present** in DB — taxonomy is ZPM-neutral-centric.

### Top used attributes (active catalog, global)

| ID | Attribute | Group | Usage | Coverage % |
|----|-----------|-------|------:|-----------:|
| 21 | Конструкция | Общие | 599 | 98.4 |
| 33 | Тип опоры | Нейтральное оборудование | 580 | 95.2 |
| 26 | Ножки | Общие | 579 | 95.1 |
| 25 | Наличие борта | Нейтральное оборудование | 569 | 93.4 |
| 31 | Регулируемость опоры по высоте (max мм) | Нейтральное оборудование | 545 | 89.5 |
| 22 | Материал столешницы | Нейтральное оборудование | 535 | 87.8 |
| 20 | Макс. нагрузка (до, кг) | Общие | 427 | 70.1 |
| 51 | Конструкция полки | Другое | 435 | 71.4 |

### Rare / empty attributes (global)

**Empty (0% fill, selected):** 13, 14, 15, 16, 32, 35, 55, 102, 103, 104, …

**Test / junk attrs (≤0.2%):** 105–111 (`шир ТЕСТ`, `выс ТЕСТ`, `дл ТЕСТ`, …) — **do not use in Hero**.

**Misleading high-use field:** ID 43 «Дополнительные сведения» — often contains price notes / ops text, not buyer-facing specs → **specs tab only**.

### Universal dimension fields (`oc_product`, not attributes)

| Field | Filled | Coverage % |
|-------|-------:|-----------:|
| length | 586 | **96.2** |
| width | 586 | **96.2** |
| height | 586 | **96.2** |
| weight | 531 | **87.2** |

These are the **primary Hero-safe** fields today.

---

## Task 3 — Family analysis

**Method:** Family coverage = `filled SKUs in family / SKUs in family`.  
Category path used where reliable; «Столы» matched via category name (`LIKE '%Стол%'`) because direct `category_id` assignment returned 0 for candidate IDs 81/85/87.

| Family | SKUs (active) | Data quality | Key decision attributes (from catalog) |
|--------|--------------:|--------------|----------------------------------------|
| **Моечные ванны** | **152** (cat path `80`) | Good | Размер раковины (29), Мойка (23), Отверстие под смеситель (28), Наличие борта (25), Конструкция борта (47) |
| **Столы** | **420** (name match) | Good | L/W/H (product fields), Материал столешницы (22), Конструкция полки (51), Макс. нагрузка (20), Конструкция (21) |
| **Нейтральное оборудование** | **609** (root `79` = entire TEST catalog) | Good for ZPM-owned lines | Same as global top attrs; sink/table attrs dominate |
| **Тепловое оборудование** | **0** | **No data on TEST** | SAFE UNKNOWN |
| **Холодильное оборудование** | **0** | **No data on TEST** | SAFE UNKNOWN |

### Моечные ванны (152 SKUs) — family-relative coverage

| Attribute | Family coverage % | Helps selection? |
|-----------|------------------:|----------------|
| Размер раковины (ДхШхВ, мм) — **29** | **96.7** | Yes — primary bowl geometry |
| Мойка — **23** | **98.0** | Yes — construction type |
| Отверстие под смеситель — **28** | **98.0** | Yes |
| Наличие борта — **25** | **98.0** | Yes |
| Конструкция — **21** | **98.0** | Yes — разборная/сварная |
| Конструкция борта — **47** | **71.1** | Conditional |
| Габариты нетто (мм) — **12** | **21.1** | No — redundant vs L/W/H |
| «Количество секций» | **Not in DB** | Closest: «Размер секции» (30) **0.5%**, «Назначение секции» (24) **0.7%** → **AVOID** |

### Столы (420 SKUs) — family-relative coverage

| Attribute | Family coverage % | Helps selection? |
|-----------|------------------:|----------------|
| L / W / H (`oc_product`) | **~100** (inherited from neutral dims fill rate) | Yes — primary |
| Материал столешницы — **22** | **100.0** | Yes |
| Конструкция полки — **51** | **100.0** | Yes — shelf/no shelf |
| Макс. нагрузка — **20** | **99.8** | Yes |
| Конструкция — **21** | **100.0** | Yes |
| Тип опоры — **33** | **100.0** | Yes |
| Материал полки — **112** | **89.8** | Conditional |
| Усиление — **115** | **89.8** | Conditional |
| Высота борта — **18** | **39.4** | Avoid in Hero (border subset only) |

### Нейтральное оборудование (609 SKUs)

On TEST, category `79` spans **all active products** — treat as **manufacturer default family**, not a narrow UX slice. Hero strategy should branch on **child categories** (80 sinks, 87 production tables, 83 racks, etc.), not root `79`.

### Тепловое / Холодильное

Categories exist (`category_id` **90**, **95**) but **`COUNT(active products) = 0`**.  
**Cannot** derive Hero attributes from catalog data on this environment. Re-run discovery when TEST catalog includes representative SKUs.

---

## Task 4 — Hero candidates (data-backed only)

### Моечные ванны

| Priority | Attributes (attribute_id) | Rationale |
|----------|---------------------------|-----------|
| **A** | L/W/H + weight (product fields); **Размер раковины (29)** | 96%+ family fill; bowl size is primary filter |
| **A** | **Мойка (23)**, **Отверстие под смеситель (28)** | 98% fill |
| **B** | **Наличие борта (25)**, **Конструкция борта (47)** | 98% / 71% |
| **B** | **Конструкция (21)** | 98% |
| **C** | **Тип опоры (33)**, **Регулируемость опоры (31)** | 75%+ in family |
| **C** | **Макс. нагрузка (20)** | 12.8% in family — **AVOID** despite global 70% |

*Not recommended:* «Количество секций» — **attribute absent**; «Размер секции» / «Назначение секции» &lt;1% fill.

### Столы

| Priority | Attributes | Rationale |
|----------|------------|-----------|
| **A** | L/W/H + weight (product fields) | 96%+ global |
| **A** | **Материал столешницы (22)**, **Конструкция полки (51)** | 100% in family |
| **B** | **Макс. нагрузка (20)**, **Конструкция (21)** | ~100% |
| **B** | **Тип опоры (33)** | 100% |
| **C** | **Материал полки (112)**, **Усиление (115)** | 89.8% — conditional |
| **C** | **Наличие борта (25)** | 100% but often «нет» — secondary |

### Нейтральное оборудование (other sub-lines)

Use **sub-category** profiles (стеллажи, полки, тележки, шкафы) in a future pass — root-level attrs mix table/sink/rack semantics. **Defer** a single Hero list for cat `79`.

### Тепловое / Холодильное

**SAFE UNKNOWN** — no active SKUs on TEST.

---

## Task 5 — Coverage validation (proposed Hero fields)

Coverage thresholds: **90–100% SAFE** | **70–89% CONDITIONAL** | **&lt;70% AVOID**

### Universal (all families with ZPM neutral goods)

| Field | Coverage % | Class |
|-------|----------:|-------|
| Длина (product.length) | 96.2 | SAFE |
| Ширина (product.width) | 96.2 | SAFE |
| Высота (product.height) | 96.2 | SAFE |
| Масса (product.weight) | 87.2 | CONDITIONAL |

### Current SUPER_ATTS

| ID | Coverage % | Class |
|----|----------:|-------|
| 12 Габариты нетто | 8.9 | AVOID |
| 13 Габариты брутто | 0.0 | AVOID |
| 15 Гарантия | 0.0 | AVOID |

### Family-specific (validated subsets)

| Family | Attribute | Family coverage % | Class |
|--------|-----------|------------------:|-------|
| Sinks | Размер раковины (29) | 96.7 | SAFE |
| Sinks | Мойка (23) | 98.0 | SAFE |
| Tables | Материал столешницы (22) | 100.0 | SAFE |
| Tables | Конструкция полки (51) | 100.0 | SAFE |
| Tables | Макс. нагрузка (20) | 99.8 | SAFE |
| Sinks | Габариты нетто (12) | 21.1 | AVOID |

**Do not recommend** weak fields: 12, 13, 15, 43 (ops notes), test attrs 105–111, packaging duplicates 44–46 for Hero (high fill but low decision value vs L/W/H).

---

## Task 6 — Current W1A.2 Hero layout review

**URL measured:** pilot стол `СП-П-18/6`  
**Viewport:** 1440×900  
**Evidence:** `site-002-w1b-hero-layout.json`

| Zone | Selector | Width px | % of `.product-hero__layout` (1325px) | Target % | Status |
|------|----------|--------:|--------------------------------------:|---------:|--------|
| Media | `.product-hero__media` | 379.5 | **28.6%** | 25–30% | **OK** |
| Content | `.product-hero__identity` | 569.25 | **43.0%** | 45–50% | **Slightly low (−2 pp)** |
| Buy Box | `.product-hero__buybox` | 316.25 | **23.9%** | 20–25% | **OK** |

**CSS grid:** `grid-template-columns: 379.5px 569.25px 316.25px`  
**Areas:** `"context context context" "media identity buybox"`

**Hero attribute cells on pilot:** 4 rows (Длина, Ширина, Высота, Масса) — matches controller logic; **no SUPER_ATTS** rendered.

**Document only — no layout change in Wave 1B.**

---

## Task 7 — Universal Hero strategy

### 1. What should always be shown

- **Артикул** (`model`) — already in Hero meta.
- **Status / price / cart** — buy-box block (W1A.2).
- **Dimensions:** Длина, Ширина, Высота when &gt;0 in `oc_product` (**96.2%** fill).
- **Масса** when &gt;0 (**87.2%** — show with fallback «—» acceptable).

### 2. What should be family-specific

Implement **category-path → attribute ID list** (max **4** attrs beyond dimensions to fit 8-cell grid target from Wave 1A map):

| Family key | Category signal | Recommended SUPER_ATTS replacement IDs |
|------------|-----------------|--------------------------------------|
| `sinks` | path contains cat **80** | **29**, **23**, **28**, **25** (optional **47**) |
| `tables` | name/path «Стол» | **22**, **51**, **20**, **21** |
| `racks` / `shelves` | cats **83**, **88**, … | **Future pass** — distinct attrs (уровни, нагрузка полки) |
| `thermal` | cat **90** | SAFE UNKNOWN (no SKUs) |
| `cold` | cat **95** | SAFE UNKNOWN (no SKUs) |

### 3. What stays in specifications only

- Packaging block: 44–46, 52–54, 56, 57  
- «Дополнительные сведения» (43)  
- Комплект поставки / отгрузки (48, 58)  
- Страна производства (34), Стандарт (42)  
- Duplicate габариты attrs 12, 13  
- All **empty** and **ТЕСТ** attributes  

### 4. Should SUPER_ATTS remain?

**Yes, as a pattern** — config-driven allowlist filtered in `product.php` — but **not** the current global list `(12,13,15)`.

### 5. Family-specific SUPER_ATTS needed?

**Yes.** Global list fails on coverage and semantics:

- 13/15 unused in entire catalog  
- 12 redundant with product L/W/H  
- Decision attrs differ by family (bowl size vs shelf vs rack levels)

**Proposed config shape (documentation only — not implemented):**

```php
// Illustrative — Wave 1C+ implementation
define('SUPER_ATTS_DEFAULT', array());
define('SUPER_ATTS_BY_CATEGORY', array(
  80 => array(29, 23, 28, 25),   // моечные ванны
  // 'stoly' => array(22, 51, 20, 21), // resolve leaf category IDs
));
```

Controller must resolve **nearest ancestor** match in `oc_category_path`.

### 6. Risks and limitations

| Risk | Impact | Mitigation |
|------|--------|------------|
| TEST catalog lacks thermal/cold SKUs | Hero rules unverified for 2 requested families | Re-run 1B when products imported |
| «Столы» matched by name, not single `category_id` | Coverage accurate; routing must mirror same rule | Align with SEO category paths under `87` |
| 609 vs 134 products vs Run 5 baseline | Catalog grew or counting method differed | Use **609 active** as denominator for this report |
| Attribute 43 pollution | Ops/price text in «specs» | Exclude from Hero allowlists |
| 8-cell Hero grid vs 4 dims + 0 SUPER_ATTS today | Pilot стол shows **4 cells only** | Family attrs add 2–4 cells; cap at 8 with «—» placeholders (Wave 1C decision) |
| Content column 43% vs 45–50% target | Minor UX imbalance | Layout tuning deferred (post–1B, frozen now) |

---

## SAFE UNKNOWN

| Item | Why unknown | What would verify |
|------|-------------|-------------------|
| Hero rules for **тепловое** / **холодильное** | 0 active products in cats 90/95 on TEST | Import pilot SKUs; re-run family SQL |
| Exact **`category_id`** for «Столы» in path table | IDs 81/85/87 returned 0 products; name match → 420 | Map `oc_category_path` to leaf «Столы производственные» (`87` suspected) |
| Full **60-attribute** inventory in one export | PMA parser returned partial pages in some runs | Single SQL export via phpMyAdmin UI |
| Production vs TEST catalog parity | Only TEST examined | Compare prod DB when authorized |
| «Количество секций» as Hero field | **Attribute does not exist** in DB | Create attribute + 1C fill if business requires |

---

## Deliverables checklist

| Deliverable | Status |
|-------------|--------|
| SUPER_ATTS analysis | Done |
| Attribute inventory | Done (60 attrs; partial empty list) |
| Family analysis (5 families) | Done — 3 with data, 2 SAFE UNKNOWN |
| Coverage statistics | Done |
| Hero recommendations | Done |
| Hero ratio measurements | Done |
| Strategy document (this file) | Done |

---

## Git / storefront

| Action | Status |
|--------|--------|
| Git commit | **NO** |
| Git push | **NO** |
| Storefront changes | **NO** |
| Database writes | **NO** |

---

*Wave 1B — read-only discovery. Implementation belongs to Wave 1C+ after operator approval.*
