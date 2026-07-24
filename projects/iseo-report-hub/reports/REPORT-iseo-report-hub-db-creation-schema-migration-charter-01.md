# REPORT — I-SEO REPORT HUB DB CREATION + SCHEMA MIGRATION CHARTER 01

## 1. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive | `X:` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD (pre-commit) | `3003f30eef6a3c12d67361da4d55ae1fcf440e88` |
| Staged/index before work | **empty** |
| Foreign WIP | **Preserved** — unrelated `M`/`??` paths left untouched |
| Write scope | Active Brain docs only under `projects/iseo-report-hub/` (allowlisted product + reports + OPERATIONAL-INDEX) |
| Runtime path (read-only confirm) | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\` — **exists**; **not modified** |
| MySQL client (read-only) | `mysql.exe Ver 8.4.3` — version check only; **no** DB create/list/mutate |
| app-source forbidden artefacts | `.env` / `.env.local` / nested `.git` / `vendor/` / `node_modules` — **absent** |

---

## 2. Docs Reviewed

- `AGENTS.md` / `.cursorrules` (MARS session constraints)
- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-PHP-MYSQL-MVP-TECHNICAL-BRIEF-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-MVP-SCHEMA-DRAFT-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-MVP-ROUTE-AND-SCREEN-MAP-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-MVP-PHASE-1A-APP-SKELETON-RESULT-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-MVP-PHASE-1B-RUNTIME-SYNC-RESULT-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-LOCAL-HOSTS-RESMOKE-RESULT-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DEPLOY-SYNC-POLICY-v0.1.md`
- `projects/iseo-report-hub/app-source/database/schema-draft-not-migration.md`
- `projects/iseo-report-hub/app-source/database/README.md`
- `projects/iseo-report-hub/app-source/config/database.example.php`
- `projects/iseo-report-hub/app-source/.env.example`
- `projects/iseo-report-hub/app-source/.gitignore` + repo root `.gitignore` (env patterns)

---

## 3. DB Charter Summary

| Field | Value |
|-------|-------|
| DB name | `iseo_report_hub_dev` |
| Host / port | `127.0.0.1` / `3306` |
| Charset | `utf8mb4` |
| Collation | Prefer `utf8mb4_unicode_ci` or confirm MySQL 8 compatible default before SQL |
| Boundary | Local Laragon/dev only; no production; no real client data; no dumps in Git |
| Creation | **Not executed** — procedure deferred to next wave |
| Requirements before create | MySQL access method; local `.env.local`; migration runner model; drop/reset + backup policy |

Doc: `product/I-SEO-REPORT-HUB-DB-CREATION-CHARTER-v0.1.md`

---

## 4. Migration Policy Summary

| Field | Value |
|-------|-------|
| Source path | `projects/iseo-report-hub/app-source/database/migrations/` (planned; not created) |
| Runtime path | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\database\migrations\` |
| Format | **SQL files** + simple ledger later (MVP recommendation) |
| Naming | e.g. `2026_07_24_000001_create_core_tables.sql` |
| Ledger | `schema_migrations` (`id`, `migration`, `checksum`, `executed_at`, `batch`) — not created |
| Execution | Local dev only; HITL; no auto-run on HTTP; dry-run/plan before apply; backup before destructive |
| Rollback | Forward-only MVP OK; destructive rollback needs explicit approval |

Doc: `product/I-SEO-REPORT-HUB-MIGRATION-POLICY-v0.1.md`

---

## 5. Initial Schema Plan Summary

| Phase | Tables |
|-------|--------|
| DB-01 | `schema_migrations`, `users`, `roles`, `user_roles`, `audit_log` |
| DB-02 | `clients`, `projects`, `sites`, `project_type_profiles` |
| DB-03 | `reporting_periods`, `weekly_checkpoints`, `monthly_reports` |
| DB-04 | `report_blocks`, `report_block_values`, `work_item_categories`, `work_items`, `kpi_definitions`, `kpi_values` |
| DB-05 | `evidence_items`, `evidence_files`, `evidence_links`, `reviewer_comments`, `published_snapshots` |

**First migration recommendation:** DB-01 + minimal DB-02 only (not full report schema).  
**Seed policy:** no real users/passwords in Git; local admin via separate HITL; demo seed optional later.

Doc: `product/I-SEO-REPORT-HUB-INITIAL-SCHEMA-PLAN-v0.1.md`

---

## 6. Local Env / Secrets Summary

| Field | Value |
|-------|-------|
| `.env.example` | Committed placeholders (source) |
| `.env.local` | Local-only; **not created** |
| `.env` | Forbidden unless separately approved |
| Recommended storage | Runtime `.env.local` only; source keeps `.env.example` |
| Ignore | Root: `.env`, `.env.*`, `!.env.example`; app-source: `.env`, `.env.local` — gap on broad `.env.*` under app-source noted for future hygiene (no edit this wave) |
| Credentials | None written; reports must use PASS/FAIL only |

Doc: `product/I-SEO-REPORT-HUB-LOCAL-ENV-DB-SECRETS-POLICY-v0.1.md`

---

## 7. Validation

| Constraint | Result |
|------------|--------|
| no DB created/mutated | **pass** |
| no SQL executed | **pass** |
| no migration files | **pass** |
| no `.env` / `.env.local` | **pass** |
| no credentials/secrets | **pass** |
| no app-source code edits | **pass** |
| no runtime edits | **pass** |
| no source→runtime sync | **pass** |
| no WordPress | **pass** |
| no Composer/npm / vendor/node_modules | **pass** |
| no demo workspace edits | **pass** |
| no registry changes | **pass** |
| no vhost/hosts / service restart | **pass** |
| no push/fetch/pull/checkout/reset/restore/clean/stash | **pass** |
| foreign WIP preserved | **pass** |

---

## 8. Commit

| Field | Value |
|-------|--------|
| Exact-path stage | yes |
| Staged list (docs commit) | `projects/iseo-report-hub/OPERATIONAL-INDEX.md`; `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DB-CREATION-CHARTER-v0.1.md`; `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-MIGRATION-POLICY-v0.1.md`; `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-INITIAL-SCHEMA-PLAN-v0.1.md`; `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-LOCAL-ENV-DB-SECRETS-POLICY-v0.1.md`; `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-db-creation-schema-migration-charter-01.md` |
| Commit message | `docs(iseo-report-hub): add db migration charter` |
| Commit hash | `d38613bb2ec7fd078ae19418936934ec4721a2bf` (`d38613bb`) — six Active Brain docs only |
| Hash-fill follow-up | `4f0a48471023999d69647866c8639e5a6ef34ce8` (`4f0a4847`) — `docs(iseo-report-hub): record db migration charter commit hash` (this report path only) |
| HEAD verification | `git show --name-only --oneline --stat d38613bb` — only the six Active Brain docs above |
| Push | **no** |

---

## 9. SAFE UNKNOWN

- Final MySQL collation for `CREATE DATABASE` (`utf8mb4_unicode_ci` vs `utf8mb4_0900_ai_ci`).
- Local MySQL application username/password (must never be recorded).
- Exact migration runner CLI entrypoint when implemented.
- Whether `app-source/.gitignore` should add broad `.env.*` (documented gap; not changed here).

---

## 10. Recommended Next Action

**DB creation + DB-01/DB-02 migration files/apply charter.**

---

## 11. Files Changed

### Active Brain docs

- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DB-CREATION-CHARTER-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-MIGRATION-POLICY-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-INITIAL-SCHEMA-PLAN-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-LOCAL-ENV-DB-SECRETS-POLICY-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-db-creation-schema-migration-charter-01.md`

### Not changed

- `projects/iseo-report-hub/app-source/**`
- `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\**`
- `workspaces/**`, `registry/**`, other projects

---

## 12. Git Actions

| Action | Done |
|--------|------|
| exact-path git add | **yes** |
| commit | **yes** (after procedure) |
| push | **no** |
| fetch | **no** |
| pull | **no** |
| checkout | **no** |
| reset | **no** |
| restore | **no** |
| clean | **no** |
| stash | **no** |
