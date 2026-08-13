# SCHEDULE EXECUTION FORENSIC — Phase 3H.8

## Classification
**`REMINDER_TRIGGER_EXECUTED`**

## Facts
- Node: `Reminder Schedule Trigger` (scheduleTrigger, every 15 minutes)
- Workflow settings timezone: unset (gate uses CONFIG `Europe/Moscow`)
- Executions at expected window (MSK):
  - 2026-08-13 10:00:21 — exec 29969
  - 2026-08-13 10:15:21 — exec 29977
  - Same pattern on 2026-08-12 / 11 / 10
- Activation: Admin active throughout
- Not wrong timezone: local_date and windowKey use Europe/Moscow correctly in gate output
