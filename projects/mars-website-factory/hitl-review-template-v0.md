# Operational template — HITL review (v0)

**Status:** **documentation-only** human-in-the-loop decision record. **Not** legally binding signatures, **not** cryptographic approval, **not** autonomous agent approval.

**Normative references:** [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md), [approval-semantics-v0.md](approval-semantics-v0.md), [reference-project-hitl-governance-v0.md](reference-project-hitl-governance-v0.md), [human-supervision-model-v0.md](human-supervision-model-v0.md), [orchestration-signals-v0.md](orchestration-signals-v0.md).

---

## 1. Decision context

| Field | Value |
|-------|-------|
| Gate (e.g. post-blueprint, post-design, pre-delivery) | |
| Artifacts in scope (ids / paths) | |
| Approver role(s) — **real human roles** | |
| Date | |

**Explicit:** Record **role titles and human names** only if the project actually uses named approvers. Otherwise use **role** + **contact channel** — do **not** invent signatories.

---

## 2. Approvals

| Item | Decision (approve / reject / defer) | Conditions |
|------|-------------------------------------|------------|
| | | |

---

## 3. Conditional approvals

Per [approval-semantics-v0.md](approval-semantics-v0.md):

| Condition | Satisfied by (artifact / evidence) | Owner |
|-----------|--------------------------------------|-------|
| | | |

---

## 4. Waivers

| Waiver | Scope | Risk acknowledged | Approver |
|--------|-------|-------------------|------------|
| | | | |

---

## 5. Escalations

| Issue | Escalated to | Status |
|-------|----------------|--------|
| | | |

Use signals such as **NEED HUMAN APPROVAL**, **SECURITY RISK**, **STRUCTURE CHANGE** per [system-signals-dictionary.md](../../governance/system-signals-dictionary.md) when applicable.

---

## 6. Freeze decisions

| Action | Scope frozen | Rationale |
|--------|--------------|-----------|
| Freeze / maintain / break | | |

Cross-ref [semantic-freeze-semantics-v0.md](semantic-freeze-semantics-v0.md).

---

## 7. Reopen conditions

Document **what evidence** or **which artifact revision** allows reopening a closed gate without silent scope creep.

---

## 8. Forbidden patterns (checklist)

- [ ] No **self-approval** by implementer lane alone ([reference-project-hitl-governance-v0.md](reference-project-hitl-governance-v0.md)).
- [ ] No **fake client** acceptance.
- [ ] No **autonomous** “bot approved” language.

---

## 9. Outcome summary

**Final posture:** (approved to proceed / blocked / conditional)

**Next operational step:** (e.g. R0x in [reference-run-sequence-v0.md](reference-run-sequence-v0.md))

---

*Template v0 — human authority without forged signatures.*
