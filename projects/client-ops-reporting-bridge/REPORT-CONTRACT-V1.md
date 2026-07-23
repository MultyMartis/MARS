# Report Contract v1 — `mars.client_ops.report`

**Status:** FROZEN DOCUMENTATION SEMANTICS / PHASE 0A  
**Schema name:** `mars.client_ops.report`  
**Schema version:** `1.0`  
**Validator implementation:** NOT IMPLEMENTED (no executable JSON Schema required for Phase 0A)

---

## 1. Identity and versioning

| Field | Rule |
|-------|------|
| `schema_name` | Must equal `mars.client_ops.report` for v1 |
| `schema_version` | `major.minor` string (MVP: `1.0`) |
| Unsupported major | Consumers **must** treat as **BLOCKED** (cannot trust normalization) |
| Compatible minor | Additive optional fields only; required MVP fields remain stable |
| Ownership | Shared contract owns semantics; producer fills producer-owned fields; consumer may add delivery/AI extensions downstream |

---

## 2. Minimal required envelope (MVP v1)

```json
{
  "schema_name": "mars.client_ops.report",
  "schema_version": "1.0",
  "event_id": "uuid",
  "event_type": "site.post_1c_monitor",
  "generated_at": "ISO-8601",
  "observed_at": "ISO-8601",
  "environment": "production",
  "site": {
    "site_id": "SITE-002",
    "site_name": "ЗПМ",
    "domain": "bzpm.ru"
  },
  "producer": {
    "name": "ocpilot.site-002.post-1c-exporter",
    "version": "1.0"
  },
  "run": {
    "run_id": "2026-07-23_12-30-03",
    "source_status": "ONBOARDING_REQUIRED",
    "normalized_status": "ATTENTION",
    "summary_code": "ONBOARDING_REQUIRED",
    "reason_codes": [
      "CATEGORY_PLP_ADDED",
      "BASELINE_DELTA_NONZERO"
    ]
  },
  "action": {
    "required": true,
    "code": "REVIEW_ONBOARDING",
    "text": "Проверить новые ветки каталога."
  },
  "metrics": {
    "baseline_count": 1737,
    "current_count": 1817,
    "added_urls": 80,
    "removed_urls": 0,
    "onboarding_needed_count": 4
  },
  "freshness": {
    "age_seconds": 120,
    "stale": false
  },
  "security": {
    "classification": "internal",
    "contains_secrets": false,
    "redacted": true
  }
}
```

This example is **sanitized documentation**. It does **not** prove an exporter produced it.

---

## 3. Field table

| Path | JSON type | Required | Allowed / constraints | Owner | Semantic meaning | Validation | Missing / invalid handling |
|------|-----------|----------|------------------------|-------|------------------|------------|----------------------------|
| `schema_name` | string | yes | exactly `mars.client_ops.report` | contract / producer | Schema identity | Exact match | Reject → BLOCKED |
| `schema_version` | string | yes | `^\d+\.\d+$`; MVP `1.0` | contract / producer | Version | Parse major.minor; reject unsupported major | BLOCKED |
| `event_id` | string | yes | UUID string (stable for normalized event) | producer | Deduplication key | Non-empty UUID-like; stable across retries of same observation | Missing → BLOCKED; regenerate only for distinct observation |
| `event_type` | string | yes | Documented namespaced value; MVP `site.post_1c_monitor` | producer | Event class | Allowlist for MVP | Unknown → BLOCKED for MVP consumers |
| `generated_at` | string | yes | ISO-8601 datetime | producer | Exporter generation time | Parseable datetime | Missing/invalid → BLOCKED |
| `observed_at` | string | yes | ISO-8601 datetime | producer | Source observation completion time | Parseable; should be ≤ generated_at | Missing/invalid → BLOCKED |
| `environment` | string | yes | Explicit; MVP `production` (also future `sandbox` / `staging` if documented) | producer | Execution environment | Non-empty allowlist | Missing → BLOCKED |
| `site.site_id` | string | yes | Stable site id (e.g. `SITE-002`) | producer | Site identity | Non-empty | Missing → BLOCKED |
| `site.site_name` | string | yes | Human site label | producer | Display name | Non-empty; no secrets | Missing → BLOCKED |
| `site.domain` | string | yes | Public domain hostname | producer | Domain | Hostname without credentials | Missing → BLOCKED |
| `producer.name` | string | yes | Exporter identity string | producer | Who generated envelope | Non-empty | Missing → BLOCKED |
| `producer.version` | string | yes | Producer version | producer | Producer revision | Non-empty | Missing → BLOCKED |
| `run.run_id` | string | yes | Source run folder / run id | producer | Correlate to source run | Non-empty; **no absolute Storage path** | Missing → BLOCKED |
| `run.source_status` | string | yes | Source vocabulary preserved (e.g. `ONBOARDING_REQUIRED`, `NO_ACTION_REQUIRED`, `HYGIENE_REVIEW_REQUIRED`, `FAILURE_REVIEW_REQUIRED`, or conflict codes) | producer | Raw/source classification vocabulary | Non-empty | Missing → BLOCKED |
| `run.normalized_status` | string | yes | `OK` \| `ATTENTION` \| `FAILED` \| `BLOCKED` | producer via severity rules | Site status for consumers | Exact enum | Invalid → BLOCKED |
| `run.summary_code` | string | yes | Deterministic machine code | producer | Primary summary code | Non-empty uppercase snake or documented set | Missing → BLOCKED |
| `run.reason_codes` | array of string | yes | Deterministic machine codes; may be empty array only when status OK and no reasons | producer | Supporting machine reasons | Array; elements non-empty strings | Missing field → BLOCKED; do not invent |
| `action.required` | boolean | yes | true/false | producer | Whether operator action required | Boolean | Missing → BLOCKED |
| `action.code` | string | yes | Machine action code | producer | Action class | Non-empty when required=true; for OK may use `NONE` | Missing when required → BLOCKED |
| `action.text` | string | yes | Human-readable action | producer | Operator-facing text | No secrets, no raw paths, no stack traces | Missing → BLOCKED |
| `metrics.baseline_count` | integer | yes | ≥ 0 integer | producer | Baseline URL count | Integer; **must not silent-default to 0 if source missing** | Missing → BLOCKED |
| `metrics.current_count` | integer | yes | ≥ 0 integer | producer | Current observed URL count | Integer; no silent zero default | Missing → BLOCKED |
| `metrics.added_urls` | integer | yes | ≥ 0 integer | producer | Added URL count | Integer; no silent zero default | Missing → BLOCKED |
| `metrics.removed_urls` | integer | yes | ≥ 0 integer | producer | Removed URL count | Integer; no silent zero default | Missing → BLOCKED |
| `metrics.onboarding_needed_count` | integer | yes | ≥ 0 integer | producer | Onboarding needs count | Integer; no silent zero default | Missing → BLOCKED |
| `freshness.age_seconds` | integer | yes | ≥ 0 | producer | Age of observation vs generation/consume policy clock | Deterministic computation | Missing → BLOCKED |
| `freshness.stale` | boolean | yes | true/false | producer | Staleness flag | If `true` → site_status must be BLOCKED | Missing → BLOCKED |
| `security.classification` | string | yes | MVP `internal` | producer | Distribution class | Allowlist | Missing → BLOCKED |
| `security.contains_secrets` | boolean | yes | Must be `false` for distributable envelope | producer | Secret presence claim | Must be false | true or missing → reject / BLOCKED |
| `security.redacted` | boolean | yes | Must be `true` for distributable envelope | producer | Redaction claim | Must be true | false or missing → reject / BLOCKED |

---

## 4. Timestamp semantics

| Field | Meaning |
|-------|---------|
| `generated_at` | When the **exporter** produced the envelope |
| `observed_at` | When the **source observation** completed (monitor finish / captured_at authority) |

Consumers must not treat `generated_at` as the sitemap observation time.

---

## 5. Deduplication (`event_id`)

- `event_id` identifies one **normalized observation event**.
- Retries of delivery for the same observation **must reuse** the same `event_id`.
- A new observation (new run / new trustworthy export) gets a new `event_id`.
- Exact UUID algorithm is Phase 1 design detail; semantic requirement is **stability for dedupe**.

---

## 6. Status and reason rules

- `run.normalized_status` uses frozen site vocabulary: OK / ATTENTION / FAILED / BLOCKED.
- `run.source_status` preserves source vocabulary and must not be overwritten by Telegram/AI outcomes.
- `reason_codes` are deterministic machine codes (no free-form prose).
- `action.text` is human-readable and must not carry secrets or raw paths.
- Metric counts are integers and **must not silently default to zero** when source values are missing.

---

## 7. Freshness and security

| Rule | Effect |
|------|--------|
| Freshness computed deterministically | Documented clock basis in Phase 1 design (exporter generation vs observed_at) |
| `stale=true` | Forces **BLOCKED** |
| `contains_secrets=false` | Required for distributable envelope |
| `redacted=true` | Required for distributable envelope |
| Absolute artifact paths | **Forbidden** in envelope |
| Raw logs / stack traces / credentials | **Forbidden** |

---

## 8. Sanitized BLOCKED example — source artifact conflict

```json
{
  "schema_name": "mars.client_ops.report",
  "schema_version": "1.0",
  "event_id": "00000000-0000-4000-8000-000000000001",
  "event_type": "site.post_1c_monitor",
  "generated_at": "2026-07-23T12:35:00+07:00",
  "observed_at": "2026-07-23T12:32:21+07:00",
  "environment": "production",
  "site": {
    "site_id": "SITE-002",
    "site_name": "ЗПМ",
    "domain": "bzpm.ru"
  },
  "producer": {
    "name": "ocpilot.site-002.post-1c-exporter",
    "version": "1.0"
  },
  "run": {
    "run_id": "2026-07-23_12-30-03",
    "source_status": "SOURCE_ARTIFACT_CONFLICT",
    "normalized_status": "BLOCKED",
    "summary_code": "SOURCE_ARTIFACT_CONFLICT",
    "reason_codes": [
      "CLASSIFICATION_MISMATCH",
      "RUN_SUMMARY_VS_MONITOR_CLASSIFICATION"
    ]
  },
  "action": {
    "required": true,
    "code": "REVIEW_SOURCE_ARTIFACTS",
    "text": "Состояние сайта не подтверждено: конфликт исходных артефактов. Проверить monitor-classification и run-summary."
  },
  "metrics": {
    "baseline_count": 1737,
    "current_count": 1817,
    "added_urls": 80,
    "removed_urls": 0,
    "onboarding_needed_count": 4
  },
  "freshness": {
    "age_seconds": 159,
    "stale": false
  },
  "security": {
    "classification": "internal",
    "contains_secrets": false,
    "redacted": true
  }
}
```

If metrics themselves cannot be trusted because required metric artifacts are missing/malformed, metric fields must not be fabricated; exporter should fail closed to BLOCKED without inventing counts.

---

## 9. Explicit deferred fields (not in MVP v1 required envelope)

Do **not** add to MVP v1 required envelope:

- ATLAS references
- MARS `project_id` (unless later separately chartered as necessary)
- Client routing hints
- Telegram chat IDs / bot data
- OpenRouter / AI provider fields
- Hub Gateway-specific fields
- Absolute artifact paths
- Raw logs / stack traces
- Credentials / secret references for runtime
- Universal advertising / lead / order / WooCommerce metrics
- Client self-service / dashboard / automatic remediation fields

### Optional extension guidance (non-frozen)

Downstream consumers may attach extension objects such as `delivery` or `ai` **after** attempts, without changing producer ownership of site facts. Extension schemas are **out of Phase 0A freeze**.

---

## 10. Ownership summary

| Concern | Owner |
|---------|-------|
| Envelope schema semantics | Shared contract (this document) |
| Filling producer fields | Future exporter |
| Validation / dedupe / delivery | Future n8n consumer |
| Presentation | Telegram templates |
| Commentary | Optional AI (non-authoritative) |
