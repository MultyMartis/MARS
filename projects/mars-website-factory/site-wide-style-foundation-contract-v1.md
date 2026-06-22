# Website Factory Site-Wide Style Foundation Contract v1

**Status:** **documented** — mandatory project artefact template before block implementation.  
**Not:** `_variables.scss`, runtime token engine, or automated design-system generator.

**Purpose:** Single project-level SSOT answering: which container, rhythm, type, color roles, radii, buttons, and cards apply site-wide before any block HTML/SCSS.

**Upstream:** [practical-value-normalization-contract-v1.md](practical-value-normalization-contract-v1.md)  
**Downstream:** [block-implementation-specification-contract-v1.md](block-implementation-specification-contract-v1.md)  
**Peer:** [frontend-visual-foundation-contract-v1.md](frontend-visual-foundation-contract-v1.md) (demo page composition — **after** this foundation for greenfield shell path)

**Registry:** [registries.md §6](registries.md#6-frontend-production-rules).

---

## Mandatory gate

```text
Site-Wide Style Foundation (operator-approved)
        ↓
Page / Block Implementation Specification
        ↓
HTML Structure Gate
        ↓
SCSS Implementation Gate
```

While foundation is not operator-approved:

```text
implementation_authorized: false
```

---

## Required document sections (per project)

Each project file (e.g. `FP-XXXX-VN-SITE-WIDE-STYLE-FOUNDATION.md`) **must** include all sections below. Use `SAFE UNKNOWN` where evidence does not support a value.

### 1. Source authority

- Visual source path + hash
- Audit artefacts used
- Forbidden sources list (project policy)
- Grounding review verdict

### 2. Foundation scope

- Pages covered (e.g. Home first)
- Sections in scope vs deferred
- What foundation does **not** decide (e.g. unresolved Header/Hero split)

### 3. Evidence inputs

- Design foundation extraction path
- Normalization path
- Operator rules cited (OL-01, etc.)

### 4. Container system

| Layer | Document |
|-------|----------|
| Viewport / full-width | Full-bleed media, band backgrounds |
| Main container | Repeated content bounds from evidence |
| Narrow container | Quote, form side panels if evidenced |
| Media bleed | Photos, mosaics |
| Exceptions | Per-section full-width rows |

Bind to [WF-GRID-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-GRID-DISCIPLINE-v1.md) at implementation time.

#### Single Base Container Law (mandatory)

Every site has **one primary content container** class (project default: `.container`). It owns:

- `width: 100%`
- `max-width` (e.g. `--container-main`)
- horizontal centering (`margin-left: auto; margin-right: auto`)
- standard page horizontal padding (`padding-left` / `padding-right` via `--pad-x`)

Header, Footer, and standard content sections **must reuse** this class on the inner wrapper — not duplicate its geometry in BEM `__container` selectors.

**Prohibited without documented exception:** per-block `__container` selectors repeating `max-width` + horizontal centering + horizontal padding; nested primary containers; new `--container-*` tokens per block for convenience; selector-specific spacing tokens (`--header-*`, `--footer-*` for primitive scale); alias chains that only rename `--pad-*` for one block.

**Physical CSS rule:** production SCSS uses `padding-top/right/bottom/left` and `margin-top/right/bottom/left` — not logical `padding-block` / `padding-inline` / `margin-block` / `margin-inline` by default ([universal-style-scale-law-v1.md](universal-style-scale-law-v1.md)).

**Allowed exceptions:** visual evidence of a different width field (e.g. `--container-hero`) — requires exception register: evidence, semantic role, scope, approval, source-to-token mapping.

**Container exception gate:** Existing base container lookup → visual evidence → exception classification → approval → token registration → implementation. On skip: `CONTAINER GATE — FAIL`.

**Enforcement:** **MANDATORY DOCUMENTED PRODUCTION GATES** — **AUTOMATED ENFORCEMENT — NOT YET IMPLEMENTED**

### 5. Spacing scale

- **Compact core scale** — role-named primitives (e.g. `--pad-x`, `--pad-y`, `--pad-gap`, `--pad-gap-line`, `--pad-box`) — not selector-named aliases
- Section padding classes (consume core scale — do not invent per-block vocabulary)
- Component padding classes
- Layout gaps
- Text gaps
- Exception rules

**Authority:** [universal-style-scale-law-v1.md](universal-style-scale-law-v1.md) · [css-variable-first-law-v1.md](css-variable-first-law-v1.md) (corrected: reusable → token; unique geometry → direct local CSS)

Cross-ref [frontend-section-spacing-rule-v1.md](frontend-section-spacing-rule-v1.md) for same-bg vs diff-bg boundaries.

#### Section Owns Its Rhythm Law (mandatory)

Spacing between major page regions belongs to the **section or layout region** (`section`, `.section`, `.site-header`, `.site-footer`, other classified major layout regions). It must **not** be simulated by padding or margin on the first/last internal child.

| Ownership | Owner | Examples |
|-----------|-------|----------|
| Section/layout-region rhythm | Outer shell | `padding-block` on `.site-header`, `.site-footer`, `.section` |
| Internal component spacing | Component | card padding, button padding, nav `gap` |
| Inter-component spacing | Parent of siblings | `.section__content { gap: … }` |
| Exact geometry | Local exception only | evidenced unique geometry |

**Rhythm modifiers (approved tokens only):** `compact` · `standard` · `large` · `none` — map to `--section-padding-compact`, `--section-padding-standard`, `--section-padding-large`, or layout-region tokens (`--footer-padding-block`, `--header-padding-block-*`).

**Forbidden:** `main > div { padding-block: … }` without semantic section contract; first/last child padding used as section boundary workaround.

**Gate:** `SECTION RHYTHM GATE — FAIL` when boundary spacing is owned by internal children.

**Enforcement:** **MANDATORY DOCUMENTED PRODUCTION GATES** — **AUTOMATED ENFORCEMENT — NOT YET IMPLEMENTED**

### 6. Section rhythm

Define **classes only** — assign values after evidence + normalization:

| Class | Intent |
|-------|--------|
| `compact` | Tight continuation (cadence XS–S) |
| `standard` | Default section (cadence M) |
| `large` | Reset / breathing (cadence L) |
| `feature` | Major band / CTA isolation |
| `hero` | First-screen / SECTION-001 class |
| `custom-exception` | Named operator-approved deviation |

Map tiers per [cadence-tier-model.md](cadence-tier-model.md).

### 7. Typography hierarchy

For each role: `display`, `H1`, `H2`, `H3`, `body-large`, `body`, `small`, `label`, `button`:

- desktop size (observed range → normalized proposal)
- mobile size (or SAFE UNKNOWN)
- weight
- line-height (default `font-size + 4px` per [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) §3)
- letter-spacing (default: none — OL word-break laws apply)
- color role
- allowed exceptions

### 8. Color roles

Roles only — **no invented HEX** without evidence:

`page-background` · `surface` · `primary-text` · `secondary-text` · `accent` · `inverse` · `border` · `muted` · `interactive`

Record observed families (e.g. light blue page wash) as evidence notes; HEX proposals require normalization confidence or SAFE UNKNOWN.

### 9. Radius system

Default unified radius (mandatory unless operator exception):

```text
--radius-main   — standard rounding (buttons, inputs, cards, panels)
--radius-full   — circles and pills only
```

Prohibited by default: `--radius-small`, `--radius-medium`, `--radius-large`, `--control-radius`, `--button-radius`, `--button-letter-spacing`. Authority: [universal-style-scale-law-v1.md](universal-style-scale-law-v1.md) · [no-button-letter-spacing-law-v1.md](no-button-letter-spacing-law-v1.md).

All project CSS variables live in `src/scss/style.scss` — [one-project-scss-file-law-v1.md](one-project-scss-file-law-v1.md).

### 10. Border system

### 11. Shadow system

### 12. Button system

All CTAs use the universal `.btn` system ([universal-button-system-law-v1.md](universal-button-system-law-v1.md)):

- Base class: `.btn`
- Modifiers: `.btn_dark`, `.btn--primary` (combinable)
- Tokens: `--pad-btns`, `--main-size-btns`, `--pad-gap-mini`, `--radius-full`
- Block-specific classes: placement / layout only — no duplicate geometry

### 13. Form system

### 14. Card system

Families (service card, benefit card, review card, etc.)

### 15. Image behavior

Aspect ratios, full-bleed rules, overlay panels

### 16. Grid and column rules

2-col, 3-col, 6-card grid patterns — cite layout pattern or SAFE UNKNOWN

### 17. Shared component rhythm

Spacing between repeated components (accordion rows, program items)

### 18. Responsive rules

Desktop-first evidence note; mobile = SAFE UNKNOWN until separate audit

### 19. Allowed exceptions

Exception register with Evidence ID link

### 20. SAFE UNKNOWN

Unresolved items blocking specific bindings

### 21. Operator approval

| Field | Value |
|-------|-------|
| `foundation_status` | `PROPOSAL` \| `APPROVED` \| `PARTIAL` |
| `approved_by` | operator name or pending |
| `approval_date` | ISO date or pending |

### 22. Implementation authorization

```text
implementation_authorized: false | true
header_implementation_authorized: false | true
```

Header/hero require explicit flags when grounding review is PARTIAL.

---

## Machine-readable companion

Optional `*-STYLE-FOUNDATION.json` mirroring tokens for tooling — must stay in sync with markdown SSOT.

**Component tokens:** Register shared control, button, icon, border, motion, and surface tokens in `:root` per [css-variable-first-law-v1.md](css-variable-first-law-v1.md) before block SCSS.

---

## Relationship to Production Standards governance

[production-standards-governance-v1.md](production-standards-governance-v1.md) remains the **generic** greenfield gate (C-01–C-16). For **JPG-only clean-room** pilots (FP-0002 V6), Site-Wide Style Foundation **replaces** project-specific Production Standards until operator promotes foundation to approved SSOT.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-06-22 | v1 — Mandatory gate between normalization and block specification |
| 2026-06-22 | v1.1 — Component token registration; CSS Variable First Law link |
| 2026-06-22 | v1.2 — Single Base Container Law; Section Owns Its Rhythm Law |
