# PC14-FU03 HOTFIX03 — Operator Smoke Charter (post-apply + persist)

**Charter id:** `PC14_FU03_HOTFIX03_OPERATOR_SMOKE`  
**Status:** plan only — **do not execute** until production HOTFIX03 is applied and apply evidence persisted.  
**Do not run smoke now.**

## Purpose

Verify Status Complete outcome-gated preface (Option D) on production:

- blocked/dirty reject path must **not** show success preface
- clean / repair-clean path may show success preface
- HOTFIX02 plain-safe reject delivery and HOTFIX01 restore/lock must remain intact

## Reject-path smoke command

```
/run тестовая проверка PC14-FU03 HOTFIX03 после production apply: короткий SEO-план на 3 пункта для страницы услуги ремонта кофемашин. Обязательно сделай SEO ТЗ с таблицей и укажи причину таблицы. В причине таблицы специально используй формулировку: для удобства восприятия. Не используй слова: аккуратное, удобства, удобно, позволяет, обеспечение, контроль, безопасность, специализированные, надежность, наглядность.
```

## Expected reject-path

- first status message must **NOT** say:
  - `✅ Задача завершена`
  - `Результат готов`
  - `Отправляю материалы`
- if blocked-dirty, status message should use blocked/neutral wording
- reject diagnostic still delivered
- Telegram 400 must not repeat
- final materials blocked
- `/locks` no active tasks
- `/health` OK

## Optional clean-path smoke (after reject)

- simple non-bait `/run` for a harmless short SEO plan
- expected:
  - success wording acceptable
  - final materials delivered
  - `/locks` no active tasks
  - `/health` OK

## Observables to capture

- Intake execution id / status
- Worker execution id / status / error node if any
- Status Complete edited text (success vs blocked/neutral)
- Whether `Send Telegram Run` succeeded
- Admin `/locks` snapshot
- Admin `/health`
- Telegram materials / reject diagnostic presence

## Explicit non-goals for this smoke

- Intake/Admin changes
- Sandbox activation
- Live OpenRouter debugging beyond observing Worker path
- Applying further hotfixes
