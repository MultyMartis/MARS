# Pre-Activation Preflight

**Token:** `D6C2_PRE_ACTIVATION_PREFLIGHT_PASS`

Kind: **DRY_LIFECYCLE** (not SOURCE_DELIVERY)

Gates verified:
- workflow_id allowlisted exact
- initial active=false
- version pin `dc8746bf-df9c-425d-9b3f-4ace452ac5ef`
- nodes=20
- running=0
- max_requests=1, planned_requests=0, allow_webhook_requests=false
- max_retries=0, max_concurrency=1, max_activation_changes=2
- webhook/auth structural presence
- source delivery / fabricated SITE-002 event: **skipped** (dry control)
