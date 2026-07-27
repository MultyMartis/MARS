# Security Review

- No raw secrets, tokens, Authorization headers, full webhook URLs, or customer payloads in evidence
- Activation/deactivation confirm phrases only (not credentials)
- Lock file contains owner_token locally under `local/` — not committed; evidence stores `owner_token_present` only
- Unattended mode: not enabled
