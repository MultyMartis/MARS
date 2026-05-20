# MARS Website Factory - Design Intent Transfer & Reconstruction Fidelity Governance

**Status:** **documented** - Website Factory reconstruction-fidelity discipline and human-supervised design-transfer methodology only.  
**Not:** autonomous design-reading AI, runtime fidelity scoring, screenshot diff, universal reconstruction law, redesign authority, or perfect source-fidelity guarantee.

**Core principle:** frontend reconstruction must preserve **source intent, hierarchy fidelity, semantic continuity, compositional integrity, approximation transparency, and transfer integrity**.  
It is not merely "match the screenshot," "copy the layout," "rebuild the design," or "make it visually similar."

**Companion documents:** [reconstruction-fidelity-model.md](reconstruction-fidelity-model.md), [reconstruction-drift-taxonomy.md](reconstruction-drift-taxonomy.md).  
**Related layers:** [source-interpretation-governance.md](source-interpretation-governance.md), [visual-reconciliation-layer.md](visual-reconciliation-layer.md), [responsive-intent-governance.md](responsive-intent-governance.md), [strategic-intent-governance.md](strategic-intent-governance.md), [trust-calibration-governance.md](trust-calibration-governance.md), [qa-confidence-governance.md](qa-confidence-governance.md), [adaptive-governance.md](adaptive-governance.md).  
**Forge checklist:** [`../../agents/mars-forge/reconstruction-fidelity-checklist.md`](../../agents/mars-forge/reconstruction-fidelity-checklist.md).

---

## 1. Positioning

Design Intent Transfer & Reconstruction Fidelity exists because a frontend can look polished, resemble the source, pass visual QA, and appear highly accurate while still misrepresenting intent, distorting hierarchy, losing semantics, or introducing hidden approximation drift.

| This layer governs | This layer does not govern |
|--------------------|----------------------------|
| Source-to-build fidelity, design-intent continuity, reconstruction survivability, approximation transparency, and transfer integrity | Pixel-perfect automation, computer vision, autonomous source reading, or universal fidelity scoring |
| Human-supervised review of whether the source survived translation into frontend decisions | Redesigning Triumph or any other project |
| Drift vocabulary for fidelity illusion, source-transfer degradation, hierarchy collapse, and approximation opacity | Claims of perfect source fidelity or automatic reconstruction truth |
| Forge reporting discipline for `RECONSTRUCTION FIDELITY FINDINGS` | Runtime scoring, build-time enforcement, or hidden validation engines |

The governance question is not "does it look similar?"  
The governance question is: **can a future reviewer trace how source intent became build decisions, where fidelity is strong, and where approximation was necessary?**

---

## 2. Canonical Definition

**Design-intent transfer** is the governed movement of source meaning, hierarchy, composition, responsive behavior, and strategic purpose into frontend implementation without turning visual similarity into false authority.

**Reconstruction fidelity** is the degree to which the built artifact preserves the source's intended relationships, not only its visible surface.

This layer protects:

- **Source-to-build continuity** - implementation decisions remain connected to named source authority.
- **Fidelity survivability** - the fidelity record remains readable across QA, handoff, compressed context, later edits, and future reconstruction.
- **Approximation transparency** - approximations are disclosed, bounded, and not allowed to masquerade as exact source fidelity.
- **Hierarchy fidelity** - primary, secondary, supporting, proof, CTA, and decorative layers keep their intended order and weight.
- **Semantic reconstruction integrity** - meaning, roles, entities, CTAs, proof, and section purpose survive the rebuild.
- **Compositional transfer** - visual grouping, focal path, balance, density, and cluster logic remain source-aligned.
- **Source fidelity confidence** - confidence is calibrated to evidence and source quality.
- **Reconstruction traceability** - future operators can see what was observed, inferred, assumed, approximated, or unknown.
- **Transfer survivability** - source alignment does not collapse when the artifact moves through agents, reports, QA, or later maintenance.

---

## 3. Required Vocabulary

| Concept | Meaning |
|---------|---------|
| **Reconstruction fidelity** | Preservation of source intent, hierarchy, semantics, composition, and responsive behavior through implementation. |
| **Design-intent transfer** | The governed translation of approved source intent into frontend decisions. |
| **Source-to-build continuity** | Traceable connection between source artifacts and build choices. |
| **Fidelity survivability** | Fidelity evidence remains understandable after handoff, QA, context compression, and future edits. |
| **Approximation transparency** | Practical approximations are visible, bounded, and reported. |
| **Hierarchy fidelity** | Visual and semantic priority relationships survive reconstruction. |
| **Semantic reconstruction integrity** | Meaning, CTA role, entity count, proof role, and section purpose remain source-aligned. |
| **Compositional transfer** | Grouping, focal path, balance, density, and rhythm transfer without accidental reinterpretation. |
| **Source fidelity confidence** | Confidence label for how strongly source evidence supports the reconstruction claim. |
| **Reconstruction traceability** | A future reviewer can trace observed, inferred, assumed, approximated, and unknown decisions. |
| **Fidelity drift** | Loss of source alignment while the build still appears plausible or polished. |
| **Approximation disclosure** | Explicit report of where exact source fidelity could not be proven or was not practical. |
| **Transfer survivability** | Source intent survives implementation, QA, report, handoff, and future maintenance. |
| **Reconstruction readability** | The fidelity record is reviewable and not hidden in vague "matched source" language. |
| **Source-alignment continuity** | Ongoing alignment between current source authority, implementation, QA, and report conclusions. |

---

## 4. Core Rules

- **Fidelity requires traceability.** A similarity claim without source-to-build evidence is weak.
- **Approximation should remain visible.** Hidden approximation becomes false fidelity.
- **Source intent matters.** A rebuild must preserve what the source is trying to communicate, not only visible geometry.
- **Hierarchy fidelity preserves meaning.** Changing emphasis can change story, trust, conversion, and comprehension.
- **Reconstruction confidence should remain calibrated.** Weak source evidence cannot support strong fidelity claims.
- **Visual similarity is not sufficient.** Screenshot resemblance can coexist with semantic mismatch or hierarchy collapse.
- **Source-alignment continuity matters.** Later QA and edits must not detach the build from source authority.
- **Reconstruction survivability preserves trust.** Future operators must be able to understand fidelity limits and decisions.
- **Approximation boundaries should be named.** Use source gap, responsive gap, asset gap, token gap, structural gap, or evidence gap where appropriate.
- **No perfect fidelity claims.** Report bounded fidelity, partial fidelity, approximation, SAFE UNKNOWN, or HITL need.

---

## 5. Reconstruction Review Dimensions

Use these dimensions when a source is rebuilt into frontend code:

| Dimension | Review question |
|-----------|-----------------|
| **Source authority** | Which artifact authorizes the decision, and is it active? |
| **Hierarchy fidelity** | Do priority relationships survive across text, CTA, proof, media, and surfaces? |
| **Semantic continuity** | Did meaning, role, entity count, CTA purpose, and proof structure survive? |
| **Compositional integrity** | Did grouping, focal path, rhythm, density, and balance transfer without reinterpretation drift? |
| **Responsive fidelity** | Does viewport adaptation preserve intent rather than merely survive width? |
| **Approximation boundary** | What had to be approximated, why, and how is it disclosed? |
| **Confidence calibration** | Does the fidelity claim match evidence strength? |
| **Traceability** | Can future operators reconstruct why the build looks and behaves this way? |

---

## 6. Anti-Patterns

Forbidden drift:

| Anti-pattern | Why it is forbidden |
|--------------|---------------------|
| **Screenshot worship** | Treats visible pixels as complete intent and hides source ambiguity. |
| **Fake fidelity claims** | Reports exactness or full alignment without traceable evidence. |
| **Hidden approximation** | Practical compromises are made invisible and later become false source truth. |
| **Visual mimicry without semantics** | Build resembles the source while meaning, CTA role, proof, or grouping changes. |
| **Reconstruction overconfidence** | Weak, inferred, or partial source evidence is reported as strong fidelity. |
| **Hierarchy reinterpretation drift** | Primary and supporting elements are reweighted by taste or implementation convenience. |
| **Cosmetic fidelity theater** | Polish, shadows, spacing, or type treatment substitute for real source alignment. |
| **Source-detached rebuilding** | Implementation follows existing code, template habit, or agent preference instead of active source. |
| **Approximation opacity** | Unknowns and compromises are buried behind "looks close." |
| **"Looks similar therefore accurate"** | Confuses resemblance with intent, semantics, and transfer integrity. |

Use [reconstruction-drift-taxonomy.md](reconstruction-drift-taxonomy.md) for full drift classification.

---

## 7. Forge Integration

When Forge is selected, reconstruction fidelity becomes a pre-freeze QA concern:

- Run [`reconstruction-fidelity-checklist.md`](../../agents/mars-forge/reconstruction-fidelity-checklist.md) when source-to-build transfer, approximation, hierarchy fidelity, semantic transfer, responsive fidelity, or confidence calibration affects implementation.
- Record **RECONSTRUCTION FIDELITY FINDINGS** for reconstruction-fidelity QA, source-alignment QA, approximation-transparency QA, hierarchy-fidelity QA, semantic-transfer QA, and fidelity-survivability QA.
- Use [reconstruction-fidelity-model.md](reconstruction-fidelity-model.md) to identify which layer is at risk.
- Use [reconstruction-drift-taxonomy.md](reconstruction-drift-taxonomy.md) to name drift patterns.
- Keep **RECONSTRUCTION FIDELITY FINDINGS** separate from `SOURCE INTERPRETATION FINDINGS`, `VISUAL FINDINGS`, `RESPONSIVE INTENT FINDINGS`, `STRATEGIC INTENT FINDINGS`, `QA CONFIDENCE FINDINGS`, `TRUST CALIBRATION FINDINGS`, and `ADAPTIVE GOVERNANCE FINDINGS`.
- Escalate SAFE UNKNOWN when source authority, hierarchy, semantics, responsive behavior, or approximation boundary cannot be established.

This is human-supervised design-transfer methodology. It does not claim autonomous design reading, runtime fidelity scoring, or perfect reconstruction.

---

## 8. Triumph V2 Lessons Captured

Triumph V2 exposed reusable Website Factory reconstruction lessons:

- A rebuild can resemble the active source while hierarchy fidelity still collapses through equalized cards, CTA pressure, or proof flattening.
- Screenshot similarity can hide semantic reconstruction mismatch when CTA role, entity count, proof authority, or section purpose changes.
- Missing mobile source can make responsive output survivable but not source-faithful beyond disclosed approximation.
- Existing code, old exports, or foundation defaults can contaminate transfer when source lineage is not explicit.
- Polished visual reconciliation does not prove approximation transparency, reconstruction traceability, or transfer survivability.
- A future operator needs visible fidelity boundaries, not just a statement that the build "matches" V2.

These are Website Factory governance lessons, not Triumph redesign instructions.

---

## 9. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Active source authority is unclear | Cannot prove which artifact governs reconstruction. |
| Hierarchy is ambiguous | Cannot prove primary/supporting relationships. |
| Semantics are inferred only | Cannot claim semantic reconstruction integrity. |
| Approximation boundary is hidden | Cannot tell what is source-faithful vs practical compromise. |
| Responsive behavior lacks source | Cannot prove responsive fidelity beyond survivability. |
| Existing code contradicts source | Cannot know whether to preserve implementation or reconstruct from source without decision. |
| Fidelity confidence exceeds evidence | Cannot report high fidelity without narrowing the claim. |
| Reconstruction traceability is missing | Future operators cannot review how source became build decisions. |

**Action:** state the unknown, name the needed resolver, disclose approximation if continuing, or classify the issue as HITL recommended, HITL required, blocked, or stopped.

---

## 10. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Design Intent Transfer & Reconstruction Fidelity Governance layer - source-to-build fidelity, design-intent continuity, reconstruction survivability, approximation transparency, transfer integrity, drift taxonomy, and Forge `RECONSTRUCTION FIDELITY FINDINGS`; documentation only. |
