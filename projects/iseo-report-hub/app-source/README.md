# i-SEO Report Hub — App Source Mirror

## Status

**Auth + reporting period CRUD + weekly checkpoints CRUD + monthly report content CRUD + report blocks CRUD + preview + finalization + snapshots MVP (local).** Versioned Active Brain mirror with DB-backed login/logout, safe `/health` DB status, local admin/fixture tools, internal reporting-period CRUD, period-scoped weekly checkpoint CRUD, period-scoped monthly report content CRUD, monthly-scoped report blocks CRUD, internal preview/print, finalization workflow, and internal report snapshots. Sync to Localhost runtime is done via allowlist (Model A).

| Fact | State |
|------|-------|
| Platform | Custom **PHP + SQL/MySQL** |
| WordPress | **Not used** as runtime or source of truth |
| Framework / Composer | **None** — plain PHP 8.3 |
| Database | Local `iseo_report_hub_dev` via runtime `.env.local` (not in Git) |
| Migrations | Core + reporting_periods + weekly_checkpoints + monthly_report_contents + report_blocks + report_snapshots + report_exports (DB-08) + export template/render metadata columns (DB-09) applied (separate waves) |
| Auth | **DB-backed** — `password_verify` + roles + audit |
| Reporting periods | **CRUD MVP** — list/detail/create/edit/archive-by-status |
| Weekly checkpoints | **CRUD MVP** — period-scoped list/detail/create/edit/skip-or-archive-by-status |
| Monthly report content | **CRUD MVP** — period-scoped detail/create/edit/archive-by-status; one row per period |
| Report blocks | **CRUD MVP** — monthly-scoped list/detail/create/edit/archive-by-status; unique parent+block_key |
| Report snapshots | **Internal MVP** — create/view active snapshot from finalized monthly; checksum idempotency; no public |
| Report exports | **HTML + PDF MVP (hardened) + styled v2** — internal HTML/PDF artifacts; Edge headless PDF; auth download with path/MIME/size/checksum/PDF-magic guards; idempotent; historical v1 preserved; styled v2 via `iseo_default_v1`; **no** public share |
| Report styling template | **Code-first default `iseo_default_v1` v1** — applied to styled export versions (v2+); historical exports id 1/2 unchanged; no DB template registry yet |
| Export template metadata (DB-09) | **Nullable columns on `report_exports`** — `template_id` / `template_version` / `render_target` / `render_engine` / `render_options_json` / `source_html_export_id` / `metadata_json`; backfill ids **3–4** only; ids **1–2** NULL; UI/repository write path still deferred |
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
- `GET /monthly-reports/{id}` — flat detail (includes report blocks section + finalization card)
- `GET /monthly-reports/{id}/preview` — **internal-only** assembled preview (auth required; blocks primary; no public/PDF)
- `GET /monthly-reports/{id}/preview/print` — print-friendly twin of preview (browser print only; no server PDF)
- `GET /monthly-reports/{id}/snapshot` — active snapshot summary or “no snapshot yet” (auth; internal-only)
- `POST /monthly-reports/{id}/snapshot` — create snapshot from finalized monthly (CSRF; idempotent on checksum; admin_owner / seo_lead_reviewer)
- `GET /report-snapshots/{id}` — immutable snapshot detail (auth; internal-only; no edit/delete/public)
- `GET /report-snapshots/{id}/exports` — list exports for snapshot (auth; internal-only)
- `POST /report-snapshots/{id}/exports/html` — create HTML export from snapshot (CSRF; idempotent; admin_owner / seo_lead_reviewer)
- `POST /report-snapshots/{id}/exports/html/styled` — create styled HTML export version using `iseo_default_v1` (CSRF; idempotent; does not overwrite v1)
- `POST /report-snapshots/{id}/exports/pdf` — create PDF export from ready HTML artifact via Edge headless (CSRF; idempotent; admin_owner / seo_lead_reviewer)
- `POST /report-snapshots/{id}/exports/pdf/styled` — create styled PDF from styled HTML v2 (CSRF; idempotent; does not overwrite v1)
- `GET /report-exports/{id}` — export metadata detail (auth; internal-only; HTML or PDF)
- `GET /report-exports/{id}/download` — authenticated artifact download (HTML or PDF MIME; no public URL)
- `POST /monthly-reports/{id}/submit-review` — `in_progress` → `ready_for_review` (CSRF; role-gated)
- `POST /monthly-reports/{id}/mark-reviewed` — `ready_for_review` → `reviewed` (CSRF; role-gated)
- `POST /monthly-reports/{id}/finalize` — `reviewed` → `finalized` when readiness passes (CSRF; sets `finalized_at` if null)
- `POST /monthly-reports/{id}/reopen` — `finalized` → `reviewed` (admin_owner; preserves `finalized_at`)
- `GET /monthly-reports/{id}/edit` — edit form (locked when finalized)
- `POST /monthly-reports/{id}` — update (CSRF; archive via status; refused when finalized)
- `GET /monthly-reports/{monthly_report_id}/blocks` — block list within monthly report
- `GET /monthly-reports/{monthly_report_id}/blocks/create` — create block form
- `POST /monthly-reports/{monthly_report_id}/blocks` — create block (CSRF; unique parent+block_key; refused when parent finalized)
- `GET /report-blocks/{id}` — flat block detail
- `GET /report-blocks/{id}/edit` — edit form
- `POST /report-blocks/{id}` — update (CSRF; archive via status)
- 404 fallback

No top-level `/monthly-reports` or `/report-blocks` index (period/monthly-scoped entry is enough).  
No DELETE route for reporting periods, weekly checkpoints, monthly report content, report blocks, or snapshots — archive/skip via status (snapshots: no DELETE; supersede on later version).  
No drag/drop reorder (manual `sort_order` only).  
No public share token. PDF is internal-only via authenticated download from local Edge print-to-PDF (Chrome fallback if Edge fails).

## Secrets policy

- Do **not** commit `.env` or `.env.local`.
- Do **not** create `.env.local` in this source tree.
- Runtime `.env.local` stays outside Git.
- No production credentials, no real private client metrics in this tree.
- Never print password or password hash in tool output/reports.

## What this phase is not

- No password reset / remember-me / OAuth
- No client portal auth for `client_viewer`
- No drag/drop reorder / rich text editor / public PDF share
- No hard DELETE of reporting periods, weekly checkpoints, monthly report content, report blocks, or snapshots
- No user management UI
- No real client import
- No Composer / npm / WordPress
- No snapshot v2 versioning smoke (deferred until reopen/re-finalize charter)
- No public/token publish from snapshots
- No DB-backed template registry / client branding DB / logo upload
- No silent overwrite of historical HTML/PDF exports (restyle requires new export version wave)

## Next phase

**Recommended:** Report Styling Visual QA 01 (operator visual review of styled HTML/PDF v2 against default template).
