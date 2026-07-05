# FP-0002 V9-06D9J Media Classification v1

**Date:** 2026-07-05  
**Evidence:** `validation/v9-06d9j-media-selection-upload-plan/media-classification.json`

## Classification counts

| Classification | Count | Meaning |
|----------------|------:|---------|
| UPLOAD_AND_SEED_D9K | 5 | Hero + gallery — ACF fields exist, empty, theme fallback active |
| KEEP_THEME_FALLBACK | 21 | Content imagery without ACF media wiring; stable MVP |
| OPERATOR_REVIEW_REQUIRED | 5 | People/clinical photos — licensing and replacement risk |
| DO_NOT_UPLOAD_VENDOR_OR_ICON | 7 | Logo, social SVGs, UI icons |
| DEFER_UNTIL_CONTENT_REVIEW | 2 | MP4 video files — separate content wave |

## UPLOAD_AND_SEED_D9K (D9-K MVP)

1. `hero-main.png` → `home_hero_slides[0].image`
2. `shpigovsky-gallery-01.webp` → `home_gallery_media[0].media`
3. `shpigovsky-gallery-02.webp` → `home_gallery_media[1].media`
4. `shpigovsky-gallery-03.webp` → `home_gallery_media[2].media`
5. `shpigovsky-gallery-04.webp` → `home_gallery_media[3].media`

## OPERATOR_REVIEW_REQUIRED

- Founder portrait (`founder-sergey-shpigovsky.png`)
- Specialist portraits (4) — public-facing staff imagery

## KEEP_THEME_FALLBACK (examples)

Comfort gallery, articles teasers, rehabilitation program cards, clinic landscape, staff group photo, video posters, final-form background, recovery-life BG.

## DO_NOT_UPLOAD

Logo SVG, WhatsApp/Telegram/MAX icons, external-link SVG, founder-quote inline SVG (template-embedded).
