# PC14-FU03 Post-Production-Apply Operator Smoke Charter

**Status:** draft for apply-phase use — **do not run in this proposal task**
**Target:** production Worker `p4mqb4VuPcemIDlC` after FU03 apply
**Prerequisite:** operator-approved production apply evidence complete

## Command

```
/run тестовая проверка PC14-FU03 после production apply: короткий SEO-план на 3 пункта для страницы услуги ремонта кофемашин. Обязательно сделай SEO ТЗ с таблицей и укажи причину таблицы. В причине таблицы специально используй формулировку: для удобства восприятия. Не используй слова: аккуратное, удобства, удобно, позволяет, обеспечение, контроль, безопасность, специализированные, надежность, наглядность.
```

## Expected outcomes

| Check | Expectation |
|-------|-------------|
| Task completes or strict-blocks | One of: full clean send / repair-then-clean / blocked_dirty diagnostic |
| Strategy JSON | No raw Strategy JSON dump in Telegram |
| Banned markers | No banned markers in user-visible final payload if full content sent |
| Residuals after repair | Full content blocked; short diagnostic: `STRICT QA REJECT — output blocked before final send` |
| Task ID | Visible |
| Lock | Closes with real task_id (PC-07 mapping) |
| Memory status | `approved_clean` \| `repair_attempted_clean` \| `blocked_dirty` |

## Do not

- Do not run this smoke during proposal-only phase
- Do not activate sandbox
- Do not mutate Intake/Admin
