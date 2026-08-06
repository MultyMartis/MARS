# NO-ROW-FAIL-CLOSED-BASELINE

Ambiguous transport + GET returning no row → `RECONCILE_BEFORE_RETRY`
reason_code equivalent: `NO_ROW_AMBIGUOUS`
Must NOT become `SAFE_TO_RETRY` merely because the row is absent.
Only separate authoritative proof that request never reached intake can permit future SAFE_TO_RETRY classification.
