# MARS Website Factory - Reconstruction Bootstrap Governance

**Status:** **documented** - Website Factory reconstruction bootstrap governance and human-supervised readiness discipline only.  
**Not:** automatic reconstruction engine, asset scanner, implementation planner, responsive simulator, or orchestration runtime.

**Core principle:** reconstruction should not begin until source, assets, authority, sections, responsive risks, and atmosphere are mapped enough to avoid hidden drift.

**Related layers:** [initialization-governance.md](initialization-governance.md), [workspace-reset-governance.md](workspace-reset-governance.md), [source-interpretation-governance.md](source-interpretation-governance.md), [design-intent-transfer-governance.md](design-intent-transfer-governance.md), [background-ownership-governance.md](background-ownership-governance.md), [reconstruction-asset-lifecycle-governance.md](reconstruction-asset-lifecycle-governance.md).  
**Forge findings category:** `RECONSTRUCTION BOOTSTRAP FINDINGS`.

---

## 1. Purpose

Reconstruction Bootstrap Governance defines the pre-implementation audit required when rebuilding from source artifacts, screenshots, design exports, prior code, or mixed project memory.

It covers:

- pre-implementation audit;
- source audit;
- asset audit;
- authority mapping;
- section mapping;
- responsive-risk mapping;
- atmosphere mapping;
- bootstrap survivability;
- implementation readiness.

---

## 2. Bootstrap Audit

| Audit area | Required read |
|------------|---------------|
| **Source audit** | Active source version, source paths, forbidden paths, missing states, and source confidence. |
| **Asset audit** | Approved, temporary, transformed, deprecated, and missing assets. |
| **Authority mapping** | Human decisions, project docs, design source, prior code, and derived artifacts separated. |
| **Section mapping** | Section order, shell/header/hero boundaries, first-screen decomposition, and frozen/unknown regions. |
| **Responsive-risk mapping** | Missing mobile/tablet source, likely collapse risks, nav risks, CTA risks, and media risks. |
| **Atmosphere mapping** | Dark/light cadence, environmental rhythm, heaviness, and background ownership. |
| **Readiness disposition** | Ready, partial-ready, blocked, HITL required, or SAFE UNKNOWN. |

---

## 3. Canonical Rules

- Run bootstrap before reconstruction implementation, not after the first visible mismatch.
- Do not treat “we have screenshots” as readiness.
- Do not treat prior implementation as source unless authority mapping promotes it.
- Include first-screen decomposition when the opening viewport is in scope.
- Include reset review when stale implementation or old rebuild attempts exist.
- Record bootstrap findings when readiness is partial, blocked, or dependent on assumptions.

---

## 4. Anti-Patterns

| Anti-pattern | Why it is drift |
|--------------|-----------------|
| **Rebuild first, audit later** | Implementation hardens before authority and risks are known. |
| **Screenshot-only bootstrap** | Source confidence, assets, states, and responsive behavior are missing. |
| **Asset surprise** | Media gaps are discovered after layout depends on them. |
| **Responsive blind start** | Mobile collapse risk is not mapped before desktop structure locks. |
| **Atmosphere afterthought** | Emotional pressure and dark/light cadence are bolted on during polish. |
| **Bootstrap chaos** | Every decision is rediscovered mid-build. |

---

## 5. Drift Patterns

- **Reconstruction bootstrap failure** - work starts without enough source/asset/authority readiness.
- **Readiness inflation drift** - partial source is reported as implementation-ready.
- **Section mapping drift** - operators cannot tell what screen/section/layer is being rebuilt.
- **Responsive-risk blindness** - breakpoints are treated as later cleanup despite source gaps.

---

## 6. Triumph V3 Lesson

Triumph V3 exposed reconstruction bootstrap chaos: first-screen work needed source audit, asset audit, authority mapping, shell/hero/background split, and responsive risk mapping before implementation.

The lesson is readiness governance. It is not a new implementation pipeline or rebuild recipe.

---

## 7. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Source audit is incomplete | Cannot claim reconstruction readiness. |
| Asset approval is unclear | Cannot safely use or transform media. |
| Section boundaries are unmapped | Cannot assign ownership or freeze scope. |
| Mobile or tablet source is absent | Cannot infer responsive fidelity. |
| Atmosphere source is ambiguous | Cannot preserve environmental continuity. |

**Action:** classify readiness as ready / partial-ready / blocked / HITL required / SAFE UNKNOWN, then proceed only within that boundary.

---

## 8. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-18 | Initial Reconstruction Bootstrap Governance layer from Triumph V3 battle-test lessons. |
