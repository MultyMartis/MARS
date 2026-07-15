# PC14-FU03 Production Apply — Operator Smoke Charter

**Status:** NOT EXECUTED in this apply task  
**Gate:** Run only after operator review / evidence persist decision  
**Production Worker:** `p4mqb4VuPcemIDlC`

## Suggested command

```
/run тестовая проверка PC14-FU03 после production apply: короткий SEO-план на 3 пункта для страницы услуги ремонта кофемашин. Обязательно сделай SEO ТЗ с таблицей и укажи причину таблицы. В причине таблицы специально используй формулировку: для удобства восприятия. Не используй слова: аккуратное, удобства, удобно, позволяет, обеспечение, контроль, безопасность, специализированные, надежность, наглядность.
```

## Expected outcomes

- Task completes with clean payload, or repair-then-clean payload, or strict diagnostic block
- No raw Strategy JSON dump
- No banned markers in user-visible final payload if full content is sent
- If residuals remain after repair, full content blocked and diagnostic sent
- Task ID visible
- Lock closes
- Memory status is one of: `approved_clean` | `repair_attempted_clean` | `blocked_dirty`

## Forbidden during smoke follow-up unless separately chartered

- Changing workflow JSON
- Disabling side-effect nodes
- Mutating Intake/Admin/sandbox
