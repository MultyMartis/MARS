# REPORT — I-SEO REPORT HUB DB-06 REPORT BLOCKS CHARTER 01

**project_id:** `iseo-report-hub`  
**Wave:** Report Blocks DB-06 Charter 01  
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
| HEAD before | `eb00b3f409649069bd47c187885af126a7f96863` |
| Staged/index before | empty |
| i-SEO WIP before | clean (0 paths) |
| Foreign WIP | preserved (not staged / not modified by this wave) |
| Write scope | allowlisted Active Brain docs under `projects/iseo-report-hub/` only |

---

## 2. Baseline Reviewed

| Item | Value |
|------|-------|
| Monthly Report Content CRUD primary | `65f6412443c7236f17cbf54db3b259a59eccb288` — `feat(iseo-report-hub): add monthly report content crud` |
| Hash-record | `17553a555948120fa3b84184a6610668a0ced2e5` |
| Clarify | `eb00b3f409649069bd47c187885af126a7f96863` |
| DB-05 migration | `2026_07_26_000004_create_monthly_report_contents_table.sql` · checksum `91f367cdf73d1a4b1fcfa3175f190c0470cda86e5cd5706749e2d566c82430b8` · batch **4** |
| DB | `iseo_report_hub_dev` @ `127.0.0.1` |
| Migrations / tables | **4** / **12** |
| users / roles | **1** / **6** |
| clients / projects / sites | **1** / **1** / **1** |
| reporting_periods | **2** |
| weekly_checkpoints | **4** |
| monthly_report_contents | **1** (id **1**, `in_progress`, sources `[1, 2, 3, 7]`, `LOCAL_FIXTURE_ONLY`) |
| `report_blocks` | **absent** |
| Current limitation | no report block DB model / rows / editor / ordering |

---

## 3. Charter Output

Created:

- `product/I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-CHARTER-v0.1.md`
- `product/I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-SCHEMA-PLAN-v0.1.md`
- `product/I-SEO-REPORT-HUB-REPORT-BLOCKS-LIFECYCLE-v0.1.md`
- `product/I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-IMPLEMENTATION-PLAN-v0.1.md`
- `product/I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-VALIDATION-PLAN-v0.1.md`
- `reports/REPORT-iseo-report-hub-db06-report-blocks-charter-01.md`

Updated:

- `OPERATIONAL-INDEX.md` — DB-06 charter status; baseline dependency; no DB/code/runtime in charter; next apply candidate; canonical doc entries

---

## 4. DB-06 Design Summary

| Topic | Decision |
|-------|----------|
| Table | `report_blocks` |
| Relation to `monthly_report_contents` | N:1 via `monthly_report_content_id` (ON DELETE RESTRICT) |
| Relation to `weekly_checkpoints` | soft JSON hint `source_weekly_checkpoint_ids` (no join table) |
| Relation to metrics/import | soft JSON `source_metric_refs` / `data_json` placeholders only |
| Block types | `executive_summary`, `work_completed`, `results_summary`, `key_findings`, `risks_and_blockers`, `next_month_plan`, `client_notes`, `internal_notes`, `custom_text`, `metric_snapshot`, `weekly_summary` |
| Columns | id, parent, block_key, block_type, sort_order, status, title, body, summary, data_json, source weekly/metric JSON, owner/reviewer/audit users, reviewed_at, approved_at, timestamps |
| Statuses | `draft`, `in_progress`, `ready_for_review`, `reviewed`, `approved`, `archived` |
| Unique | `UNIQUE (monthly_report_content_id, block_key)` |
| Ordering | non-unique index `(monthly_report_content_id, sort_order)`; no unique sort_order in MVP |
| FK users | `ON DELETE SET NULL` |
| JSON policy | MySQL JSON type; no extra JSON CHECK unless portable |
| DB-05 TEXT | remain additive fallback; blocks do not replace them in this wave |
| Seed | **no** seed in migration |

---

## 5. Lifecycle Summary

| Topic | Decision |
|-------|----------|
| Happy path | draft → in_progress → ready_for_review → reviewed → approved |
| Archive | any non-approved → archived |
| Reopen approved | `admin_owner` / `seo_lead_reviewer` only |
| Timestamps | `reviewed_at` / `approved_at` (app-set) |
| Approved lock | read-only except privileged reopen/archive |
| Parent finalize lock | parent monthly `finalized` locks block editing (app policy) |
| Period/weekly auto-update | **no** at DB level |
| Delete | **no** hard DELETE; archive instead |
| Reorder | update `sort_order`; temporary duplicates allowed; audit `report_block.reordered` |

---

## 6. Validation Plan

Future apply wave gates:

- migrations **4 → 5**; tables **12 → 13**
- fixture blocks under monthly content for period `2026-07` (`LOCAL_FIXTURE_ONLY`; keys executive_summary / work_completed / results_summary / key_findings / next_month_plan; sort 10–50)
- duplicate `(monthly_report_content_id, block_key)` rejected
- invalid parent FK rejected
- invalid status / block_type rejected (if CHECK used)
- JSON validity via MySQL JSON type
- parent monthly / weekly / period regression (rows unchanged except new child blocks)

---

## 7. Restrictions Confirmed

| Restriction | Confirmed |
|-------------|-----------|
| No app-source edits | yes |
| No runtime edits | yes |
| No DB mutation | yes (read-only status check only) |
| No SQL/migration creation | yes |
| No report block row changes | yes (table absent) |
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
| Commit message | `docs(iseo-report-hub): add db06 report blocks charter` |
| Commit hash | `8b62264cbc8dfc7c42461f4cd600ee374d5c6efb` |
| Hash-record follow-up | `cfb11c9ffc68c7880371dac5ac74a7a63bb8b9b0` — `docs(iseo-report-hub): record db06 report blocks charter commit hash` |
| Push | **no** |

---

## 9. SAFE UNKNOWN

- Whether apply-wave day will keep date prefix `2026_07_26` or adjust to apply-day date — sequence `_000005` remains authoritative either way.
- Exact portable syntax nuances for optional `block_type` CHECK on MySQL 8.4.3 will be confirmed at apply time; schema plan recommends CHECK if stable.
- Exact future block CRUD route surface is deferred to a separate charter after migration apply.

---

## 10. Recommended Next Action

**I-SEO Report Hub — Report Blocks DB-06 Migration Apply 01**

---

## 11. Files Changed

- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-CHARTER-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-SCHEMA-PLAN-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-BLOCKS-LIFECYCLE-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-IMPLEMENTATION-PLAN-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-VALIDATION-PLAN-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-db06-report-blocks-charter-01.md`
- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`

---

## 12. Git Actions

| Action | Performed |
|--------|-----------|
| exact-path git add | yes |
| commit | yes (primary + optional hash-record) |
| push | **no** |
| fetch | no |
| pull | no |
| checkout | no |
| reset | no |
| restore | no |
| clean | no |
| stash | no |
| broad git add | **no** |
