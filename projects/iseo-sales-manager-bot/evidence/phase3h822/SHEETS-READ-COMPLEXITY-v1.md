# SHEETS READ COMPLEXITY v1

## Production Reminder evaluation (Admin.dev)

| | Before patch | After patch |
|---|---|---|
| Logical Sheets reads | CONFIG, CLEAN, ACCESS_CONTROL, REMINDER_DELIVERIES | **same 4** |
| Per-lead Sheets API calls | 0 | **0** |
| Extra LEAD_EVENTS read in Build Claims | no | **no** (quota-safe) |

`LEADS_CURRENT` is resolved in-memory from the already-loaded `lead_clean_v2` bulk rows (product current-state store).

Required: `per-lead API calls = 0` — **met**.

Isolated proof TMP may read additional sheets for forensics; that is not the production reminder path.
