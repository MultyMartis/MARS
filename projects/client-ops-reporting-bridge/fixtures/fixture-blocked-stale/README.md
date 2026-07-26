# fixture-blocked-stale

Synthetic stale observation (`age_seconds > STALE_AFTER_SECONDS=93600`).

**Phase 1B-D6B semantics:** factual classification `NO_ACTION_REQUIRED` maps to
`normalized_status=OK` with `delivery_eligibility=STALE_REVIEW_REQUIRED`.
Age alone must not rewrite status to `BLOCKED` / `SOURCE_REPORT_STALE`.

Customer-facing `simple_text` is not emitted for stale-eligible artifacts.
Identity envelope may still be built for deterministic `event_id`.
