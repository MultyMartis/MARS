# SECURITY-REVIEW

- No n8n API key / Telegram token / webhook secret in task args, wrapper argv, or evidence JSON
- Secret contour referenced by path only (`local\tokens\n8n-api.env`) for GET-only
- Receipts/logs sanitized
- No customer payloads persisted in evidence
- Task XML hash recorded; credentials not exported

Tokens: D6D3_SECRET_BOUNDARY_PRESERVED; D6D3_SECURITY_AND_DATA_MINIMIZATION_PASS

