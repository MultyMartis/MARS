# MOSCOW TIME RENDERING v1

## Policy

- Canonical storage remains UTC/ISO where applicable.
- Operator Telegram output uses **Europe/Moscow (UTC+3)**.
- Format: `DD.MM.YYYY HH:mm МСК`

## Proof

Local unit check:

- Input UTC: `2026-07-30T19:49:48.000Z`
- Rendered: `Последний тестовый успех: 30.07.2026 22:49 МСК`
- Unit pass: **true**

Live harness `/status` lines:

```
Последний тестовый успех: 30.07.2026 22:49 МСК
Последняя тестовая ошибка: 30.07.2026 22:49 МСК
```
