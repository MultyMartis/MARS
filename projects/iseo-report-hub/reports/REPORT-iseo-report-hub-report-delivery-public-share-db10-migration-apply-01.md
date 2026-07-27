# REPORT — I-SEO REPORT HUB REPORT DELIVERY PUBLIC SHARE DB-10 MIGRATION APPLY 01

**Status:** COMPLETE  
**Date:** 2026-07-27  
**Programme:** i-SEO Report Hub  
**Wave:** Report Delivery Public Share DB-10 Migration Apply 01

---

## 1. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive | `X:` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD before | `465a63e88d3e4847e1b50c37ef64d6ee22f110c5` |
| Staged/index state | non-empty foreign staged (client-ops); **no** `projects/iseo-report-hub/` staged |
| Clean temporary worktree used | **yes** — `X:\AI MARS STORAGE\git-sync-iseo-report-delivery-public-share-db10-apply-01\repo` |
| i-SEO WIP clean before | **yes** |
| Foreign WIP preserved | **yes** (main index untouched for foreign paths) |
| Write scope | allowlisted migration + docs under `projects/iseo-report-hub/`; runtime migration file only; temp smoke under STORAGE incoming |

---

## 2. Preflight

| Check | Result |
|-------|--------|
| PHP executable | `X:\MARS-Localhost\laragon\bin\php\php-8.3.30-Win32-vs16-x64\php.exe` present |
| DB target | `iseo_report_hub_dev` |
| DB host | `127.0.0.1` |
| Migration count before | **8** |
| Table count before | **15** |
| `report_exports` count before | **4** (html **2**, pdf **2**) |
| Export ids 1–4 before | present; status `ready`; DB-09 columns present |
| `report_export_shares` absent before | **yes** |
| Migration `000009` absent before | file + ledger absent |
| Artifact checksums before | v1/v2 HTML/PDF match expected; `%PDF-` PASS |
| Runtime `.env.local` | **present** (redacted; not printed; not committed) |

---

## 3. Migration File

| Field | Value |
|-------|-------|
| Source path | `projects/iseo-report-hub/app-source/database/migrations/2026_07_27_000009_create_report_export_shares_table.sql` |
| Runtime path | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\database\migrations\2026_07_27_000009_create_report_export_shares_table.sql` |
| Checksum | `384fbb48cccc55989035056c899af701f0dbb49e2c362b44a23acaf656ba82d3` |
| Columns | 16 columns as specified (token hash only; no plaintext token column) |
| Indexes | unique `uq_report_export_shares_token_hash`; export/status; expires/status; created_by; revoked_by |
| FKs | export RESTRICT; created_by SET NULL; revoked_by SET NULL |
| CHECK | `chk_report_export_shares_status` (`active`,`revoked`,`expired`) |
| Syntax | matches prior migration style (`SET NAMES`; statement-splittable `;`; CREATE TABLE only; no DROP) |

---

## 4. Migration Apply

| Field | Value |
|-------|--------|
| Command class | runtime `php tools/db-migrate.php apply` |
| Result | **OK** — Applied count **1** |
| `schema_migrations` before/after | **8 → 9** |
| Table count before/after | **15 → 16** |
| Migration record | `2026_07_27_000009_create_report_export_shares_table.sql` batch **9**; `checksum_ok` |

---

## 5. DB Validation

| Check | Result |
|-------|--------|
| Share table columns | all 16 present; types/nullability/defaults match |
| Indexes | all required present (incl. unique token_hash) |
| FKs | three FKs present with expected DELETE rules |
| CHECK | `chk_report_export_shares_status` present |
| Share row count | **0** |
| Counts unchanged | report_exports **4**; business tables unchanged |
| No DELETE/DROP/TRUNCATE | **confirmed** (CREATE TABLE allowed) |

---

## 6. Artifact Validation

| Artifact | Checksum | Status |
|----------|----------|--------|
| v1 HTML | `c194c62b81c6ec04a52a651a24263e54e33d9cac2aa0453f3a95214b626fadc4` | unchanged |
| v1 PDF | `707e72d65f253de17070980e2be36b91f59c4e6faf4352e73d3b1849880d0320` | unchanged; `%PDF-` |
| v2 HTML | `27a6eee6f6729f5a081865a24aa1e4ca1f94554ff38d4a1278682f16f95f6ffe` | unchanged |
| v2 PDF | `a8c4d61c6216e8d70b193115faeab345c0c61ed25ee97a96b740f5f041a56b6b` | unchanged; `%PDF-` |

No new artifacts. Outside `public/` and Git.

---

## 7. HTTP / Regression

| Field | Value |
|-------|--------|
| Server method | temporary PHP built-in `-S 127.0.0.1:8092` docroot `public/` |
| Routes | `/health` 200; auth exports list 200; auth details 1–4 200; downloads 1–4 200 |
| Downloads | HTML/PDF Content-Type OK |
| `/share` | **404** |
| `/share/report/test-token` | **404** |
| Summary | **13/13 PASS** |
| No public/share implementation | **confirmed** |

---

## 8. Restrictions Confirmed

- no production DB; no remote DB
- no real data beyond fixture
- no credentials in Git/report
- no password/hash/session in report
- no `.env` committed; no source `.env.local`
- no app code edits; no auth/health edits; no fixture tool changes
- no reporting_period / weekly_checkpoint / monthly_report_contents / report_blocks / report_snapshots / report_exports row mutation
- no `report_export_shares` row insert; no share token creation
- no public route; no new export rows; no HTML/PDF artifact overwrite
- no DELETE/DROP/TRUNCATE; no DB dump
- no WordPress; no Composer/npm/package install
- no vhost/hosts/service restart; no demo/registry changes
- no push/fetch/pull/reset/clean/stash; no broad git add

---

## 9. Documentation

| Doc | Path |
|-----|------|
| Result | `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-DB10-MIGRATION-APPLY-RESULT-v0.1.md` |
| OPERATIONAL-INDEX | updated (DB-10 Apply status; next Implementation 01) |
| app-source README | DB-10 status note |
| Closeout | this report |

---

## 10. Commit

| Field | Value |
|-------|--------|
| Exact-path git add | allowlisted migration + README + result + OPERATIONAL-INDEX + this report (worktree) |
| Staged list | see section 14 / post-commit verification |
| Primary commit hash | `PENDING_PRIMARY` |
| Primary message | `feat(iseo-report-hub): add public share migration` |
| Hash-record commit | `PENDING_HASH_RECORD` — `docs(iseo-report-hub): record public share migration commit hash` |
| HEAD verification | after commits |
| Push | **no** |

---

## 11. SAFE UNKNOWN

- Laragon Apache port 80 listen state during smoke (used PHP `-S` **8092**).
- Operator retention of STORAGE incoming temp smoke scripts.

---

## 12. Recommended Next Action

**I-SEO Report Hub — Report Delivery Public Share Implementation 01**

---

## 13. Files Changed

### Git (allowlisted)

- `projects/iseo-report-hub/app-source/database/migrations/2026_07_27_000009_create_report_export_shares_table.sql`
- `projects/iseo-report-hub/app-source/README.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-DB10-MIGRATION-APPLY-RESULT-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-report-delivery-public-share-db10-migration-apply-01.md`
- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`

### Runtime (not Git)

- `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\database\migrations\2026_07_27_000009_create_report_export_shares_table.sql`

### DB summary

- `schema_migrations` **9**; tables **16**; `report_export_shares` exists with **0** rows; business counts unchanged

---

## 14. Git Actions

| Action | Done? |
|--------|-------|
| exact-path git add | **yes** (worktree allowlist) |
| commit | **yes** (primary + hash-record) |
| push | **no** |
| fetch | **no** |
| pull | **no** |
| checkout / update-ref | worktree create; post-commit `update-ref` main → new tip if safe |
| reset | **no** |
| restore | scoped main restore of i-SEO allowlisted paths if needed after update-ref |
| clean | **no** |
| stash | **no** |
| broad git add | **no** |
| clean temporary worktree | used for commit; leave path for operator |
