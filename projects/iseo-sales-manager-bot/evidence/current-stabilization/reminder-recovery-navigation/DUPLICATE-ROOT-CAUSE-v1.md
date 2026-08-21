# DUPLICATE ROOT CAUSE

## Exact first divergence

After primary Telegram success, the workflow **never entered** `Reminder Mark Window Complete` on the success path.

Therefore:

1. `pending_reminder_last_window` stayed empty → recovery gate still `proceed=true` for the same business window.
2. At recovery, `Read REMINDER_DELIVERIES` yielded an unusable empty item → recipient-level delivered skip did not fire → ADMIN_A claimed/sent again.

## Not the root

- Different business-window keys (keys were **identical**)
- Wrong recipient set (still ADMIN_A only)
- Intentional resend policy (none)

## Contributing factors

- Success path wiring: `Upsert REMINDER_DELIVERIES Delivered` was a dead-end (no Mark Complete).
- ACCESS 429 retry storm + multi-item fan-in into ledger read (hardened with collapse node).
- Skip logic previously treated `claimed` like delivered (narrowed to delivery truth only).
