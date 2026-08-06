# HEALTH SEMANTIC SEPARATION v1

## Principle

`/health` and `/status` answer **different questions** and must not share probe results as interchangeable truth.

## `/health` (on-demand)

- Bounded read-only probes at command time
- Gmail probe: **live connectivity / credential / fetch smoke** — not scheduled poll ledger
- Pass/fail lines only; no production statistics epoch
- May succeed while scheduled poll CONFIG keys were stale (pre-repair observed)

## `/status` (scheduled truth + CONFIG mirror)

- Gmail poll line: **`last_poll_success_at` + `gmail_poll_heartbeat`** from Operational scheduled runs
- Production lead line: **`last_production_processed_*`** keys
- AI / reminders / reporting from CONFIG allowlist
- Must never treat `/health` Gmail probe timestamp as poll heartbeat

## Repair impact

- Health Code node patched for clarity/consistency (no conflation with poll heartbeat)
- Status Code node patched to use authoritative matrix (see `STATUS-DATA-SOURCE-MATRIX-v1.md`)

## Operator rule

If `/health` Gmail OK but `/status` poll stale → investigate **scheduled poll heartbeat writes**, not health probe alone.
