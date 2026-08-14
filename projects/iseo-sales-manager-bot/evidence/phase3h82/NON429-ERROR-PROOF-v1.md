# NON-429 ERROR PROOF v1

Harness case `D_non429_fatal` (HTTP 500):

- no quota retry loop
- attempts=1
- last_decision=`ERROR`
- claims=0
- sends=0

Classifier: only HTTP 429 / quota message is retryable. Credentials / schema / malformed / permanent stop immediately.
