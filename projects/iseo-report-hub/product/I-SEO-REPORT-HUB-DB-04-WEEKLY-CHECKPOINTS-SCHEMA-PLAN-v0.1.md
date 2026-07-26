# I-SEO Report Hub — DB-04 Weekly Checkpoints Schema Plan v0.1

**Status:** SCHEMA PLAN ONLY — no SQL file; no DB mutation  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-26  
**Authority:** Operator I-SEO Report Hub Weekly Checkpoints DB-04 Charter 01  
**Related:** [I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-CHARTER-v0.1.md](I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-WEEKLY-CHECKPOINT-LIFECYCLE-v0.1.md](I-SEO-REPORT-HUB-WEEKLY-CHECKPOINT-LIFECYCLE-v0.1.md), [I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-SCHEMA-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-SCHEMA-PLAN-v0.1.md)

---

## 1. Table name

`weekly_checkpoints`

---

## 2. Purpose

Store one **weekly checkpoint** row per week (or weekly slice) inside a parent `reporting_periods` row.

Provides:

- parent link (`reporting_period_id`);
- ordinal identity (`week_index`);
- human/stable key (`checkpoint_key`, e.g. `2026-07-W1`);
- inclusive date bounds (`checkpoint_start`, `checkpoint_end`);
- checkpoint lifecycle `status`;
- lightweight free-text progress fields for MVP;
- owner / reviewer / audit actor hooks;
- `reviewed_at` / `completed_at` timestamps.

Does **not** store monthly final report body, report blocks, evidence blobs, or Topvisor metrics.

---

## 3. Columns

| Column | Type (planned) | Null | Default / notes |
|--------|----------------|------|-----------------|
| `id` | `BIGINT UNSIGNED` PK AI | NO | Surrogate key |
| `reporting_period_id` | `BIGINT UNSIGNED` | NO | FK → `reporting_periods.id` |
| `week_index` | `TINYINT UNSIGNED` | NO | 1–6 |
| `checkpoint_key` | `VARCHAR(32)` | NO | e.g. `2026-07-W1` |
| `checkpoint_start` | `DATE` | NO | Inclusive start |
| `checkpoint_end` | `DATE` | NO | Inclusive end |
| `status` | `VARCHAR(32)` | NO | Default `draft`; see §7 |
| `title` | `VARCHAR(255)` | NO | Display title |
| `summary` | `TEXT` | YES | Short weekly summary |
| `work_done` | `TEXT` | YES | Work completed |
| `findings` | `TEXT` | YES | Findings / observations |
| `next_steps` | `TEXT` | YES | Planned next steps |
| `risks` | `TEXT` | YES | Risks / blockers |
| `owner_user_id` | `BIGINT UNSIGNED` | YES | FK → `users.id` |
| `reviewer_user_id` | `BIGINT UNSIGNED` | YES | FK → `users.id` |
| `created_by` | `BIGINT UNSIGNED` | YES | FK → `users.id` |
| `updated_by` | `BIGINT UNSIGNED` | YES | FK → `users.id` |
| `reviewed_at` | `DATETIME` | YES | Set when status → `reviewed` (app rule) |
| `completed_at` | `DATETIME` | YES | Set when status → `completed` (app rule) |
| `created_at` | `DATETIME` | NO | `CURRENT_TIMESTAMP` |
| `updated_at` | `DATETIME` | NO | `CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP` |

---

## 4. Field meanings

| Field | Meaning |
|-------|---------|
| `reporting_period_id` | Parent monthly/reporting shell |
| `week_index` | Ordinal week within the period (1–6) |
| `checkpoint_key` | Stable label unique within period (`YYYY-MM-Wn`) |
| `checkpoint_start` / `checkpoint_end` | Inclusive calendar bounds for the checkpoint window |
| `status` | Checkpoint lifecycle state |
| `title` | Human label (required for list/detail UX later) |
| `summary` / `work_done` / `findings` / `next_steps` / `risks` | MVP free-text content; not structured blocks |
| `owner_user_id` | Specialist responsible for the week |
| `reviewer_user_id` | Reviewer for ready/review flow |
| `created_by` / `updated_by` | Audit actors |
| `reviewed_at` | When checkpoint entered `reviewed` |
| `completed_at` | When checkpoint entered `completed` |

---

## 5. Indexes

| Index | Columns | Purpose |
|-------|---------|---------|
| PK | `id` | Identity |
| Unique | (`reporting_period_id`, `week_index`) | One ordinal week per period |
| Unique | (`reporting_period_id`, `checkpoint_key`) | One key per period |
| Index | `reporting_period_id` | List checkpoints by period |
| Index | `status` | Workflow filters |
| Index | `owner_user_id` | Assignment filters |
| Index | `reviewer_user_id` | Review queue filters |
| Index | `checkpoint_start` | Calendar queries |
| Index | `created_at` | Audit / recent activity |

---

## 6. Unique constraints

1. `UNIQUE (reporting_period_id, week_index)`
2. `UNIQUE (reporting_period_id, checkpoint_key)`

Notes:

- Same `checkpoint_key` may exist under **different** periods (e.g. different projects’ `2026-07-W1`).
- `week_index` uniqueness is per period, not global.

---

## 7. Status enum (CHECK)

Preferred storage: `VARCHAR(32)` + CHECK (matches DB-03 style), not a separate lookup table.

Allowed statuses:

| Status | Meaning (short) |
|--------|-----------------|
| `draft` | Created; not actively worked |
| `in_progress` | Specialist working the week |
| `ready_for_review` | Submitted for review |
| `reviewed` | Reviewer accepted |
| `completed` | Week closed |
| `skipped` | Intentionally unused for this period |
| `archived` | Historical / frozen without delete |

Default for new rows: `draft`.

CHECK (planned):

```text
status IN (
  'draft',
  'in_progress',
  'ready_for_review',
  'reviewed',
  'completed',
  'skipped',
  'archived'
)
```

---

## 8. CHECK constraints

| Constraint | Rule |
|------------|------|
| Week index range | `week_index >= 1 AND week_index <= 6` |
| Date order | `checkpoint_start <= checkpoint_end` |
| Status allowlist | status IN (…list above…) |

### Date policy (parent range)

- **Product rule:** checkpoint date range **must** fall inside parent `reporting_periods.period_start` / `period_end` (inclusive).
- **Enforcement:** app/service validation first.
- **DB:** parent-referencing CHECK is not required for MVP (MySQL CHECK cannot easily join parent row). Future trigger/app dual-check may be chartered later.

### Nullable fields

Nullable: `summary`, `work_done`, `findings`, `next_steps`, `risks`, all user FKs, `reviewed_at`, `completed_at`.

Required: identity, parent, week_index, checkpoint_key, dates, status, title, created_at, updated_at.

---

## 9. Foreign keys

| Column | References | On delete (planned) |
|--------|------------|---------------------|
| `reporting_period_id` | `reporting_periods.id` | **RESTRICT** |
| `owner_user_id` | `users.id` | `SET NULL` |
| `reviewer_user_id` | `users.id` | `SET NULL` |
| `created_by` | `users.id` | `SET NULL` |
| `updated_by` | `users.id` | `SET NULL` |

Rationale:

- Period delete with children must not silently wipe weekly history.
- User deletion should not cascade-delete checkpoints.

---

## 10. Relation to `reporting_periods`

```text
reporting_periods (1)
  └── weekly_checkpoints (0..N)
```

- Child rows require an existing period.
- Typical N = 3; allowed N up to 6 via `week_index`.
- Period `status` is rollup; checkpoint `status` is independent child lifecycle.
- Monthly final report content is **not** a row in this table.

---

## 11. No-seed policy

| Policy | Decision |
|--------|----------|
| Seed in migration SQL | **No** |
| Seed in `schema_migrations` apply | **No** |
| Demo rows in apply-wave smoke | **Optional / allowed** if apply charter says so — local fixture period `2026-07` only; mark `LOCAL_FIXTURE_ONLY` in summary |
| Real client weekly data | **Forbidden** |

---

## 12. Rollback considerations

| Scenario | Policy |
|----------|--------|
| Migration not yet applied | Delete/uncommit migration file under apply charter only |
| Applied, table empty | Drop table + remove ledger row only with explicit destructive approval |
| Applied, demo smoke rows present | Prefer delete smoke rows first; then empty-table rollback if chartered |
| Applied, non-demo rows present | **No** destructive rollback without dedicated charter + backup |
| Prior migrations `000001` / `000002` | **Never** rewrite after apply |

Preferred forward fix: additive migrations; avoid silent DROP in normal ops.

---

## 13. Explicit non-goals for this table

- Monthly final report body
- Structured report blocks / KPI series
- Evidence / file uploads
- Client portal publish snapshots
- Auto calendar generation logic inside DDL
