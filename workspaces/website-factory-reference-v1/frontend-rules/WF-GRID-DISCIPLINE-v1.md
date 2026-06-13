# Website Factory — WF Grid Discipline v1

**Версия:** v1  
**Дата:** 2026-06-13  
**Область:** `workspaces/website-factory-reference-v1/frontend-rules/`  
**Статус:** **MANDATORY** — Foundation-level frontend layout authority  
**Authority:** Default for all Website Factory projects (Gulp, OpenCart, WordPress, corporate, landing, catalog, PDP, homepage)

**Origin:** Promoted from SITE-001 (СИБКАР) WF-V3 prototype — [reports/WF-GRID-DISCIPLINE-PROMOTION-v1.md](../reports/WF-GRID-DISCIPLINE-PROMOTION-v1.md)

**Не является:** runtime validator, automated linter, CI gate, design token spec, responsive breakpoint registry.

**Связь:** [design-system/DESIGN-SYSTEM-RULES-v1.md](../design-system/DESIGN-SYSTEM-RULES-v1.md), [blueprints/BLUEPRINT-IMPLEMENTATION-RULES-v1.md](../blueprints/BLUEPRINT-IMPLEMENTATION-RULES-v1.md), [production-qa/PRODUCTION-QA-CHECKLIST-v1.md](../production-qa/PRODUCTION-QA-CHECKLIST-v1.md), [projects/mars-website-factory/frontend-production-rules-v0.md](../../../projects/mars-website-factory/frontend-production-rules-v0.md)

---

## Purpose

WF Grid Discipline defines the **mandatory separation** between **section** (vertical / full-bleed layer) and **container** (horizontal content grid). Mixing these roles causes inconsistent visual widths, broken horizontal rhythm, and sections that appear wider or narrower than header/footer — **independent of design quality**.

This rule set applies to **all** Website Factory frontend surfaces: homepage, PDP, catalog, corporate pages, landings, Gulp static builds, OpenCart themes, WordPress themes.

---

## Rule index

| ID | Rule | Severity |
|----|------|----------|
| WF-GRID-001 | Section is not container | CRITICAL |
| WF-GRID-002 | One page = one grid contract | CRITICAL |
| WF-GRID-003 | Local width authority required | HIGH |
| WF-GRID-004 | Full-bleed is not grid break | CRITICAL |
| WF-GRID-005 | QA grid check | CRITICAL |

---

## WF-GRID-001 — Section is not container

### Definition

**Section owns:**

- backgrounds (color, image, gradient)
- vertical rhythm (section padding, gaps between blocks)
- decorative full-width elements
- full-width layout shell

**Container owns:**

- horizontal max-width
- side padding (`padding-inline`)
- content alignment within the page grid
- column alignment across the page

### Forbidden

Semantic layout elements must **not** carry the container class as their primary width authority:

```html
<section class="wf-container">
```

```html
<nav class="wf-container">
```

```html
<header class="wf-container">
```

Project-specific prefixes (`wf-v3-container`, `container`, `section-shell` misapplied on `<section>`) follow the same rule.

### Required

```html
<section class="wf-section">
    <div class="wf-container">
        ...
    </div>
</section>
```

```html
<nav class="wf-section wf-section--header">
    <div class="wf-container">
        ...
    </div>
</nav>
```

**`<nav>`, `<header>`, `<footer>`, `<main>` child regions:** same pattern — outer semantic element = section/shell role; inner `div` (or documented inner wrapper) = container role.

### Failure symptoms

- Hero content wider or narrower than header logo row
- Footer columns misaligned with main content
- Alternating section widths on the same page
- Horizontal rhythm breaks despite correct design tokens

---

## WF-GRID-002 — One page = one grid contract

Every page must declare and use **one primary content grid contract**.

### Example contract (project-defined values)

```scss
--container-max: 1280px;
--container-pad: 24px;
```

Or project Production Standards equivalent (`container-max`, `container-pad`, `section-shell` tokens).

### Rules

| Rule | Detail |
|------|--------|
| **Single authority** | All major content sections align to the same container max-width and inline padding unless WF-GRID-003 exception is documented |
| **No per-section width drift** | Changing `max-width` or horizontal padding per section is **prohibited** unless explicitly documented |
| **Header / footer parity** | Global chrome uses the **same** grid contract as page body sections |
| **Token source** | Grid contract lives in Project Production Standards, handoff `DESIGN_SPEC`, or foundation tokens — not ad-hoc in section SCSS |

### Forbidden

- Section A at `1280px`, Section B at `1170px`, header at `1200px` without documented exception
- Inline `style="max-width: …"` on sections to “fix” alignment

---

## WF-GRID-003 — Local width authority required

Any use of local horizontal width control **outside** the core container requires **documented justification**.

### Trigger properties

```scss
max-width
padding-inline
margin-inline
```

Applied on selectors that are **not** the canonical container class/wrapper.

### Required documentation

- Project log, handoff note, or inline SCSS comment with marker:

```scss
/* WF-GRID-EXCEPTION: reason — approver — date */
```

### Allowed without exception (narrow)

- Component-internal micro-layout (card innards, icon boxes) where width does not define page grid
- Full-bleed decorative pseudo-elements (see WF-GRID-004)
- Documented narrow variants (e.g. legal prose column) with explicit charter

### Forbidden

- Silent per-section `max-width` overrides to compensate for WF-GRID-001 violations
- “Fixing” misaligned sections by nudging `margin-inline` without exception record

---

## WF-GRID-004 — Full-bleed is not grid break

Full-width backgrounds and band treatments are **allowed** on the section layer.

**Content inside full-bleed sections must still use the main container.**

### Required pattern

```html
<section class="hero hero--dark">
    <div class="wf-container">
        ...
    </div>
</section>
```

```html
<section class="cta-band cta-band--accent">
    <div class="wf-container">
        ...
    </div>
</section>
```

### Rules

| Layer | Allowed |
|-------|---------|
| `<section>` | `width: 100%`, background, vertical padding, decorative ::before/::after |
| Inner `.wf-container` | `max-width`, `padding-inline`, content grid |

### Forbidden

- Treating full-bleed background as permission to skip the inner container
- Viewport-wide text blocks without inner container alignment

---

## WF-GRID-005 — QA grid check

Frontend QA **must** verify grid alignment **before** visual approval.

### Mandatory alignment checks

| Check | Pass criterion |
|-------|----------------|
| **Header alignment** | Header content edges align with primary page container |
| **Hero alignment** | Hero inner content aligns with header/body container |
| **Section alignment** | Each major section inner content aligns to the same vertical grid lines |
| **Footer alignment** | Footer columns and legal row align with body container |

### Viewports

Spot-check at minimum: desktop primary width (e.g. 1280–1440px) and one mobile width (e.g. 375px). Project QA presets may extend the matrix.

### Gate rule

**Technical PASS is impossible if grid discipline fails.**

Grid failure severity = **CRITICAL** — same halt class as WF-GRID-001 violation. Visual polish does not override grid misalignment.

### REPORT line (mandatory for Frontend QA)

```text
WF GRID DISCIPLINE — PASS | FAIL (list sections) | SAFE UNKNOWN (widths not tested)
```

---

## Applicability matrix

| Surface | WF-GRID mandatory |
|---------|-------------------|
| Homepage generation | Yes |
| PDP generation | Yes |
| Catalog / listing pages | Yes |
| Corporate / service pages | Yes |
| Landing pages | Yes |
| Gulp Frontend Agent | Yes |
| OpenCart theme implementation | Yes |
| WordPress theme implementation | Yes |
| Frontend QA | Yes — WF-GRID-005 |
| Design QA (visual) | Yes — alignment prerequisite |
| Production QA (architecture) | References handoff; implementation QA enforces |

---

## Operator checklist (pre-merge / pre-approval)

- [ ] No `<section>`, `<nav>`, `<header>`, `<footer>` with container-only class as sole width wrapper (WF-GRID-001)
- [ ] Page grid contract documented in Production Standards or handoff (WF-GRID-002)
- [ ] No undocumented local `max-width` / `padding-inline` / `margin-inline` on section roots (WF-GRID-003)
- [ ] Full-bleed sections contain inner container wrapper (WF-GRID-004)
- [ ] Header / hero / sections / footer alignment verified (WF-GRID-005)
- [ ] REPORT includes `WF GRID DISCIPLINE` line

---

## Explicit non-goals (v1)

| Non-goal | Status |
|----------|--------|
| Automated DOM linter for section/container split | **Not implemented** |
| Pixel-perfect Figma diff | **Out of scope** — separate Design QA |
| Defining global `--container-max` values | **Project / Production Standards** — not this doc |

---

## SAFE UNKNOWN

- CI enforcement of WF-GRID markers — **not implemented**
- OpenCart/WordPress-specific class naming conventions — projects map to `wf-section` / `wf-container` semantics; exact BEM names → project charter

---

*WF Grid Discipline v1 — Foundation-level mandatory rule set. Documentation only; no runtime.*
