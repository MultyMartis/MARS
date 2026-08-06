# SECURITY-REVIEW

## Controls verified

- Admin launch requires authenticated OpenCart session
- Route permission `access`/`modify` for `tool/mars_1c_exchange`
- POST only; `user_token` CSRF
- No public import URL; no GET launch
- Admin UI does not expose shell commands, credentials, or secret filesystem paths
- Dispatcher uses webhook token from local secrets; not committed
- Evidence sanitized (no admin cookies, API keys, chat IDs, personal names)

## Kill switch / retries

- Workflow accepted event under production gates (kill switch ENABLED, intake FIRST_SEEN)
- Automatic retries remain disabled; max concurrency 1 for import and report

## Gates

- `D6G_SECRET_BOUNDARY_PRESERVED` — PASS
- `D6G_ADMIN_AND_RUNTIME_SECURITY_PASS` — PASS
