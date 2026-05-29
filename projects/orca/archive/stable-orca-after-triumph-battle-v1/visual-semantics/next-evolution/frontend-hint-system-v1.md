# Frontend Hint System v1 (planned)

**Goal:** structured `factory_hints` without CSS in ORCA repo.

## Hint categories

| Category | Example |
|----------|---------|
| `partial_paths` | hero, specs, trust partials |
| `data_page_type` | `ppc-zakaz-manip` |
| `breakpoints` | stack at 760px |
| `sticky` | mobile tel+form bar |
| `caps` | cargo_cards_max |
| `cta_styles` | cargo = outline |
| `image_refs` | second-screen slug |
| `build` | gulp command, dist path |

## Example bundle

```yaml
factory_hints:
  data_page_type: ppc-zakaz-manip
  breakpoints:
    hero_stack: 760
    type_tune: 420
  sticky_mobile_bar: optional
  partial_paths:
    hero: v5-ppc/zakaz/screen-01-hero.html
  caps:
    cargo_cards_max: 6
    cargo_cards_max_mobile: 4
```

## Non-goals

- SCSS snippets in ORCA (belongs in Factory)
- Design tokens
- Auto-sync from workspace

## Feedback

Promote hints from `workspaces/.../reports/` via calibration — human only.

## SAFE UNKNOWN

Machine-readable hint schema validation — future.
