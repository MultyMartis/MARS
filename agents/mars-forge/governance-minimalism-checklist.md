# Governance Minimalism Checklist - MARS Forge

**Status:** human-supervised Forge QA checklist.  
**Purpose:** prevent governance bloat, checklist fatigue, process overload, and methodology collapse through weight.

**Factory methodology:** [`../../projects/mars-website-factory/governance-minimalism.md`](../../projects/mars-website-factory/governance-minimalism.md).  
**Complexity model:** [`../../projects/mars-website-factory/complexity-control-model.md`](../../projects/mars-website-factory/complexity-control-model.md).  
**Bloat taxonomy:** [`../../projects/mars-website-factory/governance-bloat-taxonomy.md`](../../projects/mars-website-factory/governance-bloat-taxonomy.md).

---

## 1. When to Run

Run this checklist when:

- Forge reporting now includes many governance layers;
- the operator cannot easily tell which findings are essential;
- checklist work is slowing execution without clear value;
- governance seems to duplicate itself;
- PASS/PARTIAL/SAFE UNKNOWN language is becoming ritualized;
- handoff or compressed context would struggle to preserve the governance record;
- a task risks governance-over-execution.

This checklist can be **lightweight**. It should not become another source of bloat.

---

## 2. Governance Proportionality QA

- [ ] Active governance layers match actual task risk, ambiguity, evidence gaps, and blast radius.
- [ ] Full-depth review is reserved for active risk, not applied mechanically to every concern.
- [ ] Low-risk scope uses essential or lightweight validation unless a threshold is crossed.
- [ ] Escalation-only layers remain escalation-only until their trigger appears.
- [ ] Optional-depth layers are not treated as mandatory by default.

---

## 3. Cognitive-Load QA

- [ ] The operator can name the current governance path in plain language.
- [ ] Essential blockers are distinguishable from optional observations.
- [ ] Findings are prioritized enough for a future operator to know the next safe action.
- [ ] Report length and checklist density do not hide the real risk.
- [ ] The governance record can survive handoff or compression without losing priority.

---

## 4. Operational-Readability QA

- [ ] The report explains why each invoked governance layer mattered.
- [ ] Duplicate findings are consolidated or explicitly cross-referenced.
- [ ] A future operator can tell what was checked, what was deferred, and what remains unknown.
- [ ] Governance language supports execution, freeze, escalation, or handoff decisions.
- [ ] The method remains readable without private context.

---

## 5. Checklist-Fatigue QA

- [ ] Checklist items produce evidence or decision value, not only ceremony.
- [ ] Repeated items across adjacent layers are not copied into redundant findings.
- [ ] A short scoped note is used when a full subsection would add no value.
- [ ] "All checklists completed" is not used as a substitute for evidence.
- [ ] SAFE UNKNOWN is not hidden by dense checklist completion.

---

## 6. Process-Survivability QA

- [ ] Governance depth preserves execution speed appropriate to risk.
- [ ] The current method can be resumed by another operator.
- [ ] Long-term governance remains usable after fatigue, future patches, or project handoff.
- [ ] Complexity added in this session has a named purpose and boundary.
- [ ] Governance does not become the primary artifact instead of the frontend work and evidence.

---

## 7. Governance-to-Value QA

- [ ] Each added governance step reduces a named risk or improves clarity.
- [ ] The effort required is proportionate to the value produced.
- [ ] The operator can identify when deeper review would be justified.
- [ ] The current scope does not require universal depth everywhere.
- [ ] The report states whether governance depth was essential, lightweight, escalation-only, optional-depth, deferred, or out of scope.

---

## 8. Findings Format

Use this block when material:

```text
GOVERNANCE MINIMALISM FINDINGS — <scope>

Proportionality:
- <essential / lightweight / escalation-only / optional-depth / deferred / out-of-scope>

Cognitive load:
- <readability, priority, checklist fatigue, or SAFE UNKNOWN note>

Governance-to-value:
- <why depth is justified or why depth is reduced>

Disposition: PASS | PARTIAL | FAIL | SAFE UNKNOWN
```

---

## 9. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

- the value of an added governance step cannot be justified;
- it is unclear whether full depth or escalation-only logic is appropriate;
- checklist volume hides priority;
- findings are too dense to support handoff;
- the governance path cannot be explained by the operator;
- process slowdown is visible but risk reduction is not.

**Action:** reduce the current pass to essential / lightweight / escalation-only / optional-depth where possible, or escalate when governance weight blocks reliable freeze, PASS, or handoff claims.

---

## 10. Not Claimed

- No autonomous governance simplification.
- No automatic pruning or scoring.
- No universal minimalism law.
- No removal of existing Website Factory governance.
- No perfect balance guarantee.
