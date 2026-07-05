# FP-0002 V9-06D9I Controlled ACF Seed Report v1

**Date:** 2026-07-05  
**Task:** V9-06D9-I  
**Verdict:** PASS (preflight strict HEAD gate: PARTIAL)

## Summary

Seeded 10 safe Home page #4 ACF fields from static V9 authority (`inc/home-fallbacks.php` + D9-H template fallbacks). DB checkpoint created before writes. Post-seed validation PASS: 19 Home sections, FAQ contract, hero CTA, routes ALL_200, no scope drift. No source/theme/ACF JSON changes.

## Preflight note

Local repository HEAD was `94678d27` (1 commit ahead of required D9-H HEAD `b58225fc`). The ahead commit is governance-only (`.cursorrules`, `AGENTS.md`); remote matches `b58225fc`; D9-H runtime wiring unchanged. Task proceeded on operator authorization; strict HEAD gate recorded as PARTIAL.

## DB checkpoint

`X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06d9i-controlled-acf-seed-pre-20260705-141225\`

## Fields written (10)

1. home_recovery_intro_heading  
2. home_recovery_intro_lead_1  
3. home_recovery_intro_lead_2  
4. home_intro_bands (6 rows)  
5. home_faq_heading  
6. home_specialists_heading  
7. home_comfort_heading  
8. home_comfort_lead  
9. home_reviews_heading  
10. home_articles_heading  

## Fields skipped (9)

home_hero_slides, home_advantages, home_faq_items, home_gallery_media, home_cta_title, home_cta_text, home_service_nav_items, home_reviews_teaser, home_blog_teaser_enabled

## Validation

| Check | Result |
|-------|--------|
| Runtime/DB gate | PASS |
| Dry-run | PASS |
| Apply seed | PASS (10 written) |
| Post-seed ACF verify | PASS |
| Home visual regression | PASS (19/19 sections) |
| Route smoke | ALL_200 |
| Console/network | PASS |
| No-scope-drift | PASS |
| Screenshots | 10/10 captured |

## Recommended next

D9-J Media Selection Upload Plan (hero image + gallery media)

Evidence: `validation/v9-06d9i-controlled-acf-seed/`
