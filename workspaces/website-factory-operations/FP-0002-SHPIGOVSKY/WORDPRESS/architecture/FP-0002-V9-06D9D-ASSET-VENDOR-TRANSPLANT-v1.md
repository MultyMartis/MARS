# FP-0002 V9-06D9D Asset Vendor Transplant v1

**Date:** 2026-07-05

## Summary

Copied required Home/footer assets from V9 `src/img`, `src/svg` and `dist/assets` into `theme/shpigovsky/assets/`:

- Gallery, comfort, specialists, articles, founder, staff, clinic, rehab images
- Hero `hero-main.png` (restored from D9-C git blob)
- Video posters and MP4 sources
- Vendor: Swiper, Fancybox bundles

Enqueue: `inc/home-vendors.php` on front page only; shell script deps updated.

## Evidence

`validation/v9-06d9d-home-main-footer-static-v9-transplant/asset-vendor-transplant-result.json`
