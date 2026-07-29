# FAILURE-BOUNDARIES (B0–B7)

**Token:** `D6E_FAILURE_BOUNDARIES_DEFINED`

| Id | Boundary | Meaning |
|----|----------|---------|
| B0 | Before request construction | No request object; semantic / charter / readiness failure |
| B1 | Constructed, not transmitted | Local failure before wire; may be transient with no side effect |
| B2 | Transmission attempted, acceptance unknown | Ambiguous transport; reconcile |
| B3 | Server intake response known | HTTP status/body class known |
| B4 | Durable claim row known | Data Table row present (or authoritative absence) |
| B5 | Telegram outcome known or unknown | SUCCESS / DEFINITE_FAILURE / UNKNOWN |
| B6 | Final ledger state known or unknown | PENDING / SENT / FAILED (or missing) |
| B7 | Lifecycle containment known or unknown | Contained / anomaly / CONTAINMENT_FAILED |

Each observation maps into these boundaries before a decision state is assigned.
