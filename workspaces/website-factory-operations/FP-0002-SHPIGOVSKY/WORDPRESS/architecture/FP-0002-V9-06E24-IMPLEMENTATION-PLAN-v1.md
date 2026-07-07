# FP-0002 V9-06E24 Implementation Plan

## Field groups

| Group | Action | Field | Key |
|---|---|---|---|
| `group_fp02_page_home` | add | `hero_cta_label` | `field_fp02_hero_cta_label_home` |
| `group_fp02_page_services_hub` | add | `hero_cta_label` | `field_fp02_hero_cta_label_hub` |
| `group_fp02_service_layout_hero` | relabel | `hero_cta_label` | `field_fp02_hero_cta_label_service` |
| `group_fp02_page_institutional` | relabel | `hero_cta_label` | `field_fp02_hero_cta_label_institutional` |

Label: **Текст кнопки в hero-блоке**  
Alias documented: task `hero_button_text` → project convention `hero_cta_label`.

## Frontend

- Helper: `shpigovsky_get_local_hero_cta_label( $post_id, $route_fallback = '' )`
- Fallback: local → route → `default_button_label` → static V9
- No global hero option reads

## Seed

Seed `hero_cta_label` postmeta only when empty; preserve operator values.

Evidence: `validation/v9-06e24-hero-cta-button-text-per-entity/implementation-plan.json`
