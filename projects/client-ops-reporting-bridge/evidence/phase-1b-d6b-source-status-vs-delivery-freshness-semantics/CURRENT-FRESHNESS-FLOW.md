# CURRENT-FRESHNESS-FLOW (pre-D6B conflation)

**Token:** `D6B_CURRENT_FRESHNESS_FLOW_MAPPED`

## Trace (before repair)

```
source authority (artifacts)
  → extract classification / metrics / run fields
  → observed_at / age_seconds
  → [CONFLATION] if age > 93600 → _blocked(SOURCE_REPORT_STALE)
       normalized_status=BLOCKED   ← factual axis overwritten
  → else map classification → OK/ATTENTION/FAILED
  → envelope freshness.{age_seconds,stale}
  → D5 preview/live gate treats BLOCKED (incl. stale) as not approved
```

## Conflation point

`normalizer.py` early return when `age_seconds > STALE_AFTER_SECONDS`:

- `summary_code=SOURCE_REPORT_STALE`
- `normalized_status=BLOCKED`
- `stale=True`
- `distributable=False`

## Other touchpoints

| Area | File | Role |
|------|------|------|
| Adapter | `site002_adapter.py` | passes ProcessResult freshness |
| Envelope | `envelope_builder.py` | `freshness.stale` boolean |
| Identity | `event_identity.py` | uses normalized_status/summary/reasons (age must not enter) |
| D5 preview | `producer_d5.py` | previously treated all BLOCKED alike |
| D5 live | `producer_d5.py` | blocked POST on `normalized_status==BLOCKED` |
| Orchestrator (D5R2A) | evidence `_live-orchestrator.mjs` | separate operator age check (workaround) |
| Contract docs | `REPORT-CONTRACT-V1.md` / `SEVERITY-MODEL.md` | historical stale→BLOCKED freeze |

## Post-D6B intended flow

```
authority validation first
  → factual map → source_status / normalized_status
  → apply_delivery_eligibility(age)
       FRESH_AND_ELIGIBLE | STALE_REVIEW_REQUIRED | NOT_SAFE_TO_SEND
  → preview / live gate checks delivery_eligibility
  → Workstream A ledger only after authorized POST
```
