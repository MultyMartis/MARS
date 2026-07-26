# REPORT — I-SEO REPORT HUB REPORT BLOCKS CRUD CHARTER 01

**Status:** COMPLETE (docs/policy only)  
**project_id:** `iseo-report-hub`  
**Created:** 2026-07-26  
**Authority:** Operator I-SEO Report Hub Report Blocks CRUD Charter 01  
**Primary commit:** `PENDING_PRIMARY_COMMIT_HASH`

---

## 1. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive | `X:` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD before | `86338d666f08146b6feff06536ae6d7b50eb332c` |
| Staged/index before | **empty** |
| i-SEO WIP before | **clean** (`projects/iseo-report-hub/` no modified/untracked) |
| Foreign WIP | **preserved** (untouched) |
| Write scope | Active Brain docs only under allowlisted `product/` + `reports/` + `OPERATIONAL-INDEX.md` |

HEAD matched expected DB-06 clarify commit `86338d66`. No STOP.

---

## 2. Baseline Reviewed

| Item | Value |
|------|-------|
| DB-06 migration apply commit | `1b71a0213c61844258a87afb68f9b796bd35443f` |
| DB-06 hash-record commit | `7393d7c1d287bb8d180e41be26d37f738e330821` |
| DB-06 clarify commit | `86338d666f08146b6feff06536ae6d7b50eb332c` |
| Migration | `2026_07_26_000005_create_report_blocks_table.sql` |
| Checksum | `951bc88826a6155a624377b43851f1d6f7eadb8fdf7d229cb5bffe952eee3236` |
| Batch | **5** |
| DB | `iseo_report_hub_dev` @ `127.0.0.1` |
| Counts (read-only) | migrations **5**; tables **13**; users **1**; roles **6**; clients/projects/sites **1/1/1**; reporting_periods **2**; weekly_checkpoints **4**; monthly_report_contents **1**; report_blocks **5** |
| Parent monthly | id **1**; period `2026-07`; status `in_progress`; title/markers `LOCAL_FIXTURE_ONLY`; sources `[1,2,3,7]` |
| Fixture blocks | `executive_summary`…`next_month_plan` at sort 10/20/30/40/50; all `draft`; sources `[1,2,3,7]`; `LOCAL_FIXTURE_ONLY` |
| Current limitation | **No** report blocks CRUD/UI/routes/controller/service/repository; **no** block editor; **no** drag/drop |

DB-06 validation already passed (FK/unique/CHECK/JSON + regression). This charter wave did not mutate DB.

---

## 3. Charter Output

Created/updated:

- `product/I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-CHARTER-v0.1.md`
- `product/I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-DESIGN-v0.1.md`
- `product/I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-IMPLEMENTATION-PLAN-v0.1.md`
- `product/I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-VALIDATION-PLAN-v0.1.md`
- `reports/REPORT-iseo-report-hub-report-blocks-crud-charter-01.md` (this file)
- `OPERATIONAL-INDEX.md` — Report Blocks CRUD Charter status + next implementation candidate

---

## 4. CRUD Design Summary

| Area | Design |
|------|--------|
| Routes | Nested GET/POST `/monthly-reports/{id}/blocks` (+ `/create`); flat GET `/report-blocks/{id}` + `/edit` + POST update; **no DELETE**; optional index not required |
| Views | `report-blocks/index|show|form|create|edit`; monthly show blocks section |
| Layers | `ReportBlockController` / `ReportBlockService` / `ReportBlockRepository` |
| Parent monthly | Blocks belong to one monthly row; list/create nested; monthly show integration |
| Reporting period | Resolved via monthly parent; period show keeps monthly section only |
| Weekly sources | `source_weekly_checkpoint_ids` validated + linked; no weekly row mutation |
| Manual sort | Integer `sort_order` on create/edit; list by sort_order; **no** drag/drop |
| Access | admin full; lead review/approve/archive/reorder/reopen; specialist to ready_for_review; account/internal read-only; client_viewer none |
| Validation | uniqueness, transitions, parent locks, source ids, JSON, title/body/summary lengths, internal users |
| Audit | created/updated/status_changed/reviewed/approved/archived/reordered (recommended) |
| No-delete / no-dragdrop | archive via status only; unique key not freed; no sortable UI |

---

## 5. Validation Plan

Next wave smoke covers:

- Route smoke (list/create/detail/edit; unauth redirect; no DELETE)
- Form/CSRF
- DB edit `executive_summary` → `in_progress`; create `risks_and_blockers`
- Duplicate `block_key` guard
- Invalid JSON + invalid/cross-period source weekly ids
- Manual `sort_order`
- Monthly show blocks section
- Auth/role (admin; multi-role may be policy-only)
- Regression: reporting period / weekly / monthly CRUD + login / health / 404

---

## 6. Restrictions Confirmed

| Restriction | Result |
|-------------|--------|
| No app-source edits | **Confirmed** |
| No runtime edits | **Confirmed** |
| No DB mutation | **Confirmed** (read-only check only) |
| No SQL/migration creation/edit | **Confirmed** |
| No report_blocks row changes | **Confirmed** |
| No monthly_report_contents row changes | **Confirmed** |
| No weekly_checkpoint row changes | **Confirmed** |
| No reporting_period row changes | **Confirmed** |
| No admin/password/hash changes | **Confirmed** |
| No env changes | **Confirmed** |
| No source→runtime sync | **Confirmed** |
| No service restart | **Confirmed** |
| No push/fetch/pull/reset/clean/stash | **Confirmed** |
| No broad git add | **Confirmed** (exact-path only) |

---

## 7. Commit

| Item | Value |
|------|-------|
| Exact-path git add | allowlisted docs only |
| Commit message | `docs(iseo-report-hub): add report blocks crud charter` |
| Commit hash | `PENDING_PRIMARY_COMMIT_HASH` |
| Push | **no** |

Hash-record follow-up (if needed): `docs(iseo-report-hub): record report blocks crud charter commit hash` on this REPORT only.

---

## 8. SAFE UNKNOWN

- Multi-role HTTP denial paths for `seo_specialist` / `account_client_manager` / `internal_viewer` / `client_viewer` — **not smoked** until additional local users exist (policy covered).
- Whether next-wave smoke will archive the additional `risks_and_blockers` block or leave it `draft` — deferred to implementation validation goal.
- Exact HealthController expected table-count wording vs live table count **13** — health not updated this wave (no health code edits).

---

## 9. Recommended Next Action

**I-SEO Report Hub — Report Blocks CRUD Implementation 01**

---

## 10. Files Changed

- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-CHARTER-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-DESIGN-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-IMPLEMENTATION-PLAN-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-VALIDATION-PLAN-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-report-blocks-crud-charter-01.md`
- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`

---

## 11. Git Actions

| Action | Done? |
|--------|-------|
| exact-path git add | **yes** (allowlisted docs) |
| commit | **yes** (primary; hash-record if needed) |
| push | **no** |
| fetch | **no** |
| pull | **no** |
| checkout | **no** |
| reset | **no** |
| restore | **no** |
| clean | **no** |
| stash | **no** |
| broad git add | **no** |
