# Adaptive Drift Taxonomy

**Status:** **documented** - Website Factory drift vocabulary for adaptive governance failures.  
**Not:** automated detection, runtime scoring, universal severity engine, autonomous governance correction, or replacement for human review.

**Parent layer:** [adaptive-governance.md](adaptive-governance.md).  
**Model:** [context-sensitive-discipline-model.md](context-sensitive-discipline-model.md).  
**Forge checklist:** [`../../agents/mars-forge/adaptive-governance-checklist.md`](../../agents/mars-forge/adaptive-governance-checklist.md).

---

## 1. Purpose

This taxonomy names failures where governance depth does not fit the work.

Adaptive drift can appear even when the process looks mature:

- many checklists were run;
- many findings were reported;
- escalation language was present;
- QA looked thorough;
- the workflow appeared disciplined.

The drift is that the wrong rigor level was applied to the wrong context.

---

## 2. Drift Classes

| Drift pattern | Definition | Typical symptom | Governance response |
|---------------|------------|-----------------|---------------------|
| **Governance-context mismatch** | Governance depth does not match task risk, scope, uncertainty, or consequence. | Simple edit receives full ceremony, or critical source ambiguity receives a short note. | Reclassify with [context-sensitive-discipline-model.md](context-sensitive-discipline-model.md). |
| **Static-rigidity drift** | A fixed process is applied without reassessing context. | "Always run the full process" or "always keep it light." | Require process-depth justification. |
| **Over-governance** | Process weight exceeds operational value for the scope. | Low-risk work produces long reports, repeated checklists, and fatigue. | Scale down to lightweight or standard depth. |
| **Under-governance** | Rigor is too weak for risk or consequence. | Freeze, delivery, accessibility, source authority, or business meaning receives minimal review. | Scale up to elevated, high-criticality, escalation-heavy, or continuity-sensitive depth. |
| **Disproportional QA** | QA depth is not aligned with evidence need or risk. | Full QA for trivial changes, or source-only PASS for interaction/accessibility risk. | Select targeted, standard, focused elevated, full relevant, or escalation QA. |
| **Adaptive-failure drift** | The process fails to change when new evidence changes the risk profile. | Work starts as low risk, becomes ambiguous, but governance depth remains unchanged. | Trigger adaptive-review layer. |
| **Process inflation under low risk** | Low-risk tasks accumulate full governance by habit. | Reports become longer than the change warrants. | Use governance minimalism and targeted QA. |
| **Insufficient rigor under high risk** | Critical tasks receive shallow process. | Source contradiction, mobile unknown, or freeze decision is treated as ordinary execution. | Apply high-criticality or escalation-heavy layer. |
| **One-size-fits-all governance** | Same workflow strictness is forced across all tasks. | No distinction between local edit, section freeze, recovery, and release decision. | Define discipline layer per task. |
| **Context-blind escalation** | Escalation is too much, too little, or wrong type for the authority boundary. | HITL spam for small reversible unknowns, or no HITL for human-owned decisions. | Use adaptive escalation levels. |
| **Operational rigidity** | Governance cannot flex around real operator constraints or project stage. | Process becomes unusable under session pressure or handoff needs. | Rebalance operational fit and survivability. |
| **Governance scaling collapse** | The report cannot explain why governance depth increased or decreased. | Reviewers cannot tell if process was intentionally light or accidentally skipped. | Add `ADAPTIVE GOVERNANCE FINDINGS`. |
| **Adaptive survivability erosion** | Governance either overburdens operators or under-protects future continuation. | Handoffs become bloated, or critical continuity context is missing. | Balance depth against workflow/context survivability. |

---

## 3. Over-Governance Patterns

| Pattern | Drift signal | Risk |
|---------|--------------|------|
| **Full-process reflex** | Every task invokes every layer regardless of risk. | Checklist fatigue and slower execution without better evidence. |
| **Ritual depth inflation** | More process is added because it looks mature. | Reports look safer while becoming less actionable. |
| **Low-risk escalation spam** | Minor reversible unknowns become HITL-heavy. | Human attention is wasted and escalation trust drops. |
| **Evidence duplication** | Multiple layers restate the same finding without adding decision value. | Signal-to-noise collapses. |
| **Process-over-outcome drift** | Completing governance becomes more important than preserving quality and clarity. | Execution survivability declines. |

---

## 4. Under-Governance Patterns

| Pattern | Drift signal | Risk |
|---------|--------------|------|
| **Criticality minimization** | High-impact source, freeze, business, or accessibility issues are treated as ordinary. | Critical work is under-protected. |
| **Shallow PASS on partial evidence** | PASS language exceeds source, rendered, build, or interaction evidence. | QA confidence becomes false. |
| **Authority shortcutting** | Human-owned decisions are handled as implementation choices. | Fake autonomy and hidden approval drift. |
| **Continuity-light handoff** | Long-session, recovery, or compressed context work lacks checkpoint depth. | Future operators cannot safely resume. |
| **Regression-risk flattening** | Shared selectors, tokens, includes, or breakpoints are treated as local edits. | Hidden blast radius grows. |

---

## 5. Context-Blind QA Patterns

| Pattern | Meaning |
|---------|---------|
| **Same QA matrix everywhere** | QA does not adapt to task type, evidence need, or criticality. |
| **Build-success substitution** | Build output is used as enough QA for visual, state, interaction, or accessibility risk. |
| **Visual-only confidence** | Screenshot or rendered visual review is treated as full frontend validation. |
| **Exhaustive irrelevant QA** | Unrelated checks are run while the actual risk receives little evidence. |
| **Missing adaptive QA depth** | The report never states why targeted, standard, elevated, or full relevant QA was chosen. |

---

## 6. Context-Blind Escalation Patterns

| Pattern | Meaning |
|---------|---------|
| **Escalation everywhere** | HITL is requested for low-impact, reversible, disclosed unknowns. |
| **Escalation nowhere** | The system avoids HITL even when source authority, approval, contradiction, or business meaning requires it. |
| **Escalation by discomfort** | The system escalates because it is uncertain, not because the uncertainty is material. |
| **Non-escalation by momentum** | Work continues because implementation is already moving. |
| **Escalation without depth choice** | The report says "escalate" without classifying disclosure, HITL recommended, HITL required, or blocked. |

---

## 7. Severity and Reporting Guidance

Adaptive drift severity should consider:

- consequence if the wrong depth is used;
- whether the task affects freeze, delivery, accessibility, source authority, business meaning, or continuity;
- reversibility of the work;
- strength of available evidence;
- whether process weight hides or clarifies the next safe action;
- whether future operators can understand the chosen depth.

`ADAPTIVE GOVERNANCE FINDINGS` should name:

- selected discipline layer;
- whether scaling was up, down, unchanged, or unknown;
- justification for the selected depth;
- drift pattern if mismatch is present;
- relation to QA depth, escalation depth, and survivability;
- SAFE UNKNOWN if depth cannot be justified.

---

## 8. SAFE UNKNOWN

Use **SAFE UNKNOWN** when adaptive drift cannot be ruled out.

Examples:

- unclear task criticality;
- unknown blast radius;
- uncertain source authority;
- unknown reversibility;
- missing evidence for QA depth;
- unclear escalation authority;
- context changed mid-task without depth reassessment.

**Action:** disclose the unknown, classify provisional risk, choose the safest proportional next step, and identify what evidence would confirm the appropriate governance layer.

---

## 9. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial adaptive drift taxonomy - context mismatch, static rigidity, over-governance, under-governance, disproportional QA, one-size-fits-all governance, context-blind escalation, operational rigidity, and survivability erosion; documentation only. |
