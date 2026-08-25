# Reminder Contract

**Authority:** [PRODUCTION-STABLE-BASELINE-2026-08-17.md](../baselines/PRODUCTION-STABLE-BASELINE-2026-08-17.md)

## Stable Rules

| Rule | Current value |
|------|---------------|
| Enabled | `pending_reminders_enabled=true` |
| Time | `10:00` |
| Timezone | `Europe/Moscow` |
| Days | Monday-Friday |
| Monday backlog | Includes weekend pending backlog |
| Lifecycle mutation | none |

## Candidate Selection

Include all still-actionable real pending leads.

Exclude:

- processed;
- spam;
- tests;
- archive/legacy non-production;
- records that cannot be safely classified as actionable.

## Notification-Only Boundary

A reminder tells managers what still needs attention. It must not:

- mark a lead processed;
- mark a lead spam;
- update status to contacted/reviewing;
- erase pending state;
- mutate RAW.

## Natural Monday Observation

The natural Monday reminder acceptance is still **PENDING OBSERVATION** per stable known-state docs. Do not claim PASS unless a later evidence-backed document supersedes that state.

## Schedule Safety

If the weekday gate, CONFIG, or timezone is uncertain, fail closed and investigate. Do not manually trigger during freeze or stable validation unless the operator explicitly charters a test and records it as synthetic.

## Required Evidence For Acceptance

- CONFIG keys show enabled/time/timezone.
- Admin schedule path uses Mon-Fri gate.
- Candidate query includes real pending and excludes non-actionable states.
- Monday backlog logic includes weekend pending records.
- Reminder delivery produces no lifecycle mutation.

