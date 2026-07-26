# OFFLINE-SCHEMA-MODEL

**Token:** `D6A_OFFLINE_SCHEMA_MODEL_READY`

## Model

Reuse exact 15-column D1 schema. Terminal writes mutate **only** `delivery_state`.

No offline migration DDL required. No live column add.

Optional future columns documented in SCHEMA-DECISION.md as observability-only.
