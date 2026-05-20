# Temporal Evolution Checklist - MARS Forge

**Status:** **documented** - Forge overlay checklist for human-supervised temporal evolution and project drift QA.  
**Not:** autonomous maintenance AI, runtime drift detector, permanent stability guarantee, or automatic lifecycle enforcement.

**Parent governance:** [`../../projects/mars-website-factory/temporal-evolution-governance.md`](../../projects/mars-website-factory/temporal-evolution-governance.md).  
**Survivability model:** [`../../projects/mars-website-factory/project-drift-survivability-model.md`](../../projects/mars-website-factory/project-drift-survivability-model.md).  
**Drift taxonomy:** [`../../projects/mars-website-factory/evolution-drift-taxonomy.md`](../../projects/mars-website-factory/evolution-drift-taxonomy.md).

---

## 1. When To Run

Run this checklist before freeze, after adjacent edits, or during continuity checkpoints when any of the following affect the section, page, or delivery scope:

- freeze state or unfreeze reason;
- version lineage, supersede, branch, rollback, or archive use;
- repeated patches or local fixes;
- override accumulation;
- modernization of style, code, tokens, components, dependencies, or conventions;
- long-running multi-session work;
- architectural readability after many edits;
- project identity preservation;
- governance fatigue or skipped findings;
- QA claims about long-term continuity.

Record results as **TEMPORAL EVOLUTION FINDINGS**.

---

## 2. Freeze-State QA

- [ ] Frozen baseline, section, block, version, or report is named, or **SAFE UNKNOWN** is recorded.
- [ ] Current change preserves, reopens, supersedes, branches from, or intentionally diverges from the frozen state.
- [ ] Any unfreeze reason is explicit and tied to source, HITL, defect, or approved evolution.
- [ ] Shared selectors, tokens, includes, components, breakpoints, or JS hooks do not silently alter frozen scope.
- [ ] Freeze impact is checked before broad PASS or new freeze claim.
- [ ] Freeze-state ambiguity is escalated instead of resolved by assumption.

---

## 3. Version Lineage QA

- [ ] Active version and prior relevant versions are identified.
- [ ] Archive, V1, stale screenshots, prior reports, or old implementation are not treated as current authority without lineage.
- [ ] The current artifact states what it inherits, supersedes, preserves, or invalidates when material.
- [ ] Version mixing is classified as approved reuse, stale-source contamination, or **SAFE UNKNOWN**.
- [ ] Future operator can reconstruct lineage without this session's memory.

---

## 4. Governed Evolution QA

- [ ] Evolution reason is visible: defect, source update, HITL decision, approved modernization, regression fix, or scoped improvement.
- [ ] Local improvement does not silently change design identity, business intent, accessibility posture, implementation architecture, or source authority.
- [ ] Divergence from prior state is documented when material.
- [ ] Governance layers affected by the change are named.
- [ ] Change control is proportional to impact, not hidden inside "small polish."
- [ ] Controlled divergence remains explainable after handoff.

---

## 5. Controlled Override QA

- [ ] Overrides are bounded, justified, and connected to source, HITL, defect, or monitored risk.
- [ ] Repeated overrides around the same issue trigger a continuity checkpoint.
- [ ] Temporary patches have review, normalization, or acceptance posture.
- [ ] Override stack does not become stronger than canonical token/component/selector/path.
- [ ] Cumulative override pressure is named when local exceptions accumulate.

---

## 6. Iterative-Change QA

- [ ] Recent changes are reviewed for cumulative effect, not only latest diff correctness.
- [ ] Repeated fixes have not created inconsistent rhythm, hierarchy, behavior, accessibility, source interpretation, or strategy.
- [ ] Patch history is not treated as authority without source lineage.
- [ ] Local PASS does not hide cumulative drift.
- [ ] Architectural fragmentation is recorded when similar scopes now require different rules.
- [ ] Long-running work has a continuity checkpoint when many edits have accumulated.

---

## 7. Long-Term Continuity QA

- [ ] A future operator can identify the canonical current state.
- [ ] Open findings, deferred risks, waivers, monitored risks, and SAFE UNKNOWN items remain visible.
- [ ] The project can explain what changed since the last trusted state.
- [ ] Current state does not require private memory, archaeology, or agent transcript assumptions.
- [ ] Governance records preserve enough context to continue safely later.
- [ ] Continuity readability is PASS, PARTIAL, FAIL, or SAFE UNKNOWN.

---

## 8. Architectural Survivability QA

- [ ] Structure, ownership, dependencies, tokens, includes, breakpoints, and behavior remain understandable after the change.
- [ ] The change makes future scoped edits safe or identifies why they are risky.
- [ ] Architecture is not silently rewritten through local patches.
- [ ] Modernization does not replace identity without authority.
- [ ] Regression survivability is reviewed for frozen and adjacent scopes.
- [ ] Architectural erosion is recorded when future operators would struggle to explain the current state.

---

## 9. Drift Classification

Classify any issue using [`evolution-drift-taxonomy.md`](../../projects/mars-website-factory/evolution-drift-taxonomy.md):

- [ ] Gradual design erosion
- [ ] Freeze-state divergence
- [ ] Cumulative override decay
- [ ] Patch-history contamination
- [ ] Architectural fragmentation
- [ ] Governance fatigue
- [ ] Iterative inconsistency
- [ ] Modernization drift
- [ ] Silent identity mutation
- [ ] Continuity collapse
- [ ] Version-lineage loss
- [ ] Historical ambiguity
- [ ] Uncontrolled evolution

---

## 10. Reporting Block

Use this block in Forge reports when temporal evolution is in scope:

```text
TEMPORAL EVOLUTION FINDINGS - <section or scope>

Baseline / freeze state: <artifact / version / SAFE UNKNOWN>
Version lineage: PASS | PARTIAL | FAIL | SAFE UNKNOWN
Freeze-state integrity: PASS | PARTIAL | FAIL | SAFE UNKNOWN
Governed evolution: PASS | PARTIAL | FAIL | SAFE UNKNOWN
Controlled override pressure: PASS | PARTIAL | FAIL | SAFE UNKNOWN
Iterative-change accumulation: PASS | PARTIAL | FAIL | SAFE UNKNOWN
Long-term continuity: PASS | PARTIAL | FAIL | SAFE UNKNOWN
Architectural survivability: PASS | PARTIAL | FAIL | SAFE UNKNOWN

Drift pattern(s): <taxonomy names or none>
Continuity checkpoint: not needed | done | required | deferred | HITL required
Disposition: PASS | PARTIAL | FAIL | MONITORED RISK | HITL REQUIRED | STOP
Evidence / unknowns: <short scope>
```

Keep this separate from `IMPLEMENTATION RELIABILITY FINDINGS`, `SOURCE LINEAGE FINDINGS`, `QA CONFIDENCE FINDINGS`, and `STRATEGIC INTENT FINDINGS`.

---

## 11. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

- freeze baseline is missing;
- version lineage is unclear;
- unfreeze or divergence rationale is absent;
- override history cannot be explained;
- patch history may be contaminating current decisions;
- modernization authority is missing;
- cumulative changes have not been reviewed;
- architectural survivability cannot be established;
- governance checkpoint was skipped but continuity is claimed.

**Action:** state what is unknown, what would resolve it, and whether continuation is safe with disclosure, continuity checkpoint required, HITL required, blocked, or monitored risk.

---

## 12. Non-Goals

- Do not redesign Triumph or any other project.
- Do not invent autonomous maintenance AI.
- Do not create runtime drift engines.
- Do not define universal frontend lifecycle law.
- Do not claim permanent architectural stability.
- Do not treat local "improvement" as identity authority without lineage.

---

*Documentation only - no runtime enforcement.*
