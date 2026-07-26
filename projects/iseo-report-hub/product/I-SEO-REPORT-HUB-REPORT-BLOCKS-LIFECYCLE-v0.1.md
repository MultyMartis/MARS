# I-SEO Report Hub — Report Blocks Lifecycle v0.1

**Status:** LIFECYCLE POLICY for DB-06 report block statuses — no runtime/UI  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-26  
**Authority:** Operator I-SEO Report Hub Report Blocks DB-06 Charter 01  
**Related:** [I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-CHARTER-v0.1.md](I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-SCHEMA-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-SCHEMA-PLAN-v0.1.md), [I-SEO-REPORT-HUB-MONTHLY-REPORT-LIFECYCLE-v0.1.md](I-SEO-REPORT-HUB-MONTHLY-REPORT-LIFECYCLE-v0.1.md)

---

## 1. Lifecycle states

A **report block** row is one ordered structured section inside one **monthly report content** document.

| Status | Semantics |
|--------|-----------|
| `draft` | Shell created; content may be empty; work not started |
| `in_progress` | Specialist actively drafting the block |
| `ready_for_review` | Specialist submitted; waiting for reviewer |
| `reviewed` | Reviewer accepted; `reviewed_at` expected |
| `approved` | Block approved for composition readiness; `approved_at` expected |
| `archived` | Frozen historical state without hard delete |

Default create status: `draft`.

---

## 2. Allowed transitions

### Happy path

```text
draft → in_progress → ready_for_review → reviewed → approved
```

### Recommended transition matrix

| From | To | Notes |
|------|----|-------|
| `draft` | `in_progress` | Start drafting |
| `in_progress` | `ready_for_review` | Submit for review |
| `ready_for_review` | `reviewed` | Reviewer accept |
| `reviewed` | `approved` | Approve block for composition |
| any non-`approved` | `archived` | Soft retire |
| `ready_for_review` | `in_progress` | Revision request (future app) |
| `approved` | `in_progress` or `draft` | Reopen — **`admin_owner` / `seo_lead_reviewer` only** |
| `archived` | `draft` or `in_progress` | Reopen — prefer `admin_owner` / `seo_lead_reviewer` |

### Backward / reopen policy

- `reviewed` / `approved` **must not** move backward without `admin_owner` or `seo_lead_reviewer` (future app enforcement).
- Prefer correction notes in block `summary` / body over silent status rollback.
- DB CHECK enforces status **values**, not transition graph. Transition graph is app/service policy.

---

## 3. Owner / reviewer

| Field | Role |
|-------|------|
| `owner_user_id` | Primary specialist drafting the block |
| `reviewer_user_id` | Lead/reviewer for `ready_for_review` → `reviewed` |
| `created_by` / `updated_by` | Audit actors (nullable FKs) |

Role expectations (future app; not DB-enforced):

| Role | Block responsibilities |
|------|------------------------|
| `admin_owner` | Any transition; reopen approved; archive; reorder |
| `seo_lead_reviewer` | Review; set reviewed/approved; reopen approved; reorder |
| `seo_specialist` | Own assigned block draft; draft → in_progress → ready_for_review |
| `account_client_manager` | Read / limited coordinate (exact edit policy deferred) |
| `internal_viewer` | Read-only |
| `client_viewer` | **No** internal block management in MVP |

---

## 4. Reviewed / approved timestamps

| Event | Timestamp policy |
|-------|------------------|
| Enter `reviewed` | Set `reviewed_at` if null; refresh only under admin correction policy |
| Leave `reviewed` backward (privileged) | Prefer retain `reviewed_at` + audit note |
| Enter `approved` | Set `approved_at` if null |
| Reopen from `approved` (privileged) | Prefer retain `approved_at` + audit note until reopen policy is implemented |
| Enter `archived` | Do **not** require `approved_at` |
| Create / update content | Touch `updated_at` / `updated_by` |

DB schema stores nullable DATETIME columns; **setting** them is an app-layer rule for future CRUD.

---

## 5. Approved lock policy

| Status | Editability (future app) |
|--------|--------------------------|
| `draft` / `in_progress` | Full edit by owner/admin (subject to parent lock) |
| `ready_for_review` | Limited owner edit; reviewer acts |
| `reviewed` | Locked except privileged reopen |
| `approved` | **Read-only** except privileged reopen/archive |
| `archived` | Frozen; reopen prefer privileged roles |

Approved means the **section** is ready for composition — it is **not** a client publish event and does **not** finalize the parent monthly document.

---

## 6. Archived policy

| Status | When to use |
|--------|-------------|
| `archived` | Keep row for history but freeze from normal specialist edit |

Rules:

- Prefer `archived` over DELETE.
- Archived blocks remain FK-linked to the monthly report content.
- Unique `(monthly_report_content_id, block_key)` still applies — archiving does not free the key for a second active row; reopen/edit the same row or charter a redesign (e.g. soft-key versioning).

---

## 7. Relation to parent monthly report status

| Parent monthly status | Block edit policy (future app) |
|-----------------------|--------------------------------|
| `draft` / `in_progress` / `ready_for_review` / `reviewed` | Block lifecycle proceeds normally |
| `finalized` | **Lock all block editing** except `admin_owner` (and optionally `seo_lead_reviewer` if later chartered) |
| `archived` | Blocks should not be actively edited |

| Topic | Policy |
|-------|--------|
| Independent statuses | Yes at DB level — no trigger syncing block ↔ parent |
| Parent finalize lock | App/service policy: parent `finalized` locks block mutations |
| Parent TEXT fields | Remain fallback; no automatic overwrite from blocks in MVP |
| Parent status auto-update from blocks | **No** at DB level |

---

## 8. Relation to weekly checkpoint statuses

| Topic | Policy |
|-------|--------|
| Prerequisite | Prefer having weekly checkpoints present, but **do not** DB-require completed weeks before creating blocks |
| Source hint | `source_weekly_checkpoint_ids` may list current period checkpoint ids |
| Coupling | Weekly checkpoint status changes do **not** auto-change block status |
| Aggregation | No automatic copy of weekly TEXT into block body in DB-06 |

---

## 9. Audit events (future app layer)

Recommended audit event names (not created by DB-06 migration):

- `report_block.created`
- `report_block.updated`
- `report_block.status_changed`
- `report_block.reviewed`
- `report_block.approved`
- `report_block.archived`
- `report_block.reordered`

Payload should include block id, monthly report content id, period id (resolved), old/new status or order when relevant. No secrets.

---

## 10. Deletion policy

| Action | MVP policy |
|--------|------------|
| Hard DELETE | **Forbidden** in MVP product flows |
| Soft path | Use `archived` |
| DB FK on monthly parent | `ON DELETE RESTRICT` — cannot drop monthly content while blocks exist |
| Smoke cleanup | Apply wave may delete **demo** smoke block rows only if charter allows leaving known demo set |

No cascade delete of block history through casual monthly content deletion.

---

## 11. Reorder policy

| Topic | Policy |
|-------|--------|
| Mechanism | Update `sort_order` values (future service); optional batch reorder |
| Unique sort_order | **Not** enforced in MVP DB |
| Temporary duplicates | Allowed during draft reorder; list tie-break by `id` |
| Audit | Emit `report_block.reordered` for batch/order changes |
| UI | Drag/drop deferred; not part of DB-06 migration wave |
| Parent finalize | Reorder blocked when parent monthly is `finalized` (app policy) |
