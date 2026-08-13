# REMINDER ROOT CAUSE — Phase 3H.8

## Primary
**`live_pending_selector_queried_obsolete_LEADS_tab_instead_of_authoritative_lead_clean_v2`**

Exact failed decision: `Reminder Build Claims` → `reminder_skip_reason=zero_pending` because `Read CLEAN for Reminder` queried obsolete `LEADS` instead of authoritative `lead_clean_v2`.

## Schedule class
`REMINDER_TRIGGER_EXECUTED` (not a schedule miss / timezone miss)

## Secondary
Pre-repair `/reminder_status` did not expose last evaluation decision (observability gap) — repaired to contract `iseo-reminder-observability-v1.1`.
