# MARS Website Factory — Human Escalation & Decision Boundary Governance

**Status:** **documented** — Website Factory HITL governance and human-supervised decision-boundary methodology only.  
**Not:** autonomous governance AI, runtime approval engine, universal escalation law, self-governing autonomy, or replacement for human project authority.

**Core principle:** AI frontend systems must know **when to stop, when to escalate, and when human authority is required**.

**Companion documents:** [decision-boundary-model.md](decision-boundary-model.md), [escalation-drift-taxonomy.md](escalation-drift-taxonomy.md).  
**Related layers:** [adaptive-governance.md](adaptive-governance.md), [decision-transparency-governance.md](decision-transparency-governance.md), [trust-calibration-governance.md](trust-calibration-governance.md), [knowledge-provenance-governance.md](knowledge-provenance-governance.md), [context-survivability-governance.md](context-survivability-governance.md), [failure-recovery-governance.md](failure-recovery-governance.md), [governance-minimalism.md](governance-minimalism.md), [governance-prioritization.md](governance-prioritization.md), [source-interpretation-governance.md](source-interpretation-governance.md), [qa-confidence-governance.md](qa-confidence-governance.md), [implementation-reliability-governance.md](implementation-reliability-governance.md), [multi-agent-coordination-governance.md](multi-agent-coordination-governance.md), [operational-workflow-governance.md](operational-workflow-governance.md), [visual-reconciliation-layer.md](visual-reconciliation-layer.md), [safe-unknown-boundary.md](safe-unknown-boundary.md).  
**Forge checklist:** [`../../agents/mars-forge/human-escalation-checklist.md`](../../agents/mars-forge/human-escalation-checklist.md).

---

## 1. Positioning

Human Escalation & Decision Boundary Governance formalizes the authority layer above SAFE UNKNOWN, source interpretation, visual reconciliation, implementation reliability, and QA confidence.

| This layer governs | This layer does not govern |
|--------------------|----------------------------|
| Escalation honesty, authority clarity, stop conditions, contradiction transparency, and bounded autonomy | A runtime approval service, policy engine, ticket workflow, or autonomous decision system |
| Human-visible checkpoints for ambiguous, contradictory, high-impact, or authority-sensitive frontend decisions | Universal product governance across all domains |
| Drift vocabulary for AI overreach, silent continuation, fake autonomy, escalation hesitation, and hidden HITL dependency | Redesigning Triumph or any other project |
| Reporting discipline for `HUMAN ESCALATION FINDINGS` | Automatic enforcement or certification |

SAFE UNKNOWN is necessary but not sufficient. A system can honestly say "unknown" and still drift if it continues through an unresolved decision, hides the need for human approval, or lets implementation momentum substitute for authority.

---

## 2. Canonical Definition

**Human escalation governance** is the discipline of making unresolved decision boundaries visible before AI-assisted frontend work crosses them.

It preserves:

- **Escalation honesty** — the system states when it cannot decide safely.
- **Authority clarity** — human-owned decisions remain human-owned.
- **Safe uncertainty handling** — ambiguity is not hidden inside implementation.
- **Human decision visibility** — approvals, waivers, overrides, and unresolved questions are reportable.
- **Bounded autonomy** — AI may act only inside the authority granted by source, project pack, prompt, and prior human decisions.
- **Contradiction transparency** — conflicting sources or instructions are surfaced instead of silently reconciled by taste.

The issue is not that AI can never proceed under uncertainty. The issue is that uncertainty, assumptions, contradiction, and authority boundaries must be classified before continuation.

---

## 3. Required Vocabulary

| Concept | Meaning |
|---------|---------|
| **Escalation boundary** | The point where available source, prompt scope, or governance no longer authorizes autonomous continuation. |
| **HITL authority** | Human-in-the-loop ownership over decisions that affect meaning, scope, approval, release, contradiction resolution, or project-specific tradeoffs. |
| **Bounded autonomy** | Permission for AI-assisted work to continue only within explicit source authority, approved assumptions, and scoped implementation responsibility. |
| **Escalation honesty** | Transparent declaration that a decision needs human review, cannot be proven, or should not be silently made by AI. |
| **Authority integrity** | Human approval, project pack authority, source priority, and governance boundaries are not replaced by confidence, momentum, or convenience. |
| **Decision ownership** | The named owner of a decision: source artifact, governance rule, operator instruction, project pack, or human approval. |
| **Unresolved ambiguity** | A material ambiguity with no sufficient source, rule, or approved assumption to resolve it. |
| **Contradiction escalation** | The act of stopping or raising conflict when approved-looking sources, prompts, packs, or requirements disagree. |
| **Assumption accumulation** | Multiple small assumptions stacking until the combined decision exceeds safe autonomy. |
| **Escalation survivability** | A future operator can understand what was escalated, why, what evidence existed, and what decision is still needed. |
| **Unsafe continuation** | Continuing implementation when ambiguity, contradiction, missing authority, or risk requires stop or HITL. |
| **Escalation contamination** | Prior guesses, stale approvals, archive sources, or implementation momentum influencing the escalation decision. |
| **Silent drift continuation** | Work proceeds through unresolved issues without explicit findings, stop note, or human checkpoint. |
| **Human approval boundary** | The edge beyond which only a human decision, waiver, or project authority can authorize continuation. |
| **Implementation stop condition** | A condition where implementation should pause instead of producing code, QA PASS, freeze, or delivery claims. |

---

## 4. Required Principles

- **Unresolved ambiguity may require stopping.**
- **Contradictions must surface visibly.**
- **Human authority must stay explicit.**
- **Escalation should be traceable.**
- **Assumption chains increase risk.**
- **Implementation momentum is dangerous.**
- **AI confidence must not replace authority.**
- **Stop conditions are healthy.**
- **SAFE UNKNOWN must be paired with action:** continue with disclosure, request HITL, stop, or block by contradiction.
- **Approval cannot be implied** from silence, prior visual similarity, build success, or a confident implementation narrative.

---

## 5. Stop Conditions

Stop or escalate before implementation, freeze, PASS, or delivery claim when:

| Stop condition | Why continuation is unsafe |
|----------------|----------------------------|
| Approved-looking sources conflict | AI cannot choose the authority chain by taste. |
| Source is missing for material meaning, layout, interaction, state, responsive behavior, asset, or copy | SAFE UNKNOWN alone does not authorize invention. |
| The prompt asks for a change that contradicts project pack, governance, or active source without override | Human authority must resolve the override. |
| Multiple assumptions are required to complete a section | Assumption accumulation can become hidden redesign. |
| A decision changes conversion meaning, CTA role, trust claims, service entities, pricing, legal/compliance language, or project scope | Business authority is required. |
| Implementation requires structural regrouping, design reinterpretation, or source priority change | This crosses from execution into decision ownership. |
| QA evidence cannot support requested confidence | PASS/freeze must not exceed verification boundary. |
| A waiver, approval, or human decision is referenced but not present | Fake approval is forbidden. |

---

## 6. Bounded Continuation

Autonomous continuation is allowed only when:

- the decision is reversible, local, and low-impact;
- source or governance clearly authorizes the choice;
- no contradiction is present;
- assumptions are few, explicit, and reported when material;
- the REPORT can name the proof boundary;
- continuation does not create fake approval, hidden redesign, or delivery confidence.

When the decision is useful but not fully proven, use **autonomous-with-disclosure** from [decision-boundary-model.md](decision-boundary-model.md), not silent continuation.

---

## 7. Anti-Patterns

Forbidden drift:

| Anti-pattern | Why it is forbidden |
|--------------|---------------------|
| **Continuing through ambiguity** | Hides unresolved decisions inside implementation. |
| **Silent redesign assumptions** | Turns missing authority into creative direction. |
| **Hidden decision substitution** | AI makes a human-owned choice without naming it. |
| **Pretending approval exists** | Converts absent HITL into fake authority. |
| **Escalation suppression** | Avoids reporting risk to keep progress moving. |
| **"Probably intended" continuation** | Treats plausibility as source authority. |
| **Fake autonomous authority** | Claims the system can decide what only humans can approve. |
| **Contradiction minimization** | Reframes conflict as harmless instead of surfacing it. |
| **Assumption stacking** | Many small guesses become one large unapproved design decision. |
| **Implementation inertia** | Work continues because code is already moving, not because authority is clear. |

---

## 8. Forge Integration

When Forge is selected, human escalation governance becomes a pre-freeze and reporting concern:

- Run [`human-escalation-checklist.md`](../../agents/mars-forge/human-escalation-checklist.md) before declaring section PASS, freeze, or delivery readiness when ambiguity, contradiction, approval, override, or assumption risk is present.
- Record **HUMAN ESCALATION FINDINGS** for escalation-boundary QA, stop-condition QA, contradiction escalation QA, HITL visibility QA, assumption-threshold QA, and authority-integrity QA.
- Use [decision-boundary-model.md](decision-boundary-model.md) to classify the decision level.
- Use [escalation-drift-taxonomy.md](escalation-drift-taxonomy.md) to name drift patterns.
- Keep findings separate from **SOURCE INTERPRETATION FINDINGS**, **IMPLEMENTATION RELIABILITY FINDINGS**, and **QA CONFIDENCE FINDINGS**, then summarize whether the work is safe to continue, HITL-recommended, HITL-required, or blocked.
- Use [multi-agent-coordination-governance.md](multi-agent-coordination-governance.md) when escalation ownership, role authority, reviewer independence, validator integrity, or fake consensus affects responsibility clarity.
- Use [knowledge-provenance-governance.md](knowledge-provenance-governance.md) when escalation depends on unknown origin, stale lineage, source-authority collapse, provenance gaps, or undocumented transformation.
- Use [operational-workflow-governance.md](operational-workflow-governance.md) when escalation is triggered by missing checkpoints, context-loss execution, unsafe parallel modification, freeze omission, or unstable handoff.
- Use [context-survivability-governance.md](context-survivability-governance.md) when escalation is triggered by compression loss, checkpoint amnesia, freeze-memory loss, summary contamination, reconstruction ambiguity, or missing escalation memory.
- Use [failure-recovery-governance.md](failure-recovery-governance.md) when escalation is triggered by missing trusted state, rollback ambiguity, contradictory checkpoints, broken freeze recovery, degraded-state risk, panic-fix contamination, or failed continuity restoration.
- Use [governance-minimalism.md](governance-minimalism.md) when escalation-only logic can replace universal heavy process, or when mandatory depth risks governance paralysis; report `GOVERNANCE MINIMALISM FINDINGS` separately.
- Use [governance-prioritization.md](governance-prioritization.md) when escalation requests need relevance weighting, severity proportionality, or protection from escalation fatigue; report `RISK WEIGHTING FINDINGS` separately.
- Use [adaptive-governance.md](adaptive-governance.md) when escalation depth must scale by context, authority, consequence, reversibility, or uncertainty; report `ADAPTIVE GOVERNANCE FINDINGS` separately.
- Use [decision-transparency-governance.md](decision-transparency-governance.md) when escalation, non-escalation, STOP, waiver, or continuation decisions need visible rationale; report `REASONING VISIBILITY FINDINGS` separately.
- Use [trust-calibration-governance.md](trust-calibration-governance.md) when escalation confidence affects operator trust, authority credibility, false trust escalation, or trust-preserving continuation; report `TRUST CALIBRATION FINDINGS` separately.

This is human-supervised methodology. It does not create approval automation, runtime gates, or self-governing autonomy.

---

## 9. Triumph V2 Lessons Captured

Triumph V2 exposed reusable Website Factory escalation lessons:

- Visual source ambiguity can be reported as SAFE UNKNOWN, but material grouping or priority choices may still need a human decision before DOM or copy changes.
- Missing mobile source can allow responsive survivability work, but not confident responsive intent claims without disclosure or HITL.
- A contradiction between active screenshots, semantic matrices, implementation notes, and legacy PDFs must be surfaced, not resolved from momentum.
- Assumption chains around equipment, pricing, fleet entities, CTA meaning, or section order can cross from implementation into business authority.
- A section can be stable, visually close, and buildable while still requiring escalation because decision ownership is unclear.
- Human decision checkpoints protect delivery confidence; they are not a failure of the frontend workflow.

These are Website Factory governance lessons, not Triumph-specific redesign instructions.

---

## 10. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Required action |
|-----------|-----------------|
| Unknown is low-impact and reversible | Continue only with disclosure and proof boundary. |
| Unknown affects meaning, hierarchy, interaction, responsive intent, state, accessibility, asset authority, or freeze | Classify via [decision-boundary-model.md](decision-boundary-model.md); HITL may be recommended or required. |
| Unknown combines with other assumptions | Treat as assumption accumulation; escalate if threshold is crossed. |
| Unknown hides a source contradiction | Block by contradiction until human or source priority resolves it. |
| Unknown involves approval, waiver, delivery, or release readiness | HITL required; AI cannot approve itself. |

**Action:** state what is unknown, why AI cannot safely decide, what would resolve it, and whether the current boundary is autonomous-safe, autonomous-with-disclosure, HITL-recommended, HITL-required, blocked-by-ambiguity, or blocked-by-contradiction.

---

## 11. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Human Escalation & Decision Boundary Governance layer — escalation honesty, bounded autonomy, HITL authority, stop conditions, drift taxonomy, and Forge `HUMAN ESCALATION FINDINGS`; documentation only. |
| v0.1 | 2026-05-17 | Linked Multi-Agent Coordination & Responsibility Governance for escalation ownership, role authority, reviewer independence, validator integrity, and fake-consensus risk. |
| v0.2 | 2026-05-17 | Linked Knowledge Provenance & Source Lineage Governance for provenance gaps, stale lineage, unknown-origin source, and authority-chain escalation. |
| v0.3 | 2026-05-17 | Linked Operational Workflow & Execution Discipline Governance for workflow escalation, missing checkpoints, context-loss execution, unsafe parallel modification, freeze omission, and unstable handoff. |
| v0.4 | 2026-05-17 | Linked Knowledge Compression & Context Survivability Governance for compression loss, checkpoint amnesia, freeze-memory loss, summary contamination, reconstruction ambiguity, and escalation-memory loss. |
| v0.5 | 2026-05-17 | Linked Failure Recovery & Operational Resilience Governance for missing trusted state, rollback ambiguity, contradictory checkpoints, degraded-state risk, panic-fix contamination, and failed continuity restoration. |
| v0.6 | 2026-05-17 | Linked Governance Minimalism & Complexity Control for escalation-only logic, governance paralysis prevention, and proportional HITL depth. |
| v0.7 | 2026-05-17 | Linked Governance Prioritization & Risk Weighting for escalation relevance, severity proportionality, and escalation fatigue prevention. |
| v0.8 | 2026-05-17 | Linked Decision Transparency & Reasoning Visibility Governance for escalation explainability, visible stop-condition rationale, assumption disclosure, and traceable continuation decisions. |
| v0.9 | 2026-05-17 | Linked Adaptive Governance & Context-Sensitive Discipline for context-aware escalation depth, proportional HITL use, and authority-sensitive process scaling. |
