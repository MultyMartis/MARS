# PARSE LEAD RUNTIME FIX v1

## Result

**PASS.** `Parse Lead` no longer uses `require('crypto')`, which is unavailable in the n8n task-runner contour.

## Implemented runtime behavior

- `lead_id` is deterministic from `gmail_message_id` when present.
- When that value is unavailable, a pure-JavaScript FNV/djb2 fallback is used.
- Repeated parser execution on the same synthetic input yields stable lead and message identifiers.
- The emitted workflow version is `operational.dev.phase3b2`.

## Evidence

The local harness case `PARSE_STABLE` passed: stable identifiers and no crypto require. The original Sales-Manager-v2 workflow was not modified.
