# TASK-TRIGGER

- Type: Daily CalendarTrigger
- StartBoundary: 2026-07-31T13:00:00+07:00
- Rationale: 30 minutes after SITE-002 monitor window (12:30); separate delayed scan; not chained
- Timezone: local UTC+07
- During phase: exactly one *manual* Start-ScheduledTask; no automatic trigger fired
- After proof: task **Disabled** (ongoing schedule not authorized)

Token: D6D3_TASK_TRIGGER_DEFINED

