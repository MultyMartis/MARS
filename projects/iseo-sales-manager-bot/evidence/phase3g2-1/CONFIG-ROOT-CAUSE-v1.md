# `/config` root cause — Phase 3G.2.1

**Class:** runtime code exception (invalid token in Config Summary array literal)

## Defect

Phase 3G.2 Config Summary patch inserted multiple array elements as a single string containing literal `\n` sequences:

```text
'Стандарт первого ответа: INTLSEO approved templates',\n  'Персонализация...'
```

Live error: `Invalid or unexpected token` at Config Summary; Safe Telegram Reply not reached.

## Not the cause

- Router mismatch
- Authorization (Admin passed)
- Telegram parse rejection
- PROFILE_EVENTS

## Repair

Rebuilt Config Summary footer with discrete array lines covering contour, stats epoch, source display, parser/template/personalization versions, AI, reminders, reporting sync state, active recipient count; secrets omitted; unavailable → `не задано`; try/catch guard; `onError=continueRegularOutput`.

Post-patch Config Summary hash: `95ED814DCE102723`.
