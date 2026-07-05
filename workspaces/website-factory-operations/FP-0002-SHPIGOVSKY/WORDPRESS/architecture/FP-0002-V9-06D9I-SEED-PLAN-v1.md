# FP-0002 V9-06D9I Seed Plan v1

**Date:** 2026-07-05  
**Task:** V9-06D9-I  
**Authority:** D9-H field map + `inc/home-fallbacks.php` + D9-H template fallbacks

## Write scope

- **Object:** Home page #4 only  
- **Fields written:** 10  
- **Fields skipped:** 9  
- **Media uploads:** 0  
- **Options writes:** 0  

## Source mapping

| Field | Source | Visual impact |
|-------|--------|---------------|
| home_recovery_intro_* | recovery-intro.php fallbacks | SHOULD_MATCH_FALLBACK |
| home_intro_bands | shpigovsky_home_intro_bands_fallback_items() | SHOULD_MATCH_FALLBACK |
| home_faq_heading | faq.php fallback | NONE_EXPECTED |
| home_*_heading / comfort_lead | Section template fallbacks | NONE_EXPECTED |

## Explicit exclusions

- Hero image, gallery media → D9-J  
- FAQ items expansion (5→10) → would change visual  
- Footer/options fields → out of Home #4 scope  
- Reviews/specialists card bodies → deferred  

Evidence: `validation/v9-06d9i-controlled-acf-seed/seed-plan.json`
