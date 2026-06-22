# Website Factory Block Implementation Specification Contract v1

**Status:** **documented** — mandatory per-block artefact before HTML and SCSS.  
**Not:** Layout Spec (see [layout-spec-law-v1.md](layout-spec-law-v1.md)), automated codegen, or Forge task JSON.

**Purpose:** Bind one block/section to approved Site-Wide Style Foundation tokens so implementers do not invent spacing, type, or colors.

**Upstream:** [site-wide-style-foundation-contract-v1.md](site-wide-style-foundation-contract-v1.md)  
**Peer:** [layout-spec-law-v1.md](layout-spec-law-v1.md) (zone/row composition), [group-decomposition-law-v1.md](group-decomposition-law-v1.md) (GROUP-IDs)

---

## Core rule

**Implementers must not choose spacing, typography, container, or component values independently when Site-Wide Style Foundation already defines them.**

Deviations require exception register entry + operator approval.

---

## Required sections (per block)

### Identity

- `block_spec_id` (e.g. `FP-0002-V6-SPEC-SECTION-001-HEADER`)
- `section_id` (grounded section reference)
- `component_ids` (CMP-* list)
- `forge_block_id` if registry-bound (optional)

### Source evidence

- JPG region (Y range, screenshot ref)
- Grounding review classification
- Confidence

### Parent page section

- Page slug
- Section order
- Neighbor sections (rhythm context: same-bg vs diff-bg)

### Component bindings

Map each visible group to foundation component family.

### Container binding

- `container-main` \| `container-narrow` \| `full-bleed` \| `exception`

### Container usage (mandatory)

```markdown
## Container usage

Primary container reused: YES/NO

Container exception requested: YES/NO

Container exception evidence:
```

Rules: [site-wide-style-foundation-contract-v1.md](site-wide-style-foundation-contract-v1.md) §4 Single Base Container Law · [WF-GRID-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-GRID-DISCIPLINE-v1.md) WF-GRID-006.

### Section rhythm ownership (mandatory)

```markdown
## Section rhythm ownership

Top rhythm owner:

Bottom rhythm owner:

Internal spacing owners:

First-child boundary spacing: NONE

Last-child boundary spacing: NONE
```

Rules: [site-wide-style-foundation-contract-v1.md](site-wide-style-foundation-contract-v1.md) §6 Section Owns Its Rhythm Law · [frontend-section-spacing-rule-v1.md](frontend-section-spacing-rule-v1.md) §2.6.

### Typography bindings

Per element role → foundation typography token.

### Spacing bindings

Per region → **core spacing scale token** (`--pad-*`) or shared component token — **not** selector-named aliases. See [universal-style-scale-law-v1.md](universal-style-scale-law-v1.md).

### Existing style scale usage (mandatory)

```markdown
## Existing style scale usage

Spacing tokens reused:

Radius tokens reused:

Typography tokens reused:

Color tokens reused:

Component tokens reused:

## New token requests

New primitive tokens requested:

New shared component tokens requested:

Independent consumers:

Why existing scale is insufficient:

## Exact geometry

Direct exact values:

Evidence:

## Property syntax

Logical properties required: NO

Physical padding/margin properties planned: YES
```

### Color bindings

Per element → color role (not raw hex unless exception).

### Grid bindings

Column pattern ID, gap token.

### Exact geometry constraints

Provable constraints only (e.g. header bar height observed range).

### Normalized values

Table linking Evidence ID → token.

### Exceptional values

Rows outside foundation with approval slot.

### Asset bindings

Image slots, icons, logo — path policy only.

### Responsive behavior

Desktop evidence; mobile SAFE UNKNOWN unless specified.

### Interaction behavior

Accordion, carousel, form — minimal; SAFE UNKNOWN default.

### SAFE UNKNOWN

Items blocking HTML or SCSS.

### Forbidden deviations

Values agent must not invent.

### HTML structure authorization

```text
html_structure_authorized: false | true
```

### SCSS authorization

```text
scss_authorized: false | true
```

Requires `html_structure_authorized: true` + foundation `APPROVED` or scoped operator waiver.

### Token lookup (mandatory before SCSS)

Each block specification must include:

```markdown
## Variables reused

## New tokens proposed

## Block-level tokens

## Exact geometry exceptions

## Technical CSS values

## Arbitrary values prohibited

## Token lookup result
```

**Authority:** [css-variable-first-law-v1.md](css-variable-first-law-v1.md)

HTML gate does **not** automatically authorize SCSS. SCSS is permitted only after token lookup passes [frontend-pre-scss-validation-checklist-v1.md](frontend-pre-scss-validation-checklist-v1.md).

### Visual QA acceptance criteria

- Screenshot compare region
- Foundation token checklist
- Operator visual review required per [operator-visual-approval-law-v1.md](operator-visual-approval-law-v1.md)

---

## Gate sequence (per block)

```text
Block Implementation Specification (draft)
        ↓ operator review
Block Implementation Specification (approved)
        ↓
HTML only (structure gate)
        ↓ HTML review
SCSS (foundation bindings only)
        ↓
Visual QA
        ↓
Correction loop → spec | foundation | audit defect class
```

---

## Filename convention

```text
<PROJECT>-SPEC-<SECTION-ID>-<BLOCK-NAME>.md
```

Example: `FP-0002-V6-SPEC-SECTION-001-HEADER.md` — create only when Gate 3 opens.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-06-22 | v1 — Connects foundation to HTML/SCSS gates |
| 2026-06-22 | v1.1 — Token lookup sections; CSS Variable First Law binding |
| 2026-06-22 | v1.2 — Container usage + section rhythm ownership mandatory sections |
| 2026-06-23 | v1.3 — Existing style scale usage; new token requests; property syntax; Universal Style Scale Law binding |
