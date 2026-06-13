# Website Factory — WF Layout Discipline v1

**Версия:** v1  
**Дата:** 2026-06-13  
**Область:** `workspaces/website-factory-reference-v1/frontend-rules/`  
**Статус:** **MANDATORY** — Foundation-level inner-zone layout authority  
**Authority:** Default for all Website Factory projects (Gulp, OpenCart, WordPress, corporate, landing, catalog, PDP, homepage)

**Origin:** Promoted from SITE-001 (СИБКАР) WF-V3 Layout Authority Review — [reports/WF-LAYOUT-DISCIPLINE-PROMOTION-v1.md](../reports/WF-LAYOUT-DISCIPLINE-PROMOTION-v1.md)

**Complements (does not replace):** [WF-GRID-DISCIPLINE-v1.md](WF-GRID-DISCIPLINE-v1.md) — outer section/container contract

**Не является:** runtime validator, automated linter, CI gate, design token spec, responsive breakpoint registry.

**Связь:** [design-system/DESIGN-SYSTEM-RULES-v1.md](../design-system/DESIGN-SYSTEM-RULES-v1.md), [blueprints/BLUEPRINT-IMPLEMENTATION-RULES-v1.md](../blueprints/BLUEPRINT-IMPLEMENTATION-RULES-v1.md), [production-qa/PRODUCTION-QA-CHECKLIST-v1.md](../production-qa/PRODUCTION-QA-CHECKLIST-v1.md), [projects/mars-website-factory/frontend-production-rules-v0.md](../../../projects/mars-website-factory/frontend-production-rules-v0.md)

---

## Purpose

WF Layout Discipline defines **mandatory authority** for **inner-zone layout** — how space inside `.wf-container` (or project equivalent) is split between hero columns, card grids, trust strips, finance modules, and responsive collapse.

**WF-GRID-DISCIPLINE** governs **Container Layer** (section shell, max-width, padding, section ≠ container).  
**WF-LAYOUT-DISCIPLINE** governs **Layout Layer** (hero split, card grid, trust split, finance split, zone composition, collapse).

Without Layout Layer authority, agents independently produce incompatible split models (`65% / 35%`, `60% / 40%`, `1fr 42%`, `3fr 2fr`, `5fr 7fr`) — **layout drift between projects** despite correct container discipline.

---

## Rule index

| ID | Rule | Severity |
|----|------|----------|
| WF-LAYOUT-001 | Layer separation — Container vs Layout | CRITICAL |
| WF-LAYOUT-002 | Hero split authority | CRITICAL |
| WF-LAYOUT-003 | Card grid authority | HIGH |
| WF-LAYOUT-004 | Trust grid authority | HIGH |
| WF-LAYOUT-005 | Finance layout authority | HIGH |
| WF-LAYOUT-006 | Responsive collapse authority | HIGH |
| WF-LAYOUT-007 | Percentage split restriction | CRITICAL |
| WF-LAYOUT-008 | Authority review rule | CRITICAL |

---

## WF-LAYOUT-001 — Layer separation (Container Layer vs Layout Layer)

### Two-layer model

```text
Layer 1 — CONTAINER (WF-GRID-DISCIPLINE)
  Section shell → inner container wrapper
  Contract: max-width · padding-inline · one page = one grid contract

Layer 2 — LAYOUT (this document)
  Inside container only
  Zone splits: hero · cards · trust · finance · nested grids
```

### Container Layer owns

- Section vs container markup split (WF-GRID-001)
- Page-wide `--container-max`, `--container-pad`
- Header / hero / body / footer outer alignment
- Full-bleed backgrounds on section; content still in container

### Layout Layer owns

- Hero gallery/offer or content/visual split
- Fixed-count card grids (`N` columns at desktop)
- Trust / proof equal strips
- Finance head/panel splits (credit, banks)
- Nested grids inside zone columns (CTA row, specs row)
- Responsive stack / column reduction per zone

### Forbidden

- Using container tokens (`max-width`, `padding-inline`) to compensate for undefined inner-zone authority
- Mixing Container Layer fixes with ad-hoc Layout Layer percentages per block
- Treating WF-GRID PASS as sufficient for layout freeze — **Layout Layer requires separate authority**

### Failure symptoms

- Same container contract, different hero math on PDP vs homepage
- Percentage tracks + gap overflow inside container
- Card column count changes silently when container max changes
- Credit block uses `fr`, hero uses `%`, trust uses flex — no shared grammar

---

## WF-LAYOUT-002 — Hero split authority

Every hero with two primary columns **must** declare an authorized split model **before** production freeze.

### Required pattern (proportional gallery/commerce hero — e.g. PDP)

```scss
grid-template-columns: {gallery-fr}fr {offer-fr}fr;
gap: var(--hero-zone-gap); /* spacing token only */
```

Ratio intent lives in **named fr tokens**, not percentage pair:

```scss
$hero-gallery-fr: 13;
$hero-offer-fr: 7;
/* conceptual 65/35 — arithmetic via fr, not % */
```

### Required pattern (asymmetric content/visual hero — e.g. homepage)

```scss
grid-template-columns: minmax(0, 1fr) minmax({visual-min}px, {visual-max-fr}fr);
```

Homepage hero **must not** silently inherit PDP ratio — separate L2 charter with documented visual column floor.

### Required safeguards

| Safeguard | Detail |
|-----------|--------|
| **Offer/commerce min-width** | `minmax(360px, …)` or documented floor on narrow column — protects nested 3-col CTA/specs |
| **Gap from tokens** | Hero zone gap from spacing scale only — no ad-hoc gap breaking ratio math |
| **Cross-surface consistency** | Same page type family uses same hero **pattern class** (fr pair or minmax), not per-agent improvisation |

### Forbidden

- `65% 35%` (or any `%` `%` pair) when `gap > 0` — see WF-LAYOUT-007
- Hybrid `1fr 42%` without documented L2 exception
- Different hero split grammar on sibling surfaces (PDP `%`, homepage `fr/%`) without charter

### Zone type reference

| Type | Pattern | Example |
|------|---------|---------|
| **L1** | `{gallery-fr}fr {offer-fr}fr` | PDP hero 13fr 7fr |
| **L2** | `{content-fr}fr minmax({visual-min}px, {visual-max}fr)` | Homepage hero |

---

## WF-LAYOUT-003 — Card grid authority

Curated card rows (featured inventory, dealer advantages, equipment tiles) **must** use fixed-count equal columns at desktop.

### Required pattern

```scss
grid-template-columns: repeat(N, minmax(0, 1fr));
gap: var(--card-grid-gap);
```

| Rule | Detail |
|------|--------|
| **Documented N** | Column count `N` frozen per zone in blueprint / layout charter — not inferred from SCSS |
| **Card min-width floor** | Recommended `minmax(260px, 1fr)` threshold — below floor, reduce `N` or stack (WF-LAYOUT-006) |
| **Equal fr tracks** | No percentage column widths for card grids |

### Catalog listing exception

Full catalog listing may use `repeat(auto-fill, minmax(280px, 1fr))` — **separate charter** from homepage curated `N=4` (or project value). Not interchangeable.

### Forbidden

- Percentage-based card column widths
- `auto-fit` on homepage featured rows without catalog charter
- Undocumented column count drift between waves

---

## WF-LAYOUT-004 — Trust grid authority

Trust / proof strips (vehicle proof, dealer proof) **must** use equal-split grid grammar aligned with card grid family.

### Required pattern

```scss
grid-template-columns: repeat(N, minmax({item-min}px, 1fr));
gap: var(--trust-grid-gap);
```

| Rule | Detail |
|------|--------|
| **Documented N** | Item count frozen (e.g. N=5 PDP vehicle proof) |
| **Item min-width** | Floor per item (~180px recommended) — below floor, collapse per WF-LAYOUT-006 |
| **Grid family** | Prefer CSS Grid over flex `flex: 1` for equal strips — same gap semantics as WF-LAYOUT-003 |

### Zone type reference

| Type | Pattern |
|------|---------|
| **L5** | `repeat(N, minmax({item-min}px, 1fr))` |

Homepage and PDP trust rows share **L5 grammar**; content differs, pattern does not.

---

## WF-LAYOUT-005 — Finance layout authority

Two-zone finance modules (credit head + form panel, bank logo rows) **must** follow documented split types.

### Credit / head-panel module (L4)

```scss
grid-template-columns: {head-fr}fr {panel-fr}fr;
gap: var(--finance-zone-gap);
```

Reference ratio: `5fr 7fr` — stable across container widths; gap absorbed by fr math.

| Rule | Detail |
|------|--------|
| **fr ratio tokens** | Head and panel fr values named and frozen — not recomputed per page |
| **Panel divider** | Border/padding separation tokenized — panel `padding-left` must not silently shrink form area without review |
| **Nested form grid** | `repeat(2, 1fr)` inside panel inherits panel min-width — validate at narrowest parent |

### Bank logo row

`repeat(N, minmax(0, 1fr))` — same as WF-LAYOUT-003 with documented `N` (e.g. 8).

### Forbidden

- Finance hero-style `%` splits
- Different credit split on PDP vs homepage without documented exception

---

## WF-LAYOUT-006 — Responsive collapse authority

Every zone with desktop multi-column layout **must** document collapse behavior **before** production freeze.

### Required documentation (per zone)

| Field | Content |
|-------|---------|
| **Breakpoint** | Viewport or container width where layout changes |
| **Collapse mode** | Stack · reduce N · horizontal scroll (last resort, documented) |
| **Nested grid behavior** | CTA/specs/search fields when parent column stacks |
| **Min-width triggers** | When `N` reduces (card grid, trust strip) |

### Mandatory zones (minimum)

- Hero (L1 / L2)
- Trust strip (L5)
- Featured / card row (L3)
- Credit panel (L4)

### Gate rule

**Production freeze blocked** if responsive collapse for hero/trust/featured is **SAFE UNKNOWN**.

### Forbidden

- Desktop-only prototypes shipped to production without collapse charter
- Silent `flex-wrap` without documented breakpoint authority

---

## WF-LAYOUT-007 — Percentage split restriction

**Percentage split models are prohibited as default layout authority.**

### Forbidden (default)

```scss
grid-template-columns: 65% 35%;
grid-template-columns: 1fr 42%;  /* hybrid % track */
grid-template-columns: 60% 40%;
```

When `gap > 0`, percentage tracks sum to 100% of container **plus** gap — implicit overflow, floating absolute widths, layout drift under container/gap tweaks.

### Allowed authority models

| Model | Use |
|-------|-----|
| **fr ratio pair** | `{a}fr {b}fr` — gap absorbed correctly |
| **minmax floors** | `minmax(360px, …)` on commerce/offer columns |
| **Fixed-count equal grid** | `repeat(N, minmax(0, 1fr))` |
| **Documented exception** | Percentage only via `/* WF-LAYOUT-EXCEPTION: reason — approver — date */` |

### Exception marker (narrow)

```scss
/* WF-LAYOUT-EXCEPTION: reason — approver — date */
grid-template-columns: …;
```

Percentage exceptions require **operator charter** — not agent default, not silent SCSS.

### Conceptual ratio preservation

Design freeze may state **65/35 visual intent** — implementation **must** map to fr pair (e.g. 13fr 7fr), not `%` pair.

---

## WF-LAYOUT-008 — Authority review rule

**Any new layout model must pass layout authority review before freeze.**

### Triggers for review

| Trigger | Action |
|---------|--------|
| New zone split type (L1–L5 variant) | Document pattern + map to surfaces |
| New hero ratio on existing page type | HITL review — no silent token change |
| New card column count `N` | Blueprint + layout charter update |
| Cross-surface pattern change (PDP ↔ homepage) | Authority review — WF-LAYOUT-001 layer check |
| Percentage split request | WF-LAYOUT-007 exception path only |
| Responsive collapse undefined | Block freeze until WF-LAYOUT-006 complete |

### Review deliverable

Layout authority review report (project or Factory) with:

- Zone inventory table (model · gap · drift class)
- Container baseline PASS (WF-GRID)
- Layout layer PASS / NOT READY verdict
- Promotion or iteration list

### Gate rule

**No WF-V3 (or successor) full program freeze** while Layout Layer = NOT READY.

Reference audit: SITE-001 — [SITE-001-WFV3-LAYOUT-AUTHORITY-REVIEW-v1.md](../../../projects/ocpilot/sites/site-001/reports/SITE-001-WFV3-LAYOUT-AUTHORITY-REVIEW-v1.md)

---

## Zone type catalog (reference)

| Type | Name | Pattern | Example zones |
|------|------|---------|---------------|
| **L1** | Proportional split | `{a}fr {b}fr` | PDP hero |
| **L2** | Asymmetric hero | `{content-fr}fr minmax({visual-min}px, …)` | Homepage hero |
| **L3** | Fixed-count equal grid | `repeat(N, minmax(0, 1fr))` | Featured, banks, equipment |
| **L4** | Module head/panel | `{head-fr}fr {panel-fr}fr` | Credit block |
| **L5** | Equal proof strip | `repeat(N, minmax({item-min}px, 1fr))` | Trust row |

---

## QA layout check (operator)

Frontend QA **must** verify inner-zone authority **after** WF-GRID-005 PASS.

| Check | Pass criterion |
|-------|----------------|
| **Hero split model** | Authorized L1 or L2 — no default `%` tracks |
| **Card grids** | Documented `N`; no percentage columns |
| **Trust strip** | L5 or documented equal grid — not ad-hoc flex |
| **Finance modules** | L4 fr ratio or documented bank `N` |
| **Cross-surface** | Sibling heroes use consistent pattern family |
| **Collapse** | Documented or explicitly SAFE UNKNOWN with freeze block |

### REPORT line (mandatory for Frontend QA)

```text
WF LAYOUT DISCIPLINE — PASS | FAIL (list zones) | SAFE UNKNOWN (collapse not tested)
```

**Technical PASS is impossible if Layout Layer fails** — same halt class as WF-LAYOUT-007 violation on hero `%` model.

---

## Applicability matrix

| Surface | WF-LAYOUT mandatory |
|---------|---------------------|
| Homepage generation | Yes — L2 hero, L3 featured, L5 trust |
| PDP generation | Yes — L1 hero, L5 trust, L4 credit |
| Catalog / listing pages | Yes — L3 with catalog charter |
| Corporate / service pages | Yes — zone types per blueprint |
| Landing pages | Yes |
| Gulp Frontend Agent | Yes |
| OpenCart theme implementation | Yes |
| WordPress theme implementation | Yes |
| Frontend QA | Yes — layout REPORT line |
| Production freeze | Blocked if Layout Layer NOT READY |

---

## Operator checklist (pre-merge / pre-approval)

- [ ] Container Layer PASS confirmed (WF-GRID-005) before layout checks
- [ ] Hero split uses fr/minmax authority — not default `%` (WF-LAYOUT-002, WF-LAYOUT-007)
- [ ] Card grids use documented `N` (WF-LAYOUT-003)
- [ ] Trust strip uses L5 grid grammar (WF-LAYOUT-004)
- [ ] Finance modules use L4/L3 patterns (WF-LAYOUT-005)
- [ ] Responsive collapse documented per zone (WF-LAYOUT-006)
- [ ] No new layout model without authority review (WF-LAYOUT-008)
- [ ] REPORT includes `WF LAYOUT DISCIPLINE` line

---

## Explicit non-goals (v1)

| Non-goal | Status |
|----------|--------|
| Automated layout lint / DOM audit | **Not implemented** |
| Defining global fr token values | **Project / Production Standards** |
| Pixel-perfect Figma diff | **Out of scope** — Design QA |
| Replacing WF-GRID-DISCIPLINE | **Complements only** |

---

## SAFE UNKNOWN

- CI enforcement of WF-LAYOUT markers — **not implemented**
- Exact offer min-width (360px vs 380px) — **project HITL after fr migration**
- Catalog auto-fill column math — **charter required before use**

---

*WF Layout Discipline v1 — Foundation-level mandatory rule set. Documentation only; no runtime.*
