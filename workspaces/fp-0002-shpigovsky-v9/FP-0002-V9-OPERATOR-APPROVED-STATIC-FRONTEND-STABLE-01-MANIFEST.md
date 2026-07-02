# FP-0002 V9 Operator-Approved Static Frontend Stable-01 Manifest

**Baseline ID:** `FP-0002-V9-OPERATOR-APPROVED-STATIC-FRONTEND-STABLE-01`  
**Operator status:** `FP0002_V9_03G_SCROLL_TO_TOP_OPERATOR_APPROVED`  
**Date:** 2026-07-02

## Baseline identity

| Field | Value |
|-------|-------|
| Workspace | `workspaces/fp-0002-shpigovsky-v9/` |
| Routes | 31 clean-route static pages |
| Full pages | 9 |
| Placeholders | 18 |
| Legal demo docs | 4 |
| Git tag (expected) | `fp-0002-v9-operator-approved-static-frontend-stable-01` |
| Parent HEAD | `5e7c86db73398df6a01074a60af3afa796de41b3` |

## Operator approval scope

- V9 clean-route static architecture
- Shared components and responsive behavior
- Section reveal animations; color-only button hover
- Gallery/Fancybox and modal/form animation
- Triumph-derived consultation modal runtime + Shpigovsky visual design
- Semitransparent modal overlay; stable background on open/close
- O-Centre G6 permanently removed
- Preloader and global page-load fade permanently removed
- Scroll-to-top after `scrollY > 500`
- Reduced-motion behavior; desktop and mobile approved

## Included paths

- Full V9 workspace (src, dist, tools, foundation, audits, docs)
- Package/build configuration
- Route manifest `tools/v9-route-manifest.json`

## Excluded paths

- `node_modules/`, caches, preview PID files
- Storage evidence trees
- V8, Triumph, unrelated workspaces

## Build commands

```bash
cd workspaces/fp-0002-shpigovsky-v9
npm install
npm run build
npm run validate
npm run preview
```

## Validation commands

- `npm run validate`
- Runtime smoke via `tools/v9-preview-server.mjs`

## Hash freeze (post clean build)

| Artifact | SHA-256 |
|----------|---------|
| CSS `dist/assets/css/style.css` | `F89FCB86A678C5FB4D4A94DB2E423095A23564B6C3BE19D7E39CF5AF0D30ABDE` |
| JS `dist/assets/js/main.js` | `19518C4BF86FBDA4FD5128D67EF00CBF7A2BDC6000A571B65D75BFA6AF27DB8A` |
| Source tree | `8C52CE697D994DA44632FB8B9623CCF073E512444D80797D61E8CB0176498B1B` |
| Dist tree | `AC15B53F9F2B18F02B6897568618FFB6376D508FF0F9AD6C60FF439A1CE30CCB` |
| Backup ZIP | `2FED546105F615650036F6E920E9B68BF63FDEEF383B18DED327F3DB49394F6D` |

## Production blockers

- `[ДЕМО: ...]` tokens on legal pages (23 total across 4 docs)
- Placeholder service/institutional pages
- No form backend; no cookie consent banner
- Genotyping route not published

## Restore guidance

1. Checkout tag `fp-0002-v9-operator-approved-static-frontend-stable-01`
2. Or restore ZIP: `X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v9\v9-03-stable-baseline-checkpoint\snapshot-operator-approved-v9-03g\FP-0002-V9-OPERATOR-APPROVED-STATIC-FRONTEND-STABLE-01.zip`
3. `npm install && npm run build && npm run validate`

## Forge handoff

V9 `src/` = implementation source; V9 `dist/` = rendered visual authority. Next phase: **V9-04 Forge WordPress Intake Pack** (not yet created).
