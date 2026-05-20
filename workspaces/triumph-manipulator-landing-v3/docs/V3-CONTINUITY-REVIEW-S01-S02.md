# Triumph Manipulator Landing V3 — Continuity Review S01/S02

## Scope

This review covers the current V3 implementation continuity between:

- Screen 01: `hero-screen-01`
- Screen 02: `equipment-pricing-screen-02`
- the transition from the dark hero/trust strip into the light equipment/pricing section

Primary authority:

- `projects/triumph-manipulator-landing/design/v1/01.png`
- `projects/triumph-manipulator-landing/design/v1/02.png`
- `projects/triumph-manipulator-landing/design/v1/full.png`
- `projects/triumph-manipulator-landing/design/frontend-section-map.md`
- `projects/triumph-manipulator-landing/design/mockups-index.md`

Forbidden authority:

- V2 CSS, DOM, assets, breakpoint fixes, or accumulated implementation decisions.

## Density Rhythm

Screen 01 is intentionally dense: header, oversized offer, rate badge, CTA, proof grid, and bottom trust strip all sit inside a dark commercial first impression. Screen 02 is less atmospheric but still dense because the three equipment cards are the decision engine.

Current continuity is broadly survivable, but Screen 02 had slightly too much top/bottom air for the `full.png` rhythm. The pricing section must feel like the next operational step after the Screen 01 trust strip, not a detached brochure block.

## Spacing Rhythm

Observed source rhythm:

- Screen 01 ends with a dark trust strip at the bottom edge.
- Screen 02 begins immediately on a light field with the red eyebrow and large uppercase heading.
- The transition needs enough top air for section recognition, but not a large gap.

Current implementation risk:

- Screen 02 vertical padding was a little generous relative to the continuous landing export.
- The light section background was slightly grey, which softened the transition away from the sharper source white field.

Minimal stabilization decision:

- Normalize Screen 02 background to white.
- Slightly reduce Screen 02 vertical padding.
- Keep Screen 01 layout intact.

## Atmosphere Continuity

Screen 01 carries a dark, high-pressure construction atmosphere. Screen 02 intentionally drops into a white commercial comparison field. The continuity mechanism is not shared background mood; it is shared red accent, uppercase typography, operational proof language, and compact conversion hierarchy.

The transition survives if Screen 02 remains plain, commercial, and equipment-led. It would fail if Screen 02 gained soft SaaS decoration, heavy shadows, decorative gradients, or unrelated typography.

## Commercial Intensity

Screen 01 commercial pressure:

- immediate service offer;
- hourly price frame;
- primary application CTA;
- callback urgency;
- proof and trust claims.

Screen 02 commercial pressure:

- equipment options;
- visible parameters;
- prices;
- direct order buttons;
- calculation CTA.

The commercial intensity is consistent. Screen 02 does not need more decoration or additional persuasion; it needs to keep the comparison grid clear.

## Typography Continuity

The current typography relationship is aligned with V1:

- oversized uppercase headings;
- strong weight;
- tight tracking;
- red accent line/eyebrow language;
- compact supporting copy.

No typography replacement is needed. Russian line-integrity discipline must continue in visible copy with protected short words and numeric groups.

## Visual Pressure

Screen 01 pressure is concentrated in the hero title, truck media, red CTA, and bottom trust strip. Screen 02 pressure shifts to the pricing heading, card imagery, red tonnage labels, prices, and order buttons.

This is a healthy pressure transfer. The only stabilization need is to avoid visual decompression between S01 and S02.

## Card Language

Screen 01 bottom trust cells and Screen 02 equipment cards use different card roles:

- Screen 01 trust cells: dark metric/proof strip.
- Screen 02 cards: white equipment comparison cards.

They still share operational density, red icon/accent usage, and compact proof language. Screen 03 should continue this by using simple bordered proof/review cards, not a new card aesthetic.

## Section Transition Quality

The transition is source-consistent:

- dark proof strip closes Screen 01;
- light pricing field opens Screen 02;
- red accent and uppercase rhythm bridge the mood change.

Risk:

- too much light-section padding can make Screen 02 feel disconnected.
- too much grey background can make it feel like a different landing system.

Stabilization:

- reduce Screen 02 vertical spacing slightly;
- keep the light field cleaner and closer to source white.

## "Same Landing?" Survivability

S01 and S02 survive as the same landing if:

- red accent remains identical;
- headings stay heavy and uppercase;
- proof language stays operational;
- cards remain practical and rectangular;
- section spacing stays compact enough for one continuous scroll;
- V2 or modern SaaS styling is not imported.

Verdict: survivable after minimal spacing/background normalization. No redesign is warranted.

## SAFE UNKNOWN

- Exact pixel spacing between the Screen 01 trust strip and Screen 02 heading in the original working file.
- Exact intended mobile/tablet transition behavior.
- Whether `full.png` and individual slice exports differ in any hidden crop or export state.
- Exact source typography token values beyond visible raster approximation.

## Approximation Boundary

The stabilization is limited to CSS rhythm correction in Screen 02. It does not claim pixel-perfect reproduction and does not change section meaning, hierarchy, card content, or CTA priority.
