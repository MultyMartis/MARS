# FINAL-STATE-v1

## Verdict

`CLEAN DUPLICATE SOURCE FIXED — INGEST IDEMPOTENCY LIVE PASS`

Secondary note: `SOURCE FIXED — HISTORICAL DUPLICATES RETAINED FOR SEPARATE RECONCILIATION`

## Soak

`READY FOR NEW 48H SOAK` — **do not start** until operator approval.

## Counters

| Metric | Value |
|--------|------:|
| duplicate CLEAN clusters found | 3 |
| production-real duplicate clusters | 2 |
| SAFE_UNKNOWN duplicate clusters | 0 |
| proven-test residual clusters | 1 |
| current duplicate-producing paths | 0 |
| CLEAN writer nodes (ingest append/upsert) | 1 Ops (+ DEDUP ledger) |
| same-event executions tested | 3 |
| additional CLEAN leads from same-event replay | 0 |
| distinct events tested | 2 |
| false dedupe events | 0 |
| duplicate creation events after fix | 0 |
| real historical rows mutated | 0 |
| SAFE_UNKNOWN rows mutated | 0 |
| moderator messages | 0 |
| customer messages | 0 |
| AI calls | 0 |

## Git base

origin/mars/canonical-post-recovery @ `12327f1d` at wave start; worktree `wave/iseo-sm-clean-dup-forensic-20260826-175345`.
