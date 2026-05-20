# MARS Website Factory — Decision Boundary Model

**Status:** **documented** — Website Factory decision-boundary vocabulary and human-supervised escalation methodology only.  
**Not:** runtime approval engine, autonomous policy system, universal legal/governance model, or automated gatekeeper.

**Parent layer:** [human-escalation-governance.md](human-escalation-governance.md).  
**Companion taxonomy:** [escalation-drift-taxonomy.md](escalation-drift-taxonomy.md).  
**Forge checklist:** [`../../agents/mars-forge/human-escalation-checklist.md`](../../agents/mars-forge/human-escalation-checklist.md).

---

## 1. Purpose

The Decision Boundary Model gives Website Factory operators and Forge-style frontend work a shared vocabulary for deciding whether AI-assisted work may continue, continue with disclosure, recommend HITL, require HITL, or stop.

It answers:

- Is this decision inside bounded autonomy?
- Is disclosure enough?
- Does a human need to decide?
- Is ambiguity or contradiction blocking implementation?
- What must be recorded so a future operator can understand the boundary?

---

## 2. Boundary Levels

| Level | Meaning | Allowed action |
|-------|---------|----------------|
| **autonomous-safe** | Source, governance, prompt scope, and implementation ownership clearly authorize the decision. | Continue normally; report only if material. |
| **autonomous-with-disclosure** | A low-risk assumption or inference is needed, but it is reversible, scoped, and does not affect human-owned meaning or approval. | Continue with explicit disclosure, confidence boundary, and rollback note if needed. |
| **HITL-recommended** | A human decision would materially improve confidence, but scoped continuation can proceed if risk is disclosed and no contradiction or approval boundary is crossed. | Continue only if risk is acceptable and clearly reported; request human decision when practical. |
| **HITL-required** | Decision affects meaning, authority, approval, waiver, release, business claims, source priority, structural regrouping, or project-specific tradeoff. | Stop at the decision boundary until human approval, waiver, or instruction exists. |
| **blocked-by-ambiguity** | Material ambiguity prevents safe implementation and cannot be resolved by source, governance, or bounded assumption. | Stop; record unknown, resolver needed, and impact. |
| **blocked-by-contradiction** | Approved-looking sources, instructions, or governance conflict with no priority rule. | Stop; surface contradiction and require human/source-priority resolution. |

---

## 3. Stop Conditions

Stop before implementation, PASS, freeze, or delivery readiness when any condition applies:

- A contradiction affects source authority, content, hierarchy, CTA role, responsive intent, interaction behavior, state behavior, accessibility semantics, or implementation ownership.
- A material source is missing and the decision cannot remain local, reversible, or low-impact.
- The work would create, remove, regroup, rename, or reprioritize meaning without explicit authority.
- The decision depends on more than two material assumptions or one high-impact assumption.
- The report would need to imply human approval, waiver, release readiness, or business acceptance that is not present.
- The requested confidence exceeds evidence boundaries from [qa-confidence-governance.md](qa-confidence-governance.md).
- The implementation would rely on hidden overrides, unclear source priority, or fragile coupling that requires structural authority.

Stop conditions are healthy. They protect human authority and prevent fake autonomy.

---

## 4. Escalation Triggers

| Trigger | Typical boundary |
|---------|------------------|
| Missing active source path or version charter | HITL-required or blocked-by-ambiguity |
| Conflicting screenshots, matrices, project notes, or prompt instructions | blocked-by-contradiction |
| Missing mobile source for a high-impact responsive decision | HITL-recommended or HITL-required |
| Unknown hover/focus/form/modal/carousel behavior | autonomous-with-disclosure for inert styling; HITL-required for functional behavior |
| Copy, pricing, legal, trust proof, service entity, or CTA meaning change | HITL-required |
| Structural regrouping of visual clusters or DOM ownership | HITL-required |
| Assumption chain across source, layout, copy, responsive, and QA | HITL-required or blocked-by-ambiguity |
| Build/test unavailable but report asks for PASS | autonomous-with-disclosure for source-only claim; blocked for broad PASS |
| Waiver, approval, freeze, or delivery acceptance is absent | HITL-required |

---

## 5. Contradiction Handling

Contradictions must be surfaced visibly:

1. Name the conflicting sources or instructions.
2. State the decision affected.
3. Check whether a current priority rule resolves the conflict.
4. If no priority rule exists, classify as **blocked-by-contradiction**.
5. Do not choose by aesthetic taste, implementation convenience, or prior-session memory.
6. Record the needed human decision, source priority update, or project pack correction.

**Rule:** contradiction minimization is drift. A small contradiction can become large when it defines source authority.

---

## 6. Assumption Thresholds

Assumptions become unsafe when they accumulate.

| Assumption condition | Boundary guidance |
|----------------------|-------------------|
| One low-impact implementation assumption | autonomous-with-disclosure |
| One reversible visual or spacing approximation with clear source direction | autonomous-with-disclosure |
| Multiple assumptions inside one section, but no meaning or authority change | HITL-recommended |
| Any assumption that changes meaning, CTA purpose, proof claim, service entity, approval, or source priority | HITL-required |
| Assumptions needed because sources contradict | blocked-by-contradiction |
| Assumptions needed because required source is absent | blocked-by-ambiguity or HITL-required |

Assumption chains should be treated as risk multipliers, not isolated harmless guesses.

---

## 7. Escalation Traceability

Every escalation finding should preserve:

| Field | Purpose |
|-------|---------|
| **scope** | Page, section, `block_id`, files, viewport, state, or artifact. |
| **boundary level** | One of the six model levels. |
| **trigger** | Ambiguity, contradiction, approval, assumption chain, evidence gap, source priority, or stop condition. |
| **evidence** | Source paths, prompt text, implementation pack note, QA evidence, or missing evidence. |
| **decision owner** | Human operator, project owner, source artifact, governance rule, or unknown. |
| **allowed action** | Continue, continue with disclosure, request HITL, stop, or block. |
| **resolver needed** | Approval, source priority, annotated mockup, content decision, waiver, implementation-pack update, or QA evidence. |

Traceability keeps escalation survivable across sessions.

---

## 8. Human Override Authority

Humans may override an escalation boundary, but the override must be explicit enough to preserve authority integrity.

Acceptable human override records:

- `HITL APPROVED — continue with desktop source only; mobile intent remains PARTIAL.`
- `HITL WAIVER — pricing copy deferred; do not invent equipment prices.`
- `HITL DECISION — design/v2/03.png overrides legacy PDF for section order.`
- `HITL SCOPE CHANGE — implement visual structure only; interactions out of scope.`

Forbidden override claims:

- `Approved` with no source or human note.
- `Assumed approved because no objection.`
- `Proceeding because likely intended.`
- `PASS after human review` when no review is recorded.

Human override does not erase uncertainty; it names who owns the risk.

---

## 9. Reporting Vocabulary

Use this concise form inside `HUMAN ESCALATION FINDINGS`:

```text
HUMAN ESCALATION FINDINGS — <scope>

Boundary level: autonomous-safe | autonomous-with-disclosure | HITL-recommended | HITL-required | blocked-by-ambiguity | blocked-by-contradiction
Trigger: <ambiguity / contradiction / approval / assumption chain / evidence gap / source priority / stop condition>
Decision owner: <source / governance / operator / HITL / unknown>
Evidence: <paths, notes, QA evidence, or missing evidence>
Disposition: continue | continue with disclosure | HITL requested | stopped | blocked
Resolver needed: <specific human/source/QA action>
```

---

## 10. SAFE UNKNOWN

SAFE UNKNOWN answers what is not known. The decision boundary answers what to do next.

| SAFE UNKNOWN condition | Boundary decision |
|------------------------|-------------------|
| Unknown is low-impact and reversible | autonomous-with-disclosure |
| Unknown blocks source-faithful implementation | blocked-by-ambiguity |
| Unknown hides a contradiction | blocked-by-contradiction |
| Unknown affects human-owned business or approval decision | HITL-required |
| Unknown affects QA confidence only | qualify PASS/PARTIAL/FAIL per QA confidence governance |

**Rule:** SAFE UNKNOWN without a boundary decision can still permit drift.

---

## 11. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial decision boundary levels, stop conditions, escalation triggers, contradiction handling, assumption thresholds, traceability, and human override authority. |
