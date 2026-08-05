# BACKOFF AND RETRY POLICY v1

**Status:** DEPLOYED and happy-path live-proven.

Critical operations retain bounded retry: maximum 3 attempts with 30-second delay for bounded ledger read, ACCESS_CONTROL read and claim upsert. No `continueOnFail` is permitted on access or claim.

During final proof all three critical classes succeeded on their normal path; quota errors=0. Offline harness separately proves exhaustion → zero send.
