# CURRENT-ACTIVATION-FLOW

**Token:** `D6C_CURRENT_ACTIVATION_FLOW_MAPPED`

## Tooling

- Allowlisted client: `n8n/runners/lib/client-ops-n8n-activation-client.mjs`
- Endpoints: `POST /api/v1/workflows/tkM4H0G0gM3q9Foi/activate|deactivate`
- Host pin: `n8n.ai-metacode.com`
- Confirmation phrases required (D5/D6A2/D6C phrases)

## Historical traces

| Phase | Trace | Activation changes |
|-------|-------|--------------------|
| D5R2 | inactive → POST → HTTP 404 before intake | 0 |
| D5R2A | inactive → activate → readiness → 1 POST 202 → Telegram → deactivate → active=false | 2 |
| D6A2 | inactive → activate → synthetic verify → deactivate | 2 |
| D6B2 | freshness apply; no activation | 0 |

## Gaps closed by D6C

Preflight freshness/dedupe gates, readiness-before-window, bounded request window, lifecycle lock, unconditional deactivate, recontainment verification, emergency containment distinct from delivery retry, charter consumption, sanitized evidence.
