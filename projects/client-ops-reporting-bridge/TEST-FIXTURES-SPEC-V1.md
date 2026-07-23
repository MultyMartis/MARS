# Test Fixtures Specification v1

**Status:** DESIGN ONLY / PHASE 0B  
**Fixture files:** NOT CREATED as a runtime set in Phase 0B  
**Future locus:** `projects/client-ops-reporting-bridge/fixtures/`  
**Rule:** No raw production Storage artifact copies into Git

---

## 1. Purpose

Specify sanitized synthetic fixtures sufficient for L1–L3 acceptance without exposing production logs, paths as envelope content, or secrets.

Phase 0B delivers this **specification only** (not the binary/JSON fixture tree), unless separately chartered.

---

## 2. Future fixture locus

```text
projects/client-ops-reporting-bridge/fixtures/
  README.md
  manifest.json
  fixture-ok/
  fixture-attention-onboarding/
  ...
```

Each fixture directory should contain:

- `source/` — sanitized synthetic monitor JSON trio (+ optional companions)
- `expected/envelope.json` — expected normalized envelope
- `expected/event-identity.json` — canonical identity inputs
- `expected/simple.txt` — expected SIMPLE message
- `meta.md` — provenance and version notes

---

## 3. Global prohibitions

- No real production Storage copies.
- No real Telegram chat IDs / tokens.
- No absolute source paths inside expected envelopes.
- No raw `run.log` bodies from production.
- Baseline **1737** may appear only as **checkpoint wording** in synthetic metrics, not as “current live sitemap”.
- Observed **1817** may appear only as **latest inspected observation pattern** in synthetic conflict/onboarding fixtures, not as live state claim.

---

## 4. Required fixture cases

### fixture-ok

| Item | Spec |
|------|------|
| Source files | classification `NO_ACTION_REQUIRED`; metrics consistent (e.g. B=C, A=0, R=0, onboarding=0); run-summary classification matches; finished timestamp fresh |
| Sanitized values | Invented run_id; metrics may use small integers |
| Expected envelope | OK / `NO_ACTION_REQUIRED` / `NONE` |
| event identity | Stable for identical inputs |
| SIMPLE | `· OK` header; counts match |
| Provenance | Synthetic |

### fixture-attention-onboarding

| Item | Spec |
|------|------|
| Source | `ONBOARDING_REQUIRED`; onboarding_needed_count > 0; metrics consistent; run-summary classification matches monitor-classification |
| Expected | ATTENTION / `ONBOARDING_REQUIRED` / `REVIEW_ONBOARDING` |

### fixture-attention-hygiene

| Item | Spec |
|------|------|
| Source | `HYGIENE_REVIEW_REQUIRED`; consistent metrics; matching run-summary |
| Expected | ATTENTION / `HYGIENE_REVIEW_REQUIRED` / `REVIEW_HYGIENE` |

### fixture-failed-execution

| Item | Spec |
|------|------|
| Source | Non-zero failure evidence and/or `FAILURE_REVIEW_REQUIRED` |
| Expected | FAILED / `SOURCE_EXECUTION_FAILED` / `REVIEW_SOURCE_FAILURE` |

### fixture-blocked-stale

| Item | Spec |
|------|------|
| Source | Valid otherwise; `observed_at` older than 93600s relative to fixture `now` pin |
| Expected | BLOCKED / `SOURCE_REPORT_STALE` / `REVIEW_SCHEDULER_AND_ARTIFACTS` |
| Note | Fixture must pin `now` in meta for determinism |

### fixture-blocked-missing-artifact

| Item | Spec |
|------|------|
| Variants | Missing each of the three required JSON files |
| Expected | BLOCKED / `SOURCE_ARTIFACT_MISSING` |

### fixture-blocked-malformed-json

| Item | Spec |
|------|------|
| Variants | Truncated/invalid JSON per authority file |
| Expected | BLOCKED / `SOURCE_ARTIFACT_MALFORMED` |

### fixture-blocked-classification-conflict

| Item | Spec |
|------|------|
| Pattern | **Synthetic** derivation of known SITE-002 conflict class: monitor-classification `ONBOARDING_REQUIRED`; run-summary classification `NO_ACTION_REQUIRED`; added URLs `80`; onboarding needed `4` |
| Metrics | May use baseline `1737` / current `1817` as **synthetic checkpoint/observation numbers** matching documented pattern — **not** live claims |
| Expected | BLOCKED / `SOURCE_ARTIFACT_CONFLICT` / `REVIEW_SOURCE_ARTIFACTS` |
| Reasons | include `CLASSIFICATION_MISMATCH`, `RUN_SUMMARY_VS_MONITOR_CLASSIFICATION` |
| Prohibited | Copying raw Storage files from `2026-07-23_12-30-03` |

### fixture-blocked-metric-conflict

| Item | Spec |
|------|------|
| Source | baseline/current/added/removed break `C == B + A - R`, and/or negative counts |
| Expected | BLOCKED / `SOURCE_ARTIFACT_CONFLICT` |

### fixture-blocked-missing-baseline

| Item | Spec |
|------|------|
| Source | Omit `baseline_url_count` or `current_url_count` |
| Expected | BLOCKED / `SOURCE_ARTIFACT_MISSING` — **no silent zero** |

### fixture-blocked-unsupported-schema

| Item | Spec |
|------|------|
| Source/envelope | Unsupported schema major or unsupported source vocabulary |
| Expected | BLOCKED / `SOURCE_SCHEMA_UNSUPPORTED` |

### fixture-blocked-invalid-time

| Item | Spec |
|------|------|
| Source | `observed_at` > now + 300s, or unparseable timestamp |
| Expected | BLOCKED / `SOURCE_TIME_INVALID` / `REVIEW_SOURCE_TIME` |

### fixture-security-secret-detected

| Item | Spec |
|------|------|
| Source | Otherwise valid facts but action text contains absolute path / token marker, or security flags invalid |
| Expected | **No publication**; `ENVELOPE_SECURITY_REJECTED` |
| SIMPLE | Must not send rejected content |

### fixture-dedupe-repeat

| Item | Spec |
|------|------|
| Source | Identical to fixture-ok (or attention) processed twice |
| Expected | Second pass: same `event_id`; `DUPLICATE_ALREADY_SENT` after first SENT |

### fixture-delivery-retry

| Item | Spec |
|------|------|
| Source | Same envelope identity after simulated Telegram failure |
| Expected | Same `event_id`; `RETRY_ALLOWED` → eventual SENT without new site event |

---

## 5. Expected envelope rules

- Match `REPORT-CONTRACT-V1.md` required fields.
- `security.contains_secrets=false`, `security.redacted=true` for publishable fixtures.
- No absolute paths in `action.text`.

---

## 6. Expected event identity

- Per `EVENT-ID-AND-DEDUPE-V1.md`.
- Fixtures store canonical identity JSON used for hashing, not production UUIDs from live systems.

---

## 7. Expected SIMPLE message

- Per `TELEGRAM-SIMPLE-TEMPLATES.md`.
- Header status equals normalized status.
- Counts exact.
- Baseline wording: Baseline/Current/Added/Removed — never `Sitemap: 1737` as live-only.

---

## 8. Provenance and version rules

| Rule | Detail |
|------|--------|
| Provenance | Mark `synthetic` in meta |
| Update | Bump fixture version when algorithm changes expected outcomes |
| Conflict fixture | Cite Phase 0A pattern docs; do not claim live re-inspection |
| Git | Only sanitized fixtures may be committed in a future charter |

---

## 9. Phase 0B action statement

This task creates **the specification document only**. It does **not** create the `fixtures/` tree or copy Storage artefacts.
