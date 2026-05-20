# Review Ergonomics Model

**Status:** **documented** - Website Factory human-supervised review-density and cognitive-survivability model only.  
**Parent layer:** [cognitive-load-governance.md](cognitive-load-governance.md).  
**Not:** cognitive-monitoring AI, universal reviewer-capacity model, automatic report optimizer, or perfect readability guarantee.

---

## 1. Purpose

The Review Ergonomics Model defines how Website Factory governance selects review density, signal prioritization, attention allocation, governance readability, and sustainable cognition for human reviewers.

It exists to prevent a governance system from becoming technically thorough but operationally unreadable.

---

## 2. Review Layers

| Layer | Use when | Required ergonomic posture |
|-------|----------|----------------------------|
| **Lightweight-review layer** | Work is local, reversible, well-sourced, low-risk, and low-ambiguity | Short summary, grouped observations, no dense specialist report unless material risk appears. |
| **Operational-review layer** | Normal Forge or Website Factory work needs standard evidence, QA, and handoff clarity | Findings stay scoped, prioritized, and tied to next action. |
| **Elevated-review layer** | Risk, uncertainty, source ambiguity, accessibility trust, business meaning, or implementation fragility increases | Add evidence depth, but preserve critical-path summary and proportional density. |
| **Critical-review layer** | Freeze, delivery, source authority, safety, accessibility trust, business consequence, or project identity may be blocked | Highest-risk signal appears first; evidence supports decision without burying the blocker. |
| **Escalation-review layer** | HITL, waiver, contradiction, approval, or authority decision is required | Escalation trigger, decision owner, evidence boundary, and unresolved question remain visible. |
| **Continuity-review layer** | Handoff, compression, recovery, long-session context, freeze memory, or future resumability is material | Preserve state, evidence, unknowns, and next safe action in readable form. |
| **Cognitive-survivability layer** | Report density, terminology, finding volume, or review fatigue threatens usable review | Compress, group, prioritize, summarize, or escalate until review can survive. |

---

## 3. Review Density

Review density is the amount of evidence, findings, terminology, cross-links, and governance explanation placed in front of a human reviewer.

Density should increase when:

- consequence is high;
- evidence is weak, partial, or contradictory;
- source authority is unclear;
- freeze, delivery, trust, accessibility, or strategic intent may be affected;
- future handoff depends on preserving exact rationale.

Density should decrease, group, or defer when:

- findings are cosmetic, duplicated, low-risk, or reversible;
- evidence repeats another layer without adding decision value;
- report volume hides the next safe action;
- reviewer attention should be reserved for higher-risk items.

**Rule:** review density is not maturity. Density is useful only when it improves decision quality, confidence honesty, escalation clarity, or continuity.

---

## 4. Signal Prioritization

Signal prioritization protects the reviewer's ability to see what matters first.

High-priority signal includes:

- blockers to freeze, delivery, approval, or safe continuation;
- source authority contradictions;
- high-impact SAFE UNKNOWN;
- accessibility or trust risks;
- strategic intent, CTA, proof, or business meaning drift;
- workflow, checkpoint, recovery, or continuity failure;
- evidence gaps that change confidence or escalation posture.

Low-priority signal should be grouped or demoted when it is:

- cosmetic and reversible;
- already covered by another finding;
- informational only;
- too speculative for action;
- unrelated to the current review decision.

---

## 5. Attention Allocation

Reviewer attention is finite. This model treats attention as an operational resource that must be allocated deliberately.

| Attention target | Allocation rule |
|------------------|-----------------|
| Critical risk | Place before dense evidence and category detail. |
| Material uncertainty | Pair with consequence and resolver. |
| Escalation | Name decision owner, trigger, and required human action. |
| Evidence | Keep enough proof to support confidence without repeating low-value detail. |
| Continuity | Preserve the next safe action and unresolved unknowns. |
| Minor observations | Group, defer, or report as informational unless they affect trust, accessibility, strategy, or freeze. |

---

## 6. Governance Readability

Governance readability requires:

- short critical-path summary before detailed findings;
- explicit disposition: PASS, PARTIAL, FAIL, SAFE UNKNOWN, HITL REQUIRED, BLOCKED, or deferred;
- finding language that states consequence and action, not only category;
- visible separation between evidence, inference, assumption, and unknown;
- scoped report blocks instead of repeated full-system narration;
- terminology that helps review rather than performing authority.

Unreadable governance is drift even when its details are individually correct.

---

## 7. Sustainable Cognition

Sustainable cognition means reviewers can repeat the process without quality erosion.

The model protects sustainable cognition by:

- limiting mandatory depth to material risk;
- using lightweight and operational review when sufficient;
- reserving critical and escalation review for real thresholds;
- compressing or grouping low-value findings;
- keeping cross-layer references minimal and purposeful;
- preserving explicit SAFE UNKNOWN rather than forcing exhaustive closure.

---

## 8. Review Layer Selection

Before reporting, select the lightest layer that still protects the risk:

| Question | Selection meaning |
|----------|-------------------|
| What decision must the reviewer make? | Determines whether summary, evidence, escalation, or freeze posture leads. |
| What can break if the reviewer misses the signal? | Determines criticality and density. |
| What evidence is needed to support confidence? | Determines proof depth. |
| What can be grouped without hiding risk? | Reduces noise. |
| What must survive handoff or compression? | Determines continuity density. |
| Is the reviewer being asked to process too much? | Triggers cognitive-survivability layer. |

---

## 9. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

- review layer cannot be selected;
- density may be too high or too low;
- critical signal may be buried;
- compression may hide evidence or rationale;
- attention allocation is unclear;
- reviewer sustainability cannot be claimed.

**Action:** state the possible review layers, name the risk that determines depth, preserve the highest-value signal, and choose whether to summarize, expand, group, defer, escalate, or stop.

---

*Documentation only - no runtime enforcement.*
