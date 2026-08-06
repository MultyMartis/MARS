# FOUR-RECIPIENT REMINDER ALIGNMENT v1

## Defect

`/config`=4 · `/reminder_status`=3 after MOD_C restore.

## Root cause

Stale CONFIG `pending_reminder_active_recipients_count=3`.

## Fix

1. CONFIG → 4  
2. Admin `Reminder Commands` live ACCESS count (Phase 3H.6)  
3. Reminder engine already dynamic — unchanged time 10:00 Europe/Moscow  
