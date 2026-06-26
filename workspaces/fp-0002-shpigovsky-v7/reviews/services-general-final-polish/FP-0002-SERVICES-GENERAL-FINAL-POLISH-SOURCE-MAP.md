# FP-0002 — Services General Final Polish Source Map

**Date:** 2026-06-26  
**Pass 2 commit:** `d4fde896`  
**Authority:** PNG 26.06.2026 → `Spig_v1.2.fig` → scoped source

## Changed source (final polish)

| File | Scope | Change |
| ---- | ----- | ------ |
| `src/scss/style.scss` | `.page-uslugi`, `.services-category-hub*` | Hero overlay/readability, hub density, link emphasis, decor modifiers, compact hubs |
| `src/pages/uslugi.html` | Eating / genotyping hubs | `--compact` modifier classes |

## Unchanged (protected)

| File | Status |
| ---- | ------ |
| `src/pages/index.html` | unchanged |
| `src/partials/sections/home-*.html` | unchanged |
| `src/js/main.js` | unchanged |
| `src/partials/sections/hero-inner.html` | unchanged |
| `src/partials/sections/services-category-hub.html` | unchanged |

## Asset scope

| Asset | Status |
| ----- | ------ |
| `services-hero.webp` | preserved (Figma `1:1351`) |
| `services-addictions-0{1,2,3}.webp` | preserved |
| `services-mental-health-0{1,2,3}.webp` | preserved |
| `services-hub-decor.webp` | preserved (shared decor) |
| Probe exports `services-hub-*`, `*-decor.webp` duplicates | removed from `src/` |

## Review evidence

`workspaces/fp-0002-shpigovsky-v7/reviews/services-general-final-polish/`
