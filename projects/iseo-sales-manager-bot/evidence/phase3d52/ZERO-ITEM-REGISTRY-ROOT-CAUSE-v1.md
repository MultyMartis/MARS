# ZERO-ITEM REGISTRY ROOT CAUSE v1

## Primary root cause

n8n Code nodes inlined Phase 3D.5.1 `access-lib` with:

`require('crypto').createHash('sha256')`

On the production task-runner this throws **`Module 'crypto' is disallowed`**, aborting `Check User Authorization` after Sheets reads. Execution status=`error`; Telegram reply never sent.

This is the same class of defect previously fixed in Operational `Parse Lead` (Phase 3B.2).

## Secondary root cause (amplifies silence)

`Read Authorization Config` returned one item per CONFIG row (~33). Each item triggered `Read ACCESS_CONTROL`, producing ~66 items and Google Sheets **rate limiting**. Subsequent operator commands failed at Sheets nodes with **zero reply items**.

`alwaysOutputData=true` does **not** convert API errors into a safe reply path unless `onError` continues and a downstream Code node emits a Telegram response.

## Not root causes

- Webhook missing (executions existed)
- Wrong bot Trigger ownership (Sales Manager credential unique among Admin contour)
- Empty ACCESS_CONTROL identities (Phase 3D.5.1 population already restored 2 rows)
- ACCESS_CONTROL authorization SoT logic itself (failed before decision completed)
