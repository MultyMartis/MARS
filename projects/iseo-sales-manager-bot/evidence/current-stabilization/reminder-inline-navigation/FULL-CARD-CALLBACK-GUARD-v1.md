# FULL CARD CALLBACK GUARD v1

## Rule

`🟢 Полная карточка` is added **only** when callback_data is non-empty (`sm:f:<token>`).

Never emit an inline button with empty callback_data (avoids Telegram error: *Text buttons are unallowed in the inline keyboard*).

## Acceptance

- `full_card_included: true`
- `empty_callback_buttons: 0`

Pad slots in fixed-size keyboards always receive non-empty `sm:g:all` (or equivalent) text+callback pairs — never blank.
