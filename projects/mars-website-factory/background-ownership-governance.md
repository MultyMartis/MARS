# MARS Website Factory - Background Ownership Governance

**Status:** **documented** - Website Factory background ownership governance and human-supervised media/background traceability only.  
**Not:** asset pipeline, image transformer, design renderer, runtime media manager, or automatic visual diff.

**Core principle:** background is architecture when it controls readability, atmosphere, section boundaries, or shell continuity.

**Related layers:** [layout-shell-governance.md](layout-shell-governance.md), [first-screen-decomposition-model.md](first-screen-decomposition-model.md), [atmosphere-continuity-governance.md](atmosphere-continuity-governance.md), [overlay-focal-balance-governance.md](overlay-focal-balance-governance.md), [reconstruction-asset-lifecycle-governance.md](reconstruction-asset-lifecycle-governance.md), [visual-reconciliation-layer.md](visual-reconciliation-layer.md), [compositional-structure-awareness.md](compositional-structure-awareness.md).  
**Forge findings categories:** `BACKGROUND OWNERSHIP FINDINGS`, `OVERLAY BALANCE FINDINGS`, `FOCAL-POINT FINDINGS`.

---

## 1. Purpose

Background Ownership Governance clarifies which layer owns backgrounds, overlays, media, section bands, and atmospheric continuity during reconstruction or first-screen work.

It covers:

- background authority;
- environmental ownership;
- shell background;
- hero-local background;
- overlay ownership;
- atmospheric continuity;
- section boundary ownership;
- media ownership traceability.

---

## 2. Ownership Taxonomy

| Background type | Default owner | Governance concern |
|-----------------|---------------|--------------------|
| **Shell background** | Layout shell | Page continuity, nav readability, global environment. |
| **Hero-local background** | Hero system | Opening offer, hero mood, content readability. |
| **Section background** | Section/block owner | Boundary, density, local hierarchy. |
| **Atmospheric background** | Atmosphere layer | Emotional pressure and continuity across sections. |
| **Overlay / scrim** | Overlay layer plus affected owner | Readability, contrast, foreground separation. |
| **Media background** | Asset lifecycle plus visual owner | Source rights, transformation traceability, mutation disclosure. |

---

## 3. Canonical Rules

- Name whether a background is shell-owned, hero-local, section-local, atmospheric, or overlay-owned.
- Do not mutate approved assets to solve ownership ambiguity.
- Do not let a hero-local background define global page atmosphere without authority.
- Do not add overlays without explaining readability, atmosphere, or source fidelity rationale.
- Treat section boundary backgrounds as composition decisions, not decoration.
- Record media source, transformation, and derived-asset status when a background depends on image assets.
- Hero overlays must preserve environment readability and must not suffocate media energy.
- Focal visual regions must survive responsive scaling; background-position fixes are not sufficient if the source subject is lost.
- Text-safe zones and media-safe zones should be named when hero media, copy, and overlay pressure compete.

---

## 4. Anti-Patterns

| Anti-pattern | Why it is drift |
|--------------|-----------------|
| **Wrong background owner** | A shell or hero decision is implemented in the wrong layer. |
| **Overlay laundering** | Scrims hide poor background/readability decisions without ownership. |
| **Approved asset mutation** | Source media is changed without disclosure or authority. |
| **Global atmosphere from local hero** | One hero background contaminates later sections. |
| **Section boundary blur** | Backgrounds erase where one section ends and another begins. |
| **Media provenance loss** | Operators cannot tell where a background image came from or whether it is transformed. |
| **Atmosphere suffocation** | Overlay pressure makes media technically readable but visually dead. |
| **Focal-point drift** | Primary vehicle/product/person/environment moves out of the meaningful field. |

---

## 5. Drift Patterns

- **Background authority drift** - implementation uses a background without proving who owns it.
- **Environmental ownership drift** - atmosphere, shell, and section background decisions collapse together.
- **Overlay ownership drift** - readability layers appear without explicit owner.
- **Media traceability drift** - approved, temporary, transformed, and deprecated assets blur together.
- **Overlay pressure drift** - scrims or masks overcorrect readability and erase source atmosphere.
- **Hero focal anchoring drift** - the visual subject is no longer anchored across breakpoints.

---

## 6. Triumph V3 Lesson

Triumph V3 exposed wrong background ownership and approved asset mutation pressure: background decisions can appear cosmetic while actually changing shell, hero, atmosphere, and source fidelity.

The governance lesson is to map background ownership and media traceability before visual repair. This is not an asset-editing template.

---

## 7. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Background spans shell and hero | Cannot prove whether shell or hero owns it. |
| Overlay exists without source rationale | Cannot prove readability or aesthetic intent. |
| Asset is transformed but not disclosed | Cannot prove authority or fidelity. |
| Section boundary background is ambiguous | Cannot tell if banding is structural or decorative. |
| Media source is missing | Cannot claim approved asset use. |

**Action:** classify ownership, source, transformation, and affected layer before implementation or freeze.

---

## 8. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-18 | Initial Background Ownership Governance layer from Triumph V3 battle-test lessons. |
| v0.1 | 2026-05-18 | Added V4 overlay balance, focal anchoring, text-safe/media-safe zone, and responsive focal survival rules. |
