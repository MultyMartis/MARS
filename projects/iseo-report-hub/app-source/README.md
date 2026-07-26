# i-SEO Report Hub — App Source Mirror

## Status

**Auth + reporting period CRUD MVP (local).** Versioned Active Brain mirror with DB-backed login/logout, safe `/health` DB status, local admin/fixture tools, and internal reporting-period CRUD. Sync to Localhost runtime is done via allowlist (Model A).

| Fact | State |
|------|-------|
| Platform | Custom **PHP + SQL/MySQL** |
| WordPress | **Not used** as runtime or source of truth |
| Framework / Composer | **None** — plain PHP 8.3 |
| Database | Local `iseo_report_hub_dev` via runtime `.env.local` (not in Git) |
| Migrations | Core + reporting_periods applied (separate waves) |
| Auth | **DB-backed** — `password_verify` + roles + audit |
| Reporting periods | **CRUD MVP** — list/detail/create/edit/archive-by-status |
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
- `GET /reporting-periods/{id}` — detail
- `GET /reporting-periods/{id}/edit` — edit form
- `POST /reporting-periods/{id}` — update (CSRF; archive via status)
- 404 fallback

No DELETE route for reporting periods — archive via `status=archived`.

## Secrets policy

- Do **not** commit `.env` or `.env.local`.
- Do **not** create `.env.local` in this source tree.
- Runtime `.env.local` stays outside Git.
- No production credentials, no real private client metrics in this tree.
- Never print password or password hash in tool output/reports.

## What this phase is not

- No password reset / remember-me / OAuth
- No client portal auth for `client_viewer`
- No weekly checkpoint / monthly content editor
- No hard DELETE of reporting periods
- No user management UI
- No real client import
- No Composer / npm / WordPress

## Next phase

**Recommended:** Weekly Checkpoints DB-04 Charter 01 (or Reporting Period CRUD Hardening 01 if role matrix needs multi-user smoke).
