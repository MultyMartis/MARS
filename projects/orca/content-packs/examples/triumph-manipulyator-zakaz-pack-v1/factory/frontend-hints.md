# Factory — Frontend hints

## Page marker

```html
<body data-page-type="ppc-zakaz-manip">
```

## Partial map

| Section | Path |
|---------|------|
| Hero | `partials/sections/v5-ppc/zakaz/screen-01-hero.html` |
| Specs | `.../screen-02-specs.html` |
| Tasks | `.../screen-02-tasks.html` |
| Order | `.../screen-02b-order-steps.html` |
| Pricing | `.../screen-02c-pricing-factors.html` |
| FAQ | `.../screen-04-faq.html` |
| Final CTA | `.../final-contact-cta.html` |
| Trust | `partials/sections/v5-page01/screen-03-trust-reviews.html` |
| B2B | `partials/sections/v5-page01/screen-03b-b2b.html` |
| Footer | `partials/sections/v5-page01/landing-footer.html` |

## SCSS scope

| File | Scope |
|------|-------|
| `_v5-hero-extensions.scss` | `.hero--v5`, first-screen |
| `_v5-machine-showcase.scss` | `body[data-page-type='ppc-zakaz-manip']` |

## Data attributes (forms)

- `data-form-id`: `zakaz-hero-quote`, `zakaz-contact-quote`
- `data-cta-source`: per-button traceability (e.g. `zakaz-hero-cargo-bytovki`)

## Assets

- Hero bg: `/assets/img/hero/hero-bg-final.jpg`
- Specs image: `/assets/img/v5/second-screen/second-screen-index-baseline.jpg`

## Do not

- Point Factory to v4 index `screen-01-hero.html` as reference
- Use 5-ton pack partial paths without substitution

## QA reports (workspace)

- `reports/v5-production-hardening-audit-v1.md`
- `reports/v5-typography-stable-snapshot-report-v1.md`

Human QA — not auto-linked to pack validation.
