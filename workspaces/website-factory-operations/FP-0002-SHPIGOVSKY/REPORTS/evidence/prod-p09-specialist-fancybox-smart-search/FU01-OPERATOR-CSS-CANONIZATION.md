# PROD-P09-FU01 — Operator CSS Drift Canonization

**Date:** 2026-08-14  
**Wave:** FP-0002 PROD-P09-FU01

## Required gate

```text
OPERATOR CSS DRIFT CANONIZED BEFORE FU01 IMPLEMENTATION
```

```text
OPERATOR CSS DRIFT PRESERVED AND CANONIZED
```

## Drift found

| File | Drift | Action |
|------|-------|--------|
| `assets/css/fp02-search.css` | **YES** | Canonized production → local before FU01 edits |
| `assets/css/v9-style.css` | **YES** | Canonized production → local (not uploaded in FU01) |
| `assets/js/v9-shell.js` | NO | MATCH at wave start |
| `searchform.php` | NO | MATCH |
| `search-panel.php` | NO | MATCH |
| `offcanvas.php` | NO | MATCH at wave start (later FU01 markup change) |

## Operator edits in `fp02-search.css` (preserved)

Compared local P09 canonical vs production-before:

- `.site-search-suggest { margin-top: 16px → 30px }`
- `.site-search-suggest` `border-top` commented out
- `.site-search-suggest` `padding-top` commented out

These edits were treated as authoritative and kept through FU01 mobile CSS additions.

## Operator edits in `v9-style.css`

Unrelated layout tweaks (program CTA spacing, founder quote, uslugi intro, etc.). Canonized into local source so future deploys cannot overwrite production. **Not** part of FU01 upload set.

## Evidence artifacts

- `FU01-OPERATOR-CSS-DRIFT-BEFORE.json`
- `FU01-OPERATOR-CSS-CANONIZATION.json`
- `fu01-diffs/*.local-vs-prod.diff`
- `fu01-local-pre-canon/` (local bytes before overwrite)
- Rollback snapshots: `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p09-fu01-layer-b-pre\`
