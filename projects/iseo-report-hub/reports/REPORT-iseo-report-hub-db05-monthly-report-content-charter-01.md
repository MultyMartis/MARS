# REPORT — I-SEO REPORT HUB DB-05 MONTHLY REPORT CONTENT CHARTER 01

**project_id:** `iseo-report-hub`  
**Wave:** Monthly Report Content DB-05 Charter 01  
**Date:** 2026-07-26  
**Result:** COMPLETE — documentation / policy only  
**Push:** no

---

## 1. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive | `X:` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD before | `865cd4b50a31e1605bf45ffa3256dc48499eedca` |
| Staged/index before | empty |
| i-SEO WIP before | clean (0 paths) |
| Foreign WIP | preserved (not staged / not modified by this wave) |
| Write scope | allowlisted Active Brain docs under `projects/iseo-report-hub/` only |

---

## 2. Baseline Reviewed

| Item | Value |
|------|-------|
| Weekly Checkpoints CRUD primary | `911db07d8ca51bb1778c53ca570ef3b8950234a0` — `feat(iseo-report-hub): add weekly checkpoints crud` |
| Hash-record | `64c42cbe6616be19b6d8ea3340466e7bab1f7bf9` |
| Clarify | `6f968ed2` / `865cd4b5` |
| DB-04 migration | `2026_07_26_000003_create_weekly_checkpoints_table.sql` · checksum `8ab9c0e84a262ab9c8662cd502ab18943810dc6a034d2cd25a89935e2ddaacd3` · batch **3** |
| DB | `iseo_report_hub_dev` @ `127.0.0.1` |
| Migrations / tables | **3** / **11** |
| users / roles | **1** / **6** |
| clients / projects / sites | **1** / **1** / **1** |
| reporting_periods | **2** |
| weekly_checkpoints | **4** |
| `monthly_report_contents` | **absent** |
| Current limitation | no monthly report content DB model / row / editor |

---

## 3. Charter Output

Created:

- `product/I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-CHARTER-v0.1.md`
- `product/I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-SCHEMA-PLAN-v0.1.md`
- `product/I-SEO-REPORT-HUB-MONTHLY-REPORT-LIFECYCLE-v0.1.md`
- `product/I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-IMPLEMENTATION-PLAN-v0.1.md`
- `product/I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-VALIDATION-PLAN-v0.1.md`
- `reports/REPORT-iseo-report-hub-db05-monthly-report-content-charter-01.md`

Updated:

- `OPERATIONAL-INDEX.md` — DB-05 charter status; next apply candidate; canonical doc entries

---

## 4. DB-05 Design Summary

| Topic | Decision |
|-------|----------|
| Table | `monthly_report_contents` |
| Relation to `reporting_periods` | 1:0..1 via `reporting_period_id` |
| Relation to `weekly_checkpoints` | soft JSON hint `source_weekly_checkpoint_ids` (no join table) |
| Content model | structured TEXT fields (not blocks) |
| Statuses | `draft`, `in_progress`, `ready_for_review`, `reviewed`, `finalized`, `archived` |
| Unique | `UNIQUE (reporting_period_id)` |
| FK period | `ON DELETE RESTRICT` |
| FK users | `ON DELETE SET NULL` |
| JSON policy | JSON type; optional CHECK only if portable; app validates same-period membership later |
| Seed | **no** seed in migration |

---

## 5. Lifecycle Summary

| Topic | Decision |
|-------|----------|
| Happy path | draft → in_progress → ready_for_review → reviewed → finalized |
| Archive | any non-finalized → archived |
| Reopen finalized | `admin_owner` only |
| Timestamps | `reviewed_at` / `finalized_at` (app-set) |
| Finalized lock | read-only except admin reopen/archive |
| Period status auto-update | **no** at DB level |
| Delete | **no** hard DELETE; archive instead |

---

## 6. Validation Plan

Future apply wave gates:

- migrations **3 → 4**; tables **11 → 12**
- one demo monthly row for period `2026-07` (`LOCAL_FIXTURE_ONLY`)
- duplicate `reporting_period_id` rejected
- invalid FK / invalid status rejected
- JSON validity verified if applicable
- health + Reporting Period CRUD + Weekly Checkpoints CRUD regression

Charter wave did **not** insert the demo row.

---

## 7. Restrictions Confirmed

| Restriction | Confirmed |
|-------------|-----------|
| No app-source edits | yes |
| No runtime edits | yes |
| No DB mutation | yes (read-only status check only) |
| No SQL/migration creation | yes |
| No monthly report row changes | yes |
| No weekly checkpoint changes | yes |
| No reporting_period changes | yes |
| No admin/password/hash changes | yes |
| No env changes | yes |
| No source sync | yes |
| No service restart | yes |
| No push/fetch/pull/reset/clean/stash | yes |

---

## 8. Commit

| Item | Value |
|------|-------|
| Exact-path git add | yes (allowlisted docs only) |
| Commit message | `docs(iseo-report-hub): add db05 monthly report content charter` |
| Primary commit hash | `PENDING_PRIMARY_COMMIT_HASH` |
| Hash-record follow-up | `PENDING_HASH_RECORD_COMMIT_HASH` (if needed) |
| Push | **no** |

---

## 9. SAFE UNKNOWN

- Whether apply-wave MySQL will include an extra JSON CHECK beyond the JSON column type (deferred to apply decision on portability).
- Exact weekly checkpoint id list at apply time if fixture ids change (smoke must resolve by `checkpoint_key`).

---

## 10. Recommended Next Action

**I-SEO Report Hub — Monthly Report Content DB-05 Migration Apply 01**

---

## 11. Files Changed

- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-CHARTER-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-SCHEMA-PLAN-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-MONTHLY-REPORT-LIFECYCLE-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-IMPLEMENTATION-PLAN-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-VALIDATION-PLAN-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-db05-monthly-report-content-charter-01.md`
- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`

---

## 12. Git Actions

| Action | Performed |
|--------|-----------|
| exact-path git add | **yes** |
| commit | **yes** |
| push | **no** |
| fetch | **no** |
| pull | **no** |
| checkout | **no** |
| reset | **no** |
| restore | **no** |
| clean | **no** |
| stash | **no** |
| broad git add | **no** |
