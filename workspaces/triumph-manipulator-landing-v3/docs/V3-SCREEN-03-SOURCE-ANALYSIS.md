# Triumph Manipulator Landing V3 — Screen 03 Source Analysis

## Scope

This document governs Screen 03 reconstruction for V3.

Primary layout authority:

- `projects/triumph-manipulator-landing/design/v1/03.png`
- `projects/triumph-manipulator-landing/design/v1/full.png` as S02 -> S03 -> S04 continuity reference
- `projects/triumph-manipulator-landing/design/frontend-section-map.md`
- `projects/triumph-manipulator-landing/design/mockups-index.md`

Approved asset authority:

- `projects/triumph-manipulator-landing/design/shared-assets/`

Forbidden authority:

- V2 workspace, V2 CSS, V2 DOM, V2 assets, V2 section order, V2 responsive fixes, or V2 patch history.

## Section Role

Screen 03 is a trust and review bridge. It follows the equipment/pricing comparison and answers the buyer's next concern: whether the company is reliable enough for private clients, construction companies, and business customers.

It is not a generic testimonial carousel, not a decorative awards block, and not a lead form. It combines operational trust claims with visible review evidence.

## Commercial Purpose

The section supports conversion by reducing risk after the buyer has seen equipment tiers and prices:

- confirms own fleet and technical condition;
- confirms experienced operators;
- confirms transparent pricing before dispatch;
- confirms legal/business-ready payment with VAT;
- shows public review sources and sample reviews;
- reinforces delivery geography and response speed in the bottom metrics strip.

The commercial pressure is moderate but important. It should feel credible and operational, not celebratory or over-designed.

## Hierarchy

Observed hierarchy in `03.png`:

1. Red eyebrow: `ПОЧЕМУ НАМ ДОВЕРЯЮТ`.
2. Large dark heading: `Работаем с частными клиентами, строительными компаниями и бизнесом`.
3. Short explanatory paragraph about punctual delivery, agreed cost, and task-specific equipment selection.
4. Four left proof cards in a 2x2 grid.
5. Right review summary card with large `4.9`, red stars, review-source logos, and review CTA.
6. Three individual review rows.
7. Muted integration placeholder note.
8. Dark bottom metrics strip with four operational claims.

The left proof block and right review block are peers. Neither should dominate so strongly that the two-column trust/review relationship collapses on desktop.

## Pressure Zones

Primary pressure:

- the large heading;
- the 4.9 rating;
- the red stars;
- the four proof cards;
- the dark bottom metrics strip.

Secondary pressure:

- review names and star rows;
- review-source labels/logos;
- the red review CTA;
- muted integration note.

The section should not introduce large illustrations, new gradients, floating glass cards, or SaaS-style testimonial widgets. Source pressure is rectangular, compact, and evidence-based.

## Relationship With Previous Sections

Relationship with Screen 01:

- Screen 03 reuses dark metric-strip language from Screen 01, but after the review/proof area.
- Red line icons and operational claims continue the same service vocabulary.

Relationship with Screen 02:

- Screen 02 proves equipment and prices.
- Screen 03 proves reliability and trust after that decision point.
- Both screens live on a light field and use simple bordered cards.

Screen 03 must therefore continue Screen 02's white commercial surface and Screen 01's trust-strip intensity without becoming a visually separate mini-site.

## Responsive Pressure Areas

V1 authority is desktop raster-based. Responsive behavior is not directly specified.

High-pressure areas:

- two-column proof/review layout can become cramped on tablets;
- four proof cards need to retain reading order;
- review summary logos and CTA can collide;
- individual review rows can overflow if metadata stays horizontal too long;
- dark metrics strip must collapse without detached giant whitespace;
- avatar crops from the V1 source may lose clarity if scaled too far.

Conservative responsive behavior:

- desktop: two columns, proof cards left, review stack right;
- tablet: single-column section flow with proof block before review evidence;
- mobile: one-column proof cards, simplified review metadata, metric strip stacked.

## Asset Inspection

Approved shared review assets found:

- `shared-assets/reviews/yandex_logo.svg`
- `shared-assets/reviews/avito_logo.svg`
- `shared-assets/reviews/rate_star.svg`

These are suitable for Screen 03 review-source/rating usage and were copied into the V3 workspace without renaming or recompression.

No approved ready assets were found for:

- 2GIS logo;
- reviewer avatar portraits;
- red line proof/metric icons as separate source assets.

Implementation may use governed Font Awesome line icons for proof/metric semantics. Reviewer avatars may be approximated from the V1 `03.png` source raster as reconstruction-only background crops because they are visible but secondary evidence, not the central section artwork.

## SAFE UNKNOWN

- Exact original review copy and whether the visible sample reviews are production text or mockup text.
- Exact source and licensing status of reviewer avatar photos.
- Exact 2GIS logo asset source.
- Whether live reviews were intended to be embedded dynamically or entered as static fallback content.
- Mobile/tablet source intent.
- Exact typography, spacing, and card measurements from the original design file.
- Whether rating `4.9` and review platform set are current commercial truth.

## Approximation Boundaries

Allowed and disclosed:

- semantic HTML structure for the trust/review section;
- SCSS values derived from visible raster relationships;
- approved shared review SVGs used directly;
- temporary use of `03.png` as a reconstruction source for small reviewer avatar crops;
- CSS text fallback for 2GIS label where no approved ready logo exists;
- governed Font Awesome icons where source line icons are unavailable;
- conservative responsive stacking.

Not allowed without HITL:

- importing V2 review/trust structure or styling;
- inventing a new testimonial carousel;
- changing the section role into a lead form, FAQ, or awards block;
- claiming live review integration exists;
- replacing the V1 commercial trust rhythm with modern SaaS social-proof styling;
- presenting reconstruction avatar crops as final production assets.
