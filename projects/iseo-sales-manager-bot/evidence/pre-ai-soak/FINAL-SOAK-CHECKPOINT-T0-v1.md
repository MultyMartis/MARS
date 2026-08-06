# FINAL SOAK CHECKPOINT T0 v1

| Field | Value |
|---|---|
| Process-line | ISEO-SALES-MANAGER-BOT — PHASE 3H.5 FINAL PRE-AI SOAK OBSERVATION CHECKPOINT T+0 |
| Final soak T+0 (charter) | **2026-08-06 16:20 Europe/Moscow** |
| Checkpoint executed at | **2026-08-06 19:52 Europe/Moscow** |
| Soak elapsed at checkpoint | **~3h 32m** |
| Remaining to earliest T+48 | until **2026-08-08 16:20 Europe/Moscow** (~44h 28m at observation) |
| Next calendar checkpoint | T+6 @ **2026-08-06 22:20 Europe/Moscow** (not claimed; not fabricated) |
| Mode | Read-only live observation |
| Workflows patched | **0** |
| Soak restarted | **no** |
| AI enabled | **no** |
| Phase 3I.1 started | **no** |

## Verdict

`SOAK T+0 STOP — PRODUCTION INVARIANT VIOLATION`

## STOP proofs (sanitized)

1. **Access change after T+0** — Admin exec ~16:54 МСК upserted MOD_C_REVOKED identity to `active` (same identity hash as baseline revoked Никита).
2. **Revoked delivery** — Ops exec ~16:56 МСК expanded delivery to **4** chats including the MOD_C identity and sent **4** successful Telegram lead cards (baseline active recipients=3).
3. **Profile integrity break** — after reactivation, MOD_C row observed with blank `profile_no` while identity remains active; baseline required profile **4 / revoked / no cards**.

## What remained healthy

- Operational.dev `xSnXPy8cEHoZw6xG` active, **45** nodes, schedule **2** minutes
- Admin.dev `wLrLp4WQHm1VJmxz` active, **85** nodes
- Sales-Manager-v2 inactive
- Sole Gmail **intake** remains Operational `Gmail Fetch Leads` (Admin has health probe only)
- Scheduled empty polls succeed with heartbeat `iseo-gmail-poll-heartbeat-v1.0`
- AI OFF · OpenRouter calls observed **0** · customer auto-send **0**
- Reminder engine armed (10:00 Europe/Moscow); no production reminder send required/observed for 06.08 10:00 window (T+0 after that window)
- Reporting mode MANUAL unchanged

## Genuine lead activity after T+0 (not itself a soak failure)

| Alias | Approx МСК | Notes |
|---|---|---|
| PROD_LEAD_2 | 06.08.2026 16:26 | ingested; **3/3** eligible cards; MOD_C revoked at that moment |
| PROD_LEAD_3 | 06.08.2026 16:56 | ingested; **4** cards including reactivated MOD_C; later marked **spam** via callback |

Baseline PROD_LEAD_1 (05.08.2026 17:22 МСК processed) remains historical truth; CONFIG `last_production_processed_*` was overwritten by later Ops runtime stamps (watch item / status-cache semantics).

## Phase 3I.1 gate

**Blocked.** No AI pilot. Explicit operator remediation required before any soak PASS claim.

## Evidence set

See supporting files in this folder with suffix `-T0-v1.md`.
