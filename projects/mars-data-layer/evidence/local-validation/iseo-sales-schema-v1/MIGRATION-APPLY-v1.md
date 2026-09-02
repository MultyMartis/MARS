# MIGRATION-APPLY-v1

**Date:** 2026-09-03  
**Contract:** `EMPTY DB → ALL MIGRATIONS → SUCCESS` (no hand-created tables; no mid-stream manual patches)

## Apply order (canonical)

1. `database/roles/001_create_roles.sql`
2. `database/core/migrations/0001_roles_and_schemas.sql`
3. `database/core/migrations/0002_mars_core.sql`
4. `database/app_iseo_sales/migrations/0001_schema_and_inbound.sql`
5. `database/app_iseo_sales/migrations/0002_leads_and_events.sql`
6. `database/app_iseo_sales/migrations/0003_access_delivery_jobs.sql`
7. `database/app_iseo_sales/migrations/0004_functions_and_grants.sql`
8. `database/fixtures/iseo_sales/synthetic_v1.sql` (synthetic only)

## Runner

Windows platform-neutral: `tests/iseo_sales/apply_and_test.ps1`  
(Same SQL order as `01_schema_apply.sh`; does not change test semantics.)

## Results

| Pass | Reset from empty | Migrations | Fixtures | Notes |
|------|------------------|------------|----------|-------|
| 1 | Yes | SUCCESS | SUCCESS | First empty-DB apply |
| 2 | Yes (`-ResetFirst`) | SUCCESS | SUCCESS | Repeatability |
| 3 | Yes (`-ResetFirst`) | SUCCESS | SUCCESS | Marker `_repeatability-pass3.ok` |

**Verdict:** migrations apply from empty `mars` without source patches between files.
