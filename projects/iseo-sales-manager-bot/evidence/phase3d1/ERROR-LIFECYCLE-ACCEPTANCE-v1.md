# ERROR-LIFECYCLE-ACCEPTANCE-v1

**Phase:** 3D.1  
**Surface:** Admin.dev `/last_error` (+ `/status` alignment)

## Lifecycle values

| Value | Meaning |
|-------|---------|
| `open` | Active production failure requiring attention |
| `resolved` | Historical / closed (retained in ERRORS) |
| `controlled_test` | Synthetic / controlled check |

## Classification rules (read path)

1. Explicit `error_lifecycle` / `lifecycle` / `error_status` column when present.
2. Synthetic markers → `controlled_test`.
3. Pre-Phase-3D Telegram flood / delivery failures (`telegram_delivery_failed`, `telegram_retry_exhausted`, … before cutover) → `resolved`.
4. Else → `open`.

## Required empty-open behaviour

```text
Активных рабочих ошибок нет.

Последняя устранённая ошибка:
<sanitized summary and time>
```

## Live acceptance

`/last_error` returned exactly the no-active pattern with last resolved `telegram_delivery_failed` (historical). Error history retained.

`/status` updated so a timestamp alone is not presented as an active failure unless `last_error_lifecycle=open`; points operators to `/last_error` for details.
