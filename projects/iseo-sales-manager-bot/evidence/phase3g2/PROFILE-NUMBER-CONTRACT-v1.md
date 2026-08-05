# Profile number contract proof

**Phase:** 3G.2  
**Status:** FILLED  
**Sanitized labels only:** ADMIN_A · MOD_A · MOD_B_REVOKED · MOD_C_REVOKED  
**Forbidden in this file:** Telegram IDs, workbook IDs, secrets, emails, phones.

## Contract

Field `reply_profile_number` is a positive integer, immutable after assignment, independent of Sheets row order and Telegram identity. Admin mutations address profiles **only by number**. Changing name/enable flags must not change ACCESS_CONTROL `role` or `status`.

Authority: `architecture/REPLY-PROFILE-NUMBERING-v1.md`.

## Live proof

| Label | Number | Client name | Enabled | Access | Pass |
|-------|-------:|-------------|---------|--------|------|
| ADMIN_A | 1 | Андрей | true | active | yes |
| MOD_B_REVOKED | 2 | Оля | false | revoked | yes |
| MOD_A | 3 | Михаил | true | active | yes |
| MOD_C_REVOKED | 4 | Никита | false | revoked | yes |

Source: live Sheets readback (`PROFILE-NUMBER-READBACK.json`).

| Check | Result |
|-------|--------|
| Unique numbers 1–4 | pass (`duplicate_numbers=false`) |
| Not Telegram ID | harness check #5 PASS |
| Not row index | harness check #4 PASS |
| Stable across sort | harness check #3 PASS |

## Result

- [x] Field present and seeded 1–4
- [x] Labels only; no PII identifiers
