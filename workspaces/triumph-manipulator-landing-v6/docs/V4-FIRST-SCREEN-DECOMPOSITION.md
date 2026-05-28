# Triumph Manipulator Landing V4 — First-Screen Decomposition

## 1. Purpose

This document prevents first-screen collapse during V4 reconstruction planning.

The first viewport may visually contain several systems at once. V4 must keep ownership separate so implementation does not become a hero hack or inherited patch stack.

## 2. Critical Rule

**HEADER != HERO != SLIDER**

This rule applies even when header, hero content, background imagery, and potential slider-like visuals occupy the same viewport.

## 3. First-Screen Systems

| System | Owns | Does not own |
|---|---|---|
| Header system | Logo placement, navigation, contact affordances, desktop/mobile header states. | Hero copy, hero background, slider behavior, section content. |
| First-screen shell | Overall first viewport structure, layering boundaries, spatial relationship between header and hero. | Copy meaning, CTA wording, image sourcing. |
| Hero content system | H1/offer, support copy, commercial hierarchy, CTA group, trust or benefit snippets if source proves them. | Header navigation, persistent menu behavior, background asset source. |
| Hero background ownership | Background image/color/overlay/crop if V1 proves it. | Hero copy, CTA priority, slider interaction. |
| Future slider possibility | Only source-proven carousel/slide behavior, if present. | Static hero reconstruction, header behavior, background ownership by default. |
| Mobile header ownership | Mobile brand/nav/contact survivability. | Mobile hero layout fixes or hidden desktop patch inheritance. |
| Navigation survivability | Readable route/contact access under responsive collapse. | Visual redesign or invented IA. |

## 4. Header System

Header reconstruction must be treated as a system with its own source authority.

Required findings before implementation:

- Which logo variant is source-correct for the first-screen background.
- Whether navigation is visible in V1.
- Which links are present and whether copy is legible enough to lock.
- Whether phone/contact/social controls are present.
- Whether header overlays the hero, occupies its own band, or participates in a first-screen shell.
- How mobile navigation should survive when desktop layout collapses.

SAFE UNKNOWN:

- Exact V1 header visual content is not confirmed until `design/v1/01.png` is visible and inspected.

## 5. First-Screen Shell

The first-screen shell owns the structural relationship between:

- Header.
- Hero content.
- Background/image layer.
- Primary conversion controls.
- Any top-of-page support elements.

Implementation must not treat the first viewport as one monolithic `hero` partial if separate ownership is visible in V1.

## 6. Hero Content System

Hero content must be reconstructed from V1 source evidence only.

Before implementation, identify:

- H1 text.
- Supporting text.
- Primary CTA.
- Secondary CTA, if present.
- Price/time/region/service claims, if present.
- Trust/proof snippets, if present.

Russian typography survivability is mandatory in HTML. Examples:

- `в&nbsp;Краснодаре`
- `с&nbsp;НДС`
- `от&nbsp;30&nbsp;минут`
- `и&nbsp;т.д.`
- `для&nbsp;юр.&nbsp;лиц`

## 7. Hero Background Ownership

Hero background must not be inferred from available shared assets.

Allowed sources:

- V1 first-screen raster evidence.
- Approved shared asset only when source and operator confirm it represents the intended background.
- Explicit human decision.

Forbidden:

- Reusing V3 crops.
- Reusing V3 hero hacks.
- Creating decorative replacement backgrounds.
- Cropping or resizing approved assets without lineage and reason.
- Duplicating background-baked labels, callouts, numbers, arrows, technical marks, or annotations as HTML/CSS overlays.

Baked annotation rule:

- Approved background/image assets own the labels, callouts, numbers, arrows, technical marks, and annotations already visible in their pixels.
- HTML annotations may be created only when source evidence shows them as independent UI/text elements, they are not already baked into the image, they are needed for accessibility/content reasons, and the decision is documented.
- For Screen 01, `hero-bg-final.png` already contains baked technical annotations/callouts; no `hero-screen-01__annotations` layer or equivalent duplicate overlay is allowed.

## 8. Slider Possibility

No slider implementation is authorized by default.

If V1 appears slider-like, V4 must distinguish:

- Static visual carousel motif.
- Actual interactive slider requirement.
- Background image sequence.
- Decorative frame.

Until proven, slider behavior is SAFE UNKNOWN and must not be implemented.

## 9. Mobile Header Ownership

Mobile header must remain a header system, not a side effect of hero breakpoint patches.

Planning requirements:

- Logo remains identifiable.
- Contact/navigation entry remains reachable.
- Header hit targets are not hidden by hero composition.
- Mobile menu state, if needed, is documented before implementation.
- No desktop-only navigation assumption is allowed.

## 10. Navigation Survivability

Navigation is survivable when a human user can still understand:

- Where the brand is.
- How to contact the company.
- How to move through anchored sections, if anchors exist.
- What action is primary.

This task does not implement navigation. It only defines the ownership boundary for the future reconstruction.

## 11. Current Decomposition Result

Confirmed:

- V4 first screen must be decomposed into separate systems before implementation.
- Header, hero, background, and slider possibility are separate concerns.
- Mobile header ownership is mandatory.

SAFE UNKNOWN:

- Exact header content.
- Exact H1 and CTA wording.
- Exact first-screen image/background.
- Whether any slider behavior exists.
- Exact mobile collapse behavior.
