# CURRENT PRODUCTION BASELINE v1

**Срез:** Phase 3E.1, 2026-08-05. **Статус:** документированный live baseline (Parser 3.3); live semantic acceptance PENDING.

| Контур | Workflow ID | Active | Nodes | Роль |
|---|---|---:|---:|---|
| Sales-Manager-v2 | `h8I2Tl2yl4uzhUnB` | false | — | rollback; не активировать без отдельного решения |
| i-SEO Sales Manager - Operational.dev | `xSnXPy8cEHoZw6xG` | true | 45 | sole Gmail intake; **`sm-parser-v3.3`**; **`sm-msg-v2.3`**; multi-recipient; claim-before-send |
| i-SEO Sales Manager - Admin.dev | `wLrLp4WQHm1VJmxz` | true | 59 | `message` + `callback_query`, ACCESS_CONTROL, actor attribution, archive commands |

## CONFIG

`environment=production`; `ai_enabled=false`; `parser_version=sm-parser-v3.3`; `message_format_version=sm-msg-v2.3`; semantic model `lead-semantic-v1`.

## Доступ

Наблюдалось без идентификаторов: active admin — 1; active moderator — 1; revoked moderators — 2. Отзыв намеренный; Olya/Nikita не восстановлены.

## Parser / card baseline (3E.1)

- Lead Semantic Model: website states, intent precedence, comment boundary, first-reply consistency.
- Pending action captions: **`✅ Обработано`** / **`🚫 Спам`** (final **`✅ Обработан`** unchanged).
- Callbacks unchanged: `sm:p:<token12>` / `sm:s:<token12>`.
- Local harness **46/46 PASS**; live semantic acceptance **PENDING**.
- OpenRouter disabled; AI OFF; новые workflows не создавались.

## Prior 3D.8.x

Actor attribution (3D.8.2) and short button labels (3D.8.3) remain in force.

## Git baseline

Phase 3E.1 sync worktree `mars/iseo-sm-phase3e1-parser33`. Main workspace may contain foreign WIP — selective staging only.
