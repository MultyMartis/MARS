# iSEO Sales local tests

Requires a disposable local PostgreSQL with `DATABASE_URL` pointing at an empty (or dedicated) `mars` database.

## Apply schema + fixtures

```bash
export DATABASE_URL='postgresql://mars_owner@127.0.0.1:5432/mars'
bash tests/iseo_sales/01_schema_apply.sh
```

From repo root of `projects/mars-data-layer`.

## Constraint / behavior assertions

```bash
psql "$DATABASE_URL" -v ON_ERROR_STOP=1 -f tests/iseo_sales/02_constraints.sql
```

## Permission smoke

```bash
psql "$DATABASE_URL" -v ON_ERROR_STOP=1 -f tests/iseo_sales/03_permissions.sql
```

Notes:

- Roles are created `NOLOGIN` by default; `SET ROLE` works when connected as a superuser/owner that can assume them.
- If `SET ROLE` fails in your environment, grant temporary membership or enable LOGIN out-of-band (never commit passwords).
- These tests do **not** claim production apply readiness.
