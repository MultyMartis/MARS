# FINAL SOAK PROFILE INTEGRITY T0 v1

## Baseline required

| # | Client-facing name | Status | Cards |
|---|---|---|---|
| 1 | Андрей (ADMIN_A) | active | yes |
| 2 | Оля (MOD_B) | active | yes |
| 3 | Михаил (MOD_A) | active | yes |
| 4 | Никита (MOD_C_REVOKED) | revoked | no |

## Observed after T+0

| Signal | Result |
|---|---|
| Access change after T+0 | **1** (Admin upsert ~16:54 МСК) |
| MOD_C identity reactivated | **yes** (status `active`) |
| Profile row count | 4 |
| Blank profile numbers | **1** (MOD_C identity row) |
| Profile wipes | 0 (rows remain 4; not emptied) |
| Duplicate profile numbers 1–3 | 0 |
| Revoked deliveries | **1 lead fanout** (PROD_LEAD_3 → 4 chats including MOD_C) |

## Classification

**STOP** — revoked identity must not be active and must not receive cards during soak without explicit emergency charter. Observed reactivation + delivery violates soak invariants.

Operator note: upsert coincided with moderator-admin webhook traffic (`/moderator_*` family earlier in the session). Checkpoint does not restore or further mutate access.
