# NO-POLICY-BYPASS

**Token:** `D6E2_NO_POLICY_BYPASS_VERIFIED`

```json
{
  "no_bypass": true,
  "probes": [
    {
      "id": "PENDING",
      "decision": "RECONCILE_BEFORE_RETRY",
      "reason_code": "PENDING_NEVER_AUTO_RETRY",
      "retry_authorized": false,
      "bypass": false
    },
    {
      "id": "SENT",
      "decision": "UNSAFE_TO_RETRY",
      "reason_code": "ALREADY_SENT",
      "retry_authorized": false,
      "bypass": false
    },
    {
      "id": "TELEGRAM_SUCCESS_PENDING",
      "decision": "UNSAFE_TO_RETRY",
      "reason_code": "HISTORICAL_PENDING_BLIND_RETRY_PROHIBITED",
      "retry_authorized": false,
      "bypass": false
    },
    {
      "id": "UNKNOWN_EXEC_PENDING",
      "decision": "RECONCILE_BEFORE_RETRY",
      "reason_code": "TELEGRAM_UNKNOWN_PENDING",
      "retry_authorized": false,
      "bypass": false
    },
    {
      "id": "CONTAINMENT_FAILED",
      "decision": "FINAL_FAILURE",
      "reason_code": "CONTAINMENT_FAILED",
      "retry_authorized": false,
      "bypass": false
    }
  ]
}
```
