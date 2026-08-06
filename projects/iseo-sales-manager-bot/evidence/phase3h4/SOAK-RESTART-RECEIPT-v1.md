# SOAK RESTART RECEIPT v1

## Prior soak invalidated

Soak attempt 1 (started 06.08.2026 14:20 МСК) invalidated by Phase 3H.4 observability repair — not by production delivery failure.

## New soak T+0 (provisional)

| Field | Value |
|---|---|
| T+0 | **2026-08-06 19:15 Europe/Moscow** |
| T+0 ISO | 2026-08-06T16:15:00.000Z |
| Earliest valid PASS | **2026-08-08 19:15 Europe/Moscow** |
| Earliest PASS ISO | 2026-08-08T16:15:00.000Z |

## Preconditions met at restart

- Reminder status live acceptance PASS
- Status live acceptance PASS
- Three consecutive empty-poll heartbeats PASS (exec 24222, 24223, 24228)
- Offline harness PASS
- AI OFF · reminders ON · active recipients=3

## Rules (unchanged)

- No feature work during soak
- Phase 3I.1 blocked until soak PASS + explicit approval
- Checkpoint evidence under `evidence/phase3h4/SOAK-CHECKPOINT-T0-v2.md` + ongoing `evidence/pre-ai-soak/`

## Note

Parent operator may adjust T+0 if deploy completion time differs; provisional anchor documented for charter continuity.
