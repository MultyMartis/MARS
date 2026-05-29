# Visual semantics — Semantic density

## Field

`visual_density: high`

## Count budget (hero, approximate)

| Unit | Count |
|------|-------|
| H1 + lead | 2 |
| Spec lines | 5 |
| Form fields + submit + call | 4+ |
| Proof items | 4 |
| Cargo cards | 6 |
| Notice | 1 |
| **Total distinct messages** | ~22 before scroll |

## Why high is acceptable here

- `hero_layout_mode: grid_form_aside` + `hero__lower` zoning separates scan phases
- `compactness_level: compact` — icon lines, not paragraphs

## vs G0

G0 was **high + unstructured** = destructive. G2 is **high + zoned** = productive.

## Reduction levers (allowed drift)

- Cap cargo cards at 4 on mobile
- Merge redundant «мин. заказ» proof label
- Collapse proof strip on smallest breakpoints — **visual only**, keep semantics

## Forbidden

- Removing specs to «simplify» without PPC approval
- Adding 7th cargo type without task doctrine
