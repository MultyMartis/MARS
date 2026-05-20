# Triumph Manipulator Landing V3 — Screen 01 Source Analysis

## Scope

This document restarts Screen 01 analysis after the asset authority correction. It is analysis only and does not authorize implementation.

Primary layout authority:

- `projects/triumph-manipulator-landing/design/v1/01.png`
- `projects/triumph-manipulator-landing/design/v1/full.png` as continuity reference

Approved asset authority:

- `projects/triumph-manipulator-landing/design/shared-assets/`

Forbidden implementation authority:

- V2 workspace, V2 CSS, V2 DOM, V2 assets, V2 section naming, V2 responsive fixes, and V2 accumulated patch history.

## Source Hierarchy

1. `design/v1/01.png` controls Screen 01 layout, visual hierarchy, composition, and local screen intent.
2. `design/v1/full.png` confirms Screen 01 is the top slice of one continuous landing and shows its relation to the following pricing/trust content.
3. `design/shared-assets/` supplies approved asset candidates only after inspection.
4. V3 docs define execution boundaries and reporting discipline.

Shared assets may satisfy logo/social/review/media needs only where they support the V1 source. They must not change the V1 structure, hierarchy, composition, or screen order.

## Composition Clusters

Screen 01 is a dark high-contrast conversion hero with these visible clusters:

- Top header bar: logo at left, horizontal navigation centered, phone/social/callback group at right.
- Left hero content: oversized uppercase heading, red location line, short explanatory copy, rate badge, primary CTA, callback note, and six proof items.
- Right media field: dominant manipulator truck photo over construction/sunset background with small technical callouts around the crane/body/load zones.
- Bottom trust row: four dark cells with red line icons, strong metric/claim text, and smaller supporting copy.

The V1 composition gives the vehicle/media more width than the left copy block. The left block carries conversion hierarchy; the right block carries product proof and visual credibility.

## Header / Logo Role

The header belongs to Screen 01's dark hero environment. It is not a separate light page header.

Observed roles:

- Logo anchors brand identity at the far left.
- Navigation is secondary and compact.
- Phone number and social icons support fast contact.
- Red "Заказать звонок" button is a high-priority header action.

Asset mapping:

- `brand/logo--white.svg` is the approved candidate for the header logo.
- `social/WhatsApp-ico.svg` and `social/Telegram-ico.svg` are approved candidates for the two visible header social icons.
- `social/MAX-ico.svg` is not visible in the Screen 01 header and should not be introduced there.

## Hero Media / Background Role

The right-side hero media is not decorative only. It identifies the service: a real manipulator truck, crane boom, bed/body, construction context, and sunset-lit industrial atmosphere.

Observed media features:

- Large truck occupies the right half and overlaps the emotional background.
- Crane boom and hook are visible and labeled.
- Callouts identify `5-10 т стрела`, `кузов 6-7 м`, and `грузоподъёмность до 10 тонн`.
- Background shows construction materials/site context and orange sunset light.

Asset mapping:

- No standalone hero background, vehicle photo, manipulator image, or construction-site raster asset was found in `design/shared-assets/`.
- The exact source photo/media remains **SAFE UNKNOWN**.
- A CSS-drawn vehicle or generic replacement image would be an approximation, not a source-faithful asset transfer.
- Because this media is central to Screen 01, CSS mockups and semantic placeholders are forbidden as reconstruction substitutes.
- A temporary crop from `projects/triumph-manipulator-landing/design/v1/01.png` is allowed as a reconstruction asset until a final production asset decision is made.

## CTA Role

The primary CTA is a red filled button in the left conversion cluster. It sits below the rate badge and before the proof grid.

Observed CTA rhythm:

- Rate badge first establishes price frame.
- Main red CTA follows as the strongest action.
- Small callback note beside the CTA reinforces speed and urgency.
- Header callback button gives a second, smaller conversion route.

Approximation boundary:

- CTA copy, hierarchy, and relative order must remain tied to the V1 raster.
- Any change to CTA priority or location requires HITL because it affects conversion hierarchy.

## Trust / Proof Rhythm

Screen 01 uses two proof layers:

- Six left proof items under the CTA: compact operational promises with red outline icons.
- Four bottom trust cells: larger claims/metrics with red line icons and supporting copy.

This creates a rhythm of conversion first, service details second, broad trust third. The bottom row also bridges Screen 01 into the next landing section in `full.png`.

Asset mapping:

- Shared assets do not include the red line icons shown for these proof/trust items.
- Review assets (`reviews/yandex_logo.svg`, `reviews/avito_logo.svg`, `reviews/rate_star.svg`) belong to later review content and must not be inserted into Screen 01 proof areas.

## Responsive Pressure Areas

V1 authority is desktop raster-based. Responsive behavior is not directly specified.

High-pressure areas:

- Header navigation plus phone/social/callback may not fit narrow widths.
- Left content heading has large uppercase lines and red emphasis.
- CTA plus callback note may need stacking without changing priority.
- Six proof items may collapse from two columns to one while preserving order.
- Right truck/media field may lose meaning if cropped too aggressively.
- Bottom four trust cells likely need a 2x2 or single-column collapse, but exact mobile rhythm is **SAFE UNKNOWN**.

Responsive decisions must be conservative and explicitly documented during implementation.

## SAFE UNKNOWN Areas

- Original hero truck/photo/background asset source.
- Exact pixel measurements, type sizes, and spacing tokens from the raster.
- Exact text extraction for all small proof/trust labels where raster legibility is limited.
- Source of the red line proof/trust icons.
- Whether technical callout lines and labels are separate editable assets or baked into the hero image.
- Mobile/tablet layout intent.
- Exact relationship between `01.png` and `full.png` if any visual mismatch is later found.

## Approximation Boundaries

Allowed only with explicit disclosure during future implementation:

- Conservative HTML semantics for header, hero content, CTA, proof list, media figure, and trust row.
- CSS layout values derived from measured visual relationships rather than claimed exact tokens.
- Responsive stacking that preserves source order and hierarchy.
- Temporary raster crops from the V1 Screen 01 source PNG, when clearly documented as reconstruction-only assets.

Not allowed without HITL:

- Replacing the real manipulator media with a CSS illustration, semantic placeholder, or generic raster as source-equivalent media.
- Importing V2 structure, class names, breakpoints, or image choices.
- Moving review assets into Screen 01.
- Changing CTA priority, proof order, section meaning, or bottom trust rhythm.

## Current Implementation Decision

Do not rebuild Screen 01 in this task. The previous implementation has been reset again after repeating the failed CSS/semantic hero-media approach. Future implementation must start from this analysis, inspect `V3-ASSET-AUTHORITY.md`, and use the documented temporary source crops when the central hero media is required.

Header was also reset after the incorrect first Screen 01 reconstruction. Final header reconstruction remains pending and must use V1 layout authority plus `design/shared-assets/` asset authority.
