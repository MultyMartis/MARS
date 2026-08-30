# I-SEO Report Hub — DB-03 Reporting Periods Schema Plan v0.1

**Status:** SCHEMA PLAN ONLY — no SQL file; no DB mutation  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-25  
**Authority:** Operator I-SEO Report Hub DB-03 Reporting Periods Migration Charter 01  
**Related:** [I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-CHARTER-v0.1.md](I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-REPORTING-PERIOD-LIFECYCLE-v0.1.md](I-SEO-REPORT-HUB-REPORTING-PERIOD-LIFECYCLE-v0.1.md), [I-SEO-REPORT-HUB-MVP-SCHEMA-DRAFT-v0.1.md](I-SEO-REPORT-HUB-MVP-SCHEMA-DRAFT-v0.1.md)

---

## 1. Table name

`reporting_periods`

---

## 2. Purpose

Store one **monthly reporting period** per project. Provides:

- project/month history key (`period_key`);
- calendar bounds (`period_start`, `period_end`);
- period-level lifecycle `status`;
- ownership / review assignment hooks;
- audit timestamps and actor FKs;
- `finalized_at` for closed periods.

Does **not** store weekly checkpoint or monthly final **content**. Those remain DB-04+.

---

## 3. Fields

| Column | Type (planned) | Null | Default / notes |
|--------|----------------|------|-----------------|
| `id` | `BIGINT UNSIGNED` PK AI | NO | Surrogate key |
| `project_id` | `BIGINT UNSIGNED` | NO | FK → `projects.id` |
| `period_key` | `CHAR(7)` or `VARCHAR(7)` | NO | `YYYY-MM` e.g. `2026-07` |
| `period_start` | `DATE` | NO | First day of period |
| `period_end` | `DATE` | NO | Last day of period |
| `status` | `ENUM(...)` or `VARCHAR(32)` | NO | See §5; prefer ENUM for MVP |
| `title` | `VARCHAR(190)` | YES | Optional display title |
| `summary` | `TEXT` | YES | Short period summary / notes |
| `owner_user_id` | `BIGINT UNSIGNED` | YES | FK → `users.id` |
| `reviewer_user_id` | `BIGINT UNSIGNED` | YES | FK → `users.id` |
| `created_by` | `BIGINT UNSIGNED` | YES | FK → `users.id` |
| `updated_by` | `BIGINT UNSIGNED` | YES | FK → `users.id` |
| `finalized_at` | `TIMESTAMP` | YES | Set when status → `finalized` |
| `created_at` | `TIMESTAMP` | NO | `CURRENT_TIMESTAMP` |
| `updated_at` | `TIMESTAMP` | YES | `ON UPDATE CURRENT_TIMESTAMP` |

**Not included in DB-03:** `week_1_status`, `week_2_status`, `week_3_status`, `monthly_status` — avoid denormalized checkpoint columns; use future child tables instead.

---

## 4. Field meanings

| Field | Meaning |
|-------|---------|
| `period_key` | Canonical month identity for UX/history (`2026-07`). Must match calendar month of `period_start`. |
| `period_start` / `period_end` | Inclusive calendar bounds for the monthly cycle. Require `period_start <= period_end`. |
| `status` | Period lifecycle state (workflow before report editor). |
| `title` | Human label (e.g. “July 2026 — Project X”); may mirror period_key if empty in UI later. |
| `summary` | Lightweight period-level narrative; **not** a substitute for monthly report body. |
| `owner_user_id` | Specialist responsible for driving the period. |
| `reviewer_user_id` | Lead/reviewer for close/review. |
| `created_by` / `updated_by` | Who created / last changed the period shell. |
| `finalized_at` | Timestamp of finalization; null until finalized. |

---

## 5. Statuses

Final MVP period status set for DB-03:

| Status | Meaning |
|--------|---------|
| `draft` | Period shell created; work not actively running |
| `active` | Period in progress (weekly work happening conceptually) |
| `weekly_review` | Weekly checkpoint review phase at period level |
| `monthly_review` | Month-close / final report under internal review |
| `finalized` | Period closed for operational reporting; ready for later publish pipeline |
| `archived` | Historical; no active edits |

**Note:** Report Lifecycle v0.1 describes finer states (`planned`, `active_week_1`…, `published`). DB-03 intentionally **collapses** to the six statuses above. Mapping is documented in the lifecycle companion for DB-03.

Recommended ENUM:

```text
draft | active | weekly_review | monthly_review | finalized | archived
```

Default for new rows: `draft`.

---

## 6. Foreign keys

| Column | References | On delete (planned) |
|--------|------------|---------------------|
| `project_id` | `projects.id` | `RESTRICT` or `CASCADE` — prefer **RESTRICT** for local safety (do not silently wipe periods) |
| `owner_user_id` | `users.id` | `SET NULL` |
| `reviewer_user_id` | `users.id` | `SET NULL` |
| `created_by` | `users.id` | `SET NULL` |
| `updated_by` | `users.id` | `SET NULL` |

All user FKs are **nullable**.

---

## 7. Indexes

| Index | Columns | Purpose |
|-------|---------|---------|
| PK | `id` | Identity |
| Unique | (`project_id`, `period_key`) | One period per project/month |
| Index | `project_id` | List periods by project |
| Index | `period_key` | Cross-project month queries |
| Index | `status` | Workflow filters |
| Index | `owner_user_id` | Specialist workload |
| Index | `reviewer_user_id` | Reviewer queue |
| Index | `finalized_at` | Closed-period queries |
| Index | `created_at` | Chronological listing |

(`project_id` may be covered by the unique key; still list it as required for clarity — implementation may rely on unique prefix.)

---

## 8. Uniqueness

**Required:** `UNIQUE (project_id, period_key)`.

Effects:

- No overlapping duplicate project/month rows.
- Duplicate insert must be refused by the engine (smoke gate).

---

## 9. Check constraints (if supported / practical)

MySQL 8.4 supports CHECK. Recommended if keepable in migration without fragility:

| Constraint | Rule |
|------------|------|
| `chk_reporting_periods_dates` | `period_start <= period_end` |
| `chk_reporting_periods_key_shape` | `period_key` matches `^[0-9]{4}-[0-9]{2}$` (optional; may enforce in app if CHECK regex awkward) |

**Application-level (mandatory even if CHECK omitted):**

- `period_key` must match the calendar month of `period_start` (e.g. start `2026-07-01` → key `2026-07`).
- Prefer `period_end` = last day of that month for MVP monthly cycles.

If CHECK proves noisy in local apply, document deferral to app validation — do not block DB-03 on exotic CHECK syntax.

---

## 10. Deferred tables (DB-04+)

| Table | Why deferred |
|-------|--------------|
| `weekly_checkpoints` | Checkpoint content + week_number states |
| `monthly_reports` | Month-close report body / approval / publish hooks |
| `report_blocks` / values | Block editor storage |
| `work_items` / KPI / evidence | Content domain |
| `published_snapshots` | Client-facing publish |

Also deferred: denormalized `week_*_status` / `monthly_status` columns on `reporting_periods`.

---

## 11. Sample safe rows (placeholders only)

**Illustrative only — do not insert real client data. Not executed in this charter wave.**

Assume a local fixture project `id = 1` exists (today: projects count is **0**; insert would require a prior safe fixture).

| id | project_id | period_key | period_start | period_end | status | title | owner_user_id |
|----|------------|------------|--------------|------------|--------|-------|---------------|
| 1 | 1 | `2026-07` | `2026-07-01` | `2026-07-31` | `draft` | `Demo Period 2026-07` | 1 |
| 2 | 1 | `2026-08` | `2026-08-01` | `2026-08-31` | `active` | `Demo Period 2026-08` | 1 |

Duplicate of `(1, '2026-07')` must fail unique check.

If `clients`/`projects` remain empty, DB-03 apply validates **structure only** (no period row required).
