# Severity Model

**Status:** FROZEN DOCUMENTATION SEMANTICS / PHASE 0A

---

## 1. Frozen site statuses

| Status | Meaning |
|--------|---------|
| **OK** | Payload valid; artifact set complete; artifact fresh; source/monitor completed successfully; facts internally consistent; operator action not required. |
| **ATTENTION** | Monitor completed successfully; facts trustworthy; review / onboarding / hygiene / other operator action required; **not** an execution failure. |
| **FAILED** | Source process or monitor actually failed; failure supported by source evidence (non-zero execution failure, sitemap fetch failure, parse failure, explicit source import failure, etc.). |
| **BLOCKED** | System cannot determine a trustworthy site state; no factual OK/ATTENTION/FAILED determination can be made safely. |

---

## 2. BLOCKED coverage

BLOCKED must cover at least:

- stale report
- missing baseline
- malformed JSON
- incomplete required artifact set
- contradictory artifacts (unresolved)
- unsupported or unknown schema major version
- impossible source verification
- missing required fields
- exporter unable to establish a trustworthy observation

**Important distinction:** BLOCKED means **unable to verify site state**, not that the site itself failed.

---

## 3. Status separation

| Family | Values | Mutates site_status? |
|--------|--------|----------------------|
| **site_status** (`run.normalized_status`) | OK, ATTENTION, FAILED, BLOCKED | — (authoritative site claim) |
| **delivery_status** | NOT_ATTEMPTED, SENT, RETRYING, FAILED | **No** |
| **ai_status** | DISABLED, NOT_REQUESTED, SUCCESS, FAILED | **No** |

Rules:

- Telegram delivery failure must not alter `site_status`.
- AI failure must not alter `site_status`.
- AI failure must not block SIMPLE delivery.
- `site_status` is determined **before** delivery and AI handling.
- Minimal SITE/exporter payload must not pretend Telegram or AI already happened.

---

## 4. Deterministic decision order

1. Validate envelope/schema identity and major version support.
2. Validate required artifact completeness and JSON parse.
3. Validate freshness (`stale=true` → BLOCKED).
4. Apply artifact precedence and conflict rules ([ARTIFACT-AUTHORITY-AND-PRECEDENCE.md](ARTIFACT-AUTHORITY-AND-PRECEDENCE.md)).
5. If monitor/source execution failure evidenced → FAILED.
6. Else if trustworthy facts require operator action → ATTENTION.
7. Else if trustworthy facts require no action → OK.
8. If any step prevents trustworthy determination → BLOCKED.

Never skip to OK/ATTENTION when trust is broken.

---

## 5. Rule tables

### 5.1 Site status derivation (summary)

| Condition | site_status |
|-----------|-------------|
| Schema major unsupported | BLOCKED |
| Required artifacts missing/malformed | BLOCKED |
| Unresolved logical contradiction among authorities | BLOCKED |
| Stale | BLOCKED |
| Monitor/source execution failure evidenced | FAILED |
| Trustworthy + action required (onboarding/hygiene/review) | ATTENTION |
| Trustworthy + no action required | OK |

### 5.2 Delivery / AI isolation

| Event | site_status | delivery_status | ai_status |
|-------|-------------|-----------------|-----------|
| Telegram send failure | unchanged | FAILED (or RETRYING) | unchanged |
| AI timeout/failure | unchanged | unchanged | FAILED |
| AI disabled | unchanged | unchanged | DISABLED |
| No AI requested | unchanged | unchanged | NOT_REQUESTED |

---

## 6. Examples

| Scenario | site_status | Notes |
|----------|-------------|-------|
| Complete fresh artifacts; classification NO_ACTION_REQUIRED; metrics consistent | OK | Action not required |
| Complete fresh artifacts; ONBOARDING_REQUIRED; metrics show onboarding needs | ATTENTION | Not a failure |
| Monitor exit non-zero / sitemap fetch failed with evidence | FAILED | Site/process failure evidenced |
| `monitor-classification` vs `run-summary.classification` unresolved conflict | BLOCKED | Cannot verify |
| Missing `changed-summary.json` | BLOCKED | Incomplete set |
| `stale=true` | BLOCKED | Freshness fail |
| Telegram down after ATTENTION normalized | ATTENTION | delivery_status FAILED only |
| AI empty response | ATTENTION (example) | Fallback to SIMPLE; ai_status FAILED |

---

## 7. Source status vs normalized status

- `run.source_status` preserves source vocabulary (e.g. `ONBOARDING_REQUIRED`, `NO_ACTION_REQUIRED`, `SOURCE_ARTIFACT_CONFLICT`).
- `run.normalized_status` uses only OK / ATTENTION / FAILED / BLOCKED.
- Mapping from source vocabulary to normalized status is deterministic and owned by shared severity + precedence rules.

Illustrative mapping (non-exhaustive):

| Source signal | Typical normalized |
|---------------|--------------------|
| `NO_ACTION_REQUIRED` + consistent metrics | OK |
| `ONBOARDING_REQUIRED` / `HYGIENE_REVIEW_REQUIRED` + consistent | ATTENTION |
| `FAILURE_REVIEW_REQUIRED` or evidenced execution failure | FAILED |
| `SOURCE_ARTIFACT_CONFLICT` / trust failure | BLOCKED |
