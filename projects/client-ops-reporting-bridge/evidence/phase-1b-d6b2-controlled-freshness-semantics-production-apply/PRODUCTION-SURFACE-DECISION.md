# PRODUCTION-SURFACE-DECISION

**Token:** D6B2_PRODUCTION_SURFACE_PRODUCER_ONLY

## Rationale

Accepted D6B semantics live in the Python producer/adapter path:

- delivery_eligibility.py, normalizer.py, producer_d5.py, envelope/pipeline/adapter

n8n Workstream A ledger (20-node workflow @ dc8746bf-...) already separates intake from Telegram finalization. Freshness/eligibility is evaluated **before** webhook POST by the producer gate.

D6B2 did **not** copy producer files to a separate runtime and did **not** mutate producer bytes (producer_bytes_mutated_during_d6b2=0). D6B2 hash-locked and declared the already-present effective producer path.

## Call chain

SITE-002 artifacts → site002_adapter / normalizer → delivery_eligibility → producer_d5 preview/live gate → (only if FRESH_AND_ELIGIBLE) webhook → n8n ledger.

## Decision

- **n8n workflow content mutations:** 0
- **Data Table schema mutations:** 0
- Production apply surface = monorepo producer package used via PYTHONPATH=projects/client-ops-reporting-bridge/src
