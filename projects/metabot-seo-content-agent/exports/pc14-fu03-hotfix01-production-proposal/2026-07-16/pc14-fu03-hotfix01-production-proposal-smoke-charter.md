# PC14-FU03 HOTFIX01 — Operator Smoke Charter (post-apply)

**Status:** plan only — **do not execute** until production HOTFIX01 is applied and apply evidence persisted.  
**Do not retry `/run` before production HOTFIX01 apply.**  
Pending old smoke lock cleanup remains separate, operator-approved only.

## Bait command

```
/run тестовая проверка PC14-FU03 HOTFIX01 после production apply: короткий SEO-план на 3 пункта для страницы услуги ремонта кофемашин. Обязательно сделай SEO ТЗ с таблицей и укажи причину таблицы. В причине таблицы специально используй формулировку: для удобства восприятия. Не используй слова: аккуратное, удобства, удобно, позволяет, обеспечение, контроль, безопасность, специализированные, надежность, наглядность.
```

## Expected acceptable outcomes

### Preferred
- STRICT QA REJECT diagnostic is sent
- Lock closes
- Memory status `blocked_dirty`

### Also acceptable
- Repair produces clean output
- Final clean materials sent
- Lock closes
- Memory status `repair_attempted_clean` or equivalent

## Not acceptable
- False complete preface only (`✅ Задача завершена` / `Результат готов. Отправляю материалы...`)
- No final materials
- Pending lock left active (`task_id=pending`, `status=active`)
- Worker error at restore nodes
- Banned strict markers leaking in final public output
- Raw Strategy JSON dump
- Production stuck before close lock

## Observables to capture
- Intake execution id / status
- Worker execution id / status / error node if any
- Admin `/locks` snapshot for the lock key
- Admin `/health`
- Telegram materials presence / reject diagnostic presence
- Memory row status if available
