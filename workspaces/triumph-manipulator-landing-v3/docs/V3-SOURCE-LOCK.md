# Triumph Manipulator Landing V3 — Source Lock

## Purpose

This source lock starts the real V3 Forge execution for `triumph-manipulator-landing-v3`.

V3 is a clean rebuild from V1 source authority. It is not a V2 continuation, not a governance expansion phase, and not proof of autonomous frontend delivery.

## Primary V1 Layout Authority

The current repo-visible V1 layout authority surfaces are:

- `projects/triumph-manipulator-landing/design/v1/`
- `projects/triumph-manipulator-landing/design/v1/01.png`
- `projects/triumph-manipulator-landing/design/v1/02.png`
- `projects/triumph-manipulator-landing/design/v1/03.png`
- `projects/triumph-manipulator-landing/design/v1/04.png`
- `projects/triumph-manipulator-landing/design/v1/full.png`
- `projects/triumph-manipulator-landing/design/mockups-index.md` as the repo-visible V1 archive index.
- `projects/triumph-manipulator-landing/design/frontend-section-map.md` as repo-visible V1 continuity context.

The V1 mockups are treated as one vertical landing composition in natural order: `01.png` -> `02.png` -> `03.png` -> `04.png`. The `full.png` export is available as a continuity reference, but its exact role versus the four slice exports must be verified before implementation decisions depend on it.

V1 layout authority defines section structure, hierarchy, composition, visual intent, and screen order.

## Approved Asset Authority

Approved shared asset authority for V3 is:

- `projects/triumph-manipulator-landing/design/shared-assets/`

This folder may provide approved logo, hero/media, vehicle/manipulator, icon/social, review, and other visual materials when those files exist and are suitable for the active V1 reconstruction scope.

Shared assets do not override V1 layout authority. They must not change section structure, hierarchy, composition, visual intent, or screen order.

The previous Screen 01 pass treated assets as unknown without first registering and inspecting `design/shared-assets/`. That missing asset claim is invalid/incomplete. Future reconstruction must inspect `design/shared-assets/` before declaring any required asset `UNKNOWN`.

## Conditional Reference

`workspaces/triumph-manipulator-landing/` exists as the earlier V1-era frontend workspace. It may be inspected only as conditional V1 continuity context if the operator explicitly confirms it as part of the V1 source pack.

Until that confirmation, it is not implementation authority for V3 CSS, DOM, section naming, copy, or responsive behavior.

## Approved Governance References

The following documents may guide process, escalation, QA posture, and evidence discipline:

- `projects/triumph-manipulator-landing/V3-BATTLE-TEST-CHARTER.md`
- `projects/triumph-manipulator-landing/V3-SOURCE-AUTHORITY.md`
- `projects/triumph-manipulator-landing/V3-EXECUTION-BOUNDARIES.md`
- `projects/triumph-manipulator-landing/V3-GOVERNANCE-MODE.md`
- `projects/triumph-manipulator-landing/V3-FAILURE-CONDITIONS.md`
- `projects/triumph-manipulator-landing/V3-SUCCESS-CRITERIA.md`
- `agents/frontend-gulp-agent/README.md`
- `agents/mars-forge/README.md`
- `projects/mars-website-factory/adaptive-governance.md`
- `projects/mars-website-factory/delivery-survivability-model.md`

These references govern how to work. They do not replace V1 as the source of what to rebuild.

## Forbidden V2 Inheritance

The following are forbidden as V3 implementation authority:

- `workspaces/triumph-manipulator-landing-v2/` CSS, DOM, partials, scripts, includes, build patches, or local fixes.
- `projects/triumph-manipulator-landing/design/v2/` as a visual target.
- V2 section order, copy, breakpoint fixes, accumulated patch history, or freeze state.
- Any implementation decision justified by "V2 already solved it" unless the operator explicitly approves a governance lesson for V3 and the result does not override V1 source authority.

## Known Ambiguities

- Exact V1 source pack boundary is not fully operator-confirmed.
- Text/copy authority inside the V1 raster exports has not been extracted or verified.
- Asset authority is split from layout authority: `design/shared-assets/` is approved asset authority, but each asset still needs scope-specific suitability review before embedding.
- Responsive behavior is not defined by the visible V1 desktop-oriented raster exports.
- The relationship between the V1 four-slice exports and `full.png` needs confirmation before conflicts are resolved.
- The earlier V1 workspace may contain starter structure, but its authority status is conditional.

## SAFE UNKNOWN Areas

Mark SAFE UNKNOWN and stop the affected scope when:

- V1 raster source does not expose copy, hierarchy, asset origin, or responsive intent clearly enough.
- `design/shared-assets/` has not been inspected for a needed asset before an asset gap is declared.
- `full.png` conflicts with slice exports.
- The V1 workspace appears to answer a question not answered by the approved design exports.
- V2 appears to provide a convenient solution for missing V1 information.
- A reconstruction choice would change section meaning, CTA priority, trust hierarchy, visual rhythm, or mobile collapse behavior.

## Lock Statement

V3 source authority is locked as follows:

V1 `design/v1` defines what to rebuild. `design/shared-assets` defines approved asset candidates. Forge and Website Factory governance define how to execute and report. V2 defines only what to avoid or learn from, never what to implement.
