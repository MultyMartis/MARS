# GMAIL-ROUTING-REPAIR-v1

**Phase:** 3C.2

## Gmail filter mutations

| Action | Count |
|--------|-------|
| Filters created | 0 |
| Filters deleted | 0 |
| Filters modified | 0 |
| Trash actions removed | 0 (none present) |

**No Gmail filter change was required:** existing filters already add the production incoming parent label and do not Trash.

## Required routing outcome (verified on live filters)

- Do not move to Trash via filter — **satisfied** (0 trash filters)
- Add production incoming lead label — **configured** on filters #1 and #2
- Do not add PROCESSED/ERROR before n8n — **satisfied** (filters only add incoming ± IMPORTANT)

## Collateral repair (Operational.dev — not Gmail filters)

Authorized under eligible-lead downstream failure / production processing:

1. **Classify Duplicate** — base lead on `Merge AI or Fallback` (Sheets lookup had replaced the item).
2. **Format Telegram Lead Card** — read lead from `Classify Duplicate`.
3. **Send Telegram Lead Card** — `chatId` from `Normalize CONFIG` (fixes empty chat_id).
4. **Add/Remove Gmail label nodes** — `messageId` from `$json.gmail_message_id || $('Parse Lead')` (stale `Lead-Mail-Parser` / `Normalize-AI-Result` refs).

These OPS fixes stopped a reprocess flood and allowed Telegram + Gmail label finalization.
