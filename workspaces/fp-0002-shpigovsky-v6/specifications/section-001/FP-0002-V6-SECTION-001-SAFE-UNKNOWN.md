# FP-0002 V6 SECTION-001 SAFE UNKNOWN

**Scope:** SECTION-001 — Header + Hero composite  
**Foundation ref:** [FP-0002-V6-FOUNDATION-SAFE-UNKNOWN.md](../../foundation/FP-0002-V6-FOUNDATION-SAFE-UNKNOWN.md)

---

## Structural

| ID | Item | Blocks HTML? | Resolution path |
|----|------|--------------|-----------------|
| SU-S001-001 | Exact Header block height as one CSS value | Partial — use element bounds | Operator approve composite layout at HTML gate |
| SU-S001-002 | Header/Hero Y split coordinate | No — composite section | **Y=174 forbidden for CSS** |
| SU-S001-003 | Hero frosted panel exact radius px | Partial — visual QA | Block exception EX-S001-RAD-002 |
| SU-S001-004 | Hero photo top corner radius px | Partial | Block exception |
| SU-S001-005 | Separator rule exact color/weight | No | Color role `border-subtle` |

---

## Container

| ID | Item | Blocks HTML? | Resolution path |
|----|------|--------------|-----------------|
| SU-S001-006 | JPG inset 130px vs `container-main` 1220px centering math | Partial | `container-padding-inline-desktop` block proposal |
| SU-S001-007 | Whether inner narrow group needed inside 1220px | No | Measure at HTML structure gate |

---

## Typography

| ID | Item | Blocks HTML? |
|----|------|--------------|
| SU-S001-008 | All font-family choices | Yes for production font loading |
| SU-S001-009 | Exact px per role — global | No — block proposals in spec |
| SU-S001-010 | Line-height per role | Partial |

---

## Color

| ID | Item | Blocks HTML? |
|----|------|--------------|
| SU-S001-011 | Accent red HEX for hero CTA | Partial — structure can use role |
| SU-S001-012 | Header CTA border color HEX | Partial |
| SU-S001-013 | Frosted panel background rgba | Partial |

---

## Interaction

| ID | Item | Blocks HTML? |
|----|------|--------------|
| SU-S001-014 | Sticky header | No — do not implement without approval |
| SU-S001-015 | Nav hover/active | No |
| SU-S001-016 | Search behavior | No |
| SU-S001-017 | Dropdown menus | No — not in JPG |
| SU-S001-018 | CTA href / tel: links | Partial — content decision |

---

## Responsive

| ID | Item | Blocks desktop HTML? |
|----|------|---------------------|
| SU-S001-019 | Mobile header layout ≤1024px | **No** — desktop may proceed after spec approval |
| SU-S001-020 | Mobile hero crop/stack | **No** |
| SU-S001-021 | Breakpoint behavior between 1024–1398 | Partial |

---

## Button geometry

| ID | Item | Note |
|----|------|------|
| SU-S001-022 | Global `button-height-standard: 30px` | **DEFERRED** — hero uses 45px EX-S001-001 |
| SU-S001-023 | Header outline button exact height | Block-level ~32px proposal |

---

## CSS-forbidden values (SECTION-001)

| Value | Classification |
|-------|----------------|
| Y = 174px | OBSERVED_JPG_ESTIMATE — CSS_USE_FORBIDDEN |
| width = 1138px as max-width | OBSERVED_JPG_VALUE |
| height = 30px for hero CTA | Contradicts evidence |

---

## Items resolved by operator decision 2026-06-22

| ID | Resolution |
|----|------------|
| SU-002 | Composite SECTION-001 — Hero not separate major section |
| SU-001 | Y=174 estimate documented; geometry from elements only |
