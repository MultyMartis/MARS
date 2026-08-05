# CALLBACK LOOKUP CONTRACT v2

## Canonical token

Dual-FNV `fnvToken(lead_id)` → 12 hex chars. **Never sha256** for lead tokens (n8n task-runner disallows `crypto`; prior OPS/Admin divergence caused `unknown_lead`).

Callback shapes unchanged: `sm:p:<token12>` / `sm:s:<token12>`.

## Persistence

Generate token once before CLEAN/LEADS persistence; store as `telegram_action_token` / `callback_token`.

## Admin resolution

1. Exact stored token match
2. Else recompute with **same** `fnvToken`
3. Distinguish: not_found / storage_error / archived / already_processed / already_spam / ambiguous

User messages (no technical detail to moderators):

- storage: `Не удалось проверить заявку. Попробуйте ещё раз через минуту.`
- archived: `Эта карточка относится к архивному периоду и больше не изменяет рабочую статистику.`
- missing: `Заявка не найдена в рабочем реестре. Обратитесь к администратору.`
