# FP-0002 V9-06E24 Final Local Hero CTA Contract

## Authority

- **Field name:** `hero_cta_label` (documented alias for task `hero_button_text`)
- **Admin label:** Текст кнопки в hero-блоке
- **Architecture:** page/entity-local only — E22 preserved
- **Forbidden:** global `Герои`, `group_fp02_block_hero_fallbacks`

## Covered contexts

Home, services hub, all service posts with hero (`group_fp02_service_layout_hero`), institutional pages with hero.

## Excluded

Contacts, reviews, legal — no hero CTA button.

## Operator QA checklist

- [ ] Edit home → verify **Текст кнопки в hero-блоке** visible
- [ ] Edit `/uslugi/` page → same field visible
- [ ] Edit service subdivision/leaf → same field visible
- [ ] Confirm **Настройки сайта** has no **Герои**
- [ ] Frontend CTA text unchanged after seed

Evidence: `validation/v9-06e24-hero-cta-button-text-per-entity/final-e24-local-hero-cta-contract.json`
