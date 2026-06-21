# OPS WF-04 — Deadline Management v1

**Status:** **documented** — cross-cutting human-operated workflow (architecture family).  
**Workflow ID:** WF-04  
**Program:** OPS — Business Operations Domain  
**Date:** 2026-06-04  
**Parent:** [../foundation/OPS-WORKFLOW-ARCHITECTURE-v1.md](../foundation/OPS-WORKFLOW-ARCHITECTURE-v1.md) · [../foundation/OPS-DEADLINE-MODEL-v1.md](../foundation/OPS-DEADLINE-MODEL-v1.md)

---

## 1. Purpose

Define how **deadlines and reminders** are created, monitored, and escalated across all OPS threads — using the Deadline Model without claiming calendar, cron, or notification products.

**Clarification:** **No calendar implementation** in Phase 3.

---

## 2. Scope

WF-04 is **cross-cutting**: it overlays WF-01 through WF-06 rather than replacing them. Every active OpsCase may have 0..n `Deadline` and `Reminder` records.

---

## 3. Deadline creation

| Step | Actor | Action |
|------|-------|--------|
| 1 | Human operator or Executive Assistant rhythm | Identify obligation (report due, doc route, follow-up) |
| 2 | Link to `case_id` | Mandatory parent OpsCase |
| 3 | Set `category` | `REPORTING` \| `DOCUMENTS` \| `FOLLOW_UP` \| `COMPLIANCE` \| `OTHER` |
| 4 | Set `due_at` | Human-attested date/time |
| 5 | Set `priority` | May differ from case priority (DL-01) |
| 6 | Set `owner` | Responsible human |
| 7 | Initial `status` | `ACTIVE` |

**Examples (monthly reporting):**

| Label | Category | Typical timing |
|-------|----------|----------------|
| Internal draft complete | `REPORTING` | e.g. 5th business day of month |
| Approval complete | `REPORTING` | Before client send |
| Client send | `REPORTING` | Contractual or studio default |

---

## 4. Monitoring

| Activity | Description |
|----------|-------------|
| **Status review** | Operator periodically sets `DUE_SOON`, `OVERDUE` per judgment — no auto-scanner claimed |
| **Case coupling** | Critical deadline at risk may move case to `BLOCKED` |
| **Primary due mirror** | Case field `due_at` may reference most important deadline |
| **Reporting** | Operator checklist or cockpit display **SAFE UNKNOWN** |

**Rule WF04-M01:** `OVERDUE` does not auto-close or auto-escalate — human evaluates WF-05.

---

## 5. Reminder generation

| Step | Action |
|------|--------|
| 1 | Operator sets `remind_at` relative to `due_at` (e.g. T−2 days) |
| 2 | Link `reminder_id` to `deadline_id` when applicable |
| 3 | Status `SCHEDULED` until operator acknowledges |
| 4 | `ACKNOWLEDGED` or `DISMISSED` — does not change deadline status (RM-02) |

Executive Assistant **surfaces** reminders; does not schedule autonomously.

---

## 6. Escalation trigger

When monitoring reveals risk, human may invoke WF-05:

| Trigger type | Example |
|--------------|---------|
| `DEADLINE_PASSED` | `due_at` elapsed, status not `MET` |
| `APPROVAL_STALE` | Approval in `READY_FOR_REVIEW` beyond studio threshold (**SAFE UNKNOWN**) |
| `BLOCKER_PERSISTENT` | Parent case `BLOCKED` too long |

Creates or updates `EscalationRecord` — see [OPS-WF-05-ESCALATION-HANDLING-v1.md](OPS-WF-05-ESCALATION-HANDLING-v1.md).

---

## 7. Priority handling

| Priority | Handling guidance |
|----------|-------------------|
| `LOW` | Monitor on routine rhythm |
| `NORMAL` | Standard studio cadence |
| `HIGH` | Visible in operator standup; may pair with case `HIGH` |
| `URGENT` | Immediate human attention; strong candidate for WF-05 |

**Rule WF04-P01:** Urgent deadline does not bypass approval gates (HA-03).

---

## 8. Relationship with all workflows

| Workflow | WF-04 interaction |
|----------|-------------------|
| WF-01 | `REPORTING` deadlines for draft, approval, send |
| WF-02 | `DOCUMENTS` deadlines for prep and route milestones |
| WF-03 | `FOLLOW_UP` deadlines for response windows |
| WF-05 | Triggered from overdue or stale gates |
| WF-06 | Completion blocked if critical deadlines open without waiver |

---

## 9. OpsCase usage

WF-04 does not require a dedicated case type. Deadlines attach to:

| Parent case type | Typical deadlines |
|------------------|-------------------|
| `MONTHLY_REPORTING` | Reporting rhythm |
| `DOCUMENT_CLOSING` | Document milestones |
| `FOLLOW_UP` | Response due |
| `PROJECT_COMPLETION` | Wrap-up checklist dates |
| `ESCALATION` | Resolution target date (optional) |

---

## 10. Explicit non-goals

| Non-goal | Status |
|----------|--------|
| Google/Outlook sync | Out of scope |
| RRULE / recurring engine | Out of scope v1 |
| SLA enforcement automation | Forbidden |
| HomeGateway reminder UI | **SAFE UNKNOWN** |

---

*OPS WF-04 — Deadline Management v1 · human-operated only.*
