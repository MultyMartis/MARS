# REPORT — I-SEO REPORT HUB DB-04 WEEKLY CHECKPOINTS CHARTER 01

**project_id:** `iseo-report-hub`  
**Wave:** Weekly Checkpoints DB-04 Charter 01  
**Date:** 2026-07-26  
**Type:** documentation / policy only  

---

## 1. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive | `X:` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD before | `f1d8a17e52fd7eb401b34cb3d044a061ebb6f5e7` |
| HEAD after primary commit | `PENDING_PRIMARY_COMMIT_HASH` |
| Staged / index (pre-write) | **Empty** |
| i-SEO WIP clean before | **Yes** (no modified/untracked under `projects/iseo-report-hub/`) |
| Foreign WIP | **Preserved** (not staged, not restored, not cleaned) |
| Write scope | Active Brain i-SEO Report Hub allowlisted docs only (7 paths) |

---

## 2. Baseline Reviewed

| Item | Value |
|------|-------|
| Reporting Period CRUD primary | `392258fc572ac17b479618ba888b6b2ffe0feb68` — `feat(iseo-report-hub): add reporting period crud` |
| Reporting Period CRUD hash-record | `f1d8a17e52fd7eb401b34cb3d044a061ebb6f5e7` — `docs(iseo-report-hub): record reporting period crud commit hash` |
| Auth primary / hash-record | `d4b3b2e2…` / `0cd2cfb7…` |
| DB-03 primary / hash-record | `c19c29b8…` / `2f88d0ce…` |
| Local fixture primary / hash-record | `348b4089…` / `7c543116…` |
| DB | `iseo_report_hub_dev` @ `127.0.0.1` |
| Migration count | **2** |
| Tables count | **10** |
| Users / roles | **1** / **6** |
| Clients / projects / sites | **1** / **1** / **1** |
| Reporting periods | **2** — `2026-07` draft (id 1); `2026-08` archived (id 3) |
| `weekly_checkpoints` | **Absent** (expected) |
| Current limitation | No weekly checkpoint DB model / CRUD / monthly content editor |

Docs / code reviewed (read-only): OPERATIONAL-INDEX, README, product charter, MVP scope, report model, initial schema plan, auth implementation result, DB-03 schema/lifecycle/apply docs, reporting period lifecycle, local fixture apply result, reporting period CRUD implementation result + closeout, migrations `000001`/`000002`, `db-migrate.php`, ReportingPeriod Service/Repository/Controller (read-only).

---

## 3. Charter Output

Created:

- `product/I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-CHARTER-v0.1.md`
- `product/I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-SCHEMA-PLAN-v0.1.md`
- `product/I-SEO-REPORT-HUB-WEEKLY-CHECKPOINT-LIFECYCLE-v0.1.md`
- `product/I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-IMPLEMENTATION-PLAN-v0.1.md`
- `product/I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-VALIDATION-PLAN-v0.1.md`
- `reports/REPORT-iseo-report-hub-db04-weekly-checkpoints-charter-01.md`

Updated:

- `OPERATIONAL-INDEX.md` — DB-04 charter status; baseline dependency on Reporting Period CRUD; no DB/code/runtime changes; next apply candidate

---

## 4. DB-04 Design Summary

| Topic | Decision |
|-------|----------|
| Table | `weekly_checkpoints` |
| Relation | Child of `reporting_periods` via `reporting_period_id` ON DELETE RESTRICT |
| Columns | id, reporting_period_id, week_index, checkpoint_key, dates, status, title, free-text fields, owner/reviewer/audit FKs, reviewed_at/completed_at, timestamps |
| Statuses | `draft`, `in_progress`, `ready_for_review`, `reviewed`, `completed`, `skipped`, `archived` |
| Unique | `(reporting_period_id, week_index)` and `(reporting_period_id, checkpoint_key)` |
| CHECK | week_index 1–6; start ≤ end; status allowlist |
| User FKs | ON DELETE SET NULL |
| Date-in-parent | App/service validation (not parent-join DB CHECK) |
| No-seed policy | Migration creates table only; no seed rows |
| Deferred | Monthly final content (later DB-05 / Report Content); blocks/evidence/Topvisor |

---

## 5. Lifecycle Summary

| Topic | Decision |
|-------|----------|
| Happy path | draft → in_progress → ready_for_review → reviewed → completed |
| Skip/archive | any non-completed → skipped or archived |
| Timestamps | `reviewed_at` / `completed_at` set by future app on status enter |
| Reopen reviewed/completed | admin_owner only |
| Delete | **No** hard DELETE in MVP — archive/skipped instead |
| Period status | Remains rollup; not auto-updated by checkpoint transitions in DB-04 |

---

## 6. Validation Plan

| Gate (future apply) | Expect |
|---------------------|--------|
| Migration / table counts | **2→3** / **10→11** |
| Demo smoke | W1 completed, W2 reviewed, W3 draft for period `2026-07` |
| Duplicates | week_index / checkpoint_key rejected |
| FK | invalid period rejected; period delete RESTRICT with children |
| CHECK | week range / dates / status |
| Regression | health + reporting period CRUD intact; no secrets |
| This charter wave | docs only; no SQL/DB mutation |

---

## 7. Restrictions Confirmed

| Restriction | Status |
|-------------|--------|
| No app-source edits | Confirmed |
| No runtime edits | Confirmed |
| No DB mutation | Confirmed (read-only status only) |
| No SQL / migration creation | Confirmed |
| No fixture changes | Confirmed |
| No reporting_period row changes | Confirmed |
| No admin/password/hash changes | Confirmed |
| No `.env` / `.env.local` changes | Confirmed |
| No source→runtime sync | Confirmed |
| No service restart | Confirmed |
| No demo/registry changes | Confirmed |
| No push/fetch/pull/reset/clean/stash | Confirmed |

---

## 8. Commit

| Item | Value |
|------|-------|
| Exact-path git add | Yes — allowlisted docs only |
| Commit message | `docs(iseo-report-hub): add db04 weekly checkpoints charter` |
| Primary commit hash | `PENDING_PRIMARY_COMMIT_HASH` |
| Hash-record follow-up | `PENDING_HASH_RECORD_COMMIT_HASH` (if needed) |
| Push | **No** |

---

## 9. SAFE UNKNOWN

| Item | Note |
|------|------|
| Exact runtime file drift vs `app-source/` for non-CRUD paths | Not re-audited this wave; Model A policy unchanged |
| Whether apply wave will keep or delete demo W1–W3 rows after smoke | Deferred to apply charter |
| Final date prefix if apply executes on a different calendar day | Sequence `_000003` remains authoritative; date prefix may follow apply-day convention |

---

## 10. Recommended Next Action

**I-SEO Report Hub — Weekly Checkpoints DB-04 Migration Apply 01**

---

## 11. Files Changed

- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-CHARTER-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-SCHEMA-PLAN-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-WEEKLY-CHECKPOINT-LIFECYCLE-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-IMPLEMENTATION-PLAN-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-VALIDATION-PLAN-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-db04-weekly-checkpoints-charter-01.md`
- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`

---

## 12. Git Actions

| Action | Performed |
|--------|-----------|
| Exact-path git add | **Yes** |
| Commit | **Yes** (scoped docs) |
| Push | **No** |
| Fetch | **No** |
| Pull | **No** |
| Checkout | **No** |
| Reset | **No** |
| Restore | **No** |
| Clean | **No** |
| Stash | **No** |
| Broad git add | **No** |
