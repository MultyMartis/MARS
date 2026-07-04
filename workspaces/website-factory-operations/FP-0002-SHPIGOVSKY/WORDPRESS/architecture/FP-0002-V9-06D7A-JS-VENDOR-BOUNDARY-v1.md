# FP-0002 V9-06D7A JS Vendor Boundary v1

**Date:** 2026-07-04

## Enqueued in D7-A

| Handle | File | Behaviors active |
|--------|------|------------------|
| `shpigovsky-v9-shell` | `assets/js/v9-shell.js` | reveal, offcanvas, modal open/close, scroll-to-top |

## D7-A modifications to packaged JS

- Lead form `initLeadForm` not called in boot()
- `[data-lead-form]` submit events prevented (no AJAX, no fetch, no recaptcha load)

## Deferred vendors (documented, not enqueued)

| Vendor | V9 dist path | Reason |
|--------|--------------|--------|
| Swiper | `dist/assets/vendor/swiper/` | Home/service/reviews carousels — D7-B+ |
| Fancybox | `dist/assets/vendor/fancybox/` | Galleries/lightbox — D7-B+ |
| Inputmask | static CDN in V9 pages | Phone mask with forms — forms wave |

## Remote dependencies

None enqueued from theme in D7-A.

## Result

COMPLETE
