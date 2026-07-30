# D6D3 Failure Baseline (preserved)

- Task: `\MARS_SITE_002_Client_Ops_Producer`
- Scheduled invocations attributable to D6D3: **1**
- Result: `BLOCKED_KILL_SWITCH`
- Exit code: **20**
- Reason: `KILL_SWITCH_SITE_MISMATCH`
- Real artifact evaluation: **not reached**

## Root cause

Wrapper parsed kill-switch JSON and passed the **parsed result object** into `runUnattendedProducer`.
Producer re-parses expecting raw JSON shape with `site_id`.
Parsed object lacked `site_id` → fail-closed before inventory.

## Post-failure action (D6D3)

- Wrapper corrected locally under runtime-state (pass RAW JSON)
- No second D6D3 scheduled invocation
- Producer task disabled
- Production side effects: 0

D6D3R does **not** rewrite this failure; it proves the corrected path separately.
