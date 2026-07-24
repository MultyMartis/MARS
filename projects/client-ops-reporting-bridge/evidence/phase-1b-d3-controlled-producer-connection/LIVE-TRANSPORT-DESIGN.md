# LIVE-TRANSPORT-DESIGN

## D2 vs D3

| Area | D2 | D3 | Verification |
|------|----|----|--------------|
| Transport modes | disabled / fixture / mock | + gated `http` | BlockedHttpTransport remains; LiveHttpTransport only via D3 auth |
| Network on import | none | none | module import safe |
| Dry-run | offline only | offline only | `dry_run` raises before dial |
| Real HTTPS | forbidden | urllib + default SSL context | no `verify=False` |
| Redirects | n/a | rejected / not followed | `_NoRedirectHandler` |
| Auth header | representation only | real `X-MARS-Client-Ops-Token` | value redacted in evidence |
| Retries | 0 | 0 | max_retries must be 0 |
| Concurrency | 1 | 1 | sequential guard |
| Endpoint | ignored profile shapes only | allowlisted host+route | `n8n.ai-metacode.com` + `/webhook/` |
| CLI | push-webhook blocked | dedicated `producer-d3-controlled-live` | push-webhook remains D2-blocked |

## Implementation

- `producer_http.py` — allowlist + LiveHttpTransport
- `producer_d3_gates.py` — phrases, budget, charter state
- `producer_d3.py` — controlled pipeline
- Orchestrator Node runner activates/deactivates and correlates; Python owns the POST
