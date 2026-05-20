# MARS Website Factory - Evolutionary Drift Taxonomy

**Status:** **documented** - Website Factory drift vocabulary for governance evolution and self-refinement review only.  
**Not:** automated drift detection, runtime governance mutation, universal methodology law, or proof of autonomous governance adaptation.

**Parent governance:** [governance-evolution-governance.md](governance-evolution-governance.md).  
**Model:** [self-refinement-model.md](self-refinement-model.md).  
**Forge checklist:** [`../../agents/mars-forge/governance-evolution-checklist.md`](../../agents/mars-forge/governance-evolution-checklist.md).

---

## 1. Purpose

This taxonomy names drift patterns that appear when governance cannot evolve safely.

Evolutionary drift is not only "too much governance" or "bad process." It includes both extremes:

- governance becomes too rigid to adapt;
- governance changes too freely to preserve continuity;
- old assumptions survive without review;
- new rules accumulate without proportionality;
- refinement happens without traceability.

The taxonomy supports **GOVERNANCE EVOLUTION FINDINGS** in Forge reports.

---

## 2. Drift Patterns

| Drift pattern | Meaning | Typical signal |
|---------------|---------|----------------|
| **Governance stagnation** | Governance stops improving even when repeated evidence shows the method no longer fits. | Same friction or failure repeats, but rules remain unchanged. |
| **Methodology fossilization** | A method survives as fixed doctrine after its context has changed. | "This is how we do it" replaces evidence review. |
| **Legacy-rule accumulation** | Old rules pile up without classification, deprecation, or usefulness review. | Operators face many inherited rules with unclear current value. |
| **Anti-evolution drift** | Adaptation itself is treated as suspicious or forbidden. | Any method update is rejected as weakening governance. |
| **Frozen-process decay** | A static process decays because it cannot respond to new risks, tools, sources, or project realities. | Process looks stable but produces stale decisions. |
| **Institutional rigidity** | The organization protects familiar methodology over operational evidence. | Human review defends process identity instead of project quality. |
| **Self-protection governance** | Governance becomes hard to critique because it treats its own existence as proof of correctness. | Problems are blamed on operators rather than reviewing the method. |
| **Uncontrolled governance mutation** | Governance changes silently, locally, or impulsively without traceability. | Reports, checklists, or methods differ without reason or history. |
| **Continuity-breaking evolution** | Methodology changes in a way that breaks old report readability, authority lineage, or lesson reuse. | Future operators cannot interpret prior findings after a rule change. |
| **Refinement opacity** | Governance is refined without explaining source evidence, rationale, scope, or impact. | A new rule exists but no one can tell why. |
| **Governance ossification** | Governance remains structurally intact but loses practical adaptability. | It appears mature while becoming obsolete. |
| **Adaptive survivability erosion** | Governance cannot balance stability and adaptation over long-term use. | Either process collapses under change or refuses change until it fails. |
| **Historical-lineage disruption** | Refinement breaks traceability from old rationale to new method. | Old lessons, decisions, and rules become disconnected from current governance. |

---

## 3. Stagnation Family

| Pattern | Description | Risk |
|---------|-------------|------|
| **Governance stagnation** | The method remains unchanged despite repeated drift evidence. | Obsolete governance keeps producing known failures. |
| **Methodology fossilization** | A once-useful method becomes preserved as ritual. | Context changes while authority does not. |
| **Frozen-process decay** | Process stability hides slow loss of fit. | A mature-looking process becomes fragile. |
| **Institutional rigidity** | Governance culture resists updating assumptions. | Operators stop surfacing needed refinements. |
| **Governance ossification** | Governance is documented but no longer metabolizes lessons. | Documentation survives while adaptability dies. |

---

## 4. Legacy-Rule Family

| Pattern | Description | Risk |
|---------|-------------|------|
| **Legacy-rule accumulation** | Old rules remain active without current scope or rationale. | Operators inherit contradictory or stale methodology. |
| **Unreviewed governance inheritance** | Prior project/process assumptions are imported into current work without review. | Old context becomes false authority. |
| **Legacy governance drift** | Governance created for one condition continues after that condition has expired. | Stale controls block better current decisions. |
| **Old-process absolutism** | Age is treated as correctness. | "Old process therefore correct" replaces evidence. |

---

## 5. Mutation Family

| Pattern | Description | Risk |
|---------|-------------|------|
| **Uncontrolled governance mutation** | Method changes without authority, scope, or traceability. | Governance becomes unpredictable and hard to trust. |
| **Continuity-breaking evolution** | Change improves local fit but breaks historical readability. | Reports and lessons lose compatibility. |
| **Refinement opacity** | The change exists, but its reason and impact are unclear. | Future operators cannot review or reverse it. |
| **Methodology churn** | Governance changes too often or too broadly for stable use. | Operators cannot know which method governs. |
| **Hidden authority expansion** | Refinement silently increases what governance claims to control. | Governance power grows without review. |

---

## 6. Anti-Evolution Family

| Pattern | Description | Risk |
|---------|-------------|------|
| **Anti-evolution drift** | Adaptation is resisted even when evidence supports it. | Governance becomes brittle and obsolete. |
| **Governance self-protection** | The method protects itself from critique or pruning. | Process survival outranks operational usefulness. |
| **Adaptation resistance** | Operators avoid refinement because old methodology feels safer. | Necessary learning never reaches governance. |
| **Methodology identity lock** | Governance identity is treated as more important than project needs. | Methodology becomes institutional ego. |

---

## 7. Continuity Family

| Pattern | Description | Risk |
|---------|-------------|------|
| **Historical-lineage disruption** | Old rationale, evidence, or lesson path is broken by refinement. | Future work cannot trace why governance changed. |
| **Refinement without memory** | Governance changes without preserving the lesson that motivated it. | The same debate will be rediscovered later. |
| **Deprecation opacity** | Rules disappear or weaken without historical state. | Operators cannot tell what is retired vs forgotten. |
| **Report compatibility break** | New methodology makes older reports hard to interpret. | Long-term governance memory becomes fragmented. |

---

## 8. Classification Guide

Use this guide when writing **GOVERNANCE EVOLUTION FINDINGS**:

| If the issue is... | Classify as... |
|--------------------|----------------|
| Old rules remain active without current rationale | Legacy-rule accumulation / legacy governance drift |
| Method cannot change despite new evidence | Governance stagnation / anti-evolution drift |
| Process looks mature but no longer fits | Governance ossification / frozen-process decay |
| Governance changes silently | Uncontrolled governance mutation / refinement opacity |
| New method breaks old report readability | Continuity-breaking evolution / historical-lineage disruption |
| Governance protects itself from critique | Self-protection governance / institutional rigidity |
| Refinement adds too much process for the evidence | Hidden authority expansion / legacy-rule accumulation / governance bloat companion finding |
| Refinement lacks source lesson | Refinement opacity / refinement without memory |

---

## 9. Severity Heuristics

| Severity | Use when |
|----------|----------|
| **Low** | Drift is local, visible, reversible, and does not affect authority or continuity. |
| **Medium** | Drift affects checklist use, report consistency, operator clarity, or repeated friction. |
| **High** | Drift affects governance authority, freeze/report interpretation, reusable lessons, or future methodology trust. |
| **Critical** | Drift may break historical continuity, create false authority, block necessary adaptation, or silently mutate Website Factory governance. |

Severity should stay proportional and may require separate `RISK WEIGHTING FINDINGS`.

---

## 10. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

- the age, source, or authority of a governance rule is unclear;
- the rationale for refinement is missing;
- continuity impact is unknown;
- it is unclear whether a rule is active, deprecated, experimental, or local;
- the drift could be stagnation or valid stability;
- the change could be refinement or uncontrolled mutation;
- future report compatibility cannot be determined.

**Action:** name the missing evidence, identify the resolver, and avoid treating either the old method or the new method as automatically correct.

---

## 11. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial evolutionary drift taxonomy - stagnation, fossilization, legacy-rule accumulation, anti-evolution drift, uncontrolled mutation, continuity-breaking evolution, refinement opacity, governance ossification, adaptive survivability erosion, and historical-lineage disruption; documentation only. |
