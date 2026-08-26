# POST-FIX-DUPLICATE-CHECK-v1

| Check | Result |
|-------|--------|
| Live Ops CLEAN write | `appendOrUpdate` / `lead_id` |
| Live Ops DEDUP write | `appendOrUpdate` / `dedup_key` |
| Same-event additional CLEAN | 0 |
| Distinct-event false dedupe | 0 |
| current duplicate-producing paths | **0** (ingest append-always path removed) |
| Historical PRODUCTION_REAL clusters | still present (not deleted) |
| TMP cleandup workflows left | 0 |

Historical inventory clusters remain until a separate reconciliation wave.
