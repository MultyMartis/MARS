# i-SEO Report Hub — Report 5 Draft Path Cleanup Implementation Scope v0.1

**Next wave name:** `I-SEO Report Hub — Report 5 Draft Path Cleanup Implementation 01`  
**Charter wave:** Report 5 Draft Path Cleanup Charter 01  
**Date:** 2026-08-21  
**Decision / target UX:** see sibling product docs in this pack

---

## Objective

Make report id **5** (and any similarly empty draft) look like an intentional **empty draft workspace**, not broken smoke debris — using **view/render-layer** changes only. Keep report **1** as the primary demo path. No DB mutation. No PDF/export/share mutation.

---

## Allowed

- View / render-layer changes only under Model A `projects/iseo-report-hub/app-source/`  
- Exact source → runtime sync of allowlisted files in the implementation wave  
- Reuse existing `UiTextSanitizer`, `ClientReportDocument`, `UiLabels`  
- Empty-state presentation improvements on:
  - monthly report detail when **0 blocks / 0 work entries** (draft)
  - client preview for empty draft (wording alignment if needed)
  - reporting period monthly-report card label/status demotion when empty draft
- CSS for empty-draft callout / demotion badge if needed  
- Display-only flags computed in controller **only if** view cannot already derive emptiness from passed counts (prefer view-side)

## Forbidden

- DB mutation (any table)  
- Seed / fixture create / SQL cleanup / delete report 5  
- Auto-create report blocks or work entries  
- Report 1 content/status mutation  
- POST apply / finalize / reopen / snapshot create during validation  
- Export / PDF / share mutation; no new export; no export 4 file change  
- Share create/revoke/token print  
- `.env` edits; package install; production; WordPress/i-seo.su/WPilot  
- Broad git ops / foreign WIP remediation  

---

## Likely files

| Path | Role |
|------|------|
| `app/Views/pages/monthly-reports/show.php` | Empty-draft top card / message / CTA emphasis |
| `app/Views/pages/reporting-periods/show.php` | Monthly card demotion label (`Пустой черновик` / `Черновик без работ`) |
| `app/Views/pages/reporting-periods/index.php` | Only if period-row copy needs light demotion (prefer show.php) |
| `app/Support/ClientReportDocument.php` | Preview empty/draft wording alignment if required |
| `app/Support/UiLabels.php` | Shared RU labels for empty-draft demotion |
| `app/Views/partials/monthly-work-entries.php` | Only if empty-state CTA alignment needed |
| `public/assets/css/app.css` | Empty-draft callout / demotion badge styles |
| Optional: `app/Controllers/MonthlyReportContentController.php` / `ReportingPeriodController.php` | Display-only emptiness flag — last resort |

**Do not** invent `MonthlyReportController.php` — monthly detail is `MonthlyReportContentController`.

---

## Implementation sequence (recommended)

1. Detect empty draft from block/entry counts + draft status (display-only)  
2. Add empty-draft framing on `/monthly-reports/{id}` top card  
3. Soften collapsed finalization summary copy for empty draft  
4. Demote label on `/reporting-periods/{id}` monthly card  
5. Confirm preview keeps calm section fallbacks + draft note  
6. CSS polish  
7. Validate (below)  
8. Recapture screenshots under Storage  

---

## Validation (implementation wave)

| Check | Expect |
|-------|--------|
| `GET /monthly-reports/5` | HTTP 200 |
| `GET /monthly-reports/5/preview` | HTTP 200 |
| `GET /reporting-periods` | HTTP 200 |
| `GET /reporting-periods/3` (or period owning report 5) | HTTP 200; empty-draft label visible |
| `GET /monthly-reports/1` | Unaffected manager demo (P1 still holds) |
| P0 forbidden strings | Absent on normal-visible surfaces |
| DB counts | Unchanged vs pre-impl baseline (report 5 still 0/0; report 1 still 6/7) |
| Export / share / PDF | Unchanged; export 4 size/checksum unchanged |
| Screenshot recapture | see below |

### Screenshot recapture (Storage only; not git)

Suggested filenames under a dated Storage folder for the impl wave:

- `14_monthly_report_5_empty_after_cleanup.png`  
- `15_monthly_report_5_preview_after_cleanup.png`  
- `03_reporting_periods_after_report5_cleanup.png`  
- optional: period show card screenshot for report 5 demotion  

---

## Deferred (explicit)

- Option C seed of blocks/work entries (separate data charter)  
- PDF/export HTML alignment and PDF regeneration  
- Export 4 overwrite / share mutation  
- Mobile-first redesign  
- Backend readiness rule changes  

---

## Entry criteria

- This charter pack accepted  
- P0 + P1 acceptance still stand  
- Operator confirms implementation wave start  

## Exit criteria

See [I-SEO-REPORT-HUB-REPORT-5-DRAFT-PATH-CLEANUP-SAFETY-ACCEPTANCE-v0.1.md](I-SEO-REPORT-HUB-REPORT-5-DRAFT-PATH-CLEANUP-SAFETY-ACCEPTANCE-v0.1.md).

---

## Next implementation prompt (operator paste)

```text
# MARS — I-SEO REPORT HUB REPORT 5 DRAFT PATH CLEANUP IMPLEMENTATION 01

Implement render/UX-only empty-draft cleanup for report id 5 per:
- projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-5-DRAFT-PATH-DECISION-v0.1.md
- projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-5-TARGET-EMPTY-DRAFT-UX-v0.1.md
- projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-5-DRAFT-PATH-CLEANUP-IMPLEMENTATION-SCOPE-v0.1.md
- projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-5-DRAFT-PATH-CLEANUP-SAFETY-ACCEPTANCE-v0.1.md

Hard restrictions: no DB mutation; no seed/delete; no export/share/PDF mutation; no report 1 regression; no production; no push unless asked; exact-path commits; preserve foreign WIP; use clean worktree if main index dirty.

Validate GET /monthly-reports/5, /monthly-reports/5/preview, /reporting-periods (+ period owning report 5), and /monthly-reports/1. Recapture Storage screenshots. Write implementation result + closeout + OPERATIONAL-INDEX update.
```
