# OFFLINE-IMPLEMENTATION

## Added

- `src/client_ops_reporting_bridge/delivery_eligibility.py`
- `tests/test_delivery_eligibility_d6b.py`
- `n8n/harness/d6b-freshness-semantics-harness.py`
- Phase doc + evidence pack under `PHASE-1B-D6B-…` / `evidence/phase-1b-d6b-…`

## Modified

- `normalizer.py` — remove stale→BLOCKED rewrite; apply eligibility after factual map
- `errors.py` — ProcessResult fields: `delivery_eligibility`, `freshness_threshold_seconds`, `freshness_reason`
- `envelope_builder.py` — `distributable` only when `FRESH_AND_ELIGIBLE` + non-BLOCKED
- `producer_d5.py` — preview + live gate use delivery_eligibility; stale verdict `SOURCE_VALID_BUT_STALE_REVIEW_REQUIRED`
- `pipeline.py` / `site002_adapter.py` — no customer `simple_text` when not distributable
- `fixtures/fixture-blocked-stale/*` — expected semantics updated
- Related unit tests for stale/BLOCKED distributable expectations

## Unchanged (explicit)

- Workstream A ledger PENDING/SENT/FAILED
- `STALE_AFTER_SECONDS=93600`
- `max_retries=0`, `DEFAULT_CONCURRENCY=1`
- Production n8n workflow / Data Table
- SITE-002 runtime / scheduler
