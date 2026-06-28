# CF-003 Readiness Receipt — Upper Page Nav Band

**Date:** 2026-06-28  
**Family:** CF-003 — Upper page nav band (breadcrumbs + local subnav + container)  
**Implementation:** NOT PERFORMED

## Affected pages

| Template | Page |
|----------|------|
| Services Hub | `src/pages/uslugi-v2.html` |
| Service Subdivision | `src/pages/usluga-podrazdel-v1.html` |
| Service Leaf | `src/pages/usluga-konechnaya-v1.html` |

Home (`index.html`) does not use upper-nav wrapper — out of CF-003 scope.

## Current wrapper classes (DRIFT)

- `.page-uslugi-v2__upper-nav`
- `.page-service-subdivision-v1__upper-nav`
- `.page-service-leaf-v1__upper-nav`

## Shared partials (already identical includes)

- `partials/components/breadcrumbs.html`
- `partials/components/services-page-subnav.html`

## CSS drift (wrapper-only)

| Selector | Notes |
|----------|-------|
| `.page-uslugi-v2__upper-nav` | `gap: 15px`; padding 0 |
| `.page-service-subdivision-v1__upper-nav` | `gap: 15px`; padding 0 |
| `.page-service-leaf-v1__upper-nav` | `gap: 12px`; `padding-top: 16px`; `padding-bottom: 8px` |

## Responsive drift

Documented in `audits/component-family-audit-v8-bootstrap-01/FP-0002-V8-COMPONENT-FAMILY-AUDIT-v1.md` — wrapper spacing differs; shared partial responsive rules are common.

## Recommended authority candidates

- Partial target: `partials/components/page-upper-nav.html` (name TBD at implementation)
- Class family target: `.page-upper-nav*` (operator decision — **not chosen in this pass**)

## Browser baseline evidence

Available:

- `audits/bootstrap-reconciliation/V8-BASELINE-BROWSER-PARITY.json`
- `audits/bootstrap-reconciliation/V8-BROWSER-PARITY-MANIFEST.json`
- External screenshots: `C:\MARS Phenix\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\parity-evidence\bootstrap-reconciliation\`

## Rollback source

Bootstrap reconciliation commit on `mars/canonical-post-recovery` (this task).

## Gate

**READY** after bootstrap commit/push — awaiting operator approval before CF-003 implementation.
