# FP-0002 V9-06D9H ACF Admin Editability Wiring Report v1

**Date:** 2026-07-05  
**Task:** V9-06D9-H  
**Verdict:** PASS

## Summary

Connected Home + Footer admin editability through ACF on top of D9-G static V9 transplant. Added 9 heading/lead fields to `group_fp02_page_home`, created `inc/home-fallbacks.php`, wired 11 template surfaces. Bounded runtime delivery: 14 files. Post-implementation validation PASS.

## Preflight note

Repository HEAD at task execution: `1e565ded` (1 commit after D9-G `ea8c65a9`). FP-0002 theme unchanged between commits. Local/remote synced.

## Changed source

| Area | Files |
|------|-------|
| ACF JSON | `acf-json/group_fp02_page_home.json` |
| Theme helpers | `inc/home-fallbacks.php`, `functions.php` |
| Home templates | hero, recovery-intro, faq, gallery, feature-grid, specialists, comfort, reviews, articles-teaser |
| Components/layout | final-form.php, footer.php |

## Validation

- Route smoke: ALL_200 (7 routes)
- Home visual: 19/19 sections, FAQ `faq-heading`, hero CTA, sliders/dots, footer
- No DB/ACF value writes
- Checksums: 14/14 source/runtime match

## Recommended next

D9-I Controlled ACF Seed from Static V9

Evidence: `validation/v9-06d9h-acf-admin-editability-wiring/`
