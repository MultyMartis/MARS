# GMAIL-FILTER-AUDIT-v1

**Phase:** 3C.2  
**API:** `users.settings.filters.list` via Gmail OAuth through temporary Operational probe (restored)

## Matrix (sanitized)

| Filter | Match class | Add label | Skip inbox | Delete/Trash | Forward | Relevant |
|--------|-------------|-----------|------------|--------------|---------|----------|
| #1 | automated_form_like (`from` only) | OPS incoming + IMPORTANT | no | **no** | no | yes |
| #2 | address_or_domain_bound (`from` only) | OPS incoming | no | **no** | no | yes |

## Counts

| Metric | Value |
|--------|-------|
| Filters total | 2 |
| Filters with Trash/delete action | **0** |
| Filters adding OPS incoming | **2** |
| Filters changed this phase | **0** |

## Match parity (website-form sender)

- Filter #1 `from` hash equals recent website-form message `from` hash.
- Filter #1 action includes OPS incoming label id (name class lead-like parent) + IMPORTANT.
- Live message after successful processing shows OPS PROCESSED (nested child under same family), not Trash.

## Conclusion

No Gmail filter moves website lead mail to Trash. Labeling filters already target the production incoming parent label used by Operational.dev.
