# MARS Website Factory - Reasoning Visibility Model

**Status:** **documented** - Website Factory reasoning-visibility model and human-supervised review methodology only.  
**Not:** hidden chain-of-thought exposure, autonomous reasoning engine, scoring model, formal proof system, or universal explainability law.

**Parent governance:** [decision-transparency-governance.md](decision-transparency-governance.md).  
**Companion taxonomy:** [reasoning-drift-taxonomy.md](reasoning-drift-taxonomy.md).  
**Forge checklist:** [`../../agents/mars-forge/reasoning-visibility-checklist.md`](../../agents/mars-forge/reasoning-visibility-checklist.md).

---

## 1. Purpose

The Reasoning Visibility Model defines the review layers that should remain visible when Website Factory governance produces findings, recommendations, escalations, prioritization, or conclusions.

It does not require private deliberation. It requires a **reviewable rationale** that lets humans inspect:

- what evidence was used;
- how evidence was interpreted;
- what priority was assigned and why;
- why escalation was or was not triggered;
- what conclusion was reached;
- what uncertainty remains;
- how the decision can be reconstructed later.

---

## 2. Canonical Layers

| Layer | What must remain visible | Drift if hidden |
|-------|--------------------------|-----------------|
| **Evidence layer** | Source artifacts, QA observations, commands, screenshots, implementation files, human decisions, or missing evidence that support the claim. | Unverifiable recommendation, evidence collapse, fake certainty. |
| **Interpretation layer** | Whether the evidence is observed, inferred, assumed, contradictory, partial, stale, or unknown. | Hidden assumptions, inferred certainty inflation, source ambiguity. |
| **Prioritization layer** | Why a finding is critical, operational, strategic, continuity, cosmetic, escalation-only, or informational. | Invisible prioritization logic, equal-priority overload, critical-risk dilution. |
| **Escalation layer** | Why the decision is autonomous-safe, autonomous-with-disclosure, HITL-recommended, HITL-required, blocked, or STOP. | Opaque escalation, hidden HITL dependency, silent continuation. |
| **Conclusion layer** | The resulting recommendation, disposition, PASS/PARTIAL/FAIL/SAFE UNKNOWN, action, deferral, or freeze posture. | Conclusion-without-traceability, reasoning collapse into verdicts. |
| **Uncertainty layer** | What remains unknown, what assumptions remain, what would resolve the uncertainty, and whether it affects action. | Fake certainty through summarization, confidence opacity. |
| **Traceability layer** | The links between evidence, interpretation, priority, escalation, conclusion, unknowns, and future review. | Decision ambiguity, traceability erosion, governance black-boxing. |

---

## 3. Layer Requirements

### 3.1 Evidence Layer

The evidence layer should name the basis for material claims:

- source artifact, implementation pack, project note, screenshot, file, command, preview, QA observation, or human decision;
- direct, rendered, source-level, build-level, inferred, assumed, or unknown evidence level;
- missing evidence when a claim cannot be supported.

**Rule:** no strong conclusion should appear without a visible evidence layer.

### 3.2 Interpretation Layer

The interpretation layer should explain how the evidence is being read:

- observed vs inferred vs assumed vs unknown;
- contradiction, ambiguity, stale lineage, or source-priority issue;
- transformation from source into implementation, QA, or recommendation.

**Rule:** interpretation should not masquerade as fact.

### 3.3 Prioritization Layer

The prioritization layer should explain why some findings matter more:

- operational consequence;
- severity and reversibility;
- strategic, continuity, source-authority, QA confidence, or escalation impact;
- whether action is stop, fix before freeze, disclose, defer, monitor, or record only.

**Rule:** priority order should be reviewable, not implied by report placement.

### 3.4 Escalation Layer

The escalation layer should explain:

- trigger: ambiguity, contradiction, approval boundary, assumption chain, evidence gap, source priority, or stop condition;
- decision owner: source, governance, operator, HITL, or unknown;
- boundary level: autonomous-safe, autonomous-with-disclosure, HITL-recommended, HITL-required, blocked-by-ambiguity, blocked-by-contradiction, or STOP.

**Rule:** escalation requires a rationale; non-escalation can also require a rationale when consequence is high.

### 3.5 Conclusion Layer

The conclusion layer should be readable as a scoped outcome:

- recommendation or finding;
- disposition;
- proof boundary;
- next action;
- deferrals or unresolved items.

**Rule:** conclusions should not be broader than their evidence, interpretation, priority, and uncertainty layers.

### 3.6 Uncertainty Layer

The uncertainty layer should state:

- what is unknown;
- why it matters;
- whether it affects freeze, delivery, trust, source authority, accessibility, visual intent, strategic intent, or HITL;
- what would resolve it.

**Rule:** uncertainty should not be compressed into vague "risk" language.

### 3.7 Traceability Layer

The traceability layer ties the model together:

- evidence -> interpretation -> priority -> escalation -> conclusion -> unknowns -> action;
- links to companion governance findings when relevant;
- enough context for future review after handoff or compression.

**Rule:** a future operator should be able to reconstruct the conclusion without private memory.

---

## 4. Reasoning Traceability

Reasoning traceability is sufficient when a reviewer can answer:

- What evidence supported the conclusion?
- What was interpreted, inferred, assumed, or unknown?
- Why was this issue prioritized this way?
- Why was escalation chosen, avoided, or deferred?
- What tradeoff was accepted?
- What confidence boundary limits the conclusion?
- What would change the conclusion?

If those questions cannot be answered from the report or artifacts, record **REASONING VISIBILITY FINDINGS** or **SAFE UNKNOWN**.

---

## 5. Transparency Proportionality

Not every observation needs the same explanation depth.

| Decision type | Expected transparency |
|---------------|-----------------------|
| Low-risk cosmetic observation | Short evidence and disposition may be enough. |
| Reversible scoped implementation detail | Evidence, assumption disclosure, and proof boundary. |
| QA PASS/PARTIAL/FAIL or freeze claim | Evidence level, uncertainty, proof boundary, conclusion traceability. |
| Prioritization across many findings | Priority rationale, consequence, action order, signal-to-noise handling. |
| HITL, STOP, contradiction, waiver, approval, source-priority decision | Full evidence, interpretation, escalation rationale, uncertainty, decision owner, and next action. |

**Rule:** transparency depth increases with consequence, uncertainty, irreversibility, escalation relevance, and authority sensitivity.

---

## 6. Conclusion Reconstruction

A conclusion is reconstructable when it can be restated as:

```text
Because <evidence> was interpreted as <observed/inferred/assumed/unknown>,
and because <priority / consequence>,
the decision is <disposition / recommendation>,
with <uncertainty / proof boundary>,
requiring <next action / escalation / deferral>.
```

This format is optional, but the content should remain readable in normal REPORT prose.

---

## 7. SAFE UNKNOWN

Record **SAFE UNKNOWN** when any required layer is missing and material:

- evidence layer missing;
- interpretation unclear;
- prioritization unsupported;
- escalation unexplained;
- conclusion too broad;
- uncertainty hidden;
- traceability broken;
- future operator cannot reconstruct the decision.

**Action:** identify the missing layer, name what would restore it, and classify continuation as safe with disclosure, verify further, HITL recommended, HITL required, blocked, or STOP.

---

## 8. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Reasoning Visibility Model - evidence, interpretation, prioritization, escalation, conclusion, uncertainty, and traceability layers; documentation only. |
