# I-SEO Report Hub — Weekly Checkpoint Lifecycle v0.1

**Status:** LIFECYCLE POLICY for DB-04 weekly checkpoint statuses — no runtime/UI  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-26  
**Authority:** Operator I-SEO Report Hub Weekly Checkpoints DB-04 Charter 01  
**Related:** [I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-CHARTER-v0.1.md](I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-SCHEMA-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-SCHEMA-PLAN-v0.1.md), [I-SEO-REPORT-HUB-REPORTING-PERIOD-LIFECYCLE-v0.1.md](I-SEO-REPORT-HUB-REPORTING-PERIOD-LIFECYCLE-v0.1.md)

---

## 1. Lifecycle states

A **weekly checkpoint** tracks one weekly progress slice inside a **reporting period**.

| Status | Semantics |
|--------|-----------|
| `draft` | Shell created; content may be empty; work not started |
| `in_progress` | Specialist actively filling weekly progress |
| `ready_for_review` | Specialist submitted; waiting for reviewer |
| `reviewed` | Reviewer accepted; timestamps `reviewed_at` expected |
| `completed` | Week closed for ops; `completed_at` expected |
| `skipped` | Intentionally unused (e.g. short month / not needed) |
| `archived` | Frozen historical state without hard delete |

Default create status: `draft`.

---

## 2. Allowed transitions

### Happy path

```text
draft → in_progress → ready_for_review → reviewed → completed
```

### Recommended transition matrix

| From | To | Notes |
|------|----|-------|
| `draft` | `in_progress` | Start work |
| `in_progress` | `ready_for_review` | Submit |
| `ready_for_review` | `reviewed` | Reviewer accept |
| `reviewed` | `completed` | Close week |
| any non-`completed` | `skipped` | Intentional skip |
| any non-`completed` | `archived` | Soft retire |
| `ready_for_review` | `in_progress` | Revision request (future app) |
| `skipped` / `archived` | `draft` or `in_progress` | Reopen — prefer `admin_owner` only |

### Backward / reopen policy

- `reviewed` / `completed` **must not** move backward without `admin_owner` (future app enforcement).
- Prefer opening a correction note in free-text fields over silent rollback of status.
- DB CHECK enforces status **values**, not transition graph. Transition graph is app/service policy.

---

## 3. Owner / reviewer

| Field | Role |
|-------|------|
| `owner_user_id` | Primary specialist for the checkpoint |
| `reviewer_user_id` | Lead/reviewer for `ready_for_review` → `reviewed` |
| `created_by` / `updated_by` | Audit actors (nullable FKs) |

Role expectations (future app; not DB-enforced):

| Role | Checkpoint responsibilities |
|------|----------------------------|
| `admin_owner` | Any transition; reopen reviewed/completed; archive/skip |
| `seo_lead_reviewer` | Review; set reviewed/completed; assign reviewer |
| `seo_specialist` | Own assigned checkpoints; draft → in_progress → ready_for_review |
| `account_client_manager` | Read / limited coordinate (exact edit policy deferred) |
| `internal_viewer` | Read-only |
| `client_viewer` | **No** internal checkpoint management |

---

## 4. Reviewed / completed timestamps

| Event | Timestamp policy |
|-------|------------------|
| Enter `reviewed` | Set `reviewed_at` if null; refresh only under admin correction policy |
| Leave `reviewed` backward (admin only) | Clear or retain `reviewed_at` — prefer retain + audit note |
| Enter `completed` | Set `completed_at` if null |
| Enter `skipped` / `archived` | Do **not** require `completed_at` |
| Create / update content | Touch `updated_at` / `updated_by` |

DB schema stores nullable DATETIME columns; **setting** them is an app-layer rule for future CRUD.

---

## 5. Skipped / archived policy

| Status | When to use |
|--------|-------------|
| `skipped` | Week intentionally not used (flexible calendar; fewer than 3/4 weeks needed) |
| `archived` | Keep row for history but freeze from normal specialist edit |

Rules:

- Prefer `skipped` / `archived` over DELETE.
- Skipped weeks still occupy unique `week_index` / `checkpoint_key` (no reuse of same index for another week without admin redesign charter).
- Archived checkpoints remain FK-linked to the period.

---

## 6. Relation to reporting period status

Period status (DB-03) remains the **rollup**:

| Period status (examples) | Typical checkpoint picture |
|--------------------------|----------------------------|
| `draft` | Checkpoints may be absent or all `draft` |
| `active` | Some `in_progress` / `ready_for_review` |
| `weekly_review` | One or more `ready_for_review` / `reviewed` |
| `monthly_review` | Weekly checkpoints mostly `completed` / `skipped`; monthly content elsewhere |
| `finalized` / `archived` | Checkpoints should not be actively edited (future app rule) |

DB-04 does **not** auto-update period status when checkpoint status changes. Future service may propose rollup rules; not part of migration DDL.

---

## 7. Draft / in_progress / reviewed / completed semantics

| Status | Content expectation | Editability (future app) |
|--------|---------------------|--------------------------|
| `draft` | May be empty title+shell | Full edit by owner/admin |
| `in_progress` | Free-text fields being filled | Full edit by owner/admin |
| `ready_for_review` | Content ready enough for review | Limited owner edit; reviewer acts |
| `reviewed` | Accepted snapshot of week narrative | Locked except admin_owner |
| `completed` | Closed week | Locked except admin_owner |

Free-text fields are sufficient for MVP; structured blocks come later.

---

## 8. Audit events (future app layer)

Recommended audit event names (not created by DB-04 migration):

- `weekly_checkpoint.created`
- `weekly_checkpoint.updated`
- `weekly_checkpoint.status_changed`
- `weekly_checkpoint.reviewed`
- `weekly_checkpoint.completed`

Payload should include checkpoint id, period id, old/new status when relevant. No secrets.

---

## 9. Deletion policy

| Action | MVP policy |
|--------|------------|
| Hard DELETE | **Forbidden** in MVP product flows |
| Soft path | Use `skipped` or `archived` |
| DB FK on period | `ON DELETE RESTRICT` — cannot drop period while checkpoints exist |
| Smoke cleanup | Apply wave may delete **demo** smoke rows only if charter allows leaving table empty or known demo set |

No cascade delete of weekly history through casual period deletion.
