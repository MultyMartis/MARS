# FP-0002 V9-06E26A About Page Seed v1

## Target

- Page ID: `11`
- Route: `/o-centre/`
- Writes: ACF postmeta only

## Strategy

- Preserve existing hero fields when non-empty
- Seed scalar `about_*` fields from static V9 authority
- Seed repeaters: narrative paragraphs, spectrum, cards, program items, infrastructure G0–G5 text
- CTA/reviews/specialists/final-form: reusable block options (no overwrite)
- No media uploads; program/infrastructure images use theme static asset fallbacks

## Hero preserved

- `hero_eyebrow`, `hero_title_override`, `hero_lead`, `hero_cta_label` — preserved or V9 defaults applied when empty

Evidence: `validation/v9-06e26a-about-page-wordpress-acf-port/about-page-seed-result.json`
