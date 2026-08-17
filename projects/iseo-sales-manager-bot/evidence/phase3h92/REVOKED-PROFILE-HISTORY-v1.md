# REVOKED PROFILE HISTORY — Phase 3H.9.2 (MOD_A)

Reconstructed from Admin executions + ACCESS snapshots + ACCESS_EVENTS appends. Not inferred from the current row alone.

| When (Europe/Moscow) | Exec | Action | MOD_A state | Notes |
|---|---|---|---|---|
| 2026-08-06 16:54 | 3H.6 evidence | four-recipient baseline | active | All four active after MOD_C restore |
| 2026-08-16 19:09:53 | `32813` | `/moderators` | **active** | List showed 3 active moderators |
| 2026-08-16 19:10:07 | `32814` | `/moderator_remove` | still active | Revoked **MOD_C** (not MOD_A) |
| 2026-08-16 19:10:17 | **`32815`** | **`/moderator_remove`** | **revoked** | ACCESS_EVENTS `moderator_revoked` prior=active; `revoked_at` 19:10:18 |
| 2026-08-16 19:10:27 | `32816` | `/moderator_remove` | revoked | Revoked **MOD_B** |
| 2026-08-16 20:23:54 | `32881` | `/moderator_pending` | revoked | All three mods listed as temporarily revoked |
| 2026-08-16 20:24:04 | `32882` | `/moderator_add` | revoked | Restored **MOD_B** only |
| 2026-08-16 20:24:16 | `32883` | `/moderator_add` | revoked | Restored **MOD_C** only |
| 2026-08-17 15:49 | `33554` | raw callback read | revoked | Phase 3H.9.1 live=3 |
| 2026-08-17 16:17:10 | `33571` | `/moderator_add` | **active** | This phase restore |

Actor for 32814–32816 and 32882–32883: ADMIN_A (`auth_role=admin`, user hash `3FBE21323E22`). Source: `admin_command`. Not harness, not migration, not automated reminder.

Side effect of the Aug 16 upsert path: reply-profile columns on the mutated moderator rows were wiped (numbers/names). Out of scope to repair MOD_B/MOD_C in this phase.
