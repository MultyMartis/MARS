# FP-0002 V9-06D9A Global Typography Asset Font Audit v1

**Date:** 2026-07-05  
**Evidence:** `validation/v9-06d9a-visual-parity-audit/global-typography-asset-font-audit.json`

## CSS bundles

| Surface | Stylesheets loaded | Status |
|---------|-------------------|--------|
| Static V9 | style.css, swiper-bundle.min.css, fancybox.css | all 200 |
| WP runtime | v9-style.css only | 200 |

Runtime does not enqueue Swiper/Fancybox vendor CSS required for gallery/modal parity.

## Font loading

| Metric | Static | Runtime |
|--------|--------|---------|
| Font requests | 11 | 10 |
| Failed | 0 | **5** |
| Failed URLs | — | `/assets/fonts/inter/inter-{300,400-latin,500,500-latin,300-latin}.woff2` |

Theme-relative font URLs (`/wp-content/themes/shpigovsky/assets/fonts/inter/inter-400.woff2`) return **200** but are **not referenced** by CSS.

## Key CSS variables (body computed)

| Token | Static | Runtime | Match |
|-------|--------|---------|------:|
| --font-family-base (computed) | Inter, system-ui… | Inter, system-ui… | yes |
| font-size | 18px | 18px | yes |
| font-weight | 300 | 300 | yes |
| line-height | 24px | 24px | yes |
| color | rgb(71, 83, 113) | rgb(71, 83, 113) | yes |
| -webkit-font-smoothing | antialiased | antialiased | yes |

## Image assets

- Static hero: `/assets/img/hero/hero-main.png` — 200 on static server
- Runtime hero image: not in DOM; theme path 404
- Gallery images: not seeded; not requested on runtime home

## Issue summary

Primary global parity defect is **font URL pathing** copied from static dist without WordPress theme URI rewrite. Secondary: missing vendor asset enqueue.

## Recommended repair

**D9-B** font path repair; **D9-E** vendor enqueue.

## Result

Global font/asset parity: **FAIL**
