# MARS Website Factory - Reconstruction Drift Taxonomy

**Status:** **documented** - taxonomy for human-supervised reconstruction-fidelity review.  
**Not:** automated detection, runtime scoring, screenshot diff, computer vision, or universal drift law.

**Parent governance:** [design-intent-transfer-governance.md](design-intent-transfer-governance.md).  
**Model:** [reconstruction-fidelity-model.md](reconstruction-fidelity-model.md).  
**Forge checklist:** [`../../agents/mars-forge/reconstruction-fidelity-checklist.md`](../../agents/mars-forge/reconstruction-fidelity-checklist.md).

---

## 1. Purpose

This taxonomy names drift patterns where a frontend reconstruction appears plausible, polished, or visually close while losing source-to-build fidelity, design-intent continuity, approximation transparency, or transfer integrity.

Use it in `RECONSTRUCTION FIDELITY FINDINGS` when reconstruction fidelity is material to QA or freeze.

---

## 2. Drift Patterns

| Drift pattern | Meaning | Common signal | Governance response |
|---------------|---------|---------------|---------------------|
| **Reconstruction drift** | The build gradually departs from source intent during translation. | Many small "reasonable" choices no longer read like the source. | Re-anchor to source and name affected fidelity layers. |
| **Fidelity illusion** | The build looks close enough to imply stronger fidelity than evidence supports. | "Looks matched" language without source-to-build trace. | Narrow confidence and disclose proof boundary. |
| **Approximation contamination** | Approximation spreads into areas later treated as exact source truth. | A compromise becomes a reusable pattern or freeze claim. | Mark approximation boundary and prevent inheritance. |
| **Source-transfer degradation** | Source meaning, hierarchy, or structure weakens as it moves into code. | Implementation follows template or existing code over active source. | Reconnect decision to source authority. |
| **Visual-intent loss** | Visual similarity remains while focal path, density, mood, or emphasis changes. | Screenshot resemblance but wrong reading order. | Run visual reconciliation and hierarchy fidelity review. |
| **Semantic reconstruction mismatch** | Meaning, role, entity count, CTA purpose, proof role, or section purpose changes. | Same layout shape carries different business or content meaning. | Run semantic source lock and strategic/source interpretation review. |
| **Layout reinterpretation drift** | The source layout is rebuilt through a different structural idea. | Grouping, cards, wrappers, or columns are reorganized by taste. | Check structural fidelity and composition awareness. |
| **Hierarchy fidelity collapse** | Primary/supporting relationships flatten, invert, or become ambiguous. | Secondary proof, media, or detail overtakes claim or CTA. | Record hierarchy-fidelity findings and escalate if material. |
| **Reconstruction overconfidence** | Fidelity claims exceed source quality, observed evidence, or QA scope. | "Fully matched" after screenshot-only or partial review. | Calibrate confidence and add QA confidence findings. |
| **Source-to-build divergence** | Build decisions cannot be traced back to active source. | No source refs for material layout, content, responsive, or style decisions. | Require source-alignment review or SAFE UNKNOWN. |
| **Screenshot mimicry drift** | Surface geometry is copied while intent, semantics, or responsive behavior is ignored. | Pixel-ish layout with wrong CTA role, grouping, or mobile story. | Separate visual similarity from reconstruction fidelity. |
| **Approximation opacity** | Approximation exists but is not visible in report, source notes, or QA. | Gaps are hidden behind "close enough." | Add approximation disclosure and confidence boundary. |
| **Fidelity survivability erosion** | Future operators cannot understand fidelity claims or reconstruction limits. | REPORT lacks source refs, approximations, unknowns, or confidence labels. | Add traceability, evidence boundary, and survivability notes. |

---

## 3. High-Risk Combinations

Some drift patterns become more dangerous together:

| Combination | Risk |
|-------------|------|
| **Fidelity illusion + reconstruction overconfidence** | Weak evidence becomes trusted freeze language. |
| **Screenshot mimicry drift + semantic reconstruction mismatch** | Visual QA may pass while meaning changes. |
| **Approximation contamination + fidelity survivability erosion** | Future edits inherit hidden compromises as source truth. |
| **Layout reinterpretation drift + hierarchy fidelity collapse** | A technically clean rebuild changes the story. |
| **Source-transfer degradation + source-to-build divergence** | Active source loses authority to template, old code, or agent preference. |

---

## 4. Anti-Pattern Vocabulary

Use these anti-pattern labels when they are clearer than a drift class:

- **Screenshot worship** - treating a screenshot as complete design law.
- **Fake fidelity claims** - claiming full or exact fidelity without evidence.
- **Hidden approximation** - hiding compromises, unknowns, or inferred choices.
- **Visual mimicry without semantics** - copying visible form while changing meaning.
- **Reconstruction overconfidence** - inflating fidelity confidence beyond evidence.
- **Hierarchy reinterpretation drift** - changing priority relationships by taste.
- **Cosmetic fidelity theater** - polish that substitutes for source alignment.
- **Source-detached rebuilding** - building from old code, template habits, or guesses.
- **Approximation opacity** - making approximations unreadable to future operators.
- **"Looks similar therefore accurate"** - treating resemblance as proof of intent transfer.

---

## 5. SAFE UNKNOWN Triggers

Record **SAFE UNKNOWN** instead of a fidelity PASS when:

- source authority is missing or contradictory;
- source hierarchy is unreadable or ambiguous;
- semantic role is inferred but not supported;
- mobile / tablet source is missing and responsive fidelity is material;
- approximation exists but cannot be bounded;
- existing code and active source conflict;
- rendered similarity is available but source-to-build traceability is absent;
- future operators would not be able to reconstruct the fidelity basis.

---

## 6. Reporting Guidance

When a drift pattern is found, report:

- drift pattern name;
- affected fidelity layer;
- source reference;
- build symptom;
- evidence strength;
- approximation boundary, if any;
- confidence adjustment;
- action: no action, tune, disclose, defer, HITL, block, or stop.

---

## 7. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial reconstruction drift taxonomy - reconstruction drift, fidelity illusion, approximation contamination, source-transfer degradation, semantic mismatch, hierarchy collapse, overconfidence, source-to-build divergence, screenshot mimicry, approximation opacity, and survivability erosion; documentation only. |
