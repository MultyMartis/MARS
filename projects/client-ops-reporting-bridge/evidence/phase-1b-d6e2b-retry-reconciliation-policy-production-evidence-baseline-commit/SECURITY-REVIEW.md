# SECURITY-REVIEW — D6E2B

**Token:** `D6E2B_SECURITY_CLEAN`

Scoped candidate scan: no n8n API key values, Telegram tokens, webhook secrets, Authorization bearer values, secret-bearing webhook URLs, raw credentials, .env values, customer payloads, raw execution/workflow/Telegram payloads, or personal Telegram identity in allowlisted files.

Mentions of the phrase `webhook secret` appear only as **denied-category labels** in security docs / boolean flags (`no_webhook_auth_secret: true`) — not secret values.

Repository-wide unrelated historical findings (if any) are outside candidate scope and do not block this commit.

Allowed sanitized identifiers retained: workflow ID, versionId, Data Table ID, event IDs, execution 3416, sanitized message_id=7, states/counts/timestamps.
