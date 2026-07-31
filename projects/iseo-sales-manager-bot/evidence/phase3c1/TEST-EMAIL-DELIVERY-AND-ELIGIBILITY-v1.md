# TEST EMAIL DELIVERY AND ELIGIBILITY v1

## Verdict

**Test email found in mailbox: YES** (bounded read-only probes).

## Evidence (no PII)

| Field | Result |
|-------|--------|
| Post-cutover automated-form-like messages | **2** unique timestamps in `newer_than:1d in:anywhere` / `in:trash` |
| Newest candidate received_at (UTC) | `2026-07-31T08:50:05.000Z` |
| Second candidate received_at (UTC) | `2026-07-30T23:48:41.000Z` |
| fromClass | `automated_form_like` |
| subjectClass (newest) | `empty` (headers sparse in probe shape) / second: `other` |
| INBOX | **false** |
| UNREAD | **false** |
| TRASH | **true** |
| Incoming production label | **absent** |
| PROCESSED label | **absent** |
| ERROR label | **absent** |
| Custom label count | **0** |
| Eligible under production `labelIds` filter | **NO** (`prodFilterCount=0`) |
| `label:leads_iseo newer_than:7d` count | **0** |

## Stage stop

`website → email delivery → Gmail mailbox` **succeeded**.  
Stopped at **Gmail label/query eligibility** (message in Trash without incoming label).

## Notes

- Message bodies, addresses, subjects, and label IDs are not recorded.
- Old workflow labels (PROCESSED/ERROR) were **not** present on the post-cutover candidates.
