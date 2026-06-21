# REPORT — BZPM W5A UX STRUCTURE

**Execution case:** `bzpm-catalog-redesign`  
**Document:** `BZPM-UX-STRUCTURE-v1`  
**Date:** 2026-06-08  
**Lane:** A (Website Factory)  
**Mode:** UX Structure only — no visual design, no wireframes, no UI styling, no implementation  
**Source of truth:** [BZPM-BLUEPRINT-v1.md](BZPM-BLUEPRINT-v1.md) · [BZPM-REDESIGN-ARCHITECTURE-v1.md](BZPM-REDESIGN-ARCHITECTURE-v1.md)

**Rule:** This document defines **information sequence**, **decision sequence**, and **interaction sequence** — not colors, typography, spacing, visual hierarchy, grid systems, or components.

---

## Executive Summary

`BZPM-UX-STRUCTURE-v1` converts [BZPM-BLUEPRINT-v1](BZPM-BLUEPRINT-v1.md) into a **top-to-bottom page sequence** a designer can use to begin low-fidelity UX prototyping without revisiting audits, architecture, or blueprint phases.

**Decision chain preserved:** equipment type → family → series → SKU (W1C-F-01).

**Six catalog surfaces structured:**

| Surface | Block count | Primary buyer decision |
|---------|-------------|------------------------|
| Catalog Root | 6 blocks | D1 — Which equipment class? |
| Mid-level Category | 5 blocks | D1.5 — Which product family within class? |
| Parent Category | 10 blocks | D2–D3 — Right family? Which series? |
| Series Page | 8 blocks | D4–D5 — Which SKU within series? |
| Listing Card | 1 decision model | Open PDP / compare / skip |
| PDP | 22 blocks in 7 zones | D6–D8 — Right model? Fit? Convert? |

**Architectural invariants expressed as UX sequence:**

1. Navigation pages (root, mid-level) execute **orientation and routing** — selection deferred.
2. Parent category: **series navigation first**, flat grid secondary and scope-labeled.
3. Series page: **grid is primary** — coherent 10-SKU scope is efficiency benchmark.
4. PDP: **single-SKU evaluation** — in-series alternatives replace misaligned cross-family «Похожие».
5. Commercial blocks **tiered by decision relevance** — not repeated wallpaper on deep pages.

**Explicitly not in this document:** visual design, wireframes, responsive layout, OpenCart, Twig, CSS, JS, nomenclature decoding (D-02), sibling SKU matrix (V-09), task-first wizards (WH-08).

---

## Section A — Catalog Root UX Structure

**Page:** `/katalog`  
**Page mode:** Type-selection entry point (navigation page, not listing)  
**Primary decision:** D1 — Select equipment class  
**Buyer sees first:** Orientation, then type navigation — not SKU grid.

### Page sequence (top to bottom)

```text
USR-CR-01  Orientation Block
USR-CR-02  Breadcrumb Anchor Block
USR-CR-03  Type Navigation Block          ← primary decision zone
USR-CR-04  Light Procurement Reference Block
USR-CR-05  Trust Summary Block
USR-CR-06  SEO Reference Block            ← below fold only
```

### Block definitions

#### USR-CR-01 — Orientation Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Establish page role and catalog entry context |
| **User question answered** | «Where am I? What is this page for?» |
| **Input** | CMS page title (H1); one-line catalog purpose copy |
| **Output** | Buyer understands this is catalog entry, not a product listing |
| **Next action** | Proceed to type navigation (USR-CR-03) or read procurement links (USR-CR-04) |

**Decision supported:** Pre-D1 orientation — buyer confirms they are at the right entry point.

**Interaction sequence:** Land → read H1 + purpose line → proceed downward.

---

#### USR-CR-02 — Breadcrumb Anchor Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Position buyer in site information architecture |
| **User question answered** | «How do I return to the site root?» |
| **Input** | Site hierarchy: Главная → Каталог |
| **Output** | Navigable path to home |
| **Next action** | Continue into catalog OR navigate to Главная |

**Decision supported:** None — navigation anchor only.

**Interaction sequence:** Optional upward navigation; does not compete with D1.

---

#### USR-CR-03 — Type Navigation Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Execute D1 — route buyer to one of 9 equipment classes |
| **User question answered** | «What kind of equipment do I need?» |
| **Input** | 9 top-level categories: name, representative image, optional SKU count per category |
| **Output** | Navigation to selected mid-level or parent category page |
| **Next action** | Select one category card → exit to family hub or parent category |

**Decision supported:** D1 — equipment type selection.

**Interaction sequence:** Scan 9 entries → select one → leave catalog root in ≤1 click.

**Must NOT contain:** SKU grid, faceted filters, series chips, subcategory taxonomy.

---

#### USR-CR-04 — Light Procurement Reference Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Surface B2B procurement paths without full-form scroll cost |
| **User question answered** | «How do I buy as dealer / arrange delivery / get consultation?» |
| **Input** | Links: Дилерам · Доставка · Консультация |
| **Output** | Buyer aware of procurement entry points |
| **Next action** | Continue catalog browse OR navigate to procurement surface |

**Decision supported:** Pre-procurement awareness — does not replace D1.

**Interaction sequence:** Notice links → optionally leave catalog path.

---

#### USR-CR-05 — Trust Summary Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Establish manufacturer trust (ЗПМ as OEM) once per catalog session path |
| **User question answered** | «Is this a legitimate OEM manufacturer?» |
| **Input** | «Сделано в России», certification reference — summary or link |
| **Output** | Trust signal at first catalog touch |
| **Next action** | Continue to type navigation OR follow link to certificate detail |

**Decision supported:** Trust confirmation — secondary to D1.

**Interaction sequence:** Below type grid or via link/modal — must not block D1.

---

#### USR-CR-06 — SEO Reference Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Search/indexing value; zone description for production areas |
| **User question answered** | «What production zones does this catalog cover?» (reference only) |
| **Input** | Long-form zone description (мойка, подготовка, хранение) |
| **Output** | Indexable reference content |
| **Next action** | None required for catalog navigation |

**Decision supported:** None — reference only; must not compete with D1.

**Interaction sequence:** Below fold only; buyer acting on D1 does not need to scroll through this block first.

---

### Catalog Root — Suppressed zones

| Zone | Why suppressed |
|------|----------------|
| Product SKU grid | Conflicts with type-selection role (W1C-F-02) |
| Faceted filters | Belongs to family/series surfaces |
| Full dealer application form | Replaced by USR-CR-04 |
| Duplicate advantages grids | Wasteful scroll (W2-F-07) |
| Series-level chips | Taxonomy one level down |
| Task-first wizard | Out of v1 scope (WH-08) |
| Placeholder / demo content | Trust erosion (W1A-F-03, W1A-F-04) |

### Catalog Root — Flow summary

**Information flow:**

```text
ENTER → orient (USR-CR-01)
      → anchor hierarchy (USR-CR-02)
      → select equipment class (USR-CR-03) → EXIT to category
      → optional: procurement awareness (USR-CR-04)
      → optional: trust confirmation (USR-CR-05)
      → reference only below fold (USR-CR-06)
```

**Decision flow:**

```text
D1: «What equipment class?» → USR-CR-03 (primary)
Pre-D1: «Am I in the right place?» → USR-CR-01
```

**Navigation flow:**

```text
Expert with article code → bypass via header search (out of page scope)
B2B buyer → USR-CR-04 procurement links
Unsure of class → read type names/images → USR-CR-03 OR header search
```

---

## Section B — Mid-Level Category UX Structure

**Page example:** «Нейтральное оборудование»  
**Page mode:** Navigation page — family hub within equipment class  
**Primary decision:** Select product family (subfamily)  
**Buyer sees first:** Orientation (class scope), then subfamily navigation.

### Page sequence (top to bottom)

```text
USR-ML-01  Orientation Block
USR-ML-02  Breadcrumb Block
USR-ML-03  Subfamily Navigation Block          ← primary decision zone
USR-ML-04  Listing Zone Block                  ← optional, secondary
USR-ML-05  Below-listing Minimal Block         ← optional
```

### Block definitions

#### USR-ML-01 — Orientation Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Define what belongs in this equipment class |
| **User question answered** | «Does my need fit this equipment type?» |
| **Input** | H1 + 2–4 sentence class description |
| **Output** | Buyer understands class scope vs sibling classes |
| **Next action** | Proceed to subfamily selection (USR-ML-03) |

**Decision supported:** D1 confirmation — buyer validates they chose correct equipment class.

---

#### USR-ML-02 — Breadcrumb Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Hierarchy context |
| **User question answered** | «Where am I in the catalog hierarchy?» |
| **Input** | Full path: Главная → Каталог → [Class] |
| **Output** | Navigable hierarchy (4+ levels readable) |
| **Next action** | Navigate up OR continue forward |

**Decision supported:** None — navigation anchor.

---

#### USR-ML-03 — Subfamily Navigation Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Route buyer to product families within class |
| **User question answered** | «Which product family within this class do I need?» |
| **Input** | Subfamily cards/chips: names + optional counts (e.g. 5 entries) |
| **Output** | Navigation to parent family page |
| **Next action** | Select one subfamily → exit to parent category |

**Decision supported:** Family routing within class — sole primary taxonomy surface (P-02).

**Interaction sequence:** Scan subfamilies → select one → leave mid-level in ≤1 click.

**Must NOT contain:** Parallel filter row duplicating chips.

---

#### USR-ML-04 — Listing Zone Block (optional)

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Mixed-family browse when SKU count warrants secondary path |
| **User question answered** | «Can I browse SKUs across families without picking one first?» |
| **Input** | Product cards from multiple families (Listing Card contract) |
| **Output** | Scoped SKU browse; routing to PDP |
| **Next action** | Open PDP OR return to subfamily navigation |

**Decision supported:** Secondary SKU discovery — deferred selection path.

**Trigger:** Present only when SKU count warrants; always secondary to USR-ML-03.

---

#### USR-ML-05 — Below-listing Minimal Block (optional)

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Pagination when listing zone present |
| **User question answered** | «Are there more results on another page?» |
| **Input** | Pagination controls |
| **Output** | Next/previous page of mixed-family results |
| **Next action** | Continue browse OR navigate via subfamily chips |

**Decision supported:** Pagination only.

**Must NOT contain:** Full certificates, dealer form repeat (W2-F-07).

---

### Mid-Level Category — Flow summary

**Information flow:**

```text
ENTER → read class scope (USR-ML-01)
      → confirm hierarchy (USR-ML-02)
      → select subfamily (USR-ML-03) → EXIT to parent category
      OR (optional) browse mixed grid (USR-ML-04) → EXIT to PDP
```

**Decision flow:**

```text
D1 confirm: «Right equipment class?» → USR-ML-01
Family route: «Which family?» → USR-ML-03 (primary)
SKU selection: DEFERRED — not executed on mid-level page
```

**Navigation flow:**

```text
Subfamily Navigation = sole primary taxonomy surface
No parallel «Подкатегории» filter row duplicating chips
```

**Selection flow:**

```text
Selection deferred — mid-level routes, does not execute SKU choice
```

---

## Section C — Parent Category UX Structure

**Page example:** «Моечные ванны»  
**Page mode:** Navigation-primary, selection-secondary  
**Primary decision:** D3 — Select series (preferred) OR scoped flat browse (secondary)  
**Buyer sees first:** Family scope (orientation), then series navigation — not flat SKU grid as primary.

### Complete user journey map

| Journey step | What buyer sees | Decision that happens | Block |
|--------------|-----------------|----------------------|-------|
| 1 — Land | H1 + family description | «Am I in the right family?» (D2) | USR-PC-01 |
| 2 — Orient | Breadcrumb path | «Where am I in hierarchy?» | USR-PC-02 |
| 3 — Narrow | Series chips with counts | «Which OEM series?» (D3) | USR-PC-03 |
| 4 — Scope | Scope indicator + result count + sort | «What am I looking at?» | USR-PC-04 |
| 5 — Refine | Filter access + active summary | «How do I narrow further?» (D4, D5) | USR-PC-05, USR-PC-06 |
| 6 — Select | Product grid (secondary) | «Which SKU?» (pre-PDP) | USR-PC-07 |
| 7 — Continue | Pagination | Multi-page browse | USR-PC-08 |
| 8 — Decide series | Family selection guide (optional) | «Which series without opening each?» (D3) | USR-PC-09 |
| 9 — Escalate | Consultative CTA (conditional) | «Do I need human help?» (D8) | USR-PC-10 |

**Where selection begins:** USR-PC-07 (Product Grid) — but **preferred path** exits at USR-PC-03 to series page.  
**Where browsing ends:** PDP open from card OR compare add OR series page exit via chip.

### Page sequence (top to bottom)

```text
ABOVE LISTING
  USR-PC-01  Orientation Block
  USR-PC-02  Breadcrumb Block
  USR-PC-03  Series Navigation Block              ← primary decision zone
  USR-PC-04  Scope Control Block
  USR-PC-05  Filter Access Block
  USR-PC-06  Active Filter Summary Block

LISTING ZONE
  USR-PC-07  Product Grid Block                    ← secondary

BELOW LISTING
  USR-PC-08  Pagination Block
  USR-PC-09  Family Selection Guide Block          ← optional
  USR-PC-10  Consultative CTA Block                ← conditional
```

### Block definitions — above listing

#### USR-PC-01 — Orientation Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Define family boundaries — what belongs, what does not |
| **User question answered** | «Is this the right product family for my need?» (моечная ванна vs котломойка vs рукомойник) |
| **Input** | H1 + 2–4 sentence family description |
| **Output** | Buyer understands family scope |
| **Next action** | Proceed to series navigation (USR-PC-03) OR apply filters (USR-PC-05) |

**Decision supported:** D2 — right family confirmation.

---

#### USR-PC-02 — Breadcrumb Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Hierarchy context |
| **User question answered** | «What is my path from home to here?» |
| **Input** | 4–5 level path |
| **Output** | Navigable hierarchy; series position inferable |
| **Next action** | Navigate up OR continue forward |

**Decision supported:** None — navigation anchor.

---

#### USR-PC-03 — Series Navigation Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Primary narrowing axis — route to OEM series pages |
| **User question answered** | «Which OEM series line should I explore?» |
| **Input** | Single-axis chips: series names + SKU counts; links to series pages |
| **Output** | Navigation to series page |
| **Next action** | Select series chip → EXIT to series page (preferred path) |

**Decision supported:** D3 — series selection.

**Interaction sequence:** Scan chips with counts → select one → leave parent category for series page.

**Must NOT:** Act as inline filter toggle; mix axes without legend; duplicate filter «Подкатегории» set.

---

#### USR-PC-04 — Scope Control Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Declare what listing currently shows |
| **User question answered** | «What scope of products am I viewing?» |
| **Input** | Scope indicator («Все SKU семейства» vs «Серия: ПРЕМИУМ-3»); result count («N товаров»); sort controls |
| **Output** | Buyer knows current selection scope |
| **Next action** | Change sort OR proceed to grid browse |

**Decision supported:** Scope awareness — prevents confusion when grid shows mixed families.

---

#### USR-PC-05 — Filter Access Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Attribute narrowing within current scope |
| **User question answered** | «How do I narrow by size, sections, material?» |
| **Input** | Filter panel entry (desktop: sidebar; mobile: overlay entry); filter groups scoped to family |
| **Output** | Applied constraints ready for grid refresh |
| **Next action** | Apply filters → view results with active summary (USR-PC-06) |

**Decision supported:** D4 (section count), D5 (dimensions) within declared scope.

**Rule:** Filter «Подкатегории» mirrors chip set OR is removed — no 44 vs 18 mismatch.

---

#### USR-PC-06 — Active Filter Summary Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Show applied constraints in results zone |
| **User question answered** | «What filters are currently active?» |
| **Input** | Active filter chips/tags + clear action |
| **Output** | Visible constraint state |
| **Next action** | Clear filters OR refine further OR browse grid |

**Decision supported:** Filter state confirmation — buyer sees what constraints apply before evaluating cards.

---

### Block definitions — listing zone

#### USR-PC-07 — Product Grid Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | SKU selection within declared scope (secondary on parent) |
| **User question answered** | «Which specific SKU matches my constraints?» |
| **Input** | Listing cards per Section E contract; pagination; empty state; compare affordance per card |
| **Output** | PDP routing, compare adds |
| **Next action** | Open PDP OR add to compare OR select series chip instead |

**Decision supported:** Pre-PDP SKU discrimination (D4, D5, D7 partial).

**Trigger condition:** **OPEN QUESTION OQ-06** — default: show with mandatory scope labeling until operator resolves hide-until-series-selected fork.

**Inside grid must contain:** Listing cards; pagination when >1 page; empty state + link to series chips or filter reset; labeled compare affordance.

---

### Block definitions — below listing

#### USR-PC-08 — Pagination Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Multi-page navigation within scoped results |
| **User question answered** | «Are there more SKUs on another page?» |
| **Input** | Page controls |
| **Output** | Next/previous page of scoped results |
| **Next action** | Continue browse OR exit via series chip |

**Decision supported:** Pagination only.

---

#### USR-PC-09 — Family Selection Guide Block (optional, recommended)

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Prose series comparison without matrix |
| **User question answered** | «How do ПРЕМИУМ, ПРЕМИУМ-3, СТАНДАРТ differ?» |
| **Input** | 3–5 sentence comparison of named series |
| **Output** | Informed series choice without opening each series page |
| **Next action** | Select series chip (USR-PC-03) |

**Decision supported:** D3 — series choice when chips alone insufficient.

---

#### USR-PC-10 — Consultative CTA Block (conditional)

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Human help when self-serve insufficient |
| **User question answered** | «Should I ask an expert instead of browsing?» |
| **Input** | «Поможем подобрать» / «Задать вопрос» |
| **Output** | Consultation lead |
| **Next action** | Initiate consultation OR continue self-serve |

**Decision supported:** D8 — human escalation.

**Trigger:** Family has >10 series OR high chip overlap.

---

### Parent Category — Suppressed zones

| Zone | Why suppressed |
|------|----------------|
| Full certificates slider | W2-F-07 |
| Full dealer application form | W2-F-07 — link only |
| Duplicate advantages grids | W2 duplication |
| Second chip row duplicating parent on child | P-02 |
| Parallel unmatched filter checkboxes | W1B-F-03 |

### Parent Category — Flow summary

**Information flow:**

```text
ENTER → read family scope (USR-PC-01)
      → scan series options (USR-PC-03) → preferred EXIT to series page
      OR → declare scope (USR-PC-04)
      OR → apply filters (USR-PC-05 + USR-PC-06)
      OR → browse grid with scope awareness (USR-PC-07)
      → PDP or compare
      → optional: series guide (USR-PC-09)
      → conditional: consult (USR-PC-10)
```

**Decision flow:**

```text
First decision:  D2 «Right family?» → USR-PC-01
Second decision: D3 «Which series?» → USR-PC-03 (preferred) + USR-PC-09 (support)
Third decision:  D4/D5 narrow → USR-PC-05/06
Fourth decision: Pre-PDP SKU → USR-PC-07 (secondary)
```

**Selection flow:**

```text
Preferred:  Series Navigation → Series Page → SKU grid (coherent scope)
Secondary:  Flat grid with series label on cards + filters (mixed-family page 1)
```

**Navigation flow:**

```text
Series chips = links to series pages, NOT inline filter toggles
Breadcrumbs + chips + filter subcategories must NOT present three conflicting taxonomies
```

---

## Section D — Series Page UX Structure

**Page example:** «Ванны цельнотянутые ПРЕМИУМ-3» (10 SKU)  
**Page mode:** Selection-primary (efficiency benchmark per W2-F-10)  
**Primary decision:** Identify correct SKU within one OEM line  
**Buyer sees first:** Series identity + series description — then scoped grid.

### Page sequence (top to bottom)

```text
BEFORE GRID
  USR-SP-01  Series Identity Block
  USR-SP-02  Series Description Block
  USR-SP-03  Breadcrumb Block
  USR-SP-04  Adjacent Series Navigation Block
  USR-SP-05  Scope Control Block

INSIDE GRID
  USR-SP-06  Product Grid Block                    ← primary page content

AFTER GRID
  USR-SP-07  Pagination Block
  USR-SP-08  Consultative CTA Block                ← conditional
```

### Decision support zones

| Zone type | Blocks | Role |
|-----------|--------|------|
| **Decision support** | USR-SP-02 (series meaning), USR-SP-04 (sibling series exit) | Educate D3; allow reroute without parent chip row |
| **Selection support** | USR-SP-05 (filters + count), USR-SP-06 (grid) | Execute D4, D5, D7 within series scope |
| **Commercial support** | USR-SP-08 (consultative CTA) | D8 escalation when cards insufficient |
| **Suppressed** | Parent 18-chip row; certificates slider; dealer form; degenerate filters; misaligned cross-family cards | W2-F-07, W1B-F-04, P-03 |

### Block definitions — before grid

#### USR-SP-01 — Series Identity Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Series name as page identity |
| **User question answered** | «Which exact OEM line am I viewing?» |
| **Input** | H1 (series name) |
| **Output** | Unambiguous series identity |
| **Next action** | Read series description (USR-SP-02) OR proceed to grid |

**Decision supported:** Series scope confirmation.

---

#### USR-SP-02 — Series Description Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Educate what this series means vs siblings |
| **User question answered** | «What does ПРЕМИУМ-3 mean compared to П, С, Л, СТАНДАРТ?» |
| **Input** | 3–5 sentences: construction type, grade tier, typical use, differentiation vs sibling series |
| **Output** | Buyer understands series tier without decoding nomenclature |
| **Next action** | Apply filters (USR-SP-05) OR browse grid (USR-SP-06) OR check sibling series (USR-SP-04) |

**Decision supported:** D3 — series meaning confirmation.

---

#### USR-SP-03 — Breadcrumb Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Hierarchy context |
| **User question answered** | «How do I return to family or class?» |
| **Input** | 5-level path |
| **Output** | Navigable return to family |
| **Next action** | Navigate up OR continue selection |

**Decision supported:** None — navigation anchor.

---

#### USR-SP-04 — Adjacent Series Navigation Block (conditional)

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Exit/reroute to sibling series without parent chip row |
| **User question answered** | «Should I look at a different series in this family?» |
| **Input** | Compact links to sibling series in same family |
| **Output** | Navigation to adjacent series pages |
| **Next action** | Switch series page OR continue on current series |

**Decision supported:** D3 reroute — navigation without reintroducing 18-chip parent row.

**Trigger:** When sibling series exist.

---

#### USR-SP-05 — Scope Control Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Narrow within series only |
| **User question answered** | «How do I filter to the right size/section within this series?» |
| **Input** | Sort controls; discriminating filter groups only; result count; degenerate filters suppressed |
| **Output** | Meaningful constraints applied to 10-SKU scope |
| **Next action** | View filtered grid (USR-SP-06) |

**Decision supported:** D4 (sections), D5 (dimensions) within series.

---

### Block definitions — inside grid

#### USR-SP-06 — Product Grid Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | SKU selection within coherent series scope — **primary page content** |
| **User question answered** | «Which SKU in this series matches my size and section needs?» |
| **Input** | Listing cards (Section E contract); pagination; empty state; compare affordance |
| **Output** | PDP routing, cart action, compare adds |
| **Next action** | Open PDP OR add to cart/compare OR consult (USR-SP-08) |

**Decision supported:** D4, D5, D7 (pre-PDP) — primary selection surface.

**Inside grid information minimum per card:** article, name, status, price, CTA, L×W×H, section count, lead time if под заказ.

---

### Block definitions — after grid

#### USR-SP-07 — Pagination Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Multi-page within series |
| **User question answered** | «Are there more SKUs in this series?» |
| **Input** | Page controls |
| **Output** | Continued series-scoped browse |
| **Next action** | Continue browse OR open PDP |

**Decision supported:** Pagination only. N/A for ПРЕМИУМ-3 (10 SKU single page).

---

#### USR-SP-08 — Consultative CTA Block (conditional)

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Human help when card differentiators insufficient |
| **User question answered** | «The SKUs look too similar — can someone help me choose?» |
| **Input** | «Поможем подобрать» |
| **Output** | Consultation lead |
| **Next action** | Initiate consultation OR open PDP for closest match |

**Decision supported:** D8 — human escalation.

**Trigger:** Card differentiators insufficient — ПРЕМИУМ-3 case: differences only in code/dims/price.

---

### Series Page — Flow summary

**Information flow:**

```text
ENTER (from parent chip or breadcrumb)
  → read series meaning (USR-SP-02)
  → optionally check sibling series (USR-SP-04)
  → apply discriminating filters (USR-SP-05)
  → compare cards in grid (USR-SP-06)
  → PDP / cart / compare
  → if stuck: consult (USR-SP-08)
```

**Selection flow:**

```text
Series scope = selection scope (P-03)
All grid SKUs ∈ same series
Filters narrow within series only — never expand to cross-family
```

---

## Section E — Listing Card UX Structure

**Object:** Listing Card Decision Model  
**Role:** Discrimination and routing unit — not a mini-PDP.

### Listing Card Decision Model

**Primary card decision:** Open PDP / add to compare / skip — without opening every SKU.

### Three-second comprehension rule

**What must the buyer understand within 3 seconds:**

| Priority | Information | Why |
|----------|-------------|-----|
| 1 | Article code + short name | SKU identity |
| 2 | Availability status + qty (single zone) | Can I get it? (D7) |
| 3 | Price | Commercial viability (D7) |
| 4 | Series label (parent listings) | Am I in right series? (D3) |
| 5 | L×W×H + section count (when populated) | Physical fit (D4, D5) |

### Decision the card SHOULD support

| Decision | Supported by | User question |
|----------|--------------|---------------|
| «Is this the right SKU?» | Article, name, dimensions, sections | «Does this match what I need?» |
| «Is it available at acceptable terms?» | Status, qty, price, lead time | «Can I buy it now / when?» |
| «Is it in the right series?» | Series label (parent grids) | «Is this ПРЕМИУМ-3 or another line?» |
| «Should I compare instead of open?» | Compare affordance (labeled) | «Is this a candidate for side-by-side?» |
| «Should I skip?» | Sufficient attrs to reject | «Not my size/series — move on» |

### Decision the card should NOT be expected to support

| Decision | Why not on card | Where instead |
|----------|-----------------|---------------|
| Full specification review | 20+ rows belong on PDP | PDP Zone 2 (USR-PDP-09, USR-PDP-10) |
| Series education | Prose comparison needs space | Series description (USR-SP-02), family guide (USR-PC-09) |
| Nomenclature decoding | Out of v1 scope (D-02) | — |
| Marketing trust (certificates, advantages) | Commercial blocks tiered elsewhere | Catalog root trust (USR-CR-05), PDP commercial zone |
| Final purchase commitment | Conversion needs full PDP context | PDP hero (USR-PDP-03) |
| Cross-series comparison matrix | Not market standard (V-09) | Compare page + in-series alternatives on PDP |

### Information priority map

```text
TIER 1 — MANDATORY (always visible)
  USR-LC-01  Article code
  USR-LC-02  Short product name
  USR-LC-03  Availability status (single zone)
  USR-LC-04  Price
  USR-LC-05  Primary CTA
  USR-LC-06  PDP link

TIER 2 — STRONGLY RECOMMENDED (parent/series listings when data exists)
  USR-LC-07  Series / line label          ← mandatory on parent grid
  USR-LC-08  L×W×H (structured)
  USR-LC-09  Section count
  USR-LC-10  Lead time (if под заказ)
  USR-LC-11  Thumbnail image (meaningful alt)

TIER 3 — OPTIONAL (context-dependent)
  USR-LC-12  Material
  USR-LC-13  Variant indicator (e.g. «Н»)
  USR-LC-14  Discount badge
  USR-LC-15  Delivery summary (only if populated)

TIER 4 — ACTIONS (secondary to information)
  USR-LC-16  Compare (labeled)
  USR-LC-17  Wishlist / favorites
  USR-LC-18  «Подробнее»
```

### Forbidden on listing card

| Pattern | Why |
|---------|-----|
| Duplicated availability (two zones) | W1B-F-08 |
| Full spec table (20+ attributes) | W1A-F-05 |
| Placeholder / demo content | W1A-F-03 |
| Empty reserved fields (delivery span with no text) | W2-F-05 |
| Marketing prose | W2-F-07 |
| Decoded nomenclature legend | D-02 |
| Misleading status styling | W1B-F-09 |

### Card interaction sequence

```text
SCAN card (3-second rule)
  → MATCH? → open PDP (USR-LC-06) OR add to compare (USR-LC-16)
  → UNCERTAIN? → open PDP for detail
  → REJECT? → skip to next card
  → NO SUITABLE CARDS? → adjust filters (parent/series scope control) OR consult
```

---

## Section F — PDP UX Structure

**Page mode:** Single-SKU evaluation and conversion surface  
**Example SKU:** ВМЦ-П3-2/500 (моечные ванны, ПРЕМИУМ-3)  
**Primary action:** Add to cart OR initiate B2B consultation with sufficient self-serve information consumed.

### Complete decision path (validated against Blueprint)

```text
Correct series?        → USR-PDP-02 Series Context Block
        ↓
Correct model?         → USR-PDP-01 Identity + USR-PDP-04/05 Properties
        ↓
Correct specifications?→ USR-PDP-08 Description + USR-PDP-09 Min Spec + USR-PDP-10 Full Specs
        ↓
Available?             → USR-PDP-03 Commercial Core
        ↓
Suitable alternative?  → USR-PDP-12 In-Series Alternatives
        ↓
Purchase / inquiry     → USR-PDP-03 CTA + USR-PDP-19 Consultative CTA + USR-PDP-18 Commercial Detail
```

**Validation note:** Blueprint confirms this path. «Похожие товары» cross-family block is **removed** from default path — replaced by USR-PDP-12. Sibling SKU matrix is **excluded** (V-09).

### Page sequence (top to bottom)

```text
ZONE 0 — GLOBAL
  USR-PDP-00  Breadcrumb Block

ZONE 1 — HERO (first screen)
  USR-PDP-01  Product Identity Block
  USR-PDP-02  Series Context Block
  USR-PDP-03  Commercial Core Block
  USR-PDP-04  Selected Properties Block
  USR-PDP-05  Category-Critical Properties Block
  USR-PDP-06  Media Block
  USR-PDP-07  Secondary Actions Block

ZONE 2 — PRIMARY
  USR-PDP-08  Description Block
  USR-PDP-09  Minimum Spec Summary Block
  USR-PDP-10  Full Specifications Block
  USR-PDP-11  Documents Entry Block

ZONE 3 — SECONDARY
  USR-PDP-12  In-Series Alternatives Block
  USR-PDP-13  Compare Feedback Block
  USR-PDP-14  Return-to-Series Block

ZONE 4 — REFERENCE
  USR-PDP-15  Full Documentation Block
  USR-PDP-16  Extended Description Block

ZONE 5 — RELATED
  USR-PDP-17  Cross-Family Related Block

ZONE 6 — COMMERCIAL
  USR-PDP-18  Commercial Detail Block
  USR-PDP-19  Consultative CTA Block
  USR-PDP-20  Trust Micro-Signals Block
  USR-PDP-21  Legal Disclaimer Block
```

### Zone 0

#### USR-PDP-00 — Breadcrumb Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Navigation context — 4-level hierarchy to SKU |
| **Decision supported** | Hierarchy orientation |
| **User questions answered** | «Where am I? How do I return to series or family?» |
| **Input** | Category tree path |
| **Output** | Navigable hierarchy; series link inferable |
| **Transition** | Navigate up OR proceed to hero evaluation |

---

### Zone 1 — Hero blocks

#### USR-PDP-01 — Product Identity Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | SKU identity |
| **Decision supported** | «Is this the exact model I searched for?» |
| **User questions answered** | «What is this product called? What is the article code?» |
| **Input** | H1 title; article code; copy-to-clipboard affordance |
| **Output** | Unambiguous SKU identification |
| **Transition** | Confirm identity → evaluate series (USR-PDP-02) |

**Must NOT contain:** placeholder mini-description; demo brand logo.

---

#### USR-PDP-02 — Series Context Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Answer «am I in the right series?» on first screen |
| **Decision supported** | Correct series? (D3 confirmation at SKU level) |
| **User questions answered** | «Which OEM series does this SKU belong to?» |
| **Input** | Series name; link to series listing; optional one-line tier descriptor |
| **Output** | Series affiliation visible before scroll |
| **Transition** | Series confirmed → evaluate fit (USR-PDP-04/05) OR navigate to series page |

---

#### USR-PDP-03 — Commercial Core Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | D7 availability and price at conversion point |
| **Decision supported** | Available? Ready to purchase? |
| **User questions answered** | «Is it in stock? How many? What is the price?» |
| **Input** | Availability status; qty when in stock; price; primary CTA; qty selector |
| **Output** | Purchase-ready state |
| **Transition** | Add to cart OR review specs first (Zone 2) OR consult (USR-PDP-19) |

---

#### USR-PDP-04 — Selected Properties Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Quick physical fit check |
| **Decision supported** | Correct model? (dimensional fit) |
| **User questions answered** | «Will it fit my space?» |
| **Input** | L×W×H×mass (4 props) |
| **Output** | Structured dimensional snapshot |
| **Transition** | Fit confirmed → commercial action OR deeper specs |

---

#### USR-PDP-05 — Category-Critical Properties Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Family-specific fit beyond dimensions |
| **Decision supported** | Correct specifications? (category-critical subset) |
| **User questions answered** | «How many sections? What material? What construction type?» |
| **Input** | Family-specific attribute set (see table below) |
| **Output** | Category-relevant decision data on first screen |
| **Transition** | Fit confirmed → purchase OR full specs (USR-PDP-09/10) OR in-series alts (USR-PDP-12) |

**Family minimum (v1):**

| Family | Category-critical properties |
|--------|------------------------------|
| Моечные ванны | Section count, bowl dimensions, material (AISI grade), construction (цельнотянутая/сварная) |
| Столы / neutral (pattern) | Configuration type, sink/bowl presence, material |
| Other families | **OQ-01** — top 3 discriminating attrs from spec table |

---

#### USR-PDP-06 — Media Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Product visual confirmation |
| **Decision supported** | Visual identity confirmation |
| **User questions answered** | «Does this look like the equipment I expect?» |
| **Input** | Product image(s) |
| **Output** | Visual identification |
| **Transition** | Visual confirmed → continue evaluation |

**Must NOT contain:** misaligned «Похожие» products in hero zone.

---

#### USR-PDP-07 — Secondary Actions Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Compare and save for later |
| **Decision supported** | D9 — should I compare this SKU? |
| **User questions answered** | «Can I save this for later comparison?» |
| **Input** | Compare toggle; favorites toggle |
| **Output** | Item added to compare or wishlist |
| **Transition** | Compare added → feedback (USR-PDP-13) OR continue evaluation |

---

### Zone 2 — Primary blocks

#### USR-PDP-08 — Description Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Confirm fit — назначение, комплектация, ключевые отличия |
| **Decision supported** | Correct model? (functional fit) |
| **User questions answered** | «What is this product for? What is included?» |
| **Input** | Structured product description |
| **Output** | Buyer understands product role and package |
| **Transition** | Fit confirmed → specs OR alternatives OR purchase |

---

#### USR-PDP-09 — Minimum Spec Summary Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Default-visible decision set |
| **Decision supported** | Correct specifications? (without tab switch) |
| **User questions answered** | «What are the key technical parameters?» |
| **Input** | 5–8 rows: category-critical attrs + logistics (вес нетто/брутто, упаковка) |
| **Output** | Meaningful spec context at load |
| **Transition** | Sufficient → purchase OR full specs (USR-PDP-10) OR in-series alts |

---

#### USR-PDP-10 — Full Specifications Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Complete technical record (20+ rows) |
| **Decision supported** | Engineering/procurement-grade specification review |
| **User questions answered** | «What is the complete technical specification?» |
| **Input** | Full attribute table |
| **Output** | All rows accessible via tab or expand |
| **Transition** | Specs confirmed → purchase OR documents (USR-PDP-11/15) |

---

#### USR-PDP-11 — Documents Entry Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Route to downloadable assets |
| **Decision supported** | Documentation availability for tender/engineering |
| **User questions answered** | «Are there PDFs, certificates, drawings?» |
| **Input** | Document list or tab entry |
| **Output** | PDF/download access |
| **Transition** | Download OR return to purchase decision |

---

### Zone 3 — Secondary blocks

#### USR-PDP-12 — In-Series Alternatives Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Within-series SKU comparison — **replaces misaligned «Похожие»** |
| **Decision supported** | Suitable alternative? (same series, different size/section/variant) |
| **User questions answered** | «Is there a better size or section count in this series?» |
| **Input** | SKUs from same series as current PDP |
| **Output** | Navigation to sibling SKUs |
| **Transition** | Switch to sibling PDP OR confirm current SKU → purchase |

**Rule:** Cross-family items never occupy this block's position.

---

#### USR-PDP-13 — Compare Feedback Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Confirm compare action |
| **Decision supported** | Compare action acknowledgment |
| **User questions answered** | «Was my compare action successful?» |
| **Input** | Compare state from USR-PDP-07 |
| **Output** | «Добавлено к сравнению» feedback |
| **Transition** | Continue compare build OR return to evaluation |

---

#### USR-PDP-14 — Return-to-Series Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Resume browsing with filter context |
| **Decision supported** | Continue browsing without hierarchy re-navigation |
| **User questions answered** | «How do I go back to the listing I came from?» |
| **Input** | Series URL + applied filter state (if any) |
| **Output** | Return to filtered series listing |
| **Transition** | Exit to series page OR stay on PDP |

---

### Zone 4 — Reference blocks

#### USR-PDP-15 — Full Documentation Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Deep documentation for tender/engineering |
| **Decision supported** | Procurement documentation completeness |
| **User questions answered** | «Where are all downloadable documents?» |
| **Input** | PDFs, certificates per SKU |
| **Output** | Downloadable proof package |
| **Transition** | Download OR purchase |

---

#### USR-PDP-16 — Extended Description Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Long-form reference |
| **Decision supported** | Deep product understanding (non-blocking) |
| **User questions answered** | «Is there more detailed product narrative?» |
| **Input** | Extended marketing/technical prose |
| **Output** | Deep product narrative |
| **Transition** | Reference only — not required for initial fit |

---

### Zone 5 — Related blocks

#### USR-PDP-17 — Cross-Family Related Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Continuation paths outside current series |
| **Decision supported** | Accessory / compatible equipment discovery |
| **User questions answered** | «What related equipment might I also need?» |
| **Input** | Accessories, compatible equipment — valid relationships only |
| **Output** | Navigation to related products |
| **Transition** | Explore related OR return to in-series decision |

**Must NOT:** Appear before USR-PDP-12; use «Похожие» label for cross-family items.

---

### Zone 6 — Commercial blocks

#### USR-PDP-18 — Commercial Detail Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | B2B procurement confidence at CTA |
| **Decision supported** | Purchase / inquiry (B2B context) |
| **User questions answered** | «What are lead time, delivery terms, dealer options?» |
| **Input** | Price + availability (ref from USR-PDP-03); lead time when под заказ; delivery summary + link; dealer/opt path link |
| **Output** | Procurement-ready context |
| **Transition** | Purchase OR dealer path OR consult |

---

#### USR-PDP-19 — Consultative CTA Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Human escalation when self-serve insufficient (D8) |
| **Decision supported** | Purchase / inquiry via human channel |
| **User questions answered** | «Can I talk to someone about this SKU?» |
| **Input** | «Задать вопрос» / «Поможем подобрать» |
| **Output** | Consultation lead |
| **Transition** | Initiate consultation OR complete self-serve purchase |

**Position rule:** Visible at or before primary zone end — not only below all tabs.

---

#### USR-PDP-20 — Trust Micro-Signals Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Lightweight trust at conversion |
| **Decision supported** | Manufacturer trust reinforcement |
| **User questions answered** | «Is this OEM-certified / made in Russia?» |
| **Input** | «Сделано в России», certification badge |
| **Output** | Trust reinforcement near buy box |
| **Transition** | Purchase confidence increased |

---

#### USR-PDP-21 — Legal Disclaimer Block

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Price/legal transparency |
| **Decision supported** | Legal compliance awareness |
| **User questions answered** | «What are the legal terms of this offer?» |
| **Input** | Оферта / price disclaimer text |
| **Output** | Legal compliance |
| **Transition** | Informational only |

---

### PDP — Suppressed zones

| Zone | Why suppressed |
|------|----------------|
| Misaligned «Похожие товары» (cross-family default) | W1A-F-06 — replaced by USR-PDP-12 |
| Full dealer application form inline | W2-F-07 |
| Full certificates slider | W2-F-07 |
| Duplicate advantages grids | W2 duplication |
| In-page sibling SKU matrix | V-09 |
| Placeholder mini-description | W1A-F-03 |
| Demo brand logo | W1A-F-04 |
| Q&A community block | No BZPM evidence |

---

## Section G — Mobile UX Structure

**Scope:** Information priorities per page type — not layout, breakpoints, or responsive patterns.

**Rule:** Mobile preserves **decision-equivalent information**, not DOM parity (P-09).

### Priority tier definitions

| Tier | Meaning |
|------|---------|
| **P1 — Critical** | Must be reachable without excessive scroll; decision cannot proceed without it |
| **P2 — High** | Strongly affects selection quality; may live in overlay if state is visible |
| **P3 — Medium** | Improves decision confidence; acceptable below P1–P2 |
| **P4 — Lower** | Reference depth; hidden behind tab/expand acceptable |
| **P5 — Lowest** | Non-decision content; collapse or defer |

### G1 — Catalog Root (mobile)

| Priority | Blocks / information |
|----------|---------------------|
| **P1** | USR-CR-03 Type Navigation (9 category entries) |
| **P2** | USR-CR-01 Orientation; USR-CR-04 Light Procurement Reference |
| **P3** | USR-CR-05 Trust Summary (compact) |
| **P4** | USR-CR-02 Breadcrumb |
| **P5** | USR-CR-06 SEO Reference |

---

### G2 — Mid-level Category (mobile)

| Priority | Blocks / information |
|----------|---------------------|
| **P1** | USR-ML-03 Subfamily Navigation |
| **P2** | USR-ML-01 Orientation; USR-ML-02 Breadcrumb |
| **P3** | USR-ML-04 Listing Zone — cards Tier 1–2 |
| **P4** | Sort / filter (if listing present) |
| **P5** | Below-listing commercial (must remain suppressed) |

---

### G3 — Parent Category (mobile)

| Priority | Blocks / information |
|----------|---------------------|
| **P1** | USR-PC-03 Series Navigation chips; listing card Tier 1 (price, status, article, CTA) |
| **P2** | USR-PC-06 Active Filter Summary; sort; USR-PC-04 scope indicator + count; USR-PC-01 Orientation |
| **P3** | USR-PC-05 Filter access (overlay acceptable); series label + dimensions on cards; labeled compare |
| **P4** | USR-PC-09 Family Selection Guide; USR-PC-08 Pagination |
| **P5** | SEO text; suppressed commercial blocks |

**Mobile-specific rule:** Filters may be in fullscreen overlay — **applied constraints must appear in results zone** (USR-PC-06 = P2, not hidden inside closed overlay).

---

### G4 — Series Page (mobile)

| Priority | Blocks / information |
|----------|---------------------|
| **P1** | USR-SP-06 grid Tier 1: price, status, article, CTA; USR-SP-02 series description opening line |
| **P2** | USR-SP-05 scoped filters + result count; L×W×H + section count on cards; labeled compare |
| **P3** | Full USR-SP-02 series description; card Tier 2; USR-SP-08 Consultative CTA (if triggered) |
| **P4** | USR-SP-04 Adjacent series links; USR-SP-07 Pagination; sort |
| **P5** | Suppressed commercial blocks |

---

### G5 — Listing Card (mobile)

| Priority | Information |
|----------|-------------|
| **P1** | USR-LC-04 Price; USR-LC-03 Availability; USR-LC-01 Article; USR-LC-05 Primary CTA |
| **P2** | USR-LC-07 Series label; USR-LC-08 L×W×H; USR-LC-09 Section count |
| **P3** | USR-LC-10 Lead time (if под заказ); USR-LC-11 Image; USR-LC-18 «Подробнее» |
| **P4** | USR-LC-12 Material; USR-LC-13 Variant; USR-LC-14 Discount; USR-LC-15 Delivery (if populated) |
| **P5** | — |

**Suppress on mobile card:** duplicate status; empty delivery; icon-only compare without label.

---

### G6 — PDP (mobile)

| Priority | Blocks / information |
|----------|---------------------|
| **P1** | USR-PDP-03 Commercial Core; USR-PDP-02 Series Context; USR-PDP-04/05 key properties; USR-PDP-01 Article |
| **P2** | USR-PDP-07 labeled compare/favorites; USR-PDP-09 Minimum Spec Summary |
| **P3** | USR-PDP-12 In-Series Alternatives; USR-PDP-19 Consultative CTA; USR-PDP-08 Description opening |
| **P4** | USR-PDP-10 Full Specifications; USR-PDP-11/15 Documents; USR-PDP-06 Media (full gallery) |
| **P5** | USR-PDP-16 Extended Description; USR-PDP-17 Cross-Family Related; repeated certificates/advantages/dealer blocks |

**Suppress on mobile PDP:** misaligned «Похожие» before in-series block; duplicate availability; full dealer form.

---

## Section H — Cross-Page UX Rules

Rules derived from Blueprint Section H (CP-01–CP-33). Apply on **every** catalog surface.

### H1 — One decision per page type

| Rule ID | Statement |
|---------|-----------|
| **UX-01** | Each page type supports **one primary buyer decision** — secondary decisions must not compete for first-screen attention. |
| **UX-02** | Catalog root primary = D1 (equipment class). Mid-level primary = family route. Parent primary = D3 (series). Series primary = SKU within series. PDP primary = single-SKU evaluation + conversion. |
| **UX-03** | When two decision surfaces compete (chips + flat grid on parent), **navigation decision ranks above selection** — series chips before grid browse. |

### H2 — One primary selection surface

| Rule ID | Statement |
|---------|-----------|
| **UX-04** | Each page has **one primary selection or navigation surface** — no parallel chip/filter/breadcrumb taxonomy redundancy (CP-15). |
| **UX-05** | Parent category: series chips = primary taxonomy; filters = attribute narrowing within declared scope; grid = output surface. |
| **UX-06** | Series page: grid = primary; adjacent series links = secondary navigation only. |

### H3 — Navigation vs selection sequence

| Rule ID | Statement |
|---------|-----------|
| **UX-07** | Catalog root and mid-level execute **navigation only** — SKU grid never primary (CP-11). |
| **UX-08** | Parent category: series navigation is **primary above listing**; flat grid is secondary and scope-labeled (CP-12). |
| **UX-09** | Series page: grid is primary; parent 18-chip row must not reappear (CP-13). |
| **UX-10** | PDP: single-SKU evaluation — no in-page selection matrix (CP-14, V-09). |

### H4 — Information ownership in sequence

| Rule ID | Statement |
|---------|-----------|
| **UX-11** | Each fact type appears in **one primary position** per view; secondary positions summarize or link (CP-01). |
| **UX-12** | Price: once per card; once in PDP hero — not repeated 3+ times on same view (CP-02). |
| **UX-13** | Availability: single zone on card; single zone in PDP hero (CP-03). |
| **UX-14** | Full specs (20+ rows): PDP only — never on listing card (CP-04). |
| **UX-15** | In-series alternatives: PDP Zone 3 primary — never misaligned cross-family «Похожие» as default (CP-10). |

### H5 — Commercial block sequence discipline

| Rule ID | Statement |
|---------|-----------|
| **UX-16** | Global trust appears **once** at catalog entry — not repeated identically on every subpage (CP-19). |
| **UX-17** | Consultative CTA on PDP must be **elevated** — reachable before scrolling past all primary content (CP-20). |
| **UX-18** | Commercial signals appear **at choice points** (card, PDP CTA) — not as footer wallpaper (CP-21). |
| **UX-19** | Empty reserved commercial fields **must not render** in sequence (CP-22). |

### H6 — Decision chain integrity

| Rule ID | Statement |
|---------|-----------|
| **UX-20** | Decision chain type → family → series → SKU must be **recoverable from page sequence** — buyer can name their position at any point. |
| **UX-21** | Expert article-code path via header search must not be obstructed by mandatory below-fold blocks on catalog root (CP-28). |
| **UX-22** | Compare affordances require **accessible naming** on mobile — not icon-only silent actions (CP-29). |
| **UX-23** | Filter overlay on mobile: applied constraints must appear in **results zone sequence**, not only inside closed overlay. |

### H7 — v1 scope exclusions in sequence

| Rule ID | Statement |
|---------|-----------|
| **UX-24** | No nomenclature decoding legend in page sequence (CP-30, D-02). |
| **UX-25** | No task-first wizard on catalog root (CP-31, WH-08). |
| **UX-26** | No Trapeza layout/taxonomy copy (CP-32, R-01). |
| **UX-27** | Series description blocks are **architectural slots** — copy production is separate workstream (CP-33, OQ-12). |

---

## Section I — Decision Flow Validation

Validation of UX structure against completed audits and approved artifacts. Status key:

| Status | Meaning |
|--------|---------|
| **RESOLVED** | UX structure defines sequence that resolves finding at structure level |
| **PARTIAL** | Structure addresses intent; content, operator decision, or implementation still required |
| **UNRESOLVED** | Finding remains open |
| **IMPL-DEPENDENT** | Requires runtime/build verification beyond UX structure |

### I1 — W1A Product Audit

| Finding | UX structure mapping | Status | Notes |
|---------|---------------------|--------|-------|
| W1A-F-01 PDP = single-SKU | Section F, UX-10 | **RESOLVED** | No in-page matrix |
| W1A-F-02 Hero 4 props only | USR-PDP-04, USR-PDP-05 | **RESOLVED** | Category-critical extension |
| W1A-F-03 Placeholder mini-description | USR-PDP-01 suppressed | **RESOLVED** | Forbidden in hero |
| W1A-F-04 Demo brand logo | USR-PDP-01 suppressed | **RESOLVED** | Forbidden in hero |
| W1A-F-05 Specs hidden in tabs | USR-PDP-09, USR-PDP-10 | **RESOLVED** | Min spec default-visible in sequence |
| W1A-F-06 «Похожие» = котломойки | USR-PDP-12 replaces default path | **RESOLVED** | Priority #1 |
| W1A-F-07 Icon-only compare/fav | USR-PDP-07, UX-22 | **RESOLVED** | Labeled actions required |
| W1A-F-08 Gallery 1 image | USR-PDP-06 | **PARTIAL** | Zone in sequence; image count = content |
| W1A-F-09 Reference table 404 | — | **UNRESOLVED** | Out of UX structure scope |
| W1A-F-10 Breadcrumbs 4-level | USR-PDP-00, all breadcrumb blocks | **RESOLVED** | Mandatory in sequence |
| W1A-F-11 Article copy | USR-PDP-01, USR-LC-01 | **RESOLVED** | Mandatory |
| W1A-F-12 Stock qty shown | USR-PDP-03, USR-LC-03 | **RESOLVED** | Single zone rule |
| WH-11 «Похожие» breaks path | USR-PDP-12 | **RESOLVED** | |
| WH-12 No sibling matrix bounce | USR-PDP-12 + series grid | **PARTIAL** | Mitigated; matrix excluded (V-09) |
| WH-13 Missing series context | USR-PDP-02 | **RESOLVED** | First-screen in hero sequence |
| WH-14 Insufficient hero props | USR-PDP-05 | **RESOLVED** | Family-specific rule |
| WH-15 B2B context near CTA | USR-PDP-18, USR-PDP-19 | **RESOLVED** | Commercial zone in sequence |

---

### I2 — W1B Category Audit

| Finding | UX structure mapping | Status | Notes |
|---------|---------------------|--------|-------|
| W1B-F-01 Thin cards | Section E Tier 2 | **RESOLVED** | Discriminating fields in card sequence |
| W1B-F-02 18 chips + 36 filters | USR-PC-03, USR-PC-05, USR-PC-06 | **RESOLVED** | Single taxonomy + synced filter |
| W1B-F-03 44 vs 18 filter mismatch | USR-PC-05, UX-04 | **RESOLVED** | Mirror or remove |
| W1B-F-04 Degenerate filters on series | USR-SP-05 | **RESOLVED** | Suppress degenerate groups |
| W1B-F-05 Placeholder chip icons | USR-PC-03 | **PARTIAL** | Structure defines name+count; image = content |
| W1B-F-06 Mixed 5 families page 1 | USR-LC-07, USR-PC-04 | **RESOLVED** | Series label + scope indicator |
| W1B-F-07 Compare empty = ЛК | UX-22, Section E | **PARTIAL** | Rule stated; **IMPL-DEPENDENT** |
| W1B-F-08 Duplicate status on card | USR-LC-03, UX-13 | **RESOLVED** | Single zone |
| W1B-F-09 Под заказ styling | Section E forbidden | **RESOLVED** | Semantic rule |
| W1B-F-10 No active filter summary | USR-PC-06 | **RESOLVED** | Mandatory in sequence |
| W1B-F-11 Mobile filter overlay | G3 P2, UX-23 | **RESOLVED** | Active summary in results zone |
| WH-06 Thin for pre-PDP compare | Section E Tier 2 | **RESOLVED** | Within V-12 pattern |

---

### I3 — W1C Buyer Decision Flow

| Finding | UX structure mapping | Status | Notes |
|---------|---------------------|--------|-------|
| W1C-F-01 Decision chain | All sections | **RESOLVED** | Chain in page sequences |
| W1C-F-02 Catalog = 9 cards | USR-CR-03 | **RESOLVED** | |
| W1C-F-03 Chips + flat grid simultaneous | Section C journey map, UX-03 | **PARTIAL** | Grid secondary; OQ-06 fork open |
| W1C-F-04 Search by article works | UX-21 | **RESOLVED** | Expert bypass preserved |
| W1C-F-05 Dimension search | USR-LC-08, USR-PC-05 | **RESOLVED** | L×W×H on card + filters |
| W1C-F-06 Task query empty | UX-25 | **PARTIAL** | Link-only v1 |
| W1C-F-07 No series description | USR-SP-02, USR-PC-09 | **RESOLVED** | NEW in sequence |
| W1C-F-08 Placeholder + «Похожие» on path | USR-PDP-01, USR-PDP-12 | **RESOLVED** | |
| W1C-F-09 Compare infra exists | USR-LC-16, USR-PDP-07 | **RESOLVED** | |
| W1C-F-10 SEO text no task nav | USR-CR-06, UX-25 | **RESOLVED** | Below fold |
| WH-01 No guided series choice | USR-SP-02, USR-PC-09 | **RESOLVED** | Prose guides in sequence |
| WH-09 Chips + grid reduces series-first | Section C, UX-03 | **PARTIAL** | OQ-06 unvalidated |
| WH-10 Product database behavior | UX-20 | **RESOLVED** | Retained with guided layers |

---

### I4 — W1D Competitor Intelligence

| Finding | UX structure mapping | Status | Notes |
|---------|---------------------|--------|-------|
| W1D-F-01 Trapeza database model | UX-20 | **RESOLVED** | Database-first retained |
| W1D-F-02 Functional subtaxonomy | UX-26, USR-PC-03 | **RESOLVED** | OEM series retained |
| W1D-F-03 Section-count filters | USR-LC-09, USR-PC-05 | **RESOLVED** | Filter attribute adopted |
| W1D-F-04 Trapeza PDP brand/model | USR-PDP-02 | **PARTIAL** | Series context — not marketplace pattern |
| W1D-F-09 No sibling matrix on PDP | UX-10 | **RESOLVED** | V-09 validated |
| W1D-F-10 Thin cards market norm | Section E | **RESOLVED** | V-12 — enrichment only |
| V-06 No task wizard | UX-25 | **RESOLVED** | |
| V-09 Sibling matrix not standard | UX-10 | **RESOLVED** | |
| R-01 / D-03 No Trapeza copy | UX-26 | **RESOLVED** | |

---

### I5 — W2 Information Density

| Finding | UX structure mapping | Status | Notes |
|---------|---------------------|--------|-------|
| W2-F-01 PDP gallery 1 slide | USR-PDP-06 | **PARTIAL** | Zone in sequence; media count = content |
| W2-F-02 PDP hero layout | Section F Zone 1 sequence | **RESOLVED** | Information repackaging — not layout |
| W2-F-03 Specs hidden in tabs | USR-PDP-09 | **RESOLVED** | Default-visible in sequence |
| W2-F-04 Card padding/space | Section E | **PARTIAL** | Structure adds fields; physical space = design phase |
| W2-F-05 Empty p-card__delivery | USR-LC-15, UX-19 | **RESOLVED** | Populate or suppress |
| W2-F-06 Catalog root marketing-heavy | Section A sequence | **RESOLVED** | Commercial tiered |
| W2-F-07 Repeated certificates/dealer | Suppressed zones all sections | **RESOLVED** | |
| W2-F-08 Taxonomy on 3 surfaces | UX-04, Section C | **RESOLVED** | |
| W2-F-09 Dimensions on 4 surfaces | UX-11, Section E/F | **RESOLVED** | Differentiated roles |
| W2-F-10 ПРЕМИУМ-3 benchmark | Section D | **RESOLVED** | Series structure models benchmark |
| W2-F-11 Owner feedback triangulation | All sections | **RESOLVED** | |
| WH-16 Empty space = layout | USR-PDP-06, USR-PDP-09 | **PARTIAL** | IA addresses; gallery = design |
| WH-17 Thin cards | Section E | **RESOLVED** | |
| WH-18 Repeated footer blocks | UX-16 | **RESOLVED** | |
| WH-19 Placeholder amplifies | UX-11 suppressed zones | **RESOLVED** | |
| WH-20 Below Trapeza on card fields | Section E Tier 2 | **RESOLVED** | |

---

### I6 — W4 Architecture + W5 Blueprint

| Artifact | UX structure mapping | Status | Notes |
|----------|---------------------|--------|-------|
| P-01 Product-database first | UX-20 | **RESOLVED** | |
| P-02 One primary selection surface | UX-04 | **RESOLVED** | |
| P-03 Series scope = selection scope | Section D | **RESOLVED** | |
| P-04 Information at decision point | All block sequences | **RESOLVED** | |
| P-05 Visible packaging ≠ more data | USR-PDP-09 | **RESOLVED** | |
| P-06 No wasteful duplication | UX-11–13 | **RESOLVED** | |
| P-07 Commercial contextual | UX-16–19 | **RESOLVED** | |
| P-08 Trapeza informs, not copies | UX-26 | **RESOLVED** | |
| P-09 Mobile decision-equivalent | Section G | **RESOLVED** | |
| P-10 Status honesty | Open Questions | **RESOLVED** | UNKNOWNs flagged |
| Blueprint block contracts | Sections A–F | **RESOLVED** | Full translation |
| Blueprint CP-01–33 | Section H UX-01–27 | **RESOLVED** | |

---

### I7 — Validation summary

| Category | Count |
|----------|-------|
| **RESOLVED** | 62 |
| **PARTIAL** | 12 |
| **UNRESOLVED** | 1 |
| **IMPL-DEPENDENT** | 3 (grouped under PARTIAL notes) |

**Remaining at UX structure level:**

| Item | Status | Owner |
|------|--------|-------|
| W1A-F-09 Reference table 404 | UNRESOLVED | Content/URL — outside UX structure |
| OQ-06 Parent grid default visibility | PARTIAL | Operator decision |
| OQ-01 Non-sink hero properties | PARTIAL | W1E deferred |
| Compare populated UX (U-02) | IMPL-DEPENDENT | Engineering |
| Filter AJAX active state (U-03) | IMPL-DEPENDENT | Engineering |
| p-card__delivery data feed (U-06) | IMPL-DEPENDENT | Data/Engineering |
| Mobile P1 first-screen fit (U-04, OQ-09) | IMPL-DEPENDENT | Design + device test |

---

## Open Questions

Carried from Blueprint; UX structure does not assume answers.

| ID | Question | UX structure impact |
|----|----------|-------------------|
| OQ-01 | Category-critical hero properties for non-sink families? | USR-PDP-05 incomplete for столы, стеллажи, тепловое |
| OQ-02 | Backend rule for «Похожие товары»? | USR-PDP-12 may need CMS relation type change |
| OQ-03 | `p-card__delivery` empty by design or missing data? | USR-LC-15 conditional |
| OQ-04 | Populated compare table attributes? | Compare secondary surface |
| OQ-05 | Filter AJAX — result counts and active chips? | USR-PC-06 — **IMPL-DEPENDENT** |
| OQ-06 | Hide parent flat grid until series selected? | USR-PC-07 trigger condition |
| OQ-07 | `/custom-equipment` role in task path? | Conditional CTA trigger |
| OQ-08 | PRJ-0009 stack constraints? | Engineering handoff |
| OQ-09 | Mobile P1 fit on common devices? | Section G — **IMPL-DEPENDENT** |
| OQ-10 | Polygon WIP — findings already addressed? | Avoid duplicate effort |
| OQ-11 | Sort options — популярность / наличие? | USR-PC-04, USR-SP-05 |
| OQ-12 | Series description copy ownership? | USR-SP-02, USR-PC-09 — content ops |

---

## Document lineage

| Input | Role |
|-------|------|
| [BZPM-BLUEPRINT-v1.md](BZPM-BLUEPRINT-v1.md) | Direct source — block contracts translated to UX sequence |
| [BZPM-REDESIGN-ARCHITECTURE-v1.md](BZPM-REDESIGN-ARCHITECTURE-v1.md) | Architectural invariants |
| [BZPM-FINDINGS-REGISTER-v1.md](BZPM-FINDINGS-REGISTER-v1.md) | Validation evidence |
| [BZPM-REDESIGN-STRATEGY-v1.md](BZPM-REDESIGN-STRATEGY-v1.md) | Strategic themes |
| [BZPM-DECISION-LOG-v1.md](BZPM-DECISION-LOG-v1.md) | Hard constraints |

**Next phase:** Low-fidelity UX prototyping / visual design (designer handoff from this document).

---

*BZPM-UX-STRUCTURE-v1 — UX structure only. No UI. No wireframes. No implementation. A designer can begin low-fidelity prototyping immediately after reading this document without revisiting audit, architecture, or blueprint phases.*
