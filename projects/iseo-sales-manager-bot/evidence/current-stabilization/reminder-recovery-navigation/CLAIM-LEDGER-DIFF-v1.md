# CLAIM / LEDGER DIFF — 2026-08-21

## Primary `36699`

| Step | Result |
|------|--------|
| Read REMINDER_DELIVERIES | 1 empty item `{}` (pre-write / soft-empty under retry storm) |
| Upsert Claim | success — key `…|3FBE21323E22BFC1` claimed |
| Telegram | message_id **1060** |
| Upsert Delivered | success echo — status delivered, `msg:1060` |

## Recovery `36708`

| Step | Result |
|------|--------|
| Read REMINDER_DELIVERIES | empty `{}` again at eval time → skip set empty |
| Build Claims | created **new** send for same key |
| Telegram | message_id **1061** |
| Upsert Claim/Delivered | **429** |

## Post-incident sheet truth (probe)

Sheet `REMINDER_DELIVERIES` holds **one** row for the window:

- status: `delivered`
- telegram_message_ref_safe: `msg:1060` (primary)
- recovery upsert did not overwrite (429)

## Diff summary

Primary wrote delivery truth; recovery did not observe it at Build Claims time and re-sent.
