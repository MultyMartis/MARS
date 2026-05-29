# Visual semantics — Frontend priority

## `frontend_priority` stack (as-built)

```yaml
frontend_priority:
  - hero_main      # .hero__content
  - hero_aside     # form
  - hero_lower     # proof + cargo + notice
  - specs          # #specs
  - tasks          # #tasks
  - pricing_factors
  - trust_reviews
```

## Section P-levels (pack)

| Section | Priority |
|---------|----------|
| hero | P0 |
| specs, tasks | P0 |
| pricing, order steps | P1 |
| trust, b2b, dark strip | P2 |
| faq, final cta | P2 |

## Implementation hints

```yaml
factory_hints:
  data_page_type: ppc-zakaz-manip
  partial_paths:
    hero: v5-ppc/zakaz/screen-01-hero.html
    hero_scss: scss/sections/_v5-hero-extensions.scss
    specs_scss: scss/sections/_v5-machine-showcase.scss
  build: gulp — workspace README
```

## Factory must not

- Reorder P0 sections below fold without pack amendment
- Drop `data-page-type` marker
- Merge zakaz partials into generic index hero

## Reports feedback loop

Workspace reports (`v5-*-report-v1.md`) inform calibration — not auto-ingested.
