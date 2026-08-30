# I-SEO Report Hub — Report Delivery Public Share DB-10 Migration Apply Result v0.1

**Date:** 2026-07-27  
**Programme:** i-SEO Report Hub  
**Wave:** Report Delivery Public Share DB-10 Migration Apply 01  
**DB target:** `iseo_report_hub_dev` @ `127.0.0.1` only

---

## 1. Status

| Field | Value |
|-------|-------|
| Status | **complete** |
| Migration applied | **yes** |
| Final `schema_migrations` count | **9** |
| Final table count | **16** |
| `report_export_shares` exists | **yes** |
| Share rows count | **0** |
| `report_exports` count unchanged | **yes** (4) |
| Artifact checksums unchanged | **yes** |
| No public/share implementation | **yes** |
| No token created | **yes** |
| No package install | **yes** |

---

## 2. Migration

| Field | Value |
|-------|-------|
| Filename | `2026_07_27_000009_create_report_export_shares_table.sql` |
| Checksum (SHA-256) | `384fbb48cccc55989035056c899af701f0dbb49e2c362b44a23acaf656ba82d3` |
| Table created | `report_export_shares` |
| Columns | `id`, `report_export_id`, `token_hash`, `token_label`, `status`, `expires_at`, `revoked_at`, `revoked_by`, `created_by`, `created_at`, `last_accessed_at`, `access_count`, `max_access_count`, `last_access_ip_hash`, `last_user_agent_hash`, `metadata_json` |
| Indexes | `PRIMARY`; unique `uq_report_export_shares_token_hash`; `idx_report_export_shares_export_status`; `idx_report_export_shares_expires_status`; `idx_report_export_shares_created_by`; `idx_report_export_shares_revoked_by` |
| FKs | `fk_report_export_shares_export` → `report_exports(id)` ON DELETE RESTRICT; `fk_report_export_shares_created_by` → `users(id)` ON DELETE SET NULL; `fk_report_export_shares_revoked_by` → `users(id)` ON DELETE SET NULL |
| CHECK | `chk_report_export_shares_status` — `status` IN (`active`,`revoked`,`expired`) |
| Engine / collation | InnoDB / `utf8mb4_0900_ai_ci` |
| `schema_migrations` before/after | **8 → 9** (batch **9**) |

---

## 3. Runtime Sync

| Field | Value |
|-------|-------|
| Source migration path | `projects/iseo-report-hub/app-source/database/migrations/2026_07_27_000009_create_report_export_shares_table.sql` |
| Runtime migration path | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\database\migrations\2026_07_27_000009_create_report_export_shares_table.sql` |
| Source/runtime checksum match | **yes** |
| `.env.local` untouched | **yes** (present; not printed; not committed) |
| Broad sync | **no** — migration file only |

---

## 4. DB Validation

| Check | Before | After |
|-------|--------|-------|
| `schema_migrations` | 8 | 9 |
| tables | 15 | 16 |
| `report_export_shares` | absent | present; rows **0** |
| `report_exports` | 4 | 4 |
| html / pdf export rows | 2 / 2 | 2 / 2 |
| users / roles | 1 / 6 | 1 / 6 |
| clients / projects / sites | 1 / 1 / 1 | 1 / 1 / 1 |
| reporting_periods | 2 | 2 |
| weekly_checkpoints | 4 | 4 |
| monthly_report_contents | 1 | 1 |
| report_blocks | 6 | 6 |
| report_snapshots | 1 | 1 |

Columns, indexes, FKs, and status CHECK introspected and match migration. Business tables unchanged. No share row insert. No `report_exports` mutation. No DELETE/DROP/TRUNCATE.

---

## 5. Artifact Validation

| Artifact | Path (runtime) | Checksum | Status |
|----------|----------------|----------|--------|
| v1 HTML | `storage/exports/reports/monthly-1/snapshot-1/monthly-1-v1.html` | `c194c62b81c6ec04a52a651a24263e54e33d9cac2aa0453f3a95214b626fadc4` | unchanged |
| v1 PDF | `storage/exports/reports/monthly-1/snapshot-1/monthly-1-v1.pdf` | `707e72d65f253de17070980e2be36b91f59c4e6faf4352e73d3b1849880d0320` | unchanged; `%PDF-` |
| v2 HTML | `storage/exports/reports/monthly-1/snapshot-1/monthly-1-v2.html` | `27a6eee6f6729f5a081865a24aa1e4ca1f94554ff38d4a1278682f16f95f6ffe` | unchanged |
| v2 PDF | `storage/exports/reports/monthly-1/snapshot-1/monthly-1-v2.pdf` | `a8c4d61c6216e8d70b193115faeab345c0c61ed25ee97a96b740f5f041a56b6b` | unchanged; `%PDF-` |

Artifact file count remains **4**. No new artifacts. Outside `public/` and outside Git (`X:\AI MARS`).

---

## 6. HTTP / Regression

Temporary PHP built-in server `127.0.0.1:8092` (docroot `public/`). Session inject for local admin (no password/session printed).

| Check | Result |
|-------|--------|
| `GET /health` | 200 |
| auth `GET /report-snapshots/1/exports` | 200 |
| auth `GET /report-exports/{1..4}` | 200 |
| auth downloads 1–4 | 200; HTML/PDF Content-Type OK |
| `GET /share` | **404** |
| `GET /share/report/test-token` | **404** |
| Summary | **13/13 PASS** |

No public share route implemented. No app code changed this wave.

---

## 7. Restrictions

- no production / remote DB
- no real data beyond existing LOCAL_FIXTURE_ONLY fixture exports
- no app code edits (`app/**`, tools, controllers)
- no share row / token creation
- no public route / service / UI
- no `report_exports` row mutation
- no artifact regeneration/overwrite
- no package install/download
- no secrets / credentials / password / hash / session in Git or reports
- no `.env` / source `.env.local`; runtime `.env.local` untouched and uncommitted
- no DROP/TRUNCATE/DELETE; CREATE TABLE via migration only
- no push / fetch / pull / reset / clean / stash / broad git add

---

## 8. What Still Does Not Exist

- share service / repository / controller
- token creation / revoke UI
- public `GET /share/report/{token}` implementation
- access-count / audit event writers
- email delivery
- client portal
- short `/r/{token}` route
- production deployment

---

## 9. Next Phase

**I-SEO Report Hub — Report Delivery Public Share Implementation 01**

---

## 10. SAFE UNKNOWN

- Whether Laragon Apache on port 80 was listening during this wave (smoke used temporary PHP `-S` on **8092**, consistent with prior waves).
- Exact future plaintext token encoding / URL presentation format (policy exists; implementation deferred).
