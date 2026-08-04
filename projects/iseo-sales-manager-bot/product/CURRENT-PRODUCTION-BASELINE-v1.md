# CURRENT PRODUCTION BASELINE v1

**Срез:** Phase 3D.8.3, 2026-08-05. **Статус:** документированный live baseline.

| Контур | Workflow ID | Active | Nodes | Роль |
|---|---|---:|---:|---|
| Sales-Manager-v2 | `h8I2Tl2yl4uzhUnB` | false | 19 | rollback; не активировать без отдельного решения |
| i-SEO Sales Manager - Operational.dev | `xSnXPy8cEHoZw6xG` | true | 45 | sole Gmail intake, multi-recipient, claim-before-send, short action labels |
| i-SEO Sales Manager - Admin.dev | `wLrLp4WQHm1VJmxz` | true | 59 | `message` + `callback_query`, ACCESS_CONTROL, actor attribution, `/my_status`, `/delivery_status`, `/delivery_users`, archive commands |

## CONFIG

`environment=production`; `ai_enabled=false`; `parser_version=sm-parser-v3.2`; `message_format_version=sm-msg-v2.2`.

## Доступ

Наблюдалось без идентификаторов: active admin — 1; active moderator — 1; revoked moderators — 2. Отзыв намеренный; Olya/Nikita не восстановлены.

## Action-button baseline (3D.8.3)

- Pending action captions: **`✅ Обработано`** / **`🚫 Спам`** (не путать с финальным **`✅ Обработан`**).
- Callbacks unchanged: `sm:p:<token12>` / `sm:s:<token12>`.
- OPS Format создаёт `telegram_has_buttons`, `telegram_callback_processed`, `telegram_callback_spam` и сохраняет `telegram_reply_markup`.
- OPS Send With Buttons передаёт `replyMarkup` и `inlineKeyboard` на верхнем уровне параметров.
- Admin callback lead token синхронизирован с Format на FNV dual-hash; actor hashes остаются sha256.
- OpenRouter disabled; AI OFF; новые workflows не создавались.

## Actor attribution (3D.8.2 COMPLETE)

Оператор подтвердил: Admin→spam и moderator→processed с безопасными `Кем:` метками из ACCESS_CONTROL.

## Git baseline

Phase 3D.8.2: `28504b9a` + tip `f4c94a44`. Phase 3D.8.3: см. report §§20–21. Основной workspace может содержать чужой WIP; работа выполнялась в clean worktree.
