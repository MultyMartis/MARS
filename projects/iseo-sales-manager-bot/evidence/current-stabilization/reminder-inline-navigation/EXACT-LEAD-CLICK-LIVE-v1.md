# EXACT LEAD CLICK LIVE v1

## Contract

Lead buttons use stable token namespace `sm:q:<fnvToken(lead_id)>` (no names, no sheet row numbers).

Production `queue_open` reuses existing compact lead renderer + actions.

## Acceptance proof (ADMIN_A)

- message_id **1092**
- `lead_has_reply_markup: true`
- Full-card button included only with non-empty callback (`full_card_included: true`)
- `empty_callback_buttons: 0`
- `wrong_lead_resolutions: 0`
- `real_lead_status_mutations_by_test: 0`

## Note

Acceptance opened the compact lead view via the same token contract used by production `sm:q:` handlers. No processed/spam mutation performed.
