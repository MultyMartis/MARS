# I-SEO Report Hub — Migration Policy v0.1

**Status:** POLICY ONLY — no migration files created  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-24  
**Authority:** Operator I-SEO Report Hub DB Creation + Schema Migration Charter 01  
**Related:** [I-SEO-REPORT-HUB-DB-CREATION-CHARTER-v0.1.md](I-SEO-REPORT-HUB-DB-CREATION-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-INITIAL-SCHEMA-PLAN-v0.1.md](I-SEO-REPORT-HUB-INITIAL-SCHEMA-PLAN-v0.1.md), [I-SEO-REPORT-HUB-MVP-SCHEMA-DRAFT-v0.1.md](I-SEO-REPORT-HUB-MVP-SCHEMA-DRAFT-v0.1.md)

---

## 1. Status

| Fact | State |
|------|-------|
| Document type | Migration **policy** only |
| Migration files created | **No** |
| SQL executed | **No** |
| Ledger table created | **No** |
| Runner implemented | **No** |

This policy defines how future migrations must be authored and applied. It does **not** create `database/migrations/` files or run DDL.

---

## 2. Migration Location

| Role | Path |
|------|------|
| **Planned source (SoT)** | `projects/iseo-report-hub/app-source/database/migrations/` |
| **Runtime after sync** | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\database\migrations\` |

Migration files are versioned in Active Brain `app-source` and copied to Localhost runtime only under an explicit sync/apply charter (Model A: source → runtime). Executable apply happens against **local** `iseo_report_hub_dev` only until a separate environment charter says otherwise.

Current Phase 0/1A state: `database/` holds documentation only (`schema-draft-not-migration.md`); **no** `migrations/` directory yet.

---

## 3. Migration Format

| Option | Pros | Cons |
|--------|------|------|
| **SQL files** | Transparent; easy HITL review; diff-friendly | Rollback scripts optional/manual |
| **PHP migration runner** | Can encode up/down; stateful helpers | More app code; harder for non-PHP reviewers |
| **Heavy framework migrator** | Familiar if Laravel/etc. | **Not** in MVP platform decision |

**Recommended MVP:** timestamped **SQL files** + a simple **migration ledger table** once the runner exists, unless a later charter proves a PHP runner is required for reversible/stateful work.

Do not auto-invent a full migration framework in the first apply wave.

---

## 4. Migration Naming

Use sortable timestamps and a short purpose slug:

```text
2026_07_24_000001_create_core_tables.sql
2026_07_24_000002_create_reporting_period_tables.sql
```

Rules:

- one logical change set per file (or one clearly named batch);
- no spaces in filenames;
- no secrets or real client data in SQL comments;
- seeds, if any, live under `database/seeds/` and are **separate** from schema migrations.

---

## 5. Migration Ledger

**Planned table:** `schema_migrations`

| Field | Purpose |
|-------|---------|
| `id` | Surrogate PK |
| `migration` | Filename / migration id (unique) |
| `checksum` | Hash of applied file content |
| `executed_at` | When applied |
| `batch` | Optional batch number for grouped applies |

**Not created in this task.** Ledger DDL belongs in the first migration (or a tiny bootstrap migration) when the apply wave is chartered.

---

## 6. Execution Rules

1. Migrations run **only** against local `iseo_report_hub_dev` initially.
2. **Operator HITL** before every apply (dry-run/plan review).
3. **No auto-run** on page load.
4. **No migration execution** during normal HTTP request handling.
5. Migration runner (when built) must print a **dry-run / plan** before apply.
6. **Backups** before destructive changes (DROP/ALTER that can lose data).
7. Apply from reviewed files under `app-source/database/migrations/` after sync to runtime (or CLI pointed at source with explicit charter).
8. Fail closed: if ledger says already applied, do not re-apply silently.

---

## 7. Rollback Policy

| Rule | Statement |
|------|-----------|
| Destructive rollback | Requires **explicit operator approval** |
| MVP default | **Forward-only** migrations are acceptable |
| Down scripts | Optional later; not required for first local schema |
| Failed apply | Stop; report; fix forward migration or restore from backup under HITL |
| Production | No rollback/apply against production without a separate production charter |

---

## 8. SAFE UNKNOWN

- Exact CLI entrypoint name (`php bin/migrate.php`, shell wrapper, etc.) — decide when runner is implemented.
- Whether checksum algorithm is SHA-256 or another — decide at runner design time.
- Whether `database/migrations/` is included in the next source→runtime sync allowlist by default — confirm in the apply/sync charter.
- Need for PHP-based reversible migrations — unknown until complexity appears.
