# I-SEO Report Hub — Monthly Report Content CRUD Implementation Plan v0.1

**Status:** PLANNING ONLY — execute in next wave  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-26  
**Authority:** Operator I-SEO Report Hub Monthly Report Content CRUD Charter 01  
**Related:** [I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-CHARTER-v0.1.md](I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-DESIGN-v0.1.md](I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-DESIGN-v0.1.md), [I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-VALIDATION-PLAN-v0.1.md)

---

## 1. Next wave name

**`I-SEO Report Hub — Monthly Report Content CRUD Implementation 01`**

Purpose: implement the first internal CRUD/editor for `monthly_report_contents` on local MVP (Model A source → runtime), using DB-05 table + fixture period `2026-07` + monthly demo id **1** + W1–W4 source references — without report blocks, PDF/export, client portal, schema changes, or hard delete.

---

## 2. Allowed app-source files next wave

| Path | Purpose |
|------|---------|
| `app-source/app/routes.php` | Register nested period monthly-report + flat monthly-report routes |
| `app-source/app/bootstrap.php` | Require new classes if needed |
| `app-source/app/Controllers/MonthlyReportContentController.php` | New controller |
| `app-source/app/Services/MonthlyReportContentService.php` | Validation + workflow + audit |
| `app-source/app/Repositories/MonthlyReportContentRepository.php` | Persistence |
| `app-source/app/Views/pages/monthly-reports/show.php` | Detail |
| `app-source/app/Views/pages/monthly-reports/form.php` | Shared form |
| `app-source/app/Views/pages/monthly-reports/create.php` | Create wrapper |
| `app-source/app/Views/pages/monthly-reports/edit.php` | Edit wrapper |
| optional `app-source/app/Views/pages/monthly-reports/index.php` | Only if top-level index implemented |
| `app-source/app/Views/pages/reporting-periods/show.php` | Parent period monthly report section |
| `app-source/app/Views/partials/header.php` | Nav only if needed |
| `app-source/app/Controllers/DashboardController.php` | Card/count only if needed |
| `app-source/app/Views/pages/dashboard.php` | Only if needed |
| `app-source/public/assets/css/*` (existing) | Minimal styles / badges |
| `app-source/public/assets/js/*` | Only if strictly needed (prefer none) |
| `app-source/README.md` | Routes note if existing pattern requires |
| `product/` result doc(s) | Implementation result |
| `reports/` closeout | Implementation REPORT |
| `OPERATIONAL-INDEX.md` | Status update |

Also allowed if existing patterns require tiny wiring:

- `app-source/app/Support/*` — only unavoidable shared helpers
- Reuse of `ReportingPeriodRepository` / `WeeklyCheckpointRepository` for parent/source load (read-only from monthly wave perspective)

**Not allowed without separate charter:**

- New migrations / SQL schema edits
- Auth core rewrite / password/hash changes
- Report blocks tables/UI / PDF/export
- Topvisor / API / n8n
- Client portal
- Fixture tool rewrite
- `.env` / `.env.local` edits
- Real client data import
- DELETE routes/UI
- Mutations to `weekly_checkpoints` or `reporting_periods` rows (except reading)
- HealthController expected-table wording fix (unless operator expands charter)

---

## 3. Runtime sync policy

- Model A: after source changes, allowlist sync **source → runtime** for touched app files only.
- Runtime root: `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\`
- No wipe; no unrelated runtime edits.
- No Composer/npm.
- No tools/migrations sync unless a file in the allowlist was intentionally changed (it should not be).

---

## 4. DB actions allowed next wave

On `iseo_report_hub_dev` @ `127.0.0.1` only:

1. **UPDATE** existing `monthly_report_contents` rows via CRUD (smoke: prefer id **1** for `2026-07`).
2. **INSERT** a monthly row only when create-if-missing is exercised on a period that truly has none — document resulting row; prefer **not** creating a second period row unless operator expands smoke.
3. **INSERT** optional `audit_log` events for create/update/status/reviewed/finalized/archived.
4. **SELECT** joins for detail/forms/parent context/source checkpoints.

---

## 5. DB actions not allowed

- Schema CREATE/ALTER/DROP
- New migration files
- DELETE of monthly report contents (including smoke cleanup) without separate destructive charter
- TRUNCATE / DROP tables
- Mutations to users/roles/passwords
- Mutations to clients/projects/sites
- Mutations to `reporting_periods` rows
- Mutations to `weekly_checkpoints` rows
- Any non-local / production DB
- Real client data inserts

---

## 6. Smoke list

1. `php -l` on changed PHP files — PASS  
2. Auth GET `/reporting-periods/1/monthly-report` — shows demo monthly id **1**  
3. Auth GET `/monthly-reports/1` — PASS; parent + source links  
4. Auth GET edit form `/monthly-reports/1/edit` — PASS  
5. POST update title/content/status → `in_progress` (CSRF) — persisted; `LOCAL_FIXTURE_ONLY` retained  
6. POST duplicate create for period `2026-07` — refused safely; count remains **1** (or documented)  
7. Invalid `source_weekly_checkpoint_ids` — refused  
8. Source weekly checkpoint links shown on detail  
9. Optional: status → `ready_for_review` if field-lock smoke still safe; else keep `in_progress` and document  
10. Parent reporting period detail shows monthly report section  
11. Unauthenticated monthly routes → `/login`  
12. `/health` 200; `/login` 200; `/not-existing` 404  
13. Reporting period CRUD + weekly checkpoint CRUD regression PASS  
14. Audit events present if implemented  
15. Confirm **no** DELETE route/UI  
16. No password/hash in output/docs  

Exact assertions live in the validation plan.

---

## 7. Commit policy

- Exact-path staging only (implementation charter allowlist)
- Never `git add .` / `-A` / `commit -a`
- Preserve foreign WIP
- Commit and push are **separate**; **no push** unless implementation charter explicitly authorizes
- Suggested primary message: `feat(iseo-report-hub): add monthly report content crud`
- Docs hash-record follow-up if REPORT needs commit hash: `docs(iseo-report-hub): record monthly report content crud commit hash`
- Staged area must be empty before staging; only allowlisted paths may appear in `git diff --cached --name-only`

---

## 8. STOP conditions

STOP and do not proceed / do not commit if:

- Repo root / drive / volume / branch unsafe
- Staged index non-empty before start (or contains non-allowlist paths before commit)
- i-SEO foreign/unrelated WIP unexpectedly present in scope
- DB target ≠ `iseo_report_hub_dev` @ `127.0.0.1`
- DB-05 table missing or demo monthly baseline unexpectedly destroyed
- Scope expands into report blocks / PDF / portal / Topvisor / schema
- Credentials would be printed or committed
- Broad git add would be required
- Push requested without charter (default: no push)

Output token example:

`STOP — I-SEO MONTHLY REPORT CONTENT CRUD IMPLEMENTATION SAFETY CONDITION FAILED`
