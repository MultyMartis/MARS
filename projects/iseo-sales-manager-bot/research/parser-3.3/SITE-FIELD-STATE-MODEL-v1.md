# SITE FIELD STATE MODEL v1

**NOT IMPLEMENTED — Parser 3.3 backlog.**

| State | Значение | Пример без реальных данных |
|---|---|---|
| `provided` | пригодный site/domain явно указан | `https://example.test/` |
| `explicitly_absent` | отправитель явно сообщил, что сайта нет | «сайта пока нет» |
| `alternative_contact` | значение является messenger/contact, не сайтом | `@sample_handle` |
| `invalid_or_placeholder` | формула, мусор, шаблон или некорректное значение | `UNKNOWN`, `#ERROR!`, `-` |
| `missing` | поле отсутствует и явного утверждения нет | отсутствует label/value |

`site_value`, `site_state`, `site_evidence_source` и `site_raw_redacted` должны быть раздельными. Нельзя превращать `explicitly_absent` в `missing` или messenger в site.