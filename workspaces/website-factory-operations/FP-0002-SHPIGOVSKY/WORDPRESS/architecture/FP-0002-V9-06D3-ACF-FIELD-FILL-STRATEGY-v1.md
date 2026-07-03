# FP-0002 V9-06D.3 ACF Field Fill Strategy v1

**Phase:** V9-06D.3 — PLANNING ONLY
**Groups covered:** 13/13

## Constraints

- No Flexible Content
- No unbounded repeaters (all max rows defined)
- ACF Extended PRO not used for FP-0002 fields
- Options values not written in D.3
- Production content not written in D.3

## Groups

### Service — Layout and Hero (`group_fp02_service_layout_hero`)

- Object type: `service`
- Targets: `[73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87]`
- Wave 1 fields: `['service_layout_variant', 'hero_lead']`
- Repeater max: `{}`
- Extraction: Manual/scripted extract from V9 src HTML sections into bounded ACF fields
- Allowed empty: Empty allowed for non-wave-1 fields; wave-1 targets require minimal fill in D.4
- Demo/legal blocker: False

### Service — Structured Sections (`group_fp02_service_structured_sections`)

- Object type: `service`
- Targets: `[73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87]`
- Wave 1 fields: `['intro_text']`
- Repeater max: `{'signs_items': 12, 'programme_items': 6, 'stages': 8}`
- Extraction: Manual/scripted extract from V9 src HTML sections into bounded ACF fields
- Allowed empty: Empty allowed for non-wave-1 fields; wave-1 targets require minimal fill in D.4
- Demo/legal blocker: False

### Service — FAQ (`group_fp02_service_faq`)

- Object type: `service`
- Targets: `[73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87]`
- Wave 1 fields: `[]`
- Repeater max: `{'faq_items': 15}`
- Extraction: Manual/scripted extract from V9 src HTML sections into bounded ACF fields
- Allowed empty: Empty allowed for non-wave-1 fields; wave-1 targets require minimal fill in D.4
- Demo/legal blocker: False

### Service — Relationships / Related Services (`group_fp02_service_relationships`)

- Object type: `service`
- Targets: `[73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87]`
- Wave 1 fields: `[]`
- Repeater max: `{}`
- Extraction: Manual/scripted extract from V9 src HTML sections into bounded ACF fields
- Allowed empty: Empty allowed for non-wave-1 fields; wave-1 targets require minimal fill in D.4
- Demo/legal blocker: False

### Page — Home (`group_fp02_page_home`)

- Object type: `page`
- Targets: `[4]`
- Wave 1 fields: `['home_hero_slides', 'home_service_nav_items', 'home_cta_title', 'home_cta_text']`
- Repeater max: `{'home_hero_slides': 5, 'home_service_nav_items': 6, 'home_advantages': 8, 'home_intro_bands': 6, 'home_reviews_teaser': 6, 'home_gallery_media': 12, 'home_faq_items': 15}`
- Extraction: Manual/scripted extract from V9 src HTML sections into bounded ACF fields
- Allowed empty: Empty allowed for non-wave-1 fields; wave-1 targets require minimal fill in D.4
- Demo/legal blocker: False

### Page — Services Hub (`group_fp02_page_services_hub`)

- Object type: `page`
- Targets: `[5]`
- Wave 1 fields: `['services_hub_intro', 'services_hub_query_mode', 'services_hub_show_placeholders']`
- Repeater max: `{'services_hub_faq_items': 15}`
- Extraction: Manual/scripted extract from V9 src HTML sections into bounded ACF fields
- Allowed empty: Empty allowed for non-wave-1 fields; wave-1 targets require minimal fill in D.4
- Demo/legal blocker: False

### Page — Institutional (`group_fp02_page_institutional`)

- Object type: `page`
- Targets: `[11, 12, 13, 14, 15, 16]`
- Wave 1 fields: `[]`
- Repeater max: `{'institutional_content_sections': 8, 'institutional_stages': 8, 'infrastructure_g0_g5': 6}`
- Extraction: Manual/scripted extract from V9 src HTML sections into bounded ACF fields
- Allowed empty: Empty allowed for non-wave-1 fields; wave-1 targets require minimal fill in D.4
- Demo/legal blocker: False

### Page — Contacts (`group_fp02_page_contacts`)

- Object type: `page`
- Targets: `[20]`
- Wave 1 fields: `['contacts_address', 'contacts_phones', 'contacts_form_intro']`
- Repeater max: `{'contacts_phones': 4, 'contacts_messengers': 6, 'contacts_blocks': 8}`
- Extraction: Manual/scripted extract from V9 src HTML sections into bounded ACF fields
- Allowed empty: Empty allowed for non-wave-1 fields; wave-1 targets require minimal fill in D.4
- Demo/legal blocker: False

### Page — Reviews (`group_fp02_page_reviews`)

- Object type: `page`
- Targets: `[18]`
- Wave 1 fields: `[]`
- Repeater max: `{'reviews_items': 50}`
- Extraction: Manual/scripted extract from V9 src HTML sections into bounded ACF fields
- Allowed empty: Empty allowed for non-wave-1 fields; wave-1 targets require minimal fill in D.4
- Demo/legal blocker: False

### Page — Legal (`group_fp02_page_legal`)

- Object type: `page`
- Targets: `[3, 22, 23, 24]`
- Wave 1 fields: `[]`
- Repeater max: `{}`
- Extraction: Do not migrate DEMO legal bodies; set blocker flags only in later legal wave
- Allowed empty: Legal meta may be empty until WAVE_4; body remains foundation/demo
- Demo/legal blocker: True

### Blog Post — Article Meta (`group_fp02_blog_post_article_meta`)

- Object type: `post`
- Targets: `['PLANNED_POST_FIXTURE']`
- Wave 1 fields: `[]`
- Repeater max: `{}`
- Extraction: Manual/scripted extract from V9 src HTML sections into bounded ACF fields
- Allowed empty: Empty allowed for non-wave-1 fields; wave-1 targets require minimal fill in D.4
- Demo/legal blocker: False

### Site Options — Contacts and Organisation (`group_fp02_site_options_contacts`)

- Object type: `options`
- Targets: `['fp02-site-settings']`
- Wave 1 fields: `[]`
- Repeater max: `{'social_links': 8}`
- Extraction: Extract from V9 layout/footer/modal; operator review; no D.3 write
- Allowed empty: Empty allowed until options seed phase; templates must not fatally fail
- Demo/legal blocker: False

### Site Options — Modal and Global CTA (`group_fp02_site_options_modal_cta`)

- Object type: `options`
- Targets: `['fp02-site-settings']`
- Wave 1 fields: `[]`
- Repeater max: `{}`
- Extraction: Extract from V9 layout/footer/modal; operator review; no D.3 write
- Allowed empty: Empty allowed until options seed phase; templates must not fatally fail
- Demo/legal blocker: False

## Result

COMPLETE — planning only.
