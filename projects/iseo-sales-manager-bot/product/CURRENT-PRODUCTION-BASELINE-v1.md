# CURRENT PRODUCTION BASELINE v1

**Срез:** Phase 3D.8, 2026-08-05. **Статус:** документированный live baseline.

| Контур | Workflow ID | Active | Nodes | Роль |
|---|---|---:|---:|---|
| Sales-Manager-v2 | `h8I2Tl2yl4uzhUnB` | false | 19 | rollback; не активировать без отдельного решения |
| i-SEO Sales Manager - Operational.dev | `xSnXPy8cEHoZw6xG` | true | 45 | sole Gmail intake, multi-recipient, claim-before-send |
| i-SEO Sales Manager - Admin.dev | `wLrLp4WQHm1VJmxz` | true | 57 | `message` + `callback_query`, ACCESS_CONTROL, `/my_status`, `/delivery_status`, `/delivery_users`, archive commands |

## CONFIG

`environment=production`; `ai_enabled=false`; `parser_version=sm-parser-v3.2`; `message_format_version=sm-msg-v2.2`.

## Доступ

Наблюдалось без идентификаторов: active admin — 1; active moderator — 1; revoked moderators — 2. Отзыв намеренный; Olya/Nikita не восстановлены.

## Action-button baseline

- OPS Format создаёт `telegram_has_buttons`, `telegram_callback_processed`, `telegram_callback_spam` и сохраняет `telegram_reply_markup`.
- OPS Send With Buttons передаёт `replyMarkup` и `inlineKeyboard` на верхнем уровне параметров.
- Admin callback lead token синхронизирован с Format на FNV dual-hash; actor hashes остаются sha256.
- Local harness: 30/30 PASS. Telegram API подтвердил обе кнопки на обеих отправках.
- После token sync synthetic callback применил `pending→processed`; edited copy осталась без кнопок.
- `Expand Card Sync` нашёл 1 копию: визуальная проверка второй moderator copy остаётся pending.
- OpenRouter disabled; AI OFF; новые workflows не создавались.

## Git baseline

Канонические коммиты: `6351ce6c` (3D.7.1 duplicate fix), `ce06f240` (3D.7), `e78303e2` (3D.6 closeout). На старте задачи `origin/mars/canonical-post-recovery` указывал на `6351ce6c`. Основной workspace содержит чужой WIP; работа выполняется только в clean worktree.