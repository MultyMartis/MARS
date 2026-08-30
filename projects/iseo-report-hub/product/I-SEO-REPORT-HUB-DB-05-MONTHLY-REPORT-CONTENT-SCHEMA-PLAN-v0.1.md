# I-SEO Report Hub — DB-05 Monthly Report Content Schema Plan v0.1

**Status:** SCHEMA PLAN ONLY — no SQL file; no DB mutation  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-26  
**Authority:** Operator I-SEO Report Hub Monthly Report Content DB-05 Charter 01  
**Related:** [I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-CHARTER-v0.1.md](I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-MONTHLY-REPORT-LIFECYCLE-v0.1.md](I-SEO-REPORT-HUB-MONTHLY-REPORT-LIFECYCLE-v0.1.md), [I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-SCHEMA-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-SCHEMA-PLAN-v0.1.md), [I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-SCHEMA-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-SCHEMA-PLAN-v0.1.md)

---

## 1. Table name

`monthly_report_contents`

---

## 2. Purpose

Store at most **one** monthly/final report working document per parent `reporting_periods` row.

Provides:

- parent link (`reporting_period_id`);
- lifecycle `status`;
- structured TEXT content fields for MVP;
- optional JSON snapshot of source weekly checkpoint ids;
- owner / reviewer / audit actor hooks;
- `reviewed_at` / `finalized_at` timestamps.

Does **not** store report blocks, evidence blobs, Topvisor metrics, or published client snapshots.

---

## 3. Columns

| Column | Type (planned) | Null | Default / notes |
|--------|----------------|------|-----------------|
| `id` | `BIGINT UNSIGNED` PK AI | NO | Surrogate key |
| `reporting_period_id` | `BIGINT UNSIGNED` | NO | FK → `reporting_periods.id`; unique |
| `status` | `VARCHAR(32)` | NO | Default `draft`; see §7 |
| `title` | `VARCHAR(255)` | NO | Display title |
| `executive_summary` | `TEXT` | YES | Client-facing executive summary draft |
| `work_completed` | `TEXT` | YES | Work completed in the period |
| `results_summary` | `TEXT` | YES | Results / outcomes summary |
| `key_findings` | `TEXT` | YES | Key findings |
| `risks_and_blockers` | `TEXT` | YES | Risks and blockers |
| `next_month_plan` | `TEXT` | YES | Plan for next month |
| `client_notes` | `TEXT` | YES | Notes intended for client communication (still internal until publish module) |
| `internal_notes` | `TEXT` | YES | Internal-only notes |
| `source_weekly_checkpoint_ids` | `JSON` | YES | Soft list of weekly checkpoint ids used as source hint |
| `owner_user_id` | `BIGINT UNSIGNED` | YES | FK → `users.id` |
| `reviewer_user_id` | `BIGINT UNSIGNED` | YES | FK → `users.id` |
| `created_by` | `BIGINT UNSIGNED` | YES | FK → `users.id` |
| `updated_by` | `BIGINT UNSIGNED` | YES | FK → `users.id` |
| `reviewed_at` | `DATETIME` | YES | Set when status → `reviewed` (app rule) |
| `finalized_at` | `DATETIME` | YES | Set when status → `finalized` (app rule) |
| `created_at` | `DATETIME` | NO | `CURRENT_TIMESTAMP` |
| `updated_at` | `DATETIME` | NO | `CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP` |

---

## 4. Field meanings

| Field | Meaning |
|-------|---------|
| `reporting_period_id` | Parent monthly/reporting shell (1:0..1) |
| `status` | Monthly content lifecycle state |
| `title` | Human label for list/detail UX later |
| `executive_summary` … `internal_notes` | MVP structured narrative fields |
| `source_weekly_checkpoint_ids` | Optional JSON array of `weekly_checkpoints.id` values as a **snapshot hint**, not a hard normalized join |
| `owner_user_id` | Specialist responsible for drafting |
| `reviewer_user_id` | Reviewer for ready/review flow |
| `created_by` / `updated_by` | Audit actors |
| `reviewed_at` | When content entered `reviewed` |
| `finalized_at` | When content entered `finalized` |

---

## 5. Indexes

| Index | Columns | Purpose |
|-------|---------|---------|
| PK | `id` | Identity |
| Unique | (`reporting_period_id`) | At most one monthly content row per period |
| Index | `status` | Workflow filters |
| Index | `owner_user_id` | Assignment filters |
| Index | `reviewer_user_id` | Review queue filters |
| Index | `created_by` | Audit filters |
| Index | `updated_by` | Audit filters |
| Index | `created_at` | Audit / recent activity |
| Index | `finalized_at` | Finalized queue / reporting filters |

Note: unique on `reporting_period_id` already supports parent lookup; a separate non-unique index on that column is optional/redundant.

---

## 6. Unique constraints

1. `UNIQUE (reporting_period_id)`

Notes:

- MVP enforces **one monthly report content row per reporting period**.
- Creating a second row for the same period must fail at DB level.

---

## 7. Status enum (CHECK)

Preferred storage: `VARCHAR(32)` + CHECK (matches DB-03 / DB-04 style), not a separate lookup table.

Allowed statuses:

| Status | Meaning (short) |
|--------|-----------------|
| `draft` | Created; not actively worked |
| `in_progress` | Specialist drafting monthly narrative |
| `ready_for_review` | Submitted for review |
| `reviewed` | Reviewer accepted |
| `finalized` | Monthly content locked as final working document |
| `archived` | Historical / frozen without delete |

Default for new rows: `draft`.

CHECK (planned):

```text
status IN (
  'draft',
  'in_progress',
  'ready_for_review',
  'reviewed',
  'finalized',
  'archived'
)
```

---

## 8. CHECK constraints

| Constraint | Rule |
|------------|------|
| Status allowlist | status IN (…list above…) |
| JSON validity (optional) | If MySQL syntax supports a portable/safe JSON CHECK for `source_weekly_checkpoint_ids`, prefer it; otherwise rely on JSON column type + app validation |

### JSON field policy

| Topic | Policy |
|-------|--------|
| Type | `JSON` nullable |
| Intended shape | Array of unsigned integers (checkpoint ids), e.g. `[1,2,3,7]` |
| Hard FK | **No** — not a join table; ids are a soft hint |
| Empty vs null | Both allowed; prefer `NULL` when no sources recorded |
| Invalid JSON | Rejected by MySQL JSON type when value is non-null invalid JSON |
| Extra CHECK | Use only if apply wave confirms portable syntax on MySQL 8.4.3 without migration fragility |
| Membership validation | App/service should verify ids belong to the same `reporting_period_id` (not DB-enforced in MVP) |

### Nullable fields

Nullable: all content TEXT fields, `source_weekly_checkpoint_ids`, all user FKs, `reviewed_at`, `finalized_at`.

Required: identity, parent, status, title, created_at, updated_at.

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

- Period delete with monthly content must not silently wipe the working document.
- User deletion should not cascade-delete monthly content.
- No FK from JSON weekly ids to `weekly_checkpoints` in MVP.

---

## 10. Relation to `reporting_periods`

```text
reporting_periods (1)
  └── monthly_report_contents (0..1)
```

- Child row requires an existing period.
- Unique parent enforces at most one monthly content document.
- Period `status` remains rollup; monthly content `status` is an independent lifecycle.
- DB must **not** auto-update period status when monthly content status changes.

---

## 11. Relation to `weekly_checkpoints`

```text
reporting_periods (1)
  ├── weekly_checkpoints (0..N)
  └── monthly_report_contents (0..1)
         └── source_weekly_checkpoint_ids (JSON soft hint → weekly_checkpoints.id[])
```

| Aspect | Policy |
|--------|--------|
| Hard join table | Deferred |
| Soft snapshot | JSON id list on monthly row |
| Cascade | None |
| Integrity | App validates same-period membership later |
| Weekly status coupling | None at DB level |

---

## 12. No-seed policy

| Policy | Decision |
|--------|----------|
| Seed in migration SQL | **No** |
| Seed in `schema_migrations` apply | **No** |
| Demo row in apply-wave smoke | **Optional / allowed** if apply charter says so — local fixture period `2026-07` only; mark content fields with `LOCAL_FIXTURE_ONLY` |
| Real client monthly data | **Forbidden** |

---

## 13. Rollback considerations

| Scenario | Policy |
|----------|--------|
| Migration not yet applied | Delete/uncommit migration file under apply charter only |
| Applied, table empty | Drop table + remove ledger row only with explicit destructive approval |
| Applied, demo smoke row present | Prefer delete smoke row first; then empty-table rollback if chartered |
| Applied, non-demo rows present | **No** destructive rollback without dedicated charter + backup |
| Prior migrations `000001`–`000003` | **Never** rewrite after apply |

Preferred forward fix: additive migrations; avoid silent DROP in normal ops.

---

## 14. Explicit non-goals for this table

- Structured report blocks / KPI series
- Evidence / file uploads
- Client portal publish snapshots
- PDF/export artifacts
- Topvisor metrics storage
- Automatic aggregation of weekly free-text into monthly fields inside DDL
