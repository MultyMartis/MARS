# PC14-FU03 HOTFIX02 — Operator Smoke Charter (post-apply)

**Status:** plan only — **do not execute** until production HOTFIX02 is applied and apply evidence persisted.  
**Do not retry `/run` before production HOTFIX02 apply.**  
Pending old smoke lock cleanup remains separate, operator-approved only.

## Purpose

Verify Telegram STRICT QA REJECT delivery no longer fails with HTTP 400 entity-parse, and that memory `blocked_dirty` remains reachable on the reject path (memory-first fan-out). HOTFIX01 restore/lock closure must remain intact.

## Bait command

Same reject-path pattern as HOTFIX01 smoke (execution fixture `3364` / task `seo202607201222012uqhz9`):

```
/run тестовая проверка PC14-FU03 HOTFIX02 после production apply: короткий SEO-план на 3 пункта для страницы услуги ремонта кофемашин. Обязательно сделай SEO ТЗ с таблицей и укажи причину таблицы. В причине таблицы специально используй формулировку: для удобства восприятия. Не используй слова: аккуратное, удобства, удобно, позволяет, обеспечение, контроль, безопасность, специализированные, надежность, наглядность.
```

## Expected acceptable outcomes

### Preferred (reject path)
- STRICT QA REJECT diagnostic is **sent** to Telegram (no 400 entity parse)
- Reject text is plain-safe (no raw `*` / `_` / backticks / `[]` entity hazards)
- Lock closes
- Memory status `blocked_dirty` (memory-first fan-out)

### Also acceptable
- Repair produces clean output
- Final clean materials sent (plain-safe)
- Lock closes
- Memory status `repair_attempted_clean` or equivalent

## Not acceptable
- `Send Telegram Run` Telegram HTTP 400 / can't parse entities
- False complete preface only (`✅ Задача завершена` / `Результат готов. Отправляю материалы...`) with no final materials/diagnostic
- Pending lock left active
- Worker error at restore nodes (HOTFIX01 regression)
- Memory append skipped while send fails (pre-HOTFIX02 fan-out regression)
- Banned strict markers leaking in final public output
- Raw Strategy JSON dump

## Observables to capture
- Intake execution id / status
- Worker execution id / status / error node if any
- Whether `Send Telegram Run` succeeded
- Admin `/locks` snapshot for the lock key
- Admin `/health`
- Telegram materials presence / reject diagnostic presence
- Memory row status if available

## Explicit non-goals for smoke
- Preface gating (deferred HOTFIX03)
- Intake/Admin changes
- Live OpenRouter debugging beyond observing Worker path
