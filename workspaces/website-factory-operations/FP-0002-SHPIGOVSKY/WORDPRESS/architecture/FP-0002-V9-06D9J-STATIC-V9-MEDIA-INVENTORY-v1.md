# FP-0002 V9-06D9J Static V9 Media Inventory v1

**Date:** 2026-07-05  
**Mode:** READ_ONLY  
**Evidence:** `validation/v9-06d9j-media-selection-upload-plan/static-v9-media-inventory.json`

## Authority paths

| Role | Path |
|------|------|
| Static V9 source | `workspaces/fp-0002-shpigovsky-v9/src/` |
| Static V9 dist | `workspaces/fp-0002-shpigovsky-v9/dist/` |
| Theme assets (Git) | `WORDPRESS/theme/shpigovsky/assets/` |
| Runtime theme assets | `MARS-Localhost/.../themes/shpigovsky/assets/` |

## Summary

- **40** Home-related media assets inventoried (images, SVG icons, video files).
- **5** classified `UPLOAD_AND_SEED_D9K` (hero + 4 gallery slides with ACF targets).
- **21** classified `KEEP_THEME_FALLBACK` (section imagery without ACF wiring yet).
- **5** classified `OPERATOR_REVIEW_REQUIRED` (founder + specialist portraits).
- **7** classified `DO_NOT_UPLOAD_VENDOR_OR_ICON` (logo, social SVGs, external-link icon).
- **2** classified `DEFER_UNTIL_CONTENT_REVIEW` (MP4 video files).

## ACF-linked content images (D9-K candidates)

| Section | Asset | Static path | Theme fallback | SHA256 match V9↔theme |
|---------|-------|-------------|----------------|------------------------|
| hero | hero-main.png | `src/img/hero/hero-main.png` | `assets/img/hero/hero-main.png` | MATCH |
| gallery | shpigovsky-gallery-01.webp | `src/img/content/gallery/...` | theme gallery folder | MATCH |
| gallery | shpigovsky-gallery-02.webp | same | same | MATCH |
| gallery | shpigovsky-gallery-03.webp | same | same | MATCH |
| gallery | shpigovsky-gallery-04.webp | same | same | MATCH |

## Static-only sections (theme fallback active, no ACF media field)

Comfort (6 room images + logo decor), specialists (4 portraits), founder quote photo, clinic landscape, staff group, rehabilitation program (4), rehabilitation requirements corridor, recovery-life background, articles teaser (3), video posters (2), final-form background, recovery-intro decor.

## Current usage

All Home frontend media is served from **theme asset URLs** (`THEME_FALLBACK_ACTIVE`). No WP Media Library attachments are referenced on Home (`attachment_count: 0`).
