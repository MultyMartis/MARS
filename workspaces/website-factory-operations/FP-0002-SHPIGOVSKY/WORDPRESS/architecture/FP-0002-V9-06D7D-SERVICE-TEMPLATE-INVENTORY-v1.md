# FP-0002 V9-06D7D Service Template Inventory v1

**Date:** 2026-07-05  
**Task:** V9-06D7-D Service Template Source

## V9 source files

| Layout | V9 page | Dist |
|--------|---------|------|
| Parent / subdivision | `src/pages/usluga-podrazdel-v1.html` | parent service routes under `dist/uslugi/` |
| Detail / leaf | `src/pages/usluga-konechnaya-v1.html` | child service routes |
| Alcohol-special | Same leaf page for Service 74 route | `dist/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` |

## Parent section order (V9)

1. services-inner-hero-v2  
2. internal-page-nav  
3. services-category-section-v2 (children)  
4. service-subdivision-nature-v1  
5. program-cta-band  
6. services-program-v2  
7. service-subdivision-stages-v1  
8. service-subdivision-team-stats-v1  
9. clinic-landscape  
10. specialists  
11. founder-quote  
12. comfort  
13. reviews  
14. faq  
15. final-form  

## Detail section order (V9)

1. services-inner-hero-v2  
2. internal-page-nav  
3. service-leaf-intro-v1  
4. service-leaf-bordered-info-v1  
5. program-cta-band  
6. service-leaf-signs-v1  
7. service-leaf-approach-v1  
8. clinic-landscape  
9. services-program-v2  
10. service-leaf-stages-v1  
11. service-leaf-corridor-v1  
12. specialists  
13. founder-quote  
14. comfort  
15. reviews  
16. faq  
17. final-form  

## D7-D integration scope

Implemented now: hero, subnav, children/intro, CTA bands, signs, program, stages, FAQ, final-form.  
Deferred: nature, team-stats, landscape, specialists, founder-quote, comfort, reviews, corridor, bordered-info (no dedicated ACF / shared block wave).

Evidence JSON: `validation/v9-06d7d-service-template-source/v9-service-template-inventory.json`

## Result

COMPLETE
