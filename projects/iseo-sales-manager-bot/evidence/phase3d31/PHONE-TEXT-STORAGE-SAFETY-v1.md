# PHONE-TEXT-STORAGE-SAFETY-v1

## Change (Operational.dev, same ID)

On **Append or Update CLEAN v2** and **Append RAW v2**:

- `options.cellFormat = RAW` (Sheets `valueInputOption=RAW`)
- phone / parsed_phone expressions coerced with `String(...)`

## Expected new writes

- Leading `+` preserved as text
- No formula execution
- No `#ERROR!` from plus-prefixed phones

## Historical policy

Existing `#ERROR!` cells left in place. Telegram suppress invalid contacts. Narrow one-row correction deferred (no safe authoritative alternate recovered beyond RAW evidence without PII exposure in this charter).
