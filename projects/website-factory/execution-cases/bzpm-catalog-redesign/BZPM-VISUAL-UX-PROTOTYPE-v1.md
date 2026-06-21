# REPORT — BZPM W6 VISUAL UX PROTOTYPE

**Execution case:** `bzpm-catalog-redesign`  
**Document:** `BZPM-VISUAL-UX-PROTOTYPE-v1`  
**Date:** 2026-06-08  
**Lane:** A (Website Factory)  
**Mode:** Low-fidelity visual UX — block schematics only  
**Source of truth:** [BZPM-UX-STRUCTURE-v1.md](BZPM-UX-STRUCTURE-v1.md) · [BZPM-BLUEPRINT-v1.md](BZPM-BLUEPRINT-v1.md) · [BZPM-REDESIGN-ARCHITECTURE-v1.md](BZPM-REDESIGN-ARCHITECTURE-v1.md)

**Rule:** This document defines **where blocks live**, **how blocks relate**, **what appears first**, and **what receives attention** — not colors, typography, icons, animations, or implementation.

**Explicitly not in this document:** final UI design, design system, branding, OpenCart, Twig, CSS, JS, new audit findings, architecture changes.

---

## Executive Summary

`BZPM-VISUAL-UX-PROTOTYPE-v1` transforms [BZPM-UX-STRUCTURE-v1](BZPM-UX-STRUCTURE-v1.md) into **ASCII page schematics** and **information layout maps** for six catalog surfaces plus listing card.

**Purpose:** A designer can begin wireframes immediately; an OCPilot engineer can understand future page composition before visual design begins.

**Six surfaces prototyped:**

| Surface | Schematics | Primary visual emphasis |
|---------|------------|-------------------------|
| Catalog Root | Desktop + Mobile | Type navigation dominates first screen |
| Mid-level Category | Desktop + Mobile | Subfamily routing; selection deferred |
| Parent Category (Моечные ванны) | Desktop + Mobile | Three layers: Navigation → Selection → Result |
| Series Page (ПРЕМИУМ-3) | Desktop + Mobile | Series scope = grid scope |
| Listing Card | Information layout | Tier 1–4 + 3-second scan model |
| PDP | Desktop + Mobile | Seven evaluation zones + decision ladder |

**Architectural invariants expressed visually:**

1. Navigation pages (root, mid-level) — orientation and routing; no SKU grid as primary.
2. Parent category — series navigation receives first attention; flat grid secondary and scope-labeled.
3. Series page — grid is primary content within coherent series scope.
4. PDP — single-SKU evaluation; in-series alternatives replace misaligned cross-family blocks.
5. Commercial blocks — tiered; suppressed zones marked explicitly on every schematic.

**Block ID convention:** Schematics reference UX Structure block IDs (`USR-CR-*`, `USR-PC-*`, etc.) for traceability to blueprint contracts.

---

## Catalog Root Prototype

**Page:** `/katalog`  
**Page mode:** Navigation — type selection entry  
**Primary decision:** D1 — Which equipment class?  
**Primary action:** Select one of 9 category entries → exit to mid-level or parent category

### Desktop schematic

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  [ SITE HEADER — out of page scope; search bypass for expert path ]         │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  NAVIGATION LAYER                                                           │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  USR-CR-02  Breadcrumb Anchor                                       │    │
│  │  Главная › Каталог                                                  │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  USR-CR-01  Orientation Block                          ◄── read first │    │
│  │  H1: Каталог оборудования                                           │    │
│  │  One-line catalog purpose copy                                      │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  PRIMARY DECISION ZONE — D1                                                 │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  USR-CR-03  Type Navigation Block              ◄◄◄ ATTENTION HERE │    │
│  │                                                                     │    │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐                                │    │
│  │  │ Class 1 │ │ Class 2 │ │ Class 3 │   ... 9 entries total         │    │
│  │  │ + image │ │ + image │ │ + image │   name · image · optional count│    │
│  │  └─────────┘ └─────────┘ └─────────┘                                │    │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐                                │    │
│  │  │ Class 4 │ │ Class 5 │ │ Class 6 │                                │    │
│  │  └─────────┘ └─────────┘ └─────────┘                                │    │
│  │                                                                     │    │
│  │  PRIMARY ACTION: select one card → EXIT to category (≤1 click)      │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  SECONDARY SUPPORT LAYER — does not compete with D1                         │
│  ┌──────────────────────────────┐  ┌──────────────────────────────────┐     │
│  │  USR-CR-04                   │  │  USR-CR-05                       │     │
│  │  Light Procurement Reference │  │  Trust Summary (compact)         │     │
│  │  Дилерам · Доставка ·        │  │  «Сделано в России» · cert link  │     │
│  │  Консультация                │  │                                  │     │
│  │  SECONDARY ACTION: leave     │  │  SECONDARY: trust confirm        │     │
│  │  catalog for procurement     │  │                                  │     │
│  └──────────────────────────────┘  └──────────────────────────────────┘     │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  REFERENCE LAYER — below fold only                                          │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  USR-CR-06  SEO Reference Block                                    │    │
│  │  Long-form zone description (мойка, подготовка, хранение)           │    │
│  │  No required action for catalog navigation                        │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  [ SITE FOOTER ]                                                            │
└─────────────────────────────────────────────────────────────────────────────┘

SUPPRESSED ON THIS PAGE (not shown):
  ✗ Product SKU grid          ✗ Faceted filters         ✗ Series chips
  ✗ Full dealer form          ✗ Duplicate advantages    ✗ Task wizard
  ✗ Placeholder / demo content
```

### Mobile schematic

```text
┌──────────────────────────┐
│  [ SITE HEADER ]         │
├──────────────────────────┤
│                          │
│  P1 — CRITICAL           │
│  ┌────────────────────┐  │
│  │ USR-CR-03          │  │
│  │ Type Navigation    │  │  ◄◄◄ FIRST ATTENTION
│  │                    │  │
│  │ ┌────────────────┐ │  │
│  │ │ Class 1        │ │  │  vertical stack
│  │ │ name + image   │ │  │  or 2-col grid
│  │ └────────────────┘ │  │
│  │ ┌────────────────┐ │  │
│  │ │ Class 2        │ │  │
│  │ └────────────────┘ │  │
│  │ ... (9 entries)    │  │
│  │                    │  │
│  │ PRIMARY ACTION     │  │
│  └────────────────────┘  │
│                          │
│  P2 — HIGH               │
│  ┌────────────────────┐  │
│  │ USR-CR-01          │  │
│  │ Orientation H1     │  │
│  │ + purpose line     │  │
│  └────────────────────┘  │
│  ┌────────────────────┐  │
│  │ USR-CR-04          │  │
│  │ Procurement links  │  │
│  └────────────────────┘  │
│                          │
│  P3 — MEDIUM             │
│  ┌────────────────────┐  │
│  │ USR-CR-05 Trust    │  │
│  │ (compact)          │  │
│  └────────────────────┘  │
│                          │
│  P4 — LOWER              │
│  USR-CR-02 Breadcrumb    │
│                          │
│  P5 — LOWEST (scroll)    │
│  USR-CR-06 SEO Reference   │
│                          │
├──────────────────────────┤
│  [ FOOTER ]              │
└──────────────────────────┘
```

### Expected user path

```text
ENTER /katalog
  │
  ├─► Expert with article code ──► header search bypass (out of page scope)
  │
  ├─► B2B buyer ──► notice USR-CR-04 ──► optional leave to Дилерам/Доставка
  │
  └─► Default path:
        read USR-CR-01 (orient)
          → scan USR-CR-03 (D1: pick equipment class)
            → EXIT to mid-level or parent category

Primary action:    select category card (USR-CR-03)
Secondary actions: procurement links (USR-CR-04); trust link (USR-CR-05)
No selection:      no SKU choice on this page
```

---

## Mid-Level Category Prototype

**Page example:** «Нейтральное оборудование»  
**Page mode:** Navigation — family hub within equipment class  
**Primary decision:** D1.5 — Which product family within class?

### Desktop schematic

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  [ SITE HEADER ]                                                            │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  ORIENTATION LAYER                                                          │
│  USR-ML-02  Breadcrumb:  Главная › Каталог › [Equipment Class]              │
│  USR-ML-01  Orientation Block                                               │
│             H1: Нейтральное оборудование                                    │
│             2–4 sentence class description                                  │
│             Answers: «Does my need fit this equipment type?» (D1 confirm)   │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  PRIMARY DECISION ZONE — family routing                                     │
│  USR-ML-03  Subfamily Navigation Block                    ◄◄◄ ATTENTION     │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐          │
│  │ Subfam 1 │ │ Subfam 2 │ │ Subfam 3 │ │ Subfam 4 │ │ Subfam 5 │  ...     │
│  │ + count  │ │ + count  │ │ + count  │ │ + count  │ │ + count  │          │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────────┘          │
│  PRIMARY ACTION: select one → EXIT to parent category (≤1 click)            │
│  Must NOT: parallel filter row duplicating chips                            │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  SECONDARY LAYER — optional, always subordinate to USR-ML-03                │
│  USR-ML-04  Listing Zone Block (optional)                                   │
│  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐                               │
│  │ Card   │ │ Card   │ │ Card   │ │ Card   │  mixed-family SKU browse      │
│  │ mixed  │ │ mixed  │ │ mixed  │ │ mixed  │  Listing Card contract        │
│  └────────┘ └────────┘ └────────┘ └────────┘                               │
│  SECONDARY ACTION: open PDP OR return to subfamily navigation               │
│  USR-ML-05  Pagination (if listing present)                                  │
└─────────────────────────────────────────────────────────────────────────────┘

SUPPRESSED:
  ✗ Full certificates / dealer form repeat
  ✗ Parallel «Подкатегории» filter row duplicating chips
```

### Mobile schematic

```text
┌──────────────────────────┐
│  [ HEADER ]              │
├──────────────────────────┤
│  P1 — CRITICAL           │
│  ┌────────────────────┐  │
│  │ USR-ML-03          │  │  ◄◄◄ FIRST ATTENTION
│  │ Subfamily Nav      │  │
│  │ ┌────────────────┐ │  │
│  │ │ Subfamily 1    │ │  │
│  │ └────────────────┘ │  │
│  │ ┌────────────────┐ │  │
│  │ │ Subfamily 2    │ │  │
│  │ └────────────────┘ │  │
│  │ ...                │  │
│  │ PRIMARY ACTION     │  │
│  └────────────────────┘  │
│                          │
│  P2 — HIGH               │
│  USR-ML-01 Orientation   │
│  USR-ML-02 Breadcrumb    │
│                          │
│  P3 — MEDIUM (optional)  │
│  USR-ML-04 Listing cards  │
│  (Tier 1–2 only)         │
│                          │
│  P4 — LOWER (optional)   │
│  Sort / filter           │
│                          │
│  P5 — SUPPRESSED         │
│  ✗ Below-listing         │
│    commercial blocks     │
├──────────────────────────┤
│  [ FOOTER ]              │
└──────────────────────────┘
```

### Flow maps

**Navigation flow:**

```text
Subfamily Navigation (USR-ML-03) = sole primary taxonomy surface
  → select subfamily → parent category page
  OR (optional) browse mixed grid → PDP
```

**Decision flow:**

```text
D1 confirm: «Right equipment class?» → USR-ML-01
Family route: «Which family?»        → USR-ML-03 (primary)
SKU selection: DEFERRED — not on mid-level page
```

**Selection flow:**

```text
Selection deferred — mid-level routes only; does not execute SKU choice
```

---

## Parent Category Prototype

**Page example:** «Моечные ванны»  
**Page mode:** Navigation-primary, selection-secondary  
**Primary decision:** D3 — Select series (preferred) OR scoped flat browse (secondary)

### Three-layer model

```text
┌─────────────────────────────────────────────────────────────────┐
│  LAYER 1 — NAVIGATION                                           │
│  Orient buyer · declare hierarchy · route to series             │
│  Blocks: USR-PC-01, USR-PC-02, USR-PC-03                        │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 2 — SELECTION SUPPORT                                    │
│  Declare scope · refine constraints · show active filters       │
│  Blocks: USR-PC-04, USR-PC-05, USR-PC-06                        │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 3 — RESULT                                               │
│  Display scoped SKU output · pagination · post-browse support   │
│  Blocks: USR-PC-07, USR-PC-08, USR-PC-09, USR-PC-10             │
└─────────────────────────────────────────────────────────────────┘
```

### Desktop schematic

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  [ SITE HEADER ]                                                            │
└─────────────────────────────────────────────────────────────────────────────┘

═══════════════════════════════════════════════════════════════════════════════
  LAYER 1 — NAVIGATION
═══════════════════════════════════════════════════════════════════════════════

  USR-PC-02  Breadcrumb
  Главная › Каталог › [Class] › Моечные ванны

  USR-PC-01  Orientation Block                              ◄── D2: right family?
  H1: Моечные ванны
  2–4 sentence family description
  (моечная ванна vs котломойка vs рукомойник)

  USR-PC-03  Series Navigation Block                        ◄◄◄ PRIMARY ATTENTION
  ┌─────────────────────────────────────────────────────────────────────────┐
  │  [ПРЕМИУМ-3 (10)] [ПРЕМИУМ (24)] [СТАНДАРТ (18)] [П (12)] [С (8)] ...  │
  │  single-axis chips · name + SKU count · links to series pages           │
  │  NOT inline filter toggles                                              │
  │                                                                         │
  │  PREFERRED PATH: select chip → EXIT to series page                      │
  └─────────────────────────────────────────────────────────────────────────┘

═══════════════════════════════════════════════════════════════════════════════
  LAYER 2 — SELECTION SUPPORT
═══════════════════════════════════════════════════════════════════════════════

  USR-PC-04  Scope Control Block
  ┌─────────────────────────────────────────────────────────────────────────┐
  │  Scope: «Все SKU семейства»  │  N товаров  │  Sort: [dropdown]          │
  └─────────────────────────────────────────────────────────────────────────┘

  ┌──────────────────────┬──────────────────────────────────────────────────┐
  │  USR-PC-05           │  USR-PC-06  Active Filter Summary                │
  │  Filter Access       │  ┌────────────────────────────────────────────┐  │
  │  (sidebar)           │  │ [Секции: 2 ×] [L: 1200 ×] [Clear all]     │  │
  │                      │  └────────────────────────────────────────────┘  │
  │  □ Кол-во секций     │                                                  │
  │  □ Размеры L/W/H     │  Applied constraints visible BEFORE grid eval    │
  │  □ Материал          │                                                  │
  │  □ Подкатегории      │  (mirrors chip set OR removed — no 44 vs 18)     │
  │    (synced w/ chips) │                                                  │
  └──────────────────────┴──────────────────────────────────────────────────┘

═══════════════════════════════════════════════════════════════════════════════
  LAYER 3 — RESULT (secondary on parent — scope-labeled)
═══════════════════════════════════════════════════════════════════════════════

  USR-PC-07  Product Grid Block                               ◄── pre-PDP SKU
  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐
  │ Card   │ │ Card   │ │ Card   │ │ Card   │   cards MUST show series label
  │ series │ │ series │ │ series │ │ series │   when scope = all family
  │ label  │ │ label  │ │ label  │ │ label  │
  └────────┘ └────────┘ └────────┘ └────────┘
  SECONDARY PATH: browse grid → PDP or compare
  (OQ-06: default visibility — show with scope labeling until operator resolves)

  USR-PC-08  Pagination

  USR-PC-09  Family Selection Guide (optional, below listing)
  Prose: «ПРЕМИУМ vs ПРЕМИУМ-3 vs СТАНДАРТ differ by…»
  Supports D3 when chips alone insufficient

  USR-PC-10  Consultative CTA (conditional)
  «Поможем подобрать» — trigger: >10 series OR high chip overlap

SUPPRESSED:
  ✗ Full certificates slider    ✗ Full dealer form    ✗ Duplicate advantages
  ✗ Second chip row on child      ✗ Unmatched filter checkboxes
```

### Mobile schematic

```text
┌──────────────────────────┐
│  [ HEADER ]              │
├──────────────────────────┤
│                          │
│  P1 — CRITICAL           │
│  ┌────────────────────┐  │
│  │ USR-PC-03          │  │  ◄◄◄ SERIES CHIPS
│  │ Series Navigation  │  │  horizontal scroll
│  │ [chip][chip][chip] │  │  + partial visibility indicator
│  │ › preferred EXIT   │  │
│  └────────────────────┘  │
│                          │
│  ┌────────────────────┐  │
│  │ USR-PC-07 Grid     │  │
│  │ Card Tier 1:       │  │
│  │ article·status·    │  │
│  │ price·CTA           │  │
│  └────────────────────┘  │
│                          │
│  P2 — HIGH               │
│  USR-PC-06 Active filters│  ◄── must show in results zone
│  USR-PC-04 Scope + count │
│  Sort control            │
│  USR-PC-01 Orientation   │
│                          │
│  P3 — MEDIUM             │
│  [Filters ▼] overlay     │  USR-PC-05
│  entry — constraints     │
│  visible via USR-PC-06   │
│  Card Tier 2:            │
│  series label·L×W×H·     │
│  sections·compare        │
│                          │
│  P4 — LOWER              │
│  USR-PC-09 Series guide  │
│  USR-PC-08 Pagination    │
│                          │
│  P5 — SUPPRESSED         │
│  ✗ SEO text  ✗ certs/dealer repeat
│                          │
├──────────────────────────┤
│  [ FOOTER ]              │
└──────────────────────────┘
```

### Decision and selection flows

```text
DECISION FLOW (top to bottom attention):
  1. D2 «Right family?»     → USR-PC-01
  2. D3 «Which series?»     → USR-PC-03 (+ USR-PC-09 support)
  3. D4/D5 narrow           → USR-PC-05 / USR-PC-06
  4. Pre-PDP SKU            → USR-PC-07 (secondary)

SELECTION FLOW:
  Preferred:  USR-PC-03 → Series Page → coherent SKU grid
  Secondary:  USR-PC-07 flat grid + series label on cards + filters

Where selection begins: USR-PC-07
Where browsing ends:     PDP · compare · series page via chip
```

---

## Series Prototype

**Page example:** «Ванны цельнотянутые ПРЕМИУМ-3» (10 SKU)  
**Page mode:** Selection-primary (efficiency benchmark)  
**Primary decision:** D4–D5 — Which SKU within series?  
**Core invariant:** **Series scope = selection scope (P-03)**

### Desktop schematic

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  [ SITE HEADER ]                                                            │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  SERIES CONTEXT ZONE — before grid                                          │
│                                                                             │
│  USR-SP-01  Series Identity                                                │
│  H1: Ванны цельнотянутые ПРЕМИУМ-3                                          │
│                                                                             │
│  USR-SP-02  Series Description Block                        ◄── D3 confirm  │
│  3–5 sentences: construction · grade tier · use · vs sibling series        │
│                                                                             │
│  USR-SP-03  Breadcrumb                                                      │
│  Главная › … › Моечные ванны › ПРЕМИУМ-3                                    │
│                                                                             │
│  USR-SP-04  Adjacent Series Navigation (conditional)                        │
│  Siblings: [ПРЕМИУМ] [СТАНДАРТ] [П] [С] [Л] — compact links, NOT 18-chip row│
│                                                                             │
│  USR-SP-05  Scope Control Block                                             │
│  Sort │ discriminating filters only │ N товаров │ degenerate filters hidden │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  PRIMARY CONTENT — SELECTION WITHIN SERIES SCOPE                            │
│                                                                             │
│  USR-SP-06  Product Grid Block                              ◄◄◄ ATTENTION   │
│  ┌──────────────────────────────────────────────────────────────────────┐ │
│  │  ALL SKUs ∈ same series (ПРЕМИУМ-3)                                  │ │
│  │  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐                         │ │
│  │  │ Card   │ │ Card   │ │ Card   │ │ Card   │  ... 10 SKU            │ │
│  │  │ ВМЦ-…  │ │ ВМЦ-…  │ │ ВМЦ-…  │ │ ВМЦ-…  │                         │ │
│  │  │ L×W×H  │ │ L×W×H  │ │ L×W×H  │ │ L×W×H  │                         │ │
│  │  │ sects  │ │ sects  │ │ sects  │ │ sects  │                         │ │
│  │  │ price  │ │ price  │ │ price  │ │ price  │                         │ │
│  │  │ status │ │ status │ │ status │ │ status │                         │ │
│  │  │ [CTA]  │ │ [CTA]  │ │ [CTA]  │ │ [CTA]  │                         │ │
│  │  └────────┘ └────────┘ └────────┘ └────────┘                         │ │
│  │  Series label on card: optional (page-scoped — redundant)             │ │
│  └──────────────────────────────────────────────────────────────────────┘ │
│  PRIMARY ACTION: open PDP · add to cart · add to compare                    │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  AFTER GRID                                                                 │
│  USR-SP-07  Pagination (N/A for 10 SKU single page)                         │
│  USR-SP-08  Consultative CTA (conditional)                                  │
│             «Поможем подобрать» — when card differentiators insufficient    │
└─────────────────────────────────────────────────────────────────────────────┘

SUPPRESSED ON SERIES PAGE:
  ✗ Parent 18-chip row          ✗ Certificates slider    ✗ Dealer form
  ✗ Degenerate filters            ✗ Misaligned cross-family cards
  ✗ In-page sibling SKU matrix (V-09)
```

### Mobile schematic

```text
┌──────────────────────────┐
│  [ HEADER ]              │
├──────────────────────────┤
│                          │
│  P1 — CRITICAL           │
│  ┌────────────────────┐  │
│  │ USR-SP-02 opening  │  │  series meaning — first line
│  │ line               │  │
│  └────────────────────┘  │
│  ┌────────────────────┐  │
│  │ USR-SP-06 Grid     │  │  ◄◄◄ PRIMARY
│  │ Card Tier 1:       │  │
│  │ price·status·      │  │
│  │ article·CTA        │  │
│  │ (all ∈ ПРЕМИУМ-3)  │  │
│  └────────────────────┘  │
│                          │
│  P2 — HIGH               │
│  USR-SP-05 filters+count │
│  Card: L×W×H·sections    │
│  Labeled compare         │
│                          │
│  P3 — MEDIUM             │
│  Full USR-SP-02 desc     │
│  Card Tier 2 fields      │
│  USR-SP-08 Consult CTA   │
│  (if triggered)          │
│                          │
│  P4 — LOWER              │
│  USR-SP-04 Adjacent      │
│  series links            │
│  USR-SP-07 Pagination    │
│  Sort                    │
│                          │
│  P5 — SUPPRESSED         │
│  ✗ Commercial wallpaper  │
│                          │
├──────────────────────────┤
│  [ FOOTER ]              │
└──────────────────────────┘
```

### Series = Selection Scope (visual proof)

```text
┌─────────────────────────────────────────┐
│  SERIES PAGE BOUNDARY: ПРЕМИУМ-3        │
│  ┌───────────────────────────────────┐│
│  │  Filter scope: WITHIN series only ││
│  │  Grid scope:   ALL SKUs ∈ series  ││
│  │  Card scope:   same series implied││
│  │  Exit paths:   PDP · sibling ser. ││
│  └───────────────────────────────────┘│
│  NEVER: expand grid to cross-family     │
│  NEVER: reintroduce parent 18-chip row  │
└─────────────────────────────────────────┘
```

---

## Listing Card Prototype

**Object:** Listing Card — discrimination and routing unit (not mini-PDP)  
**Primary card decision:** Open PDP / add to compare / skip

### Information layout — single card

```text
┌──────────────────────────────────────────────────────────────┐
│  LISTING CARD — information hierarchy (no visual styling)    │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ TIER 1 — MANDATORY (always visible)          ◄── scan  │  │
│  │                                                        │  │
│  │  USR-LC-01  Article code          e.g. ВМЦ-П3-2/500   │  │
│  │  USR-LC-02  Short product name                         │  │
│  │  USR-LC-03  Availability (SINGLE ZONE)                 │  │
│  │             «В наличии · N шт.» OR «Под заказ»         │  │
│  │  USR-LC-04  Price                                      │  │
│  │  USR-LC-05  Primary CTA              [ В корзину ]     │  │
│  │  USR-LC-06  PDP link (card surface or explicit)        │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ TIER 2 — STRONGLY RECOMMENDED              ◄── fit     │  │
│  │                                                        │  │
│  │  USR-LC-07  Series label (*mandatory on parent grid*) │  │
│  │  USR-LC-08  L × W × H (structured)                     │  │
│  │  USR-LC-09  Section count                              │  │
│  │  USR-LC-10  Lead time (if под заказ)                  │  │
│  │  USR-LC-11  Thumbnail (meaningful alt)                 │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ TIER 3 — OPTIONAL                          ◄── context │  │
│  │                                                        │  │
│  │  USR-LC-12  Material    USR-LC-13  Variant (Н)         │  │
│  │  USR-LC-14  Discount    USR-LC-15  Delivery (if data) │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ TIER 4 — ACTIONS (secondary to information)            │  │
│  │                                                        │  │
│  │  USR-LC-16  Compare (labeled)                          │  │
│  │  USR-LC-17  Wishlist                                   │  │
│  │  USR-LC-18  «Подробнее»                                │  │
│  └────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────┘

FORBIDDEN ON CARD (never render):
  ✗ Duplicate availability zone    ✗ Full spec table (20+ rows)
  ✗ Placeholder content            ✗ Empty delivery field
  ✗ Marketing prose                ✗ Nomenclature legend
  ✗ Misleading status styling
```

### 3-second understanding model

```text
SECOND 0–1: IDENTITY
  ┌─────────────────────────────────────┐
  │ Article + short name                │  «Which SKU is this?»
  └─────────────────────────────────────┘

SECOND 1–2: COMMERCIAL VIABILITY
  ┌─────────────────────────────────────┐
  │ Status (single) + price             │  «Can I get it? At what cost?»
  └─────────────────────────────────────┘

SECOND 2–3: FIT + ROUTING
  ┌─────────────────────────────────────┐
  │ Series label (parent) · L×W×H ·     │  «Right series? Right size?»
  │ sections · [CTA] · compare          │  «Open · compare · skip?»
  └─────────────────────────────────────┘

CARD INTERACTION:
  MATCH     → open PDP (USR-LC-06) OR compare (USR-LC-16)
  UNCERTAIN → open PDP
  REJECT    → skip to next card
  NO MATCH  → adjust filters OR consult
```

### Card in grid context (parent vs series)

```text
PARENT CATEGORY GRID (mixed scope):
  ┌────────┐  series label REQUIRED (USR-LC-07)
  │ ПРЕМ-3 │  — buyer sees series without decoding title
  └────────┘

SERIES PAGE GRID (coherent scope):
  ┌────────┐  series label OPTIONAL — page scope implies series
  │ ВМЦ-…  │
  └────────┘
```

---

## PDP Prototype

**Page mode:** Single-SKU evaluation and conversion  
**Example SKU:** ВМЦ-П3-2/500 (моечные ванны, ПРЕМИУМ-3)  
**Primary action:** Add to cart OR B2B consultation

### Decision ladder (mapped to blocks)

```text
Correct Series?         → USR-PDP-02 Series Context
        ↓
Correct Model?          → USR-PDP-01 Identity + USR-PDP-04/05 Properties
        ↓
Correct Specs?          → USR-PDP-08 + USR-PDP-09 + USR-PDP-10
        ↓
Available?              → USR-PDP-03 Commercial Core
        ↓
Alternative?            → USR-PDP-12 In-Series Alternatives
        ↓
Convert                 → USR-PDP-03 CTA + USR-PDP-19 + USR-PDP-18
```

### Desktop schematic — seven evaluation zones

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  [ SITE HEADER ]                                                            │
└─────────────────────────────────────────────────────────────────────────────┘

ZONE 0 — GLOBAL
  USR-PDP-00  Breadcrumb:  Главная › … › ПРЕМИУМ-3 › [SKU name]

═══════════════════════════════════════════════════════════════════════════════
ZONE 1 — ORIENTATION (first screen — «where am I in the decision chain?»)
═══════════════════════════════════════════════════════════════════════════════

  ┌──────────────────────────────┬────────────────────────────────────────────┐
  │  USR-PDP-06  Media Block     │  USR-PDP-01  Product Identity             │
  │  Product image(s)             │  H1 · article · copy affordance           │
  │                               │                                            │
  │                               │  USR-PDP-02  Series Context  ◄── D3       │
  │                               │  Series name · link to series page         │
  │                               │  optional one-line tier descriptor         │
  └──────────────────────────────┴────────────────────────────────────────────┘

═══════════════════════════════════════════════════════════════════════════════
ZONE 2 — PRODUCT VALIDATION (first screen — «is this the right model?»)
═══════════════════════════════════════════════════════════════════════════════

  USR-PDP-04  Selected Properties Block
  L × W × H × mass

  USR-PDP-05  Category-Critical Properties Block
  Sections · bowl dims · material · construction type
  (family-specific — моечные ванны v1 minimum)

  USR-PDP-07  Secondary Actions
  Compare (labeled) · Favorites

═══════════════════════════════════════════════════════════════════════════════
ZONE 3 — COMMERCIAL VALIDATION (first screen — «can I buy it?»)
═══════════════════════════════════════════════════════════════════════════════

  USR-PDP-03  Commercial Core Block                              ◄◄◄ ATTENTION
  Status · qty · price · qty selector · PRIMARY CTA [ В корзину ]

═══════════════════════════════════════════════════════════════════════════════
ZONE 4 — SPECIFICATION SUMMARY (default-visible — scroll or inline)
═══════════════════════════════════════════════════════════════════════════════

  USR-PDP-08  Description Block
  Назначение · комплектация · ключевые отличия

  USR-PDP-09  Minimum Spec Summary Block
  5–8 rows: category-critical + logistics — DEFAULT VISIBLE

  USR-PDP-10  Full Specifications Block
  20+ rows — tab or expand

  USR-PDP-11  Documents Entry Block

═══════════════════════════════════════════════════════════════════════════════
ZONE 5 — FULL REFERENCE DATA (deep — not required for initial fit)
═══════════════════════════════════════════════════════════════════════════════

  USR-PDP-15  Full Documentation Block
  USR-PDP-16  Extended Description Block

═══════════════════════════════════════════════════════════════════════════════
ZONE 6 — ALTERNATIVES (in-series only — replaces misaligned «Похожие»)
═══════════════════════════════════════════════════════════════════════════════

  USR-PDP-12  In-Series Alternatives Block          ◄── same series SKUs only
  USR-PDP-13  Compare Feedback Block
  USR-PDP-14  Return-to-Series Block (with filter state)

  USR-PDP-17  Cross-Family Related (Zone 5 related — deprioritized, labeled)
              «Сопутствующие» — accessories only; NOT before USR-PDP-12

═══════════════════════════════════════════════════════════════════════════════
ZONE 7 — COMMERCIAL SUPPORT (at conversion — elevated consult)
═══════════════════════════════════════════════════════════════════════════════

  USR-PDP-18  Commercial Detail Block
  Lead time · delivery summary · dealer path

  USR-PDP-19  Consultative CTA Block                 ◄── visible before all tabs
  «Задать вопрос» / «Поможем подобрать»

  USR-PDP-20  Trust Micro-Signals (compact)
  USR-PDP-21  Legal Disclaimer

SUPPRESSED ON PDP:
  ✗ Misaligned «Похожие» (cross-family default)
  ✗ Full dealer form inline    ✗ Certificates slider
  ✗ Duplicate advantages       ✗ Sibling SKU matrix (V-09)
  ✗ Placeholder mini-desc      ✗ Demo brand logo
```

### Mobile schematic

```text
┌──────────────────────────┐
│  [ HEADER ]              │
├──────────────────────────┤
│  USR-PDP-00 Breadcrumb   │
│                          │
│  P1 — CRITICAL           │
│  ┌────────────────────┐  │
│  │ USR-PDP-03         │  │  ◄◄◄ COMMERCIAL FIRST
│  │ Commercial Core    │  │  price·status·CTA
│  │ [ В корзину ]      │  │
│  └────────────────────┘  │
│  USR-PDP-02 Series ctx   │
│  USR-PDP-01 Article      │
│  USR-PDP-04/05 Key props │
│                          │
│  P2 — HIGH               │
│  USR-PDP-07 Compare/fav  │
│  (labeled)               │
│  USR-PDP-09 Min spec     │
│  summary                 │
│                          │
│  P3 — MEDIUM             │
│  USR-PDP-12 In-series    │
│  alternatives            │
│  USR-PDP-19 Consult CTA  │
│  USR-PDP-08 Description  │
│  opening                 │
│                          │
│  P4 — LOWER              │
│  USR-PDP-10 Full specs   │
│  USR-PDP-11/15 Docs      │
│  USR-PDP-06 Media gallery│
│                          │
│  P5 — SUPPRESSED/COLLAPSE│
│  USR-PDP-16 Extended desc│
│  USR-PDP-17 Cross-family │
│  ✗ Repeated certs/dealer │
│                          │
├──────────────────────────┤
│  [ FOOTER ]              │
└──────────────────────────┘
```

### First-screen attention map (desktop)

```text
┌────────────────────────────────────────────────────────────┐
│  HIGHEST ATTENTION                                         │
│  ┌──────────────────────────────────────────────────────┐│
│  │ USR-PDP-03 Commercial Core — price · status · CTA    ││
│  └──────────────────────────────────────────────────────┘│
│  ┌─────────────────────┐  ┌──────────────────────────────┐│
│  │ USR-PDP-02 Series   │  │ USR-PDP-01 Identity          ││
│  │ USR-PDP-04/05 Props │  │ USR-PDP-06 Media             ││
│  └─────────────────────┘  └──────────────────────────────┘│
│  MEDIUM — visible without deep scroll                      │
│  USR-PDP-09 Min spec · USR-PDP-19 Consult CTA              │
│  LOWER — requires scroll                                   │
│  USR-PDP-10 Full specs · USR-PDP-12 Alternatives · Zone 7  │
└────────────────────────────────────────────────────────────┘
```

---

## Mobile Priority Maps

Visual priority order for every page type. P1 = must reach without excessive scroll.

### G1 — Catalog Root

```text
P1 ████████████████████  USR-CR-03 Type Navigation (9 entries)
P2 ████████████          USR-CR-01 Orientation · USR-CR-04 Procurement
P3 ████████              USR-CR-05 Trust Summary (compact)
P4 ████                  USR-CR-02 Breadcrumb
P5 ██                    USR-CR-06 SEO Reference
```

### G2 — Mid-Level Category

```text
P1 ████████████████████  USR-ML-03 Subfamily Navigation
P2 ████████████          USR-ML-01 Orientation · USR-ML-02 Breadcrumb
P3 ████████              USR-ML-04 Listing cards (Tier 1–2) — if present
P4 ████                  Sort / filter — if listing present
P5 ✗ SUPPRESSED          Below-listing commercial blocks
```

### G3 — Parent Category (Моечные ванны)

```text
P1 ████████████████████  USR-PC-03 Series chips
                         USR-PC-07 Card Tier 1 (price·status·article·CTA)
P2 ████████████          USR-PC-06 Active filters · sort · scope+count
                         USR-PC-01 Orientation
P3 ████████              USR-PC-05 Filter overlay · card Tier 2
                         series label · dimensions · compare
P4 ████                  USR-PC-09 Series guide · USR-PC-08 Pagination
P5 ✗ SUPPRESSED          SEO · certificates · dealer form
```

### G4 — Series Page (ПРЕМИУМ-3)

```text
P1 ████████████████████  USR-SP-06 Grid Tier 1 · USR-SP-02 opening line
P2 ████████████          USR-SP-05 Filters+count · card L×W×H·sections
                         labeled compare
P3 ████████              Full USR-SP-02 · card Tier 2 · USR-SP-08 Consult
P4 ████                  USR-SP-04 Adjacent series · pagination · sort
P5 ✗ SUPPRESSED          Commercial wallpaper blocks
```

### G5 — Listing Card

```text
P1 ████████████████████  Price · Availability · Article · Primary CTA
P2 ████████████          Series label · L×W×H · Section count
P3 ████████              Lead time · Image · «Подробнее»
P4 ████                  Material · Variant · Discount · Delivery
P5 —                     (nothing below P4 on card)
```

### G6 — PDP

```text
P1 ████████████████████  USR-PDP-03 Commercial · USR-PDP-02 Series
                         USR-PDP-04/05 Props · USR-PDP-01 Article
P2 ████████████          USR-PDP-07 Compare/fav · USR-PDP-09 Min spec
P3 ████████              USR-PDP-12 In-series alts · USR-PDP-19 Consult
                         USR-PDP-08 Description opening
P4 ████                  USR-PDP-10 Full specs · Docs · Media gallery
P5 ✗ COLLAPSE            Extended desc · Cross-family · repeated commercial
```

### Cross-page mobile rule

```text
Filter overlay (mobile): applied constraints MUST appear in results zone
  → USR-PC-06 = P2 on parent category — NOT hidden inside closed overlay
Compare affordances: labeled text required — NOT icon-only silent
```

---

## Prototype Validation

Validation of `BZPM-VISUAL-UX-PROTOTYPE-v1` against approved artifacts. No new findings introduced.

### Against Architecture (P-01–P-10)

| Principle | Prototype expression | Status |
|-----------|---------------------|--------|
| P-01 Product-database first | Root = 9 cards; parent retains series chips; grid secondary | **SATISFIED** |
| P-02 One primary selection surface | Each schematic marks one ◄◄◄ attention zone | **SATISFIED** |
| P-03 Series scope = selection scope | Series prototype: grid boundary box; filters within series only | **SATISFIED** |
| P-04 Information at decision point | Card tiers map to D3–D7; PDP zones map to decision ladder | **SATISFIED** |
| P-05 Visible packaging ≠ more data | USR-PDP-09 default-visible; no new data invented | **SATISFIED** |
| P-06 No wasteful duplication | Single availability zone on card; suppressed blocks marked | **SATISFIED** |
| P-07 Commercial contextual | Trust at root once; consult at choice points; deep repeats suppressed | **SATISFIED** |
| P-08 Trapeza informs, not copies | OEM series chips retained; no Trapeza layout copied | **SATISFIED** |
| P-09 Mobile decision-equivalent | Section G priority maps per page type | **SATISFIED** |
| P-10 Status honesty | OQ-06 fork shown; no assumed answers | **SATISFIED** |

### Against Blueprint (block contracts)

| Surface | UX Structure blocks | Prototype coverage | Status |
|---------|--------------------|--------------------|--------|
| Catalog Root | USR-CR-01–06 | Desktop + Mobile schematics | **SATISFIED** |
| Mid-level | USR-ML-01–05 | Desktop + Mobile schematics | **SATISFIED** |
| Parent | USR-PC-01–10 | Three-layer model + schematics | **SATISFIED** |
| Series | USR-SP-01–08 | Scope boundary + schematics | **SATISFIED** |
| Listing Card | USR-LC-01–18 | Tier layout + 3-second model | **SATISFIED** |
| PDP | USR-PDP-00–21 | Seven zones + decision ladder | **SATISFIED** |
| Commercial tiers | Blueprint Section F | Suppression markers on all pages | **SATISFIED** |

### Against UX Structure (UX-01–UX-27)

| Rule | Prototype check | Status |
|------|----------------|--------|
| UX-01 One decision per page | Each schematic labels primary decision (D1–D8) | **SATISFIED** |
| UX-03 Navigation ranks above selection | Parent: USR-PC-03 before USR-PC-07 | **SATISFIED** |
| UX-04 One primary taxonomy surface | Mid-level: no parallel filter row shown | **SATISFIED** |
| UX-07 Root/mid = navigation only | No SKU grid as primary on either | **SATISFIED** |
| UX-08 Parent series-first | Layer 1 Navigation before Layer 3 Result | **SATISFIED** |
| UX-09 Series grid primary | USR-SP-06 marked ◄◄◄ on series page | **SATISFIED** |
| UX-10 PDP single-SKU | No matrix; USR-PDP-12 replaces «Похожие» | **SATISFIED** |
| UX-13 Single availability zone | Card Tier 1 shows one status zone | **SATISFIED** |
| UX-15 In-series alternatives primary | Zone 6 before cross-family USR-PDP-17 | **SATISFIED** |
| UX-16 Global trust once | USR-CR-05 at root; suppressed on deep pages | **SATISFIED** |
| UX-17 Consultative CTA elevated | USR-PDP-19 in Zone 7 before tab depth | **SATISFIED** |
| UX-23 Mobile filter state visible | USR-PC-06 = P2 on mobile parent schematic | **SATISFIED** |

### Potential conflicts

| ID | Conflict | Prototype handling | Resolution owner |
|----|----------|-------------------|------------------|
| **C-01** | OQ-06: parent grid default show vs hide until series selected | Prototype shows grid with scope labeling (blueprint default); fork noted on parent schematic | Operator |
| **C-02** | Desktop vs mobile block order on PDP | Mobile elevates USR-PDP-03 above media — decision-equivalent, not DOM parity (P-09) | Design phase |
| **C-03** | USR-ML-04 optional listing — trigger undefined | Shown as optional secondary layer; not primary | Content/operator |
| **C-04** | OQ-01: USR-PDP-05 incomplete for non-sink families | Prototype uses моечные ванны example only; other families marked OQ-01 | W1E deferred |
| **C-05** | Parent mobile P1 combines series chips AND card Tier 1 | Both P1 per UX Structure G3 — first-screen fit unvalidated (OQ-09) | Design + device test |

### Satisfied rules summary

| Category | Count |
|----------|-------|
| Architecture principles satisfied | 10 / 10 |
| Blueprint block contracts mapped | 6 / 6 surfaces |
| UX Structure cross-page rules satisfied | 12 / 12 checked |
| Suppressed zones marked on all schematics | Yes |

---

## Open Questions

Carried from approved artifacts — prototype does not assume answers.

| ID | Question | Prototype impact |
|----|----------|------------------|
| OQ-01 | Category-critical hero properties for non-sink families? | PDP Zone 2 incomplete for столы, стеллажи, тепловое |
| OQ-02 | Backend rule for «Похожие товары»? | USR-PDP-12 may need CMS relation change |
| OQ-03 | `p-card__delivery` empty by design or missing data? | USR-LC-15 conditional on card layout |
| OQ-04 | Populated compare table attributes? | Compare Tier 4 action — secondary surface |
| OQ-05 | Filter AJAX — result counts and active chips? | USR-PC-06 visual state — IMPL-DEPENDENT |
| OQ-06 | Hide parent flat grid until series selected? | Parent Layer 3 visibility fork — **shown with labeling in prototype** |
| OQ-07 | `/custom-equipment` role in task path? | Conditional CTA trigger only |
| OQ-08 | PRJ-0009 stack constraints? | Engineering handoff — out of prototype scope |
| OQ-09 | Mobile P1 fit on common devices? | All mobile priority maps — **IMPL-DEPENDENT** |
| OQ-10 | Polygon WIP — findings already addressed? | Avoid duplicate design effort |
| OQ-11 | Sort options — популярность / наличие? | USR-PC-04, USR-SP-05 scope control |
| OQ-12 | Series description copy ownership? | USR-SP-02, USR-PC-09 — content ops |

---

## Document lineage

| Input | Role |
|-------|------|
| [BZPM-UX-STRUCTURE-v1.md](BZPM-UX-STRUCTURE-v1.md) | Direct source — block sequence translated to schematics |
| [BZPM-BLUEPRINT-v1.md](BZPM-BLUEPRINT-v1.md) | Block contracts and suppression matrix |
| [BZPM-REDESIGN-ARCHITECTURE-v1.md](BZPM-REDESIGN-ARCHITECTURE-v1.md) | Architectural invariants and three-layer model |

**Next phase:** High-fidelity wireframes and visual design (designer handoff from this document).

---

*BZPM-VISUAL-UX-PROTOTYPE-v1 — low-fidelity visual UX only. No UI kit. No branding. No implementation. Designer begins wireframes; engineer understands page composition before visual design.*
