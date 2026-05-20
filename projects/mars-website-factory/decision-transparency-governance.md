# MARS Website Factory - Decision Transparency & Reasoning Visibility Governance

**Status:** **documented** - Website Factory transparency governance and human-supervised reasoning-visibility methodology only.  
**Not:** chain-of-thought exposure, autonomous reasoning engine, universal transparency law, perfect explainability guarantee, or replacement for human project judgment.

**Core principle:** frontend governance decisions must preserve **explainability, visible reasoning, escalation clarity, prioritization traceability, and review readability**.  
It is not merely "produce findings," "make decisions," "report conclusions," or "state recommendations."

**Companion documents:** [reasoning-visibility-model.md](reasoning-visibility-model.md), [reasoning-drift-taxonomy.md](reasoning-drift-taxonomy.md).  
**Related layers:** [governance-prioritization.md](governance-prioritization.md), [cognitive-load-governance.md](cognitive-load-governance.md), [qa-confidence-governance.md](qa-confidence-governance.md), [trust-calibration-governance.md](trust-calibration-governance.md), [human-escalation-governance.md](human-escalation-governance.md), [knowledge-provenance-governance.md](knowledge-provenance-governance.md), [context-survivability-governance.md](context-survivability-governance.md), [visual-reconciliation-layer.md](visual-reconciliation-layer.md).  
**Forge checklist:** [`../../agents/mars-forge/reasoning-visibility-checklist.md`](../../agents/mars-forge/reasoning-visibility-checklist.md).

---

## 1. Positioning

Decision Transparency & Reasoning Visibility Governance formalizes how Website Factory governance keeps decisions reviewable after findings, recommendations, prioritization, escalation, and QA conclusions are produced.

| This layer governs | This layer does not govern |
|--------------------|----------------------------|
| Reasoning visibility, decision traceability, escalation explainability, prioritization transparency, conclusion readability, and review survivability | Exposing hidden chain-of-thought, private model internals, or unrestricted deliberation |
| Human-readable explanation of what evidence, assumptions, uncertainty, and tradeoffs shaped a governance conclusion | Autonomous reasoning engines, scoring systems, or universal explainability frameworks |
| Drift vocabulary for opaque reasoning, hidden assumptions, silent tradeoffs, invisible prioritization, unverifiable conclusions, and black-box governance | Claims that every decision can be perfectly explained |
| Forge reporting discipline for `REASONING VISIBILITY FINDINGS` | Redesigning Triumph or any other project |

A governance system may provide recommendations, generate convincing reports, output strong conclusions, and appear highly intelligent while still hiding assumptions, obscuring tradeoffs, weakening traceability, or making reasoning unverifiable.

The governance question is not "did the system reach a conclusion?"  
The governance question is: **can a future operator understand why that conclusion was reached, what evidence shaped it, what uncertainty remained, and what decision should happen next?**

---

## 2. Canonical Definition

**Decision transparency** is the discipline of making governance decisions traceable enough for human review, escalation, handoff, and later reconstruction.

**Reasoning visibility** is the human-readable exposure of the evidence, interpretation, assumptions, prioritization logic, uncertainty, and conclusion boundary that support a governance outcome.

This layer preserves:

- **Reasoning visibility** - the report shows the rationale in reviewable terms without exposing private chain-of-thought.
- **Decision traceability** - a conclusion can be traced to evidence, source authority, interpretation, prioritization, and escalation posture.
- **Escalation explainability** - HITL, STOP, waiver, or continuation decisions explain why escalation was or was not required.
- **Prioritization transparency** - high-risk items are visibly weighted above minor findings.
- **Conclusion readability** - recommendations are understandable, scoped, and reconstructable.
- **Reasoning continuity** - later sessions can understand the decision path without relying on memory.
- **Decision survivability** - decisions remain useful after compression, handoff, freeze, recovery, or review.

Reasoning visibility is not a demand for hidden chain-of-thought. It is a demand for **reviewable rationale**: evidence, assumptions, tradeoffs, priority logic, uncertainty, and conclusion boundaries.

---

## 3. Required Vocabulary

| Concept | Meaning |
|---------|---------|
| **Reasoning visibility** | The visible rationale that connects evidence, interpretation, assumptions, prioritization, uncertainty, escalation, and conclusion. |
| **Decision traceability** | A future operator can reconstruct why a governance decision was made and what sources or rules supported it. |
| **Escalation explainability** | Escalation, non-escalation, HITL, STOP, waiver, or continuation decisions explain their trigger and boundary. |
| **Prioritization transparency** | The report shows why some findings matter more than others. |
| **Conclusion readability** | Recommendations and verdicts remain scoped, human-readable, and reviewable. |
| **Reasoning continuity** | Reasoning survives handoff, compression, future QA, and freeze review. |
| **Hidden assumption** | A material assumption affects a conclusion but is not disclosed. |
| **Silent tradeoff** | A decision sacrifices one value, risk, or constraint for another without saying so. |
| **Opaque escalation** | A HITL or non-HITL decision is made without explaining why. |
| **Unverifiable reasoning** | The rationale cannot be tied to evidence, source, assumption, or uncertainty. |
| **Black-box governance** | Governance asks reviewers to trust the system instead of reviewing the rationale. |
| **Traceable conclusion** | A conclusion names evidence, interpretation, priority, uncertainty, and action boundary. |
| **Transparency proportionality** | Explanation depth scales with consequence, uncertainty, escalation relevance, and review risk. |

---

## 4. Core Rules

- **Conclusions should remain explainable.**
- **Prioritization should stay visible.**
- **Escalation requires reasoning.**
- **Uncertainty should remain readable.**
- **Assumptions should be disclosed** when they affect a material conclusion.
- **Governance must remain reviewable** by a future operator.
- **Reasoning traceability matters** as much as the final recommendation.
- **Transparency preserves trust** because reviewers can inspect the path, not only the verdict.
- **Tradeoffs should be named** when they affect severity, scope, freeze, escalation, or implementation direction.
- **Recommendations should not exceed their rationale.**
- **Transparency should be proportional**: critical, ambiguous, irreversible, or authority-sensitive decisions require more visible rationale than low-risk observations.

---

## 5. Anti-Patterns

Forbidden drift:

| Anti-pattern | Why it is forbidden |
|--------------|---------------------|
| **Black-box governance** | Asks humans to trust opaque system output instead of reviewing rationale. |
| **Recommendation without reasoning** | Produces action guidance without evidence, assumption, uncertainty, or priority path. |
| **Escalation without explanation** | Sends or suppresses HITL without naming the trigger. |
| **Hidden tradeoffs** | Conceals what was deprioritized, deferred, or accepted as risk. |
| **Silent assumptions** | Lets guesses become decision inputs without disclosure. |
| **Opaque prioritization** | Makes findings appear ordered or severe without explaining why. |
| **Unverifiable conclusions** | Conclusions cannot be reconstructed from available artifacts. |
| **Fake certainty through summarization** | Polished summaries hide uncertainty, evidence gaps, or partial validation. |
| **Reasoning collapse into verdicts** | The report gives PASS/FAIL/STOP without the rationale needed for review. |
| **"Trust the system" governance** | Replaces human-supervised review with confident language. |

Use [reasoning-drift-taxonomy.md](reasoning-drift-taxonomy.md) for full drift classification.

---

## 6. Forge Integration

When Forge is selected, reasoning visibility becomes a pre-freeze and report-readability concern:

- Run [`reasoning-visibility-checklist.md`](../../agents/mars-forge/reasoning-visibility-checklist.md) when findings, prioritization, escalation, QA confidence, source lineage, context survivability, or visual reconciliation produce recommendations or conclusions.
- Record **REASONING VISIBILITY FINDINGS** for reasoning-visibility QA, prioritization-traceability QA, escalation-explainability QA, uncertainty-visibility QA, assumption-disclosure QA, and traceable-conclusion QA.
- Use [reasoning-visibility-model.md](reasoning-visibility-model.md) to keep evidence, interpretation, prioritization, escalation, conclusion, uncertainty, and traceability layers readable.
- Use [reasoning-drift-taxonomy.md](reasoning-drift-taxonomy.md) to name opaque reasoning, hidden assumptions, unexplained escalation, invisible prioritization logic, conclusion-without-traceability, silent tradeoff drift, unverifiable recommendation, governance black-boxing, reasoning collapse, decision ambiguity, implicit conclusion inflation, confidence opacity, and traceability erosion.
- Keep **REASONING VISIBILITY FINDINGS** separate from `RISK WEIGHTING FINDINGS`, `QA CONFIDENCE FINDINGS`, `HUMAN ESCALATION FINDINGS`, `SOURCE LINEAGE FINDINGS`, `CONTEXT SURVIVABILITY FINDINGS`, and `VISUAL FINDINGS`, then summarize whether the decision path is reviewable.
- Use [trust-calibration-governance.md](trust-calibration-governance.md) when visible rationale affects trust calibration, perceived reliability, confidence proportionality, or credibility survivability; report `TRUST CALIBRATION FINDINGS` separately.
- Use [cognitive-load-governance.md](cognitive-load-governance.md) when reasoning visibility risks becoming unreadable, over-dense, attention-fragmenting, or cognitively unsustainable; report `COGNITIVE LOAD FINDINGS` separately.
- Treat reasoning visibility as human-supervised methodology, not hidden chain-of-thought disclosure or autonomous reasoning validation.

---

## 7. Triumph V2 Lessons Captured

Triumph V2 exposed reusable Website Factory transparency lessons:

- A report can contain many correct findings while leaving the reason for priority order unclear.
- Visual, source, QA confidence, escalation, and implementation findings need a visible decision path before freeze.
- SAFE UNKNOWN is more useful when it explains why the unknown matters and what would resolve it.
- Escalation decisions are hard to review when assumptions, source priority, or tradeoffs are summarized away.
- A confident conclusion can look operationally strong while hiding the evidence level, source boundary, or decision owner.
- Multi-session work needs reasoning continuity; future operators should not have to infer why a recommendation was made.

These are Website Factory governance lessons, not Triumph redesign instructions.

---

## 8. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Evidence path is missing | Cannot reconstruct why the conclusion was reached. |
| Assumptions are suspected but not named | Cannot tell whether the conclusion depends on hidden guesses. |
| Tradeoffs are unclear | Cannot know what risk was accepted or deprioritized. |
| Prioritization logic is invisible | Cannot verify why findings were ordered, escalated, deferred, or demoted. |
| Escalation rationale is absent | Cannot judge whether HITL, STOP, waiver, or continuation was appropriate. |
| Conclusion exceeds visible rationale | Cannot trust recommendation scope. |
| Reasoning was compressed away | Cannot reconstruct decision path from the current record. |

**Action:** state what reasoning layer is missing, what evidence or human decision would restore traceability, and whether continuation is safe with disclosure, HITL recommended, HITL required, blocked, or STOP.

---

## 9. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Decision Transparency & Reasoning Visibility Governance layer - reasoning visibility, decision traceability, escalation explainability, prioritization transparency, conclusion readability, drift taxonomy, and Forge `REASONING VISIBILITY FINDINGS`; documentation only. |
| v0.1 | 2026-05-17 | Linked Human Cognitive Load & Review Ergonomics Governance for readable rationale, proportional transparency depth, attention clarity, and cognitive survivability. |
