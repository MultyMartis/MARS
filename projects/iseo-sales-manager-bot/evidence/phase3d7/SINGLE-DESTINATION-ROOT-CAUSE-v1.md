# SINGLE-DESTINATION ROOT CAUSE v1

**Phase:** 3D.7  
**Date:** 2026-08-04

## Verdict

Operational.dev delivered every accepted lead to **one** CONFIG destination: `telegram_manager_chat_id` from Normalize CONFIG (legacy manager chat — operator-observed as Андрей only).

## Exact nodes

| Node | Role |
|------|------|
| Send Telegram Lead Card With Buttons | `chatId = {{$('Normalize CONFIG').first().json.telegram_manager_chat_id}}` |
| Send Telegram Lead Card | same expression |

## Findings

| Question | Answer |
|----------|--------|
| Recipient source | CONFIG via Normalize CONFIG — **not** ACCESS_CONTROL |
| ACCESS_CONTROL read in Operational.dev (pre-3D.7) | **No** |
| Recipient items before Telegram send | **1** (no fan-out) |
| Telegram sends per lead | **at most 1** successful path |
| Delivery idempotency | **Lead-level** (`telegram_already_delivered` / `delivery_status`) — insufficient for fan-out |
| Stored Telegram message refs | Single CLEAN / gate fields — one chat |
| Assumes one destination | **Yes** |

## Safe matrix (recent window)

Recent Gmail polls in the forensic window were empty (no Format/Send runs). Structural proof still holds: chat expression is single CONFIG destination.

| Lead Execution | Active Staff | Recipient Items | Sends Attempted | Sends Successful |
|---|---:|---:|---:|---:|
| *(no lead-bearing exec in last ~100 empty polls)* | 4 | 1 (by design) | 1 | ≤1 |

## Secondary defect fixed in 3D.7

`IF Need Telegram Send` true branch previously targeted the send path when `skip_telegram=true`, leaving `Telegram Skip Pass` orphaned. Rewired: skip → Skip Pass; need-send → button/plain send.

## Not the cause

ACCESS_CONTROL authorization, moderator management, and `/my_status` — those Admin paths work; delivery never consulted the registry.
