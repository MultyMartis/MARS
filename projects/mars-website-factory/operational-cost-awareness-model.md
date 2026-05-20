# Operational Cost Awareness Model - Website Factory

**Status:** documented Website Factory model for human-supervised governance cost classification.  
**Not:** runtime cost engine, automatic budget optimizer, financial accounting model, universal cost law, or perfect efficiency calculator.

**Parent layer:** [governance-economics.md](governance-economics.md).  
**Companion taxonomy:** [governance-cost-drift-taxonomy.md](governance-cost-drift-taxonomy.md).  
**Forge checklist:** [`../../agents/mars-forge/governance-economics-checklist.md`](../../agents/mars-forge/governance-economics-checklist.md).

---

## 1. Purpose

The Operational Cost Awareness Model gives Website Factory operators a shared vocabulary for classifying the cost of governance depth.

It does not assign numeric budgets. It helps answer:

- how much governance effort is appropriate for this task;
- what kind of validation cost is being added;
- whether review allocation is proportional;
- whether survivability protection remains sustainable;
- whether governance depth creates enough value density.

The model exists because governance can be correct in intent and still economically unsustainable in operation.

---

## 2. Cost Layers

| Layer | Use when | Cost posture |
|-------|----------|--------------|
| **lightweight-governance-cost** | Scope is local, reversible, well-sourced, low-risk, and narrow in blast radius. | Keep checks targeted; avoid full report expansion unless a risk emerges. |
| **operational-standard-cost** | Ordinary frontend slice with stable source, normal QA needs, and routine handoff. | Use standard Forge/foundation checks with concise evidence and scoped findings. |
| **elevated-review-cost** | Ambiguity, shared implementation risk, responsive/interaction/state/accessibility complexity, source interpretation, or regression risk is material. | Add specialist checks only where they produce evidence or reduce material uncertainty. |
| **high-criticality-cost** | Freeze, delivery, business meaning, source authority, accessibility trust, project identity, or release confidence may be affected. | Higher cost is justified when evidence, escalation, and survivability value are explicit. |
| **continuity-preservation-cost** | Handoff, compression, long session, recovery, freeze restoration, organizational memory, or future resumability affects trust. | Invest in checkpoints and traceability, but prevent continuity documentation from becoming the work. |
| **escalation-cost** | Human-owned decisions, contradictions, approval gaps, unresolved authority, or high-impact SAFE UNKNOWN affect continuation. | Escalation overhead is justified by decision ownership; avoid escalation spam for low-value uncertainty. |
| **governance-sustainability** | Governance volume, checklist fatigue, report length, review burden, or long-term repeatability threatens operation. | Scale depth, consolidate findings, defer low-value checks, and preserve value density. |

---

## 3. Governance Cost Scaling

Governance cost should scale with:

- **risk consequence** - what can break if the issue is missed;
- **uncertainty** - how much source, evidence, authority, or context is missing;
- **reversibility** - how hard it is to correct later;
- **blast radius** - whether the change affects one section, shared tokens, includes, breakpoints, scripts, or project identity;
- **evidence need** - whether stronger validation would change a decision;
- **continuity pressure** - whether future operators need durable checkpoints;
- **review burden** - whether attention is being spent on high-value concerns;
- **operational timing** - whether cost is acceptable for the current stage, freeze state, or delivery pressure.

Scaling up is justified when the added cost produces material risk reduction, evidence, decision clarity, escalation clarity, or continuity survivability.

Scaling down is justified when additional process produces low-value repetition, duplicates another layer, slows execution without new evidence, or weakens report readability.

---

## 4. Proportional Investment

Proportional governance investment means:

| Question | Proportionality signal |
|----------|------------------------|
| What value does this cost buy? | Evidence, risk reduction, decision clarity, source authority, QA confidence, handoff stability, or survivability. |
| Is the risk present or theoretical? | Present risks justify cost more strongly than generic possible risks. |
| Would more validation change the decision? | If no, additional validation may be low-value overhead. |
| Can a cheaper governance path preserve enough safety? | Targeted, lightweight, escalation-only, optional-depth, or deferred handling may be sufficient. |
| Is review attention being preserved? | High-value findings stay visible instead of being buried in process volume. |
| Can future operators use the record? | Documentation cost is justified when it improves continuation, freeze trust, or recovery. |

**Rule:** expensive governance should leave behind expensive-value evidence: clearer risk, stronger confidence, resolved authority, safer freeze, better handoff, or durable lesson.

---

## 5. Validation Economics

Validation has cost in:

- setup time;
- source reading;
- rendered review;
- build or tool execution;
- viewport/state coverage;
- cross-layer interpretation;
- report writing;
- reviewer attention;
- escalation coordination;
- future handoff complexity.

Validation is economically healthy when:

- each check answers a distinct question;
- evidence boundaries remain visible;
- expensive checks are tied to material consequence;
- QA depth follows evidence need and risk;
- repeated checks are consolidated;
- PASS/PARTIAL/FAIL language stays scoped;
- unknowns are disclosed without triggering unlimited process by default.

Validation is economically unhealthy when:

- every possible check is treated as mandatory;
- build, source, screenshot, rendered, and interaction evidence are repeated without decision value;
- report length grows faster than confidence;
- QA becomes ceremony rather than evidence;
- expensive review is spent on low-impact reversible details.

---

## 6. Review Allocation

Reviewer attention is a limited operational resource.

Allocate review effort toward:

- high consequence;
- high uncertainty;
- irreversible or hard-to-reverse changes;
- shared implementation dependencies;
- source authority ambiguity;
- accessibility trust;
- business intent and conversion hierarchy;
- freeze/delivery risk;
- continuity and handoff fragility.

Allocate less review effort toward:

- local reversible changes;
- well-sourced low-risk edits;
- duplicated findings;
- purely informational observations;
- cosmetic drift with no material consequence;
- concerns already covered by stronger evidence elsewhere.

**Rule:** review allocation should make the most important risks easier to see, not only make the report larger.

---

## 7. Operational Sustainability

Operational sustainability means governance can be repeated across:

- many sections;
- long sessions;
- context compression;
- future operators;
- project handoffs;
- maintenance passes;
- reference-case reuse;
- repeated QA/freeze cycles.

Sustainable governance:

- keeps entry points navigable;
- uses report blocks only when they create decision value;
- prevents validation-cost explosion;
- consolidates duplicated findings;
- reserves full depth for material risk;
- treats operator attention as finite;
- preserves enough continuity without turning every session into an archive exercise.

Unsustainable governance may look mature because it has many layers, but it becomes operationally fragile when cost grows faster than value.

---

## 8. Governance Efficiency Balancing

Use this balancing statement in reports when economics affects scope:

```text
Operational cost layer: lightweight-governance-cost | operational-standard-cost | elevated-review-cost | high-criticality-cost | continuity-preservation-cost | escalation-cost | governance-sustainability
Cost driver: <risk / uncertainty / evidence need / review burden / continuity / escalation / sustainability>
Investment rationale: <why this depth is justified>
Efficiency check: <what was targeted, consolidated, deferred, or kept lightweight>
Survivability-to-cost balance: <why continuity protection is enough without becoming excessive>
Disposition: PASS | PARTIAL | FAIL | SAFE UNKNOWN
```

---

## 9. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

- the cost layer cannot be classified;
- governance depth may be too expensive for the value produced;
- scaling down might under-protect a material risk;
- validation economics are unclear;
- review allocation appears imbalanced but evidence is incomplete;
- continuity preservation cost may exceed operational benefit;
- escalation cost is unclear because authority or consequence is unresolved.

**Action:** disclose the unknown, choose the safest provisional cost layer, and name what evidence would justify keeping, increasing, reducing, or deferring governance depth.

---

*Documentation only - no runtime enforcement or automatic cost optimization.*
