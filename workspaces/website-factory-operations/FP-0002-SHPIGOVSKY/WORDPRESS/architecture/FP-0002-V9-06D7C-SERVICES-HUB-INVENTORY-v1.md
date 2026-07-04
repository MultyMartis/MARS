# FP-0002 V9-06D7C Services Hub Inventory v1

**Date:** 2026-07-05  
**Task:** V9-06D7-C Services Hub Template Source

## V9 source

| Item | Value |
|------|-------|
| Canonical page | `src/pages/uslugi.html` |
| Body class | `page-uslugi` |
| Hero | `partials/sections/hero-inner.html` |
| Category hubs | `partials/sections/services-category-hub.html` × 4 |
| Program block | `partials/sections/home-rehabilitation-program.html` |
| FAQ | `partials/sections/faq.html` |
| CTA form | `partials/sections/final-form.html` |

## Section order (V9)

1. hero-inner  
2. services-category-hub — addictions  
3. services-category-hub — mental health  
4. services-category-hub — eating disorders (compact, no gallery)  
5. services-category-hub — genotyping (compact, no gallery)  
6. home-rehabilitation-program  
7. founder-quote  
8. comfort  
9. faq  
10. final-form  

## Service group / card structure

- Parent section: `section.services-category-hub` + slug modifier  
- Cards: `article.services-category-hub__service` with linked title and optional text  
- Per-group CTA: consultation modal button  

## Deferred in D7-C

- Hero background image  
- Decor and gallery images per category  
- founder-quote  
- comfort  
- genotyping hub (no Service CPT parent in 15-object skeleton)  

Evidence: `validation/v9-06d7c-services-hub-template-source/v9-services-hub-inventory.json`

## Result

COMPLETE
