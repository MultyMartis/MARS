# I-SEO Report Hub — Weekly Checkpoints CRUD Implementation Plan v0.1

**Status:** PLANNING ONLY — execute in next wave  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-26  
**Authority:** Operator I-SEO Report Hub Weekly Checkpoints CRUD Charter 01  
**Related:** [I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-CHARTER-v0.1.md](I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-DESIGN-v0.1.md](I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-DESIGN-v0.1.md), [I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-VALIDATION-PLAN-v0.1.md)

---

## 1. Next wave name

**`I-SEO Report Hub — Weekly Checkpoints CRUD Implementation 01`**

Purpose: implement the first internal CRUD UI/service for `weekly_checkpoints` on local MVP (Model A source → runtime), using DB-04 table + fixture period `2026-07` + W1–W3 rows — without monthly editor, report blocks, client portal, schema changes, or hard delete.

---

## 2. Allowed app-source files next wave

| Path | Purpose |
|------|---------|
| `app-source/app/routes.php` | Register nested + flat weekly checkpoint routes |
| `app-source/app/bootstrap.php` | Require new classes if needed |
| `app-source/app/Controllers/WeeklyCheckpointController.php` | New controller |
| `app-source/app/Services/WeeklyCheckpointService.php` | Validation + workflow + audit |
| `app-source/app/Repositories/WeeklyCheckpointRepository.php` | Persistence |
| `app-source/app/Views/pages/weekly-checkpoints/index.php` | List |
| `app-source/app/Views/pages/weekly-checkpoints/show.php` | Detail |
| `app-source/app/Views/pages/weekly-checkpoints/form.php` | Shared form |
| `app-source/app/Views/pages/weekly-checkpoints/create.php` | Create wrapper |
| `app-source/app/Views/pages/weekly-checkpoints/edit.php` | Edit wrapper |
| `app-source/app/Views/pages/reporting-periods/show.php` | Parent period checkpoint section |
| `app-source/app/Views/partials/header.php` | Nav only if needed |
| `app-source/app/Controllers/DashboardController.php` | Card/link only if needed |
| `app-source/app/Views/pages/dashboard.php` | Only if needed |
| `app-source/public/assets/css/*` (existing) | Minimal styles / badges |
| `app-source/public/assets/js/*` | Only if strictly needed (prefer none) |
| `app-source/README.md` | Routes note if existing pattern requires |
| `product/` result doc(s) | Implementation result |
| `reports/` closeout | Implementation REPORT |
| `OPERATIONAL-INDEX.md` | Status update |

Also allowed if existing patterns require tiny wiring:

- `app-source/app/Support/*` — only unavoidable shared helpers
- Reuse of `ReportingPeriodRepository` / `ReportingPeriodService` for parent load (read-only from weekly wave perspective)

**Not allowed without separate charter:**

- New migrations / SQL schema edits
- Auth core rewrite / password/hash changes
- Monthly content tables/UI / report blocks
- Topvisor / API / n8n
- Client portal
- Fixture tool rewrite
- `.env` / `.env.local` edits
- Real client data import
- DELETE routes/UI
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

1. **INSERT** new `weekly_checkpoints` rows via CRUD (smoke: `2026-07-W4` with `LOCAL_FIXTURE_ONLY`).
2. **UPDATE** weekly checkpoint rows (fields/status per locks) — prefer W4 for edit/archive smoke.
3. **INSERT** optional `audit_log` events for create/update/status/reviewed/completed.
4. **SELECT** joins for list/detail/forms/parent context.

---

## 5. DB actions not allowed

- Schema CREATE/ALTER/DROP
- New migration files
- DELETE of weekly checkpoints (including smoke cleanup) without separate destructive charter
- TRUNCATE / DROP tables
- Mutations to users/roles/passwords
- Mutations to clients/projects/sites
- Mutations to `reporting_periods` rows (read-only parent context)
- Any non-local / production DB
- Real client data inserts

---

## 6. Smoke list

1. `php -l` on changed PHP files — PASS  
2. Auth GET list under period `2026-07` — shows W1/W2/W3  
3. Auth GET detail W1 — PASS  
4. Auth GET create form under period — PASS  
5. POST create W4 `2026-07-W4` (CSRF) — row created; `LOCAL_FIXTURE_ONLY`  
6. POST duplicate W4 — refused safely  
7. Auth GET/POST edit W4 title/status — persisted  
8. Mark W4 `skipped` or `archived` — PASS; row still exists  
9. Parent reporting period detail shows checkpoint section/links  
10. Unauthenticated weekly routes → `/login`  
11. `/health` 200; `/login` 200; `/not-existing` 404  
12. Reporting period list/detail regression PASS  
13. Audit events present if implemented  
14. Confirm **no** DELETE route/UI  
15. No password/hash in output/docs  

Exact assertions live in the validation plan.

---

## 7. Commit policy

- Exact-path staging only (implementation charter allowlist)
- Never `git add .` / `-A` / `commit -a`
- Preserve foreign WIP
- Commit and push are **separate**; **no push** unless implementation charter explicitly authorizes
- Suggested primary message: `feat(iseo-report-hub): add weekly checkpoints crud`
- Docs hash-record follow-up if REPORT needs commit hash: `docs(iseo-report-hub): record weekly checkpoints crud commit hash`
- Staged area must be empty before staging; only allowlisted paths may appear in `git diff --cached --name-only`

---

## 8. STOP conditions

STOP and do not proceed / do not commit if:

- Repo root / drive / volume / branch unsafe
- Staged index non-empty before start (or contains non-allowlist paths before commit)
- i-SEO foreign/unrelated WIP unexpectedly present in scope
- DB target ≠ `iseo_report_hub_dev` @ `127.0.0.1`
- DB-04 table missing or W1–W3 baseline unexpectedly destroyed
- Scope expands into monthly editor / blocks / portal / schema
- Credentials would be printed or committed
- Broad git add would be required
- Push requested without charter (default: no push)

Output token example:

`STOP — I-SEO WEEKLY CHECKPOINTS CRUD IMPLEMENTATION SAFETY CONDITION FAILED`
