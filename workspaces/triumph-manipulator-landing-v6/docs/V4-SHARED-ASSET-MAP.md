# Triumph Manipulator Landing V4 — Shared Asset Map

## 1. Purpose

This document maps repo-visible approved shared assets for the V4 clean reconstruction run.

`design/shared-assets/` may provide reusable visual materials. It does not define landing structure, section order, commercial narrative, copy, or semantic intent.

## 2. Asset Use Rule

If an approved asset already exists:

- Use the asset as-is.
- Do not rename it.
- Do not recompress it.
- Do not resize it.
- Do not create a derived replacement unless a documented reason exists.

Any derived asset creation must document:

- Source lineage.
- Original path.
- Derived path.
- Dimensions.
- Transformation reason.
- Human approval or explicit reconstruction need.

## 3. Repo-Visible Shared Assets

| Asset id | Path | Intrinsic size from SVG | Category | V4 use status |
|---|---|---:|---|---|
| AS-BRAND-DARK-LOGO | `projects/triumph-manipulator-landing/design/shared-assets/brand/logo--dark.svg` | 324.251pt x 60pt | Brand logo | Approved candidate for light backgrounds. |
| AS-BRAND-WHITE-LOGO | `projects/triumph-manipulator-landing/design/shared-assets/brand/logo--white.svg` | 324.251pt x 60pt | Brand logo | Approved candidate for dark backgrounds. |
| AS-BRAND-FAVICON | `projects/triumph-manipulator-landing/design/shared-assets/brand/favicon.svg` | 120 x 120, viewBox 0 0 375 375 | Favicon | Approved candidate for favicon use. |
| AS-SOCIAL-TELEGRAM | `projects/triumph-manipulator-landing/design/shared-assets/social/Telegram-ico.svg` | 45.001pt x 45pt | Social/contact icon | Approved candidate when Telegram is present in V1/source copy. |
| AS-SOCIAL-WHATSAPP | `projects/triumph-manipulator-landing/design/shared-assets/social/WhatsApp-ico.svg` | 45pt x 45.002pt | Social/contact icon | Approved candidate when WhatsApp is present in V1/source copy. |
| AS-SOCIAL-MAX | `projects/triumph-manipulator-landing/design/shared-assets/social/MAX-ico.svg` | 45pt x 45pt | Social/contact icon | Approved candidate when MAX is present in V1/source copy. |
| AS-REVIEWS-AVITO | `projects/triumph-manipulator-landing/design/shared-assets/reviews/avito_logo.svg` | 150pt x 150pt | Review/proof mark | Approved candidate when Avito proof exists in source. |
| AS-REVIEWS-YANDEX | `projects/triumph-manipulator-landing/design/shared-assets/reviews/yandex_logo.svg` | 150pt x 150pt | Review/proof mark | Approved candidate when Yandex proof exists in source. |
| AS-REVIEWS-RATE-STAR | `projects/triumph-manipulator-landing/design/shared-assets/reviews/rate_star.svg` | 50 x 50 | Rating icon | Approved candidate when rating proof exists in source. |

## 4. Asset Authority Boundaries

Shared assets may answer:

- Which logo files are available.
- Which social icons are available.
- Which review/proof SVGs are available.
- Which file paths can be referenced without creating replacements.

Shared assets may not answer:

- Whether a header exists.
- Which navigation links exist.
- Where reviews appear.
- Whether social icons belong in header, hero, footer, or form.
- What commercial message V4 should carry.
- Whether a slider exists.

## 5. First-Screen Candidate Assets

Candidate assets for first-screen systems:

- Header brand: `logo--dark.svg` or `logo--white.svg`, depending on V1 background evidence.
- Contact/social affordances: Telegram, WhatsApp, MAX, only if source requires these.
- Favicon: `favicon.svg`, only for shell metadata, not visual section authority.

SAFE UNKNOWN:

- No hero background, vehicle/manipulator raster, or first-screen photo asset was found in `shared-assets/`.
- If V1 first screen requires large imagery, its source lineage must come from V1 raster evidence or a separately approved asset.

## 6. Derived Asset Register

No derived V4 assets were created in this task.

| Derived asset | Source | Dimensions | Transformation reason | Status |
|---|---|---:|---|---|
| None | None | None | None | No derived assets authorized. |

## 7. Contamination Prevention

Do not fill missing V4 assets from:

- V3 crops.
- V3 reconstruction assets.
- V3 local overrides.
- V2 implementation folders.
- Unapproved downloaded replacements.

If an asset is missing, mark SAFE UNKNOWN and request human decision rather than silently replacing source intent.
