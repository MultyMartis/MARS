# AFFECTED-MESSAGE-ROUTING-FORENSIC-v1

**Phase:** 3C.2  
**Observed:** 2026-07-31  
**PII policy:** no bodies, addresses, domains, Gmail IDs, or label IDs

## Primary Phase 3C.1 incident candidate

| Field | Safe value |
|-------|------------|
| Received (UTC) | 2026-07-31T08:50:05Z |
| Sender class | automated_form_like |
| Sender domain hash | (hashed; matches filter-1 from-hash class) |
| Recipient role | production mailbox (address present) |
| Subject class | empty |
| System labels | IMPORTANT, TRASH, CATEGORY_PERSONAL |
| Custom labels | 0 |
| OPS incoming | absent |
| OPS PROCESSED | absent |
| OPS ERROR | absent |
| INBOX | absent |
| Ever in INBOX | SAFE UNKNOWN (not proven from current metadata) |
| Auto-forwarded | no evidence (no X-Forwarded headers observed on probe) |
| Gmail filter match (from) | **exact match** to filter #1 criteria hash class |
| External client move | SAFE UNKNOWN |

## Additional same-class candidates

| Received (UTC) | Trash | Incoming | Processed | Notes |
|----------------|-------|----------|-----------|-------|
| 2026-07-31T11:11:41Z | no | no (after finalize) | **yes** | finalized by Operational.dev after Phase 3C.2 OPS repair |
| 2026-07-30T23:48:41Z | yes | no | no | different sender class/hash; not filter-1 |
| 2026-07-28T19:14:23Z | yes | no | no | different sender class/hash |

## Interpretation

- Incident mail sits in Trash without OPS incoming/PROCESSED.
- Same sender class later delivered to INBOX, received OPS processing, and finalized with nested PROCESSED label.
- Do **not** restore or reprocess the Trash incident message in this phase.
