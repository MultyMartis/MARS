# UNIQUE-LEAD-SELECTION-v1

## Bounded read

`Read CLEAN for Leads` uses Data Location A1 range `A1:ZZ250` (header + bounded recent window). Code additionally caps scan to newest 250 rows by timestamp/`row_number`.

## Filters

- Production CLEAN rows only (tab `lead_clean_v2`)
- Exclude `SYNTHETIC_TEST` / phase markers / synthetic lead ids
- Exclude technical-retry-only rows when marked

## Identity preference

1. `lead_id`
2. Gmail message identity (`source_message_id` / `gmail_message_id`)
3. Deterministic fallback (`client_name|site|created_at`) — **not** phone/site alone

## Collapse policy

Same business key → prefer latest timestamp; tie-break by richer valid fields / telegram refs. Technical retries collapse into the same lead. Different legitimate leads with reused phone/site remain distinct.

Return: `min(requested, available_unique)` newest first.
