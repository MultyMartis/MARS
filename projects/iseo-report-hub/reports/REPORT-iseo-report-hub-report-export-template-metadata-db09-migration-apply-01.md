# REPORT — I-SEO REPORT HUB REPORT EXPORT TEMPLATE METADATA DB-09 MIGRATION APPLY 01

**Status:** COMPLETE  
**Date:** 2026-07-27  
**Programme:** i-SEO Report Hub  
**Wave:** Report Export Template Metadata DB-09 Migration Apply 01

---

## 1. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive | `X:` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD before | `7f03af180d18d835cd8c8741eb58a5c4918f6067` |
| Staged/index state | non-empty foreign staged (client-ops); **no** `projects/iseo-report-hub/` staged |
| Clean temporary worktree used | **yes** — `X:\AI MARS STORAGE\git-sync-iseo-report-export-template-metadata-db09-apply-01\repo` |
| i-SEO WIP clean before | **yes** |
| Foreign WIP preserved | **yes** (main index untouched for foreign paths) |
| Write scope | allowlisted migration + docs under `projects/iseo-report-hub/`; runtime migration file only; temp scripts under STORAGE incoming |

---

## 2. Preflight

| Check | Result |
|-------|--------|
| PHP executable | `X:\MARS-Localhost\laragon\bin\php\php-8.3.30-Win32-vs16-x64\php.exe` present |
| DB target | `iseo_report_hub_dev` |
| DB host | `127.0.0.1` |
| Migration count before | **7** |
| Table count before | **15** |
| `report_exports` count before | **4** (html **2**, pdf **2**) |
| Export ids 1–4 before | present; keys/checksums match baseline |
| DB-09 columns absent before | **yes** |
| Migration `000008` absent before | file + ledger absent |
| Artifact checksums before | v1/v2 HTML/PDF match expected; `%PDF` PASS |
| Runtime `.env.local` | **present** (redacted; not printed; not committed) |

---

## 3. Migration File

| Field | Value |
|-------|-------|
| Source path | `projects/iseo-report-hub/app-source/database/migrations/2026_07_27_000008_add_template_metadata_to_report_exports_table.sql` |
| Runtime path | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\database\migrations\2026_07_27_000008_add_template_metadata_to_report_exports_table.sql` |
| Checksum | `75202829747e4a15138e2a89760fc68995e5e2cc56f1b20b80664f7a08eb37d0` |
| Columns | `template_id`, `template_version`, `render_target`, `render_engine`, `render_options_json`, `source_html_export_id`, `metadata_json` (all NULL-able; after `source_snapshot_checksum_sha256`) |
| Indexes | `idx_report_exports_template`; `idx_report_exports_source_html` |
| FK | `fk_report_exports_source_html_export` → `report_exports(id)` ON DELETE SET NULL |
| Syntax | matches prior migration style (`SET NAMES`; statement-splittable `;`; no DROP) |

---

## 4. Migration Apply

| Field | Value |
|-------|--------|
| Command class | runtime `php tools/db-migrate.php apply` |
| Result | **OK** — Applied count **1** |
| `schema_migrations` before/after | **7 → 8** |
| Table count before/after | **15 → 15** |
| Migration record | `2026_07_27_000008_add_template_metadata_to_report_exports_table.sql` batch **8**; `checksum_ok` |

---

## 5. Backfill

| Field | Value |
|-------|--------|
| Method | temp PHP gated UPDATEs under `X:\AI MARS STORAGE\incoming\iseo-report-hub\db09-metadata-apply-01\` (not committed) |
| Exact gates | id + export_key + format + status + checksum; row 3 verified before row 4 |
| id 1 policy | metadata left **NULL** (no UPDATE) |
| id 2 policy | metadata left **NULL** (no UPDATE) |
| id 3 update | `iseo_default_v1` / `1` / `html_export` / `php_template_renderer` / `source_html_export_id=NULL` + JSON |
| id 4 update | `iseo_default_v1` / `1` / `pdf_export` / `edge_headless_pdf` / `source_html_export_id=3` + JSON |
| Affected rows | id 3: **1** then already-matched; id 4: **1** after EXISTS self-join removed (MySQL 1093); idempotent re-run **0/0** |
| Temp script path/status | `...\db09-metadata-apply-01\backfill-db09.php` — outside Git; retained under STORAGE incoming |

---

## 6. DB Validation

| Check | Result |
|-------|--------|
| Schema columns | all 7 present; varchar/json/bigint unsigned; nullable YES |
| Indexes | both present |
| FK | present; DELETE_RULE **SET NULL**; references `report_exports.id` |
| Row metadata matrix | 1–2 NULL; 3 HTML metadata; 4 PDF metadata + source 3 |
| Counts unchanged | report_exports **4**; business tables unchanged |
| No DELETE/DROP/TRUNCATE | **confirmed** |

---

## 7. Artifact Validation

| Artifact | Checksum | Status |
|----------|----------|--------|
| v1 HTML | `c194c62b81c6ec04a52a651a24263e54e33d9cac2aa0453f3a95214b626fadc4` | unchanged |
| v1 PDF | `707e72d65f253de17070980e2be36b91f59c4e6faf4352e73d3b1849880d0320` | unchanged; `%PDF` |
| v2 HTML | `27a6eee6f6729f5a081865a24aa1e4ca1f94554ff38d4a1278682f16f95f6ffe` | unchanged |
| v2 PDF | `a8c4d61c6216e8d70b193115faeab345c0c61ed25ee97a96b740f5f041a56b6b` | unchanged; `%PDF` |

No new artifacts. Outside `public/` and Git.

---

## 8. HTTP / Regression

| Field | Value |
|-------|--------|
| Server method | temporary PHP built-in `-S 127.0.0.1:8092` docroot `public/` |
| Routes | `/health` 200; auth exports list 200; auth details 1–4 200; downloads 1–4 200 |
| Downloads | HTML/PDF Content-Type OK |
| No public/share | `/share` **404** |
| Summary | **12/12 PASS** |

---

## 9. Restrictions Confirmed

- no production DB; no real data beyond fixture
- no credentials / password / hash / session in Git or report
- no `.env` committed; no source `.env.local`; runtime `.env.local` not printed/committed
- no app code / auth / health / fixture tool edits
- no reporting_period / weekly / monthly / blocks / snapshots row mutation
- no report_exports insert/delete; no v1 metadata backfill
- no new export rows; no HTML/PDF artifact overwrite
- no DELETE/DROP/TRUNCATE; no DB dump
- no WordPress; no Composer/npm/package install
- no vhost/hosts/service restart; no demo/registry changes
- no push/fetch/pull/reset/clean/stash; no broad git add

---

## 10. Documentation

| Doc | Path |
|-----|------|
| Result | `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-MIGRATION-APPLY-RESULT-v0.1.md` |
| OPERATIONAL-INDEX | updated (Apply status, matrix, next UI stage) |
| Closeout | this report |

---

## 11. Commit

| Field | Value |
|-------|--------|
| Exact-path git add | allowlisted migration + README + result + OPERATIONAL-INDEX + this report (worktree) |
| Staged list | see section 14 / post-commit verification |
| Primary commit hash | `c1e7ba2416f1e49ef0f115d0efa23ffcb7abd317` |
| Primary message | `feat(iseo-report-hub): add export template metadata migration` |
| Hash-record commit | `11e2c84a095a80692f62d0f4a106fb331475240f` — `docs(iseo-report-hub): record export template metadata migration commit hash` |
| HEAD verification | after commits |
| Push | **no** |

---

## 12. SAFE UNKNOWN

- Laragon Apache port 80 listen state during smoke (used PHP `-S` **8092**).
- Operator retention of STORAGE incoming temp scripts.

---

## 13. Recommended Next Action

**I-SEO Report Hub — Report Export Template Metadata UI Implementation 01**

---

## 14. Files Changed

### Git (allowlisted)

- `projects/iseo-report-hub/app-source/database/migrations/2026_07_27_000008_add_template_metadata_to_report_exports_table.sql`
- `projects/iseo-report-hub/app-source/README.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-MIGRATION-APPLY-RESULT-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-report-export-template-metadata-db09-migration-apply-01.md`
- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`

### Runtime (not Git)

- `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\database\migrations\2026_07_27_000008_add_template_metadata_to_report_exports_table.sql`

### DB summary

- `schema_migrations` **8**; `report_exports` schema + backfill ids **3–4**; counts otherwise unchanged

---

## 15. Git Actions

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
