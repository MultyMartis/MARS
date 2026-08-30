# I-SEO Report Hub — Monthly Report Lifecycle v0.1

**Status:** LIFECYCLE POLICY for DB-05 monthly report content statuses — no runtime/UI  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-26  
**Authority:** Operator I-SEO Report Hub Monthly Report Content DB-05 Charter 01  
**Related:** [I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-CHARTER-v0.1.md](I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-SCHEMA-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-SCHEMA-PLAN-v0.1.md), [I-SEO-REPORT-HUB-REPORTING-PERIOD-LIFECYCLE-v0.1.md](I-SEO-REPORT-HUB-REPORTING-PERIOD-LIFECYCLE-v0.1.md), [I-SEO-REPORT-HUB-WEEKLY-CHECKPOINT-LIFECYCLE-v0.1.md](I-SEO-REPORT-HUB-WEEKLY-CHECKPOINT-LIFECYCLE-v0.1.md)

---

## 1. Lifecycle states

A **monthly report content** row is the final/monthly working document for one **reporting period**.

| Status | Semantics |
|--------|-----------|
| `draft` | Shell created; content may be empty; work not started |
| `in_progress` | Specialist actively drafting monthly narrative |
| `ready_for_review` | Specialist submitted; waiting for reviewer |
| `reviewed` | Reviewer accepted; `reviewed_at` expected |
| `finalized` | Monthly document locked as final working content; `finalized_at` expected |
| `archived` | Frozen historical state without hard delete |

Default create status: `draft`.

---

## 2. Allowed transitions

### Happy path

```text
draft → in_progress → ready_for_review → reviewed → finalized
```

### Recommended transition matrix

| From | To | Notes |
|------|----|-------|
| `draft` | `in_progress` | Start drafting |
| `in_progress` | `ready_for_review` | Submit for review |
| `ready_for_review` | `reviewed` | Reviewer accept |
| `reviewed` | `finalized` | Lock monthly content |
| any non-`finalized` | `archived` | Soft retire |
| `ready_for_review` | `in_progress` | Revision request (future app) |
| `finalized` | `in_progress` or `draft` | Reopen — **`admin_owner` only** |
| `archived` | `draft` or `in_progress` | Reopen — prefer `admin_owner` only |

### Backward / reopen policy

- `reviewed` / `finalized` **must not** move backward without `admin_owner` (future app enforcement).
- Prefer correction notes in `internal_notes` over silent status rollback.
- DB CHECK enforces status **values**, not transition graph. Transition graph is app/service policy.

---

## 3. Owner / reviewer

| Field | Role |
|-------|------|
| `owner_user_id` | Primary specialist drafting the monthly document |
| `reviewer_user_id` | Lead/reviewer for `ready_for_review` → `reviewed` |
| `created_by` / `updated_by` | Audit actors (nullable FKs) |

Role expectations (future app; not DB-enforced):

| Role | Monthly content responsibilities |
|------|----------------------------------|
| `admin_owner` | Any transition; reopen finalized; archive |
| `seo_lead_reviewer` | Review; set reviewed/finalized; assign reviewer |
| `seo_specialist` | Own assigned monthly draft; draft → in_progress → ready_for_review |
| `account_client_manager` | Read / limited coordinate (exact edit policy deferred) |
| `internal_viewer` | Read-only |
| `client_viewer` | **No** internal monthly content management in MVP |

---

## 4. Reviewed / finalized timestamps

| Event | Timestamp policy |
|-------|------------------|
| Enter `reviewed` | Set `reviewed_at` if null; refresh only under admin correction policy |
| Leave `reviewed` backward (admin only) | Prefer retain `reviewed_at` + audit note |
| Enter `finalized` | Set `finalized_at` if null |
| Reopen from `finalized` (admin only) | Clear or retain `finalized_at` — prefer retain + audit note until reopen policy is implemented |
| Enter `archived` | Do **not** require `finalized_at` |
| Create / update content | Touch `updated_at` / `updated_by` |

DB schema stores nullable DATETIME columns; **setting** them is an app-layer rule for future CRUD.

---

## 5. Finalized lock policy

| Status | Editability (future app) |
|--------|--------------------------|
| `draft` / `in_progress` | Full edit by owner/admin |
| `ready_for_review` | Limited owner edit; reviewer acts |
| `reviewed` | Locked except admin_owner (or lead reopen policy if later chartered) |
| `finalized` | **Read-only** except `admin_owner` reopen/archive |
| `archived` | Frozen; reopen prefer admin_owner |

Finalized means the monthly **working document** is locked for internal ops — it is **not** an automatic client publish event.

---

## 6. Archived policy

| Status | When to use |
|--------|-------------|
| `archived` | Keep row for history but freeze from normal specialist edit |

Rules:

- Prefer `archived` over DELETE.
- Archived monthly content remains FK-linked to the period.
- Unique `(reporting_period_id)` still applies — archiving does not free the slot for a second row; reopen/edit the same row or charter a redesign.

---

## 7. Relation to reporting period status

Period status (DB-03) remains the **rollup**:

| Period status (examples) | Typical monthly content picture |
|--------------------------|---------------------------------|
| `draft` / `active` | Monthly content absent or `draft` / `in_progress` |
| `weekly_review` | Monthly content may still be absent while weeks progress |
| `monthly_review` | Monthly content `ready_for_review` / `reviewed` |
| `finalized` | Monthly content ideally `finalized` (app policy later) |
| `archived` | Monthly content should not be actively edited |

DB-05 does **not** auto-update `reporting_periods.status` when monthly content status changes. Future service may propose rollup rules; not part of migration DDL.

---

## 8. Relation to weekly checkpoint statuses

| Topic | Policy |
|-------|--------|
| Prerequisite | Prefer having weekly checkpoints present, but **do not** DB-require completed weeks before creating monthly content |
| Source hint | `source_weekly_checkpoint_ids` may list current period checkpoint ids |
| Coupling | Weekly checkpoint status changes do **not** auto-change monthly content status |
| Aggregation | No automatic copy of weekly TEXT fields into monthly fields in DB-05 |

Typical ops expectation (future app guidance, not DDL):

- Monthly drafting often starts after several weekly checkpoints exist.
- Finalization may prefer weeks mostly `completed` / `skipped` / `reviewed`, but that is service policy later.

---

## 9. Audit events (future app layer)

Recommended audit event names (not created by DB-05 migration):

- `monthly_report_content.created`
- `monthly_report_content.updated`
- `monthly_report_content.status_changed`
- `monthly_report_content.reviewed`
- `monthly_report_content.finalized`
- `monthly_report_content.archived`

Payload should include monthly content id, period id, old/new status when relevant. No secrets.

---

## 10. Deletion policy

| Action | MVP policy |
|--------|------------|
| Hard DELETE | **Forbidden** in MVP product flows |
| Soft path | Use `archived` |
| DB FK on period | `ON DELETE RESTRICT` — cannot drop period while monthly content exists |
| Smoke cleanup | Apply wave may delete **demo** smoke row only if charter allows leaving table empty or known demo set |

No cascade delete of monthly history through casual period deletion.
