# Cognitive Load Checklist - MARS Forge

**Status:** Forge overlay QA checklist for Website Factory human cognitive load and review ergonomics.  
**Methodology:** [cognitive-load-governance.md](../../projects/mars-website-factory/cognitive-load-governance.md), [review-ergonomics-model.md](../../projects/mars-website-factory/review-ergonomics-model.md), [cognitive-drift-taxonomy.md](../../projects/mars-website-factory/cognitive-drift-taxonomy.md).  
**Not:** cognitive-monitoring AI, runtime attention system, automatic readability scoring, universal cognition law, or perfect readability guarantee.

Use this checklist when report length, finding volume, governance density, review fatigue, signal-to-noise clarity, reviewer sustainability, or governance readability affects implementation, QA, freeze, report, or handoff.

Record findings under **COGNITIVE LOAD FINDINGS**.

---

## 1. Review Layer Selection

- [ ] Current review density is classified as one primary layer: lightweight-review, operational-review, elevated-review, critical-review, escalation-review, continuity-review, or cognitive-survivability.
- [ ] Selected review layer is justified by scope, risk, uncertainty, evidence need, reversibility, freeze/delivery consequence, and reviewer burden.
- [ ] Lightweight review is used when work is local, reversible, low-risk, well-sourced, and easy to review.
- [ ] Operational review is used for normal Forge/foundation evidence, QA, and handoff clarity.
- [ ] Elevated review is used only when risk, uncertainty, source ambiguity, accessibility trust, business meaning, or fragility requires more evidence.
- [ ] Critical review leads with blockers and highest-risk signal before dense evidence.
- [ ] Escalation review names decision owner, trigger, unresolved question, and action required.
- [ ] Continuity review preserves state, unknowns, evidence boundary, and next safe action.
- [ ] Cognitive-survivability review is triggered when report density itself threatens review quality.

---

## 2. Review-Readability QA

- [ ] The report has a short critical-path summary before dense findings when findings are numerous.
- [ ] Findings state consequence and next action, not only category.
- [ ] PASS, PARTIAL, FAIL, SAFE UNKNOWN, HITL REQUIRED, BLOCKED, or deferred disposition is readable.
- [ ] Evidence, inference, assumption, and unknown are separated when they affect confidence.
- [ ] Governance terminology helps review instead of increasing cognitive friction.
- [ ] A future operator can understand the report without private memory.

---

## 3. Signal-to-Noise QA

- [ ] Highest-risk findings are easy to locate.
- [ ] Duplicate findings are consolidated, grouped, or cross-referenced.
- [ ] Low-value, cosmetic, reversible, or informational findings do not crowd critical-path risk.
- [ ] Report density matches consequence and uncertainty.
- [ ] Signal burial is named when important findings are hidden inside volume.
- [ ] Risk weighting is used when cognitive load affects prioritization.

---

## 4. Reviewer-Sustainability QA

- [ ] Review effort is sustainable across repeated sections, sessions, handoffs, and future operators.
- [ ] Governance depth does not require every layer to report at full density by default.
- [ ] Optional-depth, escalation-only, grouping, deferral, or focused review is used where proportional.
- [ ] The report preserves reviewer attention for source authority, freeze, delivery, trust, accessibility, strategic, or escalation risk.
- [ ] Review fatigue, governance exhaustion, or operator burnout risk is recorded when material.
- [ ] Cognitive-load reduction does not hide material evidence or under-protect critical work.

---

## 5. Governance-Readability QA

- [ ] Governance path is explainable: why this review depth, why these findings, why this disposition.
- [ ] Cross-layer references are minimal and purposeful.
- [ ] Report blocks do not repeat the same claim in different governance language.
- [ ] Dense evidence is placed after priority and action are clear.
- [ ] Compression preserves proof boundary, uncertainty, escalation, and next action.
- [ ] Governance readability is not inferred from professional formatting or long reports.

---

## 6. Cognitive-Survivability QA

- [ ] Reviewer attention is treated as finite.
- [ ] Critical signal remains visible under fatigue, handoff, and context compression.
- [ ] Review depth is proportional to risk and evidence need.
- [ ] Report length improves decision quality or continuity; otherwise it is reduced, grouped, or deferred.
- [ ] Cognitive overload is not solved by adding more unprioritized detail.
- [ ] SAFE UNKNOWN is used when review survivability cannot be established.

---

## 7. Drift Checks

Check for patterns from [cognitive-drift-taxonomy.md](../../projects/mars-website-factory/cognitive-drift-taxonomy.md):

- [ ] No reviewer fatigue.
- [ ] No cognitive overload.
- [ ] No unreadable reporting.
- [ ] No attention fragmentation.
- [ ] No governance exhaustion.
- [ ] No signal-to-noise erosion.
- [ ] No review paralysis.
- [ ] No operator burnout.
- [ ] No governance readability collapse.
- [ ] No information-density overload.
- [ ] No endless-report drift.
- [ ] No review-survivability erosion.
- [ ] No cognitive continuity failure.

Any material match requires **COGNITIVE LOAD FINDINGS**.

---

## 8. REPORT Format

Use this block when cognitive load or review ergonomics affects the scope:

```text
COGNITIVE LOAD FINDINGS

Review layer: lightweight-review | operational-review | elevated-review | critical-review | escalation-review | continuity-review | cognitive-survivability
Load driver: <finding volume / report density / terminology / evidence depth / escalation complexity / continuity pressure / reviewer fatigue>
Critical signal preserved: <what must remain easiest to see>
Review-readability QA: <clear / partial / unreadable / SAFE UNKNOWN>
Signal-to-noise QA: <clear / grouped / noisy / signal buried / SAFE UNKNOWN>
Reviewer sustainability: <sustainable / fatigue risk / overload risk / burnout risk / SAFE UNKNOWN>
Governance readability: <readable / dense but justified / too dense / unclear>
Cognitive drift checked: <none | reviewer fatigue | cognitive overload | signal burial | endless-report drift | ...>
Disposition: PASS | PARTIAL | FAIL | SAFE UNKNOWN | HITL REQUIRED | BLOCKED
```

---

## 9. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

- review layer cannot be selected;
- report readability cannot be established;
- critical signal may be buried;
- detail may overload rather than clarify;
- compression may hide material evidence or rationale;
- reviewer sustainability cannot be claimed;
- cognitive-load reduction may under-protect material risk.

Required statement:

- what readability or review-survivability evidence is missing;
- which review layers are possible;
- what signal must remain visible;
- what would justify more detail, less detail, grouping, deferral, or escalation;
- whether continuation is reviewable, reviewable with disclosure, elevated-review-needed, HITL-needed, blocked, or deferred.

---

## 10. Not Claimed

- No cognitive-monitoring AI.
- No runtime attention system.
- No automatic readability scoring.
- No universal cognition law.
- No perfect readability guarantee.
- No hiding of material risk for the sake of shorter reports.

---

*Documentation only - no runtime enforcement.*
