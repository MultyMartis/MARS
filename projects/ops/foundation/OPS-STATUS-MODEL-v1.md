# OPS — Status Model v1

**Status:** **documented** — controlled status vocabularies (design).  
**Program:** OPS — Business Operations Domain  
**Phase:** 2 — Operational Data Model Foundation  
**Date:** 2026-06-04  
**Parent:** [OPS-OPERATIONAL-DATA-MODEL-v1.md](OPS-OPERATIONAL-DATA-MODEL-v1.md)  
**Is not:** enum implementation in code, state machine runtime, or per-workflow ad-hoc status invention.

---

## 1. Purpose

Provide **small controlled vocabularies** for OPS so workflows do not each invent incompatible status strings.

**Rule ST-01:** New workflows **should** map their stages to these vocabularies. If a workflow needs a status not listed, use `OTHER` + `status_detail` free text and record gap in a follow-up report — do not silently fork vocabulary.

---

## 2. Case statuses

Used by **OpsCase** — see [OPS-CASE-MODEL-v1.md](OPS-CASE-MODEL-v1.md).

| Status | Meaning |
|--------|---------|
| `OPEN` | Case created; scope confirmed |
| `IN_PROGRESS` | Active work |
| `BLOCKED` | Cannot proceed without resolution |
| `PENDING_APPROVAL` | Approval gate active |
| `READY_TO_CLOSE` | Work complete; awaiting final close record |
| `CLOSED` | Terminal success |
| `CANCELLED` | Terminal abandon |

**Do not use for cases:** `DRAFT`, `SENT`, `APPROVED` — those belong to approval or sub-records.

---

## 3. Document statuses

Used by **DocumentRecord** (operational tracking — not legal status).

| Status | Meaning |
|--------|---------|
| `NOT_STARTED` | Document work not begun |
| `IN_PREPARATION` | Draft or package assembly |
| `INTERNAL_REVIEW` | Studio review before external routing |
| `PENDING_APPROVAL` | ApprovalRequest active |
| `APPROVED_FOR_ROUTING` | Operational approval to send/route |
| `ROUTED` | Sent to counterparty or internal legal/accounting |
| `ON_HOLD` | Paused — external dependency |
| `CLOSED` | Operational thread complete |
| `CANCELLED` | Abandoned |

**Legal status** (signed, registered, etc.) is **outside OPS** — human/legal systems only.

---

## 4. Report statuses

Used by **ReportRecord** (monthly and other client reports).

| Status | Meaning |
|--------|---------|
| `CYCLE_OPEN` | Period confirmed; context gathering |
| `EVIDENCE_COLLECTION` | Work evidence stage |
| `DRAFT` | Report draft in progress |
| `MISSING_DATA_REVIEW` | Blockers on ATLAS or evidence |
| `OPERATOR_REVIEW` | Internal quality review |
| `PENDING_APPROVAL` | Awaiting approver |
| `APPROVED` | Cleared to prepare delivery |
| `DELIVERED` | Client received report (human attested) |
| `CLOSED` | Cycle completion recorded |
| `CANCELLED` | Cycle abandoned |

**Not report statuses:** `READY_FOR_REVIEW` belongs to **ApprovalRequest** only — see §8. Do **not** set `ReportRecord.status` to `READY_FOR_REVIEW`. At workflow stage 6 (Operator Review), report status is `OPERATOR_REVIEW` while linked `ApprovalRequest` may be `READY_FOR_REVIEW`.

**Label disambiguation (ST-02):** `APPROVED` on `ReportRecord` means cleared to prepare delivery; `APPROVED` on `ApprovalRequest` means approver attested readiness. Always qualify by record type in operator notes when both are active (stage 7–8).

**Alignment:** Maps to [OPS-WF-01-MONTHLY-REPORTING-v1.md](../workflows/OPS-WF-01-MONTHLY-REPORTING-v1.md) and [OPS-MONTHLY-REPORTING-WORKFLOW-v1.md](../workflows/OPS-MONTHLY-REPORTING-WORKFLOW-v1.md) stages 1–10 without replacing stage names in the stage-detail doc.

---

## 5. Communication statuses

Used by **CommunicationDraft**.

| Status | Meaning |
|--------|---------|
| `DRAFT` | Message being written |
| `PENDING_APPROVAL` | Awaiting approver |
| `APPROVED` | Cleared to send |
| `SENT` | Dispatched (human attested) |
| `CANCELLED` | Not sent |

---

## 6. Escalation statuses

Used by **EscalationRecord**.

| Status | Meaning |
|--------|---------|
| `OPEN` | Escalation raised |
| `ACKNOWLEDGED` | Owner assigned |
| `IN_PROGRESS` | Active remediation |
| `RESOLVED` | Blocker cleared or deadline recovered |
| `CLOSED` | Terminal |
| `CANCELLED` | Escalation withdrawn |

---

## 7. Deadline statuses

Used by **Deadline** — see [OPS-DEADLINE-MODEL-v1.md](OPS-DEADLINE-MODEL-v1.md).

| Status | Meaning |
|--------|---------|
| `ACTIVE` | Future due date |
| `DUE_SOON` | Optional operator flag — within reminder window |
| `OVERDUE` | Past `due_at` without `met_at` |
| `MET` | Obligation attested complete |
| `WAIVED` | Explicitly waived with human note |
| `CANCELLED` | Deadline no longer applies |

---

## 8. Approval statuses (cross-reference)

Approval states are defined normatively in [OPS-APPROVAL-MODEL-v1.md](OPS-APPROVAL-MODEL-v1.md):

| Status | Meaning (ApprovalRequest) |
|--------|----------------------------|
| `DRAFT` | Request prepared; artifact not yet submitted for review |
| `READY_FOR_REVIEW` | Artifact fixed; awaiting designated approver — **WF-01 stage 6 typical entry** |
| `APPROVED` | Approver attested readiness; outbound may proceed |
| `SENT` | Outbound action executed (human confirms) |
| `COMPLETED` | Approval thread closed |
| `CANCELLED` | Request withdrawn |

**Canonical meaning of `READY_FOR_REVIEW`:** Only on `ApprovalRequest`. It does **not** apply to OpsCase, ReportRecord, or DocumentRecord status fields.

Do not reuse approval states as case or report statuses.

---

## 9. Task statuses (minimal)

Used by **TaskRecord** for checklist items within a case.

| Status | Meaning |
|--------|---------|
| `TODO` | Not started |
| `IN_PROGRESS` | Active |
| `DONE` | Complete |
| `CANCELLED` | Dropped |

---

## 10. Status mapping discipline

| Discipline | Rule |
|------------|------|
| **One primary status field** | Each record type has exactly one `status` from its vocabulary |
| **No string invention** | Avoid `in_review_2`, `almost_done` in persisted labels |
| **Cross-record consistency** | Case `PENDING_APPROVAL` should align with report or document `PENDING_APPROVAL` when linked |
| **Terminal states** | `CLOSED`, `CANCELLED`, `COMPLETED` (approval) do not transition without new record |

---

## 11. Related documents

| Document | Link |
|----------|------|
| Case model | [OPS-CASE-MODEL-v1.md](OPS-CASE-MODEL-v1.md) |
| Approval model | [OPS-APPROVAL-MODEL-v1.md](OPS-APPROVAL-MODEL-v1.md) |
| Deadline model | [OPS-DEADLINE-MODEL-v1.md](OPS-DEADLINE-MODEL-v1.md) |
| Monthly reporting workflow | [../workflows/OPS-MONTHLY-REPORTING-WORKFLOW-v1.md](../workflows/OPS-MONTHLY-REPORTING-WORKFLOW-v1.md) |

---

*OPS — Status Model v1 · controlled vocabularies (documentation only).*
