# i-SEO Report Hub — App Source Mirror

## Status

**Auth + reporting period CRUD + weekly checkpoints CRUD + monthly report content CRUD + report blocks CRUD MVP (local).** Versioned Active Brain mirror with DB-backed login/logout, safe `/health` DB status, local admin/fixture tools, internal reporting-period CRUD, period-scoped weekly checkpoint CRUD, period-scoped monthly report content CRUD, and monthly-scoped report blocks CRUD. Sync to Localhost runtime is done via allowlist (Model A).

| Fact | State |
|------|-------|
| Platform | Custom **PHP + SQL/MySQL** |
| WordPress | **Not used** as runtime or source of truth |
| Framework / Composer | **None** — plain PHP 8.3 |
| Database | Local `iseo_report_hub_dev` via runtime `.env.local` (not in Git) |
| Migrations | Core + reporting_periods + weekly_checkpoints + monthly_report_contents + report_blocks applied (separate waves) |
| Auth | **DB-backed** — `password_verify` + roles + audit |
| Reporting periods | **CRUD MVP** — list/detail/create/edit/archive-by-status |
| Weekly checkpoints | **CRUD MVP** — period-scoped list/detail/create/edit/skip-or-archive-by-status |
| Monthly report content | **CRUD MVP** — period-scoped detail/create/edit/archive-by-status; one row per period |
| Report blocks | **CRUD MVP** — monthly-scoped list/detail/create/edit/archive-by-status; unique parent+block_key |
| Secrets | **None in source** — `.env.example` placeholders only; **no** `.env` / `.env.local` |
| Runtime sync | Allowlist source → runtime |

## Paths

| Item | Value |
|------|-------|
| Source mirror (this tree) | `X:\AI MARS\projects\iseo-report-hub\app-source\` |
| Runtime target | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\` |
| Domain | `http://iseo-report-hub.test/` |
| DB | `iseo_report_hub_dev` @ `127.0.0.1` |
| PHP target | **8.3.30** (Laragon) |

## Local admin bootstrap

CLI only (runtime or source with runtime `.env.local`):

```bash
php tools/create-local-admin.php --name="Local Admin" --email=admin@iseo-report-hub.test
```

Password via hidden/local prompt or process-only `ISEO_ADMIN_PASSWORD` (never argv; never commit; never report).

## Local fixture bootstrap

CLI only (runtime with `.env.local`):

```bash
php tools/create-local-fixture.php
```

Creates one local-only demo client / project / site / reporting_period (`LOCAL_FIXTURE_ONLY`). Idempotent. Refuses any DB other than `iseo_report_hub_dev` @ `127.0.0.1`. Prints IDs/counts only — no credentials.

## Routes

- `GET /` — dashboard (requires authenticated internal role)
- `GET /login` / `POST /login` — DB-backed login
- `GET /logout` — logout + redirect login
- `GET /health` — PHP + safe DB status
- `GET /reporting-periods` — list (auth + internal role)
- `GET /reporting-periods/create` — create form
- `POST /reporting-periods` — create (CSRF)
- `GET /reporting-periods/{id}` — detail (includes weekly checkpoint + monthly report sections)
- `GET /reporting-periods/{id}/edit` — edit form
- `POST /reporting-periods/{id}` — update (CSRF; archive via status)
- `GET /reporting-periods/{period_id}/weekly-checkpoints` — list within period
- `GET /reporting-periods/{period_id}/weekly-checkpoints/create` — create form
- `POST /reporting-periods/{period_id}/weekly-checkpoints` — create (CSRF)
- `GET /weekly-checkpoints/{id}` — detail
- `GET /weekly-checkpoints/{id}/edit` — edit form
- `POST /weekly-checkpoints/{id}` — update (CSRF; skip/archive via status)
- `GET /reporting-periods/{period_id}/monthly-report` — period monthly detail (or redirect to create)
- `GET /reporting-periods/{period_id}/monthly-report/create` — create form (one per period)
- `POST /reporting-periods/{period_id}/monthly-report` — create (CSRF; duplicate guard)
- `GET /monthly-reports/{id}` — flat detail (includes report blocks section)
- `GET /monthly-reports/{id}/preview` — **internal-only** assembled preview (auth required; blocks primary; no public/PDF)
- `GET /monthly-reports/{id}/preview/print` — print-friendly twin of preview (browser print only; no server PDF)
- `GET /monthly-reports/{id}/edit` — edit form
- `POST /monthly-reports/{id}` — update (CSRF; archive via status)
- `GET /monthly-reports/{monthly_report_id}/blocks` — block list within monthly report
- `GET /monthly-reports/{monthly_report_id}/blocks/create` — create block form
- `POST /monthly-reports/{monthly_report_id}/blocks` — create block (CSRF; unique parent+block_key)
- `GET /report-blocks/{id}` — flat block detail
- `GET /report-blocks/{id}/edit` — edit form
- `POST /report-blocks/{id}` — update (CSRF; archive via status)
- 404 fallback

No top-level `/monthly-reports` or `/report-blocks` index (period/monthly-scoped entry is enough).  
No DELETE route for reporting periods, weekly checkpoints, monthly report content, or report blocks — archive/skip via status.  
No drag/drop reorder (manual `sort_order` only).  
No public share token, no export route, no server-side PDF generation.

## Secrets policy

- Do **not** commit `.env` or `.env.local`.
- Do **not** create `.env.local` in this source tree.
- Runtime `.env.local` stays outside Git.
- No production credentials, no real private client metrics in this tree.
- Never print password or password hash in tool output/reports.

## What this phase is not

- No password reset / remember-me / OAuth
- No client portal auth for `client_viewer`
- No drag/drop reorder / rich text editor / PDF export
- No hard DELETE of reporting periods, weekly checkpoints, monthly report content, or report blocks
- No user management UI
- No real client import
- No Composer / npm / WordPress

## Next phase

**Recommended:** Report Finalization Charter 01 (or Report Preview / Render Hardening 01 if multi-role / archive-exclusion live smoke needed).
