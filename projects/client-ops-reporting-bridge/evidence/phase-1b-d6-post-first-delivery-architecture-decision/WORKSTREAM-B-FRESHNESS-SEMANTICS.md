# WORKSTREAM B — Source Status vs Delivery Freshness Semantics

`D6_WORKSTREAM_B_ANALYZED`

## Current maturity

`PARTIALLY_PROVEN` / accepted open defect: `FRESHNESS_STATUS_SEMANTICS_REQUIRES_SEPARATE_REPAIR`

## Evidence already proven

1. Status mapping (factual source → Client Ops) exists and is used for D5R2A:
   - ONBOARDING_REQUIRED → ATTENTION
   - etc. (`site002_adapter_constants.STATUS_MAPPING`)
2. D5/D5R2A gates treat freshness as a **separate operator check** in orchestrator evidence (`delivery_eligibility` vs `source_status_factual`) and explicitly refuse to falsify source to BLOCKED solely for age in charter notes.
3. Core normalizer still conflates age into normalized status.

## Conflation point (code)

In `normalizer.py`, when `age_seconds > STALE_AFTER_SECONDS` (93600):

```text
return _blocked(
  summary_code="SOURCE_REPORT_STALE",
  ...
  normalized_status="BLOCKED",   # ← factual status axis overwritten
  stale=True,
  distributable=False,
)
```

Comment in `producer_d5.py` acknowledges “Authority/staleness BLOCKED” as a single gate.

**Effect:** a source that was factually ATTENTION/ONBOARDING_REQUIRED becomes Client Ops `BLOCKED` merely because the artifact aged out of delivery eligibility. That collapses two different truths.

## Target minimum model

| Axis | Vocabulary | Meaning |
|------|------------|---------|
| `source_status` / mapped `event_status` | OK / ATTENTION / FAILED / BLOCKED | Truth about source result / authority |
| `delivery_eligibility` | FRESH_AND_ELIGIBLE / STALE_REVIEW_REQUIRED / NOT_SAFE_TO_SEND | Whether notification may be sent **now** |

Smallest fit for current implementation:

- Keep factual mapping from monitor classification unchanged.
- Compute `stale` / eligibility from `observed_at` + threshold **without** rewriting mapped status to BLOCKED.
- Reserve `BLOCKED` for authority/schema/security conflicts (missing artifacts, unsupported classification, contradictory authority, security reject).

## Stale handling policy (design)

| Case | Action |
|------|--------|
| Stale + previously unseen event | Do **not** silently notify; mark `STALE_REVIEW_REQUIRED`; preserve factual status |
| Stale after already SENT | Ignore for delivery; keep ledger |
| Operator wants notify after stale | Require fresh source run (new artifacts) |
| Event identity | Remain deterministic for same source run content; **do not** mint new event_id solely due to age |
| New source run | New observed_at / content → new event_id as today |

## Places freshness can incorrectly mutate factual status

1. `normalizer.normalize` stale branch → `BLOCKED`
2. Downstream D5 live gate rejecting all `normalized_status == BLOCKED` (includes stale)
3. Any future unattended gate that equates “not eligible” with “source failed”

## Decision

`D6_FRESHNESS_SEPARATION_REQUIRED_BEFORE_UNATTENDED=YES`

Without separation, an aged ATTENTION condition may be mis-stored/mis-escalated as BLOCKED, poisoning operator semantics and any automatic eligibility logic.

## Upstream / downstream

- Upstream: none hard (orthogonal to A)
- Downstream: **D** (unattended eligibility), soft input to **E** (retry of stale artifacts forbidden)
