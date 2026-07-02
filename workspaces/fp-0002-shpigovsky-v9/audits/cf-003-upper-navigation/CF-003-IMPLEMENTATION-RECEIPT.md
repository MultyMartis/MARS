# CF-003 Implementation Receipt — Internal Upper Navigation

**Date:** 2026-06-28  
**Family:** CF-003  
**Wave:** V8 Shared Component Consolidation Wave 1  
**Status:** COMPLETE — build PASS, browser QA PASS, DOM PASS, selector PASS (2026-06-28)

---

## Canonical deliverable

| Item | Value |
|------|-------|
| Wrapper partial | `src/partials/components/internal-page-nav.html` |
| Class family | `.internal-page-nav` |
| CSS source | single block in `src/scss/style.scss` (CF-003 section) |
| Authority | Services Hub (`.page-uslugi-v2` pre-consolidation CSS) |

## Migrated pages

- `src/pages/uslugi-v2.html`
- `src/pages/usluga-podrazdel-v1.html`
- `src/pages/usluga-konechnaya-v1.html`

## Removed (no aliases retained)

- `.page-uslugi-v2__upper-nav`
- `.page-service-subdivision-v1__upper-nav`
- `.page-service-leaf-v1__upper-nav`
- Page-scoped `.breadcrumbs__*` / `.services-page-subnav__*` under page roots

## Source hash guard

- Pre: `audits/cf-003-upper-navigation/data/cf-003-source-hash-guard-pre.json`
- Post: `audits/cf-003-upper-navigation/data/cf-003-source-hash-guard-post.json`
- Protected file changes: **0**

## Backup

`C:\MARS Phenix\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\operator-checkpoints\FP-0002-V8-BEFORE-CF-003-UPPER-NAV-CONSOLIDATION.zip`

Manifest line: **FP-0002 V8 CF-003 PRE-CONSOLIDATION STATE PRESERVED**

## Build

`npm run build` — **succeeded** (2026-06-28)

## Completion evidence

- `CF-003-COMPLETION-RECEIPT.md`
- `data/CF-003-COMPLETION-BROWSER-QA.json`
- `data/CF-003-DOM-VALIDATION.json`
- `data/CF-003-FINAL-SELECTOR-VALIDATION.json`
- Screenshots (external): `C:\MARS Phenix\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\cf-003-evidence\completion\`

## Note

Leaf/subdivision visual delta vs pre-consolidation is **intentional** (Hub authority applied).
