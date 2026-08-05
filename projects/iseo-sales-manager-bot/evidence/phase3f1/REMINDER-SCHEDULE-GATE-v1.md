# REMINDER SCHEDULE GATE v1

**Function:** `isReminderWindowDue(now, cfg, opts)` in `implementation/runtime-libs/pending-leads-lib.mjs`. Consumed by an Admin.dev internal **Schedule Trigger, every 15 minutes** (not a new workflow — see [../../architecture/PENDING-REMINDER-v1.md](../../architecture/PENDING-REMINDER-v1.md)).

## Gate sequence

1. **Disabled check** — `pending_reminders_enabled !== true/'true'` → `due=false, reason=disabled`. Zero sends.
2. **Config validity** — invalid `pending_reminder_timezone` or `pending_reminder_time` → `due=false, reason=invalid_config`. Zero sends (fail closed on bad config, never a guess).
3. **Window check** — compute local time in the configured timezone (`localPartsInTimezone`); due only when `now` falls in `[target, target+windowMinutes)` (default window 20 minutes, tolerant of the 15-minute checker's own drift).
4. **Already-completed check** — if `pending_reminder_last_window` already equals the computed window key, `due=false, reason=already_completed`. Zero sends — this is the cross-poll idempotency backstop (see [REMINDER-WINDOW-KEY-v1.md](REMINDER-WINDOW-KEY-v1.md)).
5. **Due** — returns `{ due: true, windowKey, local, timezone, time }` for the caller to proceed to recipient snapshot + pending view + delivery.

Downstream (not part of this pure function, enforced by the caller / harness contract cases):

- Zero pending leads in the due window → zero sends (#26).
- Pending count below `pending_reminder_min_count` → zero sends (#27).

## Cases proven

| ID | Case | Result |
|---|---|---|
| 24 | Disabled → zero sends | PASS |
| 25 | Outside window → zero sends | PASS |
| 26 | Due window, zero pending → zero sends | PASS |
| 27 | Due window, pending below min count → zero sends | PASS |
| 28 | Due window, pending ≥ min count, 2 eligible recipients → two reminders | PASS |
| 29 | Revoked recipient never selected | PASS |
| 31 | Already-completed window → zero sends | PASS |
| 36 | Three later schedule checks after completion → zero duplicates | PASS |
| 37 | Timezone/date-boundary helper remains stable across offset inputs | PASS |
| 38 | Invalid time (`25:99`) rejected | PASS |
| 39 | Invalid timezone (`Not/AZone`) rejected | PASS |
| 40 | Valid `10:00` / `Europe/Moscow` readback | PASS |

## Fail-closed posture

Every branch that cannot positively prove "send now" returns `due=false`. There is no default-to-send path.

*Related: [REMINDER-WINDOW-KEY-v1.md](REMINDER-WINDOW-KEY-v1.md), [REMINDER-IDEMPOTENCY-v1.md](REMINDER-IDEMPOTENCY-v1.md).*
