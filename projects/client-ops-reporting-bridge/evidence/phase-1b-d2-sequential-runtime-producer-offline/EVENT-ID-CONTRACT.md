# Event ID Contract

Producer-authoritative UUID v5. Namespace `8f3c2a91-6b4e-4d7a-9c1f-2e5a8b0d4f67`.
Inputs: site_id, event_type, run_id, observed_at, normalized_status, summary_code, metrics{5}, reason_codes, action_code, schema_major.
Retries preserve event_id. Not the same as n8n D1 fingerprint.
