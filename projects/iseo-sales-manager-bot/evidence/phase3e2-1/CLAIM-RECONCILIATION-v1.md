# CLAIM-BEFORE-SEND HARDENING + RECONCILIATION v1

## Hardening applied (Operational.dev, same workflow ID)

1. Deterministic delivery key per stable lead + recipient.
2. Trustworthy ledger read required before claim.
3. Persist claim **before** Telegram send.
4. `Upsert LEAD_DELIVERIES Claim`: removed continue-as-success on error (fail before send).
5. `Restore Claimed Delivery Items`: block send if claim not persisted / claim error.
6. Stamp `delivered` after Telegram success; stamp failure → uncertain / reconciliation_required — **no automatic resend**.
7. `Append LEAD_EVENTS`: continue-on-error so Gmail finalize / CONFIG fallback can still run after quota on events.
8. Secondary CONFIG guard: `tg_delivered:<stable_lead_ref>:<recipient_ref>` (and gmail+recipient variants) written after successful send.

## Terminal rules

- `delivered` is terminal.
- Successful Telegram response must never be followed by blind resend.
- Quota after success is audit/reconciliation, not resend permission.

## Sheets CAS limitation

Google Sheets nodes do not provide atomic compare-and-set. Mitigation: serialized claim-before-send, fail-closed reads, CONFIG secondary guard, no blind retry of `claimed`/`uncertain`.
