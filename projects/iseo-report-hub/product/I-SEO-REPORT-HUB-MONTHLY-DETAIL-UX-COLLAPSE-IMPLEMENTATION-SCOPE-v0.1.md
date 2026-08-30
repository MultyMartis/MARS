# i-SEO Report Hub — Monthly Detail UX Collapse Implementation Scope v0.1

**Next wave name:** `I-SEO Report Hub — Monthly Report Detail UX Collapse Implementation 01`  
**Charter wave:** Monthly Report Detail UX Collapse Charter 01  
**Date:** 2026-08-21

---

## Objective

Reorganize `GET /monthly-reports/{id}` into a manager-friendly workspace per Target IA, Collapse Policy, and Action Safety UX — without changing data, routes (default), authorization, or delivery artifacts.

---

## Allowed

- Modify monthly report detail view markup/order  
- Modify work-entries / report-blocks partials if needed for hierarchy  
- Modify CSS for summary, action strips, collapsed panels, admin zone  
- Small helper/label tweaks **only if** required for compact readiness indicators (prefer existing `UiLabels` / sanitizer)  
- Model A source edits under `projects/iseo-report-hub/app-source/` then exact runtime sync in implementation wave  

## Forbidden

- DB mutation (any table)  
- POST finalization / reopen / snapshot / assembly-apply / work-entry writes during validation  
- Export / PDF / share mutation; no new export row; no export 4 file change  
- Share create/revoke/token print  
- Route renames unless absolutely required (default: keep `/monthly-reports/{id}`)  
- Package install; `.env` edits; production ops; WordPress/i-seo.su/WPilot mutation  
- Broad git operations / foreign WIP remediation  

---

## Likely files

| Path | Role |
|------|------|
| `app/Views/pages/monthly-reports/show.php` | Primary layout reorder + collapse wrappers |
| `app/Views/partials/monthly-work-entries.php` | Promote/simplify work-entries; reduce duplicate primary CTAs if needed |
| Report blocks markup in `show.php` (or partial if extracted) | Compact / collapse dense table |
| `public/assets/css/app.css` | Summary card, primary strip, admin zone, details styling |
| Optional: `app/Support/UiLabels.php` | Only if compact indicator labels missing |

Controller (`MonthlyReportController.php`) — **prefer no change**; pass-through data already sufficient. Touch only if view needs a tiny display flag already computable in view.

---

## Implementation sequence (recommended)

1. Introduce top summary card from existing report/period fields  
2. Add primary GET action strip  
3. Move work entries up  
4. Compact content summary  
5. Compact snapshot/export/share card; collapse tech  
6. Wrap readiness + status POSTs in collapsed/admin zone  
7. Collapse source notes / details / blocks table  
8. CSS polish; no new JS unless justified  
9. Validate (below)  
10. Recapture screenshot evidence  

---

## Validation (implementation wave)

| Check | Expect |
|-------|--------|
| `GET /monthly-reports/1` | HTTP 200 |
| P0 forbidden strings | Absent on normal-visible surfaces |
| Work entries | Visible / accessible (not collapsed away) |
| Primary actions | Visible near top |
| Diagnostics | Collapsed by default |
| DB counts | Unchanged vs pre-impl baseline |
| Export / share / PDF | Unchanged; export 4 checksum/size unchanged |
| Recapture | `04_monthly_report_1_detail_after_p1.png` (or dated Storage folder per impl charter) |

Optional GET: `/health`, preview, assembly-preview — read-only.

---

## Deferred (explicit)

- PDF/export HTML alignment and PDF regeneration  
- Export 4 overwrite  
- Share mutations  
- Report 5 deeper content pack  
- Mobile-first redesign  
- Backend state-machine changes  

---

## Entry criteria

- This charter pack accepted  
- P0 residual acceptance still stands  
- Operator confirms implementation wave start  

## Exit criteria

See [I-SEO-REPORT-HUB-MONTHLY-DETAIL-UX-COLLAPSE-ACCEPTANCE-v0.1.md](I-SEO-REPORT-HUB-MONTHLY-DETAIL-UX-COLLAPSE-ACCEPTANCE-v0.1.md).
