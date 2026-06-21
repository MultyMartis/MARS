# REPORT — BZPM W4 REDESIGN ARCHITECTURE

**Execution case:** `bzpm-catalog-redesign`  
**Document:** `BZPM-REDESIGN-ARCHITECTURE-v1`  
**Date:** 2026-06-08  
**Lane:** A (Website Factory)  
**Mode:** Architecture only — no UI, no visual design, no implementation  
**Evidence base:** W0–W2 consolidated findings ([BZPM-FINDINGS-REGISTER-v1.md](BZPM-FINDINGS-REGISTER-v1.md), [BZPM-REDESIGN-STRATEGY-v1.md](BZPM-REDESIGN-STRATEGY-v1.md), [BZPM-DECISION-LOG-v1.md](BZPM-DECISION-LOG-v1.md))

**Audit environment:** https://zpm.new-site.space/  
**Strategic rule:** Trapeza = **reference**, not **blueprint** (D-03, R-01). Goal = improve information architecture, packaging, selection speed, and commercial clarity — not replicate Trapeza layout or taxonomy.

---

## Executive Summary

BZPM operates as an **OEM product-database catalog** with a decision chain **equipment type → family → series → SKU** (W1C-F-01). Research confirms the hierarchy works at the series level (ПРЕМИУМ-3: 10 coherent SKUs, W2-F-10) but **fractures at parent categories** where chips, filters, and flat SKU grids compete on three parallel surfaces (W2-F-08, W1C-F-03).

This architecture defines **what information appears, where, when, and why** across six catalog surfaces: catalog root, category, series, listing card, PDP, and commercial blocks. It does not prescribe visual treatment.

**Top architectural moves (information-only):**

1. **Separate navigation intent from selection intent** — catalog root and parent categories orient; series pages and PDP execute selection.
2. **Consolidate taxonomy to one primary surface per page type** — eliminate parallel chip/filter/breadcrumb redundancy on parent categories.
3. **Increase semantic density on listing cards** within the market-accepted thin-card pattern (V-12) — add discriminating fields without full card redesign.
4. **Repackage PDP information** — hero answers «right model in right series?»; specs remain tabbed but category-critical differentiators gain first-screen visibility; «Похожие» realigned to in-series continuation (W1A-F-06, priority #1).
5. **Tier commercial blocks** — global trust once at catalog entry; contextual procurement signals at choice points; suppress identical footer blocks on deep pages (W2-F-07).
6. **Assign information ownership** — each fact type has one primary surface; secondary surfaces link or summarize, never duplicate.

**Explicitly not in v1:** full nomenclature decoding (D-02), large-scale taxonomy restructuring (R-03), sibling SKU matrix on PDP (V-09: not market standard), task-first wizards (W1C-F-10, W1D V-06).

---

## Architecture Principles

| # | Principle | Rationale (evidence) |
|---|-----------|----------------------|
| P-01 | **Product-database first, guided where OEM structure allows** | W1C WH-10, W1D V-08: market norm is browse/search + filters; BZPM retains OEM series chips — clarify axes, do not replace with Trapeza functional taxonomy (R-01). |
| P-02 | **One primary selection surface per page** | W2-F-08: taxonomy on 3 surfaces (chips, filter «Подкатегории», URL/breadcrumbs) increases cognitive load (WH-02). |
| P-03 | **Series scope = selection scope** | W2-F-10: ПРЕМИУМ-3 page is efficiency benchmark — coherent grid without chip row. Parent mixing 5 families on page 1 (W1B-F-06) violates this. |
| P-04 | **Information at the decision point** | W1C Decision Points D3–D9: series choice, section count, and B2B procurement signals are weak at the moment buyer decides. |
| P-05 | **Visible packaging ≠ more data** | W2-F-03: 20+ specs exist but 2/3 tabs hidden; strategy is repackage visibility, not backend expansion. |
| P-06 | **No wasteful duplication** | W2 duplication analysis: availability 2× on card, certificates/dealer identical on every catalog level, L×W×H on 4 surfaces. |
| P-07 | **Commercial signals contextual, not wallpaper** | W2 Commercial Density: dealer form + certificates repeat with low incremental value on deep pages; B2B context missing near PDP CTA (CV-01). |
| P-08 | **Trapeza informs patterns, not structure** | Adoptable: section-count filters, brand/model fields on cards, structured PDP specs, compare infra (W1D). Non-adoptable: brand-index-first nav, marketplace scale (D-03). |
| P-09 | **Mobile preserves decision information, not DOM parity** | W2 Mobile: filters hidden ≤1024px; information priority hierarchy must survive viewport change (U-04: CSS inference only). |
| P-10 | **Status honesty** | UNKNOWN items (compare populated UX, filter AJAX, backend «Похожие» rules) flagged as open questions — architecture does not assume unverified behavior. |

---

## Catalog Architecture

### Section A — Catalog Root Architecture Model

**Object:** `/katalog` — top catalog page.

#### 1. Role of the catalog root

The catalog root is a **type-selection entry point**, not a product listing or commercial landing page.

| Role | Definition |
|------|------------|
| **Primary** | Orient buyer to **equipment class** (9 top-level categories) and initiate the decision chain type → family → series → SKU. |
| **Secondary** | Establish **manufacturer trust** (ЗПМ as OEM) at first catalog touch — once per session path, not repeated on every subpage. |
| **Not** | SKU discovery, faceted filtering, series education, or full commercial conversion page. |

**Evidence:** W1C-F-02 (9 category cards, not listing); W1C-F-10 (SEO zones text without interactive task navigation); W2-F-06 (marketing-heavy, selection-light above fold).

#### 2. What information should exist there

| Zone | Information | When visible | Why |
|------|-------------|--------------|-----|
| **Orientation** | Page title + one-line catalog purpose | Always, above fold | Answers «where am I» (W2 Screen Consumption: moderate density). |
| **Type navigation** | 9 top-level category entries: **name + representative image + optional SKU count** | Always, primary zone | Supports D1 (equipment type decision). Counts validate scope without opening category. |
| **Breadcrumb / hierarchy anchor** | Главная → Каталог | Always | Positions buyer in site IA (W1A-F-10 pattern). |
| **Procurement entry (light)** | Link or compact reference to «Дилерам», «Доставка» — **not full form** | Always, header-adjacent or compact strip | B2B buyers need path awareness without scroll cost of full dealer form (CV-01, W2 Commercial). |
| **Trust (tier-1, once)** | Compact certificates / «Сделано в России» reference — **summary, not full slider** | Below type grid OR linked modal | Trust at entry; full slider deferred to contextual surfaces (W2-F-07). |
| **SEO / reference** | Long-form zone description (мойка, подготовка, хранение) | Below fold only | Search/indexing value; must not compete with type navigation (W1C-F-10). |

#### 3. What information should NOT exist there

| Excluded | Why |
|----------|-----|
| Product SKU grid or search results | Conflicts with type-selection role; creates database-at-root pattern (W1C-F-02). |
| Faceted filters | Filters belong to family/series selection surfaces (W1B-F-02). |
| Full dealer application form | High space, low selection value at entry; repeats on every subpage today (W2-F-07). |
| Duplicate advantages blocks (top + bottom identical themes) | Wasteful scroll; themes partially repeat header nav (W2 duplication). |
| Series-level chips or subcategory taxonomy | Taxonomy belongs one level down, at family page (W2-F-08). |
| Task-first wizard or interactive zone picker | Out of v1 scope; SEO text alone insufficient (W1C-F-10, WH-08). |
| Placeholder or demo content | Erodes trust (W1A-F-03, W1A-F-04). |

#### 4. Intended user action

| Buyer state | Intended action | Success criterion |
|-------------|-------------------|-------------------|
| New buyer, knows equipment class | **Select one of 9 category cards** → enter family | Reaches correct family in ≤1 click from root. |
| New buyer, unsure of class | Read type names/images → select best-fit class OR use header search/megamenu | Does not scroll through SEO block before acting. |
| Expert with article code | **Bypass root** via header search (Path 2, W1C) | Root does not obstruct fast path. |
| B2B / dealer | Notice procurement entry → continue to catalog OR navigate to «Дилерам» | Self-serve path visible without full-page form. |

#### Catalog Root Architecture Model (summary)

```text
CATALOG ROOT
├── ORIENTATION ZONE (always)
│   ├── H1 + one-line purpose
│   └── Breadcrumb anchor
├── TYPE NAVIGATION ZONE (always, primary)
│   └── 9 × [category name + image + optional count]
├── LIGHT PROCUREMENT REFERENCE (always, compact)
│   └── Links: Дилерам · Доставка · Консультация
├── TRUST SUMMARY (once, compact)
│   └── Certificates / manufacturing — summary or link, not full slider
└── REFERENCE ZONE (below fold)
    └── SEO / zone description text (non-interactive in v1)
```

---

## Category Architecture

### Section B — Category Architecture Model

**Objects:** Parent categories (e.g. «Нейтральное оборудование», «Моечные ванны»).

#### 1. Purpose of category pages

| Category level | Purpose | Page mode |
|--------------|---------|-----------|
| **Mid-level** (e.g. «Нейтральное оборудование») | **Family hub** — route buyer to product families within equipment class | **Navigation page** |
| **Parent / family** (e.g. «Моечные ванны») | **Series gateway** — explain family scope, route to series OR enable informed flat browse | **Navigation-primary, selection-secondary** |
| **Leaf family** (no series children) | **SKU listing** — direct selection within family | **Selection page** |

**Evidence:** W1B §6: parent «Моечные ванны» doubles as hub (chips) and flat listing (152 SKU); W1C-F-03: simultaneous chips + grid reduces series-first navigation (WH-09).

#### 2. Relationship: category · series · subcategories · filters

| Entity | Architectural role | Relationship rule |
|--------|-------------------|-------------------|
| **Category (parent)** | Equipment **family** container | Owns series children; defines family-level description and functional boundaries (D2: моечная ванна vs котломойка vs рукомойник). |
| **Series (subcategory)** | OEM **product line** within family | Primary narrowing axis for BZPM (W1D: rare market pattern — retain, clarify). Each series = one coherent SKU set. |
| **Subcategory chips** | **Series/family navigation affordance** | **One axis per chip row** — series OR section-count OR type, never mixed without legend (W1B-F-03, WH-02). Chips = links to series pages, not parallel filter. |
| **Filters** | **Attribute narrowing within current scope** | Active only **after scope is set** (family or series). Filter «Подкатегории» must **mirror** chip set or be removed — 44 checkboxes vs 18 chips is architectural defect (W1B-F-03). |
| **Flat SKU grid** | **Selection output** | On parent category: **secondary, below navigation** OR **hidden until scope chosen**. On series: **primary**. |

**Reference pattern (Trapeza, not blueprint):** functional subtaxonomy + section-count filters (W1D-F-02, W1D-F-03). BZPM adopts **section-count as filter attribute**, not **replacement of OEM series chips**.

#### 3. Information placement: above · inside · below listing

##### Above listing

| Information | Parent category | Mid-level category |
|-------------|-----------------|-------------------|
| H1 + **family description** (2–4 sentences: what belongs, what does not) | **Required** — currently missing (W1C-F-07) | **Required** |
| Breadcrumb path | Required | Required |
| **Series navigation** (chips or equivalent) — single-axis, with counts | **Required** — primary above-listing element | N/A (use subfamily cards instead) |
| **Scope indicator** — «Showing all family SKUs» vs «Showing: ПРЕМИУМ-3» | Required when flat grid shown | N/A |
| Sort controls | Required | Required |
| Filter access (desktop: sidebar; mobile: entry point) | Required | When SKU count warrants |
| Active filter summary (applied constraints) | **Required** — absent today (W1B-F-10) | When filters present |
| Result count («N товаров») | **Required** — absent today | When listing present |

##### Inside listing (product grid)

| Information | Rule |
|-------------|------|
| Product cards | See Listing Card Architecture Model |
| Pagination | Required when >1 page |
| Empty state | Message + link back to series chips or filter reset |
| Compare affordance | Available per card; not primary above-listing element |

##### Below listing

| Information | Parent category | Series page |
|-------------|-----------------|-------------|
| Pagination (continued) | If multi-page | If multi-page |
| **Family-level FAQ or selection guide** (series comparison prose, not matrix) | **Optional, recommended** — addresses D3 without full taxonomy audit | N/A |
| Consultative CTA («Поможем подобрать») | **Conditional** — when family has >10 series or high chip overlap | **Conditional** — when 10 similar SKUs (ПРЕМИУМ-3 case) |
| Certificates slider | **Suppress or collapse** — trust already established | **Suppress** |
| Full dealer form | **Suppress** — link to dealer page instead | **Suppress** |
| SEO text block | Below fold, optional | Minimal or absent |

#### Category Architecture Model (summary)

```text
PARENT CATEGORY (e.g. Моечные ванны)
├── ABOVE LISTING
│   ├── H1 + family description (NEW — addresses W1C-F-07)
│   ├── Breadcrumbs
│   ├── SERIES NAVIGATION (primary) — single-axis chips with counts
│   ├── Scope indicator + result count + sort
│   └── Filter entry (scope-aware; subcategory filter synced with chips)
├── LISTING ZONE
│   └── Product cards (secondary on parent — or deferred until scope chosen)
└── BELOW LISTING
    ├── Pagination
    ├── Optional: family selection guide (prose)
    ├── Conditional: consultative CTA
    └── NO full certificates/dealer repeat (W2-F-07)

MID-LEVEL CATEGORY (e.g. Нейтральное оборудование)
├── ABOVE LISTING
│   ├── H1 + family description
│   ├── Subfamily navigation (5 chips — W2 neutral cat pattern)
│   └── Sort + filter (if listing present)
├── LISTING ZONE (optional — mixed-family browse)
└── BELOW LISTING (minimal commercial)
```

---

## Series Architecture

### Section C — Series Architecture Model

**Object example:** «Ванны цельнотянутые ПРЕМИУМ-3» (10 SKU).

#### Role of series pages

Series pages are the **primary selection surface** within a family. They are the **efficiency benchmark** for the catalog (W2-F-10): coherent SKU scope, no chip fragmentation, grid matches series.

| Function | Definition |
|----------|------------|
| **Selection** | Buyer compares SKUs **within one OEM line** — sizes, sections, variants (Н). |
| **Education** | Buyer learns **what ПРЕМИУМ-3 means** vs sibling series (П, С, Л, СТАНДАРТ) — currently absent (W1C-F-07). |
| **Navigation** | Buyer may exit to **adjacent series** or return to parent family — secondary to selection. |

#### Navigation page vs selection page vs both

| Mode | Series page behavior |
|------|---------------------|
| **Primary: Selection page** | Default. Grid of series-scoped SKUs is the main content. Filters narrow within series only. |
| **Secondary: Navigation** | **Adjacent series links** (ПРЕМИУМ ↔ ПРЕМИУМ-3 ↔ СТАНДАРТ) in above-listing zone — not a second chip row duplicating parent. |
| **Not** | Repeat parent-category chip row (18 chips) — series page must not reintroduce parent-level fragmentation. |

**Evidence:** W1B §3: series page has no subcategory chips — less fragmented; W1B §6: 10 SKU coherent grid; W1B-F-04: 21 filter groups with many degenerate (min=max) — filters must be **series-relevant only**.

#### What information belongs on series pages

| Zone | Information | When | Why |
|------|-------------|------|-----|
| **Above listing** | H1 (series name) | Always | Identity |
| | **Series description block** — construction type, grade tier, typical use, differentiation vs named sibling series (prose, 3–5 sentences) | Always — **NEW** | Addresses D3, W1C-F-07, rank-10 friction; no full nomenclature decoding (D-02). |
| | Breadcrumbs (5 levels) | Always | W1B §3: hierarchy readable |
| | **Adjacent series navigation** — compact links to sibling series in same family | When siblings exist | Navigation without parent chip row |
| | Sort + scope-aware filters (only groups that discriminate within 10 SKUs) | Always | W1B-F-04: suppress degenerate filters |
| | Result count | Always | Missing today |
| **Inside listing** | Product cards with **series context implicit** (series field optional — redundant if page-scoped) | Always | Selection |
| **Below listing** | Consultative CTA | **Conditional** — when card differentiators insufficient (ПРЕМИУМ-3: 10 near-identical cards) | W1B §4: differences only in code/dims/price |
| | Certificates / dealer form | **Absent** | W2-F-07 |

#### Series Architecture Model (summary)

```text
SERIES PAGE (e.g. ПРЕМИУМ-3) — SELECTION PRIMARY
├── ABOVE LISTING
│   ├── H1
│   ├── SERIES DESCRIPTION BLOCK (NEW)
│   ├── Breadcrumbs
│   ├── Adjacent series links (compact)
│   ├── Sort + scoped filters (degenerate groups suppressed)
│   └── Result count
├── LISTING ZONE (primary)
│   └── Series-scoped product cards (10 SKU coherent grid)
└── BELOW LISTING
    ├── Conditional: consultative CTA
    └── NO certificates/dealer repeat
```

**Explicit v1 exclusion:** In-page sibling SKU matrix on series page — selection stays at listing + PDP, not matrix (V-09).

---

## Listing Card Architecture

### Section D — Listing Card Information Model

**Scope:** Information hierarchy only. No card layout, dimensions, or visual redesign.

#### Card role

The listing card is a **discrimination and routing unit** — enough information to decide «open PDP / add to compare / skip» without opening every SKU in a series.

**Evidence:** W1B-F-01 (thin card, market-norm V-12); WH-06 (too thin for meaningful pre-PDP compare); W2 WH-20 (below Trapeza on semantic fields).

#### Information hierarchy

##### Tier 1 — Mandatory (always visible on every card)

| Field | Why mandatory | Evidence |
|-------|---------------|----------|
| **Product identity** — article code (primary) + short name | Expert path, clipboard, procurement (W1A-F-11) | W1B §1 |
| **Availability status** — «В наличии» / «Под заказ» + qty when in stock | D7 decision point; B2B signal (W1A-F-12) | W1B-F-09 |
| **Price** | D7; self-serve conversion (CV-03) | W1B §1 |
| **Primary CTA** — «В корзину» or equivalent | Conversion path | W1B §1 |
| **Link to PDP** | Routing | W1B §1 |

##### Tier 2 — Strongly recommended (visible when data exists; required on parent/series listings)

| Field | Why | Evidence |
|-------|-----|----------|
| **Series / line label** (e.g. «ПРЕМИУМ-3») | Parent listings mix 5 families (W1B-F-06); buyer must see series without decoding title | WH-01, D3 |
| **Key dimensions** — L×W×H as structured fields, not only embedded in title | D5; search by size works but cards lack columns (W1C-F-05) | W1B §1 |
| **Section count** (1 / 2 / 3) when applicable | D4; encoded in name only today | W1C D4 |
| **Lead time** when status = «Под заказ» | Commercial signal at choice point (W1B §4) | W1B-F-09 |
| **Thumbnail image** with meaningful `alt` | Currently `alt=""` | W1B §1 |

##### Tier 3 — Optional (context-dependent)

| Field | When | Why |
|-------|------|-----|
| **Material** (e.g. AISI 304/430) | When discriminates within series listing | Hidden in spec tab today (W2 Visibility) |
| **Variant indicator** (e.g. «Н» non-standard) | When variant pairs exist | W1B §1 |
| **Discount badge** | When promotion active | Filter exists; low visibility (W2 Commercial) |
| **Delivery summary** | When data available — **not empty placeholder** | `p-card__delivery` empty (W2-F-05, U-06) |

##### Tier 4 — Actions (secondary to information)

| Affordance | Rule |
|------------|------|
| Compare | Available; must have **text label or accessible name** on mobile (MO-04) |
| Wishlist / favorites | Available; secondary |
| «Подробнее» | Routing to PDP; must remain discoverable on mobile (W2 Mobile: hidden today) |

#### Information that should NEVER appear on listing cards

| Excluded | Why |
|----------|-----|
| **Duplicated availability** (two zones showing same status) | Wasteful (W1B-F-08, W2 duplication) |
| **Full spec table or 20+ attributes** | Belongs on PDP / compare (W1A-F-05) |
| **Placeholder / demo content** | Trust erosion (W1A-F-03) |
| **Empty reserved fields** (e.g. delivery span with no text) | Space without information (W2-F-05, H-07) |
| **Marketing prose** (advantages, certificates) | Belongs in commercial blocks, not card |
| **Decoded nomenclature legend** | Out of v1 scope (D-02) — series **label** allowed, full code breakdown is not |
| **Misleading status class** («Под заказ» with in-stock styling) | Semantic confusion (W1B-F-09) |

#### Listing Card Information Model (summary)

```text
LISTING CARD — information layers (top = highest priority)

MANDATORY
  article · name · status (+ qty) · price · CTA · PDP link

STRONGLY RECOMMENDED (listings)
  series label · L×W×H · section count · lead time (if под заказ) · image alt

OPTIONAL
  material · variant flag · discount · delivery (if populated)

ACTIONS (secondary)
  compare (labeled) · favorites · подробнее

NEVER
  duplicate status · full specs · placeholders · empty delivery · marketing blocks
```

---

## PDP Architecture

### Section E — PDP Information Architecture

**Scope:** Information zones and packaging. No layout, gallery sizing, or visual treatment.

**Core issue (research):** Information exists; packaging is inefficient — specs hidden, series context absent, «Похожие» misaligned (W2-F-11, W1A-F-06).

**PDP role:** **Single-SKU evaluation and conversion surface** — not an in-page selection matrix (W1A-F-01, V-09).

#### Zone definitions

##### Hero zone

**Purpose:** Answer «Is this the right model in the right series?» before scroll (Strategy §3, FS-01).

| Information | Priority | When visible | Why |
|-------------|----------|--------------|-----|
| Product title (H1) | Mandatory | Always | Identity |
| **Series context line** — series name + link to series page | Mandatory | Always, first screen — **NEW packaging** | WH-13; series only in breadcrumbs today (W1A FS-01) |
| Article + copy affordance | Mandatory | Always | B2B procurement (W1A-F-11) |
| Availability + quantity | Mandatory | Always | D7, W1A-F-12 |
| Price | Mandatory | Always | D7, CV-03 |
| **Selected properties** — hero subset of specs | Mandatory | Always | W1A-F-02: currently L×W×H×mass only |
| **Category-critical properties** — section count, bowl size, material, construction type | **Mandatory addition to hero subset** | Always, first screen | IA-01: L×W×H insufficient for sink decisions (WH-14) |
| Primary CTA (cart + qty) | Mandatory | Always | CV-03 |
| Compare + favorites | Recommended | Always | PS-03; needs discoverability (MO-04) |
| Product image(s) | Mandatory | Always | W2-F-01: 1 image today — count is content issue, zone assignment is architectural |
| **Subtitle / mini-description** | Mandatory when populated; **must not be placeholder** | Always | W1A-F-03 |

**Hero must NOT contain:** Demo brand logo (W1A-F-04); duplicate full spec table (ID-01); unrelated «Похожие» products.

**Category-critical hero properties (by family — v1 minimum):**

| Family | Hero properties beyond L×W×H×mass |
|--------|--------------------------------|
| Моечные ванны | Section count, bowl dimensions, material (AISI grade), construction (цельнотянутая/сварная) |
| Столы / neutral (pattern) | Configuration type, presence of sink/bowl, material |
| *Other families* | **OPEN QUESTION** — W1E deferred; apply «top 3 discriminating attrs from spec table» rule |

##### Primary zone

**Purpose:** Confirm fit and complete specification review — visible without tab switch for **minimum viable decision set**.

| Information | Priority | When visible | Why |
|-------------|----------|--------------|-----|
| **Structured description** — назначение, комплектация, ключевые отличия | Mandatory | Default visible (tab or inline) | D8 partial self-serve |
| **Minimum spec summary** — 5–8 rows: category-critical + logistics (вес нетто/брутто, упаковка) | **Mandatory, default-visible** — not hidden behind inactive tab | W1A-F-05, W2-F-03: 20+ rows exist but hidden | Reduces «under-informative» perception without new data |
| Full spec table (Характеристики) | Mandatory | Available via tab or expand — full 20+ rows | W1A-F-05; Trapeza pattern (W1D) |
| Documents list | Mandatory when files exist | Tab or linked from primary zone | W1A-F-05; isolated today (W2 Fragmentation) |

**Packaging rule:** Hero selected props and spec table **must not duplicate the same 4 rows** without incremental value — hero = decision subset; spec table = complete record (ID-01).

##### Secondary zone

**Purpose:** Support comparison and adjacent decisions within **same series**.

| Information | Priority | When visible | Why |
|-------------|----------|--------------|-----|
| **In-series alternatives** — SKUs from same series (sizes, sections, Н variants) | **Mandatory replacement for misaligned «Похожие»** | Below primary zone | W1A-F-06 priority #1; WH-07 |
| Compare entry / «добавлено к сравнению» feedback | Recommended | Near in-series block | PS-03 |
| Link back to series listing with filter context | Recommended | When buyer entered from filtered listing | PS-04 |

**«Похожие товары» rule:** If retained, must be **reclassified** as «Другие серии» or «Другие типы» with explicit scope label — never default-prominent when showing different product families (котломойки on sink PDP, W1A-F-06).

##### Reference zone

**Purpose:** Deep reference material for engineering/procurement — not required for initial fit decision.

| Information | When | Why |
|-------------|------|-----|
| Full documentation (PDFs, certificates per SKU) | Tab «Документы» | W1A-F-05 |
| Extended description / long-form | Below specs or tab | ID-04 |
| Breadcrumb trail (4 levels) | Top of page | W1A-F-10 — navigation context |
| **Not in v1:** Q&A community block (Trapeza has; not observed on BZPM; no evidence of need) |

##### Related zone

**Purpose:** Continuation paths **outside current series** — deprioritized vs in-series alternatives.

| Information | When | Why |
|-------------|------|-----|
| Cross-family related products (accessories, compatible equipment) | Optional, clearly labeled «Сопутствующие» | Only when relationship is valid |
| Cross-series «upgrade/downgrade» links | Optional prose links in series context line — not carousel | Addresses D3 without matrix |

##### Commercial zone

**Purpose:** B2B procurement confidence **at conversion point** (CV-01).

| Information | Priority | When visible | Why |
|-------------|----------|--------------|-----|
| Price + availability (ref from hero) | Mandatory | Near CTA | CV-03 |
| **Lead time** for «Под заказ» | Mandatory when applicable | Hero + commercial zone | W1B-F-09 |
| **Delivery summary** — region, terms, link to «Доставка» | Recommended | Commercial zone, adjacent to CTA | CV-01; absent today |
| **Dealer / opt path** — link or compact CTA «Купить как дилер» | Recommended | Commercial zone | CV-01; exists in header only |
| Consultative CTA («Задать вопрос» / «Поможем подобрать») | Mandatory | **Elevated: visible at or before primary zone end** — not only below tabs | PS-05, CV-02 |
| Trust micro-signals (сертификация, «Сделано в России») | Optional | Near buy box | CV-04 |
| Legal price disclaimer | Optional | Footer of commercial zone | CV-05 |

**Commercial zone must NOT:** Repeat full dealer application form; repeat site-wide advantages blocks verbatim.

#### PDP Information Architecture (summary)

```text
PDP — information zones (top to bottom)

HERO (first screen — «right model in right series?»)
  title · series context (NEW) · article · status · price
  selected props (L×W×H×mass + category-critical)
  CTA + compare/fav · image
  NO placeholder · NO demo brand · NO misaligned «похожие»

PRIMARY (default-visible decision set)
  description summary · min spec summary (5–8 rows, visible)
  full specs (tab/expand) · documents entry

SECONDARY (in-series selection support)
  in-series alternatives (REPLACES misaligned «похожие») · compare affordance
  return-to-series link

REFERENCE
  full docs · extended description · breadcrumbs

RELATED (deprioritized)
  accessories / cross-family — labeled, optional

COMMERCIAL (at CTA)
  lead time · delivery link · dealer/opt path · consultative CTA (elevated)
```

---

## Commercial Block Architecture

### Section F — Commercial Block Architecture

**Objects:** Certificates, advantages, dealer program, consultation blocks, forms.

**Principle:** Tier blocks by **reach** and **decision relevance** — global trust once, procurement at choice points, suppress identical deep-page repeats (W2-F-07, Strategy §5–6).

#### Block classification

##### 1. Global blocks (site-wide or catalog-entry)

| Block | Information | Primary surfaces | When | Why |
|-------|-------------|------------------|------|-----|
| **Header procurement nav** | Дилерам · Доставка · Контакты | All pages via header | Always | Low-cost persistent B2B path (CV-01) |
| **Trust summary** | «Сделано в России», manufacturer certification reference | Catalog root (compact); footer site-wide | Once per catalog session | CV-04; full slider not needed every page |
| **Footer legal / company** | Оферта disclaimer, реквизиты, policy links | All pages | Always | CV-05 |

##### 2. Contextual blocks (choice-point surfaces)

| Block | Information | Surfaces | When | Why |
|-------|-------------|----------|------|-----|
| **Commercial micro-strip** | Lead time · delivery teaser · dealer link | Listing card (when data exists); PDP commercial zone | At SKU evaluation | CV-01; replaces empty `p-card__delivery` |
| **Consultative CTA** | «Поможем подобрать» / «Задать вопрос» | PDP (elevated); parent category (conditional); series page (conditional) | When self-serve insufficient — D8 | PS-05, CV-02 |
| **In-series / family guide** | Prose comparison of series (not matrix) | Series page above listing; parent category below chips | When series choice is high-friction (D3) | WH-01; W1C-F-07 |
| **Compare infrastructure** | `/compare-products` + counter | Header; cards; PDP | When buyer in comparison mode (D9) | W1C-F-09; empty state context fix needed (W1B-F-07) |

##### 3. Conditional blocks (triggered)

| Block | Trigger | Surface | Why |
|-------|---------|---------|-----|
| **Lead time callout** | SKU status = «Под заказ» | Card + PDP hero | W1B-F-09 |
| **Dealer form (full)** | Buyer clicks «Стать дилером» / explicit dealer intent | Dedicated dealer page — **not inline on every catalog page** | W2: excessive repeat |
| **Certificates detail** | Buyer requests proof / tender documentation | Dedicated page or modal from trust summary | W2-F-07 |
| **Discount visibility** | Active promotion on SKU | Card badge + PDP commercial zone | W2 Commercial |
| **Custom equipment CTA** | Buyer on task-heavy path (Scenario E) | `/custom-equipment` + search empty state | WH-08 — **link only in v1**, wizard out of scope |

##### 4. Pages where blocks should NOT appear

| Block | Suppressed on | Why |
|-------|---------------|-----|
| Full certificates slider | Series pages; PDP; deep category pages | Identical repeat, zero incremental decision value (W2-F-07) |
| Full dealer application form | Series pages; PDP; parent category (replace with link) | Same |
| Duplicate advantages grids (identical to catalog root) | All pages below catalog root | W2 duplication |
| Large consultative image block below all tabs only | PDP | PS-05: too late in flow |
| «Похожие товары» (misaligned) | PDP — until realigned to in-series scope | W1A-F-06 |

#### Commercial Block Architecture Model (summary)

```text
GLOBAL (persistent, low footprint)
  header nav · trust summary (compact) · footer legal

CONTEXTUAL (at choice points)
  commercial micro-strip · consultative CTA · series guide prose · compare

CONDITIONAL (triggered)
  lead time · full dealer form (dedicated page) · certificates detail · discount

SUPPRESS on deep catalog surfaces
  full certificate slider · full dealer form · duplicate advantages
```

---

## Mobile Architecture

### Section G — Mobile Information Priority Hierarchy

**Scope:** Information priority only — not responsive layout, breakpoints, or UI patterns.

**Evidence constraint:** Mobile analysis = CSS/HTML inference; no device screenshots (U-04, U-10).

#### Priority tiers (highest first)

Mobile must preserve **decision-equivalent information** to desktop, not necessarily **identical presentation**.

| Priority | Information | Must survive mobile | Rationale |
|----------|-------------|-------------------|-----------|
| **P1 — Critical** | Price, availability, article, primary CTA | Always visible without excessive scroll | MO-01: gallery pushes CTA below fold today |
| **P1 — Critical** | Series context (on PDP) + key discriminating attrs | First screen on PDP | MO-01, MO-02 |
| **P1 — Critical** | Series label + dimensions on listing card | Visible on card without opening PDP | Mobile filter hidden — card is last discrimination layer |
| **P2 — High** | Filter access + **active filter summary** | Filters may be in overlay, but **applied constraints must be visible in results zone** | W1B-F-11: densest tool hidden ≤1024px |
| **P2 — High** | Sort control | Accessible with listing | Category topbar |
| **P2 — High** | Series navigation chips (parent category) | Discoverable — horizontal scroll acceptable if «N more» or partial visibility indicator | 18 chips without indicator (W1B §7) |
| **P2 — High** | Compare / favorites | Labeled or feedback-visible — not icon-only silent | MO-04; tips hidden on mobile (W2 Mobile) |
| **P3 — Medium** | Minimum spec summary on PDP | Visible before or with tab access | MO-03: tabs may be overlooked |
| **P3 — Medium** | In-series alternatives block | Below primary, before cross-family related | Same selection logic as desktop |
| **P3 — Medium** | Consultative CTA | Reachable without scrolling past misaligned carousels | CV-02 |
| **P4 — Lower** | Full spec table, documents | Available via tab/expand | Hidden acceptable if P1–P3 satisfied |
| **P4 — Lower** | Certificates, advantages, dealer form | **Deprioritized or collapsed** on mobile deep pages | Scroll cost (W2 Mobile) |
| **P5 — Lowest** | SEO text blocks | Below fold, collapsed | W1C-F-10 |

#### Mobile suppression rules (information-level)

| Suppress or collapse on mobile | Why |
|--------------------------------|-----|
| Repeated certificates + dealer blocks on category/series | Same information, increased scroll (W2 Mobile) |
| Empty `p-card__delivery` | No information value (W2-F-05) |
| Duplicate availability on card | Wasted vertical space |
| Misaligned «Похожие» carousel before in-series block | High scroll, low relevance (MO-06, PS-01) |

#### Mobile Architecture Model (summary)

```text
MOBILE INFORMATION PRIORITY (descending)

P1  price · stock · article · CTA · series context · key attrs (card + PDP)
P2  filter state · sort · series chips · labeled compare
P3  spec summary · in-series alts · consultative CTA
P4  full specs · documents
P5  SEO · repeated commercial blocks (collapse)
```

---

## Information Ownership Matrix

### Section H — Information Ownership Matrix

**Goal:** Each information type has exactly one **primary surface**; secondary surfaces summarize or link — preventing duplication (W2 Fragmentation + Duplication analyses).

| Information type | Primary surface | Secondary surface | Optional surface | Must NOT appear |
|------------------|-----------------|-------------------|------------------|-----------------|
| **Price** | Listing card; PDP hero | Compare page | Search results | Repeated 3+ times on same card |
| **Availability / qty** | Listing card (single zone); PDP hero | Filter «Только в наличии» | Compare | Duplicated top+body on card (W1B-F-08) |
| **Documents** | PDP Reference zone (tab) | Series page link «Документация серии» if series-level docs exist | Catalog root trust summary | Listing card |
| **Characteristics (full)** | PDP Primary/Reference (spec table) | Compare page | — | Listing card (20+ rows) |
| **Characteristics (decision subset)** | PDP Hero + min spec summary | Listing card (Tier 2 fields) | Filter labels | Duplicated verbatim hero + spec header (ID-01) |
| **Brand** | PDP hero (ЗПМ as manufacturer); site header | Catalog root trust | — | Demo/third-party brand (W1A-F-04) |
| **Series** | Series page H1 + description | PDP series context line; listing card series label | Breadcrumb link | 18-chip row on series page |
| **Category / family** | Parent category H1 + description | Breadcrumbs; megamenu | SEO blocks | Embedded in every card title |
| **Delivery terms** | Dedicated «Доставка» page | PDP commercial zone (summary + link); commercial micro-strip on card **when populated** | Header nav | Empty `p-card__delivery` (W2-F-05) |
| **Dealer program** | Dedicated «Дилерам» page | Header nav; PDP commercial zone (compact CTA) | Catalog root (link only) | Full form on every category/series page (W2-F-07) |
| **Certificates** | Dedicated page or modal | Catalog root trust summary (compact) | PDP commercial zone (micro-signal) | Full slider on series + PDP + every category |
| **Lead time** | Listing card (when под заказ); PDP hero | PDP commercial zone | — | Hidden when status shows под заказ |
| **Dimensions L×W×H** | Listing card structured field; PDP hero selected props | Filter groups; spec table | Product title (prose) | Same 4 values in hero AND spec table header without differentiation |
| **Section count** | Listing card; PDP hero | Filter «Количество секций» (adopt Trapeza pattern, W1D-F-03) | Series description | Only in SKU code |
| **Article / nomenclature code** | Listing card; PDP hero | Search; breadcrumb (abbreviated) | — | Full decoding legend (D-02) |
| **Compare state** | Compare page | Header counter; card/PDP toggle | — | Mixed with «Личный кабинет» empty state (W1B-F-07) |
| **Consultation** | PDP consultative CTA (elevated) | Series/parent conditional CTA | Header contact | Only below all tabs (PS-05) |
| **In-series alternatives** | PDP Secondary zone | Series listing | — | Misaligned «Похожие» cross-family (W1A-F-06) |
| **Advantages (stock/ship/warranty)** | Catalog root (once) | Header links | Footer | Duplicated identically on every catalog level |

---

## Out Of Scope

### Section I — Explicitly NOT Part of v1 Architecture

| Item | Status | Reference |
|------|--------|-----------|
| **Full nomenclature decoding** (ВМЦ-П3-2/500 legend pages) | Out of scope | D-02, R-02 |
| **Full catalog restructuring** (replace OEM series with functional taxonomy) | Rejected at current stage | R-03 |
| **W1E Product Taxonomy Audit** | Deferred | D-01 |
| **OpenCart / ocStore backend redesign** | Excluded lane | R-04, W0-F-05 |
| **Database redesign** | Not in scope | — |
| **Mass content rewrite** (all SKU descriptions, all series copy) | Not required for IA; series description blocks are **architectural placeholders** — copy production is separate workstream | — |
| **Sibling SKU matrix on PDP** | Not market standard; not v1 | V-09 |
| **Task-first wizard** («Find Your Fryer»-style) | Not v1; Henny Penny exception (W1D-F-07) | WH-08 |
| **Copy Trapeza layout, taxonomy, or brand-index navigation** | Rejected | R-01, D-03 |
| **Visual design, wireframes, mockups, CSS, Twig, JS** | Explicitly excluded by charter | Audit state scope |
| **Interactive filter/compare UX specification** | Blocked by UNKNOWN session behavior | U-02, U-03 |
| **Production `bzpm.ru` deployment** | Not authorized | Audit state |
| **Q&A community block on PDP** | No BZPM evidence; Trapeza-specific | W1D |
| **Polygon WIP alignment** | SAFE UNKNOWN | U-12 |

---

## Open Questions

Architecture proceeds with these **UNKNOWN** items flagged for W3 blueprint or operator resolution — architecture does not assume answers.

| ID | Question | Impact on architecture | Evidence gap |
|----|----------|------------------------|--------------|
| OQ-01 | What are the **category-critical hero properties** for non-sink families (столы, стеллажи, тепловое)? | PDP Hero subset rule cannot be fully enumerated | W1E deferred |
| OQ-02 | What is the **backend rule** for «Похожие товары»? | In-series alternatives block may need CMS relation type change | U-05 |
| OQ-03 | Is `p-card__delivery` **empty by design** or missing data feed? | Commercial micro-strip on cards depends on data | U-06 |
| OQ-04 | What does **populated compare table** show — which attributes? | Compare as secondary surface for specs | U-02 |
| OQ-05 | Do filters show **result counts and active chips** after JS apply? | Active filter summary architecture may need client-state spec | U-03 |
| OQ-06 | Should parent category **hide flat grid by default** until series selected — or show with heavy scope labeling? | Major IA fork for parent category model | WH-09 — hypothesis, not validated |
| OQ-07 | What is **`/custom-equipment`** content role in task-path (Scenario E)? | Conditional block for task buyers | U-11 |
| OQ-08 | Production stack PRJ-0009 — does it constrain block registry implementation? | Engineering handoff | U-01 |
| OQ-09 | Mobile touch targets and text clipping — does P1 information actually fit first screen on common devices? | Mobile priority validation | U-04 |
| OQ-10 | Polygon WIP — which findings are already addressed in unpublished work? | Avoid duplicate redesign effort | U-12 |
| OQ-11 | Sort options — should «популярность» / «наличие» be added per Trapeza reference? | Category/series above-listing controls | W1D-F-03 area; not observed on BZPM |
| OQ-12 | Series description content — who owns copy for 18+ series lines? | Series description block is architectural slot; content ownership undefined | Content ops SAFE UNKNOWN |

---

## Document lineage

| Input | Role |
|-------|------|
| [BZPM-FINDINGS-REGISTER-v1.md](BZPM-FINDINGS-REGISTER-v1.md) | Evidence classification |
| [BZPM-REDESIGN-STRATEGY-v1.md](BZPM-REDESIGN-STRATEGY-v1.md) | Strategic themes → architectural principles |
| [BZPM-DECISION-LOG-v1.md](BZPM-DECISION-LOG-v1.md) | Hard constraints |
| [BZPM-AUDIT-STATE-v1.md](BZPM-AUDIT-STATE-v1.md) | Phase boundaries |
| W1A–W2 session reports | Consolidated in findings register; detail in `.recovery-temp/bzpm-audit-extract.txt` (non-canonical) |

**Next phase:** W3 Strategy Formalization & Blueprint — translate this architecture into page blueprints per Website Factory S04–S05 workflow.

---

*BZPM-REDESIGN-ARCHITECTURE-v1 — information architecture only. No UI. No implementation. Designer and engineer should use this document before any visual or code work.*
