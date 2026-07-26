# Evidence Pack — Phase 1B-D6 Post-First-Delivery Architecture Decision

Design-only architecture decision after first verified SITE-002 real-source delivery.

## Contents

| File | Purpose |
|------|---------|
| `D6-CHARTER.json` | Charter metadata / mutation caps |
| `D6-DECISION.json` | Machine-readable decisions |
| `CURRENT-BASELINE.md` | Accepted + reconfirmed live/runtime baseline |
| `WORKSTREAM-A-DURABLE-SENT-LEDGER.md` | Workstream A analysis |
| `WORKSTREAM-B-FRESHNESS-SEMANTICS.md` | Workstream B analysis |
| `WORKSTREAM-C-ACTIVATION-LIFECYCLE.md` | Workstream C analysis |
| `WORKSTREAM-D-UNATTENDED-ARCHITECTURE.md` | Workstream D analysis |
| `WORKSTREAM-E-RETRY-CONCURRENCY.md` | Workstream E analysis |
| `DEPENDENCY-GRAPH.md` | Directed prerequisites A–E |
| `FAILURE-MODE-MATRIX.md` | Consolidated failure modes |
| `MATURITY-MAP.md` | Maturity scores |
| `MINIMUM-PRODUCTION-SAFE-MODEL.md` | Minimum before unattended claim |
| `SECURITY-ARCHITECTURE.md` | Security review |
| `RECOMMENDED-PHASE-ORDER.md` | Ordered roadmap D6-1… |

## Live method

GET-only n8n / Data Table inspection. Zero mutations.

## Key outcomes

- Priority hypothesis **CONFIRMED**: A → B → C → E → D
- Next implementation: **Phase 1B-D6A** (durable SENT ledger) — not started
- `CLIENT_OPS_UNATTENDED_PRODUCTION_READY=NO`
- `CLIENT_OPS_AUTOMATIC_SITE002_CONNECTION_AUTHORIZED=NO`
