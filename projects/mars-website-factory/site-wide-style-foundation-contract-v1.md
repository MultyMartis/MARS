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

### 5. Spacing scale

- Base scale (from normalization)
- Section padding classes
- Component padding classes
- Layout gaps
- Text gaps
- Exception rules

Cross-ref [frontend-section-spacing-rule-v1.md](frontend-section-spacing-rule-v1.md) for same-bg vs diff-bg boundaries.

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

### 10. Border system

### 11. Shadow system

### 12. Button system

Families from component map (primary, secondary, etc.)

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

---

## Relationship to Production Standards governance

[production-standards-governance-v1.md](production-standards-governance-v1.md) remains the **generic** greenfield gate (C-01–C-16). For **JPG-only clean-room** pilots (FP-0002 V6), Site-Wide Style Foundation **replaces** project-specific Production Standards until operator promotes foundation to approved SSOT.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-06-22 | v1 — Mandatory gate between normalization and block specification |
