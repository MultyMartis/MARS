# Reasoning Visibility Checklist - MARS Forge

**Status:** human-supervised Forge QA checklist.  
**Purpose:** preserve reasoning visibility, decision traceability, escalation explainability, prioritization transparency, uncertainty visibility, assumption disclosure, and traceable conclusions.

**Factory governance:** [`../../projects/mars-website-factory/decision-transparency-governance.md`](../../projects/mars-website-factory/decision-transparency-governance.md).  
**Reasoning model:** [`../../projects/mars-website-factory/reasoning-visibility-model.md`](../../projects/mars-website-factory/reasoning-visibility-model.md).  
**Reasoning taxonomy:** [`../../projects/mars-website-factory/reasoning-drift-taxonomy.md`](../../projects/mars-website-factory/reasoning-drift-taxonomy.md).

Record findings as **REASONING VISIBILITY FINDINGS** in the Forge execution REPORT when any item is partial, failed, unknown, HITL-recommended, HITL-required, blocked, or affects conclusion readability.

---

## 1. When to Run

Run this checklist when:

- Forge reporting produces recommendations, conclusions, PASS/PARTIAL/FAIL, SAFE UNKNOWN, HITL, STOP, freeze, or deferral decisions;
- prioritization affects action order;
- escalation or non-escalation requires explanation;
- assumptions, uncertainty, or tradeoffs affect the conclusion;
- many governance findings need a readable decision path;
- compressed context or handoff must preserve why a decision was made.

This checklist should expose reviewable rationale. It must not request hidden chain-of-thought.

---

## 2. Reasoning-Visibility QA

- [ ] Material conclusions name the evidence they rely on.
- [ ] Evidence is interpreted as observed, inferred, assumed, contradictory, partial, stale, or unknown where relevant.
- [ ] Reasoning is visible as reviewable rationale, not private deliberation.
- [ ] Conclusions do not exceed evidence, interpretation, and uncertainty boundaries.
- [ ] A future operator can reconstruct the decision without guessing.

---

## 3. Prioritization-Traceability QA

- [ ] Priority order is explained when findings are numerous or severity-sensitive.
- [ ] Critical, operational, continuity, strategic, cosmetic/minor, escalation-only, and informational findings are distinguishable when relevant.
- [ ] High-priority findings explain consequence, not only category.
- [ ] Low-priority findings are grouped, deferred, or marked informational when appropriate.
- [ ] `RISK WEIGHTING FINDINGS` remain separate but their rationale is readable.

---

## 4. Escalation-Explainability QA

- [ ] Escalation trigger is named: ambiguity, contradiction, approval boundary, assumption chain, evidence gap, source priority, or stop condition.
- [ ] Non-escalation is explained when consequence, uncertainty, or authority sensitivity is material.
- [ ] Decision owner is visible: source, governance, operator, HITL, or unknown.
- [ ] HITL, STOP, waiver, deferral, or continuation is not asserted without rationale.
- [ ] `HUMAN ESCALATION FINDINGS` remain separate but their decision path is readable.

---

## 5. Uncertainty-Visibility QA

- [ ] Known unknowns are visible before conclusion or freeze.
- [ ] Uncertainty explains why it matters and what would resolve it.
- [ ] SAFE UNKNOWN is paired with action: continue with disclosure, verify further, defer, HITL, block, or STOP.
- [ ] Confidence does not hide evidence gaps.
- [ ] Summaries do not compress uncertainty into vague "risk" language.

---

## 6. Assumption-Disclosure QA

- [ ] Material assumptions are named.
- [ ] Assumptions are not presented as source facts, QA evidence, or human decisions.
- [ ] Assumption chains are visible when multiple guesses affect one conclusion.
- [ ] Tradeoffs are disclosed when one risk is accepted to reduce another.
- [ ] Hidden assumptions trigger **REASONING VISIBILITY FINDINGS** or escalation when material.

---

## 7. Traceable-Conclusion QA

- [ ] Conclusion states disposition: PASS, PARTIAL, FAIL, SAFE UNKNOWN, HITL recommended, HITL required, blocked, STOP, defer, or proceed.
- [ ] Conclusion includes proof boundary or scope boundary.
- [ ] Conclusion names next action.
- [ ] Conclusion can be reconstructed from evidence -> interpretation -> priority -> escalation -> uncertainty -> action.
- [ ] Conclusion readability survives handoff or compressed context.

---

## 8. Drift Taxonomy QA

Check for patterns from [`reasoning-drift-taxonomy.md`](../../projects/mars-website-factory/reasoning-drift-taxonomy.md):

- [ ] Opaque reasoning.
- [ ] Hidden assumptions.
- [ ] Unexplained escalation.
- [ ] Invisible prioritization logic.
- [ ] Conclusion-without-traceability.
- [ ] Silent tradeoff drift.
- [ ] Unverifiable recommendation.
- [ ] Governance black-boxing.
- [ ] Reasoning collapse.
- [ ] Decision ambiguity.
- [ ] Implicit conclusion inflation.
- [ ] Confidence opacity.
- [ ] Traceability erosion.

Any material match requires **REASONING VISIBILITY FINDINGS**.

---

## 9. Findings Format

Use this block when reasoning visibility affects the result:

```text
REASONING VISIBILITY FINDINGS - <section or block_id>

Decision / conclusion:
- <recommendation, PASS/PARTIAL/FAIL, HITL, STOP, deferral, freeze posture, or other conclusion>

Visible rationale:
- Evidence layer:
- Interpretation layer:
- Prioritization layer:
- Escalation layer:
- Conclusion layer:
- Uncertainty layer:
- Traceability layer:

Assumptions / tradeoffs:
- <named assumptions, accepted tradeoffs, or none>

Drift taxonomy:
- <reasoning drift pattern or none>

Disposition: PASS | PARTIAL | FAIL | SAFE UNKNOWN | HITL REQUIRED | STOP
Next action:
- <proceed / verify further / disclose partial / defer / escalate / block / stop>
```

---

## 10. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

- evidence path is missing;
- interpretation is unclear;
- assumptions or tradeoffs may be hidden;
- prioritization logic is invisible;
- escalation rationale is absent;
- conclusion cannot be reconstructed;
- compressed context may have removed reasoning.

**Action:** state the missing reasoning layer, name what would restore traceability, and avoid presenting an opaque verdict as review-ready.

---

## 11. Not Claimed

- No hidden chain-of-thought exposure.
- No autonomous reasoning engine.
- No automatic explainability scoring.
- No universal transparency law.
- No perfect explainability guarantee.
- No replacement for specialist governance, foundation QA, project authority, or HITL.
