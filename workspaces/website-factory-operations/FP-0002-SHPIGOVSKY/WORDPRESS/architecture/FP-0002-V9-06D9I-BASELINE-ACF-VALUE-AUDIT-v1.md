# FP-0002 V9-06D9I Baseline ACF Value Audit v1

**Date:** 2026-07-05  
**Task:** V9-06D9-I  
**Page:** Home #4 (front page)

## Summary

Pre-seed audit of 19 D9-H wired Home fields. Ten fields were empty and using static fallbacks on the frontend. Nine fields were skipped (already populated, media-deferred, or operator/deferred).

Evidence: `validation/v9-06d9i-controlled-acf-seed/baseline-acf-value-audit.json`

## Empty → seeded (10)

| Field | Eligibility |
|-------|-------------|
| home_recovery_intro_heading | SAFE_TEXT_SEED |
| home_recovery_intro_lead_1 | SAFE_TEXT_SEED |
| home_recovery_intro_lead_2 | SAFE_TEXT_SEED |
| home_intro_bands | SAFE_REPEATER_SEED |
| home_faq_heading | SAFE_TEXT_SEED |
| home_specialists_heading | SAFE_TEXT_SEED |
| home_comfort_heading | SAFE_TEXT_SEED |
| home_comfort_lead | SAFE_TEXT_SEED |
| home_reviews_heading | SAFE_TEXT_SEED |
| home_articles_heading | SAFE_TEXT_SEED |

## Skipped (9)

| Field | Eligibility | Reason |
|-------|-------------|--------|
| home_hero_slides | SKIP_ALREADY_POPULATED | D4 row exists; image D9-J |
| home_advantages | SKIP_ALREADY_POPULATED | D8-B seeded |
| home_faq_items | SKIP_ALREADY_POPULATED | D8-B 5 items; full V9 has 10 |
| home_gallery_media | SKIP_MEDIA_D9J | Attachment required |
| home_cta_title / home_cta_text | SKIP_ALREADY_POPULATED | Prior seed |
| home_service_nav_items | SKIP_OPERATOR_DATA | CPT primary |
| home_reviews_teaser | SKIP_PRODUCTION_REVIEW | Deferred |
| home_blog_teaser_enabled | SKIP_UNCLEAR | No posts |
