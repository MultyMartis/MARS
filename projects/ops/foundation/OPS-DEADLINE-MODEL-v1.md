# OPS — Deadline Model v1

**Status:** **documented** — conceptual deadline and reminder model (design).  
**Program:** OPS — Business Operations Domain  
**Phase:** 2 — Operational Data Model Foundation  
**Date:** 2026-06-04  
**Parent:** [OPS-OPERATIONAL-DATA-MODEL-v1.md](OPS-OPERATIONAL-DATA-MODEL-v1.md) · [OPS-CASE-MODEL-v1.md](OPS-CASE-MODEL-v1.md)  
**Is not:** calendar product, cron scheduler, or notification service implementation.

---

## 1. Purpose

Define **Deadline**, **Reminder**, and **Escalation Trigger** as operational constructs linked to **OpsCase**, with **priority** and **category** vocabularies shared across reporting, documents, follow-ups, and compliance rhythms.

**No calendar implementation** is defined or claimed in this phase.

---

## 2. Definitions

| Construct | Definition |
|-----------|------------|
| **Deadline** | A point in time by which an operational obligation should be met |
| **Reminder** | A human-facing nudge that a deadline approaches or passed — tracking intent only |
| **Escalation Trigger** | A condition (usually time- or blocker-based) that warrants elevated attention via `EscalationRecord` |

---

## 3. Deadline categories

| Category code | Label | Typical use |
|---------------|-------|-------------|
| `REPORTING` | Reporting | Internal draft due, client send due |
| `DOCUMENTS` | Documents | Contract/act prep, signature routing milestones |
| `FOLLOW_UP` | Follow-up | Post-delivery check-in, open question resolution |
| `COMPLIANCE` | Compliance | Regulatory or policy-driven dates (human-defined) |
| `OTHER` | Other | Operator-defined |

---

## 4. Priority (shared with case model)

| Priority | Meaning |
|----------|---------|
| `LOW` | Best-effort; no client commitment |
| `NORMAL` | Standard studio rhythm |
| `HIGH` | Client or leadership visibility expected |
| `URGENT` | Immediate human attention; often pairs with escalation |

**Rule DL-01:** Priority on a deadline may differ from parent case priority — human sets both explicitly.

---

## 5. Deadline fields (conceptual)

### Required

| Field | Description |
|-------|-------------|
| `deadline_id` | Unique within case |
| `case_id` | Parent OpsCase |
| `category` | Deadline category |
| `due_at` | Target date/time (human-attested; timezone **SAFE UNKNOWN**) |
| `status` | See deadline statuses in [OPS-STATUS-MODEL-v1.md](OPS-STATUS-MODEL-v1.md) |

### Suggested

| Field | Description |
|-------|-------------|
| `label` | Operator-facing description |
| `priority` | Priority vocabulary |
| `owner` | Who is responsible for meeting deadline |
| `met_at` | When obligation was attested complete |
| `notes` | Non-canonical context |

---

## 6. Reminder fields (conceptual)

| Field | Description |
|-------|-------------|
| `reminder_id` | Unique label |
| `case_id` | Parent OpsCase |
| `deadline_id` | Linked deadline (optional but recommended) |
| `remind_at` | When operator should be nudged |
| `status` | `SCHEDULED` \| `ACKNOWLEDGED` \| `DISMISSED` |
| `channel` | **SAFE UNKNOWN** — email, cockpit, manual checklist |

**Rule RM-01:** Reminders are **operator-owned** — set and dismissed by humans; no autonomous scheduling product claimed.

**Rule RM-02:** Dismissing a reminder **does not** close the deadline or case.

---

## 7. Escalation trigger (conceptual)

An **Escalation Trigger** is not necessarily a persisted row — it may be evaluated by humans from rules:

| Trigger type | Condition (examples) |
|--------------|----------------------|
| `DEADLINE_PASSED` | `due_at` elapsed and deadline status not `MET` |
| `APPROVAL_STALE` | `ApprovalRequest` in `READY_FOR_REVIEW` beyond studio SLA (**SAFE UNKNOWN** threshold) |
| `BLOCKER_PERSISTENT` | Case `BLOCKED` longer than operator threshold |
| `DATA_MISSING` | ATLAS reference unresolved through Missing Data Review |

When a trigger fires (human judgment), create or update **EscalationRecord** and optionally set case type `ESCALATION` or link child escalation to parent case.

---

## 8. Relationship with OpsCase

| Relationship | Description |
|--------------|-------------|
| **Containment** | Deadlines and reminders belong to one `OpsCase` |
| **Lifecycle** | Case may move to `BLOCKED` when critical deadline at risk |
| **Closure** | Case `CLOSED` typically requires reporting/document deadlines `MET` or explicitly waived with note |
| **Primary due** | Case field `due_at` may mirror the single most important `Deadline` |

---

## 9. Relationship with Executive Assistant role

The conceptual **Executive Assistant** (see [OPS-AGENT-DECOMPOSITION-v1.md](OPS-AGENT-DECOMPOSITION-v1.md)):

| Function | Deadline model touch |
|----------|---------------------|
| Rhythm | Proposes `REPORTING` deadlines at period open |
| Awareness | Surfaces upcoming `remind_at` dates to operator |
| Follow-up | Tracks open deadlines until `MET` or case closed |
| Escalation | Flags triggers for human escalation — **does not** auto-escalate |

**HomeGateway display** of reminders: **SAFE UNKNOWN** — future integration charter.

---

## 10. Example (monthly reporting)

| Deadline | Category | due_at | Notes |
|----------|----------|--------|-------|
| Internal draft complete | `REPORTING` | 5th business day | Linked to workflow stages 4–6 |
| Approval complete | `REPORTING` | Before client send | Pairs with `ApprovalRequest` |
| Client send | `REPORTING` | Contractual or studio default | Human confirms date |

Reminders may precede each `due_at` by operator-defined offset (e.g. 2 days).

---

## 11. Explicit non-goals

| Non-goal | Status |
|----------|--------|
| Google/Outlook calendar sync | **Out of scope** |
| Recurring RRULE engine | **Out of scope** v1 |
| Timezone normalization service | **SAFE UNKNOWN** |
| SLA enforcement automation | **Forbidden** to claim |

---

## 12. Related documents

| Document | Link |
|----------|------|
| Status model (deadline/reminder statuses) | [OPS-STATUS-MODEL-v1.md](OPS-STATUS-MODEL-v1.md) |
| Case model | [OPS-CASE-MODEL-v1.md](OPS-CASE-MODEL-v1.md) |
| Operational data model | [OPS-OPERATIONAL-DATA-MODEL-v1.md](OPS-OPERATIONAL-DATA-MODEL-v1.md) |
| Escalation statuses | [OPS-STATUS-MODEL-v1.md](OPS-STATUS-MODEL-v1.md) § Escalation |

---

*OPS — Deadline Model v1 · conceptual deadlines and reminders (documentation only).*
