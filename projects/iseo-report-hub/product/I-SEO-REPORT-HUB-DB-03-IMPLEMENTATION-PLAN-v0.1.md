# I-SEO Report Hub — DB-03 Implementation Plan v0.1

**Status:** IMPLEMENTATION PLAN for next wave — not an apply authorization by itself  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-25  
**Authority:** Operator I-SEO Report Hub DB-03 Reporting Periods Migration Charter 01  
**Related:** [I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-CHARTER-v0.1.md](I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-MIGRATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-MIGRATION-PLAN-v0.1.md), [I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-SCHEMA-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-SCHEMA-PLAN-v0.1.md)

---

## 1. Next wave name

**`I-SEO Report Hub — DB-03 Reporting Periods Migration Apply 01`**

Operator must issue an explicit apply charter before execution. This plan is the blueprint for that wave.

---

## 2. Files allowed next wave

| Path class | Allowed |
|------------|---------|
| `app-source/database/migrations/2026_07_25_000002_create_reporting_periods_table.sql` | **Yes** (create) |
| Runtime copy of that migration under Localhost project `database/migrations/` | **Yes** (sync) |
| Optional result doc under `product/` | **Yes** if charter lists it |
| Optional closeout under `reports/` | **Yes** if charter lists it |
| `OPERATIONAL-INDEX.md` | **Yes** if charter lists it |
| App PHP (controllers/services/views) | **No** unless separately approved |
| `tools/db-migrate.php` | **No** unless bugfix chartered |
| Prior migration `000001` | **No** edits |
| `.env` / `.env.local` | **No** |
| Demo workspace / registry | **No** |

---

## 3. DB actions allowed next wave

| Action | Allowed |
|--------|---------|
| Create `reporting_periods` table via migration | **Yes** |
| Insert `schema_migrations` ledger row via runner | **Yes** |
| Structural validation queries (SHOW/SELECT metadata) | **Yes** |
| Idempotent re-apply | **Yes** |
| Optional controlled unique-constraint smoke | **Yes** if safe project/fixture exists |
| Optional local-only fixture client/project for FK smoke | **Only if** apply charter explicitly allows; placeholders only |

---

## 4. DB actions not allowed

| Action | Forbidden |
|--------|-----------|
| Production DB | **Forbidden** |
| Real client data inserts | **Forbidden** |
| Destructive rollback (`DROP` non-empty, truncate, wipe) | **Forbidden** without empty-table + explicit approval |
| Password / admin / role seed changes | **Forbidden** |
| Editing applied migration checksum content after apply | **Forbidden** |
| Broad DB cleanup | **Forbidden** |

---

## 5. Smoke list

1. Preflight: volume, branch, empty unrelated stage, DB name `iseo_report_hub_dev`.
2. `db-migrate.php status` shows pending `000002`.
3. `db-migrate.php apply` succeeds.
4. Ledger row present; checksum OK.
5. Table `reporting_periods` exists.
6. Required columns present.
7. Unique + FK metadata present.
8. Idempotent re-apply no-op.
9. If projects empty: **structure-only PASS** (no period insert required).
10. If fixture/project exists and chartered: insert one period; duplicate `(project_id, period_key)` refused; delete smoke row if policy requires leaving DB clean.
11. `/health` still 200; migration/table counts may increment (no health code edit required unless charter expands).
12. No secrets printed.

---

## 6. Commit policy

- Exact-path stage only (never `git add .` / `-A` / `commit -a`).
- Commit message example: `feat(iseo-report-hub): add reporting periods migration` (final message set by apply charter).
- Docs/result paths only as allowlisted.
- **Push:** no by default.
- Preserve foreign WIP.
- Fixture passwords / real client names: never commit.

---

## 7. STOP conditions

STOP apply wave if:

- charter scope violated (UI/API/n8n creep);
- wrong DB / volume / branch;
- foreign paths staged;
- checksum mismatch;
- `000001` unhealthy;
- unexpected existing `reporting_periods`;
- operator denies fixture/rollback;
- cannot keep production / secrets out of scope.

---

## 8. Fixture decision (deferred to apply charter)

| Situation | Guidance |
|-----------|----------|
| `projects` count = 0 (current baseline) | Structure-only validation is sufficient |
| Need FK/unique smoke | Apply charter may allow a **local-only** demo client/project/period under safe placeholders |
| Existing project appears later | Prefer reusing local demo project over inventing production-like names |

This charter wave creates **no** fixture.
