# ADMIN BOOTSTRAP RECOVERY v1

## Boundary

`admin_user_ids` (CONFIG) is **recovery-only** when ACCESS_CONTROL cannot be read technically.

Internal marker: `authorization_source=admin_bootstrap_recovery` / `registry_source=ADMIN_BOOTSTRAP`.

## Allowed recovery commands

- `/start`
- `/help`
- `/status`
- `/health`
- `/config`
- `/moderators`
- `/moderator_pending`

Other admin commands (e.g. `/ai_on`) are **not** allowed under bootstrap.

## Non-negotiables

- Explicit ACCESS_CONTROL `revoked` / `blocked` row **overrides** bootstrap.
- Moderator fail-open via `manager_action_user_ids` remains **forbidden**.
- Callback mutations require real registry action-capable role — bootstrap denies `/__callback`.
- Telegram replies must not expose Sheets/crypto error details.
