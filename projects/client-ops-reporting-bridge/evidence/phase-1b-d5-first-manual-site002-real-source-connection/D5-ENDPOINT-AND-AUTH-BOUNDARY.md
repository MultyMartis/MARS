# D5-ENDPOINT-AND-AUTH-BOUNDARY

## Transport

- `create_d5_live_transport` reuses D3 HTTPS allowlist / TLS posture
- TLS verification required; redirects rejected; no `verify=False`
- Max real HTTP requests: **1**
- Auth header name (evidence only): `X-MARS-Client-Ops-Token` — value never recorded in Git
- Full webhook URL: never recorded in Git

## Auth / secret boundary

| Allowed in Git evidence | Forbidden in Git evidence |
|-------------------------|---------------------------|
| Header name present=true / redacted | Token / secret values |
| Workflow/table IDs already public in prior packs | Absolute Storage paths |
| Sanitized source labels | Webhook URLs |
| event_id UUIDs from adapter dry-run | Credential files / profiles |

## Scope

- SITE-002 / bzpm.ru only under D5 marker
- Pattern B manual source only
- No generic live mode; ordinary dry-run stays offline (`NETWORK_DISPATCH_NOT_AUTHORIZED_D5` without gates)

## Part B

No endpoint called. Network calls = 0.
