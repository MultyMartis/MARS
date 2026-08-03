# MODERATORS COMMAND LIVE ACCEPTANCE v1

`/moderators` reads active moderator rows from ACCESS_CONTROL via Unknown Command handler.

Expected:

- Оля listed as active moderator
- username shown when available
- no raw Telegram ID
- total active moderators excluding Admin = 1

Harness: formatModeratorsList PASS. Operator Telegram confirmation pending if no post-patch live execution yet.
