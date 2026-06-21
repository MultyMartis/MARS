# REPORT — BZPM W5 BLUEPRINT

**Execution case:** `bzpm-catalog-redesign`  
**Document:** `BZPM-BLUEPRINT-v1`  
**Date:** 2026-06-08  
**Lane:** A (Website Factory)  
**Mode:** Blueprint only — no UI, no visual design, no implementation  
**Source of truth:** [BZPM-REDESIGN-ARCHITECTURE-v1.md](BZPM-REDESIGN-ARCHITECTURE-v1.md)  
**Evidence base:** W0–W2 findings ([BZPM-FINDINGS-REGISTER-v1.md](BZPM-FINDINGS-REGISTER-v1.md))

**Rule:** Blueprint describes **what** appears, **when** it appears, and **why** — not **how** it looks.

---

## Executive Summary

This document translates [BZPM-REDESIGN-ARCHITECTURE-v1](BZPM-REDESIGN-ARCHITECTURE-v1.md) into **page-level information block contracts** for six catalog surfaces: catalog root, category (mid-level and parent), series, listing card, PDP, and commercial blocks.

**Blueprint scope:**

| Surface | Block count (v1) | Primary buyer action |
|---------|------------------|----------------------|
| Catalog Root | 6 blocks | Select equipment class |
| Mid-level Category | 5 blocks | Select product family |
| Parent Category | 9 blocks | Select series or scoped browse |
| Series Page | 8 blocks | Compare SKUs within one OEM line |
| Listing Card | 1 contract (4 field tiers) | Open PDP / compare / skip |
| PDP | 7 zones, 22 blocks | Evaluate single SKU and convert |
| Commercial Blocks | 4 tiers, 12 block types | Contextual trust and procurement |

**Architectural invariants carried into every blueprint:**

1. **Navigation intent ≠ selection intent** — root and parent categories orient; series and PDP execute selection.
2. **One primary selection surface per page** — no parallel chip/filter/breadcrumb taxonomy redundancy.
3. **Single information owner** — each fact type has one primary surface; secondary surfaces link or summarize.
4. **Commercial blocks tiered** — global trust once at entry; contextual signals at choice points; deep-page repeats suppressed.

**Explicitly not in this blueprint:** visual layout, wireframes, responsive breakpoints, OpenCart tasks, Twig/CSS/JS, nomenclature decoding (D-02), sibling SKU matrix (V-09), task-first wizards (WH-08).

---

## Section A — Catalog Root Blueprint

**Page:** `/katalog` — Catalog Root  
**Page mode:** Type-selection entry point (navigation page, not listing)

### User goal

Orient to **equipment class** and enter the decision chain: equipment type → family → series → SKU (W1C-F-01).

### Primary action

**Select one of 9 top-level category cards** → navigate to correct family in ≤1 click.

### Block sequence

```text
1. Orientation Block
2. Breadcrumb Anchor Block
3. Type Navigation Block          ← primary zone
4. Light Procurement Reference Block
5. Trust Summary Block
6. SEO Reference Block            ← below fold only
```

---

### Block 1 — Orientation Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Answer «where am I» and state catalog purpose in one glance |
| **Status** | **Mandatory** |
| **Input** | CMS page title; catalog purpose copy (1 line) |
| **Output** | Buyer understands this is the catalog entry, not a product listing |
| **Success condition** | Buyer can name the page role without scrolling past type navigation |

**When:** Always, above fold.  
**Why:** W2 Screen Consumption — moderate density; type navigation must not compete with ambiguous H1 (W2-F-06).

---

### Block 2 — Breadcrumb Anchor Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Position buyer in site information architecture |
| **Status** | **Mandatory** |
| **Input** | Site hierarchy: Главная → Каталог |
| **Output** | Navigable path to home |
| **Success condition** | Buyer can return to home in 1 action |

**When:** Always, top of page.  
**Why:** W1A-F-10 breadcrumb pattern; hierarchy anchor for all catalog paths.

---

### Block 3 — Type Navigation Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Enable D1 (equipment type decision) — route buyer to one of 9 equipment classes |
| **Status** | **Mandatory** |
| **Input** | 9 top-level categories: name, representative image, optional SKU count per category |
| **Output** | Navigation to selected family/category page |
| **Success condition** | Buyer reaches intended equipment class in ≤1 click; counts validate scope without opening category |

**When:** Always; primary above-fold zone.  
**Why:** W1C-F-02 (9 category cards, not listing); core catalog root function.

**Must NOT contain:** SKU grid, faceted filters, series chips, subcategory taxonomy.

---

### Block 4 — Light Procurement Reference Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Surface B2B procurement paths without full-form scroll cost |
| **Status** | **Mandatory** |
| **Input** | Links: Дилерам · Доставка · Консультация (header-adjacent or compact strip) |
| **Output** | Buyer aware of dealer/delivery/consultation paths |
| **Success condition** | B2B buyer sees self-serve procurement entry without encountering full dealer form |

**When:** Always, compact — not full-page form.  
**Why:** CV-01, W2 Commercial — B2B context missing at entry today; full form repeats on subpages (W2-F-07).

---

### Block 5 — Trust Summary Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Establish manufacturer trust (ЗПМ as OEM) once per catalog session path |
| **Status** | **Mandatory** (compact form) |
| **Input** | «Сделано в России», certification reference — summary or link to detail |
| **Output** | Trust signal at first catalog touch |
| **Success condition** | Buyer receives trust signal without full certificate slider scroll |

**When:** Below type grid OR linked modal — not competing with type navigation.  
**Why:** W2-F-07 — full slider on every subpage is wasteful; trust needed once at entry.

**Variant:** **Optional** expansion to full certificates — via link to dedicated page/modal, not inline slider.

---

### Block 6 — SEO Reference Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Search/indexing value; zone description for production areas (мойка, подготовка, хранение) |
| **Status** | **Optional** (content exists today) |
| **Input** | Long-form zone description text |
| **Output** | Indexable reference content |
| **Success condition** | SEO content does not appear above type navigation; buyer acting on type selection does not need to scroll through this block first |

**When:** Below fold only.  
**Why:** W1C-F-10 — SEO text without interactive task navigation; must not compete with D1.

---

### Catalog Root — Suppressed blocks

| Block | Status | Why suppressed |
|-------|--------|----------------|
| Product SKU grid | **Removed** | Conflicts with type-selection role (W1C-F-02) |
| Faceted filters | **Removed** | Belongs to family/series surfaces (W1B-F-02) |
| Full dealer application form | **Removed** | Replaced by Light Procurement Reference (W2-F-07) |
| Duplicate advantages grids (top + bottom) | **Removed** | Wasteful scroll; themes repeat header nav (W2 duplication) |
| Series-level chips | **Removed** | Taxonomy one level down (W2-F-08) |
| Task-first wizard | **Removed** | Out of v1 scope (W1C-F-10, WH-08) |
| Placeholder / demo content | **Removed** | Trust erosion (W1A-F-03, W1A-F-04) |

### Catalog Root — Buyer path matrix

| Buyer state | Intended action | Blueprint block involved |
|-------------|-----------------|--------------------------|
| Knows equipment class | Select category card | Type Navigation Block |
| Unsure of class | Read type names/images → select OR use header search | Type Navigation Block + header (out of page scope) |
| Expert with article code | Bypass root via search | Root does not obstruct — no mandatory blocks below fold required |
| B2B / dealer | Notice procurement links | Light Procurement Reference Block |

---

## Section B — Category Blueprint

**Page types:** Mid-level category (family hub) and parent category (series gateway).  
**Examples:** «Нейтральное оборудование» (mid-level) · «Моечные ванны» (parent).

### Category page mode matrix

| Level | Example | Page mode | Primary action |
|-------|---------|-----------|----------------|
| **Mid-level** | Нейтральное оборудование | Navigation page | Select product family (subfamily) |
| **Parent / family** | Моечные ванны | Navigation-primary, selection-secondary | Select series OR scoped flat browse |
| **Leaf family** (no series children) | — | Selection page | Select SKU within family |

---

### B1 — Mid-level Category Blueprint (Нейтральное оборудование)

#### User goal

Route from equipment class to product family within class.

#### Primary action

Select one subfamily entry → enter family page.

#### Block sequence

```text
1. Orientation Block (H1 + class description)
2. Breadcrumb Block
3. Subfamily Navigation Block          ← primary
4. Listing Zone Block                  ← optional (mixed-family browse)
5. Below-listing Minimal Block
```

#### Block definitions

| # | Block | Status | Purpose | Input | Output | Success condition |
|---|-------|--------|---------|-------|--------|-------------------|
| 1 | **Orientation** | Mandatory | Define what belongs in this equipment class | H1 + 2–4 sentence class description | Buyer understands class scope | Buyer can distinguish this class from sibling classes |
| 2 | **Breadcrumb** | Mandatory | Hierarchy context | Full path from Главная | Navigable hierarchy | 4+ levels readable (W1A-F-10 pattern) |
| 3 | **Subfamily Navigation** | Mandatory | Route to families within class | Subfamily cards/chips with names (+ optional counts) — e.g. 5 chips per W2 neutral cat pattern | Navigation to parent family pages | Buyer reaches intended family in ≤1 click |
| 4 | **Listing Zone** | Optional | Mixed-family browse when warranted | Product cards from multiple families | Scoped SKU browse | Only present when SKU count warrants; secondary to subfamily navigation |
| 5 | **Below-listing Minimal** | Optional | Pagination if listing present | Pagination controls | Page navigation | No full certificates/dealer repeat (W2-F-07) |

#### Information flow (mid-level)

```text
ENTER → read class scope (Orientation)
      → select subfamily (Subfamily Navigation) → EXIT to parent category
      OR (optional) browse mixed grid (Listing Zone) → EXIT to PDP
```

#### Navigation flow

Subfamily Navigation is **sole primary taxonomy surface** — no parallel filter «Подкатегории» row duplicating chips (P-02).

#### Selection flow

Selection is **deferred** — mid-level does not execute SKU choice; it routes to family.

#### Decision support flow

Class description answers «does my need fit this equipment type?» — not «which exact SKU?».

---

### B2 — Parent Category Blueprint (Моечные ванны)

#### User goal

Understand family scope; select OEM series OR browse within declared scope.

#### Primary action

Select series chip → enter series page (preferred path per P-03, WH-09).

#### Block sequence

```text
ABOVE LISTING
  1. Orientation Block (H1 + family description)     ← NEW
  2. Breadcrumb Block
  3. Series Navigation Block                         ← primary above-listing
  4. Scope Control Block (indicator + count + sort)
  5. Filter Access Block
  6. Active Filter Summary Block                   ← NEW

LISTING ZONE
  7. Product Grid Block                            ← secondary

BELOW LISTING
  8. Pagination Block
  9. Family Selection Guide Block                  ← optional
 10. Consultative CTA Block                         ← conditional
```

#### Block definitions — above listing

| # | Block | Status | Purpose | Input | Output | Success condition |
|---|-------|--------|---------|-------|--------|-------------------|
| 1 | **Orientation** | Mandatory | Define family boundaries — what belongs, what does not (моечная ванна vs котломойка vs рукомойник) | H1 + 2–4 sentence family description | Buyer understands family scope | Addresses W1C-F-07 absence; buyer knows if they are in correct family |
| 2 | **Breadcrumb** | Mandatory | Hierarchy context | 4–5 level path | Navigable hierarchy | Series position inferable from path |
| 3 | **Series Navigation** | Mandatory | Primary narrowing axis — route to OEM series pages | Single-axis chips: series names + SKU counts per series; links to series pages — NOT parallel filter | Navigation to series page | One taxonomy surface; 18 chips with counts; no mixed axes without legend (W1B-F-03, W2-F-08) |
| 4 | **Scope Control** | Mandatory | Declare what listing shows | Scope indicator («Все SKU семейства» vs «Серия: ПРЕМИУМ-3»); result count («N товаров»); sort controls | Buyer knows current selection scope | Result count visible — absent today (W1B-F-10 area) |
| 5 | **Filter Access** | Mandatory | Attribute narrowing within current scope | Filter panel entry (desktop: sidebar; mobile: overlay entry point); filter groups scoped to family | Buyer can narrow within scope | Filter «Подкатегории» **mirrors** chip set OR is removed — no 44 vs 18 mismatch (W1B-F-03) |
| 6 | **Active Filter Summary** | Mandatory | Show applied constraints in results zone | Active filter chips/tags + clear action | Buyer sees what constraints are applied | Addresses W1B-F-10 — no «Показать товары» without visible state |

#### Block definitions — listing zone

| # | Block | Status | Purpose | Input | Output | Success condition |
|---|-------|--------|---------|-------|--------|-------------------|
| 7 | **Product Grid** | **Conditional** — secondary on parent | SKU selection within declared scope | Listing cards per Section D; pagination | PDP routing, compare adds | Cards show series label when scope = all family (W1B-F-06); buyer can discriminate across 5 families on page 1 |

**Trigger condition for Product Grid default visibility:** **OPEN QUESTION OQ-06** — architecture allows (a) show with heavy scope labeling, or (b) hide until series selected. Blueprint default: **show with mandatory Scope Control labeling** until OQ-06 resolved.

**Inside grid must contain:** Listing cards (Section D contract); pagination when >1 page; empty state message + link to series chips or filter reset; compare affordance per card (secondary, not above-listing primary).

#### Block definitions — below listing

| # | Block | Status | Purpose | Input | Output | Success condition |
|---|-------|--------|---------|-------|--------|-------------------|
| 8 | **Pagination** | Mandatory when >1 page | Multi-page navigation | Page controls | Next/previous page of scoped results | 152 SKU / 15 per page navigable (W1B-F-02) |
| 9 | **Family Selection Guide** | Optional, recommended | Prose series comparison without matrix | 3–5 sentence comparison of named series (ПРЕМИУМ vs ПРЕМИУМ-3 vs СТАНДАРТ…) | Buyer can choose series without opening each | Addresses D3, WH-01; no full nomenclature decoding (D-02) |
| 10 | **Consultative CTA** | Conditional | Human help when self-serve insufficient | «Поможем подобрать» / «Задать вопрос» | Lead to consultation channel | **Trigger:** family has >10 series OR high chip overlap |

#### Parent category — suppressed blocks

| Block | Status | Why |
|-------|--------|-----|
| Full certificates slider | **Removed** | W2-F-07 |
| Full dealer application form | **Removed** — link only | W2-F-07 |
| Duplicate advantages grids | **Removed** | W2 duplication |
| Second chip row duplicating parent on child | **Removed** | P-02 |
| Parallel unmatched filter checkboxes | **Removed** | W1B-F-03 |

#### Information flow (parent category)

```text
ENTER → read family scope (Orientation)
      → scan series options (Series Navigation) → preferred EXIT to series page
      OR → apply filters (Filter Access + Active Filter Summary)
      OR → browse grid with scope awareness (Product Grid + Scope Control)
      → PDP or compare
```

#### Selection flow

```text
Preferred:  Series Navigation → Series Page → SKU grid (coherent scope)
Secondary:  Flat grid with series label on cards + filters (mixed-family page 1)
```

#### Navigation flow

Series Navigation chips = **links to series pages**, not inline filter toggles. Breadcrumbs + chips + filter subcategories must not present three conflicting taxonomies (W2-F-08).

#### Decision support flow

| Decision point | Supporting block | Evidence |
|----------------|------------------|----------|
| D2 — right family? | Orientation (family description) | W1C-F-07 |
| D3 — which series? | Series Navigation + optional Family Selection Guide | WH-01, rank-10 |
| D4 — section count? | Filter «Количество секций» when in scope; card field on grid | W1C D4, W1D-F-03 |
| D5 — dimensions? | Filter groups + card L×W×H | W1C-F-05 |
| D9 — compare? | Per-card compare affordance | W1C-F-09 |

---

## Section C — Series Blueprint

**Page example:** «Ванны цельнотянутые ПРЕМИУМ-3» (10 SKU)  
**Page mode:** Selection-primary (efficiency benchmark per W2-F-10)

### User goal

Compare and select SKU **within one OEM line** — sizes, sections, variants (Н).

### Primary action

Identify correct SKU from series-scoped grid → open PDP or add to cart/compare.

### Critical sequence questions

| Question | Answer |
|----------|--------|
| What must be visible **before** SKU grid? | H1, series description, breadcrumbs, adjacent series links, sort, scoped filters, result count |
| What must be visible **inside** SKU grid? | Listing cards (series context implicit — series label optional/redundant), pagination, compare per card |
| What must be visible **after** SKU grid? | Conditional consultative CTA only |
| What should **never** appear? | Parent-level 18-chip row; full certificates slider; full dealer form; degenerate filters; misaligned cross-family cards |

### Block sequence

```text
ABOVE LISTING (before grid)
  1. Series Identity Block (H1)
  2. Series Description Block                           ← NEW
  3. Breadcrumb Block
  4. Adjacent Series Navigation Block
  5. Scope Control Block (sort + scoped filters + count)

INSIDE LISTING (grid)
  6. Product Grid Block                                 ← primary

BELOW LISTING (after grid)
  7. Pagination Block
  8. Consultative CTA Block                               ← conditional
```

---

### Block definitions — before SKU grid

| # | Block | Status | Purpose | Input | Output | Success condition |
|---|-------|--------|---------|-------|--------|-------------------|
| 1 | **Series Identity** | Mandatory | Series name as page identity | H1 (series name) | Buyer knows exact OEM line | Matches breadcrumb terminal series level |
| 2 | **Series Description** | Mandatory | Educate what this series means vs siblings | 3–5 sentences: construction type, grade tier, typical use, differentiation vs named sibling series (П, С, Л, СТАНДАРТ) | Buyer understands series tier without decoding nomenclature | Addresses W1C-F-07, D3, rank-10; no full code legend (D-02) |
| 3 | **Breadcrumb** | Mandatory | Hierarchy context | 5-level path | Navigable return to family | W1B §3 — hierarchy readable |
| 4 | **Adjacent Series Navigation** | Conditional — when siblings exist | Exit/reroute to sibling series without parent chip row | Compact links to sibling series in same family | Navigation to adjacent series pages | No repeat of 18-chip parent row (P-03) |
| 5 | **Scope Control** | Mandatory | Narrow within series only | Sort controls; filter groups that discriminate within 10 SKUs; result count; **degenerate filters suppressed** (min=max sliders) | Buyer applies meaningful constraints only | W1B-F-04 — 21 groups reduced to discriminating subset |

### Block definitions — inside SKU grid

| # | Block | Status | Purpose | Input | Output | Success condition |
|---|-------|--------|---------|-------|--------|-------------------|
| 6 | **Product Grid** | Mandatory — **primary page content** | SKU selection within coherent series scope | 10 listing cards per Section D; series label on card optional (page-scoped); pagination; empty state; compare affordance | PDP routing, cart, compare | 10-SKU coherent grid without chip fragmentation (W2-F-10) |

**Inside grid information minimum per card:** article, name, status, price, CTA, L×W×H, section count, lead time if под заказ — see Section D Tier 1–2.

### Block definitions — after SKU grid

| # | Block | Status | Purpose | Input | Output | Success condition |
|---|-------|--------|---------|-------|--------|-------------------|
| 7 | **Pagination** | Mandatory when >1 page | Multi-page within series | Page controls | Continued series-scoped browse | N/A for ПРЕМИУМ-3 (10 SKU single page) |
| 8 | **Consultative CTA** | Conditional | Human help when cards insufficient | «Поможем подобрать» | Consultation lead | **Trigger:** card differentiators insufficient — ПРЕМИУМ-3 case: differences only in code/dims/price (W1B §4) |

### Series page — suppressed blocks

| Block | Status | Why |
|-------|--------|-----|
| Parent 18-chip row | **Removed** | Series page must not reintroduce parent fragmentation |
| In-page sibling SKU matrix | **Removed** | V-09 — not market standard; selection at listing + PDP |
| Full certificates slider | **Removed** | W2-F-07 |
| Full dealer form | **Removed** | W2-F-07 |
| Degenerate filter groups | **Removed** | W1B-F-04 |
| SEO text block | Optional minimal or **absent** | Low decision value on selection page |

### Series — information flow

```text
ENTER (from parent chip or breadcrumb)
  → read series meaning (Series Description)
  → optionally check sibling series (Adjacent Series Navigation)
  → apply discriminating filters (Scope Control)
  → compare cards in grid (Product Grid)
  → PDP / cart / compare
  → if stuck: Consultative CTA
```

### Series — selection flow

```text
Series scope = selection scope (P-03)
All grid SKUs ∈ same series
Filters narrow within series only — never expand to cross-family
```

---

## Section D — Listing Card Blueprint

**Object:** Listing Card Block Contract  
**Role:** Discrimination and routing unit — decide «open PDP / add to compare / skip» without opening every SKU (W1B-F-01, V-12).

### Card purpose

Provide **minimum discriminating information** for pre-PDP decision within current listing scope (parent mixed-family or series-coherent).

### Decision supported by card

| Decision | Supported by |
|----------|--------------|
| «Is this the right SKU?» | Article, name, key dimensions, section count |
| «Is it available at acceptable terms?» | Status, qty, price, lead time |
| «Is it in the right series?» | Series label (parent listings) |
| «Should I compare instead of open?» | Compare affordance (labeled) |
| «Should I skip?» | Sufficient attrs to reject without PDP open |

### Maximum information scope

Card carries **decision subset only** — never full spec table (20+ rows), never marketing blocks, never duplicate status zones.

---

### Field tiers

#### Tier 1 — Mandatory fields (always visible)

| Field | Purpose | Input source | Output | Success condition |
|-------|---------|--------------|--------|-------------------|
| **Article code** | Expert path, clipboard, procurement | Product nomenclature | Identifiable SKU | W1A-F-11 pattern available on PDP; present on card |
| **Short product name** | Human-readable identity | Product title (abbreviated if needed) | Name recognition | Buyer can grep visually in grid |
| **Availability status** | D7 decision | Stock status + qty when in stock | «В наличии» / «Под заказ» + N шт. | **Single zone only** — no duplicate (W1B-F-08) |
| **Price** | D7, self-serve conversion | Price list | Numeric price | Visible without PDP |
| **Primary CTA** | Conversion | Cart action | Add-to-cart or equivalent | Action reachable |
| **PDP link** | Routing | Product URL | Navigation to PDP | Entire card or explicit link routes to PDP |

#### Tier 2 — Strongly recommended (required on parent/series listings when data exists)

| Field | Purpose | Input source | When conditional | Success condition |
|-------|---------|--------------|------------------|-------------------|
| **Series / line label** | Discriminate in mixed-family parent grid | Series taxonomy | **Mandatory on parent category grid**; optional on series page (page-scoped) | Buyer sees series without decoding title (W1B-F-06, WH-01) |
| **L×W×H** (structured) | D5 size decision | Spec attributes | When populated | Not only embedded in title (W1C-F-05) |
| **Section count** | D4 | Spec attribute / nomenclature | When applicable to family | Visible as field, not only in code |
| **Lead time** | Commercial signal | ERP/fulfillment data | When status = «Под заказ» | W1B-F-09 — not hidden for под заказ SKUs |
| **Thumbnail image** | Recognition | Product image | When image exists | Meaningful `alt` text — not empty (W1B §1) |

#### Tier 3 — Optional fields (context-dependent)

| Field | Trigger | Purpose |
|-------|---------|---------|
| **Material** (AISI 304/430) | Discriminates within series listing | Spec attribute |
| **Variant indicator** (e.g. «Н») | Variant pairs exist in grid | Nomenclature flag |
| **Discount badge** | Active promotion on SKU | Commercial |
| **Delivery summary** | Data populated — **never empty placeholder** | Commercial micro-strip (W2-F-05, U-06) |

#### Tier 4 — Actions (secondary to information)

| Affordance | Status | Rule |
|------------|--------|------|
| **Compare** | Recommended | Text label or accessible name required on mobile (MO-04) |
| **Wishlist / favorites** | Optional | Secondary to information fields |
| **«Подробнее»** | Recommended | Must remain discoverable on mobile (hidden today per W2 Mobile) |

---

### Forbidden fields (never on listing card)

| Field / pattern | Why forbidden | Finding |
|-----------------|---------------|---------|
| Duplicated availability (two zones) | Wasted space, semantic noise | W1B-F-08, W2 duplication |
| Full spec table (20+ attributes) | Belongs on PDP / compare | W1A-F-05 |
| Placeholder / demo content | Trust erosion | W1A-F-03 |
| Empty reserved fields (delivery span with no text) | Space without information | W2-F-05, H-07 |
| Marketing prose (advantages, certificates) | Belongs in commercial blocks | W2-F-07 |
| Decoded nomenclature legend | Out of v1 scope | D-02 |
| Misleading status styling («Под заказ» with in-stock class) | Semantic confusion | W1B-F-09 |

---

### Listing Card Block Contract (summary)

```text
LISTING CARD CONTRACT v1

MANDATORY (6)
  article · name · status (single zone) · price · CTA · PDP link

STRONGLY RECOMMENDED — parent/series listings (5)
  series label · L×W×H · section count · lead time (if под заказ) · image alt

OPTIONAL (4)
  material · variant flag · discount · delivery (if populated only)

ACTIONS (3)
  compare (labeled) · favorites · подробнее

FORBIDDEN (7 patterns)
  duplicate status · full specs · placeholders · empty delivery
  marketing blocks · nomenclature legend · misleading status class

MAX SCOPE: decision subset — never full spec table or commercial wallpaper
```

---

## Section E — PDP Blueprint

**Page mode:** Single-SKU evaluation and conversion surface (W1A-F-01)  
**Example SKU:** ВМЦ-П3-2/500 (моечные ванны, ПРЕМИУМ-3)

### User goal

Confirm «right model in right series» → evaluate fit → convert (cart / quote / consult).

### Primary action

Add to cart OR initiate B2B consultation with sufficient self-serve information consumed.

### Full block map (7 zones, top to bottom)

```text
ZONE 0 — GLOBAL (page top)
  E-00  Breadcrumb Block

ZONE 1 — HERO (first screen)
  E-01  Product Identity Block
  E-02  Series Context Block                    ← NEW
  E-03  Commercial Core Block (status · price · CTA)
  E-04  Selected Properties Block
  E-05  Category-Critical Properties Block      ← NEW (hero extension)
  E-06  Media Block
  E-07  Secondary Actions Block (compare · favorites)

ZONE 2 — PRIMARY (default-visible decision set)
  E-08  Description Block
  E-09  Minimum Spec Summary Block              ← NEW default-visible
  E-10  Full Specifications Block
  E-11  Documents Entry Block

ZONE 3 — SECONDARY (in-series selection support)
  E-12  In-Series Alternatives Block            ← REPLACES misaligned «Похожие»
  E-13  Compare Feedback Block
  E-14  Return-to-Series Block

ZONE 4 — REFERENCE (deep reference)
  E-15  Full Documentation Block
  E-16  Extended Description Block

ZONE 5 — RELATED (deprioritized)
  E-17  Cross-Family Related Block

ZONE 6 — COMMERCIAL (conversion support)
  E-18  Commercial Detail Block
  E-19  Consultative CTA Block                  ← elevated
  E-20  Trust Micro-Signals Block
  E-21  Legal Disclaimer Block
```

---

### Zone 0 — Breadcrumb Block

| Attribute | Value |
|-----------|-------|
| **Purpose** | Navigation context — 4-level hierarchy to SKU |
| **Owner** | Navigation / taxonomy |
| **Status** | Mandatory |
| **Input** | Category tree path |
| **Output** | Navigable hierarchy; series link inferable |
| **Success condition** | Buyer can return to series or family in ≤2 clicks (W1A-F-10) |

---

### Zone 1 — Hero blocks

#### E-01 Product Identity Block

| Attribute | Value |
|-----------|-------|
| **Purpose** | SKU identity |
| **Owner** | Product record |
| **Status** | Mandatory |
| **Input** | H1 title; article code; copy-to-clipboard affordance |
| **Output** | Unambiguous SKU identification |
| **Success condition** | Expert can copy article without scroll (W1A-F-11) |

**Must NOT contain:** placeholder mini-description (W1A-F-03); demo brand logo (W1A-F-04).

#### E-02 Series Context Block

| Attribute | Value |
|-----------|-------|
| **Purpose** | Answer «am I in the right series?» on first screen |
| **Owner** | Taxonomy / series record |
| **Status** | Mandatory — **NEW packaging** |
| **Input** | Series name; link to series listing page; optional one-line series tier descriptor |
| **Output** | Series affiliation visible before scroll |
| **Success condition** | Buyer does not need breadcrumbs alone to determine series (WH-13, W1A FS-01) |

#### E-03 Commercial Core Block

| Attribute | Value |
|-----------|-------|
| **Purpose** | D7 availability and price decision at conversion point |
| **Owner** | Commerce / inventory |
| **Status** | Mandatory |
| **Input** | Availability status; qty when in stock; price; primary CTA; qty selector |
| **Output** | Purchase-ready state |
| **Success condition** | Status + price + CTA visible on first screen (MO-01) |

#### E-04 Selected Properties Block

| Attribute | Value |
|-----------|-------|
| **Purpose** | Quick physical fit check |
| **Owner** | Product specifications |
| **Status** | Mandatory |
| **Input** | L×W×H×mass (current 4 props — W1A-F-02) |
| **Output** | Structured dimensional snapshot |
| **Success condition** | Buyer assesses physical fit without opening spec tab |

#### E-05 Category-Critical Properties Block

| Attribute | Value |
|-----------|-------|
| **Purpose** | Family-specific fit attributes beyond dimensions |
| **Owner** | Product specifications (family-scoped rule) |
| **Status** | Mandatory — **NEW hero extension** |
| **Input** | Family-specific attribute set (see table below) |
| **Output** | Category-relevant decision data on first screen |
| **Success condition** | Sink buyer sees section count, bowl dims, material, construction without tab switch (WH-14, IA-01) |

**Family minimum (v1):**

| Family | Category-critical properties |
|--------|------------------------------|
| Моечные ванны | Section count, bowl dimensions, material (AISI grade), construction (цельнотянутая/сварная) |
| Столы / neutral (pattern) | Configuration type, sink/bowl presence, material |
| Other families | **OQ-01** — rule: top 3 discriminating attrs from spec table |

**Packaging rule:** E-04 + E-05 must not duplicate same 4 rows as spec table header without incremental value (ID-01).

#### E-06 Media Block

| Attribute | Value |
|-----------|-------|
| **Purpose** | Product visual confirmation |
| **Owner** | Product media |
| **Status** | Mandatory |
| **Input** | Product image(s) — count is content issue |
| **Output** | Visual identification |
| **Success condition** | At least one meaningful product image; zone assigned regardless of count (W2-F-01) |

**Must NOT contain:** misaligned «Похожие» products in hero zone.

#### E-07 Secondary Actions Block

| Attribute | Value |
|-----------|-------|
| **Purpose** | Compare and save for later |
| **Owner** | Compare / account infrastructure |
| **Status** | Recommended |
| **Input** | Compare toggle; favorites toggle |
| **Output** | Item added to compare or wishlist |
| **Success condition** | Labeled or feedback-visible on mobile — not icon-only silent (W1A-F-07, MO-04) |

---

### Zone 2 — Primary blocks

#### E-08 Description Block

| Attribute | Value |
|-----------|-------|
| **Purpose** | Confirm fit — назначение, комплектация, ключевые отличия |
| **Owner** | Product content |
| **Status** | Mandatory |
| **Input** | Structured product description |
| **Output** | Buyer understands product role and package |
| **Success condition** | Default-visible without tab switch (tab or inline) |

#### E-09 Minimum Spec Summary Block

| Attribute | Value |
|-----------|-------|
| **Purpose** | Default-visible decision set — reduce «under-informative» perception |
| **Owner** | Product specifications |
| **Status** | Mandatory — **NEW default-visible** |
| **Input** | 5–8 rows: category-critical attrs + logistics (вес нетто/брутто, упаковка) |
| **Output** | Sufficient spec context without tab click |
| **Success condition** | Buyer receives meaningful spec data at load — addresses W1A-F-05, W2-F-03 |

#### E-10 Full Specifications Block

| Attribute | Value |
|-----------|-------|
| **Purpose** | Complete technical record (20+ rows) |
| **Owner** | Product specifications |
| **Status** | Mandatory |
| **Input** | Full attribute table |
| **Output** | Engineering/procurement-grade data |
| **Success condition** | Available via tab or expand; all rows accessible |

#### E-11 Documents Entry Block

| Attribute | Value |
|-----------|-------|
| **Purpose** | Route to downloadable assets |
| **Owner** | Product documents |
| **Status** | Mandatory when files exist |
| **Input** | Document list or tab entry |
| **Output** | PDF/download access |
| **Success condition** | Documents discoverable from primary zone — not isolated (W2 Fragmentation) |

---

### Zone 3 — Secondary blocks

#### E-12 In-Series Alternatives Block

| Attribute | Value |
|-----------|-------|
| **Purpose** | Support within-series SKU comparison — sizes, sections, Н variants |
| **Owner** | Product relations (series-scoped) |
| **Status** | Mandatory — **replaces misaligned «Похожие»** |
| **Input** | SKUs from same series as current PDP |
| **Output** | Navigation to sibling SKUs in series |
| **Success condition** | Sink PDP shows ПРЕМИУМ-3 siblings — not котломойки (W1A-F-06, WH-07, priority #1) |

**Rule:** If legacy «Похожие товары» retained, must be reclassified as «Другие серии» or «Другие типы» with explicit scope label — never default-prominent when cross-family.

#### E-13 Compare Feedback Block

| Attribute | Value |
|-----------|-------|
| **Purpose** | Confirm compare action |
| **Owner** | Compare infrastructure |
| **Status** | Recommended |
| **Input** | Compare state from E-07 |
| **Output** | «Добавлено к сравнению» feedback |
| **Success condition** | Buyer knows compare succeeded (PS-03) |

#### E-14 Return-to-Series Block

| Attribute | Value |
|-----------|-------|
| **Purpose** | Resume browsing with filter context |
| **Owner** | Navigation |
| **Status** | Recommended |
| **Input** | Series URL + applied filter state (if any) |
| **Output** | Return to filtered series listing |
| **Success condition** | Buyer re-enters listing without hierarchy re-navigation (PS-04) |

---

### Zone 4 — Reference blocks

#### E-15 Full Documentation Block

| Attribute | Value |
|-----------|-------|
| **Purpose** | Deep documentation for tender/engineering |
| **Owner** | Product documents |
| **Status** | Mandatory when files exist |
| **Input** | PDFs, certificates per SKU |
| **Output** | Downloadable proof package |
| **Success condition** | All SKU documents accessible in tab «Документы» |

#### E-16 Extended Description Block

| Attribute | Value |
|-----------|-------|
| **Purpose** | Long-form reference |
| **Owner** | Product content |
| **Status** | Optional |
| **Input** | Extended marketing/technical prose |
| **Output** | Deep product narrative |
| **Success condition** | Available below specs or in tab — not required for initial fit |

---

### Zone 5 — Related blocks

#### E-17 Cross-Family Related Block

| Attribute | Value |
|-----------|-------|
| **Purpose** | Continuation paths outside current series |
| **Owner** | Product relations (cross-family) |
| **Status** | Optional |
| **Input** | Accessories, compatible equipment — valid relationships only |
| **Output** | Navigation to related products |
| **Success condition** | Clearly labeled «Сопутствующие»; deprioritized below in-series block |

**Must NOT:** Show cross-family items in default «Похожие» position before in-series block.

---

### Zone 6 — Commercial blocks

#### E-18 Commercial Detail Block

| Attribute | Value |
|-----------|-------|
| **Purpose** | B2B procurement confidence at CTA |
| **Owner** | Commerce / logistics |
| **Status** | Mandatory (partial fields conditional) |
| **Input** | Price + availability (ref from E-03); lead time when под заказ; delivery summary + link to «Доставка»; dealer/opt path link |
| **Output** | Procurement-ready context |
| **Success condition** | B2B buyer sees lead time, delivery, dealer path near CTA (CV-01, W1B-F-09) |

#### E-19 Consultative CTA Block

| Attribute | Value |
|-----------|-------|
| **Purpose** | Human escalation when self-serve insufficient (D8) |
| **Owner** | Sales / consultation |
| **Status** | Mandatory — **elevated position** |
| **Input** | «Задать вопрос» / «Поможем подобрать» |
| **Output** | Consultation lead |
| **Success condition** | Visible at or before primary zone end — not only below all tabs (PS-05, CV-02) |

#### E-20 Trust Micro-Signals Block

| Attribute | Value |
|-----------|-------|
| **Purpose** | Lightweight trust at conversion |
| **Owner** | Brand / certifications |
| **Status** | Optional |
| **Input** | «Сделано в России», certification badge |
| **Output** | Trust reinforcement |
| **Success condition** | Near buy box; not full certificate slider (CV-04) |

#### E-21 Legal Disclaimer Block

| Attribute | Value |
|-----------|-------|
| **Purpose** | Price/legal transparency |
| **Owner** | Legal / commerce |
| **Status** | Optional |
| **Input** | Оферта / price disclaimer text |
| **Output** | Legal compliance |
| **Success condition** | Present in commercial zone footer (CV-05) |

---

### PDP — suppressed blocks

| Block | Status | Why |
|-------|--------|-----|
| Misaligned «Похожие товары» (cross-family default) | **Removed** until realigned | W1A-F-06 |
| Full dealer application form inline | **Removed** | W2-F-07 |
| Full certificates slider | **Removed** | W2-F-07 |
| Duplicate advantages grids | **Removed** | W2 duplication |
| In-page sibling SKU matrix | **Removed** | V-09 |
| Placeholder mini-description | **Removed** | W1A-F-03 |
| Demo brand logo (AssuM) | **Removed** | W1A-F-04 |
| Q&A community block | **Out of v1** | No BZPM evidence |

---

## Section F — Commercial Blocks Blueprint

**Principle:** Tier by reach and decision relevance (W2-F-07, Strategy §5–6).

### Block inventory

| Block type | Tier | Status |
|------------|------|--------|
| Header procurement nav | Global | Mandatory |
| Trust summary (compact) | Global | Mandatory |
| Footer legal / company | Global | Mandatory |
| Commercial micro-strip | Contextual | Conditional |
| Consultative CTA | Contextual | Conditional |
| In-series / family guide (prose) | Contextual | Conditional |
| Compare infrastructure | Contextual | Mandatory (infra exists) |
| Lead time callout | Conditional | Triggered |
| Dealer form (full) | Conditional | Triggered |
| Certificates detail | Conditional | Triggered |
| Discount visibility | Conditional | Triggered |
| Custom equipment CTA | Conditional | Triggered |

---

### F1 — Global blocks (all pages)

#### Header Procurement Nav

| Attribute | Value |
|-----------|-------|
| **Allowed pages** | All pages via site header |
| **Purpose** | Persistent low-cost B2B path |
| **Trigger** | Always |
| **Input** | Дилерам · Доставка · Контакты links |
| **Output** | Navigation to procurement surfaces |
| **Success condition** | B2B path visible without catalog scroll (CV-01) |

#### Trust Summary (compact)

| Attribute | Value |
|-----------|-------|
| **Allowed pages** | Catalog root (primary); footer site-wide (secondary) |
| **Suppressed pages** | Series, PDP, deep category — full slider form |
| **Purpose** | Manufacturer trust once per catalog session |
| **Trigger** | Catalog entry |
| **Input** | «Сделано в России», certification reference |
| **Output** | Trust signal or link to detail |
| **Success condition** | No full certificate slider repeat on every catalog level (W2-F-07) |

#### Footer Legal / Company

| Attribute | Value |
|-----------|-------|
| **Allowed pages** | All pages |
| **Purpose** | Legal compliance, company identity |
| **Trigger** | Always |
| **Input** | Оферта disclaimer, реквизиты, policy links |
| **Output** | Legal navigation |
| **Success condition** | CV-05 coverage |

---

### F2 — Contextual blocks (choice-point surfaces)

#### Commercial Micro-Strip

| Attribute | Value |
|-----------|-------|
| **Allowed pages** | Listing card (when data exists); PDP Commercial zone (E-18) |
| **Suppressed pages** | Catalog root; mid-level category |
| **Purpose** | Procurement signals at SKU evaluation |
| **Trigger** | Delivery/lead time data populated |
| **Input** | Delivery teaser; lead time; dealer link |
| **Output** | Commercial context on card/PDP |
| **Success condition** | Replaces empty `p-card__delivery` (W2-F-05); never renders empty (U-06) |

#### Consultative CTA

| Attribute | Value |
|-----------|-------|
| **Allowed pages** | PDP (elevated — E-19); parent category (conditional); series page (conditional) |
| **Suppressed pages** | Catalog root as large block; below all PDP tabs only |
| **Purpose** | Human help when self-serve insufficient (D8) |
| **Trigger** | PDP: always elevated; parent: >10 series or high chip overlap; series: card differentiators insufficient |
| **Input** | «Поможем подобрать» / «Задать вопрос» |
| **Output** | Consultation lead |
| **Success condition** | Reachable without scrolling past misaligned carousels (PS-05) |

#### In-Series / Family Guide (prose)

| Attribute | Value |
|-----------|-------|
| **Allowed pages** | Series page above listing (series description block); parent category below chips (Family Selection Guide) |
| **Suppressed pages** | PDP, catalog root |
| **Purpose** | Series choice decision support without matrix |
| **Trigger** | High-friction series choice (D3) |
| **Input** | Prose comparison of named series |
| **Output** | Informed series selection |
| **Success condition** | Addresses WH-01 without nomenclature legend (D-02) |

#### Compare Infrastructure

| Attribute | Value |
|-----------|-------|
| **Allowed pages** | Header counter; listing cards; PDP secondary actions |
| **Suppressed pages** | N/A — infrastructure is global |
| **Purpose** | D9 comparison mode support |
| **Trigger** | Buyer adds item to compare |
| **Input** | `/compare-products`, `data-compare-toggle` |
| **Output** | Populated compare table |
| **Success condition** | Empty state must not show «Личный кабинет» conflation (W1B-F-07); populated UX = implementation validation (U-02) |

---

### F3 — Conditional blocks (triggered only)

| Block | Trigger condition | Allowed surface | Suppressed surfaces |
|-------|-------------------|-----------------|---------------------|
| **Lead time callout** | SKU status = «Под заказ» | Listing card; PDP hero (E-03) + commercial (E-18) | — |
| **Dealer form (full)** | Buyer clicks «Стать дилером» / explicit dealer intent | Dedicated «Дилерам» page only | All catalog category/series/PDP inline |
| **Certificates detail** | Buyer requests proof / tender documentation | Dedicated page or modal from trust summary | Inline slider on deep catalog pages |
| **Discount visibility** | Active promotion on SKU | Card badge; PDP commercial zone | — |
| **Custom equipment CTA** | Task-heavy path (Scenario E) | `/custom-equipment`; search empty state | **Link only in v1** — wizard out of scope (WH-08, U-11) |

---

### F4 — Suppression matrix (commercial blocks)

| Block | Catalog root | Mid-level cat | Parent cat | Series | PDP |
|-------|-------------|---------------|------------|--------|-----|
| Full certificates slider | Suppress (use compact trust) | Suppress | Suppress | **Suppress** | **Suppress** |
| Full dealer form | Suppress (link only) | Suppress | Suppress | **Suppress** | **Suppress** |
| Duplicate advantages grids | Allow once (below fold) | Suppress | Suppress | Suppress | Suppress |
| Large consultative image block (below tabs only) | N/A | N/A | N/A | N/A | **Suppress** |
| Misaligned «Похожие» | N/A | N/A | N/A | N/A | **Suppress** until realigned |
| Commercial micro-strip | Suppress | Suppress | Optional on cards | On cards | E-18 |

---

## Section G — Mobile Blueprint

**Scope:** Information priority per page type — not responsive layout or breakpoints (U-04).

**Rule:** Mobile preserves **decision-equivalent information**, not DOM parity (P-09).

### Priority tier definitions

| Tier | Meaning |
|------|---------|
| **P1 — Critical** | Must be reachable without excessive scroll; decision cannot proceed without it |
| **P2 — High** | Strongly affects selection quality; may live in overlay if state is visible |
| **P3 — Medium** | Improves decision confidence; acceptable below P1–P2 |
| **P4 — Lower** | Reference depth; hidden behind tab/expand acceptable |
| **P5 — Lowest** | Non-decision content; collapse or defer |

---

### G1 — Catalog Root (mobile priorities)

| Priority | Information blocks |
|----------|-------------------|
| **P1** | Type Navigation Block (9 category entries) |
| **P2** | Orientation (H1 + purpose); Light Procurement Reference |
| **P3** | Trust Summary (compact) |
| **P4** | Breadcrumb |
| **P5** | SEO Reference Block |

---

### G2 — Mid-level Category (mobile priorities)

| Priority | Information blocks |
|----------|-------------------|
| **P1** | Subfamily Navigation Block |
| **P2** | Orientation (H1 + class description); Breadcrumb |
| **P3** | Listing Zone (if present) — cards per Section D Tier 1–2 |
| **P4** | Sort / filter (if listing present) |
| **P5** | Below-listing commercial (must remain suppressed) |

---

### G3 — Parent Category (mobile priorities)

| Priority | Information blocks |
|----------|-------------------|
| **P1** | Series Navigation chips; listing card Tier 1 fields (price, status, article, CTA) |
| **P2** | Active Filter Summary; sort control; Scope indicator + result count; Orientation (family description) |
| **P3** | Filter access (overlay acceptable); series label + dimensions on cards; labeled compare |
| **P4** | Family Selection Guide; pagination |
| **P5** | SEO text; suppressed commercial blocks (certificates, dealer form) |

**Mobile-specific rule:** Filters may be in fullscreen overlay (W1B-F-11) — **applied constraints must appear in results zone** (Active Filter Summary = P2, not hidden inside closed overlay).

---

### G4 — Series Page (mobile priorities)

| Priority | Information blocks |
|----------|-------------------|
| **P1** | Product grid Tier 1: price, status, article, CTA; series description opening line |
| **P2** | Scoped filters + result count; L×W×H + section count on cards; labeled compare |
| **P3** | Full series description; in-series card Tier 2; Consultative CTA (if triggered) |
| **P4** | Adjacent series links; pagination; sort |
| **P5** | Suppressed commercial blocks |

---

### G5 — Listing Card (mobile priorities)

| Priority | Information |
|----------|-------------|
| **P1** | Price, availability, article, primary CTA |
| **P2** | Series label, L×W×H, section count |
| **P3** | Lead time (if под заказ), image, «Подробнее» |
| **P4** | Material, variant, discount, delivery (if populated) |
| **P5** | — (nothing lower than P4 on card) |

**Suppress on mobile card:** duplicate status; empty delivery; icon-only compare without label (MO-04).

---

### G6 — PDP (mobile priorities)

| Priority | Information blocks |
|----------|-------------------|
| **P1** | E-03 Commercial Core (price, status, CTA); E-02 Series Context; E-04/E-05 key properties; E-01 article |
| **P2** | E-07 labeled compare/favorites; E-09 Minimum Spec Summary; filter-equivalent: active decision attrs visible |
| **P3** | E-12 In-Series Alternatives; E-19 Consultative CTA; E-08 Description opening |
| **P4** | E-10 Full Specifications; E-11/E-15 Documents; E-06 Media (full gallery) |
| **P5** | E-16 Extended Description; E-17 Cross-Family Related; repeated certificates/advantages/dealer blocks (collapse) |

**Suppress on mobile PDP:** misaligned «Похожие» before in-series block (MO-06, PS-01); duplicate availability; full dealer form.

---

### Mobile suppression rules (all catalog pages)

| Pattern | Action | Finding |
|---------|--------|---------|
| Repeated certificates + dealer on category/series | Collapse or suppress | W2 Mobile |
| Empty `p-card__delivery` | Do not render | W2-F-05 |
| Duplicate availability on card | Remove | W1B-F-08 |
| Misaligned «Похожие» before in-series | Suppress or reorder information priority | MO-06 |

---

## Section H — Cross-Page Rules

Rules derived from architecture principles P-01–P-10 and Information Ownership Matrix. Apply on **every** catalog surface.

### H1 — Information ownership

| Rule | Statement |
|------|-----------|
| **CP-01** | Each information type has exactly **one primary surface**; secondary surfaces summarize or link — never duplicate verbatim. |
| **CP-02** | Price appears at most **once per card** and **once in PDP hero**; not repeated 3+ times on same view. |
| **CP-03** | Availability / qty: **single zone** on listing card; single zone in PDP hero. |
| **CP-04** | Full specifications (20+ rows): **PDP only** — never on listing card. |
| **CP-05** | Documents: **PDP Reference zone** primary; never on listing card. |
| **CP-06** | Series identity: **series page H1 + description** primary; PDP series context line + card series label secondary. |
| **CP-07** | Delivery terms: **«Доставка» page** primary; PDP commercial summary + card micro-strip secondary — **only when populated**. |
| **CP-08** | Dealer program: **«Дилерам» page** primary; header nav + PDP compact CTA secondary; **never** full form on catalog pages. |
| **CP-09** | Certificates: **dedicated page/modal** primary; catalog root compact trust summary secondary; **never** full slider on series/PDP/category. |
| **CP-10** | In-series alternatives: **PDP Secondary zone** primary; **never** misaligned cross-family «Похожие» as default. |

### H2 — Navigation vs selection

| Rule | Statement |
|------|-----------|
| **CP-11** | Catalog root and mid-level categories execute **navigation only** — no SKU grid as primary content. |
| **CP-12** | Parent category: **series navigation is primary** above listing; flat grid is secondary and scope-labeled. |
| **CP-13** | Series page: **grid is primary**; no parent-level chip row reintroduced. |
| **CP-14** | PDP: **single-SKU evaluation** — no in-page selection matrix (V-09). |

### H3 — Taxonomy integrity

| Rule | Statement |
|------|-----------|
| **CP-15** | **One primary taxonomy surface per page** — chips OR synced filter OR breadcrumbs path, not three conflicting sets (W2-F-08). |
| **CP-16** | Filter «Подкатегории» must **mirror** chip set or be **removed** (W1B-F-03). |
| **CP-17** | Chip row = **single axis** (series OR section-count OR type) — never mixed without legend (WH-02). |
| **CP-18** | Series-scoped pages: filters narrow **within series only** — degenerate groups suppressed (W1B-F-04). |

### H4 — Commercial block discipline

| Rule | Statement |
|------|-----------|
| **CP-19** | Global trust blocks appear **once** at catalog entry — not repeated identically on every subpage (W2-F-07). |
| **CP-20** | Consultative CTA on PDP must be **elevated** — not only below all tabs (PS-05). |
| **CP-21** | Commercial signals appear **at choice points** (card, PDP CTA) — not as footer wallpaper on deep pages. |
| **CP-22** | Empty reserved commercial fields **must not render** (W2-F-05). |

### H5 — Content integrity

| Rule | Statement |
|------|-----------|
| **CP-23** | No placeholder or demo content on any catalog surface (W1A-F-03, W1A-F-04). |
| **CP-24** | Hero selected props and spec table header must not **duplicate same rows** without differentiation (ID-01). |
| **CP-25** | Status styling must match semantic status — «Под заказ» cannot use in-stock class (W1B-F-09). |
| **CP-26** | Images must have meaningful `alt` when product identity is known. |

### H6 — Compare and search paths

| Rule | Statement |
|------|-----------|
| **CP-27** | Compare infrastructure must not conflate with account/«Личный кабинет» empty state (W1B-F-07). |
| **CP-28** | Expert article-code path via header search **must not be obstructed** by catalog root mandatory blocks. |
| **CP-29** | Compare affordances require **accessible naming** on mobile (MO-04). |

### H7 — Scope exclusions (v1)

| Rule | Statement |
|------|-----------|
| **CP-30** | No nomenclature decoding legend pages (D-02). |
| **CP-31** | No task-first wizard on catalog root (WH-08). |
| **CP-32** | No Trapeza layout/taxonomy copy (R-01, D-03). |
| **CP-33** | Series description blocks are **architectural slots** — copy production is separate workstream (OQ-12). |

---

## Section I — Blueprint Validation

Validation of `BZPM-BLUEPRINT-v1` against completed audits. Status key:

| Status | Meaning |
|--------|---------|
| **ADDRESSED** | Blueprint defines block(s) that resolve finding at IA level |
| **PARTIAL** | Blueprint addresses intent; implementation or content still required |
| **UNRESOLVED** | Finding remains open at blueprint level |
| **IMPL VALIDATION** | Requires runtime/build verification beyond blueprint |

---

### I1 — W1A Product Audit

| Finding | Blueprint section | Status | Notes |
|---------|-------------------|--------|-------|
| W1A-F-01 PDP = single-SKU | E-PDP, CP-14 | **ADDRESSED** | No in-page matrix |
| W1A-F-02 Hero 4 props only | E-04, E-05 | **ADDRESSED** | Category-critical extension defined |
| W1A-F-03 Placeholder mini-description | E-01, CP-23 | **ADDRESSED** | Forbidden in hero |
| W1A-F-04 Demo brand logo | E-01, CP-23 | **ADDRESSED** | Forbidden in hero |
| W1A-F-05 Specs hidden in tabs | E-09, E-10 | **ADDRESSED** | Min spec summary default-visible |
| W1A-F-06 «Похожие» = котломойки | E-12, CP-10 | **ADDRESSED** | In-series alternatives replace misaligned block |
| W1A-F-07 Icon-only compare/fav | E-07, CP-29 | **ADDRESSED** | Labeled actions required |
| W1A-F-08 Gallery 1 image | E-06 | **PARTIAL** | Zone assigned; image count = content workstream |
| W1A-F-09 Reference table 404 | — | **UNRESOLVED** | Out of blueprint scope — URL/content fix |
| W1A-F-10 Breadcrumbs 4-level | E-00, all category breadcrumbs | **ADDRESSED** | Mandatory on all page types |
| W1A-F-11 Article copy | E-01, Listing Card Tier 1 | **ADDRESSED** | Mandatory |
| W1A-F-12 Stock qty shown | E-03, Listing Card Tier 1 | **ADDRESSED** | Single zone rule |
| WH-11 «Похожие» breaks path | E-12 | **ADDRESSED** | Priority #1 |
| WH-12 No sibling matrix bounce | E-12, Series grid | **PARTIAL** | Mitigated via in-series alts + listing; matrix explicitly excluded (V-09) |
| WH-13 Missing series context | E-02 | **ADDRESSED** | NEW mandatory block |
| WH-14 Insufficient hero props | E-05 | **ADDRESSED** | Family-specific rule |
| WH-15 B2B context near CTA | E-18, E-19 | **ADDRESSED** | Commercial zone elevated |

---

### I2 — W1B Category Audit

| Finding | Blueprint section | Status | Notes |
|---------|-------------------|--------|-------|
| W1B-F-01 Thin cards | Section D | **ADDRESSED** | Tier 2 discriminating fields added |
| W1B-F-02 18 chips + 36 filters | B2 blocks 3, 5, 6 | **ADDRESSED** | Single taxonomy + synced filter rule |
| W1B-F-03 44 vs 18 filter mismatch | B2 block 5, CP-16 | **ADDRESSED** | Mirror or remove |
| W1B-F-04 Degenerate filters on series | C block 5 | **ADDRESSED** | Suppress degenerate groups |
| W1B-F-05 Placeholder chip icons | B2 block 3 | **PARTIAL** | Blueprint defines chip content (name+count); image quality = content |
| W1B-F-06 Mixed 5 families page 1 | D Tier 2 series label, B2 block 7 | **ADDRESSED** | Series label mandatory on parent grid |
| W1B-F-07 Compare empty = ЛК | F Compare, CP-27 | **PARTIAL** | Rule stated; **IMPL VALIDATION** (U-02) |
| W1B-F-08 Duplicate status on card | D Forbidden, CP-03 | **ADDRESSED** | Single zone |
| W1B-F-09 Под заказ styling | D Forbidden, CP-25 | **ADDRESSED** | Semantic class rule |
| W1B-F-10 No active filter summary | B2 block 6 | **ADDRESSED** | NEW mandatory block |
| W1B-F-11 Mobile filter overlay | G3 P2, CP-29 | **ADDRESSED** | Active summary visible in results zone |
| WH-06 Thin for pre-PDP compare | Section D Tier 2 | **ADDRESSED** | Semantic fields added within V-12 pattern |

---

### I3 — W1C Buyer Decision Flow

| Finding | Blueprint section | Status | Notes |
|---------|-------------------|--------|-------|
| W1C-F-01 Decision chain | All sections | **ADDRESSED** | Chain preserved in blueprint structure |
| W1C-F-02 Catalog = 9 cards | Section A | **ADDRESSED** | Type Navigation Block |
| W1C-F-03 Chips + flat grid simultaneous | B2 sequence, CP-12 | **PARTIAL** | Grid secondary + scope labeling; OQ-06 fork open |
| W1C-F-04 Search by article works | CP-28 | **ADDRESSED** | Expert bypass preserved |
| W1C-F-05 Dimension search | D Tier 2, B2 filters | **ADDRESSED** | L×W×H on card + filters |
| W1C-F-06 Task query empty | CP-31, Custom equipment CTA | **PARTIAL** | Link-only v1; wizard out of scope |
| W1C-F-07 No series description | C block 2, B2 block 9 | **ADDRESSED** | NEW mandatory blocks |
| W1C-F-08 Placeholder + «Похожие» on path | E-01, E-12 | **ADDRESSED** | |
| W1C-F-09 Compare infra exists | F Compare, D Tier 4 | **ADDRESSED** | |
| W1C-F-10 SEO text no task nav | A block 6, CP-31 | **ADDRESSED** | Below fold; no wizard |
| WH-01 No guided series choice | C block 2, B2 block 9 | **ADDRESSED** | Prose guides |
| WH-09 Chips + grid reduces series-first | B2, CP-12 | **PARTIAL** | OQ-06 — hide grid default unvalidated |
| WH-10 Product database behavior | P-01, all blueprints | **ADDRESSED** | Retained with guided prose layers |

---

### I4 — W1D Competitor Intelligence

| Finding | Blueprint section | Status | Notes |
|---------|-------------------|--------|-------|
| W1D-F-01 Trapeza database model | P-01 | **ADDRESSED** | Database-first retained |
| W1D-F-02 Functional subtaxonomy | CP-17, B2 chips | **ADDRESSED** | OEM series retained; not Trapeza copy |
| W1D-F-03 Section-count filters | D Tier 2, B2 filters | **ADDRESSED** | Adopted as filter attribute |
| W1D-F-04 Trapeza PDP brand/model | E-02 | **PARTIAL** | Series context — not brand marketplace pattern |
| W1D-F-09 No sibling matrix on PDP | CP-14, C suppressed | **ADDRESSED** | V-09 validated |
| W1D-F-10 Thin cards market norm | Section D | **ADDRESSED** | V-12 — semantic enrichment only |
| V-06 No task wizard (except HPP) | CP-31 | **ADDRESSED** | |
| V-09 Sibling matrix not standard | E suppressed, CP-14 | **ADDRESSED** | |
| R-01 / D-03 No Trapeza copy | CP-32 | **ADDRESSED** | |

---

### I5 — W2 Information Density

| Finding | Blueprint section | Status | Notes |
|---------|-------------------|--------|-------|
| W2-F-01 PDP gallery 1 slide | E-06 | **PARTIAL** | Zone defined; media count = content |
| W2-F-02 PDP hero layout | E Hero zones | **ADDRESSED** | Information repackaging defined — not layout |
| W2-F-03 Specs hidden in tabs | E-09 | **ADDRESSED** | Default-visible min summary |
| W2-F-04 Card padding/space | Section D | **PARTIAL** | Blueprint adds information density; physical space = design phase |
| W2-F-05 Empty p-card__delivery | D Tier 3, F micro-strip, CP-22 | **ADDRESSED** | Populate or suppress |
| W2-F-06 Catalog root marketing-heavy | Section A | **ADDRESSED** | Commercial blocks tiered/suppressed |
| W2-F-07 Repeated certificates/dealer | F suppression matrix | **ADDRESSED** | |
| W2-F-08 Taxonomy on 3 surfaces | CP-15, B2 | **ADDRESSED** | |
| W2-F-09 Dimensions on 4 surfaces | CP-24, D/E ownership | **ADDRESSED** | Differentiated roles per surface |
| W2-F-10 ПРЕМИУМ-3 benchmark | Section C | **ADDRESSED** | Series blueprint models benchmark |
| W2-F-11 Owner feedback triangulation | All sections | **ADDRESSED** | Empty space → repackaging; scattered → ownership rules; under-informative → Tier 2 + E-09 |
| WH-16 Empty space = layout | E-06, E-09 | **PARTIAL** | IA addresses; gallery height = design |
| WH-17 Thin cards | Section D | **ADDRESSED** | |
| WH-18 Repeated footer blocks | F, CP-19 | **ADDRESSED** | |
| WH-19 Placeholder amplifies | CP-23 | **ADDRESSED** | |
| WH-20 Below Trapeza on card fields | D Tier 2 | **ADDRESSED** | |

---

### I6 — Validation summary

| Category | Count |
|----------|-------|
| **ADDRESSED** | 58 |
| **PARTIAL** | 12 |
| **UNRESOLVED** | 1 |
| **IMPL VALIDATION** | 3 (grouped under PARTIAL notes) |

**Remaining at blueprint level:**

| Item | Status | Owner |
|------|--------|-------|
| W1A-F-09 Reference table 404 | UNRESOLVED | Content/URL — outside IA |
| OQ-06 Parent grid default visibility | PARTIAL | Operator decision |
| OQ-01 Non-sink hero properties | PARTIAL | W1E deferred |
| Compare populated UX (U-02) | IMPL VALIDATION | Engineering |
| Filter AJAX active state (U-03) | IMPL VALIDATION | Engineering |
| p-card__delivery data feed (U-06) | IMPL VALIDATION | Data/Engineering |
| Mobile P1 first-screen fit (U-04, OQ-09) | IMPL VALIDATION | Design + device test |

---

## Open Questions

Carried from architecture; blueprint does not assume answers.

| ID | Question | Blueprint impact |
|----|----------|------------------|
| OQ-01 | Category-critical hero properties for non-sink families? | E-05 rule incomplete for столы, стеллажи, тепловое |
| OQ-02 | Backend rule for «Похожие товары»? | E-12 may need CMS relation type change |
| OQ-03 | `p-card__delivery` empty by design or missing data? | D Tier 3 / F micro-strip conditional |
| OQ-04 | Populated compare table attributes? | F Compare secondary surface |
| OQ-05 | Filter AJAX — result counts and active chips? | B2 block 6 — **IMPL VALIDATION** |
| OQ-06 | Hide parent flat grid until series selected? | B2 block 7 trigger condition |
| OQ-07 | `/custom-equipment` role in task path? | F Custom equipment CTA trigger |
| OQ-08 | PRJ-0009 stack constraints? | Engineering handoff |
| OQ-09 | Mobile P1 fit on common devices? | Section G — **IMPL VALIDATION** |
| OQ-10 | Polygon WIP — findings already addressed? | Avoid duplicate effort |
| OQ-11 | Sort options — популярность / наличие? | B2/C Scope Control |
| OQ-12 | Series description copy ownership? | C block 2, B2 block 9 — content ops |

---

## Document lineage

| Input | Role |
|-------|------|
| [BZPM-REDESIGN-ARCHITECTURE-v1.md](BZPM-REDESIGN-ARCHITECTURE-v1.md) | Source of truth — not modified by this blueprint |
| [BZPM-FINDINGS-REGISTER-v1.md](BZPM-FINDINGS-REGISTER-v1.md) | Validation evidence |
| [BZPM-REDESIGN-STRATEGY-v1.md](BZPM-REDESIGN-STRATEGY-v1.md) | Strategic themes |
| [BZPM-DECISION-LOG-v1.md](BZPM-DECISION-LOG-v1.md) | Hard constraints |
| [BZPM-AUDIT-STATE-v1.md](BZPM-AUDIT-STATE-v1.md) | Phase boundaries |

**Next phase:** Visual design (designer handoff from this blueprint) · Implementation waves (OCPilot/engineering — separately chartered).

---

*BZPM-BLUEPRINT-v1 — page structure blueprint only. No UI. No implementation. Designer and engineer use this document to begin UX/UI work and implementation planning without rethinking information architecture.*
