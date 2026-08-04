# REAL EMAIL OBSERVATIONS v1

**Статус: REDACTED RESEARCH BACKLOG — NOT IMPLEMENTED в Phase 3D.8.** Никакие реальные имена, контакты, домены, идентификаторы или screenshots здесь не сохранены.

## Наблюдаемые классы

1. Многострочные label/value формы.
2. Схлопнутые в одну строку формы.
3. Переставленные и повторённые labels.
4. Поле сайта явно оставлено пустым или отмечено как отсутствующее.
5. Alternative contact (`@handle`/messenger URL) ошибочно попадает в поле сайта.
6. Placeholder/invalid values вместо контакта или сайта.
7. Длинный комментарий содержит слова, похожие на labels, и ломает границы.
8. Явный intent в комментарии конфликтует с названием формы или page context.
9. Выбранная услуга присутствует отдельно от свободного комментария.
10. Email subject/form title и source page дают слабые fallback-signals при неполных structured fields.

## Вывод

Parser 3.3 должен хранить provenance и state каждого поля, отделять extraction от intent resolution и проверяться только на sanitized fixtures. Этот документ не доказывает deployment Parser 3.3.