# OPERATIONAL RECIPIENT RESOLUTION — Phase 3H.9.2 (read-only)

Predicate (production Ops expand): `role in {admin,moderator}` AND `status=active` AND Telegram destination present. No lead manufactured. No Telegram send.

Post-restore ACCESS (`33573`):

| Alias | Unique dest | Eligible |
|---|---|---|
| ADMIN_A | yes | yes |
| MOD_B | yes | yes |
| MOD_A | yes | yes |
| MOD_C | yes | yes |

Count: **4**. Unique hashes: **4**. Revoked included: **0**. Fifth recipient: **0**. Duplicates: **0**.

Personalization: ADMIN_A and MOD_A resolve reply-profile number+name. MOD_B/MOD_C destinations resolve; reply-profile columns remain wiped from the Aug 16 upsert (not repaired this phase — other recipients not modified).
