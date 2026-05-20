# MARS Website Factory - Agent Responsibility Boundary Model

**Status:** **documented** - Website Factory role-boundary model for human-supervised multi-agent coordination.  
**Not:** runtime role registry, permission engine, orchestration service, automated approval router, or universal agent law.

**Parent layer:** [multi-agent-coordination-governance.md](multi-agent-coordination-governance.md).  
**Drift taxonomy:** [multi-agent-drift-taxonomy.md](multi-agent-drift-taxonomy.md).  
**Related governance:** [human-escalation-governance.md](human-escalation-governance.md), [qa-confidence-governance.md](qa-confidence-governance.md), [decision-boundary-model.md](decision-boundary-model.md).

---

## 1. Purpose

This model defines the responsibility and authority boundaries that should remain visible when several AI-assisted roles contribute to Website Factory frontend production.

It answers:

- Who executes?
- Who reviews?
- Who validates?
- Who coordinates?
- Who owns escalation?
- Who has HITL authority?
- What happens when roles disagree?
- What survives into the next handoff?

The model is a coordination aid for operators and reports. It is not a runtime identity system.

---

## 2. Canonical Roles

| Role | Primary responsibility | Must not silently own |
|------|------------------------|-----------------------|
| **Executor** | Implements or edits the scoped artifact within source, prompt, and governance boundaries. | Independent review, validation truth, approval, waiver, unresolved escalation. |
| **Reviewer** | Challenges the executor output against source, scope, governance, and visible risks. | The executor's assumptions, implementation momentum, or final approval. |
| **Validator** | Checks evidence, QA conditions, proof boundaries, and PASS/PARTIAL/FAIL honesty. | Source authority, human approval, or executor narrative without evidence. |
| **Orchestrator** | Sequences roles, tracks handoffs, names blockers, and preserves coordination context. | Technical truth, validation truth, human approval, or hidden authority routing. |
| **Escalation authority** | Owns routing of ambiguity, contradiction, stop conditions, and decision-boundary questions. | HITL approval unless explicitly human-owned and recorded. |
| **HITL authority** | Human decision owner for approvals, waivers, priority conflicts, business meaning, delivery readiness, and project-specific tradeoffs. | AI execution, automatic validation, or unstated retroactive approval. |

Roles may be performed by the same human operator in small workflows, but the **responsibilities must remain distinguishable** in the report. When one AI session performs multiple roles, self-review must be disclosed and cannot be treated as independent validation.

---

## 3. Authority Boundaries

| Boundary | Executor | Reviewer | Validator | Orchestrator | Escalation authority | HITL authority |
|----------|----------|----------|-----------|--------------|----------------------|----------------|
| Implement scoped source changes | Yes | No | No | No | No | Can approve scope |
| Interpret source with confidence labels | Yes, within source governance | Yes, can challenge | Yes, can test evidence boundary | Tracks | Routes ambiguity | Resolves material ambiguity |
| Declare independent review | No | Yes, if independent | No | No | No | Can accept/reject |
| Declare QA confidence | Provides evidence | Challenges gaps | Yes, within evidence | Tracks | Routes gaps | Approves waivers |
| Resolve source contradiction | No | No | No | No | Routes | Yes, or named source priority |
| Approve waiver / release / delivery | No | No | No | No | Routes | Yes |
| Freeze scope | Can propose after checks | Can object | Can qualify evidence | Tracks | Blocks unresolved escalation | Approves when required |

**Rule:** downstream position in a chain does not grant higher authority. A validator is not more true because it runs later; a reviewer is not independent because it rewrites the executor summary; an orchestrator is not a HITL authority because it sequences tasks.

---

## 4. Responsibility Traceability

Every material handoff should preserve:

| Field | Required content |
|-------|------------------|
| **Scope** | Page, section, `block_id`, file set, source artifact, viewport, state, or report boundary. |
| **Role** | Executor, reviewer, validator, orchestrator, escalation authority, HITL authority, or other named role. |
| **Decision owner** | Source artifact, governance rule, prompt scope, implementation pack, operator instruction, human decision, or SAFE UNKNOWN. |
| **Evidence owner** | Who produced or checked source-level, build-level, rendered, direct interaction, inferred, assumed, or unknown evidence. |
| **Assumptions** | Explicit assumptions retained as assumptions, not promoted by handoff. |
| **Contradictions** | Conflicts preserved until resolved by authority. |
| **Escalation state** | None, HITL-recommended, HITL-required, blocked-by-ambiguity, blocked-by-contradiction, waived, or resolved. |
| **Next owner** | Role responsible for the next action or decision. |

---

## 5. Escalation Routing

Use this routing when coordination exposes ambiguity or conflict:

| Trigger | First owner | Escalation route |
|---------|-------------|------------------|
| Source ambiguity | Executor or reviewer | Source Interpretation -> Human Escalation -> HITL if material. |
| Evidence gap | Validator | QA Confidence -> Human Escalation if PASS/freeze would exceed proof boundary. |
| Implementation ownership gap | Executor or reviewer | Implementation Reliability -> Human Escalation if structural authority is unclear. |
| Contradictory sources or prompts | Any role | Human Escalation -> HITL or named source priority; do not resolve by consensus. |
| Reviewer/executor role collapse | Reviewer or orchestrator | Multi-Agent Findings; seek independent review or disclose non-independent review. |
| Validator contamination | Validator or orchestrator | Re-run with independent evidence or mark validation partial/contaminated. |
| Orphaned escalation | Orchestrator | Assign escalation owner before freeze or delivery claim. |
| Fake consensus risk | Any role | Require evidence and authority boundary review; multiple agreement remains non-proof. |

---

## 6. Review Independence

Review is independent only when:

- the reviewer can name the executor output being reviewed;
- assumptions from the executor are visible and not inherited as verified fact;
- the reviewer has access to source, evidence, or governance sufficient to challenge the output;
- disagreement is allowed and reportable;
- review does not rely only on the executor's summary;
- review findings remain separate from validation and HITL approval.

Review is **not independent** when it:

- rewrites the executor's claim without checking source or evidence;
- treats "the previous agent said so" as authority;
- validates implementation because it looks complete;
- suppresses contradictions to preserve workflow flow;
- frames missing evidence as a low-risk detail without proof boundary.

---

## 7. Validator Integrity

Validation stays trustworthy when:

- evidence level is named and scoped;
- validation does not reuse executor claims as proof;
- unknowns remain unknown after handoff;
- PASS/PARTIAL/FAIL does not exceed evidence;
- contradiction or missing evidence can block freeze;
- validator findings are allowed to reduce confidence.

Validation is contaminated when:

- the validator inherits executor assumptions silently;
- the validator checks only the report narrative, not evidence;
- the validator treats chain agreement as proof;
- the validator is asked to confirm a desired outcome rather than evaluate scope;
- validation cannot explain what it directly verified.

---

## 8. Contradiction Handling

Contradictions must survive handoff until resolved.

| Contradiction type | Required handling |
|--------------------|-------------------|
| Source vs source | Name conflicting artifacts; apply explicit priority or HITL. |
| Source vs implementation | Record implementation drift; executor fixes or escalates. |
| Reviewer vs executor | Preserve disagreement; validator or HITL may arbitrate depending on evidence and authority. |
| Validator vs reviewer | Preserve evidence boundary; QA Confidence governs proof language. |
| Governance vs prompt | Human Escalation determines whether prompt includes valid override authority. |
| HITL vs governance | Record human decision, waiver, or project-specific override; preserve residual risk. |

Contradiction resolution cannot be inferred from the number of agents agreeing after the contradiction was dropped.

---

## 9. Ownership Clarity

Ownership is clear when a future operator can answer:

- who changed the artifact;
- who reviewed it independently;
- who validated the evidence;
- who owns unresolved ambiguity;
- who owns contradiction resolution;
- who approved or waived risk;
- who can reopen the scope;
- what remains SAFE UNKNOWN.

Ownership is unclear when the record says "we", "the agents", "the chain", or "consensus" without naming role responsibility.

---

## 10. Escalation Survivability

An escalation survives coordination when:

- the trigger remains visible after summaries and handoffs;
- the owner is named;
- the unresolved decision is described;
- the evidence and missing evidence are named;
- the authority needed to resolve it is named;
- downstream work does not treat the unresolved item as approved;
- final REPORT states whether the escalation is open, resolved, deferred, waived, or blocking.

---

## 11. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Required action |
|-----------|-----------------|
| Role is known but authority is not | Keep role separate from authority; route via human escalation. |
| Authority exists but owner is not named | Name source/governance/operator/HITL owner or block the claim. |
| Reviewer independence is partial | Disclose partial review; do not use it as independent validation. |
| Validation evidence is inherited | Reclassify evidence as inferred/assumed or rerun independent validation. |
| Escalation route is unclear | Assign escalation owner before PASS, freeze, or delivery readiness. |

---

## 12. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial responsibility boundary model for executor, reviewer, validator, orchestrator, escalation authority, HITL authority, ownership traceability, contradiction handling, and escalation survivability; documentation only. |
