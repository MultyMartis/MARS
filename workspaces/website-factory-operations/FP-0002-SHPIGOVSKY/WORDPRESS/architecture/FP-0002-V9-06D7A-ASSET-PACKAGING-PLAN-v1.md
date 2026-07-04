# FP-0002 V9-06D7A Asset Packaging Plan v1

**Date:** 2026-07-04  
**Task:** V9-06D7-A global shell asset source integration

## Source authority

| Role | Path |
|------|------|
| V9 compiled CSS | `workspaces/fp-0002-shpigovsky-v9/dist/assets/css/style.css` |
| V9 compiled JS (shell base) | `workspaces/fp-0002-shpigovsky-v9/dist/assets/js/main.js` |
| Theme destination | `WORDPRESS/theme/shpigovsky/assets/` |

## Packaged for D7-A

| Asset class | Source | Destination | Enqueued |
|-------------|--------|-------------|----------|
| Global CSS | `dist/assets/css/style.css` | `assets/css/v9-style.css` | Yes (`shpigovsky-v9`) |
| Shell JS | `dist/assets/js/main.js` | `assets/js/v9-shell.js` | Yes (`shpigovsky-v9-shell`) |
| Inter fonts | `dist/assets/fonts/inter/*` | `assets/fonts/inter/*` | No (referenced by CSS) |
| Font Awesome webfonts | `dist/assets/webfonts/*` | `assets/webfonts/*` | No (referenced by CSS) |
| Logo | `dist/assets/img/branding/logo.svg` | `assets/img/branding/logo.svg` | No (markup) |
| Social icons | `dist/assets/img/social/*` | `assets/img/social/*` | No (markup) |

## Path rewrite rule

Copied CSS absolute URLs `/assets/...` rewritten to relative `../...` so WordPress theme enqueue resolves correctly.

## Not packaged in D7-A

- Swiper / Fancybox vendor bundles (deferred)
- Page content images (home/service waves)
- Favicon bundle (optional later; WP head defers to theme/plugin)

## Manifest

`validation/v9-06d7a-global-shell-asset-source/asset-package-manifest.json` — 374 file entries with SHA-256.

## Result

COMPLETE
