# PRODUCTION PROPOSAL v1 (NOT APPLIED; PHASE 3C READY)

## Recommendation

**Phase 3B.2 readiness review:** the private-operator Telegram sandbox, Sheets mapping refresh, Parse Lead runtime fix, and zero-token AI OFF path are accepted. Promote accepted Operational.dev to production role only during an explicitly approved Phase 3C cutover window, then deactivate original Sales-Manager-v2 in the same cutover. Do **not** patch original in-place as the default path.

Admin.dev activation: keep **inactive for scheduling**; enable Telegram Trigger only after sandbox destination + allowlist are set; prefer manual/on-demand admin use first.

## Cutover order (proposed)

1. Operator approves this proposal and the Phase 3C production charter.
2. Reconfirm current workflow exports and CONFIG before the window.
3. Set CONFIG: `environment=production` only at cutover; keep `ai_enabled=false`.
4. Point Telegram manager chat to the **production** manager destination (separate from sandbox).
5. Enable Telegram send + Gmail mutate on promoted Operational graph only under charter.
6. Disable Schedule on original and enable Schedule on promoted Operational in the same cutover.
7. Keep Admin activation as a separate decision; its Trigger remains off until that decision is closed.
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

## Explicitly not done in Phase 3B.2

No production activation, no original disable, no cutover.
