# REPORT — I-SEO REPORT HUB DB-08 REPORT EXPORTS MIGRATION APPLY 01

**project_id:** `iseo-report-hub`  
**Wave:** Report Export DB-08 Migration Apply 01  
**Date:** 2026-07-27  
**Status:** COMPLETE

---

## 1. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive | `X:` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD before | `f1d590096c924f5ef007e73bbcd455c31608dc03` |
| Staged/index on main | **non-empty foreign-only** (client-ops-reporting-bridge); **no** `projects/iseo-report-hub/` staged |
| Clean temporary worktree used | **yes** — `X:\AI MARS STORAGE\git-sync-iseo-export-db08-apply-01\repo` (detached at `f1d59009`) |
| i-SEO WIP clean before | **yes** |
| Foreign WIP preserved | **yes** (main index untouched) |
| Write scope | migration SQL + app-source README + result/report docs + OPERATIONAL-INDEX; runtime exact migration (+ README) sync; local DB schema only |

---

## 2. Preflight

| Check | Result |
|-------|--------|
| PHP executable | `X:\MARS-Localhost\laragon\bin\php\php-8.3.30-Win32-vs16-x64\php.exe` (present) |
| DB target | `iseo_report_hub_dev` |
| DB host | `127.0.0.1` |
| Migration count before | **6** |
| Table count before | **14** |
| `report_exports` before | **absent** |
| Baseline business counts | reporting_periods **2**; weekly_checkpoints **4**; monthly_report_contents **1**; report_blocks **6**; report_snapshots **1**; users **1**; roles **6**; clients/projects/sites **1/1/1** |
| Snapshot id 1 before | status `active`; key `monthly-1-v1`; checksum `0d0c863c5c283edf508aa2fb52a96acb57c6b358e0f45ac7582c970a03997a38` |
| Monthly id 1 before | status `finalized`; `finalized_at` non-null; title `…LOCAL_FIXTURE_ONLY` |
| Block statuses before | **6** `reviewed` (sort 15/20/30/35/40/50) |
| Runtime `.env.local` | **present** (contents not printed; not committed) |

---

## 3. Migration File

| Field | Value |
|-------|--------|
| Path | `projects/iseo-report-hub/app-source/database/migrations/2026_07_27_000007_create_report_exports_table.sql` |
| Checksum SHA-256 | `130e1b2f0a58a5661f0be99aa254e628186c1df6e6252acabbdf97ffe5877baa` |
| Table | `report_exports` |
| Columns | 16 — see result doc |
| Indexes | `uq_report_exports_export_key`, `idx_report_exports_snapshot_format_status`, `idx_report_exports_monthly_format_status` (+ PK / FK index on `created_by`) |
| FKs | snapshot → `report_snapshots`; monthly → `monthly_report_contents`; created_by → `users` |
| CHECK | `chk_report_exports_format`; `chk_report_exports_status` |

---

## 4. Runtime Sync

| Item | Result |
|------|--------|
| Migration file copied | **yes** → `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\database\migrations\2026_07_27_000007_create_report_exports_table.sql` |
| README sync | **yes** (migrations line only) |
| `.env.local` untouched | **yes** |
| Broad sync | **no** |

---

## 5. Migration Apply

| Field | Value |
|-------|--------|
| Tool | `php tools/db-migrate.php apply` (runtime) |
| DB target | `iseo_report_hub_dev` @ `127.0.0.1` |
| Migration recorded | **yes** — batch **7**; checksum match; executed_at `2026-07-27 14:03:45` |
| Credentials printed | **no** |

---

## 6. DB Validation

| Check | Result |
|-------|--------|
| Migrations | **6 → 7** |
| Tables | **14 → 15** |
| `report_exports` exists | **yes** |
| `report_exports` row count | **0** |
| Columns / indexes / FKs / CHECKs | **validated** |
| Existing business counts | **unchanged** (periods 2; weekly 4; monthly 1; blocks 6; snapshots 1) |
| Snapshot id 1 | `active`; checksum `0d0c863c5c283edf508aa2fb52a96acb57c6b358e0f45ac7582c970a03997a38` (unchanged) |
| Monthly id 1 | `finalized` / `finalized_at` non-null (unchanged) |
| All 6 blocks | `reviewed` (unchanged) |
| No export storage files/dirs | **yes** (`storage/exports` absent) |

---

## 7. Restrictions Confirmed

- no production DB; no remote DB; no real client data  
- no credentials / password / hash / session in Git or this report  
- no `.env` committed; no source `.env.local`; runtime `.env.local` not printed/committed  
- no app code edits; no auth/health/tool edits (temp validation scripts removed; not committed)  
- no export rows; no export files  
- no reporting_period / weekly / monthly / report_block / report_snapshot row mutation  
- no DELETE / DROP / TRUNCATE; no DB dump  
- no WordPress; no Composer/npm; no vhost/hosts/service restart  
- no demo/registry changes  
- no push / fetch / pull / reset / clean / stash / broad git add  

---

## 8. Documentation

| Doc | Path |
|-----|------|
| Result | `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DB-08-REPORT-EXPORTS-MIGRATION-APPLY-RESULT-v0.1.md` |
| Closeout | `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-db08-report-exports-migration-apply-01.md` |
| OPERATIONAL-INDEX | updated (migrations **7**; tables **15**; `report_exports` empty; next = HTML Artifact Implementation 01) |
| app-source README | migrations line includes `report_exports` |

---

## 9. Commit

| Field | Value |
|-------|--------|
| Exact-path git add | **yes** (allowlisted paths in clean worktree) |
| Staged list | migration SQL; app-source README; result doc; this report; OPERATIONAL-INDEX |
| Primary commit hash | `7b059bb285452735a5834bb1a5789d22e6733d06` |
| Primary message | `feat(iseo-report-hub): add report exports migration` |
| Hash-record commit | `e0a13795c1d71aa37fadad973bc63733b91a8fa7` — `docs(iseo-report-hub): record report exports migration commit hash` |
| HEAD after wave | `e0a13795c1d71aa37fadad973bc63733b91a8fa7` |
| Push | **no** |

---

## 10. SAFE UNKNOWN

- Whether HTML Implementation 01 creates first `report_exports` row for snapshot id 1 in the same wave as artifact file write — not decided here.
- PDF export timing (post-HTML vs separate charter) — deferred per Export/PDF charter.

---

## 11. Recommended Next Action

**I-SEO Report Hub — Report Export HTML Artifact Implementation 01**

---

## 12. Files Changed

Git (Active Brain):

- `projects/iseo-report-hub/app-source/database/migrations/2026_07_27_000007_create_report_exports_table.sql`
- `projects/iseo-report-hub/app-source/README.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DB-08-REPORT-EXPORTS-MIGRATION-APPLY-RESULT-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-db08-report-exports-migration-apply-01.md`
- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`

Runtime (exact sync, not Git):

- `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\database\migrations\2026_07_27_000007_create_report_exports_table.sql`
- `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\README.md`

DB summary: `iseo_report_hub_dev` @ `127.0.0.1` — migrations **7**; tables **15**; `report_exports` **0** rows; business rows unchanged.

---

## 13. Git Actions

| Action | Result |
|--------|--------|
| exact-path git add | **yes** (allowlisted i-SEO paths in clean worktree) |
| commit | **yes** (primary + hash-record; see §9) |
| push | **no** |
| fetch | **no** |
| pull | **no** |
| checkout / update-ref | worktree add `--detach` at `f1d59009`; FF `update-ref` `mars/canonical-post-recovery` → wave HEAD after commits |
| reset | **no** |
| restore | **scoped only** on main — allowlisted i-SEO paths aligned to HEAD after update-ref; foreign staged untouched |
| clean | **no** |
| stash | **no** |
| broad git add | **no** |
| clean temporary worktree | used: `X:\AI MARS STORAGE\git-sync-iseo-export-db08-apply-01\repo`; main foreign index preserved |
