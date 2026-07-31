# GMAIL-INTAKE-FILTER-CONTRACT-v1

**Product:** i-SEO Sales Manager Bot  
**Status:** production-observed (Phase 3C.2)  
**PII:** no addresses, domains, filter IDs, or label IDs in this document

## Production intake boundary

Operational.dev Gmail Fetch uses **`labelIds` = production incoming parent label** (human name class: `LEADS_ISEO` parent).  
Do **not** broaden the n8n query to Trash, INBOX-all, or unlabeled mail.

## Expected Gmail filters (mailbox side)

| Match | Add labels | Forbidden actions |
|-------|------------|-------------------|
| Website-form sender (`from`) | incoming parent (+ optional IMPORTANT) | Trash/delete, skip-inbox without label, forward |
| Other approved lead senders | incoming parent | same |

Filters must **not** add PROCESSED or ERROR — those are n8n-owned after Telegram success / error policy.

## Label family

| Role | Shape (name class) | Owner |
|------|--------------------|-------|
| Incoming (intake) | parent `LEADS_ISEO` | Gmail filter on delivery; removed by n8n after Telegram success |
| Processed | nested child under same family | n8n only after Telegram success |
| Error | separate error label | n8n error path; preserve incoming until policy allows |

## Phase 3C.2 audit facts

- Filters enumerated: **2**; Trash actions: **0**; both add OPS incoming.
- Historical Trash of some form mail is **not** explained by Gmail filters (external/manual SAFE UNKNOWN).
- n8n must not be weakened to read Trash.

## Operator discipline

- Do not manually Trash unlabeled website-form mail before Operational poll.
- Do not create broad subject-keyword filters (`заявка` / `форма`) without charter.
- After filter changes: verify a fresh test remains non-Trash with incoming parent until processed.
