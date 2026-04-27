# MARS — Approval gates (NEED HUMAN APPROVAL)

**Status:** **documented contract only** — defines **when** human approval is **required** before proceeding. **No** workflow engine, ticket system, or HITL UI is shipped from this repo in Phase 1.

**Version:** v0.

---

## 1. Purpose

**Approval gates** specify **conditions** under which MARS **must** emit or honor **NEED HUMAN APPROVAL** (see [../governance/system-signals-dictionary.md](../governance/system-signals-dictionary.md), `../workflows/task-contract-v0.md` §3, **hitl_gates**). They align **Security / Guardrails** with **Workflow** and **Control Plane** without prescribing tooling.

---

## 2. NEED HUMAN APPROVAL — mandatory conditions (v0)

The following classes of action **require** explicit human approval in the **contract model** before execution proceeds (or before results are **adopted** as system truth):

| Condition | Rationale |
|-----------|-----------|
| **Filesystem changes** | Writes, deletes, renames, mass edits — irreversible or hard-to-revert impact; overlaps **STRUCTURE CHANGE** when tree or many files move. |
| **Structure changes** | **Project layout**, module boundaries, registry **schema** shifts, breaking renames — coordination and review. |
| **External API calls** | Egress and **third-party** effects; ties to **external-call** permission ([permissions-v0.md](permissions-v0.md)). |
| **Storage writes (especially PII)** | Durable persistence of user or sensitive data; **PII** demands heightened review and often legal/privacy process. |
| **Agent creation / update** | Alters **attack surface**, routing, and trust — **Agent Factory** defaults to HITL for non-trivial changes (`../agents/agent-factory-v0.md`). |
| **Tool usage with side effects** | Mutating tools, deploy tools, payment/email/admin tools — irreversible or externally visible effects. |

**Composite rule:** If a step spans **multiple** rows (e.g. external API + storage write), **NEED HUMAN APPROVAL** applies if **any** applicable row applies unless a **stricter** product policy is documented later.

---

## 3. Interaction with Task Contract

- **hitl_gates** on a Task **should** name **which** condition triggers approval (step id, tool id, or **condition class** from §2).
- **risk_level** **high** is a **strong signal** for approval even when §2 is borderline; exact mapping remains **product** decision — document in workflow addenda when fixed.

---

## 4. What this document does not do

- **Does not** implement approval UI, identity, or signatures.
- **Does not** define **SLA** or **approver roles** (owner, security — TBD).
- **Does not** replace **SECURITY RISK** handling: some risks may **block** entirely rather than “approve and proceed.”

---

## 5. SAFE UNKNOWN

Approver **identity**, **dual control**, and **audit trail format** for approvals are **SAFE UNKNOWN** until governance or implementation specifies them.
