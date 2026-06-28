# CF-003 Readiness Receipt — Upper Page Nav Band

**Date:** 2026-06-28  
**Family:** CF-003 — Upper page nav band (breadcrumbs + local subnav + container)  
**Implementation:** **COMPLETE** — see `audits/cf-003-upper-navigation/CF-003-IMPLEMENTATION-RECEIPT.md`

## Affected pages

| Template | Page |
|----------|------|
| Services Hub | `src/pages/uslugi-v2.html` |
| Service Subdivision | `src/pages/usluga-podrazdel-v1.html` |
| Service Leaf | `src/pages/usluga-konechnaya-v1.html` |

Home (`index.html`) does not use upper-nav wrapper — out of CF-003 scope.

## Canonical implementation (post Wave 1)

- Partial: `partials/components/internal-page-nav.html`
- Class family: `.internal-page-nav`
- CSS: single CF-003 block in `src/scss/style.scss`

## Legacy wrappers (removed)

- `.page-uslugi-v2__upper-nav`
- `.page-service-subdivision-v1__upper-nav`
- `.page-service-leaf-v1__upper-nav`

## Browser baseline evidence

Pre-consolidation captures remain under:

- `audits/bootstrap-reconciliation/V8-BASELINE-BROWSER-PARITY.json`
- External screenshots: `C:\MARS Phenix\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\parity-evidence\bootstrap-reconciliation\`

Post-consolidation completion QA: **PASS** — see `audits/cf-003-upper-navigation/CF-003-COMPLETION-RECEIPT.md` and `data/CF-003-COMPLETION-BROWSER-QA.json`.

## Gate

**COMPLETE** — ready for next shared component wave.
