# Current-State Gap Matrix — Phase 1B-D0

**Status:** CURRENT snapshot after GET-only reconfirmation
**Workflow:** `MARS Client Ops Bridge — bzpm.ru` (`tkM4H0G0gM3q9Foi`) — inactive

| Capability | Current state | Runtime evidence | Production requirement | Gap | Blocking stage |
|------------|---------------|------------------|------------------------|-----|----------------|
| Producer | Offline exporter only (`validate-only` / `build-envelope`); no network POST | Phase 1A tests; `push-webhook` absent | Authenticated producer of `mars.client_ops.report` | No runtime producer | Before runtime connection |
| Envelope generation | Implemented offline from fixtures | Phase 1A unittest; synthetic fixtures | Live sanitized envelope from SITE-002 artifacts | Live discovery / sanitization path not runtime-connected | Before live-source E2E |
| Endpoint config | Local ignored secrets file exists; route not committed | `secrets.local.env` key present (value not inspected in docs) | Ignored local profile + committed non-secret site profile | Endpoint profile incomplete | Before manual runtime POST |
| Authentication | Native Header Auth bound | B1/B2; credential `WKHmPaw6QBp7WnzP`; secret value absent from API list | Same + rotation procedure | Rotation procedure incomplete | Before production activation |
| Validation | Schema/security gates in workflow Code nodes | B2 POST matrix | Same + durable evidence | None for sandbox | Before production: retain policy |
| Security rejection | Proven | B2 rejects | Same | None for sandbox | — |
| Response | Deterministic 202/4xx/5xx contract | B2 | Same | None for sandbox | — |
| Telegram | Pattern B applied; inactive; one synthetic delivery | C0S/C1; chat `499423375`; cred `2bIC5376l7ElXb4B` | Controlled delivery + failure policy | Failure retention / replay incomplete | Before unattended operation |
| Dedupe | `DEDUPE_DEFERRED_SANDBOX` / `DEFERRED_SANDBOX` | B2 duplicate accepted twice; no Data Table/Store nodes | Durable per-`event_id` authority | Durable store missing | **Before runtime producer connection** |
| Retry | Design-only (`FAILURE-RETRY-AND-ROLLBACK-V1.md`) | Not implemented | Bounded retry + same `event_id` | No producer/n8n retry policy implemented | Before scheduler |
| Failed-event retention | None | — | Dead-letter / failed delivery record | Missing | Before unattended |
| Observability | Sanitized milestone evidence packs; n8n execution metadata | B/B1/B2/C*/C1 packs | Producer run ID + event ID + execution ID + Telegram status | Runtime producer evidence path missing | Before runtime E2E |
| Scheduling | Not connected for Client Ops Bridge | Monitor has separate Windows task (SITE-002) | Clean-runtime scheduled producer later | No Client Ops schedule | After manual E2E |
| Clean runtime | Not created for Client Ops | Universal MARS rule known; SITE-002 monitor historically from `X:\AI MARS` | Runtime from clean checkout under Storage | Client Ops clean checkout absent | Before scheduler |
| Secrets | Local ignored webhook auth secret | Key name only documented | Rotation + no Git leakage | Rotation runbook incomplete | Before production |
| Rollback | Workflow rollback docs exist; producer rollback N/A | C1 rollback readiness | Snapshot + deactivate + producer stop | Producer/dedupe rollback units unproven | Before each mutation wave |
| Production activation | Forbidden; workflow inactive | GET `active=false` | Explicit HITL + all gates | All production gates open | Final gate |

## Production disconnection (CURRENT / PROVEN)

- SITE-002 monitor: not connected
- Local/exporter runtime: not connected
- Scheduler (Client Ops): not connected
- 1C import: not connected
- Durable dedupe store: not present
- Unattended delivery: not enabled
- Production activation: not authorized
