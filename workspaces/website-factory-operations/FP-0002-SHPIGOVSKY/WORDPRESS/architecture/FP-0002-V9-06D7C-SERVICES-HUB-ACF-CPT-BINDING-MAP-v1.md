# FP-0002 V9-06D7C Services Hub ACF/CPT Binding Map v1

**Date:** 2026-07-05  
**Task:** V9-06D7-C

## Page ACF (`group_fp02_page_services_hub`)

| Field | Binding |
|-------|---------|
| `services_hub_intro` | Hero tagline when present |
| `services_hub_query_mode` | `grouped_by_parent` (default) or `flat` CPT query |
| `services_hub_show_placeholders` | Empty-state block when CPT query returns no groups |
| `services_hub_faq_items` | `template-parts/services-hub/faq.php` |

## Service CPT query

| Role | Query | Template part |
|------|-------|---------------|
| Parent groups | `post_type=service`, `post_parent=0`, `menu_order ASC` | `service-group.php` |
| Child cards | `post_parent={parent.ID}` | `components/service-card.php` |
| Parent fallback card | Parent with no children | single card in group |

## Service post fields (read-only)

| Field | Use |
|-------|-----|
| `hero_lead` | Group lead primary / card text fallback |
| `intro_text` | Group lead secondary / card text |
| `intro_note` | Group lead secondary fallback |
| `post_excerpt` | Card text fallback |
| permalink | Card link |

## Gaps (no write in D7-C)

- Category gallery images — **DEFER_CONTENT_MIGRATION**  
- Genotyping hub — **SAFE_UNKNOWN** (legacy page route; not in Service CPT parents)  
- Hero image — omitted (no ACF / no packaged asset)  

Evidence: `validation/v9-06d7c-services-hub-template-source/services-hub-acf-cpt-binding-inventory.json`

## Result

COMPLETE
