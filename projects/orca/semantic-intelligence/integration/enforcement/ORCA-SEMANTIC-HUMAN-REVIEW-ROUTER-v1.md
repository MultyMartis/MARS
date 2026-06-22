# ORCA Semantic Human Review Router v1

**Router ID:** `orca-semantic-human-review-router-v1`  
**Date:** 2026-06-22

---

## Purpose

Route phrases to human review while preserving original automated decision and full audit trace.

---

## Mandatory routing triggers

| Trigger | Route priority | Preserve |
|---------|----------------|----------|
| All `ABSTAIN` | P1 — required | `automated_decision`, `reason_code`, `ambiguity` |
| `risk.overall_risk` HIGH or CRITICAL | P1 | risk dimensions, evidence |
| Protected-strata conflicts (career/edu/DIY vs commercial signals) | P1 | opposing_evidence |
| Short-head ambiguity | P2 | short-head adjudication refs |
| Problem-query ambiguity | P2 | problem-query adjudication refs |
| Product/service conflict unresolved | P2 | product-vs-service adjudication |
| Model/rule disagreement | P1 | both decision traces |
| Random ACCEPT audit (sample rate TBD at implementation) | P3 | full record |
| Random REJECT audit (sample rate TBD) | P3 | full record |

---

## Output fields

```json
{
  "review": {
    "workflow_status": "PENDING_HUMAN",
    "route_reason": "ABSTAIN_MANDATORY",
    "route_priority": "P1",
    "automated_decision_preserved": "ABSTAIN",
    "automated_reason_code": "PROVIDER_DIY_CONFLICT",
    "review_queue_id": "...",
    "routed_at": "ISO-8601"
  }
}
```

---

## Prohibited behavior

- Human review must **not** silently overwrite automated decision without override audit entry
- Router must **not** promote ABSTAIN to ACCEPT without reviewer ID and timestamp
- Router must **not** use legacy `HOLD` label — use `ABSTAIN` + `PENDING_HUMAN`

---

## Integration pilot

Pilot must demonstrate at least one routed record per mandatory trigger category (synthetic or selected phrases).
