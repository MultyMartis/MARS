# MARS Website Factory — Source Interpretation Governance

**Status:** **documented** — Website Factory interpretation governance and human-supervised frontend methodology only.  
**Not:** automated source understanding, computer vision, screenshot diff, runtime interpretation AI, universal design-reading truth, or autonomous redesign.

**Core principle:** the source is **not automatically self-explanatory**.  
Frontend implementation quality depends on **how the source is interpreted**, not only on how HTML, CSS, responsive behavior, spacing, or components are written.

**Companion documents:** [source-confidence-model.md](source-confidence-model.md), [source-ambiguity-taxonomy.md](source-ambiguity-taxonomy.md).  
**Adjacent layers:** [knowledge-provenance-governance.md](knowledge-provenance-governance.md), [design-intent-transfer-governance.md](design-intent-transfer-governance.md), [visual-reconciliation-layer.md](visual-reconciliation-layer.md), [compositional-structure-awareness.md](compositional-structure-awareness.md), [responsive-intent-governance.md](responsive-intent-governance.md), [implementation-reliability-governance.md](implementation-reliability-governance.md), [content-density-governance.md](content-density-governance.md), [interaction-intent-governance.md](interaction-intent-governance.md), [qa-confidence-governance.md](qa-confidence-governance.md), [human-escalation-governance.md](human-escalation-governance.md), [multi-agent-coordination-governance.md](multi-agent-coordination-governance.md).  
**Forge checklist:** [`../../agents/mars-forge/source-interpretation-checklist.md`](../../agents/mars-forge/source-interpretation-checklist.md).

---

## 1. Positioning

Source Interpretation Governance formalizes a missing phase between **source receipt** and **frontend implementation**:

| Source interpretation governance **is** | It **is not** |
|-----------------------------------------|---------------|
| A disciplined read of what the source explicitly says, strongly implies, weakly implies, leaves ambiguous, or contradicts | A replacement for design, HITL approval, or source authoring |
| A risk-control layer for screenshot overfitting, semantic hallucination, false grouping, and missing-source guessing | A claim that screenshots contain complete system specification |
| A reporting vocabulary for confidence, ambiguity, assumptions, and SAFE UNKNOWN | A pixel-perfect or CV-based extraction method |
| A human-supervised anti-hallucination discipline for Website Factory frontend work | A universal design-reading ontology |

The layer exists because even a correct implementation pipeline can drift if the **input read** is wrong: invented grouping, fake semantic assumptions, source ambiguity collapse, accidental redesign, or overconfident extraction from incomplete screenshots.

---

## 2. Core Concepts

| Concept | Meaning |
|---------|---------|
| **Source interpretation** | The governed act of reading approved inputs and separating observed facts from inferred intent, assumptions, ambiguity, and unknowns. |
| **Interpretation confidence** | The declared strength of evidence for an implementation decision; see [source-confidence-model.md](source-confidence-model.md). |
| **Source ambiguity** | A source condition where multiple credible reads exist or the source does not decide the intended behavior, grouping, hierarchy, state, or breakpoint. |
| **Inferred intent** | A reasonable implementation read derived from source patterns, adjacency, or repeated design logic, but not explicitly stated. |
| **Screenshot overfitting** | Treating every visible pixel relationship as intentional and authoritative. |
| **Semantic hallucination** | Inventing meaning, entity counts, UX roles, hierarchy, or interaction logic not present in the source. |
| **Visual assumption drift** | Letting a plausible visual read become an unreported implementation assumption. |
| **False certainty** | Reporting PASS or full fidelity when the source only supports weak inference, ambiguity, or UNKNOWN. |
| **Missing-source escalation** | Stopping or escalating when required inputs are absent: mobile source, hover state, section authority, interaction rule, copy authority, or asset source. |
| **Source contradiction** | Two approved-looking sources disagree and no priority rule resolves the conflict. |
| **Visual extraction uncertainty** | Uncertainty caused by raster artifacts, compression noise, crop, low resolution, export artifacts, or hidden states. |
| **Inferred grouping** | A grouping read based on proximity, framing, or rhythm, but not explicitly documented. |
| **Undocumented intent** | An intended behavior or visual role that may exist, but is not captured in the current source set. |
| **Interpretation contamination** | Cross-version, archive, prior-session, foundation-default, or adjacent-section influence that changes the source read. |
| **Hallucinated structure** | Invented section splits, wrappers, cards, tabs, sliders, catalogs, forms, or hierarchy absent from source authority. |

---

## 3. Observed / Inferred / Assumed / Unknown

Every implementation-relevant source read should distinguish:

| Classification | Definition | Implementation posture |
|----------------|------------|--------------------------|
| **Observed** | Directly visible or written in approved source. | Implement normally, citing source path or charter. |
| **Inferred** | Strongly or weakly implied by source pattern but not explicit. | Implement only with confidence label and report when material. |
| **Assumed** | Chosen for practical completion because source is incomplete. | Avoid by default; if unavoidable, disclose approximation and resolver. |
| **Unknown** | Source does not decide the matter. | Use **SAFE UNKNOWN**, HITL, or stop depending on impact. |

**Rule:** hidden ambiguity is more dangerous than visible uncertainty. SAFE UNKNOWN is a feature, not a failure.

---

## 4. Screenshot Authority Boundary

Not every visible screenshot detail is authoritative.

Examples of non-authoritative or weak-authority screenshot details:

- Raster artifacts.
- Compression noise.
- Export artifacts.
- Accidental alignment.
- Cropping effects.
- Hidden responsive intent.
- Missing hover states.
- Absent interaction states.
- Placeholder imagery or temporary copy.
- Anti-aliased edges that look like borders or shadows.
- Low-resolution spacing that cannot support exact measurement.

**Rule:** screenshot source can be authoritative for visible hierarchy, composition, copy, and visual intent only to the degree the evidence supports. It is not a complete system specification.

---

## 5. Required Principles

- **Interpretation confidence must be explicit** for material implementation decisions.
- **Ambiguity should be surfaced, not hidden** behind polished code or confident prose.
- **SAFE UNKNOWN is a feature, not failure.**
- **Screenshot != complete system specification.**
- **Implementation must distinguish observed, inferred, assumed, and unknown.**
- **Contradictions must be reported** instead of silently resolved by taste.
- **Approximation must be disclosed** when fidelity cannot be proven from source.
- **Missing-source conditions must escalate** when they affect meaning, hierarchy, grouping, interaction, responsive intent, asset authority, or freeze.
- **Visual extraction uncertainty must not inflate into certainty.**
- **No source interpretation should authorize accidental redesign.**

---

## 6. Forbidden Drift

| Anti-pattern | Why it is forbidden |
|--------------|---------------------|
| **Pretending certainty** | Converts ambiguity into false PASS / freeze. |
| **Hallucinating UX** | Invents tabs, forms, sliders, hover logic, or mobile behavior absent from source. |
| **Inventing semantics** | Changes meaning, entity count, CTA purpose, or page story. |
| **Inventing hierarchy** | Makes a secondary object primary or creates a new section story. |
| **Fake responsive assumptions** | Treats desktop-only source as full breakpoint authority. |
| **Screenshot worship** | Treats artifacts, noise, and accidental alignment as design law. |
| **Aggressive redesign inference** | Uses incomplete source as permission to “improve” the design. |
| **Silent guessing** | Hides assumptions in implementation without REPORT disclosure. |
| **Approximation without disclosure** | Makes practical compromises look like source-faithful decisions. |
| **Inferred certainty inflation** | Promotes weak implication to explicit truth. |

---

## 7. Forge Integration

When Forge is selected, source interpretation becomes a pre-freeze QA concern:

- Run [`source-interpretation-checklist.md`](../../agents/mars-forge/source-interpretation-checklist.md) before declaring source reading complete.
- Record **SOURCE INTERPRETATION FINDINGS** when confidence, ambiguity, contradiction, missing source, or approximation affects implementation.
- Use [source-confidence-model.md](source-confidence-model.md) for confidence labels.
- Use [source-ambiguity-taxonomy.md](source-ambiguity-taxonomy.md) for named ambiguity / drift patterns.
- Use [design-intent-transfer-governance.md](design-intent-transfer-governance.md) when an interpretation becomes a source-to-build fidelity, approximation, hierarchy fidelity, semantic transfer, or reconstruction survivability claim; report `RECONSTRUCTION FIDELITY FINDINGS` separately.
- Treat source contradiction as a HITL or stop condition unless current charter priority resolves it.
- Enforce SAFE UNKNOWN when the source does not authorize the implementation decision.
- Use [decision-boundary-model.md](decision-boundary-model.md) when SAFE UNKNOWN is not enough by itself and the issue needs continue-with-disclosure, HITL, stop, or contradiction blocking.

This integrates with Forge semantic source lock, visual reconciliation, composition awareness, responsive intent, content density, and contamination governance. It does not replace them.

Interaction behavior is a source interpretation concern when hover states, clickability, focus, motion, mobile tap behavior, CTA behavior, or disclosure behavior are absent, ambiguous, inferred, or contradictory. Record those issues as **SOURCE INTERPRETATION FINDINGS** and continue into [`interaction-intent-checklist.md`](../../agents/mars-forge/interaction-intent-checklist.md) when behavior is in scope.

Implementation reliability is a source interpretation concern when include ownership, override authority, breakpoint authority, rebuild behavior, or regression impact depends on inferred, missing, ambiguous, or contradictory implementation source. Record those issues as **SOURCE INTERPRETATION FINDINGS** and continue into [`implementation-reliability-checklist.md`](../../agents/mars-forge/implementation-reliability-checklist.md) when stability over time is in scope.

Multi-agent coordination is a source interpretation concern when one role's source read, assumption, contradiction, or SAFE UNKNOWN state is handed to another role. Use [multi-agent-coordination-governance.md](multi-agent-coordination-governance.md) to prevent silent assumption inheritance, chain hallucination, fake consensus, and reviewer/validator contamination.

Knowledge provenance is a source interpretation concern when the origin, authority, freshness, derivation, transformation boundary, or lineage of a source read is unclear. Use [knowledge-provenance-governance.md](knowledge-provenance-governance.md) and [`source-lineage-checklist.md`](../../agents/mars-forge/source-lineage-checklist.md) to keep interpreted source reads from becoming hidden authority.

---

## 8. Triumph V2 Lessons Captured

Triumph V2 exposed reusable interpretation lessons for Website Factory:

- A screenshot can suggest grouping, but grouping may be inferred rather than explicit; this must be reported before DOM changes.
- A light / dark surface read can be contaminated by global foundation defaults or neighboring sections.
- Missing mobile source makes responsive intent weaker than desktop visual confidence.
- Low-resolution or cropped exports can create false certainty around spacing, alignment, and hierarchy.
- A semantically correct rebuild can still drift if the source read invents hidden structure, entity count, CTA role, or section purpose.
- Composition, cadence, density, and responsive decisions often fail at the **interpretation** layer before they fail in CSS.

These are Website Factory governance lessons, not Triumph-specific redesign instructions.

---

## 9. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it blocks certainty |
|-----------|--------------------------|
| Missing active source path | Cannot prove what source governs. |
| Missing mobile / tablet source | Breakpoint intent cannot be chartered beyond survivability. |
| Conflicting screenshots or matrices | No single source authority is established. |
| Ambiguous grouping | Cannot prove whether objects are one cluster or separate. |
| Unclear interaction state | Hover, active, modal, tab, accordion, or form behavior is not specified. |
| Asset authority missing | Cannot prove icon, image, logo, or illustration source. |
| Low-quality raster source | Visual extraction uncertainty affects spacing, hierarchy, or details. |
| Inferred semantics only | Meaning or entity role is not explicit enough for implementation confidence. |

**Action:** state what is unknown, what would resolve it, whether implementation should stop, continue with disclosed approximation, or require HITL.

---

## 10. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Source Interpretation Governance layer — interpretation confidence, ambiguity, screenshot authority boundary, Forge reporting. |
| v0.1 | 2026-05-17 | Linked Interaction Intent Governance for missing/ambiguous hover, clickability, motion, CTA, and mobile interaction source states. |
| v0.2 | 2026-05-17 | Linked Implementation Reliability Governance for inferred implementation ownership, override authority, breakpoint authority, rebuild behavior, and regression impact. |
| v0.3 | 2026-05-17 | Linked Human Escalation & Decision Boundary Governance for SAFE UNKNOWN action boundaries, HITL, stop conditions, and contradiction blocking. |
| v0.4 | 2026-05-17 | Linked Multi-Agent Coordination & Responsibility Governance for source-read handoff integrity, assumption propagation, chain hallucination, and fake-consensus risk. |
| v0.5 | 2026-05-17 | Linked Knowledge Provenance & Source Lineage Governance for origin, authority, freshness, derivation, transformation-boundary, and lineage risk in source reads. |
| v0.6 | 2026-05-17 | Linked Design Intent Transfer & Reconstruction Fidelity Governance for source-to-build fidelity, approximation transparency, hierarchy fidelity, semantic transfer, and reconstruction survivability. |
