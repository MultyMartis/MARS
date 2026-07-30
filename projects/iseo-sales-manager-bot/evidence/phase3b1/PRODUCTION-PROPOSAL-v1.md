# PRODUCTION PROPOSAL v1 (NOT APPLIED)

## Recommendation

**Promote accepted Operational.dev** to production role during an explicitly approved cutover window, then disable original Sales-Manager-v2 only after dual-run/smoke confidence. Do **not** patch original in-place as the default path.

Admin.dev activation: keep **inactive for scheduling**; enable Telegram Trigger only after sandbox destination + allowlist are set; prefer manual/on-demand admin use first.

## Cutover order (proposed)

1. Operator approves this proposal + sandbox Telegram review.
2. Refresh Google Sheets append column mappings for all v2 write nodes (blocking defect if skipped).
3. Replace `require('crypto')` in Parse Lead with task-runner-safe UUID helper.
4. Set CONFIG: `environment=prod` only at cutover; keep `ai_enabled=false`.
5. Point Telegram manager chat to **production** manager destination (separate from sandbox).
6. Enable Telegram send + Gmail mutate on promoted Operational graph only under charter.
7. Disable Schedule on original; enable Schedule on promoted Operational (or rename/promote).
8. Keep Admin Trigger off until admin chat coexistence decision is closed.
9. First production smoke: one synthetic or operator-supervised known test lead — never blind batch.
10. Monitoring period: 3–7 days AI OFF, then optional AI ON charter.

## Gmail race prevention

- Bound Gmail fetch (`returnAll=false`, low limit).
- Only one active scheduled Operational graph at a time.
- Do not run original and promoted schedules concurrently on the same incoming label.

## Rollback

1. Deactivate promoted Operational schedule.
2. Reactivate original Sales-Manager-v2 (known-good).
3. Force CONFIG `ai_enabled=false`.
4. Preserve ERRORS / LEAD_EVENTS for forensics.
5. See `plans/ROLLBACK-PLAN-v1.md`.

## Stop / rollback conditions

- Telegram delivery failures spike
- Gmail label races / double processing
- Sheets write failures / schema errors
- Any client auto-send incident (should be impossible — still a hard stop)
- Unexplained original workflow mutation

## Explicitly not done in Phase 3B.1

No production activation, no original disable, no cutover.
