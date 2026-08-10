# LEAD REOPEN CONTRACT — iseo-lead-reopen-v1.0

## Transitions
- `processed -> pending`
- `spam -> pending`

## Callback
`sm:r:<fnvToken(lead_id)>`  
Label: `↩️ Вернуть в обработку`

## Rules
- Same lead_id; no new lead row; no Telegram fanout/resend.
- Preserve historical processed/spam events; append `manager_reopened`.
- Idempotent if already pending: `Заявка уже находится в обработке.`
- Auth: Admin + active moderators only (existing callback authorization).


## Surfaces (3H.7.1)
1. Original card after processed
2. Original card after spam
3. Archive `/leads` processed
4. Archive `/leads` spam
Pending: no reopen button.
