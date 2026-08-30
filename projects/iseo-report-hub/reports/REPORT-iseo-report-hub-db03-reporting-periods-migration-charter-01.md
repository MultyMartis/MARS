# REPORT — I-SEO REPORT HUB DB-03 REPORTING PERIODS MIGRATION CHARTER 01

**project_id:** `iseo-report-hub`  
**Wave:** DB-03 Reporting Periods Migration Charter 01  
**Date:** 2026-07-25  
**Type:** documentation / policy only  

---

## 1. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive | `X:` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD before | `ee065a77696528b8c8bcb2935f024ec4331e5a4a` |
| HEAD after commit | `51f3c1f6cd59665c4d59b5227b73c3764859a887` |
| Staged / index (pre-write) | **Empty** |
| i-SEO WIP clean before | **Yes** (no modified/untracked under `projects/iseo-report-hub/`) |
| Foreign WIP | **Preserved** (not staged, not restored, not cleaned) |
| Write scope | Active Brain i-SEO Report Hub allowlisted docs only (7 paths) |

---

## 2. Baseline Reviewed

| Item | Value |
|------|-------|
| Auth implementation commit | `d4b3b2e2155f41e8f99d4ac56a47de870ea6b10c` — `feat(iseo-report-hub): add auth persistence bootstrap` |
| Auth hash-record follow-up | `0cd2cfb7735e59d3d54bf8dd9002ba45949dd47d` — `docs(iseo-report-hub): record auth persistence bootstrap commit hash` |
| Auth commits ancestor of HEAD | **Yes** |
| DB | `iseo_report_hub_dev` @ `127.0.0.1` |
| First migration | `2026_07_24_000001_create_core_tables.sql` |
| Checksum | `71dd22d0a0a0af14854b4b40d72ae611c80d74af8bfe038a413110b0be722bb4` |
| Migration count | **1** |
| Tables count | **9** |
| Current tables | `schema_migrations`, `users`, `roles`, `user_roles`, `audit_log`, `clients`, `projects`, `sites`, `project_type_profiles` |
| Users / roles | **1** / **6** (read-only check) |
| Clients / projects | **0** / **0** |
| `reporting_periods` | **Absent** (expected) |
| Local admin | `admin@iseo-report-hub.test` (password/hash not recorded) |
| Auth smoke (prior wave) | **PASS** |

Docs / code reviewed (read-only): product charter, MVP scope, report model, DB creation charter, migration policy, initial schema plan, auth implementation result, DB-01/DB-02 apply report, OPERATIONAL-INDEX, README, migration SQL `000001`, `db-migrate.php`, `DatabaseService`, `AuthService`, `HealthController`.

---

## 3. Charter Output

Created:

- `product/I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-CHARTER-v0.1.md`
- `product/I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-SCHEMA-PLAN-v0.1.md`
- `product/I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-MIGRATION-PLAN-v0.1.md`
- `product/I-SEO-REPORT-HUB-REPORTING-PERIOD-LIFECYCLE-v0.1.md`
- `product/I-SEO-REPORT-HUB-DB-03-IMPLEMENTATION-PLAN-v0.1.md`
- `reports/REPORT-iseo-report-hub-db03-reporting-periods-migration-charter-01.md`

Updated:

- `OPERATIONAL-INDEX.md` — DB-03 charter status; auth baseline dependency; next apply candidate; note that no SQL/app/runtime/DB changes in this wave

---

## 4. DB-03 Design Summary

| Topic | Decision |
|-------|----------|
| Table | `reporting_periods` only |
| Ownership | Period → project → client; site → project |
| Statuses | `draft`, `active`, `weekly_review`, `monthly_review`, `finalized`, `archived` |
| Unique | `(project_id, period_key)` |
| FKs | `project_id` → `projects`; nullable user FKs for owner/reviewer/created_by/updated_by |
| Indexes | project_id, period_key, status, owner_user_id, reviewer_user_id, finalized_at, created_at (+ unique) |
| Deferred DB-04+ | `weekly_checkpoints`, `monthly_reports`, blocks/KPI/evidence/snapshots; no denormalized week_*_status columns |

---

## 5. Validation Plan

| Gate | Plan |
|------|------|
| Migration apply | `db-migrate.php apply` on local `iseo_report_hub_dev` |
| Ledger | New row for `2026_07_25_000002_create_reporting_periods_table.sql` |
| Idempotency | Re-apply no-op; checksum mismatch STOP |
| Structure | Table + columns + indexes/unique/FK |
| Unique smoke | Duplicate project/period_key refused (if safe project exists) |
| Empty projects | Structure-only OK (current baseline: projects=0) |
| Health | After apply, migration/table counts may increment; no health code edit in charter wave |

---

## 6. Restrictions Confirmed

| Restriction | Confirmed |
|-------------|-----------|
| No app-source edits | **Yes** |
| No runtime edits | **Yes** |
| No DB mutation | **Yes** (read-only status/counts only) |
| No SQL/migration file creation | **Yes** |
| No admin/user/password/hash changes | **Yes** |
| No env changes | **Yes** |
| No source→runtime sync | **Yes** |
| No service restart | **Yes** |
| No push/fetch/pull/reset/clean/stash | **Yes** |

---

## 7. Commit

| Item | Value |
|------|-------|
| Exact-path git add | **Yes** (7 allowlisted docs only) |
| Commit message | `docs(iseo-report-hub): add db03 reporting periods charter` |
| Commit hash | `51f3c1f6cd59665c4d59b5227b73c3764859a887` |
| Push | **No** |

---

## 8. SAFE UNKNOWN

- Whether apply wave will create a local demo client/project fixture for FK/unique smoke, or remain structure-only while `projects=0`.
- Exact ON DELETE choice for `project_id` (`RESTRICT` preferred in schema plan; final SQL may confirm).
- Whether CHECK constraints for dates/`period_key` shape will ship in SQL or stay app-level.
- Exact post-apply `/health` field wording after table count increment (health code unchanged in charter; behavior depends on existing HealthController queries).

---

## 9. Recommended Next Action

**I-SEO Report Hub — DB-03 Reporting Periods Migration Apply 01**

---

## 10. Files Changed

- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-CHARTER-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-SCHEMA-PLAN-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-MIGRATION-PLAN-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORTING-PERIOD-LIFECYCLE-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DB-03-IMPLEMENTATION-PLAN-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-db03-reporting-periods-migration-charter-01.md`
- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`

---

## 11. Git Actions

| Action | Done |
|--------|------|
| Exact-path git add | **Yes** |
| Commit | **Yes** |
| Push | **No** |
| Fetch | **No** |
| Pull | **No** |
| Checkout | **No** |
| Reset | **No** |
| Restore | **No** |
| Clean | **No** |
| Stash | **No** |
