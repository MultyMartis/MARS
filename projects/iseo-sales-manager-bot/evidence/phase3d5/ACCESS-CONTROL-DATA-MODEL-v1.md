# ACCESS_CONTROL DATA MODEL v1

## Tab: ACCESS_CONTROL

Columns: telegram_user_id, telegram_user_hash, telegram_username, display_name, role, status, first_seen_at, last_seen_at, requested_at, approved_at, approved_by, revoked_at, revoked_by, source, notes.

- `telegram_user_id` stored as **text** (RAW writes).
- Identity key = Telegram user ID (not username).
- Roles: public | moderator | admin | blocked.
- Statuses: pending | active | revoked | blocked.
- Opaque approval code = deterministic hash prefix (not raw ID).

## Tab: ACCESS_EVENTS

Immutable access audit: ts, opaque_user_ref, event, prior_role, prior_status, new_role, new_status, actor_ref, source, outcome, detail.

Events: public_user_seen, moderator_requested, moderator_approved, moderator_revoked, moderator_action_denied, blocked_user_denied.

Do not mix with business LEAD_EVENTS totals.
