# MARS Website Factory - Reconstruction Fidelity Model

**Status:** **documented** - conceptual model for human-supervised frontend reconstruction fidelity.  
**Not:** runtime scoring, automated design diff, computer vision, universal fidelity law, or perfect source-alignment guarantee.

**Parent governance:** [design-intent-transfer-governance.md](design-intent-transfer-governance.md).  
**Drift taxonomy:** [reconstruction-drift-taxonomy.md](reconstruction-drift-taxonomy.md).  
**Production readiness relation:** [production-readiness-governance.md](production-readiness-governance.md) - delivery traceability depends on fidelity claims remaining explainable after handoff.  
**Forge checklist:** [`../../agents/mars-forge/reconstruction-fidelity-checklist.md`](../../agents/mars-forge/reconstruction-fidelity-checklist.md).

---

## 1. Purpose

This model gives Website Factory a shared vocabulary for reviewing how approved source material survives reconstruction into frontend output.

It separates:

- source transfer;
- structural fidelity;
- hierarchy fidelity;
- responsive fidelity;
- approximation boundaries;
- reconstruction confidence;
- fidelity survivability.

The model is a review aid. It does not calculate fidelity or replace human source review.

---

## 2. Fidelity Layers

| Layer | What it protects | Primary question |
|-------|------------------|------------------|
| **Source-authority layer** | Active source, source priority, lineage, and source-to-build ownership | Which source authorizes this reconstruction decision? |
| **Structural-fidelity layer** | Section boundaries, DOM grouping, include ownership, component shape, and block identity | Did implementation structure preserve the source's intended organization? |
| **Hierarchy-fidelity layer** | Priority relationships among claim, proof, CTA, media, details, and decorative elements | Did the reading ladder survive reconstruction? |
| **Responsive-fidelity layer** | Intent preservation across viewport collapse, stack behavior, mobile cadence, and breakpoint adaptation | Does the viewport version remain source-aligned, not merely functional? |
| **Approximation layer** | Known gaps, practical compromises, inferred choices, and unresolved source limits | What is approximated, why, and how visible is it? |
| **Reconstruction-confidence layer** | Evidence strength, uncertainty, confidence labels, and proof boundary | How strong can the fidelity claim be? |
| **Fidelity-survivability layer** | Future reviewability across reports, handoff, context compression, freeze, and later edits | Can fidelity be reconstructed later without myth or hidden assumptions? |

---

## 3. Source-Authority Layer

The source-authority layer establishes what the reconstruction is allowed to follow.

Review:

- active source path and version;
- source priority when screenshots, implementation pack, existing code, and old docs conflict;
- source lineage and derivation;
- whether the source is explicit, inferred, ambiguous, unknown, or contradictory;
- whether existing implementation is source evidence or merely prior output.

**Rule:** source transfer cannot be faithful if source authority is unclear.

---

## 4. Structural-Fidelity Layer

Structural fidelity protects the source's intended organization as it becomes markup, partials, styles, and behavior hooks.

Review:

- section and block boundaries;
- DOM grouping vs visual grouping;
- wrapper, card, list, media, CTA, and proof ownership;
- include-chain and component ownership;
- structural changes required to preserve fidelity.

**Rule:** a visually similar layout can still fail if structure reinterprets source grouping or makes future fidelity impossible.

---

## 5. Hierarchy-Fidelity Layer

Hierarchy fidelity protects meaning through priority.

Review:

- primary claim vs support copy;
- primary CTA vs secondary action;
- proof authority vs decorative trust cue;
- hero, body, dense detail, and closing CTA roles;
- type, spacing, contrast, surface, and ordering decisions that alter priority.

**Rule:** hierarchy drift is semantic drift when it changes what the user reads as important.

---

## 6. Responsive-Fidelity Layer

Responsive fidelity asks whether source intent survives viewport adaptation.

Review:

- mobile source or responsive rules;
- stack integrity and composition collapse;
- hierarchy survival under narrow width;
- CTA pressure and proof placement;
- mobile cadence, density, and operational readability;
- whether the responsive decision is source-backed, inferred, approximated, or unknown.

**Rule:** responsive survivability is necessary but insufficient; fitting the viewport does not prove source fidelity.

---

## 7. Approximation Layer

Approximation is allowed when exact fidelity cannot be proven or is impractical, but it must remain visible.

Approximation boundaries include:

- missing source boundary;
- raster / low-resolution boundary;
- responsive boundary;
- token / design-system boundary;
- asset boundary;
- structural boundary;
- interaction / state boundary;
- evidence boundary.

For each material approximation, report:

- what was approximated;
- why exact fidelity could not be claimed;
- what evidence supports the chosen approximation;
- what would resolve or improve fidelity;
- whether HITL is recommended or required.

**Rule:** approximation that is not disclosed becomes fidelity illusion.

---

## 8. Reconstruction-Confidence Layer

Reconstruction confidence is the declared strength of a fidelity claim relative to evidence.

Use confidence levels:

| Level | Meaning |
|-------|---------|
| **High source-aligned** | Active source directly supports the decision and rendered/build evidence does not contradict it. |
| **Moderate source-aligned** | Source strongly implies the decision, but some implementation or viewport detail remains inferred. |
| **Partial fidelity** | Some dimensions align while others are unverified, approximated, or deferred. |
| **Approximation disclosed** | Fidelity is intentionally bounded because source or implementation evidence is incomplete. |
| **SAFE UNKNOWN** | Source, evidence, hierarchy, semantics, or approximation boundary is insufficient. |
| **Contradictory** | Sources or implementation evidence conflict and require resolution before confidence can be claimed. |

**Rule:** confidence should narrow when evidence is source-only, screenshot-only, rendered-only, build-only, inferred, or partially observed.

---

## 9. Fidelity-Survivability Layer

Fidelity survivability protects future review.

A reconstruction record is survivable when it includes:

- active source references;
- source-to-build decision notes for material choices;
- named approximation boundaries;
- hierarchy and semantic transfer notes;
- responsive fidelity limits;
- confidence level and proof boundary;
- unresolved SAFE UNKNOWN or HITL state;
- report language that future operators can understand.

**Rule:** if future operators cannot tell why the build claims fidelity, the fidelity claim is fragile.

---

## 10. Reconstruction Escalation

Escalate when:

- source authority is missing or contradictory;
- hierarchy cannot be proven;
- semantic role, CTA role, proof authority, or entity count is ambiguous;
- responsive adaptation requires unapproved redesign;
- approximation affects business meaning, trust, accessibility, or freeze confidence;
- existing code conflicts with active source;
- high-fidelity claims would depend on weak evidence.

Use **continue with disclosure**, **PARTIAL**, **SAFE UNKNOWN**, **HITL recommended**, **HITL required**, **blocked**, or **STOP**.

---

## 11. Source-Alignment Review

Before freeze, ask:

- What source governed the reconstruction?
- Which decisions are observed vs inferred vs assumed?
- Where did approximation enter?
- Did hierarchy, semantics, composition, and responsive behavior survive?
- Does confidence match evidence?
- Can the fidelity record survive handoff and later review?

Record material answers as `RECONSTRUCTION FIDELITY FINDINGS`.

Use [production-readiness-governance.md](production-readiness-governance.md) when fidelity survivability affects delivery handoff, onboarding readability, future maintenance, or post-delivery trust; record `PRODUCTION READINESS FINDINGS` separately.

---

## 12. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Reconstruction Fidelity Model - source-authority, structural-fidelity, hierarchy-fidelity, responsive-fidelity, approximation, reconstruction-confidence, and fidelity-survivability layers; documentation only. |
| v0.1 | 2026-05-17 | Linked Production Readiness & Delivery Survivability Governance for delivery traceability, handoff-readable fidelity records, and post-delivery trust preservation. |
