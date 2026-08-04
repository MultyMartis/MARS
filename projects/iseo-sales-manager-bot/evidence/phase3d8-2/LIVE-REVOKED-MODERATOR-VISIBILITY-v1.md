# LIVE REVOKED MODERATOR VISIBILITY v1

## Access state used (unchanged)

- Admin: active
- Test moderator «Мопс»: active
- Olya: moderator / revoked (intentional)
- Nikita: moderator / revoked (intentional)

## Method

Patched formatPendingList / listRevokedFormerModerators executed against a live ACCESS_CONTROL snapshot taken from Admin callback execution context (pre-existing 3D.8.1 successes). No ACCESS_CONTROL mutation. No notifications. No /moderator_add.

## Result (sanitized)

- Pending section: empty → «Новых заявок на рабочий доступ нет.»
- Revoked section present with two former moderators (Olya display + Nikita display)
- Each entry includes a stable code (redacted in git) and revoked date
- Active list remains only «Мопс»

## Telegram command delivery

Operator should still send /moderator_pending once for human-visible confirmation in the Admin chat. Runtime formatter+live rows already produce the required body.
