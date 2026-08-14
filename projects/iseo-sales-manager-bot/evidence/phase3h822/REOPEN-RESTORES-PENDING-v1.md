# REOPEN RESTORES PENDING v1

Operator-approved `REMINDER_ACCEPTANCE_LEAD_2` (same ID as Phase 3H.8.2 reopen).

| Check | Result |
|---|---|
| Historical spam preserved | yes (`spam_at` kept on CLEAN) |
| Current status | pending via reopen |
| Source | `LEADS_CURRENT` |
| Reminder eligible | true |
| Counted | exactly once in unique set |
| Mutated this phase | **no** |

Harness case 6 PASS (historical spam + later reopen/pending → included once).
