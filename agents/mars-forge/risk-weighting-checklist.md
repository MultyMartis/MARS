# Risk Weighting Checklist - MARS Forge

**Status:** human-supervised Forge QA checklist.  
**Purpose:** preserve severity proportionality, operational focus, escalation relevance, and signal-to-noise clarity across many governance findings.

**Factory methodology:** [`../../projects/mars-website-factory/governance-prioritization.md`](../../projects/mars-website-factory/governance-prioritization.md).  
**Risk model:** [`../../projects/mars-website-factory/risk-weighting-model.md`](../../projects/mars-website-factory/risk-weighting-model.md).  
**Prioritization taxonomy:** [`../../projects/mars-website-factory/prioritization-drift-taxonomy.md`](../../projects/mars-website-factory/prioritization-drift-taxonomy.md).

---

## 1. When to Run

Run this checklist when:

- Forge reporting includes many findings across several governance layers;
- critical risks are hard to distinguish from minor observations;
- escalation volume is rising;
- cosmetic, visual, or low-value findings are consuming review attention;
- PASS, PARTIAL, FAIL, SAFE UNKNOWN, HITL, or STOP depends on priority clarity;
- report length risks hiding the next safe action;
- governance noise may weaken QA confidence.

This checklist can be lightweight. It should clarify priority, not create another equal-priority report block.

---

## 2. Risk-Weighting QA

- [ ] Findings are classified by dominant risk layer: critical, operational, continuity, strategic, cosmetic/minor, escalation-only, or informational.
- [ ] Critical-risk findings are not buried inside ordinary category lists.
- [ ] Operational risks are distinguished from visual polish or cosmetic mismatch.
- [ ] Continuity risks are visible when handoff, compression, freeze-state memory, source lineage, or recovery would be affected.
- [ ] Strategic risks are visible when CTA role, proof hierarchy, business priority, stakeholder intent, or operational trust is affected.
- [ ] Cosmetic/minor findings are grouped, deferred, or demoted when they do not affect safe progress.

---

## 3. Prioritization QA

- [ ] The report makes the highest-risk items easy to find.
- [ ] Findings include consequence and required action, not only category.
- [ ] The top risks can be summarized in plain language.
- [ ] Review attention is allocated according to consequence, uncertainty, reversibility, and authority boundary.
- [ ] Low-value findings do not crowd out critical-path risks.

---

## 4. Severity Proportionality QA

- [ ] Severity labels match evidence and consequence.
- [ ] Minor or speculative issues are not inflated into critical findings.
- [ ] Critical findings explain why they can block freeze, delivery, trust, source authority, continuity, or human approval.
- [ ] Unknowns are weighted by consequence; low-impact unknowns do not automatically become blockers.
- [ ] `critical`, `blocker`, `HITL required`, and `STOP` language is reserved for real thresholds.

---

## 5. Escalation Relevance QA

- [ ] HITL requests are tied to human authority, contradiction, approval, waiver, strategic consequence, or material uncertainty.
- [ ] Low-value escalation is avoided when disclosure, scoped fix, or deferral is enough.
- [ ] Escalation-only concerns remain escalation-only until their trigger appears.
- [ ] Escalation fatigue risk is noted when too many non-critical requests are being sent upward.
- [ ] Human escalation findings remain separate from risk-weighting findings, but their urgency is weighted.

---

## 6. Signal-to-Noise QA

- [ ] Duplicate findings are consolidated or cross-referenced.
- [ ] Informational observations do not flood the main risk list.
- [ ] Cosmetic findings are grouped unless they affect visual, strategic, accessibility, or trust intent materially.
- [ ] The report preserves a short critical-path summary before dense evidence.
- [ ] "More warnings" is not treated as a safer outcome.

---

## 7. Operational-Focus QA

- [ ] The next safe action is clear: stop, fix before freeze, escalate, disclose, defer, or record only.
- [ ] Reviewers can see what must happen before freeze.
- [ ] PASS/PARTIAL/FAIL/SAFE UNKNOWN disposition reflects weighted risk.
- [ ] Governance attention is spent where risk, uncertainty, and consequence justify it.
- [ ] The report can survive handoff or compression without losing priority.

---

## 8. Drift Taxonomy QA

Check for patterns from [`prioritization-drift-taxonomy.md`](../../projects/mars-website-factory/prioritization-drift-taxonomy.md):

- [ ] Equal-priority overload.
- [ ] Minor-drift obsession.
- [ ] Critical-risk dilution.
- [ ] Severity inflation.
- [ ] Governance noise escalation.
- [ ] Low-value escalation.
- [ ] Review imbalance.
- [ ] Cosmetic-over-critical focus.
- [ ] Signal-to-noise collapse.
- [ ] False criticality.
- [ ] Disproportionate QA allocation.
- [ ] Escalation fatigue.
- [ ] Operational focus erosion.

Any material match requires **RISK WEIGHTING FINDINGS**.

---

## 9. Findings Format

Use this block when prioritization affects the result:

```text
RISK WEIGHTING FINDINGS - <section or block_id>

Highest-risk items:
- <critical / operational / continuity / strategic risk and required action>

Risk layers:
- Critical-risk:
- Operational-risk:
- Continuity-risk:
- Strategic-risk:
- Cosmetic/minor-risk:
- Escalation-only:
- Informational:

Severity proportionality:
- <whether severity is proportional or inflated/flattened>

Escalation relevance:
- <HITL required / HITL recommended / disclosure enough / no escalation>

Signal-to-noise:
- <what was grouped, deferred, or demoted to preserve focus>

Disposition: PASS | PARTIAL | FAIL | SAFE UNKNOWN | HITL REQUIRED | STOP
```

---

## 10. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

- the dominant risk layer cannot be determined;
- severity cannot be justified from evidence;
- escalation relevance is unclear;
- report volume hides critical risk;
- review allocation appears disproportionate;
- the next safe action cannot be identified.

**Action:** state the provisional weighting, name what evidence or human decision would resolve priority, and avoid presenting all findings as equal.

---

## 11. Not Claimed

- No autonomous risk AI.
- No scoring engine.
- No universal severity law.
- No perfect prioritization guarantee.
- No replacement for specialist governance, foundation QA, project authority, or HITL.
