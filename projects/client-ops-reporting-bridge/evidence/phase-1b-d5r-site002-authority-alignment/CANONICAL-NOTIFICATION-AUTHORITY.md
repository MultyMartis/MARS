# CANONICAL-NOTIFICATION-AUTHORITY

## Decision

`CANONICAL_SITE002_NOTIFICATION_AUTHORITY_CONFIRMED`

## Precedence contract (evidence-backed)

1. **Completeness / parseability** of the three required JSON authorities.
2. **`monitor-classification.json`** — canonical **action classification** (`classification`, `next_action`, onboarding/hygiene counts).
3. **`changed-summary.json`** — canonical **delta metrics** (baseline/current/added/removed).
4. **`run-summary.json`** — canonical **run execution metadata** (`run_id`, `status`, `exit_code`, duration, timestamps, artifact path map).
5. **`run-summary.json.classification` / `.next_action`** — intended **duplicate** of monitor-classification values written by Python; must equal monitor-classification; if unequal → unresolved emitter defect → Client Ops `SOURCE_ARTIFACT_CONFLICT` / `BLOCKED` (no silent reconcile).
6. Logs (`run.log`, stderr) — debug evidence only; never override JSON authorities.

## Client Ops notification derivation (after emitter consistency)

| monitor-classification | Client Ops status | Notes |
|------------------------|-------------------|-------|
| `NO_ACTION_REQUIRED` | `OK` | only if metrics/coherence gates pass and not stale for delivery policy |
| `ONBOARDING_REQUIRED` | `ATTENTION` | |
| `HYGIENE_REVIEW_REQUIRED` | `ATTENTION` | |
| `FAILURE_REVIEW_REQUIRED` or nonzero exit | `FAILED` | |
| mismatch / malformed / incomplete | `BLOCKED` | |

Until SITE-002 runner repair lands, fresh conflicted runs remain non-distributable.
