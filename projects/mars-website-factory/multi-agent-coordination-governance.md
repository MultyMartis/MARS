# MARS Website Factory - Multi-Agent Coordination & Responsibility Governance

**Status:** **documented** - Website Factory multi-agent coordination governance and human-supervised responsibility methodology only.  
**Not:** autonomous agent governance AI, runtime orchestration engine, universal multi-agent law, self-governing agent swarm, or replacement for human project authority.

**Core principle:** multiple frontend AI systems must preserve **responsibility clarity, authority boundaries, role separation, escalation ownership, coordination survivability, and reviewer independence**.

**Companion documents:** [agent-responsibility-boundary-model.md](agent-responsibility-boundary-model.md), [multi-agent-drift-taxonomy.md](multi-agent-drift-taxonomy.md).  
**Related layers:** [knowledge-provenance-governance.md](knowledge-provenance-governance.md), [human-escalation-governance.md](human-escalation-governance.md), [qa-confidence-governance.md](qa-confidence-governance.md), [implementation-reliability-governance.md](implementation-reliability-governance.md), [source-interpretation-governance.md](source-interpretation-governance.md), [visual-reconciliation-layer.md](visual-reconciliation-layer.md), [operational-workflow-governance.md](operational-workflow-governance.md), [safe-unknown-boundary.md](safe-unknown-boundary.md).  
**Forge checklist:** [`../../agents/mars-forge/multi-agent-coordination-checklist.md`](../../agents/mars-forge/multi-agent-coordination-checklist.md).

---

## 1. Positioning

Multi-Agent Coordination & Responsibility Governance formalizes how several AI-assisted roles can participate in Website Factory frontend work without collapsing responsibility, authority, or review independence.

| This layer governs | This layer does not govern |
|--------------------|----------------------------|
| Role separation, responsibility clarity, authority boundaries, escalation ownership, reviewer independence, contradiction survivability, and handoff traceability | Runtime orchestration, scheduling, queues, autonomous swarms, or self-governing agents |
| Human-supervised coordination methodology for executor, reviewer, validator, orchestrator, escalation authority, and HITL authority roles | Universal multi-agent law across all domains |
| Drift vocabulary for reviewer/executor collapse, validator contamination, assumption propagation, fake consensus, and responsibility diffusion | Claims that multiple agreeing agents equal truth |
| Forge reporting discipline for `MULTI-AGENT FINDINGS` | Automatic enforcement, consensus scoring, or certification |

The issue is not whether multiple agents can produce more output. The issue is whether a future operator can still tell **who owned execution, who reviewed independently, who validated evidence, who escalated, what contradicted the chain, and what remains unresolved**.

---

## 2. Canonical Definition

**Multi-agent coordination governance** is the discipline of preserving explicit role, responsibility, authority, and escalation boundaries when multiple AI-assisted systems contribute to frontend production or QA.

It preserves:

- **Responsibility clarity** - each material decision or output has an owner.
- **Decision traceability** - handoffs expose what was decided, assumed, escalated, deferred, or contradicted.
- **Authority integrity** - no agent inherits authority just because it is later in the chain.
- **Escalation visibility** - unresolved ambiguity and HITL ownership survive handoffs.
- **Contradiction survivability** - conflicts are not normalized away by chained summaries.
- **Reviewer independence** - review and validation do not silently inherit executor assumptions.
- **Execution-review separation** - building, reviewing, validating, and approving remain distinct responsibilities.

Multi-agent agreement is not proof. Several agents can share the same weak premise, stale source, hidden assumption, or fabricated confidence and still produce a coordinated-looking but false result.

---

## 3. Required Vocabulary

| Concept | Meaning |
|---------|---------|
| **Agent responsibility** | The named obligation of a role for a specific output, decision, check, or escalation. |
| **Authority boundary** | The edge of what a role may decide without source, governance, operator instruction, or HITL approval. |
| **Execution ownership** | Responsibility for implementing or changing artifacts inside a scoped lane. |
| **Reviewer independence** | A reviewer evaluates output without silently adopting the executor's assumptions, desired outcome, or proof claims. |
| **Validator integrity** | Validation remains evidence-based and does not become a second expression of the executor's narrative. |
| **Escalation ownership** | A visible owner for raising, preserving, and resolving ambiguity, contradiction, or HITL-required decisions. |
| **Orchestration clarity** | The coordination plan states roles, order, authority, handoffs, blockers, and stop conditions without implying runtime automation. |
| **Assumption propagation** | An assumption moves from one agent to another as if it were verified fact. |
| **Responsibility ambiguity** | It is unclear which role owns a decision, defect, unknown, waiver, or escalation. |
| **Multi-agent contamination** | One role's premise, bias, prior output, or hidden assumption distorts another role's independent work. |
| **Chain hallucination** | A false claim is strengthened as it passes through summaries, reviews, or validators. |
| **Coordination survivability** | A future operator can reconstruct role ownership, evidence, contradictions, and unresolved decisions after handoffs. |
| **Role integrity** | Executor, reviewer, validator, orchestrator, escalation authority, and HITL authority remain separable. |
| **Review independence** | Review findings are based on evidence and scope, not on the executor's confidence or the chain's desired completion. |
| **Execution-review separation** | The same role should not treat its own implementation narrative as independent validation. |
| **Fake consensus** | Multiple agreeing outputs create confidence theater without independent evidence or authority. |

---

## 4. Required Principles

- **Reviewers require independence.**
- **Validators should not inherit assumptions silently.**
- **Responsibility must stay visible.**
- **Escalation ownership matters.**
- **Contradictions must survive handoffs.**
- **Role boundaries reduce hallucination propagation.**
- **Coordination should remain explainable.**
- **Fake consensus is dangerous.**
- **Multiple agreeing agents do not equal truth.**
- **Agent chains can amplify assumptions, ambiguity, hallucinations, and fake confidence.**
- **Authority cannot be delegated by implication** through a chain, summary, or downstream continuation.
- **HITL authority remains human-owned** even when multiple AI roles recommend the same action.

---

## 5. Coordination Rules

When more than one AI-assisted role participates in a Website Factory frontend workflow:

| Rule | Required behavior |
|------|-------------------|
| **Name the role** | Each agent lane is labeled as executor, reviewer, validator, orchestrator, escalation authority, HITL authority, or other bounded role. |
| **Name the owner** | Material decisions, assumptions, deferrals, approvals, waivers, and unknowns have visible ownership. |
| **Separate evidence from agreement** | Consensus can support prioritization, but evidence and authority still determine truth. |
| **Preserve contradictions** | A contradiction found upstream remains visible until resolved by source priority, governance, operator decision, or HITL. |
| **Block silent inheritance** | Downstream agents must restate assumptions as assumptions unless direct evidence verifies them. |
| **Protect review independence** | Reviewer and validator findings must be able to disagree with executor output without being treated as workflow failure. |
| **Escalate orphaned responsibility** | If no role owns a decision or risk, the gap itself becomes a finding. |
| **Report coordination scope** | REPORT states which roles contributed and what each role did or did not verify. |

---

## 6. Anti-Patterns

Forbidden drift:

| Anti-pattern | Why it is forbidden |
|--------------|---------------------|
| **Agents validating themselves** | Collapses executor and reviewer responsibility. |
| **Silent assumption inheritance** | Turns unverified premises into apparent facts. |
| **Circular QA** | Validation cites outputs from the same chain instead of independent evidence. |
| **Fake multi-agent consensus** | Agreement is presented as truth without authority or proof. |
| **Invisible ownership** | Defects, decisions, assumptions, or escalations have no accountable owner. |
| **Orchestration without authority clarity** | Coordination order exists, but no one knows who can decide or stop. |
| **Review collapse** | Review becomes polishing the executor narrative rather than independent challenge. |
| **Duplicated escalation responsibility** | Several roles assume someone else owns escalation. |
| **Autonomous assumption propagation** | Agents continue each other's guesses because the chain is moving. |
| **Role confusion** | Executor, reviewer, validator, orchestrator, and HITL authority are blended into one confidence story. |

---

## 7. Forge Integration

When Forge is selected and multiple AI-assisted roles, sessions, reviewers, or validators affect the same frontend scope:

- Run [`multi-agent-coordination-checklist.md`](../../agents/mars-forge/multi-agent-coordination-checklist.md) before declaring PASS, freeze, delivery readiness, or HITL completion when responsibility, authority, review independence, validation integrity, orchestration clarity, or handoff survivability is material.
- Record **MULTI-AGENT FINDINGS** for responsibility-boundary QA, reviewer independence QA, escalation ownership QA, validator integrity QA, orchestration clarity QA, handoff survivability QA, contradiction survivability QA, and fake-consensus risk.
- Use [agent-responsibility-boundary-model.md](agent-responsibility-boundary-model.md) to classify roles, boundaries, and escalation routing.
- Use [multi-agent-drift-taxonomy.md](multi-agent-drift-taxonomy.md) to name drift patterns.
- Keep findings separate from **SOURCE INTERPRETATION FINDINGS**, **IMPLEMENTATION RELIABILITY FINDINGS**, **QA CONFIDENCE FINDINGS**, and **HUMAN ESCALATION FINDINGS**, then summarize whether coordination is explainable and safe to continue.
- Use [knowledge-provenance-governance.md](knowledge-provenance-governance.md) when handoffs risk source-lineage loss, summary contamination, inherited hallucination, unknown-origin evidence, or authority-chain collapse.
- Use [operational-workflow-governance.md](operational-workflow-governance.md) when multi-session or multi-agent work creates unsafe parallel modification, checkpoint erosion, report inconsistency, unstable handoff, or context-loss execution risk.

This is human-supervised coordination methodology. It does not create runtime orchestration, automated authority routing, or self-governing agent governance.

---

## 8. Triumph V2 Lessons Captured

Triumph V2 exposed reusable Website Factory multi-agent coordination lessons:

- A semantic rebuild can involve several AI-assisted passes, but responsibility still must name who executed, reviewed, validated, and escalated.
- Visual, semantic, responsive, QA confidence, and escalation findings can reinforce one another, but agreement between findings does not replace source evidence or HITL authority.
- A downstream reviewer can inherit source ambiguity, V1/V2 contamination, or implementation assumptions if handoffs do not preserve UNKNOWN and contradiction states.
- Multiple sessions can make duplicate ownership likely: one role fixes, another reviews, another reports, and nobody owns unresolved escalation.
- Reviewer independence matters most when prior output looks polished, because polished summaries can hide missing evidence or role collapse.
- Responsibility gaps around active source, mobile intent, equipment/pricing claims, CTA meaning, or freeze readiness must remain visible across handoffs.

These are Website Factory governance lessons, not Triumph redesign instructions.

---

## 9. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Required action |
|-----------|-----------------|
| Role ownership is unclear | Classify responsibility before continuation or report as orphaned responsibility. |
| Reviewer independence cannot be established | Treat review as non-independent and avoid using it as validation proof. |
| Validator evidence depends on executor assumptions | Reclassify validation as contaminated or partial until independent evidence exists. |
| Multiple agents agree but evidence is weak | Report fake-consensus risk; do not inflate confidence. |
| Escalation owner is missing | Stop or route through human escalation governance before freeze or delivery claim. |
| Contradiction was dropped during handoff | Restore the contradiction to findings and block or escalate until resolved. |
| Orchestration order exists but authority does not | Clarify authority boundaries or mark coordination unsafe. |

**Action:** state what is unknown, which role should own resolution, what evidence or decision would resolve it, and whether coordination is autonomous-safe, autonomous-with-disclosure, HITL-recommended, HITL-required, blocked-by-ambiguity, or blocked-by-contradiction.

---

## 10. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Multi-Agent Coordination & Responsibility Governance layer - role integrity, responsibility boundaries, reviewer independence, validator integrity, escalation ownership, drift taxonomy, and Forge `MULTI-AGENT FINDINGS`; documentation only. |
| v0.1 | 2026-05-17 | Linked Knowledge Provenance & Source Lineage Governance for handoff lineage survivability, summary contamination, inherited hallucination, and authority-chain preservation. |
| v0.2 | 2026-05-17 | Linked Operational Workflow & Execution Discipline Governance for unsafe parallel modification, checkpoint erosion, report consistency, unstable handoff, and context-loss execution risk. |
