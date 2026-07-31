# GMAIL FILTER REAL MESSAGE PARITY v1

## Production filter (Operational.dev)

- Operation: `getAll`
- Bound: `labelIds` = incoming production label (same token as Sales-Manager-v2)
- `returnAll`: false, `limit`: 10
- Filter hash parity vs v2: **equal** (`true`)

## Real message vs filter

| Predicate | Candidate post-cutover mail | Production filter |
|-----------|----------------------------|-------------------|
| Incoming label | **absent** | **required** → excludes |
| INBOX | absent (in Trash) | not required by node, but label gate already excludes |
| UNREAD | absent | not required |
| PROCESSED/ERROR | absent | N/A |

## Minimal fix assessment

Do **not** broaden n8n filter to Trash/INBOX-all. Production source boundary remains the incoming label.

Required operator-side action: ensure website form mail receives the incoming label **and** is not trashed before poll.
