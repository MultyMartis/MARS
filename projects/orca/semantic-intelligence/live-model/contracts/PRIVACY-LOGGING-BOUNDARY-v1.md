# Privacy and Logging Boundary v1

**Status:** `IMPLEMENTED — Wave 3.1`

## Fields sent to external model

| Allowed | Excluded |
|---------|----------|
| phrase_id, raw_query (redacted), normalized_query (redacted), region | Client PII beyond redaction |
| business scope summary | Full manifest, unrelated projects |
| approved service registry (sanitized) | Secrets, API keys |
| taxonomy keys | Expected labels, gold authority |
| commercial policy version | Deterministic/P0-I/adjudicator outcomes |

## PII handling

Search phrases may contain accidental email, phone. `redactPii()` in adapter applies before API call.

## Raw model responses

Stored under `live-model/reports/<run-id>/raw-responses/` — local only, not committed by default.

## Retention

Operator-controlled; default recommendation: 30 days for evaluation runs, then purge raw responses.

## Secret handling

Credentials via environment only. Logs must never contain API keys or full Authorization headers.

## Operator approval boundary

Sending client-specific corpus to external model requires explicit operator authorization per project manifest.
