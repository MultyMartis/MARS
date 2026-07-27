# PHASE-1B-D6C — Controlled Activation Lifecycle Contract

## Status

Offline contract designed and implemented. Production apply **not** authorized.

`READY_FOR_D6C_CONTROLLED_PRODUCTION_APPLY_CHARTER`

## Model

`HYBRID_C1_TO_C3_BOUNDED` — near-term C1 precedent; bounded C3 lifecycle target.

## Baselines

- Workstream A: `12e4c6ad1f4199458b6f091d084f33ca5f8a965d`
- Workstream B: `94d06c05ea79eb22780588d91064006c3edf2a05`
- Order: A → B → C → E → D

## Implementation

See `evidence/phase-1b-d6c-controlled-activation-lifecycle-contract/` and:

- `n8n/runners/lib/client-ops-activation-lifecycle.mjs`
- `n8n/runners/lib/client-ops-lifecycle-lock.mjs`
- `n8n/runners/lib/client-ops-lifecycle-offline-transport.mjs`
- `n8n/harness/d6c-activation-lifecycle-harness.mjs`

## Defaults

max_requests=1 · max_retries=0 · max_concurrency=1 · max_activation_changes=2 · required_initial_workflow_active=false

## Explicit non-goals

- No Workstream E retry policy
- No Workstream D unattended integration
- No production activation in D6C
- No A/B semantic changes

## Next

Phase 1B-D6C2 — Controlled Activation Lifecycle Production Apply and Synthetic Dry-Window Verification (separate charter).
