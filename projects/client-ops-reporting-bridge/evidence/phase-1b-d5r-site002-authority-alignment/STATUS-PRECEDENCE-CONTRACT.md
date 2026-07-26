# STATUS-PRECEDENCE-CONTRACT

## Contract version

`site002-monitor-result-v1` — **clarified**, not bumped to v2.

Reason: intended semantics already required classification equality; D5R confirms the emitter violates that intent. Changing Client Ops to accept disagreement would be a material behavior change that papers over a bug. Fix the emitter; keep v1 fail-closed conflict rule.

## Separation of concerns

| Concern | Source | Client Ops field |
|---------|--------|------------------|
| Action classification | `monitor-classification.classification` (must equal run-summary.classification) | `run.source_status` / summary mapping |
| Run health / exit | `run-summary.status`, `exit_code` | failure path / FAILED |
| Delta metrics | `changed-summary` (+ corroborating counts on monitor/run) | `metrics.*` |
| Delivery eligibility / freshness | age vs `STALE_AFTER_SECONDS` | today folded into `normalized_status=BLOCKED`; **needs separate repair** |

## Explicit rules (current Client Ops — unchanged in D5R)

1. Prefer monitor-classification for classification extraction.
2. If run-summary.classification present and ≠ monitor → `SOURCE_ARTIFACT_CONFLICT` → `BLOCKED`.
3. Metric equation / onboarding count coherence checks remain.
4. Stale age → `SOURCE_REPORT_STALE` → `BLOCKED` (historical Phase 0A freeze; freshness semantics repair deferred).

## Historical vs repaired behavior

| Era | Behavior |
|-----|----------|
| D4/D5 historical | Conflict → BLOCKED (correct); root cause unexplained beyond contradiction |
| D5R current understanding | Same Client Ops behavior retained; root cause = runner overwrite bug; SITE-002 repair required before truthful live retry |
