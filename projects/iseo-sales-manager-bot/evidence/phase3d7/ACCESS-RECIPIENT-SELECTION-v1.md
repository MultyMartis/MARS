# ACCESS RECIPIENT SELECTION v1

## Include

- `role=admin` + `status=active`
- `role=moderator` + `status=active`
- Valid private delivery target (numeric Telegram user id / private chat id)
- `lead_delivery_enabled` true (defaulted when staff active + private chat confirmed)

## Exclude

- public, pending, revoked, blocked
- malformed rows
- duplicate Telegram identities (collapse)
- missing private chat / delivery disabled

## Bootstrap

`admin_user_ids` remains recovery bootstrap only and must **not** create a duplicate recipient when the Admin already exists in ACCESS_CONTROL.
