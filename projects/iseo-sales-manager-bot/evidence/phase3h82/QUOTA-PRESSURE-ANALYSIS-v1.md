# QUOTA PRESSURE ANALYSIS v1

**Window inspected:** 2026-08-14 09:55–10:20 Europe/Moscow  
**Source:** n8n execution index (Admin + Ops). Approximate Sheets node runs, not Google Cloud quota console (SAFE UNKNOWN for exact project QPS).

| Source | Execs in window | Approx Sheets node runs |
|---|---|---|
| Admin reminder path | 2 (30813, 30821) | ~12 |
| Operational 2-minute Gmail polling | 12 | ~72 |
| Command traffic | not observed as extra Admin execs in this slice | 0 attributed |
| Isolated harness | none in this window | 0 |

HTTP 429 nodes:

- 30813 Admin `Read ACCESS_CONTROL for Reminder` 10:00
- 30821 Admin `Read ACCESS_CONTROL for Reminder` 10:15
- 30822 Ops `Apply Runtime State CONFIG` 10:16

## Class

**SUSTAINED_PROJECT_QUOTA_PRESSURE** with **LOCAL_BURST_CONTRIBUTION** (Ops poll coinciding with reminder CLEAN+ACCESS).

Not classified as RANDOM_TRANSIENT_429 only: two reminder slots 15 minutes apart both 429.

## Stagger

**Not applied.** Reminder business meaning remains 10:00. Primary repair is bounded retry/backoff. Ops schedule unchanged.
