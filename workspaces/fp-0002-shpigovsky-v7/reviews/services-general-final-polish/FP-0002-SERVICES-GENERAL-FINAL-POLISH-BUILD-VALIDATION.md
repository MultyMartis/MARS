# FP-0002 — Services General Final Polish Build Validation

**Date:** 2026-06-26

## Build command

```text
npm run build
```

## Result

| Check | Result |
| ----- | ------ |
| `npm run build` (`cleanDist`) | **FAIL** — `EBUSY` on `dist/` rmdir (filesystem lock) |
| `gulp watch:dev` → `buildIncremental` | **PASS** — all pipeline tasks finished |
| SCSS compile | PASS |
| HTML includes | PASS |
| JS bundle | PASS |
| Services images in `src/` | PASS (8 finals) |
| Missing referenced assets | 0 |
| Source paths exposed in dist | 0 |
| PNG/Figma runtime refs | 0 |
| `dist/` committed | no |
| `node_modules/` committed | no |

## Dist artifacts verified

- `dist/index.html` — exists
- `dist/uslugi.html` — exists
- `dist/assets/css/style.css` — exists
- `dist/assets/js/main.js` — exists
- `dist/assets/img/content/services/` — referenced finals present

## Note

Stale probe WebP copies may remain in `dist/assets/img/content/services/` until a successful `cleanDist`; they are not referenced by HTML/CSS and are outside git scope.

## Build verdict

`PASS_WITH_CLEAN_DIST_ENVIRONMENT_CAVEAT` — incremental build validates all required outputs; canonical `npm run build` blocked by transient `dist/` lock on operator machine.
