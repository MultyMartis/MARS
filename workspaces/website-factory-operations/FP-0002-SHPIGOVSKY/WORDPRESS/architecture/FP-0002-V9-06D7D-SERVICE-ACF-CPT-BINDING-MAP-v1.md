# FP-0002 V9-06D7D Service ACF CPT Binding Map v1

**Date:** 2026-07-05

## ACF groups (read-only)

- `group_fp02_service_layout_hero` — layout variant, hero fields  
- `group_fp02_service_structured_sections` — intro, signs, programme, stages, CTA  
- `group_fp02_service_faq` — faq_items repeater  
- `group_fp02_service_relationships` — manual_related_services override  

## Section bindings

| Section | Primary source | Fallback |
|---------|----------------|----------|
| inner-hero | hero_* ACF + post_title | static eyebrow/CTA labels |
| subnav | derived breadcrumbs + anchor map | omit subnav items if empty |
| children | SERVICE_CPT_QUERY + manual_related_services | omit if no children |
| intro | intro_text, intro_note | post_content excerpt |
| signs | signs_items repeater | OMIT_IF_EMPTY |
| program | programme_items repeater | STATIC_FROM_V9 four directions |
| stages | stages repeater | OMIT_IF_EMPTY |
| faq | faq_items repeater | OMIT_IF_EMPTY |
| mid-cta | cta_* + phone_primary option | generic CTA copy |
| comfort | DEFER_CONTENT_MIGRATION | omit |

## Seeded services

| ID | Route | Variant |
|----|-------|---------|
| 73 | /uslugi/zavisimosti/ | subdivision |
| 74 | /uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/ | alcohol-special |
| 77 | /uslugi/psihicheskoe-zdorovie/ | subdivision |
| 84 | /uslugi/rasstroystva-pischevogo-povedeniya/ | subdivision |

## Result

COMPLETE
