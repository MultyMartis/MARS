# FP-0002 V9-06E24A Final Admin Polish Contract

**Wave:** V9-06E24A Service Structured Sections Required Field Polish

## Contract

| Item | Final state |
|---|---|
| Field group | `group_fp02_service_structured_sections` |
| Corrected field | `field_fp02_programme_items_service` / `programme_items` |
| Admin label | Пункты программы |
| Operator reference | Программа / условия → resolved to programme repeater |
| Method | A (make optional) |
| Required flags | repeater 0, title 0, text 0 |
| Frontend usage | USED_FRONTEND with static fallback |
| Save blocker | REMOVED (explicit optional + validation filter) |
| E24 hero CTA | PRESERVED (`hero_cta_label` unchanged) |
| Global `Герои` | ABSENT |
| Top-level Отзывы | PRESERVED |

## Operator QA checklist

1. Edit service **Зависимости** — save without filling programme text subfields.
2. Confirm **Текст кнопки в hero-блоке** still visible under Layout and Hero.
3. Confirm **Настройки сайта** has no **Герои** page.
4. Spot-check `/uslugi/zavisimosti/` programme block renders (static fallback OK).

Evidence: `validation/v9-06e24a-service-structured-sections-required-field-polish/final-e24a-admin-polish-contract.json`
