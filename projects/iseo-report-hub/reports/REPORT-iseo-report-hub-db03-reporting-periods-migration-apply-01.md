# REPORT — I-SEO REPORT HUB DB-03 REPORTING PERIODS MIGRATION APPLY 01

## 1. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive | `X:` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD before | `04c785a72ced2a2a0761a6b3cfb6033e0b4d1282` |
| Staged/index before | **empty** |
| i-SEO WIP before | **clean** (no modified/untracked under `projects/iseo-report-hub/`) |
| Foreign WIP | **Preserved** — unrelated `M`/`??` paths left untouched |
| Write scope | One migration SQL in `app-source`; one runtime migration copy; Active Brain result/report/`OPERATIONAL-INDEX` only |

---

## 2. Preflight

| Check | Result |
|-------|--------|
| PHP executable | `X:\MARS-Localhost\laragon\bin\php\php-8.3.30-Win32-vs16-x64\php.exe` — present |
| MySQL executable | `X:\MARS-Localhost\laragon\bin\mysql\mysql-8.4.3-winx64\bin\mysql.exe` — present |
| DB target | `iseo_report_hub_dev` |
| DB host | `127.0.0.1` |
| Migration count before | **1** |
| Latest migration before | `2026_07_24_000001_create_core_tables.sql` checksum `71dd22d0…be722bb4` |
| Table count before | **9** |
| users / roles before | **1 / 6** |
| clients / projects before | **0 / 0** |
| `reporting_periods` before | **absent** |
| Runtime `.env.local` | **present** (not printed; not edited; not committed) |

---

## 3. Source Migration

| Field | Value |
|-------|-------|
| Path | `projects/iseo-report-hub/app-source/database/migrations/2026_07_25_000002_create_reporting_periods_table.sql` |
| Table | `reporting_periods` |
| Fields | `id`, `project_id`, `period_key`, `period_start`, `period_end`, `status`, `title`, `summary`, `owner_user_id`, `reviewer_user_id`, `created_by`, `updated_by`, `finalized_at`, `created_at`, `updated_at` |
| FKs | project → `projects` RESTRICT; four user refs → `users` SET NULL |
| Indexes | unique `(project_id, period_key)` + seven named non-unique indexes |
| CHECKs | dates (`period_start <= period_end`); status IN six MVP values |
| Seed data | **none** |

---

## 4. Runtime Sync

| Item | Result |
|------|--------|
| Migration copied | **yes** (exact one file) |
| Runtime path | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\database\migrations\2026_07_25_000002_create_reporting_periods_table.sql` |
| Source/runtime checksum match | **yes** |
| `.env.local` | **untouched** |
| Broad sync | **no** |

---

## 5. Migration Apply

| Field | Result |
|-------|--------|
| Apply | **OK** — Applied count: 1 |
| Filename | `2026_07_25_000002_create_reporting_periods_table.sql` |
| Checksum | `5bc50e53ab20a347c8a278d1726be6c71d835b572f369a14d2256e3e986e3be9` |
| Batch | **2** |
| Ledger row | **present** |
| Idempotency second apply | `Nothing to apply. All migrations already applied.` |
| Status after | both migrations `[applied]` + `checksum_ok` |

---

## 6. DB Validation

| Check | Result |
|-------|--------|
| Migration count after | **2** |
| Table count after | **10** |
| Table exists | **yes** — `reporting_periods` |
| Columns | match DDL (types/nullability/defaults) |
| Indexes | PK, unique `(project_id, period_key)`, all required `idx_*` present |
| FKs | 5 present with expected ON DELETE rules |
| CHECK constraints | dates + status present |
| Row counts | users **1**; roles **6**; clients **0**; projects **0**; reporting_periods **0** |
| Unique/FK row smoke | **structural only** — no project fixture; no period insert |

---

## 7. Health/App Smoke

| Endpoint | Result |
|----------|--------|
| `GET /health` | **200**; DB connection pass; migration count **2**; latest migration = DB-03 file |
| Health tables present/expected | still `9 / 9` — expected HealthController limitation; **no code change** this wave |
| `GET /login` | **200** |
| `GET /not-existing` | **404** |
| Auth baseline | **not modified** |

---

## 8. Restrictions Confirmed

- no production DB
- no real client data
- no fixture rows
- no credentials in Git/report
- no password/hash in report
- no `.env` committed
- no source `.env.local`
- no auth/app code edits
- no DB dump
- no WordPress
- no Composer/npm
- no vhost/hosts/service restart
- no demo/registry changes
- no push/fetch/pull/reset/clean/stash

---

## 9. Documentation

| Artifact | Path |
|----------|------|
| Result doc | `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-MIGRATION-APPLY-RESULT-v0.1.md` |
| OPERATIONAL-INDEX | updated — DB-03 apply status + next stage |
| This closeout | `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-db03-reporting-periods-migration-apply-01.md` |

---

## 10. Commit

| Field | Value |
|-------|-------|
| Message | `feat(iseo-report-hub): add db03 reporting periods migration` |
| Exact-path git add | four allowlisted paths only |
| Staged list | migration SQL + apply result + this report + OPERATIONAL-INDEX |
| Commit hash | _pending primary commit_ |
| Hash-record follow-up | `docs(iseo-report-hub): record db03 reporting periods migration commit hash` (this report only) |
| HEAD verification | after commits |
| Push | **no** |

---

## 11. SAFE UNKNOWN

- Whether HealthController expected-table count will be raised in a later charter.
- Operator final choice if fixture charter is waived before any CRUD work.

---

## 12. Recommended Next Action

**Project/Client Local Fixture Charter 01** — unlock safe local `clients`/`projects` rows so unique/FK/CRUD smoke can run without real client data.

---

## 13. Files Changed

### Git (Active Brain)

- `projects/iseo-report-hub/app-source/database/migrations/2026_07_25_000002_create_reporting_periods_table.sql`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-MIGRATION-APPLY-RESULT-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-db03-reporting-periods-migration-apply-01.md`
- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`

### Runtime (outside Git)

- `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\database\migrations\2026_07_25_000002_create_reporting_periods_table.sql`

### DB mutation summary

- Created table `reporting_periods`
- Inserted `schema_migrations` ledger row for DB-03 (batch 2)
- No other table data changes; no fixture rows

---

## 14. Git Actions

| Action | Done? |
|--------|-------|
| exact-path git add | **yes** (allowlisted only) |
| commit | **yes** (primary + optional hash-record) |
| push | **no** |
| fetch | **no** |
| pull | **no** |
| checkout | **no** |
| reset | **no** |
| restore | **no** |
| clean | **no** |
| stash | **no** |
