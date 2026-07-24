# Event Fingerprint Contract — D1

**Algorithm:** `canonical_json_v1` (sorted-key JSON.stringify of fingerprint document)

**Why not SHA-256:** this n8n installation disallows `require('crypto')` inside Code nodes (proven by execution 3410).

## Fields

schema_name, schema_version, event_type, site_id, domain, normalized_status, summary_code, source_status, action_code, action_required, metrics.{baseline_count,current_count,added_urls,removed_urls,onboarding_needed_count}

## Excluded

secrets, tokens, paths, raw webhook payload, telegram fields, headers, delivery timestamps
