# REVOCATION AUTHORIZATION CLASSIFICATION — Phase 3H.9.2

**Classification:** `UNAUTHORIZED_STATE_DRIFT`

## Why not AUTHORIZED_LATER_REVOCATION

- There is **no** later charter replacing the four-recipient production baseline with a three-recipient set.
- Phase 3H.6 / `PRODUCTION-BASELINE-PRE-AI-SOAK-FOUR-RECIPIENT-v1.md` / this phase still list ADMIN_A, MOD_A, MOD_B, MOD_C as approved-active.
- CONFIG cache remained `pending_reminder_active_recipients_count=4`.
- Phase 3H.9.1 recorded live=3 as an unresolved mismatch, not an accepted baseline.

The Aug 16 Telegram commands are real ADMIN_A `admin_command` mutations, but they are **not** a documented recipient-set redesign:

1. All three moderators were revoked within 20 seconds (`32814`–`32816`).
2. Seventy minutes later `/moderator_pending` listed all three.
3. Only MOD_B and MOD_C were restored (`32882`, `32883`).
4. MOD_A was left revoked with no follow-up charter.

That is an incomplete restore after a mass-revoke cycle, not an explicit operator instruction to drop MOD_A from production.

## Why not SAFE_UNKNOWN

History is complete: timestamps, execution IDs, command names, ACCESS_EVENTS `moderator_revoked` / `moderator_approved`, and before/after ACCESS snapshots exist.

## Decision

Restore MOD_A only. Do not treat live=3 as canonical.
