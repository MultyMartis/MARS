# RECONCILIATION-AUTHORITY

**Token:** `D6E_RECONCILIATION_AUTHORITY_DEFINED`

Authority order (strongest → weakest):

1. `deterministic_event_identity`
2. `durable_data_table_row`
3. `durable_delivery_state`
4. `known_telegram_delivery_evidence`
5. `n8n_execution_evidence`
6. `observed_http_result`
7. `local_client_transport_result`

Rules:

- Durable SENT proof is never overridden by weaker HTTP/client evidence.
- Telegram SUCCESS with PENDING fails closed (no resend).
- Ambiguous transport never implies `SAFE_TO_RETRY` without authoritative no-intake proof.
- Execution evidence strengthens reconciliation but cannot authorize blind POST.

Planner (`client-ops-reconciliation-planner.mjs`) emits GET-only next steps; `production_mutation_authorized=false`.
