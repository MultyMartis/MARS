# MARS Forge - Reconstruction Fidelity Checklist

**Status:** **overlay checklist** for human-supervised reconstruction-fidelity QA.  
**Not:** automated design reading, runtime fidelity scoring, screenshot diff, computer vision, universal reconstruction law, or substitute for foundation QA.

**Factory methodology:** [`../../projects/mars-website-factory/design-intent-transfer-governance.md`](../../projects/mars-website-factory/design-intent-transfer-governance.md).  
**Fidelity model:** [`../../projects/mars-website-factory/reconstruction-fidelity-model.md`](../../projects/mars-website-factory/reconstruction-fidelity-model.md).  
**Drift taxonomy:** [`../../projects/mars-website-factory/reconstruction-drift-taxonomy.md`](../../projects/mars-website-factory/reconstruction-drift-taxonomy.md).

---

## 1. When to Run

Run this checklist:

- after active source authority and semantic source lock are established;
- when a section is reconstructed from screenshots, implementation pack notes, existing code, or prior source artifacts;
- alongside source interpretation, visual reconciliation, responsive intent, strategic intent, QA confidence, and trust calibration when fidelity claims affect freeze;
- before declaring source-to-build fidelity, section PASS, or freeze.

This checklist does not authorize redesign, hidden approximation, invented mobile behavior, or perfect fidelity claims.

---

## 2. Reconstruction Fidelity QA

- [ ] **Source authority named** - active source path, version, screen, section, and `block_id` are visible.
- [ ] **Source transfer classified** - decisions are observed, inferred, assumed, approximated, unknown, or contradictory.
- [ ] **Structural fidelity checked** - section boundaries, wrappers, cards, lists, proof groups, CTAs, and includes preserve source organization.
- [ ] **Hierarchy fidelity checked** - primary/supporting relationships, CTA priority, proof weight, media dominance, and decorative elements remain source-aligned.
- [ ] **Semantic transfer checked** - meaning, entity count, CTA role, proof role, and section purpose survive reconstruction.
- [ ] **Compositional transfer checked** - grouping, focal path, balance, density, rhythm, and visual clusters are not reinterpreted by taste or template habit.
- [ ] **Responsive fidelity checked** - viewport adaptation preserves intent where source or rules exist; missing source is disclosed.
- [ ] **Approximation boundaries named** - missing source, raster, responsive, token, asset, structural, interaction/state, or evidence boundaries are visible.
- [ ] **Reconstruction confidence calibrated** - fidelity claim matches evidence strength and proof boundary.
- [ ] **Reconstruction traceability preserved** - future operators can tell why the build claims fidelity and where limits remain.

---

## 3. Model Layer Gate

Use [`reconstruction-fidelity-model.md`](../../projects/mars-website-factory/reconstruction-fidelity-model.md):

- [ ] **Source-authority layer** - active source and priority are not ambiguous.
- [ ] **Structural-fidelity layer** - build structure does not reinterpret source organization.
- [ ] **Hierarchy-fidelity layer** - priority relationships survive.
- [ ] **Responsive-fidelity layer** - breakpoints preserve intent or disclose approximation.
- [ ] **Approximation layer** - compromises are visible and bounded.
- [ ] **Reconstruction-confidence layer** - confidence is high, moderate, partial, approximation disclosed, SAFE UNKNOWN, or contradictory.
- [ ] **Fidelity-survivability layer** - source refs, evidence boundaries, approximation notes, and unresolved risks survive in REPORT.

Any material layer gap requires `RECONSTRUCTION FIDELITY FINDINGS`.

---

## 4. Drift Taxonomy Gate

Check for and record patterns from [`reconstruction-drift-taxonomy.md`](../../projects/mars-website-factory/reconstruction-drift-taxonomy.md):

- [ ] Reconstruction drift.
- [ ] Fidelity illusion.
- [ ] Approximation contamination.
- [ ] Source-transfer degradation.
- [ ] Visual-intent loss.
- [ ] Semantic reconstruction mismatch.
- [ ] Layout reinterpretation drift.
- [ ] Hierarchy fidelity collapse.
- [ ] Reconstruction overconfidence.
- [ ] Source-to-build divergence.
- [ ] Screenshot mimicry drift.
- [ ] Approximation opacity.
- [ ] Fidelity survivability erosion.

Any material match requires explicit finding, confidence adjustment, or escalation.

---

## 5. Approximation Transparency QA

- [ ] Approximation is not hidden behind "matches source" or "looks close."
- [ ] Approximation reason is named: missing source, ambiguous source, low-resolution raster, missing breakpoint, token gap, asset gap, structural constraint, or evidence gap.
- [ ] Approximation scope is bounded: visual only, structural, responsive, semantic, interaction/state, asset, token, or QA evidence.
- [ ] Approximation does not silently become reusable source truth.
- [ ] Approximation is paired with action: disclose, defer, HITL recommended, HITL required, blocked, or stopped.

---

## 6. Escalation Boundary

Stop or escalate when reconstruction would:

- claim high fidelity from weak, ambiguous, missing, or contradictory source;
- preserve visual resemblance while changing meaning, CTA role, proof role, hierarchy, or source grouping;
- invent mobile / tablet behavior without source authority;
- treat an approximation as exact source fidelity;
- prefer existing code, template habit, or old exports over active source;
- freeze a section without source-to-build traceability;
- hide SAFE UNKNOWN behind polished output.

Use **PARTIAL - reconstruction fidelity**, **SAFE UNKNOWN**, **HITL recommended**, **HITL required**, **blocked**, or **STOP** rather than silent confidence.

---

## 7. REPORT Block

Use this block when reconstruction fidelity affects implementation:

```text
RECONSTRUCTION FIDELITY FINDINGS - <section or block_id> - <source ref>

Source transfer:
- <active source, observed/inferred/assumed/unknown decisions>

Fidelity layers:
- Source authority:
- Structural fidelity:
- Hierarchy fidelity:
- Semantic transfer:
- Compositional transfer:
- Responsive fidelity:

Approximation transparency:
- <approximation boundary, reason, and disclosure>

Drift taxonomy:
- <patterns found, if any>

Confidence:
- <high source-aligned | moderate source-aligned | partial fidelity | approximation disclosed | SAFE UNKNOWN | contradictory>

Disposition: PASS | PARTIAL | FAIL | SAFE UNKNOWN | HITL REQUIRED | STOP
Action: proceed | tune | approximate with disclosure | defer | request source | structure escalation | block
Evidence: <paths, source artifacts, viewport notes, rendered notes>
```

---

## 8. Not Claimed

- No autonomous design-reading AI.
- No runtime fidelity scoring.
- No automatic source-to-build validator.
- No universal reconstruction law.
- No perfect fidelity claim.
- No authority to redesign Triumph or any project.

---

## 9. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Forge reconstruction fidelity checklist; adds `RECONSTRUCTION FIDELITY FINDINGS`. |
