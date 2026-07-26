# EVENT-IDENTITY-FRESHNESS-INDEPENDENCE

**Token:** `D6B_EVENT_IDENTITY_FRESHNESS_INDEPENDENT`  
**Token:** `D6B_NEW_SOURCE_RUN_REQUIRED_FOR_NEW_EVENT`  
**Token:** `D6B_DETERMINISTIC_FRESHNESS_CLOCK_TESTS`

## Rules

- `event_id` material: site, event_type, run_id, observed_at, normalized_status, summary_code, metrics, reason_codes, action_code  
- Evaluation clock / age / `delivery_eligibility` / `stale` **do not** enter identity  
- Freshness reason codes are **not** appended to `reason_codes` (would poison identity)

## Proofs

- B11: same artifact evaluated fresh then stale → same `event_id`  
- B12: new `run_id` / `observed_at` → different `event_id`  
- Injected `now_utc` only affects eligibility, not identity document
