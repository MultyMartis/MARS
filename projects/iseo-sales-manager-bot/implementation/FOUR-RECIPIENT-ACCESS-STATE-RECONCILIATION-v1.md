# FOUR-RECIPIENT ACCESS STATE RECONCILIATION v1

**Phase:** 3H.9.2  
**Date:** 2026-08-17  
**Authority:** ACCESS_CONTROL is source of truth. CONFIG recipient counts are cache/observability only.

## Approved production set

| Alias | profile_no | Role | Required live state |
|---|---|---|---|
| ADMIN_A | 1 | admin | active · cards · reminder · personalization |
| MOD_B | 2 | moderator | active · cards · reminder |
| MOD_A | 3 | moderator | active · cards · reminder · personalization |
| MOD_C | 4 | moderator | active · cards · reminder |

Do not silently redefine this set to three.

## Drift found

On 2026-08-16 19:10 Europe/Moscow ADMIN_A ran three `/moderator_remove` commands (~20s). Seventy minutes later `/moderator_add` restored MOD_B and MOD_C only. **MOD_A stayed revoked** (`revoked_at` 2026-08-16 19:10:18 Europe/Moscow, exec `32815`).

CONFIG still cached `pending_reminder_active_recipients_count=4`. Live ACCESS staff = 3. Classification: **`UNAUTHORIZED_STATE_DRIFT`**. No later charter dropped MOD_A from the approved set.

## Restore contract

Use existing Admin `/moderator_add <code>` (Unknown Command → Prepare Access Upsert → Upsert ACCESS_CONTROL → Append ACCESS_EVENTS). Do not create a new profile. Do not renumber. Do not mutate other recipients.

Phase 3H.9.2 restored MOD_A on 2026-08-17 16:17 Europe/Moscow (exec `33571`, ACCESS_EVENTS `moderator_approved`). Profile_no 3 rehydrated via existing `/start` seed (exec `33572`, reply targeted ADMIN_A chat). Historical lead replay: 0.

## Resolver predicates (read-only)

Operational and reminder fan-out:

`role ∈ {admin, moderator}` AND `status = active` AND Telegram destination present.

Post-restore: 4 unique aliases, no fifth, no revoked, no CONFIG-only phantom.

## Known leftover (out of this phase)

Aug 16 upserts wiped `reply_profile_number` / `reply_sender_name` on MOD_B and MOD_C rows. Card/reminder selection does not require those columns. Do not repair other recipients in a MOD_A restore.

`Notify Access Subject` did not run: Sheets upsert strips `notify_text`.

## Soak / 3I.1

Four-recipient live ACCESS is restored. Soak stays interrupted until a natural 10:00 Europe/Moscow window produces 4 claims / 4 Telegram attempts / 4 deliveries / 0 duplicates. Phase 3I.1 remains blocked. AI remains OFF.
