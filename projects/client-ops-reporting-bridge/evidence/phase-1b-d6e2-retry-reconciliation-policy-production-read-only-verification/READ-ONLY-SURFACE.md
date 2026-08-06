# READ-ONLY-SURFACE

**Token:** `D6E2_PRODUCTION_SURFACE_READ_ONLY_CONTROL_AND_LEDGER`

**Token:** `D6E2_READ_ONLY_SURFACE_DECLARED`

Allowed reads:
- workflow GET (allowlisted id)
- execution GET/list (allowlisted workflow / historical execution 3416)
- Data Table schema GET
- Data Table rows / event lookup GET (allowlisted event ids only)
- sanitized local historical evidence
- source/runtime read-only checks

Forbidden:
- POST webhook
- activate / deactivate
- workflow PUT/PATCH
- Data Table insert/update/delete
- Telegram API
- credentials mutation
- retry execution
- reconciliation mutation (PENDING→SENT/FAILED)
