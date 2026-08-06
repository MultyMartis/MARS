# CONTRACT-SURFACE-DECISION

**Decision:** `D6B_INTERNAL_MODEL_ONLY`

| Option | Chosen? | Why |
|--------|---------|-----|
| Internal model only | **YES** | ProcessResult + preview + live gate sufficient |
| Producer contract extension | no | eligibility not required in allowlisted producer input |
| Event schema version change | no | envelope still `freshness.{age_seconds,stale}` under `1.0` |
| Data Table schema change | no | eligibility is evaluation-time, not durable ledger state |

Workstream A `PENDING/SENT/FAILED` ledger untouched.
