# SYNTHETIC vs PRODUCTION STATE SEPARATION v1

## Development (`environment=dev`)

`/status` shows тестовый успех/ошибка and states working leads are not processed by the new contour.

`/last_error` uses **Последняя тестовая ошибка** and, for controlled fixtures:

`Тип: контролируемая синтетическая проверка`

`/stats` includes only SYNTHETIC_TEST and states: **Учитываются только тестовые заявки.**

## Production (future)

- `/status` uses working success/error fields (no synthetic wording).
- `/stats` excludes SYNTHETIC_TEST: **Тестовые заявки исключены.**
- `/last_error` title: **Последняя рабочая ошибка**

Internal CONFIG keys / Sheets headers were not renamed.
