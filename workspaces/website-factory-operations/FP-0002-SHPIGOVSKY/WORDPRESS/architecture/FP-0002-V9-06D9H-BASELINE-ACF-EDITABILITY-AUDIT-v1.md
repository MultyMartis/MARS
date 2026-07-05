# FP-0002 V9-06D9H Baseline ACF Editability Audit v1

**Date:** 2026-07-05  
**Task:** V9-06D9-H

## Summary

Pre-D9-H state: D9-G static V9 Home + Footer transplant intact. ACF JSON under `WORDPRESS/acf-json/` with `group_fp02_page_home` (10 fields) and site options groups. Only hero slides, final-form CTA fields partially wired. Footer contacts read site options with static fallbacks.

## Gaps addressed in D9-H

- Section heading fields for FAQ, recovery intro, specialists, comfort, reviews, articles
- Repeater wiring: FAQ, gallery, feature-grid, recovery intro cards
- Chrome CTA labels from site options (hero, footer, final-form)
- `inc/home-fallbacks.php` static V9 authority layer

Evidence: `validation/v9-06d9h-acf-admin-editability-wiring/baseline-acf-editability-audit.json`
