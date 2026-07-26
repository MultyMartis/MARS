# D5R2 Historical Failure

## Classification

`D5R2_REQUEST_REJECTED_BEFORE_WORKFLOW_INTAKE`

## Facts

| Field | Value |
|-------|-------|
| HTTP | 404 |
| intake_accepted | false |
| real_http_requests | 1 |
| retries | 0 |
| replays | 0 |
| workflow executions added | 0 |
| Data Table rows added | 0 |
| Telegram attempted | 0 |
| activation changes | 0 |
| workflow active | false (throughout) |
| charter | CONSUMED |

## Interpretation

Candidate was fresh and source authority matched; runtime was clean; event was unseen. The one authorized producer request hit the production webhook while the workflow remained inactive (D5R2 activation cap = 0). Request was rejected **before** workflow intake. Do **not** rewrite D5R2 as successful.

## Evidence locus

`projects/client-ops-reporting-bridge/evidence/phase-1b-d5r2-controlled-real-source-retry/`
