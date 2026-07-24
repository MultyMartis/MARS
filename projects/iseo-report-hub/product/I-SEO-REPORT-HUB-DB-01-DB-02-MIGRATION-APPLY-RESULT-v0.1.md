# I-SEO Report Hub — DB-01 / DB-02 Migration Apply Result v0.1

**Status:** COMPLETE  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-24  
**Authority:** Operator I-SEO Report Hub DB Creation + DB-01 DB-02 Migration Files Apply 01  
**Related:** [I-SEO-REPORT-HUB-DB-CREATION-CHARTER-v0.1.md](I-SEO-REPORT-HUB-DB-CREATION-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-MIGRATION-POLICY-v0.1.md](I-SEO-REPORT-HUB-MIGRATION-POLICY-v0.1.md), [I-SEO-REPORT-HUB-INITIAL-SCHEMA-PLAN-v0.1.md](I-SEO-REPORT-HUB-INITIAL-SCHEMA-PLAN-v0.1.md), [I-SEO-REPORT-HUB-LOCAL-ENV-DB-SECRETS-POLICY-v0.1.md](I-SEO-REPORT-HUB-LOCAL-ENV-DB-SECRETS-POLICY-v0.1.md)

---

## 1. Status

| Field | Value |
|-------|-------|
| Wave | **Complete** |
| DB name | `iseo_report_hub_dev` |
| DB created | **Yes** (was absent) |
| Migration applied | **Yes** — `2026_07_24_000001_create_core_tables.sql` |
| Runtime `.env.local` created | **Yes** (runtime-only; not in Git) |
| Secrets in Git | **No** |

---

## 2. Source Changes

| Path | Change |
|------|--------|
| `app-source/database/migrations/2026_07_24_000001_create_core_tables.sql` | **Created** — DB-01 + minimal DB-02 DDL + role catalog seed |
| `app-source/tools/db-migrate.php` | **Created** — `status` / `apply`; refuses non-`iseo_report_hub_dev` |
| `app-source/database/README.md` | **Updated** — migration layout + apply procedure |
| `app-source/.gitignore` | **Updated** — `.env.*` + `!.env.example` |
| `app-source/.env.example` | **Unchanged** — placeholders already present |

---

## 3. Runtime Changes

| Item | Status |
|------|--------|
| `.env.local` | **Created** at `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\.env.local` — local user label `root`; password **empty local password**; values **not** printed |
| `database/README.md` | Copied source → runtime |
| `database/schema-draft-not-migration.md` | Copied source → runtime |
| `database/migrations/2026_07_24_000001_create_core_tables.sql` | Copied source → runtime |
| `tools/db-migrate.php` | Copied source → runtime (including post-apply DDL transaction fix) |
| `.gitignore` | Copied source → runtime |
| `app/` / `public/` / `config/` | **Untouched** |

---

## 4. DB Creation

| Field | Value |
|-------|-------|
| MySQL version | **8.4.3** |
| DB existed before | **No** |
| Charset | `utf8mb4` |
| Collation | `utf8mb4_0900_ai_ci` (confirmed available on server) |
| Creation result | `CREATE DATABASE IF NOT EXISTS …` — **PASS** |
| Unrelated DB mutation | **None** |

---

## 5. Migration Apply

| Field | Value |
|-------|-------|
| Migration name | `2026_07_24_000001_create_core_tables.sql` |
| Checksum (sha256) | `71dd22d0a0a0af14854b4b40d72ae611c80d74af8bfe038a413110b0be722bb4` |
| Applied status | **Applied** (ledger present; idempotent re-apply reports nothing pending) |
| Ledger row | **Present** — batch `1` |
| Tool note | First apply wrote tables + ledger; PDO `commit()` then failed because MySQL DDL auto-commits. Tool fixed to skip transaction wrap; re-synced; idempotent apply **PASS**. |

---

## 6. DB Smoke

| Check | Result |
|-------|--------|
| `php tools/db-migrate.php status` | First migration **[applied]** / `checksum_ok` |
| Expected tables (9) | `schema_migrations`, `users`, `roles`, `user_roles`, `audit_log`, `clients`, `projects`, `sites`, `project_type_profiles` — **all present** |
| Roles count | **6** |
| Users count | **0** |
| Clients count | **0** |
| HTTP `/health` | **200** (Phase 1A health unchanged; may still negate DB in body) |

---

## 7. Security Notes

- No credentials in Git.
- `.env.local` is runtime-only (outside Active Brain commit scope).
- No real users created.
- No real client data.
- No DB dumps created or committed.
- Migration seeds only non-secret role catalog codes/labels.

---

## 8. What Still Does Not Exist

- Real auth persistence in the PHP app
- Local admin user bootstrap
- Report tables (DB-03+)
- Report CRUD
- Client publishing DB / snapshots

---

## 9. Next Phase

**Recommended:** Auth persistence + local admin bootstrap charter.

---

## 10. SAFE UNKNOWN

- Whether Phase 1A `/health` will gain a real DB probe in a later charter (not changed here).
- Whether a dedicated MySQL app user (non-`root`) will replace the local empty-password Laragon account later.
