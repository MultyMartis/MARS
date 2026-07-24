# Client Ops Telegram message contract (Phase 1B-C preparation)

**Status:** PREPARED / NOT SENT
**Audience:** bzpm.ru client-facing sandbox (future)
**Preferred parse mode: plain text**
**Rich parse modes:** deferred until escaping is proven
**Buttons / inline keyboards / callbacks:** forbidden for MVP

---

## Rendering rules

1. One short status marker line including site `bzpm.ru`.
2. Deterministic fields only from accepted Client Ops envelope / sandbox response facts.
3. No raw JSON, stack traces, filesystem paths, credentials, DB/hosting details, or monitor logs.
4. No production-control links.
5. Event ID only in shortened form when operationally useful.
6. Rejected / unauthorized events must **not** produce Telegram delivery.

### Required field lines

- Статус
- Время проверки
- Результат импорта
- Найдено проблем
- Краткое действие или рекомендация
- Event (short) — optional

---

## Synthetic examples (not production data)

### OK

```text
[OK] bzpm.ru — контроль после обмена с 1С

Статус: OK
Время проверки: 2026-07-24 12:00
Результат импорта: обмен завершён без критических расхождений
Найдено проблем: 0
Рекомендация: действий не требуется
Event: a1b2c3d4
```

### ATTENTION

```text
[ATTENTION] bzpm.ru — контроль после обмена с 1С

Статус: ATTENTION
Время проверки: 2026-07-24 12:05
Результат импорта: обмен выполнен, есть позиции для проверки
Найдено проблем: 4
Рекомендация: проверить новые или изменённые позиции каталога
Event: e5f6a7b8
```

### FAILED

```text
[FAILED] bzpm.ru — контроль после обмена с 1С

Статус: FAILED
Время проверки: 2026-07-24 12:10
Результат импорта: контроль не подтвердил успешное завершение
Найдено проблем: 1
Рекомендация: требуется внимание оператора MetaCODE
Event: c9d0e1f2
```

### BLOCKED

```text
[BLOCKED] bzpm.ru — контроль после обмена с 1С

Статус: BLOCKED
Время проверки: 2026-07-24 12:15
Результат импорта: доставка отчёта заблокирована правилами безопасности
Найдено проблем: n/a
Рекомендация: связаться с MetaCODE; не повторять отправку вручную
Event: 33445566
```

---

## Client readability verdict

**PASS** — Russian, concise, non-technical for the client; technical infrastructure details excluded.

## Redaction checklist

| Item | In message |
|------|------------|
| Bot token | NO |
| Webhook secret | NO |
| Absolute paths | NO |
| Stack traces | NO |
| Raw JSON | NO |
| Full UUID (optional short only) | SHORT only |
| Production control URLs | NO |
