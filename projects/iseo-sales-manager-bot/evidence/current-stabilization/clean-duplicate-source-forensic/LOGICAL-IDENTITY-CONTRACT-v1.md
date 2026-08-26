# LOGICAL-IDENTITY-CONTRACT-v1

**Sources:** live Operational.dev Classify Duplicate + Append CLEAN mappings; `implementation/DEDUP-IMPLEMENTATION-SPEC-v1.md`

## Intended identities

| Role | Field / key | Source |
|------|-------------|--------|
| **SOURCE_EVENT_ID** | Gmail message id | Gmail poll → parser `gmail_message_id` → CLEAN `source_message_id` |
| DEDUP primary key | `dedup_key` = `gmail_message_id:{id}` | Classify Duplicate |
| **LOGICAL_LEAD_ID** | `lead_id` ≈ `lead_` + gmail_message_id | parser / merge (deterministic per source event) |
| RAW row identity | RAW sheet row + gmail_message_id | Ops RAW append path |
| Contact business keys | phone / email / site (normalized) | DEDUP secondary; `repeat` / `possible` — **may** create new CLEAN for true business repeats |

## Contract (ingest)

For a single **SOURCE_EVENT_ID**:

1. Exactly one logical CLEAN lead (`lead_id`).
2. Retries/replays may **upsert** that row and refresh DEDUP `last_seen_at`.
3. Must **not** append a second CLEAN row with the same `lead_id` / same Gmail message id.

For a **distinct** SOURCE_EVENT_ID:

- Must create a distinct `lead_id` (not false-suppressed by site-only `possible`).

## Allowed exceptions (business)

- Same phone/email → `duplicate_status=repeat` → **new** CLEAN lead is intentional (business repeat), not a same-message bug.
- Site-only → `possible` → do not suppress new lead.

## Not invented

No new identity model; patch aligns live Sheets nodes with existing DEDUP spec §5 (reprocess → update CLEAN, do not append).
