# FP-0002 V9-06D.6 ACF Binding Plan v1

**Date:** 2026-07-04

Constraints: no Flexible Content; no ACF Extended PRO; bounded repeaters only.

| Route | Fields needed | Seeded | Gaps | Fallback | Migration |
|---|---|---|---|---|---|
| home | home_hero_slides, home_service_nav_items, home_cta_title, home_cta_text, home_faq_items, home_gallery_media, home_advantages | seeded: ['home_hero_slides', 'home_service_nav_items', 'home_cta_title', 'home_cta_text'] | ['Many V9 home sections lack 1:1 ACF fields (founder-quote, specialists, videos, genotyping, comfort shared blocks)'] | Render only sections with data; use post_title for document title; omit empty repeaters | PARTIAL_BEFORE_VISUAL_PARITY |
| services_hub | services_hub_intro, services_hub_query_mode, services_hub_show_placeholders, services_hub_faq_items | seeded: ['services_hub_intro', 'services_hub_query_mode', 'services_hub_show_placeholders'] | ['Category hub leads/galleries not fully modeled as ACF; service cards from CPT query'] | H1 from post_title; intro if present; query top-level services | PARTIAL_BEFORE_VISUAL_PARITY |
| service_parent | service_layout_variant, hero_lead, hero_title_override, intro_text, cta_* | seeded: {'73': ['service_layout_variant', 'hero_lead'], '77': ['service_layout_variant', 'hero_lead'], '84': ['service_layout_variant', 'hero_lead']} | ['Loader ignores ACF layout variant; subdivision-specific sections partially unmapped'] | post_title as H1; hero_lead if present; placeholder notice for psych/RPP | YES_FOR_ZAVISIMOSTI_PARITY |
| service_child | service_layout_variant, hero_lead, intro_text, signs_items, programme_items, stages, faq_items | seeded: ['service_layout_variant', 'hero_lead', 'intro_text', 'signs_items'] | ['approach/corridor/specialists/reviews shared blocks not fully fielded'] | omit empty sections; show title + seeded intro/signs | PARTIAL_BEFORE_VISUAL_PARITY |
| contacts | contacts_address, contacts_phones, contacts_form_intro, contacts_map_url, contacts_messengers | seeded: ['contacts_address', 'contacts_phones', 'contacts_form_intro'] | ['options contacts empty; form submit deferred'] | show seeded address/phones; form markup only | OPTIONS_SEED_LATER |
| site_options | phone_primary, site_address, default_callback_*, global_cta_* | seeded: [] | ['options never seeded in D.4'] | hide optional chrome contact bits; modal labels static fallback strings only if operator-approved later | YES_FOR_CHROME_PARITY |

## Notes

- Wire `service_layout_variant` in `shpigovsky_get_service_layout_variant()` during D7-D
- Site options required for chrome parity but not seeded; use safe omit fallbacks in D7-A
- Full visual parity needs later content migration beyond minimal seed

## Result

COMPLETE
