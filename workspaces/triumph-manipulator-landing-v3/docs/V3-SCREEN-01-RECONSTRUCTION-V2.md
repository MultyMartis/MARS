# Triumph Manipulator Landing V3 — Screen 01 Reconstruction V2 Notes

## Scope

This note records the first valid Screen 01 reconstruction benchmark implementation.

Implemented scope:

- Header cluster: logo, navigation, phone, approved social icons, callback action.
- Hero conversion cluster: title, explanatory copy, rate badge, primary CTA, callback note, proof list.
- Hero media: approved shared background copied as-is to `src/assets/img/screen-01/hero-bg-final.png`.
- Bottom trust strip: four source-supported trust cells.

Not implemented:

- Screen 02+.
- Animation or polish systems.
- Screen 02+ production asset decisions.

## Asset Usage

Approved shared assets used:

- `src/assets/svg/brand/logo--white.svg`
- `src/assets/svg/social/WhatsApp-ico.svg`
- `src/assets/svg/social/Telegram-ico.svg`
- `src/assets/favicon/favicon.svg`
- `src/assets/img/screen-01/hero-bg-final.png`

Temporary reconstruction assets used:

- None for the live Screen 01 background.

`hero-bg-final.png` comes from `projects/triumph-manipulator-landing/design/shared-assets/` and is copied without resize, crop, or recompression. Observed original dimensions are `1672 x 941`; observed file size is `2,266,334 bytes`.

Screen 01 V3 now uses `hero-bg-final.png` as the integrated first-screen atmospheric background behind both the header and hero. `screen-01-environment.png` is deprecated/wrong for implementation because it is a smaller derived crop (`952 x 741`) where an approved ready shared asset exists.

## Font Awesome Usage

Approved local source:

- `shared/assets/icon-libraries/Font Awesome Pro 5.15.4/`

V3 implementation files:

- `src/assets/vendor/fontawesome/css/screen-01-fa.css`
- `src/assets/vendor/fontawesome/webfonts/fa-solid-900.svg`

The V3 build preserves the local `css/` and `webfonts/` folder relationship under `dist/assets/vendor/fontawesome/`. The Screen 01 subset uses one restrained operational family: `fas` / Font Awesome 5 solid.

Exact classes used:

- Proof list: `fas fa-weight-hanging`, `fas fa-file-invoice`, `fas fa-clock`, `fas fa-route`, `fas fa-map-marker-alt`, `fas fa-truck-loading`
- Trust strip: `fas fa-clock`, `fas fa-file-invoice`, `fas fa-tools`, `fas fa-user-hard-hat`

Header social icons remain the approved shared SVG assets because they already match the Screen 01 visual role better than Font Awesome social glyphs.

## Responsive Assumptions

- Desktop remains the primary authority because V1 is a desktop raster.
- Header navigation is allowed to wrap on tablet and hide on narrow mobile to preserve contact actions.
- The conversion cluster remains before media on mobile.
- The six proof items collapse from two columns to one while preserving order.
- The bottom trust strip collapses from four columns to two columns, then one column.
- The approved background may be position-shifted on tablet/mobile to preserve recognizability of the manipulator while keeping text readable.

## SAFE UNKNOWN

- Exact text and icon source for all small proof/trust items.
- Exact V1 typography, spacing, and breakpoints.
- Mobile-specific source intent.
- Whether media callouts were editable elements or baked into the raster.

## Approximation Disclosures

- Header, hero content, CTA, proof list, and trust strip are semantic HTML/CSS reconstructions derived from the V1 raster, not pixel-exact exports.
- Proof and trust icons are restrained local Font Awesome solid operational icons, not claimed source icon matches.
- First-screen construction/background atmosphere is implemented from the approved shared `hero-bg-final.png` with dark readability overlays.
- Breakpoints are conservative survivability choices, not source-approved mobile art direction.

## V2 Boundary

This implementation was built from V1 source analysis and approved shared assets. V2 implementation files, CSS, DOM, breakpoints, and assets were not used as authority.
