# REPORT — I-SEO REPORT HUB DB-07 REPORT SNAPSHOTS MIGRATION APPLY 01

**project_id:** `iseo-report-hub`  
**Wave:** Report Snapshot DB-07 Migration Apply 01  
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
| HEAD before | `6cb66b545004993a22a92a2072fde78528e3ca7e` |
| Staged/index on main | **non-empty foreign-only** (client-ops-reporting-bridge); **no** `projects/iseo-report-hub/` staged |
| Clean temporary worktree used | **yes** — `X:\AI MARS STORAGE\git-sync-iseo-snapshot-db07-apply-01\repo` (detached at `6cb66b54`) |
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
| Migration count before | **5** |
| Table count before | **13** |
| `report_snapshots` before | **absent** |
| Baseline business counts | reporting_periods **2**; weekly_checkpoints **4**; monthly_report_contents **1**; report_blocks **6**; users **1**; roles **6**; clients/projects/sites **1/1/1** |
| Monthly id 1 before | status `finalized`; `finalized_at` non-null; title `…LOCAL_FIXTURE_ONLY` |
| Block statuses before | **6** `reviewed` (sort 15/20/30/35/40/50) |
| Runtime `.env.local` | **present** (contents not printed; not committed) |

---

## 3. Migration File

| Field | Value |
|-------|--------|
| Path | `projects/iseo-report-hub/app-source/database/migrations/2026_07_27_000006_create_report_snapshots_table.sql` |
| Checksum SHA-256 | `8f1890f6595f5f9fedb3f1366a5207fad9eca55f94dbcc549406313d192c6ab0` |
| Table | `report_snapshots` |
| Columns | 17 — see result doc |
| Indexes | `uq_report_snapshots_monthly_version`, `uq_report_snapshots_snapshot_key`, `idx_report_snapshots_monthly_status`, `idx_report_snapshots_period_status` (+ PK / FK index on `created_by`) |
| FKs | monthly → `monthly_report_contents`; period → `reporting_periods`; created_by → `users` |
| CHECK | `chk_report_snapshots_status`; `chk_report_snapshots_version` |

---

## 4. Runtime Sync

| Item | Result |
|------|--------|
| Migration file copied | **yes** → `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\database\migrations\2026_07_27_000006_create_report_snapshots_table.sql` |
| README sync | **yes** (migrations line only) |
| `.env.local` untouched | **yes** |
| Broad sync | **no** |

---

## 5. Migration Apply

| Field | Value |
|-------|--------|
| Tool | `php tools/db-migrate.php apply` (runtime) |
| DB target | `iseo_report_hub_dev` @ `127.0.0.1` |
| Migration recorded | **yes** — batch **6**; checksum match; executed_at `2026-07-27 02:04:39` |
| Credentials printed | **no** |

---

## 6. DB Validation

| Check | Result |
|-------|--------|
| Migrations | **5 → 6** |
| Tables | **13 → 14** |
| `report_snapshots` exists | **yes** |
| `report_snapshots` row count | **0** |
| Columns / indexes / FKs / CHECKs | **validated** |
| Existing business counts | **unchanged** (periods 2; weekly 4; monthly 1; blocks 6) |
| Monthly / block fingerprints | **unchanged** (`fed3ce67…2253` / `5edaad3b…b00b`) |
| Monthly status / finalized_at | `finalized` / non-null |
| All 6 blocks | `reviewed` |

---

## 7. Restrictions Confirmed

- no production DB; no remote DB; no real client data  
- no credentials / password / hash / session in Git or this report  
- no `.env` committed; no source `.env.local`; runtime `.env.local` not printed/committed  
- no app code edits; no auth/health/tool edits  
- no snapshot rows; no reporting_period / weekly / monthly / report_block row mutation  
- no DELETE / DROP / TRUNCATE; no DB dump  
- no WordPress; no Composer/npm; no vhost/hosts/service restart  
- no demo/registry changes  
- no push / fetch / pull / reset / clean / stash / broad git add  

---

## 8. Documentation

| Doc | Path |
|-----|------|
| Result | `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DB-07-REPORT-SNAPSHOTS-MIGRATION-APPLY-RESULT-v0.1.md` |
| Closeout | `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-db07-report-snapshots-migration-apply-01.md` |
| OPERATIONAL-INDEX | updated (migrations **6**; tables **14**; `report_snapshots` empty; next = Snapshot Implementation 01) |
| app-source README | migrations line includes `report_snapshots` |

---

## 9. Commit

| Field | Value |
|-------|--------|
| Exact-path git add | **yes** (allowlisted paths in clean worktree) |
| Staged list | migration SQL; app-source README; result doc; this report; OPERATIONAL-INDEX |
| Primary commit hash | `eb1d0ce544f42876a99ea4393a98ffa780bb6f1f` |
| Primary message | `feat(iseo-report-hub): add report snapshots migration` |
| Hash-record commit | `PENDING_HASH_RECORD` — `docs(iseo-report-hub): record report snapshots migration commit hash` |
| HEAD after wave | `PENDING_HEAD_AFTER` |
| Push | **no** |

---

## 10. SAFE UNKNOWN

- Whether Implementation 01 creates first active snapshot for monthly id 1 in the same wave as service/routes, or splits create-smoke — not decided here.
- Multi-role HTTP create/view smoke may remain deferred if only admin_owner session injection exists.

---

## 11. Recommended Next Action

**I-SEO Report Hub — Report Snapshot Implementation 01**

---

## 12. Files Changed

Git (Active Brain):

- `projects/iseo-report-hub/app-source/database/migrations/2026_07_27_000006_create_report_snapshots_table.sql`
- `projects/iseo-report-hub/app-source/README.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DB-07-REPORT-SNAPSHOTS-MIGRATION-APPLY-RESULT-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-db07-report-snapshots-migration-apply-01.md`
- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`

Runtime (exact sync, not Git):

- `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\database\migrations\2026_07_27_000006_create_report_snapshots_table.sql`
- `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\README.md`

DB summary: `iseo_report_hub_dev` @ `127.0.0.1` — migrations **6**; tables **14**; `report_snapshots` **0** rows; business rows unchanged.

---

## 13. Git Actions

| Action | Result |
|--------|--------|
| exact-path git add | **yes** (allowlisted i-SEO paths in clean worktree) |
| commit | **yes** (primary + hash-record; see §9) |
| push | **no** |
| fetch | **no** |
| pull | **no** |
| checkout / update-ref | worktree add `--detach` at `6cb66b54`; FF `update-ref` `mars/canonical-post-recovery` → wave HEAD after commits |
| reset | **no** |
| restore | **scoped only** on main — allowlisted i-SEO paths aligned to HEAD after update-ref; foreign staged untouched |
| clean | **no** |
| stash | **no** |
| broad git add | **no** |
| clean temporary worktree | used: `X:\AI MARS STORAGE\git-sync-iseo-snapshot-db07-apply-01\repo`; main foreign index preserved |
