# FP-0002 Services V2 — Internal Page Reference Baseline v1

## Page

`src/pages/uslugi-v2.html`

## Reference type

`SERVICES_HUB_INTERNAL_PAGE`

## Architecture (frozen order)

1. Services-specific Hero — `services-inner-hero-v2`
2. Breadcrumbs + Subnav
3. Category family — `services-category-section-v2` ×4
4. Services Program — `services-program-v2`
5. Home Founder Quote — `home-founder-quote` (variant-b)
6. Home Comfort — `home-comfort`
7. Duplicate Program CTA — `services-program-cta-band-v2`
8. Home FAQ — `home-faq`
9. Home Final Form — `home-final-form`
10. Footer + Modal

## Operator status

```text
services_v2_operator_acceptance: CONDITIONAL_ACCEPTED_REFERENCE
services_v2_canonical_switch: NOT_STARTED
services_v1: PRESERVED_FALLBACK
```

## Rules

- Reuse canonical partial → page text → exact assets → minimal scoped variant
- No new root variables / tokens / breakpoints / button types
- All SCSS in `src/scss/style.scss` only
- Visible mockup text policy: ACTIVE
