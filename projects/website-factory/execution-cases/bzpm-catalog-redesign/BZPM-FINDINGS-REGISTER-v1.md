# BZPM Findings Register v1

**Execution case:** `bzpm-catalog-redesign`  
**Date:** 2026-06-08  
**Rule:** Hypotheses are **not** promoted to facts without evidence class upgrade.  
**Sources:** W0, W1A, W1B, W1C, W1D, W2 audit reports (consolidated 2026-06-08)

---

## Classification legend

| Class | Meaning |
|-------|---------|
| **OBSERVED FACT** | Directly evidenced on site, repo, or market fetch |
| **WORKING HYPOTHESIS** | Inference from observations; not validated |
| **VALIDATED BY MARKET** | Hypothesis tested against W1D competitor evidence |
| **REJECTED** | Hypothesis contradicted by evidence |
| **UNKNOWN** | Insufficient evidence |

---

## OBSERVED FACTS

### W0 — MARS Audit

| ID | Finding |
|----|---------|
| W0-F-01 | BZPM (ORG-0005) and SIBCAR/SITE-001 (ORG-0006) are **different organizations and projects** |
| W0-F-02 | `bzpm-catalog-redesign` was **not registered** in execution-cases-registry before this consolidation |
| W0-F-03 | Website Factory is documented methodology; **no in-pack runtime** exists |
| W0-F-04 | ATLAS holds ORG-0005, PRJ-0009 (active catalog platform), PRJ-0010 (deprecated), WEB-ZPM-01 |
| W0-F-05 | OCPilot pack contains **no BZPM references** — OpenCart experience is SITE-001 only |

### W1A — Product Audit

| ID | Finding |
|----|---------|
| W1A-F-01 | PDP functions as **single-SKU card**, not in-page selection tool |
| W1A-F-02 | Hero shows **4 selected props** (L×W×H×mass) on all checked PDPs |
| W1A-F-03 | Placeholder mini-description visible in hero: «это надо сделать дополнительным мини-описанием товара» |
| W1A-F-04 | Demo brand logo (AssuM) shown in hero |
| W1A-F-05 | Tabs: Описание (default) / Характеристики / Документы; specs **hidden until tab switch** |
| W1A-F-06 | «Похожие товары» on sink PDP shows **котломойки** (ВКС-*), not ПРЕМИУМ-3 siblings |
| W1A-F-07 | Compare and wishlist present as **icon-only** controls |
| W1A-F-08 | Gallery: **1 image**, CSS height **520px** (460px at ≤1024px), `object-fit: contain` |
| W1A-F-09 | Reference table URL (`stol-proizvodstvennyj-spb-s-12-6-1200h600h850`) returned **404** at audit time |
| W1A-F-10 | Breadcrumbs provide **4-level** hierarchy to SKU |
| W1A-F-11 | Article copy-to-clipboard pattern present |
| W1A-F-12 | Stock quantity shown («В наличии: N шт.») |

### W1B — Category Audit

| ID | Finding |
|----|---------|
| W1B-F-01 | Listing card fields: status, article, name, price, CTA, compare/fav icons — **no structured differentiators** |
| W1B-F-02 | Parent «Моечные ванны»: **18 chips** + **~36 filter groups** + **15 SKU/page**, 11 pages pagination |
| W1B-F-03 | Filter «Подкатегории»: **44 checkboxes**; chips show **18** — sets **do not match** |
| W1B-F-04 | Series «ПРЕМИУМ-3»: **10 SKU**, **~21 filter groups**; price/height sliders **degenerate** (min=max) |
| W1B-F-05 | Chip icons use `placeholder-400x400.png`; CSS hides `.zpm-sub-cat-chip__icon` |
| W1B-F-06 | Parent category **mixes 5 product families** on page 1 (ВМЦ, ВМС, ВКС…) |
| W1B-F-07 | Compare page empty state: H1 «Личный кабинет» — compare mixed with account context |
| W1B-F-08 | Status duplicated in `p-card__top` and `p-card__body` (body copy hidden via CSS) |
| W1B-F-09 | «Под заказ» cards use same `p-card--in-stock` class as in-stock |
| W1B-F-10 | Filters require «Показать товары» button; no active-filter chips in results zone |
| W1B-F-11 | ≤1024px: filters in **fullscreen overlay** behind «Фильтры» button |

### W1C — Buyer Decision Flow

| ID | Finding |
|----|---------|
| W1C-F-01 | Decision chain: **equipment type → family → series → SKU** |
| W1C-F-02 | `/katalog` shows **9 top-level category cards**, not product listing |
| W1C-F-03 | Parent categories show **chips + flat SKU grid simultaneously** |
| W1C-F-04 | Search `ВМЦ-П3-2/500` **finds SKU**; search «моечная ванна» returns **15 results including котломойки** |
| W1C-F-05 | Search `1150×700×850` returns **4 SKUs from 4 series** (L, P, P3, S) |
| W1C-F-06 | Search «мойка производственного участка» returns **empty grid** |
| W1C-F-07 | Series page: **H1 only**, no series description block |
| W1C-F-08 | PDP placeholder subtitle and «Похожие» котломойки confirmed on decision-path audit |
| W1C-F-09 | Compare infrastructure exists (`/compare-products`, `data-compare-toggle`) |
| W1C-F-10 | `/katalog` SEO text describes zones (мойка, подготовка, хранение) **without interactive task navigation** |

### W1D — Competitor Intelligence (market OBSERVED FACTS)

| ID | Finding |
|----|---------|
| W1D-F-01 | Trapeza: **product database** model — category tree + faceted filters + brand index + rich PDP |
| W1D-F-02 | Trapeza sinks: **functional subtaxonomy** (рукомойники, жироуловители…), not OEM series chips |
| W1D-F-03 | Trapeza sink filters include **«Количество секций»**, **«Наличие крышки»**, **«По наличию»** |
| W1D-F-04 | Trapeza PDP: **Модель** field + **«Все товары [Brand]»** link; no sibling SKU matrix observed |
| W1D-F-05 | Abat: category-by-type + lines 700/900; **«Где купить»** — dealer path; no catalog compare/filters observed |
| W1D-F-06 | Hoshizaki: **deep series tree + dense faceted filters** (capacity, ice type, doors…) |
| W1D-F-07 | Henny Penny: **application-first** + **«Find Your Fryer»** wizard; series landing has decision copy |
| W1D-F-08 | Electrolux Professional: **compare tray capped at 4** products site-wide |
| W1D-F-09 | **Sibling SKU matrix on PDP** — not observed at Trapeza, Abat, or sampled manufacturers |
| W1D-F-10 | **Thin listing cards** — common at Trapeza and Hoshizaki |

### W2 — Information Density

| ID | Finding |
|----|---------|
| W2-F-01 | PDP gallery: 520px fixed height, **1 slide**, no thumbnails |
| W2-F-02 | PDP hero: 2-column grid, `justify-content: space-between` |
| W2-F-03 | Spec tab: **20+ rows**; 2 of 3 tabs hidden at load |
| W2-F-04 | `p-card` padding-top `calc(var(--pad-box) * 5)` ≈ 100px |
| W2-F-05 | `p-card__delivery` **empty** on all checked cards |
| W2-F-06 | `/katalog`: 9 cards `min-height: 300px` + certificates + advantages + dealer form + SEO block |
| W2-F-07 | Certificates + dealer form **repeat** on category pages |
| W2-F-08 | «Моечные ванны»: taxonomy on **3 surfaces** — chips, filter «Подкатегории», breadcrumbs/URL |
| W2-F-09 | Dimensions appear on **4 surfaces**: title, hero props, spec tab, filter groups |
| W2-F-10 | Series «ПРЕМИУМ-3» page: **less fragmented** than parent (no chips, 10-SKU coherent grid) |
| W2-F-11 | Owner feedback triangulation: «empty space» **partially confirmed** on PDP/top catalog; «under-informative» **mixed** (specs exist but hidden); «scattered» **confirmed** |

---

## WORKING HYPOTHESES

| ID | Source | Hypothesis |
|----|--------|------------|
| WH-01 | W1C | New buyer can reach family but **lacks guided series choice** |
| WH-02 | W1C | Overlapping taxonomies (series × sections × type) **increase cognitive load** |
| WH-03 | W1C | Nomenclature code carries decisions but site **does not decode** for buyer |
| WH-04 | W1C | Expert with article code **reaches PDP in one step** |
| WH-05 | W1C | Dimension filter/search works; **series choice unsupported** after narrowing |
| WH-06 | W1C | Compare exists but listing **too thin** for meaningful pre-PDP choice |
| WH-07 | W1C | «Похожие товары» **do not support in-series decision flow** |
| WH-08 | W1C | No **task-first self-serve path** for production-task queries |
| WH-09 | W1C | Parallel chips + full grid **reduces likelihood** of series-first navigation |
| WH-10 | W1C | Site behaves as **product database with filters**, not guided selection system |
| WH-11 | W1A | PDP «похожие» block **breaks selection path** (critical business impact) |
| WH-12 | W1A | No in-page sibling matrix **increases bounce** on multi-SKU series |
| WH-13 | W1A | Missing series context on first screen **risks wrong-series purchase** |
| WH-14 | W1A | Selected props = L×W×H only **insufficient** for category-critical decisions |
| WH-15 | W1A | B2B conversion context missing near CTA **leaks dealer/project buyers** |
| WH-16 | W2 | «Empty space» feeling on PDP **linked to gallery height + hero layout**, not missing backend data |
| WH-17 | W2 | Listing under-informativeness **linked to thin cards**, not absent filters |
| WH-18 | W2 | Repeated footer blocks **reduce incremental information per scroll** |
| WH-19 | W2 | Placeholder content **amplifies perceived under-informativeness** |
| WH-20 | W2 | BZPM **matches market** on thin cards but **below Trapeza** on card semantic fields |

---

## VALIDATED BY MARKET

*(W1C/W1A/W1B hypotheses reclassified per W1D evidence)*

| ID | Original | Status | Market evidence |
|----|----------|--------|-----------------|
| V-01 | WH-01 | **Supported** | Trapeza/Abat: no series guide for sinks; functional subcats + filters |
| V-02 | WH-03 | **Supported** | Trapeza uses brand/model; OEM codes not decoded on cards — common OEM gap |
| V-03 | WH-04 | **Supported** | Trapeza product code + search; standard database behavior |
| V-04 | WH-05 | **Supported** | Trapeza section/dimension filters; multi-brand same-size remains buyer burden |
| V-05 | WH-06 | **Supported** | Trapeza: brand/model on listing; full specs on PDP/compare |
| V-06 | WH-08 | **Supported** | No task wizard on Trapeza; Henny Penny wizard is rare exception |
| V-07 | WH-09 | **Supported** | Trapeza marketplace: subcats + flat listing pattern |
| V-08 | WH-10 | **Supported** | Trapeza primary = product database; manufacturers add consultative layers |
| V-09 | W1A PS-02 | **Supported** | Trapeza → brand catalog; Abat → dealer; sibling matrix **not market standard** |
| V-10 | W1A IA-01 | **Supported** | Thin hero props common; Trapeza uses category-specific chips on homepage |
| V-11 | W1B parent grid mix | **Supported** | Trapeza multi-brand flat listings typical |
| V-12 | W2 thin cards | **Supported** | Trapeza, Hoshizaki thin cards = market norm |

---

## REJECTED

| ID | Original | Status | Evidence |
|----|----------|--------|----------|
| X-01 | W1A FS-01 (partial) | **Partially contradicted** | Trapeza import PDP shows brand+model on first screen; **BZPM OEM series gap remains real** in own-catalog context |
| X-02 | WH-02 | **Not market-wide** | Chip overlap is BZPM-specific; Trapeza avoids series×sections on one chip row |
| X-03 | W1A PS-01 / WH-07 market norm | **Insufficient** | Trapeza sample PDP: no similar block; market prevalence unknown |
| X-04 | Copy Trapeza directly | **Rejected** | Decision D-03/R-01 — different business model |

---

## UNKNOWN

| ID | Topic | Why unknown |
|----|-------|-------------|
| U-01 | Production stack PRJ-0009 (CMS/framework) | Not in MARS repo |
| U-02 | Compare table populated UX | Requires JS session |
| U-03 | Filter AJAX behavior (counts, active chips) | Static HTML audit only |
| U-04 | Mobile touch targets / text clipping | No device render |
| U-05 | Backend rules for «Похожие товары» | Only storefront result observed |
| U-06 | `p-card__delivery` — empty by design or missing data | Span present, no text |
| U-07 | Trapeza search Cyrillic UX | Test query returned empty/redirect |
| U-08 | Abat deep product pages | 404 on curl |
| U-09 | Owner feedback root cause | Layout vs content vs taxonomy — no user testing |
| U-10 | W1 screenshots in repo | Not found; mobile = CSS inference |
| U-11 | `/custom-equipment` task-path content | Not traced in W1C |
| U-12 | Polygon WIP vs audit state | Operator work may be outside repo |

---

## Priority findings (cross-phase)

| Rank | IDs | Theme | Class |
|------|-----|-------|-------|
| 1 | W1A-F-06, WH-07, V-12 | «Похожие» breaks in-series selection | OBSERVED + HYPOTHESIS |
| 2 | W1A-F-12 area, V-09 | No sibling SKU matrix | VALIDATED BY MARKET as non-standard |
| 3 | W1C-F-03, WH-09 | Chips + flat grid on parent categories | OBSERVED + HYPOTHESIS |
| 4 | W1C-F-02 area, W1B-F-02 | 18+ overlapping subcategories | OBSERVED FACT |
| 5 | W1A-F-03, W2-F-11 | Placeholder content erodes trust | OBSERVED FACT |
| 6 | W1B-F-01, W2-F-04 | Thin listing cards | OBSERVED + VALIDATED |
| 7 | W2-F-01, W2-F-02 | PDP space/info mismatch | OBSERVED FACT |
| 8 | W2-F-08 | Information fragmentation across surfaces | OBSERVED FACT |
| 9 | W1A-F-05, W2-F-03 | Rich specs hidden in inactive tabs | OBSERVED FACT |
| 10 | W2-F-07 | Repeated commercial blocks | OBSERVED FACT |

---

*BZPM Findings Register v1 — do not promote hypotheses without evidence upgrade.*
