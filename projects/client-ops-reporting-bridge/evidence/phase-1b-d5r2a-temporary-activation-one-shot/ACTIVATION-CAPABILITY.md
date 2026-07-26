# ACTIVATION-CAPABILITY — D5R2A

## Verdict

`D5R2A_TEMPORARY_ACTIVATION_CAPABILITY_CONFIRMED`

## Proof

- Established client: `n8n/runners/lib/client-ops-n8n-activation-client.mjs`
- Allowlisted workflow ID only: `tkM4H0G0gM3q9Foi`
- Activate: `POST /api/v1/workflows/{id}/activate`
- Deactivate: `POST /api/v1/workflows/{id}/deactivate`
- Confirm phrases (tooling): D5 activate/deactivate (content mutation not required)
- Pre-state GET: `active=false`, `nodes=17`, `webhook_id_present=true`, `webhook_path_present=true`
- Unrelated workflow dependency: **false**
- Node/content/credential edit required for activation: **false**
- Production webhook expected available after activate: **true** (n8n production webhook semantics)

## Caps

- activation_changes max: 2 (inactive→active→inactive)
- workflow content mutations: 0
