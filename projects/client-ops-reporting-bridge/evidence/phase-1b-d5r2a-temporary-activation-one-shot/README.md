# Evidence — Phase 1B-D5R2A

Controlled real-source delivery with temporary n8n activation and immediate re-containment for event `c84e29bf-79b1-5aea-98c4-9dc8d651fc96` / run `2026-07-26_17-48-38`.

## Outcome summary

- Pre-activation gates: **ALL PASS**
- Temporary activation: **YES** (`inactive → active`)
- Production webhook ready: **YES** (control-plane; no probe POST)
- Real producer HTTP requests: **1**
- HTTP intake: **202 recovered via GET-only** (producer stdout JSON parse failed; Respond Accepted + FIRST_SEEN)
- n8n executions: **31 → 32** (execution `3416`, success, webhook)
- Data Table rows: **2 → 3**; selected event rows: **0 → 1**; `intake_state=FIRST_SEEN`
- Telegram: attempted **1**, delivered **1**, `message_id=7`
- Retries / replay: **0**
- Deactivation: **YES** (`active → inactive`); `activation_changes=2`
- Final workflow active: **false**
- Runtime clean @ `8bb6e8f0f56388c12fdb013cf4cc1b27eb84331c`
- Old D5 charter: **UNUSED**
- D5R2 charter: **CONSUMED** (historical HTTP 404)
- D5R2A charter: **CONSUMED**

## Verdict

`D5R2A_FIRST_SEEN_DELIVERY_VERIFIED`

Readiness: `READY_FOR_D5R2A_EVIDENCE_BASELINE_COMMIT`

## Notes

- Helper scripts `_get-precheck.mjs`, `_live-orchestrator.mjs`, `_http-recovery.mjs` are phase tooling under this evidence pack (not production runners).
- Raw webhook URL, raw request body, raw execution payload, and Telegram token are **not** stored.
- Durable post-Telegram SENT ledger remains **DEFERRED** (`delivery_state` may remain `PENDING` in Data Table despite Telegram success).
