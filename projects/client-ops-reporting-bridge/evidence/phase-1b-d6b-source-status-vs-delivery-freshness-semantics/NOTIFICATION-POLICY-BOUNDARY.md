# NOTIFICATION-POLICY-BOUNDARY

**Token:** `D6B_NOTIFICATION_POLICY_BOUNDARY_DEFINED`

Three distinct questions:

1. **What is the factual source status?** → `normalized_status` / mapped event status  
2. **Is the artifact fresh/safe enough to act on now?** → `delivery_eligibility`  
3. **Does notification policy require a customer message for that status?** → existing D5/action policy (unchanged; not broadened)

D6B does **not** overload `delivery_eligibility` with “should customer receive this status type.”  
Example: fresh `FAILED` may be `FRESH_AND_ELIGIBLE` while operators still decide whether FAILED notifies.

Stale valid ATTENTION remains ATTENTION but is not live-authorized and emits no customer `simple_text`.
