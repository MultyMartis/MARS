# MARS Website Factory - Overlay and Focal Balance Governance

**Status:** **documented** - Website Factory overlay, readability, and focal-region methodology only.  
**Not:** image optimizer, automatic focal detector, responsive art-direction engine, screenshot diff, or visual renderer.

**Core principle:** overlays must preserve readability without suffocating media energy, and focal visual regions must survive responsive scaling.

**Related layers:** [background-ownership-governance.md](background-ownership-governance.md), [first-screen-decomposition-model.md](first-screen-decomposition-model.md), [atmosphere-continuity-governance.md](atmosphere-continuity-governance.md), [visual-reconciliation-layer.md](visual-reconciliation-layer.md), [responsive-intent-governance.md](responsive-intent-governance.md).  
**Forge findings categories:** `OVERLAY BALANCE FINDINGS`, `FOCAL-POINT FINDINGS`.

---

## 1. Purpose

This layer captures V4 first-screen lessons where readability fixes damaged atmosphere, focal anchoring, and commercial energy.

It governs:

- atmosphere readability balance;
- overlay pressure governance;
- background focal-point governance;
- hero focal anchoring;
- text-safe and media-safe zones;
- focal-region responsive survivability;
- media energy preservation.

---

## 2. Overlay Balance Rules

- Hero overlay must preserve environment readability.
- Overlay must not suffocate media energy.
- Over-darkening is a drift risk, not an automatic readability win.
- Scrims, gradients, and masks must have an owner and reason: text readability, shell continuity, CTA contrast, or source fidelity.
- Do not use overlay pressure to hide wrong focal anchoring or poor crop choice.
- Check overlay behavior at responsive breakpoints; a readable desktop scrim may destroy mobile media.

---

## 3. Focal-Point Rules

- Focal visual regions must survive responsive scaling.
- Hero focal anchoring must preserve the source subject: vehicle, person, product, environment, or action.
- Misplaced truck anchoring is focal drift when the primary commercial object moves out of the meaningful field.
- Text-safe zones must not cover critical media meaning.
- Media-safe zones must keep the source atmosphere visible enough to carry commercial tone.
- When the crop/focal point cannot be proven, record **SAFE UNKNOWN** rather than inventing a responsive art direction.

---

## 4. Text-Safe / Media-Safe Zones

| Zone | Governance read |
|------|-----------------|
| **Text-safe zone** | Foreground copy and CTA remain readable without excessive overlay pressure. |
| **Media-safe zone** | Critical image meaning remains visible and not hidden by text, masks, or crop. |
| **Focal anchor** | The primary visual subject stays in an intentional location across desktop/tablet/mobile. |
| **Atmosphere field** | Background environment remains legible enough to support mood and commercial seriousness. |

The zones can overlap only when the source supports it and readability can be preserved without over-darkening drift.

---

## 5. Drift Lessons Captured

| Drift | Governance lesson |
|-------|-------------------|
| **S01 over-darkening drift** | Readability fixes can erase environment, product energy, and source atmosphere. |
| **Atmosphere suffocation drift** | Overlay pressure can make a landing feel dead even when text contrast passes. |
| **Hero focal-point drift** | The hero may technically show the asset while losing the intended subject emphasis. |
| **Misplaced truck anchoring** | Industrial/service hero imagery needs stable focal placement, not arbitrary background-position patches. |
| **Overlay laundering** | A scrim can hide unresolved crop, source, or ownership problems. |

Required V4 lesson labels captured: `S01 over-darkening drift`, `atmosphere suffocation drift`, `hero focal-point drift`, `misplaced truck anchoring`.

---

## 6. Forge Use

Record:

- `OVERLAY BALANCE FINDINGS` for over-darkening, atmosphere suffocation, unreadable environment, unsupported scrims, or overlay pressure that hides source issues.
- `FOCAL-POINT FINDINGS` for lost hero subject, misplaced vehicle/product/person, unsafe text/media overlap, focal-region failure at breakpoints, or unknown crop authority.

These findings usually accompany `BACKGROUND OWNERSHIP FINDINGS`, `FIRST-SCREEN DECOMPOSITION FINDINGS`, `ATMOSPHERE CONTINUITY FINDINGS`, and `RESPONSIVE INTENT FINDINGS`.

---

## 7. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Source crop is missing | Cannot prove focal anchor. |
| Background image is derived without documented lineage | Cannot prove media-safe region. |
| Mobile art direction is absent | Cannot prove responsive focal survival. |
| Overlay reason is not documented | Cannot tell whether it protects readability or masks drift. |
| Text overlaps a critical visual subject | Cannot claim source fidelity without decision. |

**Action:** identify source image, focal subject, text-safe area, media-safe area, overlay reason, and breakpoint behavior before freeze.

---

## 8. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-18 | Initial overlay and focal balance governance from Triumph V4 lessons. |
