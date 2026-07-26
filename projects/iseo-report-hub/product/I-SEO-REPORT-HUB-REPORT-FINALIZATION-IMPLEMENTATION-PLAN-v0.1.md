# I-SEO Report Hub — Report Finalization Implementation Plan v0.1

**Status:** PLANNING ONLY — for next code wave; this charter wave does not implement  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Finalization Charter 01  
**Related:** [I-SEO-REPORT-HUB-REPORT-FINALIZATION-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-FINALIZATION-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-REPORT-FINALIZATION-DESIGN-v0.1.md](I-SEO-REPORT-HUB-REPORT-FINALIZATION-DESIGN-v0.1.md), [I-SEO-REPORT-HUB-REPORT-FINALIZATION-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-FINALIZATION-VALIDATION-PLAN-v0.1.md)

---

## 1. Next Wave Name

**I-SEO Report Hub — Report Finalization Implementation 01**

Goal: implement internal finalization transitions, readiness gates, parent/child locks, audit events, and UI cues — without public/PDF/snapshot layers.

---

## 2. Allowed App-Source Files (Next Wave)

Allowed touch set (exact paths under `projects/iseo-report-hub/app-source/`):

| Path | Role |
|------|------|
| `app/routes.php` | Explicit transition routes |
| `app/bootstrap.php` | DI wiring if needed |
| `app/Controllers/MonthlyReportContentController.php` | Action handlers + show readiness data |
| `app/Services/MonthlyReportContentService.php` | Cooperate with locks / transitions |
| `app/Repositories/MonthlyReportContentRepository.php` | Status/`finalized_at` + audit as needed |
| `app/Services/ReportFinalizationService.php` | **New** — readiness + finalize/reopen/submit/review |
| `app/Services/ReportBlockService.php` | Parent-finalized mutation guards |
| `app/Controllers/ReportBlockController.php` | Only if lock UX/messages need controller changes |
| `app/Services/ReportPreviewService.php` | Optional finalized metadata for views |
| `app/Controllers/ReportPreviewController.php` | Only if view model needs expansion |
| `app/Views/pages/monthly-reports/show.php` | Status card, checklist, buttons |
| `app/Views/pages/report-preview/show.php` | Finalization state cues |
| `app/Views/pages/report-preview/print.php` | Optional finalized label (print-safe) |
| `app/Views/pages/report-blocks/index.php` | Locked notice / disable create |
| `app/Views/pages/report-blocks/show.php` | Locked notice |
| `app/Views/pages/report-blocks/edit.php` | Locked / redirect messaging if needed |
| `app/Views/pages/report-blocks/create.php` | Locked / disable if needed |
| `public/assets/css/app.css` | Finalization / readiness / locked styles |
| `README.md` | Routes + policy notes |

Also allowed in Implementation 01 (docs, not app runtime):

- product result doc(s);
- closeout report;
- `OPERATIONAL-INDEX.md` updates.

**Not allowed without separate charter:** new migrations/SQL schema; auth/password changes; unrelated CRUD refactors; PDF/export/public share; demo workspace; registry.

---

## 3. DB Actions (Next Wave)

| Action | Policy |
|--------|--------|
| Schema / migrations | **None** |
| monthly_report_contents id **1** | Allowed: status + `finalized_at` via app transitions (LOCAL_FIXTURE_ONLY) |
| report_blocks under monthly **1** | Allowed: status prep to satisfy readiness via existing CRUD/service only |
| audit_log | Allowed: inserts for transition/readiness events |
| Other periods / clients / users | **No** |
| Real client data | **No** |

Target DB remains `iseo_report_hub_dev` @ `127.0.0.1` only.

Preferred final smoke state: monthly id **1** left **`finalized`** (locks demonstrable; later export/snapshot can build on it).

---

## 4. Runtime Sync Policy

Model A — source-first:

1. Implement in `app-source/`;
2. Exact-path allowlist sync source → `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\`;
3. Do **not** sync `.env` / `.env.local`;
4. No broad mirror copy;
5. No service restart unless proven required (prefer none);
6. Smoke against `http://iseo-report-hub.test/`.

---

## 5. Smoke List (Summary)

Full detail: validation plan. Minimum Implementation 01:

1. Preflight (root/volume/branch/index/WIP);
2. Readiness failure on current fixture (finalize blocked);
3. Prep required (+ present optional) blocks to `reviewed`/`approved` via LOCAL_FIXTURE_ONLY CRUD;
4. `submit-review` → `ready_for_review`;
5. `mark-reviewed` → `reviewed`;
6. `finalize` → `finalized` + `finalized_at` set;
7. Preview/print still auth 200;
8. Monthly edit blocked; block create/edit blocked;
9. `reopen` as admin_owner → edits allowed again;
10. Re-finalize or leave finalized — **prefer leave finalized**;
11. Audit events present;
12. Regression: periods/weekly/blocks list/preview/health/auth;
13. Confirm no public/PDF routes;
14. Commit exact-path; **push no**.

---

## 6. Commit Policy (Next Wave)

- Exact-path stage only (allowlisted source + docs);
- No `git add .` / `-A` / `commit -a`;
- Foreign WIP preserved;
- Commit and push are separate; default **push no** unless operator charter says otherwise;
- Suggested primary message pattern: `feat(iseo-report-hub): add report finalization workflow` (operator may refine).

This **charter** wave commits docs only:

`docs(iseo-report-hub): add report finalization charter`

---

## 7. STOP Conditions (Next Wave)

STOP if:

- wrong root / volume / branch;
- non-empty staged index unexpected;
- foreign or unexpected i-SEO WIP cannot be isolated;
- DB host/name mismatch;
- readiness gates skipped without documented override;
- schema migration attempted;
- public/PDF/export routes introduced;
- real client data used;
- push requested without charter;
- broad git ops required.

Output token pattern:

`STOP — I-SEO REPORT HUB REPORT FINALIZATION IMPLEMENTATION SAFETY CONDITION FAILED`
