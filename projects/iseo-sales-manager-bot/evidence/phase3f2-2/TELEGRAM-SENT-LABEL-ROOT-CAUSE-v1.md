# TELEGRAM_SENT LABEL ROOT CAUSE v1

## Summary

`lifecycle_reconciled` was humanized; `telegram_sent` leaked as a raw machine code.

## Exact cause

In Admin.dev node **Lead History Handler**:

1. `EVENT_DISPLAY` listed `delivered_to_employee` and `lead_card_delivered`, but **not** `telegram_sent`.
2. `mapEvent()` had explicit branches for `lifecycle_reconciled` and `delivered_to_employee`.
3. Fallback was:

```js
return (EVENT_DISPLAY[t] || t || 'событие').toLowerCase();
```

4. Production LEAD_EVENTS for the first real lead stores delivery as **`telegram_sent`** (Operational append), not `delivered_to_employee`.
5. Therefore the unknown code path returned the raw string `telegram_sent` into the Telegram bullet.

## Why reconciled looked fine

`lifecycle_reconciled` had an explicit early return with the human phrase, so it never hit the raw fallback.

## Not the cause

- Reporting workbook mapper is separate; this defect was the Telegram history mapper.
- Alias normalization did not rewrite `telegram_sent` → `delivered_to_employee` before display.
- Event summary fields were not used as primary text for these rows.

## Fix

- Add `telegram_sent` (and remaining supported codes) to the human map.
- Unknown codes → `техническое событие` (never raw).
- Preserve missing-timestamp wording for legacy delivery rows.
