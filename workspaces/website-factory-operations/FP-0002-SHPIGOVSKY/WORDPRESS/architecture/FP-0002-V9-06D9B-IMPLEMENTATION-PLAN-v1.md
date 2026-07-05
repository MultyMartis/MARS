# FP-0002 V9-06D9-B Implementation Plan

**Task:** V9-06D9-B Header / Font / Asset / Messenger Repair  
**Date:** 2026-07-05  
**HEAD gate:** `2d76cf9882a8283cfb014b8511b215361f032a7d`

## Objective

Restore global header/font/asset visual parity foundation: Inter font loading, messenger icon visibility, bounded runtime delivery.

## Source edits

| Change | File | Reason |
|--------|------|--------|
| Font path rewrite | `theme/shpigovsky/assets/css/v9-style.css` | Remove `/assets/fonts/` 404s |
| Font binaries | `theme/shpigovsky/assets/fonts/inter/*.woff2` | Theme had provenance only; copy from V9 dist |
| Messenger resolver | `theme/shpigovsky/inc/site-chrome.php` | Static V9 `#` fallback without options seed |
| Messenger partial | `theme/shpigovsky/template-parts/navigation/messenger-links.php` | Render fallback rows |

## Runtime delivery

Bounded copy of 10 files to:

1. **Active:** `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky\wp-content\themes\shpigovsky\`
2. **Charter path:** `...\app\public\wp-content\themes\shpigovsky\`

WordPress `ABSPATH` resolves to project root — active theme loads from (1).

## Out of scope (deferred)

- Primary nav mega-menu (D9-B2)
- Home hero/sections (D9-C/D9-D)
- Swiper/Fancybox enqueue (D9-F)
- DB / ACF / options / menu mutations

## Evidence

`validation/v9-06d9b-header-font-asset-messenger-repair/implementation-plan.json`
