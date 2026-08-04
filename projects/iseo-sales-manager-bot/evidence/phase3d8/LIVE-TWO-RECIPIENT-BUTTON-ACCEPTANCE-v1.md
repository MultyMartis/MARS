# LIVE TWO-RECIPIENT BUTTON ACCEPTANCE v1

## Pre-send

- Eligible ACCESS_CONTROL recipients: **2** (1 active admin + 1 active moderator)
- Revoked moderators: **2** (intentional; not restored)
- Synthetic fixture only (no real client email selected)
- Claim-before-send / LEAD_DELIVERIES guards active

## Results

| Check | Result |
|-------|--------|
| Admin receives exactly one original card | PASS (API send ok + reply_markup) |
| Moderator receives exactly one original card | PASS (API send ok + reply_markup) |
| Both cards show two action buttons | PASS (Telegram API `inline_keyboard` 2 buttons each) |
| No third copy across poll window | PASS (0 duplicate sends) |
| Selected recipient marks processed | PASS (harness callback after token sync: `pending→processed`) |
| Copies update to processed | PARTIAL — Edit succeeded for **1** known copy in harness; operator should confirm second client UI |
| Buttons disappear after transition | PASS on edited copy (`reply_markup=null`, status line Обработан) |
| Repeat click second mutation | Not re-tested after processed (first transition wins contract unchanged) |
| CLEAN one business fixture | PASS (synthetic lead present; status processed after callback) |
| LEAD_DELIVERIES two successful deliveries | PASS (stamp delivered ×2 on send path) |

## Notes

- Synthetic Gmail finalize (`Add Gmail PROCESSED`) errors are expected (fake Gmail id).
- Synthetic `Answer Callback Query` fails on fake `callback_query.id`; real Telegram presses use real query ids.
- `Expand Card Sync` found 1 copy in the harness.
- **ATTENTION:** operator should visually verify the second moderator copy and may perform one real Telegram click if desired.
- OpenRouter remained disabled; AI calls=0 and client messages=0.

## Verdict

`COMPLETE — BASELINE AND BACKUP READY; LIVE BUTTON CONFIRMATION PENDING`

Buttons are restored and API-proven on both sends. The remaining gap is visual confirmation in both Telegram clients because multi-copy sync observed one edited copy in the harness.
