# FP-0002 Services V2 Corrections Map v1

| # | Correction | Selector / target | Method | Status |
|---|------------|-------------------|--------|--------|
| 4.1 | Gallery equal image heights | `.services-category-section-v2__gallery-image` | `aspect-ratio: 4/3` + `object-fit: cover` on image; caption outside height | COMPLETE |
| 4.2 | Program DOM order | `.services-program-v2__item` | `__item-body` before `__item-media`; `__item-text` → `__item-desc` | COMPLETE |
| 4.3 | Program card inset | `.services-program-v2__item` | Home direction pattern: card padding, media inset, image radius | COMPLETE |
| 4.4 | Hero scene layout | `.services-inner-hero-v2` | Eyebrow top; title+lead bottom-left; CTA bottom-right via flex scene | COMPLETE |
| 4.5 | Hero title typography | `.services-inner-hero-v2__title` | `var(--font-size-h2)` / `var(--line-height-h2)` | COMPLETE |

## Authority

- Figma `Spig_v1.2.fig` nodes referenced in block maps
- PNG `26.06.2026/Услуги общая - десктоп.png` / mobile

## Verdict

`CORRECTIONS_COMPLETE_PENDING_OPERATOR_REVIEW`
