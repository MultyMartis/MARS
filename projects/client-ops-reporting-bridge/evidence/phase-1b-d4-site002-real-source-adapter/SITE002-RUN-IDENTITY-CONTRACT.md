# SITE-002 Run Identity Contract

- Prefer run-summary.run_id (scheduled folder name).
- observed_at from source — not adapter wall-clock.
- Same artifact => same event_id; different run => different event_id.
- D2 UUID namespace unchanged.
- source_contract_fingerprint is diagnostic only.

Proven: run `2026-07-07_d4-ok-sanitized-01` => `803e01fa-e0b7-561a-9b70-3c2b988d0109`; different run `2026-07-08_d4-ok-sanitized-02` => `ac8d830c-cfc4-5a94-856c-c6a1c5633d78`.
