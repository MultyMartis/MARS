# I-SEO Report Hub — Reporting Period Lifecycle v0.1

**Status:** LIFECYCLE POLICY for DB-03 period statuses — no runtime/UI  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-25  
**Authority:** Operator I-SEO Report Hub DB-03 Reporting Periods Migration Charter 01  
**Related:** [I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-CHARTER-v0.1.md](I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-SCHEMA-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-SCHEMA-PLAN-v0.1.md), [I-SEO-REPORT-HUB-REPORT-LIFECYCLE-v0.1.md](I-SEO-REPORT-HUB-REPORT-LIFECYCLE-v0.1.md), [I-SEO-REPORT-HUB-REPORT-MODEL-v0.1.md](I-SEO-REPORT-HUB-REPORT-MODEL-v0.1.md)

---

## 1. Monthly period lifecycle

A **reporting period** is one calendar month of SEO reporting work for a single **project**.

```text
draft → active → weekly_review → monthly_review → finalized → archived
```

Optional shortcuts (policy for future UI; not enforced by DB CHECK):

- `draft → active` (start work)
- `active → monthly_review` (skip formal weekly_review at period level if weekly entities handle detail later)
- `monthly_review → active` (revision loop before finalize)
- `finalized → archived` (history)
- Admin may move `archived → finalized` only under exceptional HITL (prefer not)

`finalized_at` should be set when entering `finalized` and cleared only under exceptional admin correction (future app rule).

---

## 2. Relation to 3 weekly checkpoints + final monthly report

Product model (unchanged):

| Artifact | Count per period | Storage in DB-03 |
|----------|------------------|------------------|
| Weekly checkpoint | 3 (weeks 1–3) | **Deferred** (DB-04+) |
| Final monthly report | 1 | **Deferred** (DB-04+) |

Period row is the **parent shell**:

- While only `reporting_periods` exists, `status` approximates overall progress.
- When DB-04+ adds child entities, period status remains the **rollup**; child tables hold week/final detail states.

Conceptual nesting:

```text
reporting_period (DB-03)
  ├── weekly_checkpoint week=1 (future)
  ├── weekly_checkpoint week=2 (future)
  ├── weekly_checkpoint week=3 (future)
  └── monthly_report (future)
```

---

## 3. Allowed statuses and transitions

### Status meanings

| Status | Meaning |
|--------|---------|
| `draft` | Shell created; not started |
| `active` | In-progress monthly cycle (specialist working) |
| `weekly_review` | Period-level weekly review gate |
| `monthly_review` | Month-close / final under internal review |
| `finalized` | Period closed for ops; publish pipeline may come later |
| `archived` | Historical retention |

### Happy path

```text
draft → active → weekly_review → monthly_review → finalized → archived
```

### Revision path

```text
monthly_review → active → monthly_review → finalized
```

### Mapping to Report Lifecycle v0.1 (finer model)

| Report Lifecycle v0.1 (finer) | DB-03 period status |
|-------------------------------|---------------------|
| `planned` | `draft` |
| `active_week_1` / `_2` / `_3` | `active` (optionally `weekly_review`) |
| `monthly_draft` | `active` or `monthly_review` |
| `review` / `revision_requested` | `monthly_review` |
| `approved` / `published` | `finalized` (publish remains separate snapshot concern) |
| `archived` | `archived` |

DB-03 does **not** encode `published` separately — publishing belongs to snapshot model (later phase).

---

## 4. Role responsibilities

| Role | Period responsibilities (future app; not DB-enforced) |
|------|--------------------------------------------------------|
| `admin_owner` | Create/edit any period; force status; archive |
| `seo_lead_reviewer` | Review; move to `monthly_review` / `finalized`; assign reviewer |
| `seo_specialist` | Own/edit assigned periods; drive `draft`→`active`; prepare weekly/final content later |
| `account_client_manager` | Coordinate periods for accounts; limited edit per future policy |
| `internal_viewer` | Read-only period history |
| `client_viewer` | **Not** used for internal period management; client sees published output later |

---

## 5. What happens before report editor exists

Until weekly/final tables and CRUD UI exist:

1. Periods can exist as **history shells** (project + month + status).
2. Status workflow can be exercised via future minimal admin tools or SQL smoke only under charter.
3. Specialists cannot yet store checkpoint bodies in DB — process may still use external drafts.
4. No client-facing period list from this table.
5. Auth remains sufficient to protect future internal screens; DB-03 does not add routes.

DB-03 success = **schema + ledger**, not product UX completion.

---

## 6. Future DB-04+ relation

| Wave | Expected addition |
|------|-------------------|
| DB-04 (planned) | `weekly_checkpoints`, `monthly_reports` (or equivalent) FK → `reporting_periods.id` |
| Later | Blocks, work items, KPI, evidence, reviewer comments |
| Later | `published_snapshots` for client token URLs |

Rules for future child tables:

- Child rows must reference an existing period.
- Deleting a period with children should be RESTRICT unless a dedicated cascade charter says otherwise.
- Period `status` remains rollup; do not replace child state machines with only period status.
