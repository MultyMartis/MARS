# FP-0002 V9-06D9-0 Home Full Section Transfer Plan v1

**Date:** 2026-07-05  
**Evidence:** `validation/v9-06d9-0-full-visual-port-charter/home-full-section-transfer-plan.json`

## Summary

Static V9 Home: **20 sections**. WP runtime: **6 visible**. This plan covers every section for full visual port.

## Section transfer table

| Section | WP state | Required repair | ACF needed | Media needed | Wave |
|---------|----------|-----------------|:-:|:-:|:-:|
| hero | degraded | media + ACF seed | yes | yes | D9-C |
| home-recovery-intro | missing | new partial + orchestration | yes | no | D9-D |
| founder-quote | missing | new partial | yes | yes | D9-D |
| home-treatment-prevention | partial | media pass | partial | yes | D9-E |
| home-gallery | empty | seed + Swiper | yes | yes | D9-D/E |
| home-why-us | missing | new partial | yes | yes | D9-D |
| home-staff-photo | missing | new partial | yes | yes | D9-D |
| home-feature-grid | present | — | no | no | — |
| clinic-landscape | missing | new partial | yes | yes | D9-D |
| home-recovery-life | missing | new partial | yes | yes | D9-D |
| reviews | missing | new partial + Swiper | yes | yes | D9-D/E |
| home-rehabilitation-requirements | missing | new partial | yes | no | D9-D |
| home-rehabilitation-program | partial | media seed | yes | yes | D9-E |
| home-genotyping | missing | new partial | yes | yes | D9-D |
| comfort | missing | new partial | yes | yes | D9-D |
| home-videos | missing | new partial | yes | yes | D9-D |
| specialists | missing | new partial + Swiper | yes | yes | D9-D/E |
| home-articles | empty | posts or static fallback | partial | yes | D9-E |
| faq | present | content review later | no | no | — |
| final-form | present | — | no | no | — |

## Orchestration target

Update `front-page.php` to match static `index.html` section order after D9-D partials exist.

## Safe static fallback

All missing sections can use V9 static copy/images temporarily during port waves (operator visual protocol applies).

## Result

Home transfer plan complete. **14 sections** require port/seed beyond current MVP.
