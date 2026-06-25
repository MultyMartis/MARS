# FP-0002 V7 Package #002 — Source Map

**Date:** 2026-06-26  
**Authority:** Operator-canonical src after checkpoint `95b97adf`

## External link SVG

| Figma node | Visible layer | Frontend asset | HTML destination |
| ---------- | ------------- | -------------- | ---------------- |
| `1:3609` | `arrow-up-right` in `Пункт услуги` | `src/svg/external-link.svg` | `.home-treatment-prevention__service-icon` in `home-treatment-prevention.html`, `home-why-us.html` |

## Home videos

| INCOMING source | Size | Frontend file | Preview block |
| --------------- | ---: | ------------- | ------------- |
| `INCOMING/02_CONTENT/video/Интервью с Сергеем Шпиговским.mp4` | 27 328 432 | `src/video/sergey-shpigovsky-interview.mp4` | `home-videos` card 1 |
| `INCOMING/02_CONTENT/video/Центр профилактики зависимостей Сергея Шпиговского.mp4` | 41 459 593 | `src/video/shpigovsky-center.mp4` | `home-videos` card 2 |

## Hero architecture

| Variant | Partial | Modifier | Desktop max |
| ------- | ------- | -------- | ----------- |
| Home | `partials/sections/hero.html` | `.hero--home` | 1400 × 750 |
| Inner page base | `partials/sections/hero-inner.html` | `.hero--inner` | 1400 × 628 |

## Slider pagination hooks

| Slider | Hook | Partial |
| ------ | ---- | ------- |
| Gallery | `[data-gallery-pagination]` | `home-gallery.html` |
| Reviews | `[data-reviews-pagination]` | `home-reviews.html` |
| Specialists | `[data-specialists-pagination]` | `home-specialists.html` |

## Recovery intro text

Figma frame `2 - Дом - вступление` (`1:927`) — visible text nodes audited against `home-recovery-intro.html`. Primary heading/lead/card copy already matched visible Figma text; benefits list retained as operator HTML (not present as separate visible text nodes in audited frame).
