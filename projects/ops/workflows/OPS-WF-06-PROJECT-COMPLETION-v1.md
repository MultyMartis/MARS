# OPS WF-06 — Project Completion v1

**Status:** **documented** — human-operated workflow (architecture family).  
**Workflow ID:** WF-06  
**Program:** OPS — Business Operations Domain  
**Date:** 2026-06-04  
**Parent:** [../foundation/OPS-WORKFLOW-ARCHITECTURE-v1.md](../foundation/OPS-WORKFLOW-ARCHITECTURE-v1.md) · [../foundation/OPS-ATLAS-RELATIONSHIP-v1.md](../foundation/OPS-ATLAS-RELATIONSHIP-v1.md)

---

## 1. Purpose

Conduct **operational wrap-up** when an engagement or project phase ends: review reports, documents, follow-ups, and outstanding items; obtain closure approvals; record OPS completion — **without redefining project reality in ATLAS**.

**Clarification (normative):**

> **OPS records completion.** OPS does **not** redefine project structure, status, or canonical relationships in ATLAS.

Structural project truth remains **ATLAS** (when implemented) plus human governance outside OPS.

---

## 2. Trigger

| Trigger type | Description |
|--------------|-------------|
| **Engagement end** | Contract or statement of work completion |
| **Phase gate** | Milestone marked complete in human planning |
| **Client offboarding** | Account closure rhythm |
| **Operator-initiated** | Audit of dangling operational threads |

---

## 3. Inputs

| Input | Source |
|-------|--------|
| `atlas_project_ref` (and related client/org/agreement refs) | ATLAS or attestation |
| Open OpsCases for project | WF-01, WF-02, WF-03 search by reference |
| Report history | `ReportRecord` linked cases |
| Document status | `DocumentRecord` from WF-02 |
| Open escalations | WF-05 records |
| Outstanding deadlines | WF-04 on linked cases |

---

## 4. OpsCase usage

| Aspect | Specification |
|--------|---------------|
| **Case type** | `PROJECT_COMPLETION` |
| **Open** | Scope: which project/phase — `OPEN` |
| **Review** | `IN_PROGRESS` |
| **Approval** | Closure gate — `PENDING_APPROVAL` |
| **Close** | `CLOSED` |

**Linked records:** `TaskRecord` checklist, `ApprovalRequest` (`closure`), optional summary note (non-canonical).

---

## 5. Stages

| Stage | Name | Action |
|-------|------|--------|
| 1 | Scope confirmation | Confirm project/phase and ATLAS refs |
| 2 | Report review | All expected reporting cycles closed or waived |
| 3 | Document review | Open `DOCUMENT_CLOSING` cases resolved |
| 4 | Follow-up review | Open `FOLLOW_UP` cases resolved |
| 5 | Outstanding items | List blockers, waivers, handoffs to other domains |
| 6 | Operational approval | Approver attests OPS wrap-up complete |
| 7 | Completion record | Human-attested OPS completion metadata |
| 8 | Case close | `CLOSED` |

**Automation:** None.

---

## 6. Completion review

| Review area | Pass criteria |
|-------------|---------------|
| **Reports** | No required `MONTHLY_REPORTING` case `IN_PROGRESS` for covered periods — or documented waiver |
| **Documents** | No mandatory `DOCUMENT_CLOSING` case blocking handoff — or routed to legal/accounting with note |
| **Follow-ups** | No open client commitments in `FOLLOW_UP` without owner |
| **Escalations** | No open `EscalationRecord` on project-linked cases |
| **Deadlines** | Critical deadlines `MET`, `WAIVED`, or `CANCELLED` with reason |

---

## 7. Report review

| Check | Action |
|-------|--------|
| Final period report delivered? | Verify `ReportRecord` `CLOSED` |
| Evidence archived? | Operator attestation — storage **SAFE UNKNOWN** |
| ATLAS refs used in reports consistent? | Flag intake gaps — do not fix in OPS alone |

---

## 8. Document review

| Check | Action |
|-------|--------|
| Acts/annexes/contract packs closed operationally? | `DocumentRecord` terminal states |
| Legal sign-off state | **Outside OPS** — note only |
| Accounting closure | **Outside OPS** — handoff to accounting human |

---

## 9. Outstanding items

| Item type | Handling |
|-----------|----------|
| Open WF-01 cycle | Complete or cancel with reason before WF-06 close |
| Open WF-03 | Resolve, reassign, or escalate |
| ATLAS data gaps | Intake task to ATLAS path — not OPS invention |
| Future work | New project phase → new cases — not mixed into completion case |

---

## 10. Approvals

| Gate | Subject | Approver |
|------|---------|----------|
| OPS operational wrap-up complete | `closure` on `PROJECT_COMPLETION` case | Operations lead + engagement owner (studio policy) |

Does **not** approve legal termination, final invoice, or payment — accounting/legal outside OPS.

---

## 11. Closure conditions

| Condition | Required |
|-----------|----------|
| Checklist stages 2–5 documented | Yes |
| Mandatory `ApprovalRequest` `COMPLETED` | Yes |
| OpsCase `CLOSED` | Yes |
| ATLAS project structural update | **Not required in OPS** — separate human/ATLAS process |

---

## 12. Relationship with ATLAS entities

| ATLAS entity | OPS role in WF-06 |
|--------------|-------------------|
| **Project** | Primary reference — read for scope |
| **Client / Organization** | Context for communications and reports |
| **Agreement** | Scope boundary for what “complete” means operationally |
| **Website / Service** | Optional — verify deliverables cited in reports |

**Rule WF06-A01:** OPS completion record stores **references and attestation timestamps** — not authoritative project lifecycle state.

---

## 13. Cross-workflow links

| Workflow | Link |
|----------|------|
| WF-01 | Report cycle completeness |
| WF-02 | Document package completeness |
| WF-03 | Open client threads |
| WF-04 | Deadline clearance |
| WF-05 | Must be resolved or explicitly waived |

---

*OPS WF-06 — Project Completion v1 · human-operated only.*
