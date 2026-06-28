# FP-0002 V8 — Operator Manual Polish Inventory v1

**Date:** 2026-06-29  
**HEAD at inventory:** `2de6bafab4ca80f2e1bf641468f0b973c4c21282`  
**CF-012 commit:** `9e8fa083cf957e0b05a212db88165709bd488e8b`  
**JSON:** `data/FP-0002-V8-OPERATOR-MANUAL-POLISH-INVENTORY.json`

## Operator decision

Post-CF-012 operator manual polish via Gulp watcher is accepted as the new canonical V8 source-state. Changes are preserved verbatim; no regression comparison against CF-012 before/after screenshots.

---

## Inventory table

| File | Status | Source/runtime | Change type | Operator canonical | Commit eligible |
|---|---|---|---|---:|---:|
| `src/scss/style.scss` | modified | source | SCSS declarations, selectors, media queries | yes | yes |
| `src/favicon/favicon.svg` | modified | source | asset replacement (Xara export) | yes | yes |
| `src/pages/*.html` | unchanged vs HEAD | source | none unstaged | yes (committed) | no |
| `src/partials/**` | unchanged vs HEAD | source | none unstaged | yes (committed) | no |
| `src/js/main.js` | unchanged | source | none | yes | no |
| `audits/consolidation-checkpoint/data/*.json` | modified | runtime | metadata timestamp only | no | no |
| `dist/**` | generated | runtime | build output | no | no |
| `workspaces/fp-0002-shpigovsky-v7/**` | modified | unrelated WIP | V7 evidence drift | no | no |
| `projects/ocpilot/sites/site-002/**` | modified | unrelated WIP | SITE-002 report | no | no |

---

## A. V8 source changes (operator manual polish)

### `src/scss/style.scss`

- **Declarations changed:** mobile `:root` typography tokens (`--pad-y`, `--font-size-h1/h2/h3`, line-heights); container `max-width` 1400→1460px; container horizontal padding; reviews card hover border; comfort lead max-width; founder-quote layout grid and photo max-height; hero panel padding; services-inner-hero-v2 media sizing; internal-page-nav mobile rules commented out; service-leaf approach cards border-color; assorted responsive breakpoint adjustments.
- **Selectors changed:** `.reviews__card:hover`, `.comfort__lead`, `.founder-quote__layout`, `.founder-quote--variant-b .founder-quote__photo`, `.hero__panel`, `.services-inner-hero-v2__container`, `.services-inner-hero-v2__media`, `.page-service-leaf-v1 .service-leaf-approach-v1__approach-cards`, internal-page-nav mobile selectors (commented).
- **Net diff:** +196 / −110 lines.

### `src/favicon/favicon.svg`

- **Asset changed:** replaced simplified SVG with Xara Designer export; preserved brand gradient and red cross motif.

### HTML / partials / JS

- **No unstaged diff** vs HEAD for pages, partials, or `main.js`.
- Operator watcher HTML state matches committed CF-011/CF-012 markup; canonical HTML authority = committed HEAD.

---

## B. Generated / runtime (excluded from commit)

- `dist/` — rebuilt by `npm run build`
- Consolidation audit JSON — metadata-only drift (UNRESOLVED, not staged)
- Watcher session receipt — `MARS STORAGE/.../runtime/FP-0002-V8-GULP-WATCH-SESSION.json` (STOPPED)
- Screenshot evidence — `MARS STORAGE/.../operator-manual-polish-evidence/`

---

## C. Unrelated repository WIP (excluded)

- V7: `package-lock.json`, pass-3 navigation evidence files
- SITE-002: warranty implementation report
- Corvonero, recovery temp, Figma imports, `.tools/` — untracked, excluded

---

## Cursor source changes

**0** — no HTML/SCSS/JS edits by this checkpoint task.
