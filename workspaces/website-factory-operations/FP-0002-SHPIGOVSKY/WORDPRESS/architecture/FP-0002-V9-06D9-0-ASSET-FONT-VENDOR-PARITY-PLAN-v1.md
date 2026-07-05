# FP-0002 V9-06D9-0 Asset Font Vendor Parity Plan v1

**Date:** 2026-07-05  
**Evidence:** `validation/v9-06d9-0-full-visual-port-charter/asset-font-vendor-parity-plan.json`

## Font parity (CRITICAL — global)

| Issue | Detail |
|-------|--------|
| Symptom | 5/10 Inter woff2 → HTTP 404 at `/assets/fonts/inter/*.woff2` |
| Root cause | `v9-style.css` `@font-face` uses static-dist absolute paths |
| Theme files | Exist at `assets/fonts/inter/` — HTTP 200 when URL is theme-relative |
| Fix | Rewrite URLs to `SHPIGOVSKY_THEME_URI` paths in source CSS pipeline |
| Weights | 300, 400, 500 + Cyrillic subsets |
| Wave | **D9-B** |

## CSS bundle parity

| Static | WP runtime | Action |
|--------|------------|--------|
| style.css | v9-style.css | OK (bundled) |
| swiper-bundle.min.css | missing | Enqueue D9-B/F |
| fancybox.css | missing | Enqueue D9-B/F |

## JS vendor parity

| Static | WP runtime | Action |
|--------|------------|--------|
| swiper-bundle.min.js | missing | Copy + enqueue |
| fancybox.umd.js | missing | Copy + enqueue |
| inputmask (CDN) | missing | Enqueue on forms |
| main.js modules | partial v9-shell.js | Port init D9-F |

## Image delivery targets

| Asset group | Delivery target | Wave |
|-------------|-----------------|------|
| Hero PNG | theme `assets/img/hero/` + media attachment | D9-C |
| Gallery / home content | media library or theme assets | D9-E |
| Social SVGs | theme assets (present) | D9-B |

## Cache / versioning

Retain `shpigovsky_asset_version()` filemtime after path fixes.

## Acceptance criteria

- All font network requests HTTP 200
- Swiper/Fancybox load on pages using sliders/lightbox
- Home screenshot density approaches static (~1.48 MB vs ~46 KB D9-A baseline)

## Result

Asset/font/vendor plan complete. Font repair required: **YES**.
