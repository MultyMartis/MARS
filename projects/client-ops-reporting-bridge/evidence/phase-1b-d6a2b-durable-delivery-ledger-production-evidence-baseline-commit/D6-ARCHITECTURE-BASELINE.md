# D6 Architecture Baseline

**Priority (accepted):** `A → B → C → E → D`

| Workstream | Name | Decision retained |
|------------|------|-------------------|
| A | Durable post-Telegram delivery ledger | `D6_SENT_LEDGER_REQUIRED_BEFORE_UNATTENDED=YES` |
| B | Source status vs delivery freshness | `D6_FRESHNESS_SEPARATION_REQUIRED_BEFORE_UNATTENDED=YES` |
| C | Controlled activation lifecycle | `D6_ACTIVATION_MODEL_RECOMMENDATION=HYBRID` |
| E | Retry / concurrency policy | `D6_MAX_SAFE_CONCURRENCY_TODAY=1` |
| D | Unattended monitor → Client Ops | `D6_UNATTENDED_ARCHITECTURE_RECOMMENDATION=D2` (last) |

Retained readiness flags:

- `CLIENT_OPS_UNATTENDED_PRODUCTION_READY=NO`
- `CLIENT_OPS_AUTOMATIC_SITE002_CONNECTION_AUTHORIZED=NO`

Source pack: `evidence/phase-1b-d6-post-first-delivery-architecture-decision/`
Phase doc: `PHASE-1B-D6-CLIENT-OPS-POST-FIRST-DELIVERY-ARCHITECTURE-DECISION-CHARTER.md`
