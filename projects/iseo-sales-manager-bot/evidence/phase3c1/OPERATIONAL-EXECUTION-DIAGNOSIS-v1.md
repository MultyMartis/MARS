# OPERATIONAL EXECUTION DIAGNOSIS v1

## Cutover reference

Cutover UTC: `2026-07-30T21:57:07.956Z`

## Summary

| Metric | Value |
|--------|-------|
| OPS executions sampled after cutover (API limit) | **100** |
| PROD executions after cutover | **0** |
| Average interval | **~30s** |
| Sampled empty polls (Gmail items=0) | **20** |
| Sampled nonzero Gmail fetches | **0** |
| Sampled lead Telegram sends | **0** |
| Sampled Gmail node errors | **0** |

## Matrix (sanitized excerpt)

Recent pattern: `trigger` → Schedule ran → Gmail Fetch Leads ran → **0 items** → success → no Parse/RAW/CLEAN/Telegram/runtime update (pre-observability-patch).

Post-observability-patch example execution `8665`: Schedule → Gmail → Intake Gate → Switch Intake Route → Update Runtime → Apply CONFIG (empty poll path).

## Failure stage for operator incident

**gmail_read_zero_items** (eligible count 0) — not a Schedule Trigger outage, not a credential hard-fail in sampled successes.
