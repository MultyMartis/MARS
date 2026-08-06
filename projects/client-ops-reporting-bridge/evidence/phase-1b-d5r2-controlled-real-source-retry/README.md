# Evidence — Phase 1B-D5R2

Controlled D5 manual real-source retry with revalidated fresh candidate `2026-07-26_17-48-38` / `c84e29bf-79b1-5aea-98c4-9dc8d651fc96`.

## Outcome summary

- All pre-live gates: **PASS**
- One producer HTTP request: **YES** (charter consumed)
- HTTP: **404** (not 202)
- n8n executions: **31 → 31**
- Data Table rows: **2 → 2**; selected event rows: **0 → 0**
- Telegram: **0**
- Activation changes: **0**
- Retries / replay: **0**
- Runtime clean @ `8bb6e8f0f56388c12fdb013cf4cc1b27eb84331c`
- Old D5 charter: **UNUSED**
- D5R2 charter: **CONSUMED**

## Verdict

Classification: `D5R2_REQUEST_REJECTED_BEFORE_WORKFLOW_INTAKE`

First-seen delivery: `D5R2_FIRST_SEEN_DELIVERY_NOT_VERIFIED`

Readiness: `PARTIAL_D5R2_REQUEST_REJECTED_BEFORE_WORKFLOW_INTAKE`

Note: HTTP 404 means the request was rejected before workflow intake. Do not interpret this attempt as a successful intake or as HTTP 202.
