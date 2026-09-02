# iSEO Sales local tests

Requires a disposable local PostgreSQL with connection env (or `DATABASE_URL`) pointing at a dedicated `mars` database.

## Windows (recommended on this workstation)

Load local-only secrets (not in Git), then:

```powershell
. 'X:\AI MARS\local\mars-bot-data\env.local.ps1'
cd <worktree-or-repo>\projects\mars-data-layer
.\tests\iseo_sales\apply_and_test.ps1 -ProjectRoot .
# Full reset + reapply + all suites:
.\tests\iseo_sales\apply_and_test.ps1 -ProjectRoot . -ResetFirst
```

## Apply schema + fixtures (bash)

```bash
export DATABASE_URL='postgresql://mars_owner@127.0.0.1:5433/mars'
bash tests/iseo_sales/01_schema_apply.sh
```

From repo root of `projects/mars-data-layer`. Local disposable runtime uses port **5433** by convention (not Laragon MySQL 3306).

## Constraint / behavior assertions

```bash
psql "$DATABASE_URL" -v ON_ERROR_STOP=1 -f tests/iseo_sales/02_constraints.sql
```

## Permission smoke

```bash
psql "$DATABASE_URL" -v ON_ERROR_STOP=1 -f tests/iseo_sales/03_permissions.sql
```

## Extended local validation

```bash
psql "$DATABASE_URL" -v ON_ERROR_STOP=1 -f tests/iseo_sales/04_extended_local_validation.sql
psql "$DATABASE_URL" -v ON_ERROR_STOP=1 -f tests/iseo_sales/05_inventory_and_explain.sql
```

Notes:

- Roles are created `NOLOGIN` by default; `SET ROLE` works when connected as a superuser/owner that can assume them.
- If `SET ROLE` fails in your environment, grant temporary membership or enable LOGIN out-of-band (never commit passwords).
- These tests prove **local** apply readiness; production Server Ops foundation is a separate gate.
