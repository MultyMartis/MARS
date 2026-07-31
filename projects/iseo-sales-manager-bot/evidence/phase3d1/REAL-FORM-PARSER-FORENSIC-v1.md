# REAL-FORM-PARSER-FORENSIC-v1

**Phase:** 3D.1  
**Contour:** Operational.dev (sole production Gmail intake)  
**PII policy:** no real phone/email/name/Gmail IDs in this file

## Incident template (sanitized)

Collapsed single-line Gmail snippet / request_text observed in production:

```text
Заявка на бесплатный аудит От кого: <NAME> Способ связи: Телефон Контакт: <PHONE> Адрес сайта: <SITE> Комментарий: <COMMENT>
```

Multiline equivalent (same labels):

```text
Заявка на бесплатный аудит
От кого: <NAME>
Способ связи: Телефон
Контакт: <PHONE>
Адрес сайта: <SITE>
Комментарий: <COMMENT>
```

## Parser input characteristics

| Signal | Observed |
|--------|----------|
| Real line breaks | **No** (`newline_count = 0`) |
| Collapsed single-line | **Yes** |
| HTML tags in parser text | **No** |
| NBSP | **No** (this sample) |
| Label set present | От кого / Способ связи / Контакт / Адрес сайта / Комментарий |
| Audit title phrase | **Yes** — `Заявка на бесплатный аудит` |
| Duplicated quoted section | **No** (this sample) |
| textPlain length | 0 (snippet used) |
| snippet length | > 0 |

## Root cause (forensic)

`Parse Lead` on Operational.dev was a **passthrough** stamp (`sm-parser-v3`) that only copied pre-populated `parsed_*` fields. Gmail items do not provide those fields, so labeled values remained inside `request_text` / summary only.

## Failure symptom (Telegram)

- Клиент: —
- Контакты: —
- Сайт: —
- Качество: Недостаточно для связи
- no manual-copy first reply

## Decision

Repair Parse Lead in-place (same workflow ID) with `sm-parser-v3.1` label-delimited extraction supporting multiline and collapsed single-line forms. Do **not** auto-replay the already PROCESSED malformed message (idempotency / duplicate flood risk). Request one **new** clean test lead.
