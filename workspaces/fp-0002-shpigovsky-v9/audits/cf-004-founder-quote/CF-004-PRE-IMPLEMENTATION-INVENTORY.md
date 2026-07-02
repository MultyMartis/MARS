# CF-004 Pre-Implementation Inventory — Founder Quote

**Captured:** 2026-06-28
**HEAD:** 98ea1ae66d4ef8f0c21360d6cc3ade10a385c8d9
**Wave:** CF-004 FOUNDER / EXPERT QUOTE universalization (pre-change)

## Summary

| Metric | Value |
| ------ | ----- |
| Partial path | `src/partials/sections/home-founder-quote.html` |
| Root class | `.home-founder-quote` |
| Consumer pages | 5 |
| HTML inline copies | 0 |
| CSS copies | 1 (`style.scss`) |
| Duplicate partials | 0 |

## Consumer inventory

| Page | Include path | Root class | Child classes | Label ID | CTA | Image | Page scope dependency |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `index.html` | `partials/sections/home-founder-quote.html` | `.home-founder-quote` | `__layout`, `__quote`, `__mark`, `__text`, `__figure`, `__photo`, `__author`, `__name`, `__role`, `__cta` | `home-founder-quote-label` | modal `consultation`; `data-modal-source="founder-quote"` | `assets/img/content/founder-sergey-shpigovsky.png` | modifier `--variant-b` |
| `uslugi-v2.html` | same | same | same | same | `data-modal-source="services-founder-quote"` | same | modifier `--variant-b` |
| `usluga-podrazdel-v1.html` | same | same | same | same | `data-modal-source="service-subdivision-founder"` | same | modifier `--variant-b` |
| `usluga-konechnaya-v1.html` | same | same | same | same | `data-modal-source="service-leaf-founder"` | same | modifier `--variant-b` |
| `uslugi.html` | same | same | same | same | `data-modal-source="services-founder"` | same | no modifier (variant A) |

## Include parameters

| Parameter | Purpose |
| --------- | ------- |
| `modalSource` | Per-page modal analytics source |
| `founderQuoteModifierClass` | Optional modifier token (e.g. ` home-founder-quote--variant-b`) |

## Accessibility

- Section: `aria-labelledby="home-founder-quote-label"`
- Hidden label: `#home-founder-quote-label` — «Слово основателя»
- Quote: `<blockquote>` with decorative SVG mark (`aria-hidden="true"`)
- Photo alt: «Сергей Юрьевич Шпиговский»
- CTA: button with modal hooks; accessible name from button text

## SCSS selectors (active source)

- Shared lead inset: `.home-founder-quote__text > span` (line ~644)
- Block ~1095–1214: layout, quote, mark, text, figure, photo, author, name, role, cta, variant-b
- Mobile ~3747–3770: layout stack, author static, variant-b photo/figure rules

## Result

**PASS** — single shared partial, single CSS family, five consumers, zero inline HTML copies.
