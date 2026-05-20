# Triumph Manipulator Landing V3 — Screen 02 Source Analysis

## Scope

This document governs Screen 02 reconstruction for the V3 survivability test. It is based on V1 authority and must not import V2 implementation structure, CSS, class names, responsive fixes, or accumulated patch history.

Primary layout authority:

- `projects/triumph-manipulator-landing/design/v1/02.png`
- `projects/triumph-manipulator-landing/design/v1/full.png` as Screen 01 -> Screen 02 continuity reference
- `projects/triumph-manipulator-landing/design/frontend-section-map.md`
- `projects/triumph-manipulator-landing/design/mockups-index.md`

Approved asset authority:

- `projects/triumph-manipulator-landing/design/shared-assets/`

## Section Purpose

Screen 02 converts the emotional first-screen promise into a practical fleet and pricing decision. It answers the immediate buyer question: which manipulator fits the load, what are the main working parameters, and what starting price should be expected.

The section is not a generic catalog. It is a compact commercial comparison block with three visible options:

- manipulator 5 tonnes;
- manipulator 7 tonnes;
- manipulator 10 tonnes.

Each option carries image proof, tonnage label, key dimensions, a fit-for-purpose line, a starting hourly price, and a direct order action.

## Hierarchy

Observed hierarchy in `02.png`:

1. Small red eyebrow: `ТЕХНИКА И ЦЕНЫ`.
2. Large black uppercase heading: `МАНИПУЛЯТОРЫ И ЦЕНЫ`.
3. Short supporting copy explaining equipment selection.
4. Secondary top-right CTA: `ПОЛУЧИТЬ РАСЧЁТ`, with a small reassurance line.
5. Three equal-width commercial cards.
6. Inside each card: image and tonnage badge first, model title second, three technical specs third, fit line fourth, price/action row fifth.

The card grid is the main content. The heading starts the section, but the price cards carry the actual decision pressure.

## Layout Rhythm

Screen 02 changes from the dark Screen 01 hero into a white/light commercial field. In `full.png`, the transition happens immediately after the dark trust strip. The rhythm is:

- Screen 01: dark, dense, urgent, visual/product-led.
- Screen 02: light, ordered, comparison-led, commercially explicit.

The white section needs enough top air to feel like a new block, but not so much that it becomes detached from Screen 01. The first row remains horizontally stable: heading group on the left, calculation CTA on the right.

The three-card grid forms the main rhythm. Cards are even, bordered, and calm. Red is used for section label, tonnage badges, and CTAs only.

## Visual Pressure

Primary visual pressure:

- oversized black uppercase heading;
- red section label;
- three large manipulator photos;
- red tonnage badges;
- bold hourly prices;
- red order buttons.

Secondary visual pressure:

- technical spec icons and values;
- purpose line inside each card;
- small reassurance notes under CTAs.

The section should not gain extra decoration, gradients, SaaS cards, soft shadows, or invented premium treatments. The source is plain, commercial, and operational.

## Trust / Commercial Role

Screen 02 extends trust from Screen 01 by making the service concrete:

- available equipment tiers are visible;
- buyer can compare load capacity and reach;
- prices are shown as starting points;
- operator assistance is promised after order click;
- the top CTA offers calculation without obligation.

This is a pricing and selection section, not a review section and not a lead-form section.

## Continuity Relationship With Screen 01

Screen 01 ends with a dark trust strip. Screen 02 begins on a white background with no heavy divider. Continuity depends on:

- preserving the same red accent;
- keeping strong uppercase heading rhythm;
- using compact operational proof language;
- maintaining a container width compatible with Screen 01;
- avoiding a decorative style shift that would make Screen 02 feel imported from another landing.

Screen 01 remains frozen-for-now. Only section-to-section spacing may be adjusted if the transition becomes structurally broken.

## Asset Inspection

Approved shared assets found for this scope:

- `shared-assets/hero-bg-final.png` belongs to Screen 01, not Screen 02 cards.
- `shared-assets/icons/icon-set.jpg` is a composite icon sheet, not individual ready-to-use card icons.
- `shared-assets/reviews/*` belong to later review/trust content, not Screen 02.
- `shared-assets/social/*` and `shared-assets/brand/*` do not apply to Screen 02 card imagery.

No approved standalone manipulator card photos were found for the three Screen 02 cards. Because the truck photos are central to the section, replacing them with CSS mockups or generic stock imagery is not authority-safe.

Implementation may therefore use a temporary reconstruction reference copied from `design/v1/02.png` for card image crops, clearly documented as reconstruction-only and not final production imagery.

## Responsive Pressure Areas

V1 authority is desktop raster-based. Responsive behavior is not directly specified.

High-pressure areas:

- top heading and right CTA may collide between tablet widths;
- three cards need to collapse without losing comparison order;
- spec rows inside cards can overflow if values stay in a three-column layout too long;
- price/action row needs stacking on narrow widths;
- source-screenshot image crops may become weaker when card aspect ratios change.

Responsive implementation should be conservative:

- desktop: three equal cards;
- tablet: one or two columns depending on available width;
- mobile: single-column cards with preserved internal hierarchy.

## SAFE UNKNOWN Areas

- Exact original standalone photo assets for the 5/7/10 tonne cards.
- Exact pixel measurements, type sizes, and spacings from `02.png`.
- Whether the card icons originally existed as separate vector assets or were represented only by the exported raster.
- Mobile/tablet source intent.
- Exact CTA/form destination behavior.
- Whether prices are final commercial truth or V1 mockup copy only.

## Approximation Boundaries

Allowed and disclosed:

- semantic HTML structure for the pricing/fleet section;
- SCSS values derived from visible relationships rather than claimed exact tokens;
- temporary use of `02.png` as a reconstruction image source for card media;
- governed Font Awesome operational icons where no individual approved V1 icons exist;
- conservative responsive stacking.

Not allowed without HITL:

- importing V2 markup, class names, CSS, assets, breakpoints, or patch logic;
- redesigning cards into a new premium/SaaS style;
- replacing manipulator card images with generic stock or CSS illustrations;
- changing the section role from pricing/fleet comparison to reviews, FAQ, or lead capture;
- hiding the prices or moving CTA priority away from the V1 structure.
