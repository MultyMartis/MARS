# FP-0002 V7 Package #003 — Founder Quote Variants

**Date:** 2026-06-26  
**Design authority:** `Spig_v1.2.fig` (visual reference)

## Variant A — preserved fallback

- **Modifier:** none (default)
- **Asset:** `src/img/content/founder-sergey-shpigovsky.png` (unchanged)
- **CSS:** existing `.home-founder-quote__photo` rules with `border-radius: var(--radius-main)`
- **Active on:** Services page (`uslugi.html`), rollback target for Home

## Variant B — experimental (active on Home for review)

- **Modifier:** `.home-founder-quote--variant-b`
- **Activation:** `index.html` passes `founderQuoteModifierClass: " home-founder-quote--variant-b"`
- **Same asset:** no new photo generated
- **CSS layers:**
  - Horizontal/vertical CSS `mask-image` gradient on photo (soft left/top dissolve)
  - `::before` pseudo overlay with `var(--color-page-background)` and rgba blends
  - `object-fit: cover`, `object-position: 62% 12%` (desktop); mobile stack uses vertical mask
- **Text / CTA / quote SVG:** unchanged

## Rollback (exact)

In `src/pages/index.html`, change include to:

```html
@@include('partials/sections/home-founder-quote.html', {"modalSource": "founder-quote", "founderQuoteModifierClass": ""})
```

Or remove the modifier class value entirely. Variant A CSS remains in `style.scss`.

## Operator decision

Variant B is **not** final. Operator must choose A or B after visual review.

## Evidence screenshots

| File | Variant | Viewport |
| ---- | ------- | -------- |
| `FOUNDER-QUOTE-VARIANT-A-1398.png` | A | 1398 |
| `FOUNDER-QUOTE-VARIANT-A-390.png` | A | 390 |
| `FOUNDER-QUOTE-VARIANT-B-1398.png` | B | 1398 |
| `FOUNDER-QUOTE-VARIANT-B-390.png` | B | 390 |

Variant A screenshots captured via runtime class removal in review browser (same build as B).
