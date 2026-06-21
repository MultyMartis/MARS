# OPS WF-02 — Document Closing v1

**Status:** **documented** — human-operated workflow (architecture family).  
**Workflow ID:** WF-02  
**Program:** OPS — Business Operations Domain  
**Date:** 2026-06-04  
**Parent:** [../foundation/OPS-WORKFLOW-ARCHITECTURE-v1.md](../foundation/OPS-WORKFLOW-ARCHITECTURE-v1.md)  
**MVP note:** **Deferred** from Monthly Reporting MVP — documented for operational expansion.

---

## 1. Purpose

Structure **document preparation, internal review, and routing** for contracts, acts, annexes, and closure packages as an operational thread — tracking versions, checkpoints, and handoffs without OPS becoming **legal** or **accounting** authority.

**Clarification (normative):**

> **OPS prepares and tracks.** OPS does **not** become accounting authority, legal signatory, or ledger SoT.

---

## 2. Trigger

| Trigger type | Description |
|--------------|-------------|
| **Agreement milestone** | Human identifies document obligation from ATLAS agreement ref |
| **Reporting surfacing** | WF-01 evidence or client request reveals missing act/annex |
| **Project phase change** | WF-06 may open document closing sub-threads |
| **Operator request** | Ad-hoc document package |

---

## 3. Inputs

| Input | Source | OPS handling |
|-------|--------|--------------|
| Organization / agreement refs | ATLAS | `related_atlas_entities` on OpsCase |
| Requisites | ATLAS only | Reference — never invented |
| Document templates | Human library outside OPS SoT | Operational version labels |
| Attachments checklist | Operator | `DocumentRecord` + `TaskRecord` |
| Routing instructions | Human | Notes on case |

---

## 4. OpsCase usage

| Aspect | Specification |
|--------|---------------|
| **Case type** | `DOCUMENT_CLOSING` |
| **Open** | Scope and document list confirmed — `OPEN` |
| **Preparation** | `IN_PROGRESS` · `DocumentRecord` `IN_PREPARATION` |
| **Review / approval** | `INTERNAL_REVIEW` / `PENDING_APPROVAL` |
| **External dependency** | `ON_HOLD` or `BLOCKED` |
| **Close** | `READY_TO_CLOSE` → `CLOSED` |

**Linked records:** `DocumentRecord`(s), `Deadline` (`DOCUMENTS`), `ApprovalRequest` (`document`, `closure`), optional `TaskRecord` per attachment.

---

## 5. Stages

| Stage | Name | Primary actor | Document status (typical) |
|-------|------|---------------|----------------------------|
| 1 | Intake & scope | Human operator | `NOT_STARTED` |
| 2 | Collect inputs | Document Operations role prep | `IN_PREPARATION` |
| 3 | Assemble package | Human operator | `IN_PREPARATION` |
| 4 | Internal review | Human reviewer | `INTERNAL_REVIEW` |
| 5 | Operational approval | Approver | `PENDING_APPROVAL` → `APPROVED_FOR_ROUTING` |
| 6 | Route externally | Human (legal/accounting channel) | `ROUTED` |
| 7 | Track external status | Human operator | `ON_HOLD` or `IN_PREPARATION` |
| 8 | Operational close | Human operator | `CLOSED` |

**Automation:** None.

---

## 6. Approvals

| Gate | Subject | Notes |
|------|---------|-------|
| Internal operational review complete | Document package version | Non-legal — routing permission only |
| External send / counterparty dispatch | Document package | Requires `APPROVED` — human executes send outside OPS |
| Case closure | `DOCUMENT_CLOSING` case | `ApprovalRequest` `closure` type |

**Outside OPS:** Legal signature, registration, invoice amounts, payment confirmation.

---

## 7. Outputs

| Output | Consumer |
|--------|----------|
| Document workflow status | Operator |
| Internal review package | Human reviewers |
| Routing handoff record | Legal / accounting (human channels) |
| Closed `DocumentRecord` set | WF-06 completion review |

---

## 8. Completion conditions

| Condition | Required |
|-----------|----------|
| All in-scope `DocumentRecord` `CLOSED` or `CANCELLED` with reason | Yes |
| Mandatory approvals `COMPLETED` or documented exception | Yes |
| External legal/financial outcomes | **Not** required in OPS — may remain SAFE UNKNOWN in legal systems |
| OpsCase `CLOSED` | Yes |
| Document deadlines `MET` or `WAIVED` | Yes |

---

## 9. Relationship with Document Operations role

The conceptual **Document Operations Agent** ([OPS-AGENT-DECOMPOSITION-v1.md](../foundation/OPS-AGENT-DECOMPOSITION-v1.md)):

| Function | WF-02 stage |
|----------|-------------|
| Checklist | Stages 2–3 |
| Version labels | Stage 3 |
| Completeness flags | Stages 2, 4 |
| Routing prep | Stage 6 |

Human operator owns case status and external route execution.

---

## 10. Relationship with Monthly Reporting (WF-01)

| Direction | Interaction |
|-----------|-------------|
| WF-01 → WF-02 | Report may cite document gaps; separate OpsCase recommended |
| WF-02 → WF-01 | Closed acts may become evidence in next `ReportRecord` |
| Shared ATLAS refs | Same client/project refs on both cases — no duplicate canonical data |

**Rule WF02-R01:** Document legal substance changes are **not** recorded as OPS canonical facts — operator notes only.

---

## 11. Cross-workflow links

| Workflow | Link |
|----------|------|
| WF-04 | `DOCUMENTS` category deadlines |
| WF-05 | Stale approval, persistent `ON_HOLD` |
| WF-06 | Completion checklist includes open document cases |

---

*OPS WF-02 — Document Closing v1 · human-operated only.*
