# Name validation

**Phase:** 3G.2  
**Status:** FILLED  
**Sanitized labels only:** ADMIN_A · MOD_A · MOD_B_REVOKED · MOD_C_REVOKED  
**Forbidden in this file:** Telegram IDs, workbook IDs, secrets, emails, phones.

## Accepted patterns (seed / live)

| Label | Accepted client name |
|-------|----------------------|
| ADMIN_A | Андрей |
| MOD_A | Михаил |
| MOD_B_REVOKED | Оля |
| MOD_C_REVOKED | Никита |

## Rejected (harness + live)

| Case | Harness | Live |
|------|---------|------|
| Multi-token / full name | #16 PASS | `invalid_name_full` → hint with `/reply_name_set 3 Михаил` |
| Username-shaped | #17 PASS | rejected |
| URL | #18 PASS | rejected |
| Emoji | #19 PASS | rejected |
| Empty / missing for enable | #24 PASS | enable requires prior valid name |

## Contract rules

- Single human first name; Cyrillic/Latin.
- No `@`, URL, phone, emoji, role/company labels.
- No auto-shorten of multi-token names — reject instead.
- Name set does **not** auto-enable and does **not** change access.

## Counters

| Counter | Value |
|---------|------:|
| moderator name mutations accepted | 0 |
| access roles changed by name commands | 0 |

## Result

- [x] Validation matches TEXT-CONTRACT-v2 + REPLY-PROFILE-ADMIN-v2
