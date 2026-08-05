# Profile number seed

**Phase:** 3G.2  
**Status:** FILLED  
**Sanitized labels only:** ADMIN_A · MOD_A · MOD_B_REVOKED · MOD_C_REVOKED  
**Forbidden in this file:** Telegram IDs, workbook IDs, secrets, emails, phones.

## Seed assignment

| Label | reply_profile_number | Seed status | Notes |
|-------|---------------------:|-------------|-------|
| ADMIN_A | 1 | queued → applied | Client name Андрей; enabled |
| MOD_B_REVOKED | 2 | queued → applied | Client name Оля; disabled; access revoked |
| MOD_A | 3 | queued → applied | Client name Михаил; enabled; access active |
| MOD_C_REVOKED | 4 | queued → applied | Client name Никита; disabled; access revoked |

Source: `SEED-NUMBER-RESULT.json` (data_count=4, events_count=4, backup_row_count=4). Sheet row indices omitted from committed evidence (internal only).

## Counters

| Counter | Value |
|---------|------:|
| stable reply-profile numbers | 4 |
| duplicate profile numbers | 0 |
| renumbered existing profiles | 0 |

## PROFILE_EVENTS

Tab **PROFILE_EVENTS** created; Admin node **Append PROFILE_EVENTS** added (Admin nodes 84→85). Seed wrote 4 profile-number events (sanitized labels only in this evidence).

## Result

- [x] Seed 1–4 complete; readback confirms uniqueness
