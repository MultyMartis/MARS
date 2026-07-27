# ACTIVATION-COMMAND-CONTRACT

**Token:** `D6C_ACTIVATION_COMMAND_CONTRACT_DEFINED` · `D6C_ACTIVATION_IDEMPOTENCY_DEFINED`

No customer payload. No webhook. Sanitized outputs: attempted, changed, active_after, version_id, timestamp_ms, error_class.

Unexpected already-active unknown workflow is not treated as authorized activation success.
