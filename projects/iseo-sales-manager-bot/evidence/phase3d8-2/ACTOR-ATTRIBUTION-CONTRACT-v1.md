# ACTOR ATTRIBUTION CONTRACT v1

## Authorization source

ACCESS_CONTROL is the only primary authorization source.

## Actor identity

1. Read callback actor Telegram user id (exact identity).
2. Match ACCESS_CONTROL row by user id.
3. Require role=admin|moderator and status=active.
4. Resolve display fields from the matched row only.

## Forbidden authorization sources

- username
- display name text
- Telegram message text
- callback data payload names

## Forbidden attribution sources as sole truth

- callback_query profile first/last name when ACCESS_CONTROL row exists
