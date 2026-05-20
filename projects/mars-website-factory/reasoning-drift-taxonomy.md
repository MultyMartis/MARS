# MARS Website Factory - Reasoning Drift Taxonomy

**Status:** **documented** - Website Factory reasoning drift vocabulary and human-supervised classification only.  
**Not:** automated reasoning audit, chain-of-thought inspection, runtime governance engine, universal transparency law, or perfect explainability framework.

**Parent governance:** [decision-transparency-governance.md](decision-transparency-governance.md).  
**Companion model:** [reasoning-visibility-model.md](reasoning-visibility-model.md).  
**Forge checklist:** [`../../agents/mars-forge/reasoning-visibility-checklist.md`](../../agents/mars-forge/reasoning-visibility-checklist.md).

---

## 1. Purpose

This taxonomy names drift patterns where governance decisions look polished, confident, or complete while the reasoning path becomes hard to review.

Use it when findings, recommendations, escalation choices, prioritization, QA confidence, source lineage, context survivability, or visual reconciliation produce conclusions that may be opaque.

---

## 2. Drift Patterns

| Drift pattern | Symptom | Governance risk |
|---------------|---------|-----------------|
| **Opaque reasoning** | The report states a conclusion without showing evidence, interpretation, priority, uncertainty, or action boundary. | Reviewers cannot inspect why the conclusion is valid. |
| **Hidden assumptions** | Material assumptions influence the recommendation but are not disclosed. | Guesses become governance facts. |
| **Unexplained escalation** | HITL, STOP, waiver, or continuation is chosen without naming the trigger. | Human authority boundaries become arbitrary. |
| **Invisible prioritization logic** | Findings are ordered, marked severe, deferred, or escalated without explanation. | Critical risk may be buried or false criticality may inflate. |
| **Conclusion-without-traceability** | A PASS, FAIL, recommendation, freeze posture, or action cannot be traced to evidence. | Future operators cannot reconstruct or challenge the decision. |
| **Silent tradeoff drift** | The system accepts one risk to solve another without saying so. | Hidden compromises weaken trust and handoff quality. |
| **Unverifiable recommendation** | The action advice cannot be verified from source, QA evidence, governance rule, or human decision. | Implementation can follow unsupported guidance. |
| **Governance black-boxing** | The report implies "trust the system" instead of exposing reviewable rationale. | Human-supervised governance becomes performative. |
| **Reasoning collapse** | Evidence, interpretation, uncertainty, and priority collapse into a short verdict. | Conclusions become easy to read but hard to audit. |
| **Decision ambiguity** | It is unclear what decision was made, by whom, under what authority, or within what scope. | Freeze, escalation, or continuation can inherit unclear authority. |
| **Implicit conclusion inflation** | A narrow observation becomes a broad recommendation or confidence claim. | Scope expands without evidence. |
| **Confidence opacity** | Confidence is high, medium, low, or implied, but the evidence boundary is not visible. | QA confidence and decision confidence become rhetorical. |
| **Traceability erosion** | Each summary or handoff preserves the verdict but loses rationale details. | Long-chain work becomes dependent on memory or inference. |

---

## 3. Cross-Layer Drift Examples

| Layer | Reasoning drift example |
|-------|-------------------------|
| **QA confidence** | `PASS` is reported, but evidence level, proof boundary, and unverified states are missing. |
| **Human escalation** | HITL is requested without explaining whether the trigger is contradiction, approval boundary, assumption chain, or source priority. |
| **Governance prioritization** | Critical and minor findings appear in one list with no explanation of consequence or action order. |
| **Knowledge provenance** | A recommendation cites "previous work" but does not expose source lineage, authority, or transformation. |
| **Context survivability** | A compressed summary keeps the conclusion but removes assumptions, escalation memory, or uncertainty. |
| **Visual reconciliation** | A visual finding says "mismatch" without explaining hierarchy, density, focal path, source ambiguity, or priority. |

---

## 4. Severity Guidance

| Severity | When to use |
|----------|-------------|
| **Critical** | Reasoning opacity can authorize wrong source priority, hidden HITL, freeze, delivery confidence, business meaning, trust claim, or irreversible structural direction. |
| **Operational** | Reasoning opacity affects implementation direction, QA confidence, prioritization, handoff, or next action, but can be corrected locally. |
| **Continuity** | Reasoning opacity mainly affects future reconstruction, compressed context, checkpoint memory, or handoff survivability. |
| **Informational** | Rationale could be clearer, but consequence is low, reversible, and not likely to mislead review. |

Severity should be justified in plain language. Do not inflate severity merely because a drift term applies.

---

## 5. Detection Questions

Ask:

- Can the conclusion be reconstructed from visible evidence?
- Are assumptions named?
- Are tradeoffs disclosed?
- Is prioritization logic visible?
- Is escalation or non-escalation explained?
- Is confidence scoped to evidence?
- Would a future operator understand the decision after compression or handoff?
- Does the report ask the reviewer to trust a verdict without rationale?

Any material "no" can require **REASONING VISIBILITY FINDINGS**.

---

## 6. Anti-Patterns

Forbidden report shapes:

- `Recommendation: do X` with no reason.
- `HITL required` with no trigger.
- `PASS` with no evidence boundary.
- `Critical` with no consequence.
- `Looks correct` with no visual/source/QA rationale.
- `Proceed` while assumptions remain hidden.
- `Resolved` while tradeoffs are undisclosed.
- `Trust the governance result` as a substitute for reviewable rationale.

---

## 7. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

- reasoning path cannot be reconstructed;
- conclusion cannot be tied to evidence;
- assumption or tradeoff status is unknown;
- priority order cannot be justified;
- escalation trigger is unclear;
- confidence source is invisible;
- summary may have removed rationale.

**Action:** name the drift pattern, state the missing reasoning layer, and choose: add rationale, verify further, disclose partial, defer, HITL required, block, or STOP.

---

## 8. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Reasoning Drift Taxonomy - opaque reasoning, hidden assumptions, unexplained escalation, invisible prioritization, conclusion-without-traceability, silent tradeoffs, unverifiable recommendations, governance black-boxing, reasoning collapse, decision ambiguity, conclusion inflation, confidence opacity, and traceability erosion; documentation only. |
