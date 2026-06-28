# CF-006 Pre-Implementation Inventory — Comfort / Facility Gallery

**Date:** 2026-06-28
**Family:** `home-comfort` → target `comfort`
**Classification:** SHARED_BUT_PAGE_NAMED

## Consumer table

| Page | Include path | Root class | Items | Gallery hook | Group value | IDs/ARIA | Page scope |
|---|---|---:|---|---|---|---|---|
| index.html | partials/sections/home-comfort.html | `.home-comfort` | 7 (1 decor + 6 links) | `data-fancybox` | `home-comfort` | `aria-labelledby="home-comfort-heading"` | home |
| uslugi.html | partials/sections/home-comfort.html | `.home-comfort` | 7 | `data-fancybox` | `home-comfort` | `aria-labelledby="home-comfort-heading"` | services |
| uslugi-v2.html | partials/sections/home-comfort.html | `.home-comfort` | 7 | `data-fancybox` | `home-comfort` | `aria-labelledby="home-comfort-heading"` | services-v2 |
| usluga-podrazdel-v1.html | partials/sections/home-comfort.html | `.home-comfort` | 7 | `data-fancybox` | `home-comfort` | `id="service-subdivision-comfort"`, `aria-labelledby="service-subdivision-comfort-heading"` | service-subdivision |
| usluga-konechnaya-v1.html | partials/sections/home-comfort.html | `.home-comfort` | 7 | `data-fancybox` | `home-comfort` | `id="service-leaf-comfort"`, `aria-labelledby="service-leaf-comfort-heading"` | service-leaf |

## Summary

- **Total consumers:** 5
- **Inline copies:** 0
- **Duplicate partials:** 0 active (`services-comfort-v2.html` is separate family — excluded)
- **Duplicate CSS blocks:** 0 (single family block + shared compound selectors)
- **Duplicate JS initialization:** 0 (single Fancybox bind in `main.js`)
- **Page-specific wrappers:** 0
- **Visual variants:** 0
- **Content variants:** 0 (same partial, parameterized heading/section ids only)
- **Image-set variants:** 0
- **Gallery-group variants:** 0 (all use `home-comfort`)
- **Unresolved dependencies:** none

## Boundary check

| Related family | Partial | Pages | Visual relationship | Included in CF-006 |
|---|---|---:|---|---:|
| home-comfort | home-comfort.html | 5 | facility comfort gallery mosaic | YES |
| home-clinic-landscape | home-clinic-landscape.html | 3 | single bleed landscape image | NO |
| home-gallery | home-gallery.html | 1 | Swiper carousel with captions | NO |
| services-comfort-v2 | services-comfort-v2.html | 0 canonical | alternate v2 layout | NO |
| other image rows | various | — | distinct blocks | NO |

**Boundary decision:** CF-006 scope limited to `home-comfort` family only.

## Gallery mechanism

- **Library:** Fancybox (global `window.Fancybox`)
- **Init:** `initHomeComfortFancybox()` in `main.js`
- **Selector:** `[data-fancybox="home-comfort"]`
- **Config:** `groupAll: false`, `Carousel.infinite: false`, toolbar infobar + close

## Asset paths

- Images: `assets/img/content/home-comfort/*.webp` — **HISTORICAL_ASSET_PATH_PRESERVED**
- Decor logo: `assets/img/branding/logo.svg`
