# Security Review

- Webhook auth secret stored only in non-Git `mars_1c_wrapper.local.php`
- Secret not written to terminal.json, admin HTML, or evidence JSON values
- HTTP dispatch-run / dispatch-recover / watchdog gateway require `run_token`
- No public unauthenticated report trigger
- Admin manual import remains session + user_token + modify permission
- Evidence records only secret presence / sha256 prefix where used

Gates: `D6G1_SECRET_BOUNDARY_PRESERVED`, `D6G1_PRODUCTION_SECURITY_PASS`
