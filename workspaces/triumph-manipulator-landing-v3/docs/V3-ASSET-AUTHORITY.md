# Triumph Manipulator Landing V3 — Asset Authority

## Purpose

This document registers the approved shared asset authority for V3 and records the current inspection result for `projects/triumph-manipulator-landing/design/shared-assets/`.

V3 layout, hierarchy, composition, and screen order remain governed by `projects/triumph-manipulator-landing/design/v1/`. Shared assets are approved asset candidates only; they do not override V1 visual intent.

## Asset Authority Root

Approved V3 asset authority:

- `projects/triumph-manipulator-landing/design/shared-assets/`

Future reconstruction must inspect this folder before declaring logo, hero/media, vehicle/manipulator, social/icon, review, or other visual materials **SAFE UNKNOWN**.

Do not copy the folder wholesale into V3. Copy only the exact asset files required by the active implementation scope.

Approved shared assets must be used as-is by default:

- Do not resize, rename arbitrarily, recompress, crop, recreate, or replace an approved ready asset with a derived asset.
- Derived assets are allowed only when no approved ready asset exists, source crop is required for reconstruction, the transformation is documented, and the original source, dimensions, and reason are recorded.
- If `projects/triumph-manipulator-landing/design/shared-assets/` contains a ready asset suitable for the implementation scope, that asset is the preferred authority over reconstruction crops.

## Available Logo Assets

- `brand/logo--dark.svg`
- `brand/logo--white.svg`
- `brand/favicon.svg`

Screen 01 suitability:

- `brand/logo--white.svg` is suitable for the dark Screen 01 header shown in `design/v1/01.png`.
- `brand/logo--dark.svg` is suitable for light-background contexts outside Screen 01.
- `brand/favicon.svg` is suitable for favicon/browser metadata only, not as a replacement for the header logo.

## Available Hero / Media Assets

- `hero-bg-final.png`

Screen 01 suitability:

- `hero-bg-final.png` is the approved ready Screen 01 background asset when present in `design/shared-assets/`.
- Observed original dimensions: `1672 x 941`.
- Observed file size: `2,266,334 bytes`.
- It includes the sunset construction environment, truck, manipulator, and baked technical callout composition suitable for the first-screen background.
- Because this approved ready asset exists, Screen 01 must use it as-is by default instead of temporary reconstruction crops.

## Available Social / Icon Assets

- `social/WhatsApp-ico.svg`
- `social/Telegram-ico.svg`
- `social/MAX-ico.svg`

Screen 01 suitability:

- `WhatsApp-ico.svg` and `Telegram-ico.svg` match the two circular social icons visible in the Screen 01 header.
- `MAX-ico.svg` appears later in the full landing footer/contact zone and is not visible in Screen 01 header authority.

## Available Review Assets

- `reviews/yandex_logo.svg`
- `reviews/avito_logo.svg`
- `reviews/rate_star.svg`

Screen 01 suitability:

- These assets are not suitable for Screen 01 because the V1 Screen 01 authority does not show the review-rating block.
- They are suitable candidates for later review/trust sections if those sections are reconstructed from the relevant V1 source slice.

## What Remains SAFE UNKNOWN

- Whether Screen 01 callout label lines around the manipulator image were editable vector/text assets before being baked into the approved hero raster.
- Exact icon assets for the six left proof items and four bottom trust items; current shared assets do not include those red line icons.
- Any mobile-specific asset substitutions; V1 authority is desktop raster-based.

## What Must Not Be Used

- V2 assets, V2 image choices, V2 implementation paths, V2 icon placement, or V2 responsive substitutions as V3 implementation authority.
- Shared review assets inside Screen 01 unless V1 Screen 01 source shows that review block.
- `logo--dark.svg` on the dark Screen 01 header if it would reduce contrast or contradict the V1 white logo treatment.
- Any generated CSS-only fake vehicle, semantic placeholder, or generic background as a replacement for central Screen 01 hero media.

## Temporary Reconstruction Assets

Temporary reconstruction crops may be created from V1 source PNGs only when no approved standalone asset exists for a required key visual.

For Screen 01, temporary crops belong under:

- `workspaces/triumph-manipulator-landing-v3/src/assets/reconstruction/screen-01/`

Documentation requirements:

- Name the source PNG and crop coordinates or extraction scope.
- State that the crop is reconstruction-only.
- State that final production asset replacement remains separate.
- Do not mix temporary reconstruction crops with approved shared-assets authority.
- Do not use temporary crops when `hero-bg-final.png` or another approved ready asset exists for the same Screen 01 background purpose.

## Current Asset Decision

For Screen 01 background, use `projects/triumph-manipulator-landing/design/shared-assets/hero-bg-final.png` as the preferred background authority if present. The V3 workspace copy is `src/assets/img/screen-01/hero-bg-final.png`, copied without resizing or recompression.

`src/assets/reconstruction/screen-01/screen-01-environment.png` is a wrong derived background for Screen 01 because it duplicates/crops the approved background at smaller dimensions (`952 x 741`). It may remain only as deprecated reconstruction evidence and must not be referenced by HTML, SCSS, CSS, or runtime output.
