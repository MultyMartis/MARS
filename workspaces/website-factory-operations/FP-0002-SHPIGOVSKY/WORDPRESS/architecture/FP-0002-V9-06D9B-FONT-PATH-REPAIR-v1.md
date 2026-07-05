# FP-0002 V9-06D9-B Font Path Repair

**Date:** 2026-07-05

## Problem

`v9-style.css` retained static dist root-relative `@font-face` URLs (`/assets/fonts/inter/...`). WordPress serves theme CSS from `wp-content/themes/shpigovsky/assets/css/`, so browser requested `http://shpigovsky.test/assets/fonts/...` → 404.

Theme source `assets/fonts/inter/` contained `INTER-FONT-PROVENANCE.md` only — no WOFF2 binaries.

## Repair

1. Copied 6 Inter WOFF2 files from `workspaces/fp-0002-shpigovsky-v9/dist/assets/fonts/inter/`.
2. Rewrote 6 `@font-face` `src` URLs to `../fonts/inter/...` (theme-relative from CSS).

## Validation

All theme font URLs HTTP 200. Legacy root `/assets/fonts/` paths remain 404 but are no longer referenced by CSS.

Evidence: `validation/v9-06d9b-header-font-asset-messenger-repair/font-path-repair-result.json`
