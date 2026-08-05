# Profile mutation history

**Phase:** 3G.2  
**Status:** FILLED  
**Sanitized labels only:** ADMIN_A · MOD_A · MOD_B_REVOKED · MOD_C_REVOKED  
**Forbidden in this file:** Telegram IDs, workbook IDs, secrets, emails, phones.

## PROFILE_EVENTS

- Tab **PROFILE_EVENTS** created on the operational workbook (sheet id omitted from evidence).
- Admin node **Append PROFILE_EVENTS** created (Admin node count 84→**85**).
- Seed wrote **4** number-assignment events (one per label 1–4).

## Mutation path

Prepare Access Upsert now flattens reply-profile fields for Upsert ACCESS_CONTROL (includes `reply_profile_number` schema per PATCH-RECEIPT). Name set / enable / disable write reply fields only — **no** ACCESS_CONTROL role/status side effects.

## Live mutation log (sanitized)

| Actor role | Command | Target | Effect |
|------------|---------|--------|--------|
| Admin | `/reply_name_set 3 Михаил` | MOD_A | name confirmed Михаил |
| Admin | `/reply_name_disable 3` | MOD_A | enabled→false; name preserved |
| Admin | `/reply_name_enable 3` | MOD_A | enabled→true |
| Moderator | `/reply_name_set …` | — | denied; no mutation |
| Moderator | `/reply_profiles` | — | denied; no mutation |

## Historical snapshots

| Counter | Value |
|---------|------:|
| historical reply snapshots modified | 0 |

Harness check #27 PASS — prior recipient reply snapshots unchanged by profile admin commands.

## Result

- [x] PROFILE_EVENTS + Append node present
- [x] Mutations audited without PII
