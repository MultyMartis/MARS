# EXACTLY-ONCE UNDER RETRY v1

Harness:

- Recover after one 429 then send: 4 claims / 4 successes.
- Second evaluation same business date: 0 additional claims (`SKIPPED_ALREADY_SENT` or empty claims).
- Failed all-retries run then later successful eval: date **not** poisoned; second eval can still send.
- Claim keys unique (one recipient + one business date).

Live invariant preserved: `pending_reminder_last_window` stamped only after successful window completion. Failed 2026-08-14 10:00/10:15 left `last_window=null` (reconfirmed post-change CONFIG read).
