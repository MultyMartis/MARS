# REVOKED PROFILE IDENTIFICATION — Phase 3H.9.2

Identity map (immutable `telegram_user_hash12` / approved profile numbers):

| Alias | profile_no | role | Pre-restore status | Cards | Reminder | Personalized replies | Hash12 |
|---|---|---|---|---|---|---|---|
| ADMIN_A | 1 | admin | active | yes | yes | yes | `3FBE21323E22` |
| MOD_B | 2 | moderator | active | yes | yes | wiped since Aug 16 upsert | `E67145502141` |
| **MOD_A** | **3** | moderator | **revoked** | **no** | **no** | wiped | `518CC34C4C0F` |
| MOD_C | 4 | moderator | active | yes | yes | wiped since Aug 16 upsert | `26B9B999DE8A` |

**Currently revoked approved profile (pre-restore):** MOD_A (profile 3).

Row `revoked_at`: `2026-08-16T16:10:18.363Z` = **2026-08-16 19:10:18 Europe/Moscow**.  
`revoked_by` hash matches ADMIN_A actor ref used by `/moderator_remove`.

No real names, usernames, or Telegram IDs in this file.
