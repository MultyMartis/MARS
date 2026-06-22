# FP-0002 V6 HOME SECTION 01 — REJECTED

**Recorded:** 2026-06-23  
**Status:** REJECTED — active code removed; clean visual audit restarted

## Rejected implementation

| Field | Value |
|-------|-------|
| Working name | `home-intro-mission` |
| Partial | `src/partials/sections/home-intro-mission.html` |
| SCSS block | `.home-intro-mission` and descendants in `src/scss/style.scss` |
| Structure delivered | H2 + lead paragraph + 4-item benefits list + 3×2 card grid (6 cards) |
| Card icons | Font Awesome `fa-check-circle` |
| Row 2 cards | Duplicated row 1 titles/bodies as placeholders |

## Commit

| Field | Value |
|-------|-------|
| Rejected commit | `0e5af79` |
| Message | `feat(fp-0002): implement home section 01` |
| Stable shell before | `0fe76cd` (`fp-0002-v6-responsive-shell-stable-01`) |

## Operator decision

Operator rejected the implementation after visual review. Reasons:

1. Section repeated an erroneous structure from a prior attempt.
2. Structure was derived from archived `GROUP-01`, not from sole JPG authority.
3. Sole visual authority (`HOME-PAGE-FULL-MOCKUP.jpg`) was violated.
4. Second card row was filled by duplicating placeholder content.
5. Composition, proportions, and density did not match the current mockup.
6. Code cannot be corrected on top of the erroneous structure — full removal required.
7. Section analysis must restart from zero.

## Visual authority violation

The rejected spec (`FP-0002-V6-HOME-SECTION-01-SPEC.md`) cited archived group evidence:

```text
archive/aborted-section-attempts/intro-programs/specifications/evidence/02-group-01-intro-grid.jpg
```

and assumed a 3×2 grid with row-2 duplication “per JPG layout placeholder”. Operator confirmed this chain is **prohibited** for V6 structural reconstruction.

## Archived source reuse

| Source | Used in rejected pass | Status |
|--------|----------------------|--------|
| `GROUP-01` / intro-programs archive | YES | **PROHIBITED** |
| Old BLOCK-002 coordinates without re-proof | YES | **PROHIBITED** |
| `HOME-PAGE-FULL-MOCKUP.jpg` as sole authority | NO (partial / misread) | **REQUIRED** |

## Placeholder duplication

Rejected HTML duplicated three unique cards into six (`Реабилитация без изоляции`, `Участие семьи и близких`, `Выявление и uстранение причины зависимости` ×2). Operator decision: **prohibited** — unreadable or missing content must stop implementation, not be invented by duplication.

## Incorrect assumptions

- Card grid fixed at 3×2 with six slots before clean crop proof.
- Check-circle icon cards match mockup card treatment.
- Benefits list structure matches mockup without asymmetric / decorative column proof.
- Archived GROUP-01 geometry transferable to V6.
- Automated build success implies visual acceptance.

## Active code removed

| Artefact | Action |
|----------|--------|
| `src/pages/index.html` include | REMOVED |
| `src/partials/sections/home-intro-mission.html` | DELETED from active source |
| `.home-intro-mission*` SCSS block | REMOVED from `src/scss/style.scss` |
| Operator hero mobile tweaks in `style.scss` | **PRESERVED** |

## Historical artefacts retained

| Artefact | Location | Role |
|----------|----------|------|
| Rejected commit | `0e5af79` | Git history |
| Old spec | `reviews/main-content/FP-0002-V6-HOME-SECTION-01-SPEC.md` | Historical — not authority |
| Old review | `reviews/main-content/FP-0002-V6-HOME-SECTION-01-REVIEW.md` | Historical — not authority |
| Old captures | `reviews/main-content/visual/` | Rejected evidence |
| Capture script | `reviews/main-content/_section-01-visual-capture.py` | Historical |

## Stable shell status

```text
responsive_shell_release: FP-0002-V6-RESPONSIVE-SHELL-STABLE-01
responsive_shell_status: FROZEN_PRESERVED
responsive_shell_tag: fp-0002-v6-responsive-shell-stable-01
responsive_shell_commit: 0fe76cd
shell_regression_after_removal: NONE
```

Protected operator-canonical blocks: Desktop Header, Mobile Header, off-canvas, Hero (incl. mobile operator tweaks), Desktop Footer, Mobile Footer, local Inter, buttons, design values.

## Section 02 status

```text
home_section_02: BLOCKED
```

No Section 02 work until operator approves clean Section 01 audit.

## Required restart method

1. Sole authority: `HOME-PAGE-FULL-MOCKUP.jpg` (SHA-256 verified).
2. Clean boundary re-detection on JPG — no reuse of old Y coordinates without pixel proof.
3. Isolated canonical crop + geometry/content maps.
4. Operator approval of crop, boundaries, structure, content map.
5. Only then: new Block Implementation Specification → HTML → SCSS.

## Final status

```text
home_section_01: REJECTED_REMOVED
home_section_01_active_code: NONE
home_section_01_clean_audit: COMPLETE
home_section_01_new_implementation: NOT_STARTED
home_section_02: BLOCKED
IMPLEMENTATION AUTHORIZATION — NOT GRANTED
AWAITING OPERATOR REVIEW
```
