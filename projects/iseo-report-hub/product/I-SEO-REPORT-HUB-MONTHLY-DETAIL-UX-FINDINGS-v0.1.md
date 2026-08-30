# i-SEO Report Hub — Monthly Report Detail UX Findings v0.1

**Wave:** Monthly Report Detail UX Collapse Charter 01  
**Date:** 2026-08-21  
**Route:** `GET /monthly-reports/1`  
**Scope:** documentation / UX findings only — **no** implementation

---

## Evidence

| Role | Path |
|------|------|
| Primary screenshot | `X:\AI MARS STORAGE\incoming\iseo-report-hub\screenshot-qa-p0-fix-implementation-01\20260821-023143\04_monthly_report_1_detail_after.png` |
| P0 after index | `X:\AI MARS STORAGE\incoming\iseo-report-hub\screenshot-qa-p0-fix-implementation-01\20260821-023143\P0-FIX-SCREENSHOT-INDEX.md` |
| P0 assertions | `X:\AI MARS STORAGE\incoming\iseo-report-hub\screenshot-qa-p0-fix-implementation-01\20260821-023143\P0-FIX-ASSERTIONS.md` |
| Source view (read-only) | `projects/iseo-report-hub/app-source/app/Views/pages/monthly-reports/show.php` |
| Work entries partial | `projects/iseo-report-hub/app-source/app/Views/partials/monthly-work-entries.php` |

P0 baseline accepted: `SCREENSHOT QA P0 FIX PASS_WITH_MINOR_ISSUES`. Fixture markers cleaned on normal-visible surfaces; residuals may remain in edit-form note textareas and collapsed technical details only.

---

## Current positives

1. **Complete operational surface** — status, finalization, snapshot, period context, details, source weekly notes, work entries, content fields, and report blocks all exist on one page.
2. **Actions exist** — navigation to period, weekly notes, blocks, preview; work-entry create/edit; assembly preview; snapshot/exports when applicable; finalization POST actions when allowed.
3. **P0 markers cleaned** — normal-visible `LOCAL_FIXTURE_ONLY` / `MARS_FIXTURE` and bad demo strings are hidden/replaced after P0.
4. **Work entries are present** — counters, cards, add/edit affordances, and related workflow buttons live in `monthly-work-entries` partial (`#work-entries`).
5. **Client preview and assembly routes exist** — `/monthly-reports/{id}/preview`, `/assembly-preview`, blocks list, snapshot/exports pages remain available without redesigning backend.

---

## Current problems

1. **Technical diagnostics dominate the first screen** — finalization card + readiness checklist + status-changing actions appear above the manager’s primary work area.
2. **Page is too long** — multiple full panels stack vertically; manager must scroll past diagnostics, snapshot, period, details, and source notes before reaching work entries.
3. **No clear manager workflow hierarchy** — top header buttons and work-entry action row both compete; primary vs secondary vs danger actions are not stratified.
4. **Panels compete for attention** — finalization, snapshot, details, source weekly notes, content summary, and report blocks table all present at similar visual weight.
5. **Technical details need stronger collapse** — some `<details>` already exist (snapshot/report tech), but readiness checklist, source notes, dense blocks table, and admin timestamps remain open by default.
6. **Status-changing / dangerous actions need clearer grouping** — submit-review / mark-reviewed / finalize / reopen sit in the same early “Действия” zone as ordinary workflow navigation; snapshot create POST is also mid-page.

---

## Operator question the page fails to answer quickly

On first screen, a manager should instantly know:

- What is the report state?
- What should I check next?
- Where do I edit work?
- Where do I assemble preview?
- Where do I view client preview?
- Where are files / shares?

Today those answers exist, but they are buried under diagnostics and duplicated across sections.

---

## Implication for next wave

Keep all data and actions. Reorganize presentation only: manager summary + primary workflow up top; work entries central; diagnostics and status-changing actions collapsed or visually separated. See Target IA, Collapse Policy, Action Safety UX, Implementation Scope, and Acceptance docs in this charter pack.

---

## Out of scope for findings wave

- App-source / runtime / DB / export / share / PDF mutation
- PDF regeneration or export 4 changes
- New routes (unless later implementation proves absolute need — default: keep `/monthly-reports/{id}`)
