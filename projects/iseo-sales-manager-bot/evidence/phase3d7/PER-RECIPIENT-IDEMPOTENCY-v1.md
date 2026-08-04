# PER-RECIPIENT IDEMPOTENCY v1

## Key

`lead_delivery:<stable_lead_ref>:<recipient_ref>`

`recipient_ref` = opaque `u:<hash>` — never username, never raw id in git evidence.

## States

| State | Meaning |
|-------|---------|
| pending | eligible, send attempted / in flight |
| delivered | success — never resent |
| failed_retryable | may retry (bounded) |
| failed_terminal | exhausted / hard fail |
| skipped_ineligible | not deliverable |

## Guarantees

- Successful recipients are never resent because another recipient failed.
- Later Gmail polls do not resend delivered copies.
- Max attempts: 5.
