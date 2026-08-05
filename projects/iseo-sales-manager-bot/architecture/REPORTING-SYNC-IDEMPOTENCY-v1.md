# REPORTING SYNC IDEMPOTENCY v1

- Deterministic public lead ID
- Upsert by public ID — no duplicate reporting rows
- One event append per real event; retries must not duplicate
- Backend commit first; reporting sync secondary with `SYNC_STATE`
- Bounded backoff on outage; no customer-facing errors


## 3F.2.1

Targeted CLIENT_A resync updated one row; no duplicate lead rows; last-sync stamped once after meaningful repair.
