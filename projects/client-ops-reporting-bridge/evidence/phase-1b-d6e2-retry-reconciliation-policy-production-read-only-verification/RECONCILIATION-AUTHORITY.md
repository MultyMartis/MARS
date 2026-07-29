# RECONCILIATION-AUTHORITY

**Token:** `D6E2_RECONCILIATION_AUTHORITY_VERIFIED`

```json
{
  "order": [
    "deterministic_event_identity",
    "durable_data_table_row",
    "durable_delivery_state",
    "known_telegram_delivery_evidence",
    "n8n_execution_evidence",
    "observed_http_result",
    "local_client_transport_result"
  ],
  "rules": [
    "Durable SENT proof is never overridden by weaker HTTP/client evidence",
    "Telegram SUCCESS with PENDING fails closed (no resend)",
    "Ambiguous transport never implies SAFE_TO_RETRY without authoritative no-intake proof",
    "Execution evidence strengthens reconciliation but cannot authorize blind POST"
  ]
}
```

Applied against real evidence: durable Data Table delivery_state remains authoritative;
Telegram and n8n execution are supporting; neither authorizes blind POST.
