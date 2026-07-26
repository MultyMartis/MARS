# MINIMAL-PRODUCTION-DELTA

**Token:** D6B2_MINIMAL_PRODUCTION_DELTA_DEFINED  
**Token:** D6B2_DELTA_SCOPE_CLEAN

## Allowlisted production producer files (Workstream B)

| Path | Change class |
|------|----------------|
| src/.../delivery_eligibility.py | NEW (D6B) |
| src/.../normalizer.py | MOD (remove stale→BLOCKED rewrite; apply eligibility) |
| src/.../errors.py | MOD (eligibility fields) |
| src/.../envelope_builder.py | MOD (distributable gated by eligibility) |
| src/.../producer_d5.py | MOD (preview/live gate) |
| src/.../pipeline.py | MOD (no customer text when not distributable) |
| src/.../site002_adapter.py | MOD (same) |
| constants.py | UNCHANGED threshold 93600 |

## Explicitly excluded

- Workstream A ledger / n8n nodes
- retries / concurrency
- activation lifecycle
- unattended monitor→Client Ops
- Data Table schema
- threshold tuning
