# EXECUTION FORENSIC MATRIX v1

**Window:** 2026-08-04 ~20:00–20:13 +07 (UTC 13:00–13:13)  
**Workflow:** Operational.dev `xSnXPy8cEHoZw6xG`  
**Stable lead hash:** `C3EF8E536C35E9CC`  
**Gmail message id hash:** `FAE255BA5353022D` (same message/thread across all 16 lead executions)

Empty polls 20625–20636 omitted (Gmail fetch → empty → runtime state only).

| Execution | Poll time (+07) | Stable lead ref | Business dedupe | Recipient count | Delivery key count | Sends attempted | Sends successful (TG API) | Gmail labels/finalization |
|---|---|---|---|---:|---:|---:|---:|---|
| 20637 | 20:05:30 | hash C3EF8E536C35E9CC | new | 4 | 4 (deterministic) | 4 | 4 | **none** — died at Stamp |
| 20638 | 20:06:00 | same | new | 4 | 4 | 4 | 4 | none |
| 20639 | 20:06:30 | same | new | 4 | 4 | 4 | 4 | none |
| 20640 | 20:07:00 | same | new | 4 | 4 | 4 | 4 | none |
| 20641 | 20:07:30 | same | new | 4 | 4 | 4 | 4 | none |
| 20642 | 20:08:00 | same | new | 4 | 4 | 4 | 4 | none |
| 20643 | 20:08:30 | same | new | 4 | 4 | 4 | 4 | none |
| 20644 | 20:09:00 | same | new | 4 | 4 | 4 | 4 | none |
| 20645 | 20:09:30 | same | new | 4 | 4 | 4 | 4 | none |
| 20646 | 20:10:00 | same | new | 4 | 4 | 4 | 4 | none |
| 20647 | 20:10:30 | same | new | 4 | 4 | 4 | 4 | none |
| 20648 | 20:11:00 | same | new | 4 | 4 | 4 | 4 | none |
| 20649 | 20:11:30 | same | new | 4 | 4 | 4 | 4 | none |
| 20650 | 20:12:00 | same | new | 4 | 4 | 4 | 4 | none |
| 20651 | 20:12:30 | same | new | 4 | 4 | 4 | 4 | none |
| 20652 | 20:13:00 | same | new | 4 | 4 | 4 | 4 | none |

## Determinations

| Question | Answer |
|---|---|
| How many Operational executions processed the same Gmail message? | **16** |
| Same Gmail message ID / thread ID? | **YES** (hashes identical) |
| CLEAN dedupe class | Always **`new`** (DEDUP lookup miss + CONFIG `tg_delivered:*` never written) |
| `skip_telegram` false on every poll? | **YES** for all four recipients each poll |
| LEAD_DELIVERIES rows written during incident? | **NO** |
| Later executions could read those rows? | **N/A** — none existed |
| Recipient delivery keys stable? | **YES** — `lead_delivery:<stable>:<u:HASH>` (no exec/timestamp) |
| Gmail PROCESSED completed? | **NO** during incident |
| Failure after Telegram prevented finalization? | **YES** — Stamp `.first()` throw |
| Workflow restarted from earlier retry state? | **YES** — Gmail still eligible each poll; Expand treated all as pending attempt_number=1 |

## Recipient opaque refs (stable across polls)

- Admin anchor: `u:3FBE21323E22`
- Moderators: `u:26B9B999DE8A`, `u:518CC34C4C0F`, fourth opaque `u:…` (Никита)

No raw Telegram chat IDs committed.
