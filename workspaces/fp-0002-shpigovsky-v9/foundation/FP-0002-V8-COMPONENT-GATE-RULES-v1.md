# FP-0002 V8 — Component Gate Rules v1

**Status:** ACTIVE for all V8 implementation passes after bootstrap audit approval.

Before creating any **new** page-specific class or partial wrapper, all gates must pass:

| Gate | Requirement |
| ---- | ----------- |
| `EXISTING_VISUAL_ANALOGUE_SEARCHED` | Same visual block searched on all four canonical templates and historical V7 pages |
| `EXISTING_PARTIALS_CHECKED` | `src/partials/components/` and `src/partials/sections/` reviewed |
| `EXISTING_CLASS_FAMILIES_CHECKED` | Component family registry consulted |
| `EXISTING_CSS_GEOMETRY_CHECKED` | Matching layout metrics verified in `style.scss` |
| `EXISTING_RESPONSIVE_BEHAVIOR_CHECKED` | Breakpoint behavior compared, not assumed |
| `REUSE_IMPOSSIBILITY_PROVEN` | Documented why shared partial/class cannot serve the page |

## Not considered reuse

- HTML copied with renamed wrapper classes
- New page-specific wrapper around existing partials
- Second CSS block for the same geometry
- Modifier added without visual necessity
- Accessibility markup changed without design need
- JS hooks changed without behavior need
- Semantic-only similarity without visual match
- Same visual block under different class names on different pages

## Page-specific class allowance

Permitted only when the block is **visually distinct** on inspection against Figma/export reference.
