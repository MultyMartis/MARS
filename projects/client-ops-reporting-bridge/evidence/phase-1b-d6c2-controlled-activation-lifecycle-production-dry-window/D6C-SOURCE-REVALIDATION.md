# D6C Source Revalidation

**Token:** `D6C2_ACCEPTED_D6C_SOURCE_REVALIDATED`

## Components present
- `n8n/runners/lib/client-ops-activation-lifecycle.mjs` (dry-lifecycle extension for planned_requests=0)
- `n8n/runners/lib/client-ops-lifecycle-lock.mjs`
- `n8n/runners/lib/client-ops-lifecycle-offline-transport.mjs`
- `n8n/runners/lib/client-ops-lifecycle-production-transport.mjs` (new D6C2 production binding)
- `n8n/runners/lib/client-ops-n8n-activation-client.mjs` (D6C confirm phrases)
- `n8n/harness/d6c-activation-lifecycle-harness.mjs`
- `n8n/runners/run-client-ops-d6c2-activation-lifecycle-production-dry-window.mjs`

## Checks
- `node --check` on lifecycle/lock/transports/runner: PASS
- D6C harness: **30/30 PASS** (`D6C_OFFLINE_LIFECYCLE_HARNESS_PASS`) before and after production dry run
- Material drift vs accepted D6C: **none** (dry-lifecycle preflight path is additive; source delivery path unchanged)
