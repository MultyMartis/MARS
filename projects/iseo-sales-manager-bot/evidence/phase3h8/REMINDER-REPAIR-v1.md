# REMINDER REPAIR — Phase 3H.8

Workflow: Admin.dev `wLrLp4WQHm1VJmxz` (same ID; nodes remain 87)

## Changes
1. Retarget CLEAN reads `LEADS` → `lead_clean_v2`:
   - Read CLEAN for Reminder
   - Read CLEAN for Pending
   - Read CLEAN for Stats
   - Read CLEAN for Leads
   - Read LEADS for History
2. Expand Reminder/Pending ranges to `A1:ZZ500`
3. Reminder Mark Window Complete + Prepare: evaluation observability writes; **do not** stamp `pending_reminder_last_window` on zero_pending
4. Wire IF Reminder Proceed false → Mark Window Complete (gate-skip observability)
5. Reminder Commands: expose last evaluation / decision / pending snapshot (`iseo-reminder-observability-v1.1`)

Operational.dev unchanged. Reminder time unchanged. AI OFF. No new workflows.
