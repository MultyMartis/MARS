# CURRENT-DATA-TABLE-SCHEMA

**Table:** MARS Client Ops Dedupe — bzpm.ru (`H6VYhwz7RXZCBMmu`)
**Column count:** 15 (GET-only reconfirmed)

| Column | Current Purpose | Written At | Mutable? | Required Future Role |
|--------|-----------------|------------|----------|----------------------|
| event_id | Deterministic event identity / lookup key | Claim insert | No (identity) | Identity |
| event_fingerprint | Canonical fingerprint for duplicate/conflict | Claim insert | No | Dedupe |
| site_id | Site scope | Claim insert | No | Scope |
| schema_name | Envelope schema | Claim insert | No | Intake snapshot |
| schema_version | Envelope version | Claim insert | No | Intake snapshot |
| event_type | Event type | Claim insert | No | Intake snapshot |
| event_status | normalized_status at claim (e.g. ATTENTION) | Claim insert | **Must not change on delivery finalize** | Factual event status |
| intake_state | FIRST_SEEN at claim | Claim insert | **Immutable during delivery finalize** | Intake axis |
| delivery_state | Delivery ledger (currently stuck PENDING) | Claim insert = PENDING; **terminal update missing live** | Yes (PENDING→SENT/FAILED) | Terminal delivery ledger |
| first_seen_at | Claim timestamp | Claim insert | No | Intake audit |
| last_seen_at | Claim timestamp (reserved) | Claim insert | Not used for delivery finalize in D6A | Reserved |
| duplicate_count | Reserved counter | Claim insert 0 | Not updated in D6A | Reserved |
| conflict_count | Reserved counter | Claim insert 0 | Not updated in D6A | Reserved |
| redaction_version | Policy marker | Claim insert | No | Provenance |
| sandbox_marker | Sandbox/provenance marker | Claim insert | No | Provenance |

**Authority:** Live GET column list + D1 `DEDUP-ROW-SCHEMA.json` + compose `columnSchema()`.
