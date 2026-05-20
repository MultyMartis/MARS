# MARS Website Factory - Governance Prioritization & Risk Weighting

**Status:** **documented** - Website Factory prioritization governance and human-supervised risk-weighting methodology only.  
**Not:** autonomous risk AI, scoring engine, universal severity law, perfect prioritization guarantee, or replacement for human project judgment.

**Core principle:** frontend governance must preserve **severity proportionality, operational focus, signal clarity, escalation relevance, and meaningful prioritization**.  
It is not merely "detect issues," "list findings," "flag drift," or "expand QA coverage."

**Companion documents:** [risk-weighting-model.md](risk-weighting-model.md), [prioritization-drift-taxonomy.md](prioritization-drift-taxonomy.md).  
**Related layers:** [adaptive-governance.md](adaptive-governance.md), [decision-transparency-governance.md](decision-transparency-governance.md), [cognitive-load-governance.md](cognitive-load-governance.md), [qa-confidence-governance.md](qa-confidence-governance.md), [governance-minimalism.md](governance-minimalism.md), [governance-economics.md](governance-economics.md), [implementation-reliability-governance.md](implementation-reliability-governance.md), [strategic-intent-governance.md](strategic-intent-governance.md), [human-escalation-governance.md](human-escalation-governance.md), [meta-governance-integrity.md](meta-governance-integrity.md), [visual-reconciliation-layer.md](visual-reconciliation-layer.md).  
**Forge checklist:** [`../../agents/mars-forge/risk-weighting-checklist.md`](../../agents/mars-forge/risk-weighting-checklist.md).

---

## 1. Positioning

Governance Prioritization & Risk Weighting exists because Website Factory governance now covers semantic governance, provenance governance, workflow discipline, temporal continuity, context survivability, recovery governance, governance minimalism, implementation survivability, QA confidence, and many frontend intent checks.

That coverage is valuable only if critical risks remain more visible than minor drift.

| This layer governs | This layer does not govern |
|--------------------|----------------------------|
| Severity proportionality, risk visibility, operational focus, signal-to-noise ratio, and escalation relevance | Mathematical scoring, automated risk ranking, or universal severity law |
| Human-supervised prioritization of governance findings across frontend QA layers | Replacing specialist findings from visual, strategic, implementation, QA, escalation, or source layers |
| Drift vocabulary for equal-priority overload, critical-risk dilution, severity inflation, governance noise, and review imbalance | Claiming perfect prioritization or eliminating human judgment |
| Forge reporting discipline for `RISK WEIGHTING FINDINGS` | Runtime enforcement, autonomous risk AI, or hidden decision engines |

The governance question is not "how many findings were reported?"  
The governance question is: **can the operator see what matters most, why it matters, and what must happen next?**

---

## 2. Canonical Definition

**Governance prioritization** is the discipline of preserving operational attention by making risk severity, escalation relevance, and review urgency readable across many governance findings.

**Risk weighting** is the human-supervised method for distinguishing critical, operational, continuity, strategic, cosmetic, escalation-only, and informational findings without pretending that all findings carry equal operational weight.

This layer protects:

- **Risk visibility** - dangerous findings stay visible instead of being buried in report volume.
- **Severity proportionality** - severity remains matched to impact, uncertainty, reversibility, and operational consequence.
- **Operational focus** - reviewers can identify the next safe action.
- **Governance signal clarity** - findings communicate priority, not only category.
- **Escalation relevance** - HITL requests are reserved for material decisions, contradictions, authority gaps, and critical uncertainty.
- **Prioritization survivability** - priority survives handoff, compression, fatigue, and future review.
- **Governance attention economy** - operator attention is treated as a limited operational resource.

A governance system may report many findings, look extremely thorough, generate large QA outputs, and appear highly protective while still missing critical risks, diluting operational focus, overwhelming reviewers, or hiding the truly dangerous issues.

---

## 3. Required Vocabulary

| Concept | Meaning |
|---------|---------|
| **Risk weighting** | Human-supervised classification of findings by operational consequence, urgency, reversibility, uncertainty, and escalation need. |
| **Governance prioritization** | The discipline of making the most important risks easiest to see and act on. |
| **Severity proportionality** | Severity labels remain proportional to real impact instead of inflated or flattened. |
| **Operational criticality** | The degree to which a finding can block safe execution, freeze, delivery, continuity, or trust. |
| **Signal-to-noise ratio** | The relationship between useful governance signal and low-value reporting noise. |
| **Prioritization readability** | A future operator can understand which findings matter first and why. |
| **Escalation relevance** | Escalation is tied to authority, contradiction, critical uncertainty, or material consequence. |
| **Governance noise** | Findings, warnings, or report sections that add volume without decision value. |
| **Critical-path awareness** | Review attention follows the risks that can block safe progress or damage project intent. |
| **Severity inflation** | Minor or speculative issues are reported as critical, weakening trust in severity language. |
| **Low-value finding** | A valid observation whose operational consequence is too small to justify heavy review or escalation. |
| **Review imbalance** | Reviewer attention is consumed by minor, cosmetic, duplicated, or low-risk findings while higher-risk issues receive less clarity. |
| **Focus preservation** | Governance protects the operator's ability to make safe decisions under limited attention. |
| **Governance attention economy** | The principle that attention is finite and must be spent where risk, uncertainty, and consequence justify it. |

---

## 4. Core Rules

- **Not all findings are equally important.**
- **Severity should remain proportional** to consequence, uncertainty, reversibility, and authority boundary.
- **Operational risks matter more than cosmetic drift** when freeze, delivery, trust, continuity, or source authority is affected.
- **Escalation requires weighting.** A finding should not become HITL merely because it is reportable.
- **Governance clarity matters.** The report should help a reviewer decide what to do next.
- **Excessive noise weakens QA** by hiding real blockers and exhausting review attention.
- **Prioritization preserves survivability** across long sessions, handoffs, compressed context, and future iterations.
- **Focus is a limited operational resource.**
- **Critical findings should stay visually and narratively distinct** from minor observations.
- **Low-risk issues can be deferred, grouped, or recorded as informational** when deeper review would add noise.
- **SAFE UNKNOWN should be weighted** by consequence; not every unknown has the same action requirement.

---

## 5. Prioritization Method

For each material finding, identify:

| Question | Prioritization meaning |
|----------|------------------------|
| What can break? | Operational, strategic, visual, source, QA, continuity, or escalation impact. |
| How severe is the consequence? | Critical, operational, continuity, strategic, minor, escalation-only, or informational. |
| How reversible is the issue? | Easy local fix, scoped correction, structural change, HITL decision, or delivery blocker. |
| What evidence supports it? | Direct, rendered, source-level, build-level, inferred, assumed, or unknown. |
| Does it need action now? | Stop, fix before freeze, escalate, disclose, defer, monitor, or record only. |
| Does reporting it add signal? | If not, group or demote it to avoid governance noise. |

**Rule:** priority should be stated in operational language, not only severity labels. A finding that says `critical` but does not explain operational consequence creates false criticality.

---

## 6. Forge Integration

When Forge is selected, risk weighting becomes a pre-freeze and report-readability concern:

- Run [`risk-weighting-checklist.md`](../../agents/mars-forge/risk-weighting-checklist.md) when findings are numerous, severity is unclear, escalation volume is rising, or report focus is at risk.
- Record **RISK WEIGHTING FINDINGS** for risk-weighting QA, prioritization QA, escalation relevance QA, signal-to-noise QA, severity proportionality QA, and operational-focus QA.
- Use [risk-weighting-model.md](risk-weighting-model.md) to classify findings into critical-risk, operational-risk, continuity-risk, strategic-risk, cosmetic/minor-risk, escalation-only, or informational layers.
- Use [prioritization-drift-taxonomy.md](prioritization-drift-taxonomy.md) to name equal-priority overload, minor-drift obsession, critical-risk dilution, severity inflation, governance noise escalation, low-value escalation, review imbalance, cosmetic-over-critical focus, signal-to-noise collapse, false criticality, disproportionate QA allocation, escalation fatigue, and operational focus erosion.
- Keep **RISK WEIGHTING FINDINGS** separate from `QA CONFIDENCE FINDINGS`, `GOVERNANCE MINIMALISM FINDINGS`, `IMPLEMENTATION RELIABILITY FINDINGS`, `STRATEGIC INTENT FINDINGS`, `HUMAN ESCALATION FINDINGS`, and `VISUAL FINDINGS`, then summarize which risks require action first.
- Use [governance-economics.md](governance-economics.md) when prioritization also needs review-cost awareness, governance resource allocation, validation efficiency, or governance ROI review; report `GOVERNANCE ECONOMICS FINDINGS` separately.
- Use [cognitive-load-governance.md](cognitive-load-governance.md) when prioritization must protect reviewer attention, report readability, signal visibility, or cognitive survivability across many findings; report `COGNITIVE LOAD FINDINGS` separately.
- Use [adaptive-governance.md](adaptive-governance.md) when prioritized risks need a proportional governance-depth choice, adaptive QA depth, context-aware escalation, or process-scaling justification; report `ADAPTIVE GOVERNANCE FINDINGS` separately.
- Use [decision-transparency-governance.md](decision-transparency-governance.md) when prioritization logic, severity order, tradeoffs, escalation relevance, or final recommendation needs visible rationale; report `REASONING VISIBILITY FINDINGS` separately.
- Use [meta-governance-integrity.md](meta-governance-integrity.md) when findings conflict because governance layers overlap, duplicate severity language, or obscure which layer owns the priority decision; report `META-GOVERNANCE FINDINGS` separately.
- Treat this as human-supervised prioritization governance, not scoring automation.

---

## 7. Triumph V2 Lessons Captured

Triumph V2 exposed reusable Website Factory prioritization lessons:

- A long QA report can appear safer while burying the few findings that determine freeze readiness.
- Visual, semantic, source, implementation, QA confidence, and escalation findings need priority order; otherwise every concern reads as equal.
- Minor spacing, icon, or cosmetic drift can consume disproportionate attention if critical source, CTA, proof, or freeze risks are not weighted.
- SAFE UNKNOWN matters more when it touches source authority, mobile intent, business meaning, release confidence, or human approval than when it affects a small reversible detail.
- Governance minimalism reduces bloat, but prioritization is still needed inside the findings that remain.
- Reviewers need a short critical-path summary before dense evidence, not only exhaustive category coverage.

These are Website Factory governance lessons, not Triumph redesign instructions.

---

## 8. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Severity cannot be justified | Cannot prove whether a finding is critical, operational, minor, or informational. |
| Escalation relevance is unclear | Cannot tell whether HITL is needed or whether disclosure is enough. |
| Report volume hides priorities | Cannot claim review readiness when critical findings may be buried. |
| Findings conflict in priority | Cannot decide whether visual, strategic, implementation, source, or QA risk should lead. |
| Evidence is too weak for severity | Cannot assign high severity from inferred or assumed evidence without disclosure. |
| Low-value findings overwhelm review | Cannot prove governance signal clarity. |
| Critical-path impact is unknown | Cannot determine whether freeze, delivery, trust, or continuity is affected. |

**Action:** state the missing evidence, classify the provisional risk layer, name what would resolve severity, and choose action: stop, fix before freeze, HITL required, HITL recommended, disclose, defer, or informational.

---

## 9. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Governance Prioritization & Risk Weighting layer - severity proportionality, operational focus, signal clarity, risk weighting model, prioritization drift taxonomy, and Forge `RISK WEIGHTING FINDINGS`; documentation only. |
| v0.1 | 2026-05-17 | Linked Decision Transparency & Reasoning Visibility Governance for prioritization traceability, visible severity rationale, tradeoff disclosure, and reviewable recommendations. |
| v0.2 | 2026-05-17 | Linked Adaptive Governance & Context-Sensitive Discipline for proportional governance-depth choice, adaptive QA depth, contextual escalation, and process-scaling justification. |
| v0.3 | 2026-05-17 | Linked Human Cognitive Load & Review Ergonomics Governance for reviewer attention, report readability, signal visibility, and cognitive survivability across many findings. |
