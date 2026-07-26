# D5-LIVE-GATES

Exact phrases required (no other phrase enables live HTTP):

1. `ENABLE ONE MANUAL SITE002 REAL SOURCE D5 BZPM`
2. `ACTIVATE CLIENT OPS MANUAL REAL SOURCE D5 BZPM`
3. `SEND ONE MANUAL SITE002 REAL SOURCE EVENT D5 BZPM`
4. `DEACTIVATE CLIENT OPS MANUAL REAL SOURCE D5 BZPM`
5. `EMERGENCY DEACTIVATE CLIENT OPS MANUAL REAL SOURCE D5 BZPM`

## Also required for live

- `--apply`
- environment = `manual_real_source_controlled`
- concurrency = 1
- max_retries = 0
- automatic_retry = false
- producer marker `mars-client-ops-site002-real-source-d5`
- ignored profile + auth secret present
- explicit approved source path under SITE-002 post-1c root
- source preview approved
- event_id unseen in Data Table
- D3 charter remains consumed
- D4 live remains blocked
- one-time charter unused (`real_http_requests < 1`)

## Part B status

Preview **not** approved → live gates **not** exercised. No activation, no POST, no deactivation cycle.
