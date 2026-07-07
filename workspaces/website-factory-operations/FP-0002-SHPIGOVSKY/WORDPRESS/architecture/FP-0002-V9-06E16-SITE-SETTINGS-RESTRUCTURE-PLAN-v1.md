# FP-0002 V9-06E16 — Site Settings Restructure Plan

**Evidence:** `validation/v9-06e16-operator-qa-closure-reusable-blocks-clone-cleanup-audit/site-settings-restructure-plan.json`

## Move to Общие настройки

All `group_fp02_site_options_contacts` fields plus global defaults: `default_button_label`, `default_secondary_button_label`.

## Move to Повторяемые блоки

| Current field | Target subpage |
|---------------|----------------|
| default_callback_* | Модальное окно |
| default_consent_text_reference | Финальная форма |
| global_cta_* | CTA-блоки |

## Stay page/service-local

- `group_fp02_page_home`, `group_fp02_page_services_hub`
- All service CPT field groups
- Contacts, reviews page, legal, institutional page groups

## ACF work (future)

- `acf_add_options_sub_page` registrations in plugin
- Update `location` rules from `fp02-site-settings` to new slugs
- Seed script: copy `options_*` / `fp02-reviews` values to new contexts

**Risk:** MEDIUM — mitigated by alias reads and E16 backup.
