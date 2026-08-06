# READ-ONLY-INVARIANT

See machine-readable `READ-ONLY-INVARIANT.json`.

**Token:** `D6E2_READ_ONLY_INVARIANT_ARMED`

Before any external read, mutation probes (webhook POST, activate/deactivate, Data Table mutation, Telegram, retry execution, workflow PUT) were locally rejected by `client-ops-d6e2-readonly-transport.mjs`.

GET remain allowed only for allowlisted workflow / executions / Data Table paths.
