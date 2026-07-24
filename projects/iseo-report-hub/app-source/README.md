# i-SEO Report Hub — App Source Mirror

## Status

**Auth persistence bootstrap complete (local).** Versioned Active Brain mirror with DB-backed login/logout, safe `/health` DB status, and local admin CLI bootstrap tool. Sync to Localhost runtime is done via allowlist (Model A).

| Fact | State |
|------|-------|
| Platform | Custom **PHP + SQL/MySQL** |
| WordPress | **Not used** as runtime or source of truth |
| Framework / Composer | **None** — plain PHP 8.3 |
| Database | Local `iseo_report_hub_dev` via runtime `.env.local` (not in Git) |
| Migrations | First core migration applied (separate wave) |
| Auth | **DB-backed** — `password_verify` + roles + audit |
| Secrets | **None in source** — `.env.example` placeholders only; **no** `.env` / `.env.local` |
| Runtime sync | Allowlist source → runtime for auth wave files |

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

## Routes

- `GET /` — dashboard (requires authenticated internal role)
- `GET /login` / `POST /login` — DB-backed login
- `GET /logout` — logout + redirect login
- `GET /health` — PHP + safe DB status
- 404 fallback

## Secrets policy

- Do **not** commit `.env` or `.env.local`.
- Do **not** create `.env.local` in this source tree.
- Runtime `.env.local` stays outside Git.
- No production credentials, no real private client metrics in this tree.
- Never print password or password hash in tool output/reports.

## What this phase is not

- No password reset / remember-me / OAuth
- No client portal auth for `client_viewer`
- No reporting CRUD
- No user management UI
- No DB-03+ reporting tables
- No Composer / npm / WordPress

## Next phase

**Recommended:** DB-03 reporting periods migration charter (schema for reporting periods), then project/period CRUD baseline.
