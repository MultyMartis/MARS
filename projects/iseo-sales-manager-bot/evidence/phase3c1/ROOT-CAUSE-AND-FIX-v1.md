# ROOT CAUSE AND FIX v1

## Root cause

**Stage:** Gmail label/query eligibility.

1. Website form mail **was delivered** to the production Gmail mailbox (automated-form-like, post-cutover timestamps).
2. Candidates are in **Trash** without the production **incoming** label.
3. Operational.dev Schedule Trigger + Gmail node poll every ~30s successfully with **0 eligible items** under the accepted `labelIds` filter (parity with Sales-Manager-v2).
4. Therefore no Parse → RAW → CLEAN → Telegram path ran; Admin `/status` still showed last lead success/error from **30.07.2026 22:49 МСК**.

## Not root causes (evidenced)

- Dual active operational workflows (PROD inactive, OPS active)
- Schedule Trigger disabled/disconnected
- Credential hash mismatch vs v2
- AI path (OpenRouter remains disabled)

## Fix applied in this phase

1. **Observability:** empty-poll updates `last_poll_success_at`; distinguish poll vs lead vs error in `/status`.
2. **Healthcheck:** Admin `/health` performs bounded Gmail query (same incoming label filter) and reports Russian wording with count.
3. **Early failure routing:** Intake Gate + Switch for empty/error/lead; Gmail `alwaysOutputData` + continue-on-error toward Error Handler for read failures.

## Not applied (by safety boundary)

- No untrash / broad relabel of operator messages
- No weakening of production label filter
- No reactivation of Sales-Manager-v2
- No automatic client messages / AI calls
