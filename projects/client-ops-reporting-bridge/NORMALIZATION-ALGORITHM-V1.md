# Normalization Algorithm v1

**Status:** DESIGN ONLY / PHASE 0B  
**Executable implementation:** NOT AUTHORIZED  
**Pseudocode / numbered logic only**

---

## 1. Purpose

Define a deterministic normalization algorithm that converts SITE post-1C monitor artifacts into a trustworthy `mars.client_ops.report` v1 result (or a fail-closed BLOCKED / security-rejected outcome).

Generic rules apply to the shared contract; SITE-002 field names are adapter specifics.

---

## 2. Policy constants (Phase 1 freeze)

| Constant | Value | Meaning |
|----------|-------|---------|
| `STALE_AFTER_SECONDS` | `93600` | 26 hours |
| `MAX_FUTURE_SKEW_SECONDS` | `300` | 5 minutes |
| Freshness clock | `age_seconds = floor(now_utc − observed_at)` | **Do not** use `generated_at` as observation freshness |
| Conflict outcome | BLOCKED / `SOURCE_ARTIFACT_CONFLICT` / `REVIEW_SOURCE_ARTIFACTS` | Never silent OK/ATTENTION |

---

## 3. Deterministic order (required)

1. Locate required artifacts.
2. Validate required set.
3. Parse each JSON independently.
4. Validate required source fields.
5. Establish `observed_at`.
6. Calculate `age_seconds`.
7. Apply stale rule.
8. Read monitor classification.
9. Read changed-summary metrics.
10. Read run-summary execution metadata.
11. Compare logically related fields.
12. Detect source artifact conflict.
13. Determine `source_status`.
14. Determine `site_status` (`run.normalized_status`).
15. Assign `summary_code`.
16. Assign `reason_codes`.
17. Derive `action`.
18. Construct envelope.
19. Validate envelope security fields.
20. Return normalized result.

---

## 4. Pseudocode

```text
FUNCTION normalize(run_dir, now_utc, site_config) -> Result

  artifacts = locate_required(run_dir,
    ["monitor-classification.json", "changed-summary.json", "run-summary.json"])

  IF any missing:
    RETURN blocked(SOURCE_ARTIFACT_MISSING, REVIEW_SOURCE_ARTIFACTS,
                   reasons=["REQUIRED_ARTIFACT_MISSING", missing_names...])

  FOR each artifact:
    IF not parse_json_utf8:
      RETURN blocked(SOURCE_ARTIFACT_MALFORMED, REVIEW_SOURCE_ARTIFACTS,
                     reasons=["JSON_PARSE_FAILED", artifact_name])

  IF required source fields missing for any authority role:
    RETURN blocked(SOURCE_ARTIFACT_MISSING, REVIEW_SOURCE_ARTIFACTS,
                   reasons=["REQUIRED_FIELD_MISSING", field_path...])
    # NEVER coerce missing numeric metrics to 0

  observed_at = establish_observed_at(run_summary, monitor_classification)
  IF observed_at invalid / unparseable:
    RETURN blocked(SOURCE_TIME_INVALID, REVIEW_SOURCE_TIME,
                   reasons=["OBSERVED_AT_UNPARSEABLE"])

  IF observed_at > now_utc + 300s:
    RETURN blocked(SOURCE_TIME_INVALID, REVIEW_SOURCE_TIME,
                   reasons=["OBSERVED_AT_IN_FUTURE"])

  age_seconds = floor_seconds(now_utc - observed_at)
  IF age_seconds < 0:  # residual clock anomaly
    RETURN blocked(SOURCE_TIME_INVALID, REVIEW_SOURCE_TIME,
                   reasons=["CLOCK_SKEW_NEGATIVE_AGE"])

  IF age_seconds > 93600:
    RETURN blocked(SOURCE_REPORT_STALE, REVIEW_SCHEDULER_AND_ARTIFACTS,
                   reasons=["SOURCE_STALE"], stale=true,
                   metrics=if_trustworthy_else_omit)

  classification = read_monitor_classification()
  metrics = read_changed_summary_metrics()  # fail if any required metric absent
  execution = read_run_summary_execution()

  IF metrics contain negative counts:
    RETURN blocked(SOURCE_ARTIFACT_CONFLICT, REVIEW_SOURCE_ARTIFACTS,
                   reasons=["NEGATIVE_METRIC"])

  IF baseline/current/delta internally inconsistent:
    RETURN blocked(SOURCE_ARTIFACT_CONFLICT, REVIEW_SOURCE_ARTIFACTS,
                   reasons=["METRIC_DELTA_INCONSISTENT"])

  IF classification vs onboarding_needed_count conflict:
    RETURN blocked(SOURCE_ARTIFACT_CONFLICT, REVIEW_SOURCE_ARTIFACTS,
                   reasons=["ONBOARDING_COUNT_CONFLICT"])

  IF classification vs run_summary.classification unresolved contradiction:
    RETURN blocked(SOURCE_ARTIFACT_CONFLICT, REVIEW_SOURCE_ARTIFACTS,
                   reasons=["CLASSIFICATION_MISMATCH",
                            "RUN_SUMMARY_VS_MONITOR_CLASSIFICATION"])
    # DO NOT prefer ONBOARDING_REQUIRED or NO_ACTION_REQUIRED silently

  IF unsupported source vocabulary:
    RETURN blocked(SOURCE_SCHEMA_UNSUPPORTED, REVIEW_SCHEMA_COMPATIBILITY,
                   reasons=["UNSUPPORTED_SOURCE_VOCABULARY"])

  IF execution indicates monitor failure OR classification FAILURE_REVIEW_REQUIRED:
    RETURN failed(SOURCE_EXECUTION_FAILED, REVIEW_SOURCE_FAILURE, ...)

  IF classification ONBOARDING_REQUIRED AND metrics consistent:
    RETURN attention(ONBOARDING_REQUIRED, REVIEW_ONBOARDING, ...)

  IF classification HYGIENE_REVIEW_REQUIRED AND metrics consistent:
    RETURN attention(HYGIENE_REVIEW_REQUIRED, REVIEW_HYGIENE, ...)

  IF classification NO_ACTION_REQUIRED AND metrics consistent:
    RETURN ok(NO_ACTION_REQUIRED, NONE, ...)

  RETURN blocked(SOURCE_ARTIFACT_CONFLICT, REVIEW_SOURCE_ARTIFACTS,
                 reasons=["UNRESOLVED_NORMALIZATION"])
```

After a successful logical Result is built, always run **security validation**. If security fails:

- Do **not** publish distributable envelope.
- Processing result: distribution BLOCKED with `summary_code = ENVELOPE_SECURITY_REJECTED`.
- Do not send Telegram.

---

## 5. Establish `observed_at`

**Priority (SITE-002 adapter design):**

1. Explicit completion timestamp from `run-summary.json` when present and parseable (`finished_at` or documented equivalent).
2. Else capture/completion timestamp from `monitor-classification.json` when present.
3. Else fail closed (`SOURCE_TIME_INVALID`) — do not invent from directory mtime alone for authoritative `observed_at` in Phase 1 design.

`generated_at` is set later by exporter completion time and is **not** the freshness basis.

---

## 6. Freeze rules (condition → outcome)

| Condition | site_status | summary_code | action.code |
|-----------|-------------|--------------|-------------|
| Missing required artifact | BLOCKED | `SOURCE_ARTIFACT_MISSING` | `REVIEW_SOURCE_ARTIFACTS` |
| Malformed JSON | BLOCKED | `SOURCE_ARTIFACT_MALFORMED` | `REVIEW_SOURCE_ARTIFACTS` |
| Missing baseline count | BLOCKED | `SOURCE_ARTIFACT_MISSING` | `REVIEW_SOURCE_ARTIFACTS` |
| Missing current count | BLOCKED | `SOURCE_ARTIFACT_MISSING` | `REVIEW_SOURCE_ARTIFACTS` |
| Negative counts | BLOCKED | `SOURCE_ARTIFACT_CONFLICT` | `REVIEW_SOURCE_ARTIFACTS` |
| Inconsistent delta (baseline/current/added/removed) | BLOCKED | `SOURCE_ARTIFACT_CONFLICT` | `REVIEW_SOURCE_ARTIFACTS` |
| Monitor execution failure evidenced | FAILED | `SOURCE_EXECUTION_FAILED` | `REVIEW_SOURCE_FAILURE` |
| Explicit `FAILURE_REVIEW_REQUIRED` | FAILED | `SOURCE_EXECUTION_FAILED` | `REVIEW_SOURCE_FAILURE` |
| `ONBOARDING_REQUIRED` + consistent | ATTENTION | `ONBOARDING_REQUIRED` | `REVIEW_ONBOARDING` |
| `HYGIENE_REVIEW_REQUIRED` + consistent | ATTENTION | `HYGIENE_REVIEW_REQUIRED` | `REVIEW_HYGIENE` |
| `NO_ACTION_REQUIRED` + consistent | OK | `NO_ACTION_REQUIRED` | `NONE` |
| Stale (`age_seconds > 93600`) | BLOCKED | `SOURCE_REPORT_STALE` | `REVIEW_SCHEDULER_AND_ARTIFACTS` |
| Future `observed_at` beyond skew | BLOCKED | `SOURCE_TIME_INVALID` | `REVIEW_SOURCE_TIME` |
| Other clock-invalid | BLOCKED | `SOURCE_TIME_INVALID` | `REVIEW_SOURCE_TIME` |
| Unsupported source vocabulary / schema | BLOCKED | `SOURCE_SCHEMA_UNSUPPORTED` | `REVIEW_SCHEMA_COMPATIBILITY` |
| Conflicting classifications | BLOCKED | `SOURCE_ARTIFACT_CONFLICT` | `REVIEW_SOURCE_ARTIFACTS` |
| Classification vs onboarding count conflict | BLOCKED | `SOURCE_ARTIFACT_CONFLICT` | `REVIEW_SOURCE_ARTIFACTS` |
| Unknown page types that break trust | BLOCKED | `SOURCE_ARTIFACT_CONFLICT` | `REVIEW_SOURCE_ARTIFACTS` |
| Source field absent (vs explicit zero) | BLOCKED | `SOURCE_ARTIFACT_MISSING` | `REVIEW_SOURCE_ARTIFACTS` |
| Envelope security validation fail | (no publish) | `ENVELOPE_SECURITY_REJECTED` | `REVIEW_SOURCE_ARTIFACTS` |

**Explicit zero** is valid when the source field is present and equals `0`. **Absent** fields must not become zero.

---

## 7. Metric consistency checks (SITE-002)

Let:

- `B = baseline_count`
- `C = current_count`
- `A = added_urls`
- `R = removed_urls`

Require when all present:

- `B, C, A, R` are integers ≥ 0
- `C == B + A - R` (logical delta identity for this monitor model)

If identity fails → `SOURCE_ARTIFACT_CONFLICT`.

Onboarding consistency (when classification claims onboarding):

- If `classification == ONBOARDING_REQUIRED` and `onboarding_needed_count == 0` → conflict.
- If `classification == NO_ACTION_REQUIRED` and `onboarding_needed_count > 0` → conflict (also typically conflicts with monitor-classification primacy vs run-summary).

---

## 8. Summary codes (frozen set + security extension)

### Site / source summary codes

- `NO_ACTION_REQUIRED`
- `ONBOARDING_REQUIRED`
- `HYGIENE_REVIEW_REQUIRED`
- `SOURCE_EXECUTION_FAILED`
- `SOURCE_REPORT_STALE`
- `SOURCE_ARTIFACT_MISSING`
- `SOURCE_ARTIFACT_MALFORMED`
- `SOURCE_ARTIFACT_CONFLICT`
- `SOURCE_SCHEMA_UNSUPPORTED`
- `SOURCE_TIME_INVALID`

### Distribution security extension

- `ENVELOPE_SECURITY_REJECTED`

**Note:** `ENVELOPE_SECURITY_REJECTED` is a **distribution/processing** summary code. It must not be presented as a verified site OK/ATTENTION/FAILED claim. It belongs to the Phase 0B extension list for publication gates and is consistent with fail-closed security rules in the report contract.

---

## 9. Action codes (minimum)

- `NONE`
- `REVIEW_ONBOARDING`
- `REVIEW_HYGIENE`
- `REVIEW_SOURCE_FAILURE`
- `REVIEW_SCHEDULER_AND_ARTIFACTS`
- `REVIEW_SOURCE_ARTIFACTS`
- `REVIEW_SCHEMA_COMPATIBILITY`
- `REVIEW_SOURCE_TIME`

`action.required = true` when action.code ≠ `NONE`.

---

## 10. Reason codes (deterministic machine identifiers)

Minimum catalog (non-exhaustive; implementations may add documented codes without changing meaning of these):

| reason_code | When |
|-------------|------|
| `REQUIRED_ARTIFACT_MISSING` | Required file absent |
| `JSON_PARSE_FAILED` | Malformed JSON |
| `REQUIRED_FIELD_MISSING` | Required field absent |
| `NEGATIVE_METRIC` | Count < 0 |
| `METRIC_DELTA_INCONSISTENT` | baseline/current/delta identity fails |
| `CLASSIFICATION_MISMATCH` | Classification authorities disagree |
| `RUN_SUMMARY_VS_MONITOR_CLASSIFICATION` | Specific mismatch class |
| `ONBOARDING_COUNT_CONFLICT` | Classification vs onboarding count |
| `SOURCE_STALE` | age > 93600 |
| `OBSERVED_AT_IN_FUTURE` | beyond skew |
| `OBSERVED_AT_UNPARSEABLE` | bad timestamp |
| `CLOCK_SKEW_NEGATIVE_AGE` | negative age anomaly |
| `UNSUPPORTED_SOURCE_VOCABULARY` | unknown classification token |
| `MONITOR_EXECUTION_FAILED` | exit/failure evidence |
| `UNKNOWN_PAGE_TYPE` | page type breaks trust policy |
| `EXPLICIT_ZERO_OK` | (informational; normally unused in BLOCKED paths) |
| `SECRET_MARKER_DETECTED` | security gate |
| `ABSOLUTE_PATH_DETECTED` | security gate |
| `RAW_LOG_DETECTED` | security gate |
| `SECURITY_FLAGS_INVALID` | redacted/contains_secrets invalid |

`reason_codes` must be sorted ascending when used in `event_id` canonical identity.

---

## 11. Precedence reminder

Exact order remains:

1. Completeness and freshness validation  
2. `monitor-classification.json`  
3. `changed-summary.json` metrics  
4. `run-summary.json` execution metadata  
5. `run.log` evidence/debug only  

Unresolved contradiction among required sources → BLOCKED / `SOURCE_ARTIFACT_CONFLICT` / `REVIEW_SOURCE_ARTIFACTS`.
