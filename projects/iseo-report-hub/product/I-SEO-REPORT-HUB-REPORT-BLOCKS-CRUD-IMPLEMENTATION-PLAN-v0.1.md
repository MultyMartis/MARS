# I-SEO Report Hub — Report Blocks CRUD Implementation Plan v0.1

**Status:** PLANNING ONLY — execute in next wave  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-26  
**Authority:** Operator I-SEO Report Hub Report Blocks CRUD Charter 01  
**Related:** [I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-DESIGN-v0.1.md](I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-DESIGN-v0.1.md), [I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-VALIDATION-PLAN-v0.1.md)

---

## 1. Next wave name

**`I-SEO Report Hub — Report Blocks CRUD Implementation 01`**

Purpose: implement the first internal CRUD/editor for `report_blocks` on local MVP (Model A source → runtime), using DB-06 table + monthly demo id **1** / period `2026-07` + 5 fixture blocks (+ optional additional `risks_and_blockers`) — without drag/drop, PDF/export, client portal, schema changes, hard delete, or mutations to monthly/weekly/period rows.

---

## 2. Allowed app-source files next wave

| Path | Purpose |
|------|---------|
| `app-source/app/routes.php` | Register nested monthly-report blocks + flat report-block routes |
| `app-source/app/bootstrap.php` | Require new classes if needed |
| `app-source/app/Controllers/ReportBlockController.php` | New controller |
| `app-source/app/Services/ReportBlockService.php` | Validation + workflow + audit |
| `app-source/app/Repositories/ReportBlockRepository.php` | Persistence |
| `app-source/app/Views/pages/report-blocks/index.php` | List |
| `app-source/app/Views/pages/report-blocks/show.php` | Detail |
| `app-source/app/Views/pages/report-blocks/form.php` | Shared form |
| `app-source/app/Views/pages/report-blocks/create.php` | Create wrapper |
| `app-source/app/Views/pages/report-blocks/edit.php` | Edit wrapper |
| `app-source/app/Views/pages/monthly-reports/show.php` | Parent monthly report blocks section |
| `app-source/app/Views/partials/header.php` | Nav only if needed |
| `app-source/app/Controllers/DashboardController.php` | Card/count only if needed |
| `app-source/app/Views/pages/dashboard.php` | Only if needed |
| `app-source/public/assets/css/*` (existing) | Minimal styles / badges |
| `app-source/public/assets/js/*` | Only if strictly needed (prefer none; **no** drag/drop libs) |
| `app-source/README.md` | Routes note if existing pattern requires |
| `product/` result doc(s) | Implementation result |
| `reports/` closeout | Implementation REPORT |
| `OPERATIONAL-INDEX.md` | Status update |

Also allowed if existing patterns require tiny wiring:

- `app-source/app/Support/*` — only unavoidable shared helpers
- Reuse of `MonthlyReportContentRepository` / `WeeklyCheckpointRepository` / `ReportingPeriodRepository` for parent/source load (read-only from block wave perspective)

**Not allowed without separate charter:**

- New migrations / SQL schema edits
- Auth core rewrite / password/hash changes
- Drag/drop UI / sortable libraries
- PDF/export
- Topvisor / API / n8n / metric tables
- Client portal
- Fixture tool rewrite
- `.env` / `.env.local` edits
- Real client data import
- DELETE routes/UI
- Mutations to `monthly_report_contents`, `weekly_checkpoints`, or `reporting_periods` rows
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

1. **UPDATE** existing `report_blocks` rows via CRUD (smoke: prefer `executive_summary` under monthly id **1**).
2. **INSERT** one additional smoke block (prefer `risks_and_blockers` with `LOCAL_FIXTURE_ONLY`) under monthly id **1**.
3. **UPDATE** status / `sort_order` / content fields on smoke rows as needed for validation.
4. **INSERT** optional `audit_log` events for create/update/status/reviewed/approved/archived/reordered.
5. **SELECT** joins for detail/forms/parent context/source checkpoints.

---

## 5. DB actions not allowed

- Schema CREATE/ALTER/DROP
- New migration files
- DELETE of report_blocks (including smoke cleanup) without separate destructive charter
- TRUNCATE / DROP tables
- Mutations to users/roles/passwords
- Mutations to clients/projects/sites
- Mutations to `reporting_periods` rows
- Mutations to `weekly_checkpoints` rows
- Mutations to `monthly_report_contents` rows
- Any non-local / production DB
- Real client data inserts

---

## 6. Smoke list

1. `php -l` on changed PHP files — PASS  
2. Auth GET `/monthly-reports/1/blocks` — shows 5 fixture blocks sorted 10–50  
3. Auth GET `/report-blocks/{id}` for `executive_summary` — PASS; parent + source links  
4. Auth GET edit form — PASS  
5. POST update `executive_summary` title/body/status → `in_progress` (CSRF) — persisted; `LOCAL_FIXTURE_ONLY` retained  
6. POST create `risks_and_blockers` under monthly id **1** — PASS; markers present  
7. POST duplicate `block_key` — refused safely  
8. Invalid `source_weekly_checkpoint_ids` — refused  
9. Invalid JSON (`data_json` / `source_metric_refs`) — refused  
10. Manual `sort_order` update works  
11. Source weekly checkpoint links shown  
12. Monthly report detail shows report blocks section  
13. Unauthenticated block routes → `/login`  
14. `/health` 200; `/login` 200; `/not-existing` 404  
15. Reporting period + weekly checkpoint + monthly report CRUD regression PASS  
16. Audit events present if implemented  
17. Confirm **no** DELETE route/UI and **no** drag/drop UI  
18. Confirm monthly/weekly/period row counts unchanged; report_blocks count documented  
19. No password/hash in output/docs  

Exact assertions live in the validation plan.

---

## 7. Commit policy

- Exact-path staging only (implementation charter allowlist)
- Never `git add .` / `-A` / `commit -a`
- Preserve foreign WIP
- Commit and push are **separate**; **no push** unless implementation charter explicitly authorizes
- Suggested primary message: `feat(iseo-report-hub): add report blocks crud`
- Docs hash-record follow-up if REPORT needs commit hash: `docs(iseo-report-hub): record report blocks crud commit hash`
- Staged area must be empty before staging; only allowlisted paths may appear in `git diff --cached --name-only`

---

## 8. STOP conditions

STOP and do not proceed / do not commit if:

- Repo root / drive / volume / branch unsafe
- Staged index non-empty before start (or contains non-allowlist paths before commit)
- i-SEO foreign/unrelated WIP unexpectedly present in scope
- DB target ≠ `iseo_report_hub_dev` @ `127.0.0.1`
- DB-06 table missing or fixture baseline unexpectedly destroyed
- Scope expands into drag/drop / PDF / portal / Topvisor / schema
- Parent monthly / weekly / period rows would be mutated
- Credentials would be printed or committed
- Broad git add would be required
- Push requested without charter (default: no push)

Output token example:

`STOP — I-SEO REPORT BLOCKS CRUD IMPLEMENTATION SAFETY CONDITION FAILED`
