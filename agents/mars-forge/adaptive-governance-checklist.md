# Adaptive Governance Checklist - MARS Forge

**Status:** Forge overlay QA checklist for Website Factory adaptive governance.  
**Methodology:** [adaptive-governance.md](../../projects/mars-website-factory/adaptive-governance.md), [context-sensitive-discipline-model.md](../../projects/mars-website-factory/context-sensitive-discipline-model.md), [adaptive-drift-taxonomy.md](../../projects/mars-website-factory/adaptive-drift-taxonomy.md).  
**Not:** autonomous governance adaptation, runtime policy enforcement, universal rigor law, automatic QA-depth selection, or perfect contextual scaling.

Use this checklist when task criticality, QA depth, escalation level, governance weight, context mismatch, or survivability balancing affects the scope.

Record findings under **ADAPTIVE GOVERNANCE FINDINGS**.

---

## 1. Discipline Layer Selection

- [ ] Current task is classified as one primary discipline layer: lightweight-governance, operational-standard, elevated-risk, high-criticality, escalation-heavy, continuity-sensitive, or adaptive-review.
- [ ] Selected depth is justified by scope, blast radius, reversibility, evidence, authority, criticality, and continuity pressure.
- [ ] Lightweight governance is used only when the work is local, reversible, well-sourced, low-risk, and narrow in blast radius.
- [ ] Operational-standard governance is used for ordinary frontend slices with stable source and normal production risk.
- [ ] Elevated-risk governance is used when ambiguity, responsive/interaction/state/accessibility complexity, shared implementation risk, or regression risk is material.
- [ ] High-criticality governance is used when freeze, delivery, business meaning, source authority, accessibility trust, project identity, or release confidence may be affected.
- [ ] Escalation-heavy governance is used when authority, approval, contradiction, or human-owned decisions affect continuation.
- [ ] Continuity-sensitive governance is used when handoff, compressed context, recovery, freeze restoration, long session, or multi-agent continuity affects trust.

---

## 2. Proportional Rigor QA

- [ ] Rigor matches context instead of defaulting to maximum process or minimum process.
- [ ] Governance depth is proportional to task consequence and evidence need.
- [ ] Full process is not invoked for low-risk work without a named risk.
- [ ] Critical work is not allowed to proceed with lightweight process because it is faster.
- [ ] Governance scaling remains explainable in REPORT when depth affects confidence, escalation, freeze, or handoff.
- [ ] Process depth creates useful evidence or clarity, not only ceremony.
- [ ] Governance depth is revisited if new findings change the task risk profile.

---

## 3. Adaptive QA Depth

- [ ] QA depth is selected as targeted, standard, focused elevated, full relevant, or escalation QA.
- [ ] QA depth follows source evidence, rendered evidence, interaction/state/accessibility risk, responsive risk, and freeze/delivery consequence.
- [ ] Build success is not treated as enough QA when visual, interaction, state, accessibility, source, or responsive intent is in scope.
- [ ] Screenshot or rendered visual review is not treated as full frontend validation.
- [ ] Unrelated checklists are not run at full depth when they do not add evidence or decision value.
- [ ] Specialist QA is added when a specific elevated risk requires it.
- [ ] QA confidence boundaries remain visible when adaptive QA depth is partial or targeted.

---

## 4. Contextual Escalation QA

- [ ] Escalation level is classified as no escalation, disclosure only, HITL recommended, HITL required, or blocked.
- [ ] Low-impact, reversible unknowns are not escalated as if they were critical decisions.
- [ ] Human-owned decisions are not handled as implementation choices.
- [ ] Contradictions, missing approvals, authority ambiguity, and assumption chains are escalated or blocked when material.
- [ ] Escalation is tied to authority and consequence, not discomfort, habit, or implementation momentum.
- [ ] Escalation findings stay separate from QA confidence, risk weighting, and governance minimalism findings.

---

## 5. Governance Fit QA

- [ ] Governance depth fits project stage, task scope, operator capacity, evidence state, and current delivery pressure.
- [ ] The process preserves operational clarity instead of hiding the next safe action.
- [ ] Governance flexibility is used without weakening honesty, source authority, QA confidence, or HITL boundaries.
- [ ] Optional-depth, escalation-only, or deferred paths are used when they are safer and clearer than mandatory full depth.
- [ ] The selected governance path is readable to a future operator.
- [ ] If governance feels heavy, the report names the risk that justifies the weight or scales down.
- [ ] If governance feels light, the report confirms why criticality, ambiguity, and blast radius do not require more depth.

---

## 6. Process Scaling QA

- [ ] Scaling up is triggered by material ambiguity, contradiction, shared implementation risk, freeze/delivery risk, accessibility trust, business meaning, or continuity fragility.
- [ ] Scaling down is allowed when risk is low, source is clear, evidence need is narrow, and full depth would add noise.
- [ ] Adaptive-review is triggered when context changes mid-task.
- [ ] Process scaling is stated in operational language, not hidden behind generic "QA complete" or "process followed."
- [ ] Over-governance and under-governance are both treated as drift risks.
- [ ] Governance-context mismatch is named when the chosen depth does not fit the work.

---

## 7. Survivability Balancing QA

- [ ] Governance depth protects critical work without exhausting operator attention.
- [ ] Lightweight process does not erase source, freeze, delivery, or continuity evidence needed by future operators.
- [ ] Heavy process does not make the report less actionable or less readable.
- [ ] Handoff, checkpoint, recovery, or compressed-context work receives enough continuity depth.
- [ ] Findings remain prioritized so adaptive governance does not create equal-priority overload.
- [ ] SAFE UNKNOWN is used when the correct governance depth cannot be proven.

---

## 8. Drift Checks

- [ ] No governance-context mismatch.
- [ ] No static-rigidity drift.
- [ ] No over-governance.
- [ ] No under-governance.
- [ ] No disproportional QA.
- [ ] No adaptive-failure drift when context changes.
- [ ] No process inflation under low risk.
- [ ] No insufficient rigor under high risk.
- [ ] No one-size-fits-all governance.
- [ ] No context-blind escalation.
- [ ] No operational rigidity.
- [ ] No governance scaling collapse.
- [ ] No adaptive survivability erosion.

---

## 9. REPORT Format

Use this block when adaptive governance affects the scope:

```text
ADAPTIVE GOVERNANCE FINDINGS

Discipline layer: lightweight-governance | operational-standard | elevated-risk | high-criticality | escalation-heavy | continuity-sensitive | adaptive-review
Scaling decision: scale up | scale down | unchanged | reassess | SAFE UNKNOWN
Rationale: <scope / risk / uncertainty / reversibility / evidence / authority / continuity>
QA depth: targeted | standard | focused elevated | full relevant | escalation QA
Escalation depth: none | disclosure only | HITL recommended | HITL required | blocked
Drift checked: <none | governance-context mismatch | over-governance | under-governance | disproportional QA | ...>
Survivability balance: <why the chosen depth protects future operation without unnecessary process weight>
Disposition: PASS | PARTIAL | FAIL | SAFE UNKNOWN | HITL REQUIRED | BLOCKED
```

---

## 10. SAFE UNKNOWN

Record **SAFE UNKNOWN** when the selected governance depth cannot be justified from available context.

Required statement:

- what context is missing;
- which discipline layers are possible;
- what evidence would resolve the depth selection;
- whether continuation is lightweight-safe, standard-safe, elevated-review-needed, HITL-needed, blocked, or deferred.

---

*Documentation only - no runtime enforcement.*
