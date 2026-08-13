# PENDING STATE AT WINDOW — Phase 3H.8

At exec 29969 (2026-08-13 10:00:21 MSK):

| Source | Pending visible to evaluator |
|---|---|
| `LEADS` (what reminder read) | **0** (only 1 processed row) |
| Authoritative `lead_clean_v2` (Operational write target) | Pending candidates present (post-repair dry selector later saw pending≥1 / ~8 non-test) |

`REMINDER_PROD_LEAD_A` was still pending until ~10:40 MSK spam callbacks — **not** visible to the reminder selector because it was not in the obsolete `LEADS` tab read.
