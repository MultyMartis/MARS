# REAL-LEADS-DURING-ISOLATION-v1

**Isolation window:** 2026-08-28T11:07:19Z → 11:38:55Z (MOD_B revoked)

## Policy during window

- No intentional Telegram traffic to MOD_B / Olya
- Tests via ADMIN_A only
- Olya production pending lead **not** used for status transitions

## Real lead impact

| Check | Result |
|---|---|
| Olya production lead used in tests | **no** |
| Evidence of customer-facing messages to Olya | **none in forensic** |
| Lead count change (post-restore vs known) | **14** stable at restore baseline |

**SAFE UNKNOWN:** exhaustive actor_events diff pre-revoke vs post-restore (pre-revoke snapshot lost).
