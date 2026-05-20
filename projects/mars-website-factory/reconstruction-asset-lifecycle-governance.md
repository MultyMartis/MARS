# MARS Website Factory - Reconstruction Asset Lifecycle Governance

**Status:** **documented** - Website Factory reconstruction asset lifecycle governance and human-supervised media authority methodology only.  
**Not:** DAM, asset transformer, file deduplicator, rights management system, automatic image optimizer, or runtime asset registry.

**Core principle:** reconstruction assets carry authority state. Approved, temporary, derived, transformed, and deprecated assets must not blur together.

**Related layers:** [knowledge-provenance-governance.md](knowledge-provenance-governance.md), [source-lineage-model.md](source-lineage-model.md), [background-ownership-governance.md](background-ownership-governance.md), [reconstruction-bootstrap-governance.md](reconstruction-bootstrap-governance.md), [design-intent-transfer-governance.md](design-intent-transfer-governance.md).  
**Forge findings category:** `RECONSTRUCTION ASSET FINDINGS`.

---

## 1. Purpose

Reconstruction Asset Lifecycle Governance defines how assets used in reconstruction should be classified, inherited, transformed, disclosed, and deprecated.

It covers:

- approved assets;
- reconstruction assets;
- temporary assets;
- deprecated assets;
- asset authority inheritance;
- derived asset disclosure;
- transformation traceability;
- reconstruction asset lifecycle.

---

## 2. Asset Taxonomy

| Asset state | Meaning |
|-------------|---------|
| **Approved asset** | Explicitly authorized source/project asset for implementation. |
| **Reconstruction asset** | Asset used to approximate or rebuild source fidelity, with disclosed authority. |
| **Temporary asset** | Placeholder or interim asset that must not be treated as final authority. |
| **Derived asset** | Asset transformed from another source: crop, color change, mask, compression, extraction, generated derivative. |
| **Deprecated asset** | Asset no longer active for the current version, retained only for history or rollback. |
| **Unknown-origin asset** | Asset with unclear provenance, rights, or authority. |

---

## 3. Canonical Rules

- Classify assets before using them as reconstruction authority.
- Do not mutate approved assets without derived-asset disclosure.
- Do not promote temporary assets to final silently.
- Do not use deprecated assets to reconstruct active source unless explicitly authorized.
- Track transformation reason and scope when crops, masks, recolors, or derived backgrounds are created.
- Record asset findings when authority inheritance, transformation, or lifecycle state affects fidelity or rights confidence.

---

## 4. Anti-Patterns

| Anti-pattern | Why it is drift |
|--------------|-----------------|
| **Approved asset mutation** | Source media changes without disclosure or authority. |
| **Temporary asset promotion** | Placeholder becomes production asset by inertia. |
| **Deprecated asset reuse** | Old version media contaminates active reconstruction. |
| **Unknown-origin confidence** | Asset provenance is assumed because it is present in the workspace. |
| **Derived asset opacity** | Crops, masks, or color edits hide transformation history. |
| **Asset authority laundering** | A generated or edited asset inherits approval it does not have. |

---

## 5. Drift Patterns

- **Asset lifecycle drift** - approved, temporary, derived, deprecated, and unknown assets blur together.
- **Transformation traceability drift** - future operators cannot explain why an asset differs from source.
- **Authority inheritance drift** - derived assets inherit approval without review.
- **Media ownership drift** - background or section media lacks owner and source lineage.

---

## 6. Triumph V3 Lesson

Triumph V3 exposed approved asset mutation risk: background and atmosphere repair can pressure operators to crop, alter, or substitute media without lifecycle disclosure.

The governance lesson is asset lifecycle traceability. It is not a claim that Forge manages assets automatically.

---

## 7. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Asset source is not documented | Cannot claim approval or rights confidence. |
| Asset appears transformed | Cannot prove fidelity or authority inheritance. |
| Temporary/final status is unclear | Cannot safely freeze the asset. |
| Deprecated asset may still be referenced | Requires workspace reset and lineage review. |
| Background asset ownership is unclear | Requires background ownership governance. |

**Action:** classify asset state, disclose transformation, and request authority before treating it as approved final source.

---

## 8. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-18 | Initial Reconstruction Asset Lifecycle Governance layer from Triumph V3 battle-test lessons. |
