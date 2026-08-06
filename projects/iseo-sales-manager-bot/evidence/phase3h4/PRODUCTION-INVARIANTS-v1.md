# PRODUCTION INVARIANTS v1 — Phase 3H.4

## Contour

- Operational.dev **45** nodes · active · sole Gmail fetch
- Admin.dev **85** nodes · active · commands + reminders
- Sales-Manager-v2 **inactive**
- workflows_created = **0**

## Safety

- AI **OFF** · no OpenRouter production calls
- No customer auto-send
- No role/profile wipes during observability repair
- No LEADS row loss or duplication

## Production statistics epoch (unchanged)

- received=1 · pending=0 · processed=1 · spam=0
- Authoritative lead: `lead_19fd2052066e18b7`
- Stats epoch display: 05.08.2026 16:02 МСК received

## Observability invariants (new / reinforced)

1. Scheduled poll heartbeat written on empty runs
2. `/status` production lead line uses `last_production_processed_*`
3. `/health` Gmail probe ≠ scheduled poll heartbeat
4. `/reminder_status` returns visible reply for ADMIN_A and MOD_A

## Phase gate

Phase **3I.1** remains blocked until 48h soak PASS after restart T+0.
