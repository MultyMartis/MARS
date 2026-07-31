# PRODUCTION-TELEGRAM-CARD-ACCEPTANCE-v1

**Phase:** 3D.1  
**Status:** **PENDING** — no new clean lead card in observe window

## Expected shape (post-repair)

```text
Новый лид

Клиент: <test name>
Контакты: <normalized contact> (<method>)
Сайт: <test site>
Услуга: Аудит

Кратко: <clean request/comment>

Качество: <correct quality>
Не хватает: only real missing fields, if any
Следующий шаг: useful manager action

Режим обработки: Без ИИ

──────── Ответ клиенту ────────

<manual-copy response>

───────────────────────────────
Ответ клиенту автоматически не отправляется.
```

## Pre-repair negative evidence

Malformed card showed dashes for client/contacts/site and `Недостаточно для связи` while labels existed in summary blob (see REAL-FORM-PARSER-FORENSIC-v1).

## Post-repair

Fresh production card acceptance deferred to operator’s new test submission.
