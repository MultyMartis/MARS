# I-SEO Report Hub — Reporting Period CRUD Implementation Plan v0.1

**Status:** PLANNING ONLY — execute in next wave  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-25  
**Authority:** Operator I-SEO Report Hub Reporting Period CRUD Charter 01  
**Related:** [I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-DESIGN-v0.1.md](I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-DESIGN-v0.1.md), [I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-VALIDATION-PLAN-v0.1.md)

---

## 1. Next wave name

**`I-SEO Report Hub — Reporting Period CRUD Implementation 01`**

Purpose: implement the first internal CRUD UI/service for `reporting_periods` on local MVP (Model A source → runtime), using the existing demo fixture and auth baseline — without report content editor, client portal, schema changes, or hard delete.

---

## 2. Allowed app-source files next wave

| Path | Purpose |
|------|---------|
| `app-source/app/routes.php` | Register CRUD routes |
| `app-source/app/Controllers/ReportingPeriodController.php` | New controller |
| `app-source/app/Services/ReportingPeriodService.php` | Validation + workflow + audit orchestration |
| `app-source/app/Repositories/ReportingPeriodRepository.php` | Optional dedicated repository (or fold into service if simpler) |
| `app-source/app/Views/pages/reporting-periods/index.php` | List |
| `app-source/app/Views/pages/reporting-periods/show.php` | Detail |
| `app-source/app/Views/pages/reporting-periods/form.php` | Create/edit form |
| `app-source/app/Views/partials/header.php` | Nav link |
| `app-source/app/Controllers/DashboardController.php` | Card/status/link update |
| `app-source/app/Views/pages/dashboard.php` | Only if needed for link/card markup |
| `app-source/public/assets/css/*` (existing) | Minimal styles only if required |
| `app-source/public/assets/js/*` | Only if strictly needed (prefer none) |
| `product/` result doc(s) | Implementation result |
| `reports/` closeout | Implementation REPORT |
| `OPERATIONAL-INDEX.md` | Status update |

Also allowed if existing patterns require small wiring:

- `app-source/app/bootstrap.php` — only if DI/wiring of new service is required
- `app-source/app/Support/*` — only tiny shared helpers if unavoidable

**Not allowed without separate charter:**

- New migrations / SQL schema edits
- Auth core rewrite
- Weekly/monthly content tables/UI
- HealthController expected-table fix (unless operator expands charter)
- Client portal
- Fixture tool rewrite (reuse existing fixture; CRUD may INSERT second period)
- `.env` / `.env.local` edits
- Real client data import

---

## 3. Runtime sync

- Model A: after source changes, allowlist sync **source → runtime** for touched app files only.
- Runtime root: `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\`
- No wipe; no unrelated runtime edits.
- No Composer/npm.

---

## 4. DB actions allowed next wave

On `iseo_report_hub_dev` @ `127.0.0.1` only:

1. **INSERT** new `reporting_periods` rows via CRUD (smoke: e.g. `2026-08` with `LOCAL_FIXTURE_ONLY`).
2. **UPDATE** existing period rows (title/status/owner/reviewer/dates/key per locks).
3. **INSERT** optional `audit_log` events for create/update/status_changed.
4. **SELECT** joins for list/detail/forms.

---

## 5. DB actions not allowed

- Schema CREATE/ALTER/DROP
- New migration files for this feature
- DELETE of periods (including smoke cleanup) without separate destructive charter
- TRUNCATE / DROP tables
- Mutations to users/roles/passwords
- Mutations to clients/projects/sites except read
- Any non-local / production DB
- Real client data inserts

---

## 6. Smoke list

1. `php -l` on changed PHP files — PASS  
2. GET `/reporting-periods` (auth) — list shows fixture `2026-07`  
3. GET `/reporting-periods/1` — detail PASS  
4. GET `/reporting-periods/create` — form PASS  
5. POST create `2026-08` (CSRF) — row created; marked `LOCAL_FIXTURE_ONLY`  
6. POST duplicate `2026-08` — refused safely  
7. GET edit for new/fixture period — form PASS  
8. POST edit title/status — persisted  
9. Archive via status `archived` — PASS  
10. Role/read checks if practical (at least admin path; deny unauthenticated)  
11. `/health` 200; `/login` 200; `/not-existing` 404  
12. DB counts after: reporting_periods ≥ 2 if smoke create kept; clients/projects/sites remain fixture  
13. Audit events present if implemented  
14. No password/hash in output/docs  

Exact assertions live in the validation plan.

---

## 7. Commit policy

- Exact-path staging only (implementation charter allowlist)
- Never `git add .` / `-A` / `commit -a`
- Preserve foreign WIP
- Commit and push are **separate**; **no push** unless implementation charter explicitly authorizes
- Suggested primary message shape: `feat(iseo-report-hub): add reporting period crud`
- Docs hash-record follow-up if REPORT needs commit hash: `docs(iseo-report-hub): record reporting period crud commit hash`

---

## 8. STOP conditions

STOP and do not continue mutating if:

- Repo / volume / branch preflight fails
- Staged index non-empty unexpectedly
- DB is not exactly `iseo_report_hub_dev` @ `127.0.0.1`
- Fixture baseline absent (clients/projects/sites/periods not 1/1/1/1 before smoke create)
- Scope expands into weekly/monthly editor / client portal / DELETE / schema
- Secrets would be printed or committed
- Allowlisted staging cannot be guaranteed
- Source→runtime sync would touch unapproved paths

Output token if blocked:

`STOP — I-SEO REPORT HUB REPORTING PERIOD CRUD IMPLEMENTATION SAFETY CONDITION FAILED`

---

## 9. Suggested implementation order

1. Repository/service read paths + list/detail views  
2. Routes + auth gates + nav/dashboard link  
3. Create form + store + validation + unique handling  
4. Edit form + update + status/`finalized_at` policy  
5. Audit events  
6. Sync to runtime  
7. Smoke per validation plan  
8. Result docs + OPERATIONAL-INDEX + REPORT + scoped commit  

---

## 10. Exit criteria

- CRUD usable for local admin against demo fixture
- Validation plan PASS
- No schema drift
- No real client data
- Docs + index updated
- Exact-path commit(s) recorded; push deferred unless authorized
