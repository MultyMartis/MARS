# REPORT — SITE-001 WF-V3 Catalog Blueprint v1

**Type:** Catalog information architecture blueprint — documentation only  
**Date:** 2026-06-14  
**Site:** SITE-001 — Автосалон СИБКАР  
**Program:** Website Factory · WF-V3  
**Mode:** Planning / blueprint — **no design, no CSS, no implementation**

**Explicit exclusions (honored):** No HTML · No SCSS · No JS · No OpenCart · No OCPilot · No TEST · No FTP · No visual styling · No prototype code · No workspace · No commit implied

**Authority chain:**

- [SITE-001-WFV3-PDP-DESIGN-AUTHORITY-FREEZE-v1.md](../governance/SITE-001-WFV3-PDP-DESIGN-AUTHORITY-FREEZE-v1.md) — **primary**
- [SITE-001-WFV3-HOMEPAGE-BLUEPRINT-v1.md](SITE-001-WFV3-HOMEPAGE-BLUEPRINT-v1.md)
- [SITE-001-WFV3-CATALOG-DISCOVERY-v1.md](SITE-001-WFV3-CATALOG-DISCOVERY-v1.md)
- [SITE-001-WFV3-LAYOUT-CONFORMANCE-PASS-v1.md](SITE-001-WFV3-LAYOUT-CONFORMANCE-PASS-v1.md)

**Principle:** Homepage · Catalog · PDP = **three screens of the same product**. Shared header, footer, tokens, trust tone, inventory card grammar, CTA discipline.

**Route:** `/cars/` (авто с пробегом) — primary catalog v0.1.

---

# SECTION 1 — Zone Blueprint (C0–C11)

Каждый блок — **зона планирования**, не визуальный макет.

---

## C0 — Header stack

**Содержание:** Dark topbar (город, часы, телефон) + white main bar (logo, centered nav, red pill «Перезвоните мне»).

**Rationale:** P-03 one dealer shell. **Identical partial** to Homepage H0 and PDP Z0. Catalog is not a «section without nav» — visitor always knows they are in СИБКАР.

**Homepage equivalent:** H0 — **shared partial**, no divergence.  
**PDP equivalent:** Z0 — **shared partial**, no divergence.

---

## C1 — USP benefit row

**Содержание:** Light full-width band; ~5 icon+text items (напр. «Реальные авто на складе», «160-point check», «Кредит от 6,9%», trade-in hook, рассрочка).

**Rationale:** Same layer as Homepage H1 and PDP Z1. Supports trust on a long scroll page without marquee panic (P-04, P-10). Thin band under nav — does not compete with filter + grid.

**Homepage equivalent:** H1 — **same row grammar**, same copy family.  
**PDP equivalent:** Z1 — **same row grammar**.

---

## C2 — Breadcrumbs

**Содержание:** «Главная > Авто с пробегом» — optional third segment on brand routes: «> Audi».

**Rationale:** Orientation within inventory tree. Muted gray meta — same role as PDP Z2. Utility, not hero.

**PDP equivalent:** Z2 — **same breadcrumb grammar**; catalog is parent of PDP trail.

---

## C3 — Page header

**Содержание:**

- H1 — «Каталог автомобилей с пробегом» (Phase 1 label family)  
- Result count — «Найдено N автомобилей» (static in v0.1)  
- Sort control — dropdown or segmented: по умолчанию · цена · год · пробег  

**Rationale:** Declares page job immediately after breadcrumbs. Result count = **inventory scale trust** (discovery §8.3). Sort in header — not buried in filter panel.

**Homepage equivalent:** H4 section title — **semantic parent** of featured heading «Авто с пробегом в наличии».  
**PDP equivalent:** Z3 title row — catalog H1 is **category anchor**; PDP H1 is **vehicle anchor**.

---

## C4 — Filter zone

**Содержание (conceptual — static in v0.1):**

**Tier 1 (always visible):**

- Марка · Модель · Цена от–до · Год от–до  
- Submit / apply — «Показать N автомобилей»  

**Tier 2 (expand «Расширенный поиск»):**

- Пробег до · КПП · Кузов · Топливо · Привод · Объём  

**Layout (desktop):** Left sidebar ~25–30% width, sticky optional **deferred** (static header P-11 — sticky filter is not header sticky).

**Rationale:** P-05 search first-class — catalog is where Homepage H3 search **lands and expands**. Same Tier 1 fields as homepage search for continuity. Sidebar keeps filters visible while scanning C6 grid.

**Homepage equivalent:** H3 Search — **upstream**; query params pre-fill C4.  
**PDP equivalent:** — (no filters on PDP).

**Anti-pattern:** Full-width OC `search_wrap` form above title · filter-only first screen with zero visible cards.

---

## C5 — Active filters bar

**Содержание:** Horizontal chip row — each applied criterion removable; link «Сбросить все».

**Rationale:** Transparency trust — visitor sees what shapes results. Appears when ≥1 filter active; hidden on unfiltered `/cars/` entry from H4 «Смотреть все».

**Homepage equivalent:** — (homepage search has no chip bar).  
**PDP equivalent:** —.

---

## C6 — Results grid

**Содержание:** Grid of `wf-v3-inventory-card` (catalog variant) — see §2.

**Rationale:** **Core catalog moment** — multi-vehicle Class B stage. P-01 car first at grid level: photo + price visible in scan path. Flat cards on cool neutral canvas (P-07, P-12).

**Grid (WF-LAYOUT L3 variant):**

| Viewport | Columns |
|----------|---------|
| Desktop ≥ 1280px | 3 |
| Tablet ≤ 1024px | 2 |
| Mobile ≤ 767px | 1 |

**Homepage equivalent:** H4 Featured — **same card core**, catalog adds secondary fields (§2).  
**PDP equivalent:** Z9 related links mindset — **multi-car** continuation; Z4 is single-car destination.

---

## C7 — Pagination

**Содержание:** Page numbers + prev/next — «Страница 1 из M»; static in v0.1.

**Rationale:** Assortment scale — large inventory requires explicit navigation. Support tier — not first-screen hero.

**Anti-pattern:** Infinite scroll without count — hides assortment transparency.

---

## C8 — Trust layer

**Содержание:** Horizontal proof strip — **catalog-scoped**:

- ~4–5 items: inspection program · VIN/report policy at dealer level · no hidden fees · physical address · «реальные авто на складе»  

**Rationale:** P-10 trust before promotion. Same **visual grammar** as Homepage H5 and PDP Z5 — flat tiles on `surface-secondary`. Scope = **dealer + inventory policy**, not vehicle-specific proof.

**Homepage equivalent:** H5 — **same strip grammar**, different placement (homepage above advantages).  
**PDP equivalent:** Z5 — **same grammar**; PDP adds vehicle-specific items.

**Anti-pattern:** TEST reviews slider (`sw-app`) as catalog trust substitute.

---

## C9 — Financing teaser (optional v0.1)

**Содержание:** Lightweight band — heading, rate hook, outlined CTA «Условия кредита». **No** full calculator.

**Rationale:** Secondary conversion for visitors browsing without single-car focus. Same family as Homepage H7 — shorter than homepage version acceptable.

**Homepage equivalent:** H7 — **teaser parity**.  
**PDP equivalent:** Z7 — full calculator remains PDP-only.

**Note:** May **omit** in catalog v0.1 if page length sufficient — operator HITL. Not required for 3-second test.

---

## C10 — Footer

**Содержание:** Dark inverse — contact, catalog columns (новые / пробег), legal, red callback repeat.

**Rationale:** Brand continuity terminus. Frozen PDP Z10 / Homepage H10 — **shared partial**.

**PDP equivalent:** Z10 — **identical shell**.

---

## C11 — (Reserved)

**Slot:** Future «Related categories» or «Спецпредложения» text links — **deferred**. PDP Z9 pattern. Not in catalog v0.1 minimum.

---

# SECTION 2 — Inventory Card Specification (Catalog Variant)

## Component identity

```text
Base:  wf-v3-inventory-card (from homepage H4)
Scope: catalog extends — does not fork
```

## Anatomy (top → bottom)

| # | Element | Priority | Notes |
|---|---------|----------|-------|
| 1 | **Photo link** | P0 | Single image · 16:10 · studio surface · **no swiper** |
| 2 | **Status badge** | P2 | Optional «В наличии» — top corner, one max |
| 3 | **Title** | P0 | Brand + model + year — links to PDP |
| 4 | **Price** | P0 | Brand red · bold · main figure |
| 5 | **Old price** | P2 | Strikethrough if present |
| 6 | **Meta row** | P0 | Year · mileage chips |
| 7 | **Spec chips** | P2 | Max 2: e.g. «Робот» · «1.4 л» |
| 8 | **Monthly hint** | P2 | «от 12 208 ₽/мес» — muted small |
| 9 | **CTA** | P1 | Text «Подробнее» — not solid red |

## Hover / interaction

- Card border darkens subtly (homepage card pattern)  
- Whole card clickable **or** photo + title + CTA — prototype choice  
- **No** secondary buttons on card face

---

# SECTION 3 — Filters Blueprint (Conceptual)

## Field matrix

| Field | Tier | Homepage H3 | Catalog C4 | PDP |
|-------|------|-------------|------------|-----|
| Марка | 1 | ✓ | ✓ | — |
| Модель | 1 | ✓ | ✓ | — |
| Цена от–до | 1 | ✓ | ✓ | — |
| Год от–до | 1 | partial (year) | ✓ | spec |
| Пробег до | 2 | — | ✓ | spec |
| КПП | 2 | — | ✓ | spec |
| Кузов | 2 | — | ✓ | spec |
| Топливо | 2 | — | ✓ | spec |
| Привод | 2 | — | ✓ | spec |
| Объём | 2 | — | ✓ | spec |
| Sort | header | — | C3 | — |

## UX rules

1. Tier 1 visible without expand on desktop.  
2. «Расширенный поиск» toggles Tier 2 — same mental model as TEST, **new geometry**.  
3. Apply action updates C5 chips + C6 grid + C3 count — static mock may show prefilled state only.  
4. Empty state (0 results): C6 shows message + «Сбросить фильтры» — not required in v0.1 prototype but blueprint slot reserved.

---

# SECTION 4 — Homepage → Catalog → PDP Chain

```text
┌─────────────────────────────────────────────────────────────────┐
│  HOMEPAGE                                                        │
│  H0 Header ──────────────────────────────── shared ──► C0 / Z0  │
│  H1 USP    ──────────────────────────────── shared ──► C1 / Z1  │
│  H2 Hero + H3 Search ──submit──► C4 Filters (pre-filled)        │
│  H4 Featured cards ──«Смотреть все»──► C6 Grid (unfiltered)    │
│  H4 card click ──────────────────────► PDP Z3–Z4                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  CATALOG /cars/                                                  │
│  C2 Breadcrumbs ◄── PDP Z2 parent trail                         │
│  C3 Header (H1 + count + sort)                                  │
│  C4 Filters + C5 Chips                                          │
│  C6 Grid (wf-v3-inventory-card catalog variant)                 │
│  C6 card click ──────────────────────► PDP Z3–Z4                 │
│  C8 Trust (dealer scope)                                        │
│  C10 Footer ─────────────────────────────── shared ──► Z10     │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  PDP /cars/{brand}/{product}                                     │
│  Z2 Breadcrumbs ◄── catalog parent                              │
│  Z3 Title + badges ◄── card title expanded                      │
│  Z4 Gallery + offer ◄── card price + specs expanded             │
│  Z5 Vehicle trust ◄── escalated from C8 dealer trust            │
│  Z6–Z8 Equipment · credit · banks                               │
│  Z10 Footer                                                      │
└─────────────────────────────────────────────────────────────────┘
```

---

# SECTION 5 — Catalog ↔ PDP Field Alignment Table

| Catalog C6 | PDP zone | Alignment rule |
|------------|----------|----------------|
| Photo | Z4 gallery | Same asset · same studio stage |
| Title | Z3 H1 | Catalog short → PDP full (adds КПП · mileage in title) |
| Price | Z4 offer | Exact numeric match |
| Old price | Z4 strikethrough | Exact match if shown |
| Year chip | Z4 spec «Год» | Same |
| Mileage chip | Z3/Z4 «Пробег» | Same |
| Spec chips | Z4 spec grid | Subset — no conflicts |
| Monthly hint | Z4 «от X ₽/мес» | Same or omit on catalog |
| «В наличии» | Z3 badge | Consistent |
| «Подробнее» href | PDP URL | Same product slug |

---

# SECTION 6 — Trust Model (Catalog-Specific)

## C8 content proposal

| # | Proof item | Scope |
|---|------------|-------|
| 1 | 160-point inspection program | Dealer |
| 2 | VIN / history check policy | Dealer |
| 3 | No hidden fees | Dealer |
| 4 | Physical address Новосибирск | Dealer |
| 5 | N cars in stock (if verified) | Inventory |

## Placement

- **After** C6 grid + C7 pagination — visitor scanned inventory first (inventory proof), then dealer proof.  
- **Before** C9 financing teaser (if present) and C10 footer.

## Exclusions from catalog

| Item | Where it belongs |
|------|------------------|
| Vehicle VIN button | PDP Z4 |
| «12 человек смотрят» | PDP Z3 |
| Reviews widget | Not WF-V3 catalog — optional site-wide page elsewhere |
| Bank logo carousel | PDP Z8 / footer — not catalog body |

---

# SECTION 7 — CTA Model

## Tier definitions (aligned with PDP + Homepage freeze)

| Tier | Treatment | Catalog usage |
|------|-----------|-----------------|
| **Primary** | Solid red fill, white text, pill | **Header callback only** in C0 (frozen) |
| **Secondary** | White fill, red border | Filter apply (optional outlined) · financing teaser C9 |
| **Support** | Text links | Card «Подробнее» · pagination · sort · breadcrumb |

## Zone assignment

| Zone | Primary red | Secondary | Support |
|------|-------------|-----------|---------|
| **C0 Header** | «Перезвоните мне» (frozen) | — | Phone topbar |
| **C4 Filters** | — | Outlined «Показать авто» | Expand link |
| **C6 Cards** | — | — | «Подробнее» text only |
| **C9 Financing** | — | Outlined «Условия кредита» | — |
| **C10 Footer** | Red callback repeat | — | Legal links |

**P-09 rule:** No solid red on every inventory card. Price red accent ≠ CTA fill.

---

# SECTION 8 — Section Order Summary

```text
C0   Header stack
C1   USP benefit row
C2   Breadcrumbs
C3   Page header (H1 + count + sort)
C4   Filter zone          ┐
C5   Active filters bar   ├─ first-screen cluster (desktop):
C6   Results grid         ┘   filters + ≥2 card rows visible
C7   Pagination
C8   Trust layer
C9   Financing teaser     (optional v0.1)
C10  Footer
```

**Note:** C4+C5+C6 form **first-screen cluster** on desktop ≥ 1280px — sidebar + grid geometry deferred to prototype v0.1, not blueprint amendment.

---

# SECTION 9 — Blueprint ASCII Wireframe

Desktop ≥ 1280px. Hierarchy only — no pixels, no color.

```text
+------------------------------------------------------------------+
| TOPBAR:  [city] [hours]                    [phone]               |
+------------------------------------------------------------------+
| NAV:     [LOGO]    Nav Nav Nav Nav Nav Nav          [Callback]   |
+------------------------------------------------------------------+
| USP:     (icon) Real stock  (icon) 160-check  (icon) Credit ...  |
+------------------------------------------------------------------+
| CRUMB:   Glavnaya > Avto s probegom                               |
+------------------------------------------------------------------+
| HEADER:  Katalog avtomobiley s probegom     [Sort v]  Naydeno N  |
+------------------------------------------------------------------+
|                    |                                              |
|  FILTER SIDEBAR    |  RESULTS GRID                               |
|  +--------------+  |  +--------+  +--------+  +--------+          |
|  | Marka        |  |  | [photo]|  | [photo]|  | [photo]|          |
|  | Model        |  |  | Title  |  | Title  |  | Title  |          |
|  | Price ot-do  |  |  | PRICE  |  | PRICE  |  | PRICE  |          |
|  | God ot-do    |  |  | meta   |  | meta   |  | meta   |          |
|  | [Pokazat]    |  |  | detail>|  | detail>|  | detail>|          |
|  +--------------+  |  +--------+  +--------+  +--------+          |
|  [Rasshirennyj]    |  +--------+  +--------+  +--------+          |
|                    |  | card   |  | card   |  | card   |          |
|  CHIPS: [Audi x]   |  +--------+  +--------+  +--------+          |
|         [Sbr]      |                                              |
|                    |  [ < 1 2 3 ... > ]  pagination               |
+--------------------+----------------------------------------------+
| TRUST:   [proof1] [proof2] [proof3] [proof4] [proof5]             |
+------------------------------------------------------------------+
| CREDIT:  headline + rate hook          [Usloviya kredita]  (opt)  |
+------------------------------------------------------------------+
| FOOTER (dark): contact | catalog cols | legal | [callback red]    |
+------------------------------------------------------------------+
```

---

# SECTION 10 — Three-Screen Alignment Table

| Catalog zone | Role | Homepage zone | PDP zone | Shared language |
|--------------|------|---------------|----------|-----------------|
| **C0 Header** | Dealer identity | **H0** | **Z0** | Identical partial |
| **C1 USP row** | Compact strengths | **H1** | **Z1** | Same light band |
| **C2 Breadcrumbs** | Category orientation | — | **Z2** | Parent trail |
| **C3 Page header** | Category H1 + count | **H4** title | **Z3** | Title scale family |
| **C4 Filters** | Search expanded | **H3** | — | Same Tier 1 fields |
| **C5 Active chips** | Filter transparency | — | — | Catalog-only |
| **C6 Results grid** | Multi-car browse | **H4** cards | **Z4** (destination) | `wf-v3-inventory-card` |
| **C7 Pagination** | Assortment nav | — | — | Catalog-only |
| **C8 Trust** | Dealer + inventory proof | **H5** | **Z5** | Same strip grammar |
| **C9 Financing** | Credit teaser | **H7** | **Z7** | Teaser vs full |
| **C10 Footer** | Site map, legal | **H10** | **Z10** | Identical partial |

### Shared design language checklist

| Element | Shared rule |
|---------|-------------|
| Class prefix | `wf-v3-*` |
| Typography | Inter stack, PDP v0.2 roles |
| Surfaces | Max 2 depths per zone; no card-in-card |
| Brand red | Price accent + one primary action per **page zone** |
| Header/footer/USP | Shared partials from frozen prototypes |
| Trust tone | Proof labels, not CAPS promo |
| Photography | Vehicle-dominant, studio flat stage |
| Card component | `wf-v3-inventory-card` — homepage base, catalog extension |

---

# SECTION 11 — WF-LAYOUT Notes (Planning)

| Layout ID | Catalog application | Reference |
|-----------|---------------------|-----------|
| **L-sidebar + L-grid** | C4 sidebar + C6 grid | New — define at prototype: ~3fr / ~9fr or tokenized equivalent |
| **L3 grid** | C6 N=3 desktop | Homepage featured N=4 — narrower card, same minmax grammar |
| **L5 strip** | C8 trust row | PDP/homepage trust — `repeat(5, minmax(180px, 1fr))` collapse |

**Constraint:** No `%/%` tracks with gap overflow — per WF-LAYOUT CONFORMANCE PASS precedent.

---

# SECTION 12 — Success Criteria

## Operator-facing acceptance (future HITL)

| # | Criterion | Measurement |
|---|-----------|-------------|
| 1 | **3-second test** | Logo hidden · sentence = «витрина склада — можно сравнивать машины» |
| 2 | **Sibling test** | Side-by-side Catalog + Homepage + PDP — same brand, tokens, header/footer |
| 3 | **Card continuity** | H4 card → C6 card → PDP Z4 — price/title/mileage match on same fixture |
| 4 | **Inventory-first** | ≥2 rows of cards visible with filters on desktop — no reviews/banks above grid |
| 5 | **P-01..P-10** | Visibly satisfied on static prototype |
| 6 | **Composition delta vs TEST** | Obviously different from OC `catalog_item` + swiper |
| 7 | **No new design language** | Zero divergence from PDP + Homepage freeze |

## Failure signals

- Per-card image carousel returns  
- Filter-only first screen — zero cars visible  
- New card component instead of H4 extension  
- Multiple red CTAs per card  
- Reviews slider in catalog body  
- Catalog header/footer differ from Homepage/PDP  

---

# FINAL VERDICT

## **A — Ready For Catalog Prototype**

Blueprint C0–C11 is complete. Discovery verdict A stands. Next authorized step: **Catalog Prototype Write Charter** + workspace (extend homepage/PDP partials or dedicated catalog workspace).

**Not in scope of this document:** implementation · HTML · SCSS · OpenCart · TEST · JS filter logic.

---

## UNKNOWN / SECURITY

| Item | Status |
|------|--------|
| C4 sidebar exact width token | **OPEN** — prototype v0.1 |
| C9 include or omit in v0.1 | **OPEN** — operator HITL |
| `/cars/{brand}/` H1 variant | **OPEN** — «Audi с пробегом в наличии» vs generic H1 |
| Shared partial package across 3 workspaces | **OPEN** — integration hygiene |
| Mobile filter drawer | **SAFE UNKNOWN** — after desktop ACCEPT |

**SECURITY RISK:** None (documentation only).

---

*SITE-001 WF-V3 Catalog Blueprint v1 — planning only; no design; no implementation; no commit implied.*
