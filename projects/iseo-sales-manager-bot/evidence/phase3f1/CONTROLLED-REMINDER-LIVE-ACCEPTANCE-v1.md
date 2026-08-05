# CONTROLLED REMINDER LIVE ACCEPTANCE v1

**Scope:** one controlled, operator-authorized live exercise of the scheduled reminder path (not a full production activation).

## What was reached

The scheduled trigger path executed through:

```
Schedule Trigger (15m) → Read CONFIG (Gate) → isReminderWindowDue → CLEAN pending view read → ACCESS_CONTROL read
```

`Gate → CLEAN → ACCESS` — the gate correctly evaluated `due=true` for the controlled window, the pending view read against `lead_clean_v2` succeeded, and the flow reached the ACCESS_CONTROL snapshot read for recipient selection.

## What stopped it (correct fail-closed behavior)

The ACCESS_CONTROL read hit the pre-existing Google Sheets quota / rate-limit condition (the same class of condition documented in Phase 3E.2.2/3E.2.3). Per the fail-closed contract (see [REMINDER-IDEMPOTENCY-v1.md](REMINDER-IDEMPOTENCY-v1.md) and `architecture/DELIVERY-FAIL-CLOSED-RECONCILIATION-v1.md`), the engine did **not** fall back to a cached, partial, or default recipient list — it stopped and recorded zero sends.

## Outcome

| Counter | Value |
|---|---:|
| Gate reached `due=true` | yes |
| CLEAN pending read | succeeded |
| ACCESS_CONTROL read | rate-limited (quota) |
| Dual Telegram reminder sends completed | **no** — not completed in this window due to quota |
| Reminder sends in this window | 0 |
| Fail-closed correctness | confirmed — zero sends is the correct outcome, not a defect |

## Reconciliation posture for the incomplete window

Because the window did not complete (no claim rows were written, since the flow stopped before recipient selection), there is nothing to reconcile as `claimed`/`uncertain` for this specific window attempt. The applicable rule going forward: **any later schedule check for this same calendar window must also produce zero sends** unless the operator explicitly clears the incomplete state — this matches the "later checks must remain zero when window incomplete/ledger claimed" requirement and is structurally guaranteed by the same window-key/ledger idempotency described in [REMINDER-WINDOW-KEY-v1.md](REMINDER-WINDOW-KEY-v1.md) and [REMINDER-DELIVERY-LEDGER-v1.md](REMINDER-DELIVERY-LEDGER-v1.md).

## Production state after the controlled window

Reminders were left **disabled** (`pending_reminders_enabled=false`) with the default schedule (`10:00`, `Europe/Moscow`) restored — this controlled exercise did not leave the engine armed.

## What this does and does not prove

**Proves:** the schedule trigger fires, the gate logic executes against live CONFIG, the pending view reads real CLEAN data, and the fail-closed contract holds under a real Sheets quota condition (not just an offline stub).

**Does not prove:** a successful end-to-end dual-recipient Telegram delivery under live conditions — that remains for the operator-authorized activation window (post-charter), consistent with the Phase 3F.1 verdict `OPERATOR ACTIVATION PENDING`.

*Related: [REMINDER-SCHEDULE-GATE-v1.md](REMINDER-SCHEDULE-GATE-v1.md), [REMINDER-SHEETS-CALL-BUDGET-v1.md](REMINDER-SHEETS-CALL-BUDGET-v1.md).*
