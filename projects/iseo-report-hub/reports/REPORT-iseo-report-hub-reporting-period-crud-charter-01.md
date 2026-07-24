# REPORT — I-SEO REPORT HUB REPORTING PERIOD CRUD CHARTER 01

**project_id:** `iseo-report-hub`  
**Wave:** Reporting Period CRUD Charter 01  
**Date:** 2026-07-25  
**Classification:** documentation / policy only  

---

## 1. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive | `X:` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD before | `1390a3850309ee5513463fdc98fdf93d69c79fb2` |
| Staged / index before | **empty** |
| i-SEO WIP before | **clean** (no modified/untracked under `projects/iseo-report-hub/`) |
| Foreign WIP | **preserved** (e.g. `projects/iseo-su-site-ops/**` and other unrelated paths untouched) |
| Write scope | Docs only under `projects/iseo-report-hub/product/`, `projects/iseo-report-hub/reports/`, `projects/iseo-report-hub/OPERATIONAL-INDEX.md` |

---

## 2. Baseline Reviewed

| Item | Value |
|------|-------|
| Fixture apply commit | `348b40896a86f5652ea8f7ba5ab5574ebc2abf2b` — `feat(iseo-report-hub): add local fixture bootstrap` |
| Fixture hash follow-up | `7c543116765a3a25630039a5c732c1884731b0fc` — `docs(iseo-report-hub): record local fixture bootstrap commit hash` |
| Auth baseline | `d4b3b2e2` + hash-record `0cd2cfb7`; local admin `admin@iseo-report-hub.test` |
| DB-03 apply | `c19c29b8` + hash-record `2f88d0ce`; migration batch **2**; table `reporting_periods` |
| DB | `iseo_report_hub_dev` @ `127.0.0.1` |
| Current counts (read-only) | migrations **2**; tables **10**; users **1**; roles **6**; clients/projects/sites/reporting_periods **1/1/1/1** |
| Demo fixture rows | client `Demo Client` / `demo-client`; project `Demo SEO Project` / `demo-seo-project`; site `https://demo.example.test`; period `2026-07` (`LOCAL_FIXTURE_ONLY`) |
| Current limitation | **No** reporting-period CRUD UI; no weekly/monthly content; no client portal; no real client data |

---

## 3. Charter Output

Created:

- `product/I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-CHARTER-v0.1.md`
- `product/I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-DESIGN-v0.1.md`
- `product/I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-IMPLEMENTATION-PLAN-v0.1.md`
- `product/I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-VALIDATION-PLAN-v0.1.md`
- `reports/REPORT-iseo-report-hub-reporting-period-crud-charter-01.md`

Updated:

- `OPERATIONAL-INDEX.md` — CRUD charter status; fixture baseline dependency; next implementation candidate; explicit no code/runtime/DB changes in charter

---

## 4. CRUD Design Summary

| Area | Decision |
|------|----------|
| Routes | GET list/detail/create/edit; POST create/update; auth required; CSRF on POST |
| Views | `pages/reporting-periods/index.php`, `show.php`, `form.php` |
| Service/controller | `ReportingPeriodController` + `ReportingPeriodService` (+ optional repository) |
| Access roles | admin/lead: full incl. finalize/archive; specialist: create/edit up to review, no finalize/archive; account: read + limited title/summary; internal_viewer: read-only; client_viewer: no access |
| Validation | project exists; `YYYY-MM`; dates ordered; key matches start month; status set; unique `(project_id, period_key)`; owner/reviewer internal if set |
| Audit | recommended: `reporting_period.created` / `.updated` / `.status_changed` |
| No-delete policy | No DELETE; archive via `status = archived` |
| Field locks | `period_key` only in `draft`; dates only in `draft`/`active`; `project_id` immutable after create |
| `finalized_at` | set on enter `finalized`; clear if leaving `finalized` |

---

## 5. Validation Plan

Documented for next wave:

- Route smoke (list/detail/create/edit + unauth deny)
- Form/CSRF smoke
- DB create (`2026-08` + `LOCAL_FIXTURE_ONLY`) / edit / archive
- Uniqueness + validation errors
- Auth/role (admin path required; multi-role partial if only one user)
- Audit (recommended)
- Regression: `/login`, dashboard, `/health`, `/not-existing`

---

## 6. Restrictions Confirmed

| Restriction | Confirmed |
|-------------|-----------|
| No app-source edits | Yes |
| No runtime edits | Yes |
| No DB mutation | Yes (read-only SELECT counts only) |
| No SQL/tool creation | Yes |
| No real client data | Yes |
| No fixture changes | Yes |
| No admin/password/hash changes | Yes |
| No env changes | Yes |
| No source sync | Yes |
| No service restart | Yes |
| No push/fetch/pull/reset/clean/stash | Yes |

---

## 7. Commit

| Item | Value |
|------|-------|
| Exact-path git add | Yes — allowlisted docs only |
| Commit message | `docs(iseo-report-hub): add reporting period crud charter` |
| Commit hash | `PENDING_PRIMARY_COMMIT_HASH` |
| Hash-record follow-up | `PENDING_HASH_RECORD_COMMIT_HASH` (report-only if needed) |
| Push | **no** |

---

## 8. SAFE UNKNOWN

- Whether HealthController HTML still shows expected tables as `9/9` vs `10/10` (overall `/health` remained ok after fixture; not re-audited HTML wording in this charter).
- Multi-role CRUD denial paths cannot be fully smoked until additional local users exist (only one admin user today).
- Exact audit transaction vs best-effort write strategy left to implementation detail within recommended events.

---

## 9. Recommended Next Action

**I-SEO Report Hub — Reporting Period CRUD Implementation 01**

---

## 10. Files Changed

- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-CHARTER-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-DESIGN-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-IMPLEMENTATION-PLAN-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-VALIDATION-PLAN-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-reporting-period-crud-charter-01.md`
- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`

---

## 11. Git Actions

| Action | Done? |
|--------|-------|
| exact-path git add | Yes (allowlisted docs) |
| commit | Yes (primary + optional hash-record) |
| push | **No** |
| fetch | **No** |
| pull | **No** |
| checkout | **No** |
| reset | **No** |
| restore | **No** |
| clean | **No** |
| stash | **No** |
