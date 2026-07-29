# D6D-CURSOR-AND-LOCK-BASELINE

- Local cursor outside Git; not delivery authority
- Durable Data Table overrides cursor: `D6D_LEDGER_OVERRIDES_CURSOR`
- Cursor never overrides ledger: `D6D_CURSOR_NEVER_OVERRIDES_LEDGER`
- Cursor write failure after durable SENT must not cause resend
- Producer singleton lock separate from Workstream C lifecycle lock
- MAX_CANDIDATES_PER_RUN=1, MAX_SAFE_CONCURRENCY=1, AUTOMATIC_RETRIES_ENABLED=NO, MAX_AUTOMATIC_RETRIES=0
