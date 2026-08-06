# D6D3-INITIAL-FAIL-CLOSED-RUN-BASELINE

Token: **D6D3B_INITIAL_FAIL_CLOSED_RUN_CLAIMS_ACCURATE**

| Field | Value |
|-------|-------|
| Scheduled invocation count | 1 |
| Result | `BLOCKED_KILL_SWITCH` |
| Exit | 20 |
| Reason | `KILL_SWITCH_SITE_MISMATCH` |
| Real-artifact inventory reached | NO |
| Cursor | unchanged / no SENT or DELIVERED claim |
| Side effects | 0 |
| Task post-state | Disabled |
| Wrapper fix applied after run | YES |
| Second D6D3 invocation | NO |

Root cause: wrapper parsed kill-switch and passed reduced object lacking `site_id`; producer re-parsed and fail-closed before artifact inventory.

Historical failure **must remain visible**. Do not rewrite D6D3 as success.
