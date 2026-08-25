# GROUP CLICK LIVE v1

## Production handler

`Handle Callback Action` → `action === 'group_open'`:

- Recomputes **current** pending membership
- Builds compact group text + `sm:q:` lead buttons
- `sheets_mutate: false`

## Callback reply send (post-fix)

`Prepare Callback Answer` flattens keyboard → `Switch Reply Keyboard Band` → `Safe Telegram Reply KBn` (field expressions).

## Acceptance proof (ADMIN_A)

Simulated post-click group message (same UX payload class):

- message_id **1091**
- `group_has_reply_markup: true`
- Category alias under test: Аудит
- `group_lead_callbacks` with `sm:q:` tokens: 8 sent (page slice)
- No status mutations

## Currentness

Group membership is recomputed at click time from CLEAN pending state (expected drift vs morning snapshot counts).
