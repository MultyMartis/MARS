# MARS Website Factory — Human Supervision Model v0

**Status:** **documentation only**. Website Factory v0 is **human-supervised orchestration**: humans sequence work, authorize transitions, and own REPORT evidence.

**Version:** v0.

**Related:** [first-operational-runbook-v0.md](first-operational-runbook-v0.md), [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md), [reference-project-hitl-governance-v0.md](reference-project-hitl-governance-v0.md), [project-execution-checkpoints-v0.md](project-execution-checkpoints-v0.md), [operator-lane-model-v0.md](operator-lane-model-v0.md), [`../../governance/execution-model.md`](../../governance/execution-model.md).

---

## 1. Human checkpoints

Checkpoints **C01–C08** are the **minimum** supervision spine for a reference project — see [project-execution-checkpoints-v0.md](project-execution-checkpoints-v0.md). They are **not** enforced by software in this repo.

Each checkpoint requires **named evidence** (links, REPORT IDs, ticket refs, or file paths — **project-specific storage** is **SAFE UNKNOWN**).

---

## 2. Supervision expectations

| Expectation | Description |
|-------------|-------------|
| **Readable trail** | Every material decision appears in a REPORT or equivalent audit surface ([reporting-standard-v0.md](reporting-standard-v0.md)). |
| **Two-person rule** | Where workflow specifies co-approval (e.g. PM + tech for **G3**), one person cannot stand in for both without explicit documented delegation ([stage-state-model-v0.md](stage-state-model-v0.md)). |
| **Assistant subordination** | Cursor/LLM output is **non-authoritative** for approvals and waivers ([cursor-execution-standard-v0.md](cursor-execution-standard-v0.md)). |

---

## 3. Review cadence

**Recommended** (tunable per org — not a contract):

- **Per stage REPORT** — mandatory at end of each reference run step (R01–R15) that mutates artifacts or files.
- **Per QA lane** — separate QA REPORT for blueprint, design, frontend, and final validation bundles.
- **Weekly** program-level supervision for multi-page programs — cross-page review per [multi-page-orchestration-v0.md](multi-page-orchestration-v0.md).

---

## 4. Approval discipline

- Approvals are **explicit** (“who, when, scope”) — not implied by merge or chat silence.
- **Conditional approvals** must state conditions and expiry per [approval-semantics-v0.md](approval-semantics-v0.md).
- **Waivers** require HITL authority per [validation-waiver-semantics-v0.md](validation-waiver-semantics-v0.md) / [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md).

---

## 5. Escalation discipline

- Use system signals vocabulary ([`../../governance/system-signals-dictionary.md`](../../governance/system-signals-dictionary.md), [orchestration-signals-v0.md](orchestration-signals-v0.md)).
- Escalations **must** appear in REPORT **HITL flags** and, when applicable, **Escalation report** ([reference-run-reporting-v0.md](reference-run-reporting-v0.md)).
- **No** escalation resolved “off book” without a follow-up REPORT noting resolution.

---

## 6. Freeze discipline

- Freezes are **declared in prose** with scope boundaries ([semantic-freeze-semantics-v0.md](semantic-freeze-semantics-v0.md)).
- Breaking a freeze requires **reopen** authorization + invalidation analysis — not ad-hoc edits ([revision-semantics-v0.md](revision-semantics-v0.md)).

---

## 7. SAFE UNKNOWN review

- Any unknown is listed with **what is missing** and **what would verify it** ([safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md)).
- Supervisors **must** accept or reject bounded assumptions; assumptions cannot authorize production deploy alone.

---

## 8. Clarifying statement

**Website Factory v0 is human-supervised orchestration.** There is **no** autonomous factory loop in MARS that replaces PM, design lead, tech lead, QA, or HITL approvers. Multi-agent behavior, when referenced, is **planned documentation alignment** per [agent-map.md](agent-map.md) — verify implementation separately per `AGENTS.md`.

---

*End of Human Supervision Model v0.*
