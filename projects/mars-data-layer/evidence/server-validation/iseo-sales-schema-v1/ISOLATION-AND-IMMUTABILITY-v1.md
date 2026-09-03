# ISOLATION-AND-IMMUTABILITY-v1

**Suite:** `tests/iseo_sales/03_permissions.sql` (+ extended suite)  
**Status:** PASS on server PG 18.0

## Runtime (`iseo_runtime`)

- Intended DML / approved function execution: allowed.
- DDL: denied.
- UPDATE/DELETE on immutable `lead_events` history: denied (exact privilege errors recorded in permission suite output).
- Unrelated schema write (e.g. `app_seo_content`): denied.

## Agent (`iseo_agent`)

- Narrow approved functions/tools: allowed where granted.
- Arbitrary UPDATE/DELETE on business tables: denied.
- DDL: denied.

## Reader (`iseo_reader`)

- Read-only: PASS.

## PUBLIC

- No unnecessary CREATE/WRITE on application schemas: PASS (suite probe).

Permissions were **not** weakened to make tests pass.
