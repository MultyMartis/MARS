# Triumph Manipulator Landing V3 — Implementation Rules

## Purpose

These rules protect V3 as a clean reconstruction from V1 source authority.

They apply to all future source, style, script, asset, QA, and reporting work inside `workspaces/triumph-manipulator-landing-v3/`.

## Allowed

- Clean reconstruction from approved V1 source authority.
- Use `projects/triumph-manipulator-landing/design/v1/` as layout/design authority.
- Use `projects/triumph-manipulator-landing/design/shared-assets/` as approved asset authority after scope-specific inspection.
- Use approved ready shared assets as-is by default when they exist for the active scope.
- Adaptive governance scaled to source ambiguity, implementation risk, and production consequence.
- Proportional QA with evidence-scoped confidence.
- Semantic implementation where section roles are named from source analysis, not inherited from V2.
- Survivable source structure with readable ownership for pages, partials, sections, components, SCSS, JS, and assets.
- Conservative responsive interpretation with approximation disclosure.
- Temporary raster crops from V1 source PNGs when a central source visual is required and no approved standalone asset exists.
- SAFE UNKNOWN when evidence is incomplete.
- HITL escalation for source expansion, strategic changes, or material uncertainty.

## Forbidden

- V2 patch reuse.
- V2 CSS, DOM, includes, JS, responsive fixes, local workarounds, or accumulated patch history.
- Declaring logo, hero/media, vehicle/manipulator, social/icon, review, or other visual assets `UNKNOWN` before inspecting `design/shared-assets/`.
- Letting shared assets override V1 section structure, hierarchy, composition, visual intent, or screen order.
- Resizing, arbitrarily renaming, recompressing, cropping, recreating, or replacing an approved ready shared asset with a derived asset unless explicitly required and documented.
- Hidden approximation.
- CSS mockups for key source visuals.
- Semantic placeholder media when the source visual is central to the section.
- Emergency hacks that bypass source structure or future edit safety.
- Uncontrolled utility sprawl.
- Fake fidelity claims.
- Screenshot worship that ignores semantic intent, maintainability, accessibility, or responsive survivability.
- Endless perfection loops that prevent deployable, evidence-based progress.
- Production-readiness claims without build, QA, source, and handoff evidence.

## Source Ownership

- `src/pages/` owns page entry files.
- `src/partials/layout/` owns layout shell partials.
- `src/partials/sections/` owns future source-derived section partials.
- `src/partials/components/` owns reusable include fragments only after repetition justifies extraction.
- `src/scss/base/` owns reset and base document rules.
- `src/scss/layout/` owns layout shell rules.
- `src/scss/sections/` owns future section styles.
- `src/scss/components/` owns reusable component styles only when component extraction is justified.
- `src/scss/utils/` owns tokens, variables, mixins, and narrow utilities.
- `src/js/` owns behavior. Do not add JS for visual patching.
- `src/assets/` owns implementation-ready assets only after authority is approved and the asset is actually needed.
- `dist/` is generated output. Do not hand-edit it.

Do not copy all shared assets into V3 by default. Copy only the approved asset files needed by the active reconstruction scope.

## V2 Contamination Protections

- Do not open V2 implementation files to answer V3 implementation questions unless the task is explicitly governance/audit comparison.
- Do not copy class names, partial names, section order, SCSS modules, JS behavior, breakpoint values, or asset placement from V2.
- Do not use V2 as fallback implementation authority for assets missing from `design/shared-assets/`.
- If a V2 lesson is relevant, document it as governance-only and verify it does not override V1 authority.
- If a V3 implementation choice resembles V2, justify it from V1 source, frontend fundamentals, or explicit operator approval.

## Approximation Rules

Approximation is allowed only when:

- The source gap is stated.
- The chosen implementation is conservative.
- The approximation is easy to find later.
- Future correction has a clear file owner.
- Confidence language remains limited.

Approximation is not allowed when it changes business meaning, CTA priority, section hierarchy, proof order, or responsive intent without HITL.

Approximation is also not allowed for central source visuals. If V1 requires a key hero/media visual and no approved standalone asset exists, do not replace it with CSS illustration, generic gradients, or semantic placeholder markup.

## Temporary Source Crop Assets

Temporary source crops are allowed only as reconstruction support when the V1 raster contains a required key visual that is not available as an approved standalone asset.

Rules:

- Do not create or use a derived crop when an approved ready shared asset exists for the same purpose.
- Crop only from the relevant V1 source PNG.
- Store temporary crops under a clearly named reconstruction asset path.
- Document exact extraction source, crop purpose, and production status.
- Record original source, original dimensions, transformed dimensions, and reason for transformation.
- Do not present temporary crops as final production assets.
- Keep final production asset replacement as a separate future approval/implementation task.

For Screen 01, `projects/triumph-manipulator-landing/design/shared-assets/hero-bg-final.png` is the preferred background authority if present. The implementation copy must preserve original dimensions and byte content; `src/assets/reconstruction/screen-01/screen-01-environment.png` is not an approved background source.

## Russian HTML Typography

Visible Russian HTML copy must not allow short prepositions, conjunctions, or particles to break away from the following word.

Use `&nbsp;` where a line break is forbidden by Russian reading logic.

Examples:

- `в&nbsp;Краснодаре`
- `и&nbsp;краю`
- `с&nbsp;НДС`
- `от&nbsp;30&nbsp;минут`
- `до&nbsp;10&nbsp;тонн`
- `за&nbsp;1&nbsp;час`
- `по&nbsp;Краснодару`
- `для&nbsp;юр.&nbsp;лиц`

Apply this rule in visible HTML copy, especially headings, CTA text, benefits, trust strips, forms, and cards. Do not overuse `&nbsp;` in long phrases where ordinary wrapping remains readable.

## Build Discipline

- Source-first edits only.
- Build output is disposable and regenerated from `src/`.
- Do not hand-edit `dist/`.
- Keep initial build scripts minimal and readable.
- Avoid dependencies that are not needed for the current static frontend baseline.

## Initialization Boundary

This rules file authorizes readiness setup only.

It does not authorize full section rebuild, hero reconstruction, visual polishing, V2 implementation reuse, or production readiness claims.

Header was also reset after the incorrect first Screen 01 reconstruction. Final header reconstruction remains pending and must use V1 layout authority plus `design/shared-assets/` asset authority.
