# FP-0002 Services V2 Hero Layout Map v1

**Figma:** inner hero on Services general page  
**Root:** `.services-inner-hero-v2`

## Desktop composition

| Region | Element | Alignment |
|--------|---------|-----------|
| Top-left | `.services-inner-hero-v2__eyebrow` — «Заболевания, которые мы лечим» | Top of content copy column (`justify-content: space-between` on `__copy`) |
| Bottom-left | `.services-inner-hero-v2__main` — title + lead | Bottom of scene (`align-items: flex-end` on `__scene`) |
| Bottom-right | `.services-inner-hero-v2__actions` — CTA | `align-self: flex-end` |

## Typography

- Title: `font-size: var(--font-size-h2); line-height: var(--line-height-h2);`

## Mobile (≤1024)

- Scene stacks column; CTA full width per scoped mobile rules

## Probe (1398)

- `heroScene`: true
- `heroEyebrow`: «Заболевания, которые мы лечим»
- `overflowX`: false

## Verdict

`CORRECTED_PENDING_OPERATOR_REVIEW`
