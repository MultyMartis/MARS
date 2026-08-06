# REMINDER RECIPIENT FORENSIC — Phase 3H.6

## Flow traced

1. Reminder Schedule Trigger  
2. Read Reminder CONFIG  
3. Reminder Schedule Gate  
4. Pending count from LEADS (`Read CLEAN for Reminder` → sheet LEADS)  
5. Read ACCESS_CONTROL for Reminder  
6. Reminder Build Claims eligibility  
7. Claim upsert REMINDER_DELIVERIES  
8. Send Reminder Telegram  
9. Stamp / window complete  
10. `/reminder_status` count source  

## Actual send selector

`Reminder Build Claims` dynamically selects **active admin|moderator with Telegram binding** from ACCESS_CONTROL. Independent per-recipient claim keys.

## Status display selector (before repair)

`Reminder Commands.countActiveRecipients()` read **static CONFIG** key `pending_reminder_active_recipients_count` (value `3`).

## Discrepancy

`/config` used live ACCESS action-capable count → **4**  
`/reminder_status` used stale CONFIG cache → **3**  
Actual reminder fanout would already include MOD_C once active.
