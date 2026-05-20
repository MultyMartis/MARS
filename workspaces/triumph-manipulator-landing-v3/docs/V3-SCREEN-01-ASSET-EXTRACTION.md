# Triumph Manipulator Landing V3 — Screen 01 Asset Extraction

## Purpose

This document records temporary reconstruction assets extracted from the V1 Screen 01 source and the later authority correction for the approved Screen 01 background.

Temporary reconstruction files are not final production assets. They exist only to support source-faithful Screen 01 reconstruction when no approved standalone hero truck/background asset exists.

Approved shared assets must be used as-is by default. Derived assets are allowed only when no approved ready asset exists, source crop is required for reconstruction, the transformation is documented, and the original source, dimensions, and reason are recorded.

## Source

- Source PNG: `projects/triumph-manipulator-landing/design/v1/01.png`
- Source dimensions observed during extraction: `1672 x 941`
- Extraction date: 2026-05-18

## Output Folder

- `workspaces/triumph-manipulator-landing-v3/src/assets/reconstruction/screen-01/`

## Created Assets

## Approved Background Authority

### `hero-bg-final.png`

- Source: `projects/triumph-manipulator-landing/design/shared-assets/hero-bg-final.png`
- Original dimensions: `1672 x 941`
- Original file size: `2,266,334 bytes`
- V3 implementation copy: `src/assets/img/screen-01/hero-bg-final.png`
- Purpose: full Screen 01 background covering the header and hero shell
- Status: approved shared asset; preferred Screen 01 background authority if present
- Transformation: none; copied as-is without resize, crop, or recompression

### `screen-01-reference.png`

- Extraction: full copy of `design/v1/01.png`
- Purpose: local visual comparison reference for Screen 01 reconstruction
- Status: temporary reconstruction reference only
- Production status: not approved as a final implementation asset

### `screen-01-hero-media.png`

- Extraction: raster crop from `design/v1/01.png`
- Crop rectangle: `x=720`, `y=82`, `width=952`, `height=741`
- Included source visual: right-side manipulator truck, crane, construction/sunset background, and baked-in technical callouts
- Purpose: temporary source-faithful hero media support for future Screen 01 reconstruction
- Status: temporary reconstruction asset only
- Production status: not approved as a final production asset

### `screen-01-environment.png`

- Extraction: derived duplicate/crop matching the temporary `952 x 741` reconstruction media dimensions
- Purpose claimed by previous implementation: Screen 01 background
- Status: deprecated / wrong for Screen 01 implementation because approved `hero-bg-final.png` exists in `design/shared-assets/`
- Production status: forbidden for CSS/HTML/runtime references

## Authority Notes

- `design/shared-assets/` remains the approved authority for standalone shared assets such as logo and visible social icons.
- `design/shared-assets/hero-bg-final.png` provides the approved Screen 01 hero truck/background asset and must be used as-is by default.
- These temporary crops do not expand shared asset authority and must remain clearly separated under `src/assets/reconstruction/`.
- Future derived asset work requires a documented absence of an approved ready asset plus source, dimensions, transformation, and reason.

## Forbidden Use

- Do not treat these crops as final production-ready media.
- Do not use these crops to claim full asset fidelity beyond the raster source area they preserve.
- Do not use `screen-01-environment.png` as Screen 01 background.
- Do not replace central source visuals with CSS mockups, generic backgrounds, or semantic placeholders.
- Do not use V2 assets or V2 implementation paths as fallback authority.
