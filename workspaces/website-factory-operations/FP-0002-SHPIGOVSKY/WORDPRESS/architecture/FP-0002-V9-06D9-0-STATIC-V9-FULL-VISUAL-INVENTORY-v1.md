# FP-0002 V9-06D9-0 Static V9 Full Visual Inventory v1

**Date:** 2026-07-05  
**Task:** V9-06D9-0 Full V9 Visual Port Charter  
**Evidence:** `validation/v9-06d9-0-full-visual-port-charter/static-v9-full-visual-inventory.json`

## Authority

| Role | Path |
|------|------|
| Static visual authority | `workspaces/fp-0002-shpigovsky-v9/dist/` |
| Static source authority | `workspaces/fp-0002-shpigovsky-v9/src/` |

## Global shell (14 items)

| Item | Static source | Selector | WP present | State | Repair category |
|------|---------------|----------|:----------:|-------|-----------------|
| Header root | `layout/header.html` | `header.site-header` | yes | partial | HEADER_STRUCTURE_NOT_PORTED |
| Header top line | `layout/header.html` | `.site-header__top` | yes | partial | ACF_NOT_SEEDED |
| Desktop messengers | `layout/header.html` | `.site-header__messengers` | no | missing | ACF_NOT_SEEDED |
| Mobile messengers | `layout/header.html` | `.mobile-header__messengers` | no | missing | ACF_NOT_SEEDED |
| Callback button | `layout/header.html` | `.site-header__btns-wrap .btn` | yes | present | — |
| Search | `layout/header.html` | `.site-header__search` | yes | present | — |
| Primary nav | `layout/header.html` | `.site-header__nav-list` | yes | degraded | WP_MENU_DATA_MISSING |
| Offcanvas | `layout/header.html` | `.offcanvas` | yes | partial | ACF_NOT_SEEDED |
| Footer | `layout/footer.html` | `footer.site-footer` | yes | partial | ACF_NOT_SEEDED |
| Global modal | `global-consultation-modal.html` | `[data-modal]` | yes | present | — |
| Inter fonts | `assets/fonts/inter/` | `@font-face` | yes | broken | FONT_PATH_NOT_REWRITTEN |
| Swiper vendor | `assets/vendor/swiper/` | `.swiper` | no | missing | VENDOR_ASSET_NOT_ENQUEUED |
| Fancybox vendor | `assets/vendor/fancybox/` | `[data-fancybox]` | no | missing | VENDOR_ASSET_NOT_ENQUEUED |
| Inputmask | CDN | form inputs | no | missing | VENDOR_ASSET_NOT_ENQUEUED |

## Home sections (20)

Static Home (`src/pages/index.html`) includes 20 sections in order. See evidence JSON for per-section assets, JS dependencies, and repair categories.

**Summary:** 20 static sections → 6 visible on WP runtime (D9-A confirmed).

## Secondary pages (reference)

| Page | Static page | Section count (approx) | WP template status |
|------|-------------|------------------------:|-------------------|
| Services Hub | `uslugi-v2.html` | 9 major blocks | Partial — D7-C MVP |
| Service leaf | `usluga-konechnaya-v1.html` | 15+ blocks | Partial — D7-D |
| Service subdivision | `usluga-podrazdel-v1.html` | 10+ blocks | Partial |
| Contacts | `kontakty.html` | 3 blocks | Partial — D7-E |

## Result

Static inventory complete. Full visual port scope documented.
