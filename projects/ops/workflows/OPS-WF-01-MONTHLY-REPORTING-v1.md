# OPS WF-01 — Monthly Reporting v1

**Status:** **documented** — human-operated workflow (architecture family).  
**Workflow ID:** WF-01  
**Program:** OPS — Business Operations Domain  
**MVP:** Monthly Client Reporting Control MVP  
**Date:** 2026-06-04  
**Parent:** [../foundation/OPS-WORKFLOW-ARCHITECTURE-v1.md](../foundation/OPS-WORKFLOW-ARCHITECTURE-v1.md)  
**Stage detail reference:** [OPS-MONTHLY-REPORTING-WORKFLOW-v1.md](OPS-MONTHLY-REPORTING-WORKFLOW-v1.md)

---

## Document authority (A-05)

| Document | Role |
|----------|------|
| **This file (OPS-WF-01-MONTHLY-REPORTING-v1.md)** | **Workflow contract** — triggers, inputs, OpsCase usage, approvals, outputs, completion conditions, cross-workflow links |
| **[OPS-MONTHLY-REPORTING-WORKFLOW-v1.md](OPS-MONTHLY-REPORTING-WORKFLOW-v1.md)** | **Stage detail reference** — step-by-step actions, outputs, and per-stage operator guidance for stages 1–10 |

On conflict between documents, **this file (WF-01 contract)** governs case/report/approval status timing and completion conditions. Stage-detail doc governs step granularity only.

---

## 1. Purpose

Operate the **monthly (or contract-period) client reporting cycle**: gather ATLAS context and human-attested evidence, produce and approve a draft, prepare human send, and record completion — without OPS becoming the source of business or financial truth.

---

## 2. Trigger

| Trigger type | Description |
|--------------|-------------|
| **Calendar rhythm** | Previous calendar month ends — operator or Executive Assistant rhythm proposes cycle |
| **Contract cadence** | Non-monthly period — human confirms bounds before case open |
| **Prior cycle follow-up** | WF-01 stage 10 or WF-03 may surface “start next period” reminder |

**Automation:** None. Trigger is **human-initiated**.

---

## 3. Inputs

| Input | Source | OPS handling |
|-------|--------|--------------|
| Client / project / agreement context | ATLAS or operator attestation | References on OpsCase |
| Reporting period | Human-confirmed | `reporting_period` on case |
| Work evidence | MetaBOT, ORCA, MIG, WPilot, OCPilot, tickets — **cited only** | Evidence index on `ReportRecord` |
| Report template | Human-maintained (outside OPS SoT) | Applied in draft stage |
| Prior month report (optional) | OPS archive **SAFE UNKNOWN** | Reference only |
| Internal due dates | Human-set | `Deadline` category `REPORTING` |

---

## 4. OpsCase usage

| Aspect | Specification |
|--------|---------------|
| **Case type** | `MONTHLY_REPORTING` |
| **Open** | Stage 1 — Reporting Trigger: status `OPEN` |
| **Active work** | Stages 2–6: `IN_PROGRESS`; stage 5 hold → `BLOCKED` |
| **Approval** | Stage 7: `PENDING_APPROVAL` → `IN_PROGRESS` after approval |
| **Delivery prep** | Stage 8: `IN_PROGRESS` |
| **Pre-close** | Stage 9: `READY_TO_CLOSE` — after delivery attested and completion metadata recorded |
| **Terminal** | Stage 10: `CLOSED` |

**Linked records:**

| Record | Role |
|--------|------|
| `ReportRecord` | Draft → review → delivery → close metadata; `review_log` at stage 6; `completion_metadata` at stage 9 — statuses per [OPS-STATUS-MODEL-v1.md](../foundation/OPS-STATUS-MODEL-v1.md) |
| `Deadline` | Internal draft, approval, client send |
| `ApprovalRequest` | `approval_subject_type: report` — mandatory before send |
| `TaskRecord` | Optional checklist items per stage |

**Rule WF01-C01:** One primary OpsCase per client + `reporting_period` unless human documents duplicate merge (ODM-06).

---

## 5. Stages

Stages 1–10 are normatively defined in [OPS-MONTHLY-REPORTING-WORKFLOW-v1.md](OPS-MONTHLY-REPORTING-WORKFLOW-v1.md).

| Stage | Name | Case status | Report status | Approval status (typical) |
|-------|------|-------------|---------------|---------------------------|
| 1 | Reporting Trigger | `OPEN` | `CYCLE_OPEN` | — |
| 2 | Context Collection | `IN_PROGRESS` | `CYCLE_OPEN` | — |
| 3 | Work Evidence Collection | `IN_PROGRESS` | `EVIDENCE_COLLECTION` | — |
| 4 | Draft Report Preparation | `IN_PROGRESS` | `DRAFT` | `DRAFT` |
| 5 | Missing Data Review | `BLOCKED` or `IN_PROGRESS` | `MISSING_DATA_REVIEW` | — |
| 6 | Operator Review | `IN_PROGRESS` | `OPERATOR_REVIEW` | `READY_FOR_REVIEW` |
| 7 | Approval | `PENDING_APPROVAL` → `IN_PROGRESS` | `PENDING_APPROVAL` → `APPROVED` | `APPROVED` |
| 8 | Client Delivery Preparation | `IN_PROGRESS` | `APPROVED` | `APPROVED` → `SENT` |
| 9 | Completion Recording | `READY_TO_CLOSE` | `DELIVERED` | `SENT` → `COMPLETED` |
| 10 | Closing Status Update | `CLOSED` | `CLOSED` | `COMPLETED` |

---

## 6. Approvals

| Gate | Approval subject | Approver |
|------|------------------|----------|
| Client delivery authorized | Report for period | Studio lead or delegated operator (HA-01) |
| Non-ATLAS identity in report | Attestation note | Human operator (Executive Assistant prepares packet only) |

**ApprovalRequest state path (stage 6–9):** `DRAFT` → `READY_FOR_REVIEW` → `APPROVED` → `SENT` → `COMPLETED`

**Scope:** `READY_FOR_REVIEW` applies to **ApprovalRequest** only — not `ReportRecord.status`. Report status at stage 6 is `OPERATOR_REVIEW`. See [OPS-STATUS-MODEL-v1.md](../foundation/OPS-STATUS-MODEL-v1.md) §4 and §8.

**Forbidden:** `DRAFT` → `APPROVED` without review; autonomous `APPROVED`.

Aligns with [OPS-APPROVAL-MODEL-v1.md](../foundation/OPS-APPROVAL-MODEL-v1.md) MA-01 and workflow stage 7.

---

## 7. Outputs

| Output | Consumer |
|--------|----------|
| Approved report package | Human send channel (email, portal, etc.) |
| Evidence index | Operator archive; optional client attachment |
| Completion metadata | `ReportRecord.completion_metadata` — workflow term **CompletionRecord**; OPS operational tracking; next-cycle input |
| Missing data register | ATLAS intake or operator follow-up (WF-03) |
| Follow-up list | WF-03, WF-04 reminders |

**OPS does not transmit** to client — human sends.

---

## 8. Completion conditions

| Condition | Required |
|-----------|----------|
| Report `ReportRecord` status `CLOSED` | Yes |
| Mandatory `ApprovalRequest` terminal (`COMPLETED` or documented exception) | Yes |
| Client delivery human-attested | Yes |
| Reporting `Deadline` records `MET` or `WAIVED` with note | Yes |
| OpsCase status `CLOSED` | Yes |
| No open `BLOCKED` without documented waiver | Yes |

---

## 9. Relationship with conceptual roles

### Executive Assistant

| Touchpoint | Action |
|------------|--------|
| Period boundary | Proposes Reporting Trigger checklist |
| Context | Assembles ATLAS reference packet for stage 2 |
| Deadlines | Proposes `REPORTING` deadlines and reminders (WF-04) |
| Follow-up | Surfaces stage 10 items to WF-03 |

Does **not** approve report send.

### Client Reporting Agent (Reporting Agent role)

| Touchpoint | Action |
|------------|--------|
| Evidence | Curates stage 3 bundle |
| Draft | Drives stages 4–6 under operator supervision |
| Delivery prep | Stage 8 packaging |
| Closure | Stage 9–10 metadata |

Does **not** replace human approver or sender.

### Document Closing (WF-02)

| Touchpoint | Action |
|------------|--------|
| Same period | Acts/annexes may run as separate `DOCUMENT_CLOSING` case |
| Evidence | Signed routing milestones may appear in report citations |
| Authority | OPS tracks document ops — **not** accounting or legal sign-off |

---

## 10. Cross-workflow links

| Workflow | Link |
|----------|------|
| WF-04 | Reporting deadlines and reminders |
| WF-05 | Blocker persistence, approval stale, overdue send |
| WF-03 | Post-close client questions |
| WF-06 | Engagement wrap-up includes report history review |

---

## 11. Governance

Described without violating forbidden runtime claims and **GC-OPS-008** (no fake operational automation).

---

*OPS WF-01 — Monthly Reporting v1 · human-operated only.*
