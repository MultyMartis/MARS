# Migration Standard v1

**Document:** `MIGRATION-STANDARD-v1`  
**project_id:** `mars-data-layer`  
**Date:** 2026-09-03

---

## 1. Principles

1. **Git-versioned SQL** is the only DDL source of truth.
2. **No runtime DDL** from n8n workflows, AI agents, or ad-hoc admin scripts in production.
3. Migrations run as **`mars_migrator`** (or equivalent), never as runtime roles.
4. **Forward migrations** are the normal path; expand/contract for breaking changes.
5. **No combined** destructive schema change + production workflow cutover in one untested step.

---

## 2. Layout

```text
database/
  core/migrations/
  shared/migrations/
  app_iseo_sales/migrations/
  app_seo_content/migrations/
```

Each schema family owns its ordered migration files.

---

## 3. Naming convention

```text
NNNN_short_snake_description.sql
```

- `NNNN` = zero-padded integer sequence **per schema folder** (0001, 0002, …).
- Description: lowercase snake, action-oriented (`create_jobs`, `add_leads_gmail_uid_uq`).

Optional companion:

```text
NNNN_short_snake_description.down.sql
```

Down files are **best-effort** and may be unsupported for destructive production rollbacks — see §6.

---

## 4. Ordered versioning

- Apply in lexicographic/numeric order within a schema folder.
- Record applied versions in a migrator ledger table (to be created under `mars_core` in a later schema wave), e.g. conceptual `mars_core.schema_migrations`.
- Never edit an already-applied migration on a shared branch; add a new migration.

---

## 5. Forward migration content rules

- Idempotent where practical (`IF NOT EXISTS`) **without** hiding real failures.
- Schema-qualify all objects (`app_iseo_sales.jobs`).
- Include grants appropriate to roles **in dedicated grant migrations** or clearly sectioned blocks.
- No embedding secrets.
- Prefer expand → dual-write/backfill → contract over in-place destructive renames.

---

## 6. Rollback philosophy

| Environment | Policy |
|-------------|--------|
| Local/dev | Reset DB from migrations + fixtures is preferred over long down chains |
| Pre-production | Down scripts optional; restore from dump preferred for large changes |
| Production | **Pre-migration dump required**; rollback = restore or forward-fix; do not rely on automated down for data-lossy changes |

PRE-CUTOVER vs POST-CUTOVER workflow rollback is defined in architecture — schema rollback is not a free undo of business cutover.

---

## 7. Expand / contract

1. **Expand:** add nullable columns/tables; keep old path working.
2. **Migrate data / dual-read** under charter.
3. **Contract:** remove old columns only after consumers stop using them.

---

## 8. Pre-migration backup requirement

Before production apply:

- logical dump of `mars` (or affected schemas);
- off-host copy when production SoT;
- record dump location in the change evidence note (no secrets).

---

## 9. Validation

After apply:

- migrator ledger matches expected tip;
- smoke queries / Toolkit smoke;
- privilege checks (runtime role cannot DDL);
- for shadow/cutover waves: reconciliation report.

---

## 10. Production application procedure (human-operated)

1. Charter + freeze window.
2. Backup.
3. Apply migrations as migrator.
4. Validate.
5. Only then enable workflow features that depend on new schema.
6. Evidence note under project `reports/` or bot pack evidence.

---

## 11. Forbidden

- Runtime `CREATE TABLE` from AI.
- Squashing history on production without dump + charter.
- Mixing n8n SQLite migrations into this tree.
- Shipping un-reviewed destructive `DROP` with an active dual-write consumer.
