# SECURITY-REVIEW — D6D2B

Token: **D6D2B_SECURITY_CLEAN**

Scoped scan of A+B+C+D candidate files for:
- n8n API key / Telegram token / webhook secret / Authorization header
- secret-bearing URL / raw `.env` / customer payload
- personal Telegram identity / raw workflow-execution payload
- Windows credentials / local secret values
- runtime-state secret references **with values**
- raw logs with sensitive content

Allowed sanitized values present by design: workflow ID, versionId, Data Table ID, run/event IDs, artifact hashes, path templates, counts/states, non-secret kill-switch mode, sanitized receipt/cursor fields.

Findings in scoped candidates: **none** that embed live secrets or customer payloads.

Unrelated repository-wide findings (if any) are out of D6D2B scope and do not block this evidence commit.
