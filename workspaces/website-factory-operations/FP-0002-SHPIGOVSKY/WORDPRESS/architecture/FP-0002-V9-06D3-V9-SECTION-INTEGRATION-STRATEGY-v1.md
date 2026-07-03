# FP-0002 V9-06D.3 V9 Section Integration Strategy v1

**Phase:** V9-06D.3 — PLANNING ONLY
**Runtime integration performed:** NO

## Strategy

Templates render empty/minimal states when ACF empty; no V9 HTML copied into theme in D.3; later integration maps section markup to template-parts driven by ACF.

## Section mapping

| Section | Template target | ACF source | Priority | Risk |
|---|---|---|---|---|
| hero | `front-page.php / single-service.php / template-parts` | `home_hero_slides / hero_*` | WAVE_1 | MEDIUM |
| service_card_grids | `page-templates/services-hub.php` | `services_hub_* + service query` | WAVE_1 | MEDIUM |
| signs_symptoms | `template-parts/service/alcohol-stack.php` | `signs_items` | WAVE_1 | MEDIUM |
| programme_stages | `template-parts/service/*` | `programme_items / stages` | WAVE_2 | LOW |
| faq | `service/page partials` | `faq_items / home_faq_items / services_hub_faq_items` | WAVE_2 | LOW |
| reviews | `page-templates/reviews.php` | `reviews_items` | WAVE_3 | LOW |
| contacts | `page-templates/contacts.php` | `contacts_* + options contacts` | WAVE_1 | MEDIUM |
| cta_modal_hooks | `layout partials` | `site options modal/cta` | WAVE_1_OPTIONS_DEFERRED_WRITE | MEDIUM |
| source_lists | `single.php partials` | `post content + article meta` | WAVE_4 | LOW |
| breadcrumbs | `template-parts/navigation/breadcrumbs.php` | `derived from hierarchy` | WAVE_1 | MEDIUM |
| gallery_media | `institutional / front-page partials` | `infrastructure_g0_g5 / home_gallery_media` | WAVE_3 | LOW |
| blog_article_sections | `single.php` | `post_content + group_fp02_blog_post_article_meta` | WAVE_4 | LOW |
| placeholder_notice | `service/institutional templates` | `service_layout_variant=placeholder / institutional_placeholder_notice` | WAVE_1 | MEDIUM |
| legal_document | `page-templates/legal.php` | `post_content + group_fp02_page_legal` | WAVE_4 | LOW |

## Notes

- Do not edit theme files in D.3.
- Do not copy V9 HTML into WordPress in D.3.
- Later integration binds existing skeleton template-parts to ACF data.

## Result

COMPLETE — planning only.
