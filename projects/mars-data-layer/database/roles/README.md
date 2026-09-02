# Database roles (V1)

**project_id:** `mars-data-layer`  
**Scope:** Role *definitions* only — **no passwords** in Git SQL.

Passwords, `LOGIN` enablement, and connection grants are set **out-of-band** by Server Ops (secret handoff). Migration SQL uses `CREATE ROLE` without `PASSWORD`.

---

## Roles

| Role | Purpose | Typical login |
|------|---------|---------------|
| `mars_owner` | Bootstrap / ownership of database objects (often the cluster superuser or DB owner used to apply foundation). Not created by app migrations if it already owns `mars`. | Ops-managed |
| `mars_migrator` | Apply schema migrations (`CREATE`/`ALTER`/`GRANT`). Prefer NOLOGIN until Server Ops enables controlled login. | Ops-enabled later |
| `iseo_runtime` | n8n / Toolkit mutating path for `app_iseo_sales` (INSERT/UPDATE + SECURITY DEFINER function EXECUTE). | Service account |
| `iseo_agent` | Narrow agent/read+limited ops: SELECT on selected tables; EXECUTE only on read functions (`get_lead`, `list_pending_leads`). | Service / agent |
| `iseo_reader` | Read-only reporting / shadow validation. SELECT only. | Reporting |

---

## Deferred (not in V1 SQL)

| Role family | Note |
|-------------|------|
| `content_*` (e.g. `content_runtime`, `content_reader`) | Deferred until `app_seo_content` leaves placeholder. Schema exists empty; **no** grants to iSEO roles on that schema. |

---

## Apply order

1. `database/roles/001_create_roles.sql` (idempotent role stubs)
2. `database/core/migrations/0001_roles_and_schemas.sql`
3. `database/core/migrations/0002_mars_core.sql`
4. `database/app_iseo_sales/migrations/0001` … `0004`
5. Fixtures (optional, non-prod)

See `tests/iseo_sales/01_schema_apply.sh`.
