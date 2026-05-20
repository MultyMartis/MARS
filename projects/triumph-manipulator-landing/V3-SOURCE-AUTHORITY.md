# Triumph Manipulator Landing V3 — Source Authority

## 1. Purpose

This file defines source authority for the V3 battle test.

V3 is a **full rebuild from V1 source authority** using Forge doctrine only. It must not inherit V2 implementation, V2 CSS, V2 structure, V2 local fixes, or accumulated V2 patch history.

## 2. Primary layout authority

The primary layout/design authority for V3 is the **approved V1 source pack**.

Current repo-visible V1 source surfaces include:

- `projects/triumph-manipulator-landing/design/v1/`.
- `projects/triumph-manipulator-landing/design/mockups-index.md`.
- `projects/triumph-manipulator-landing/design/frontend-section-map.md` when used as V1 continuity context.
- `workspaces/triumph-manipulator-landing/` only if explicitly approved as part of the V1 source pack for reconstruction reference.

V1 layout authority controls section structure, hierarchy, composition, visual intent, and screen order.

The exact V1 source pack boundary must be confirmed before implementation. Until then, any missing or ambiguous source boundary is **SAFE UNKNOWN**.

## 2A. Approved asset authority

The approved V3 asset authority is:

- `projects/triumph-manipulator-landing/design/shared-assets/`.

This folder may provide approved logo assets, hero/media assets, vehicle/manipulator images, icons/social assets, review assets, and other visual materials when such files exist.

Shared assets support reconstruction from V1. They must not override V1 section structure, hierarchy, composition, visual intent, or screen order.

The previous Screen 01 missing-asset claim is invalid/incomplete where it was made without first inspecting `design/shared-assets/`. Future reconstruction must inspect `design/shared-assets/` before declaring required assets **SAFE UNKNOWN**.

## 3. Secondary authority

Secondary authority is limited to **explicit approved governance lessons**.

Allowed secondary use:

- V2 drift lessons.
- V2 known-failure references.
- V2 freeze-state lessons.
- Forge doctrine checklists and Website Factory governance that help interpret risk, evidence, escalation, and review depth.

Secondary authority may guide risk handling, QA posture, and escalation. It must not override V1 source authority for implementation structure, CSS, copy, section hierarchy, or visual reconstruction.

## 4. Not authority

The following are **not V3 implementation authority**:

- Accidental V2 implementation artifacts.
- Local V2 visual fixes.
- Accumulated V2 patch history.
- Inferred V2 redesign assumptions.
- V2 CSS, include structure, responsive patches, or local workaround patterns.
- V2 final visual state as a target replacement for V1 reconstruction.
- Any asset, class, layout, breakpoint, or composition choice sourced from V2 as implementation authority.

## 5. Conflict handling

If V1 source authority and secondary governance lessons conflict:

1. Stop the affected scope.
2. Record the conflict.
3. Mark **SAFE UNKNOWN**.
4. Request HITL if the decision changes structure, hierarchy, copy, CTA priority, responsive behavior, or production-readiness posture.

## 6. Authority rule

V3 source authority is conservative:

**V1 `design/v1` defines what to rebuild. `design/shared-assets` defines approved asset candidates. Forge doctrine defines how to govern the rebuild. V2 defines only what to avoid or learn from unless explicitly approved otherwise.**

---

*Documentation only — V3 source authority.*
