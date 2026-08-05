# Stats text acceptance

**Phase:** 3G.2  
**Status:** FILLED  
**Sanitized labels only:** ADMIN_A · MOD_A · MOD_B_REVOKED · MOD_C_REVOKED  
**Forbidden in this file:** Telegram IDs, workbook IDs, secrets, emails, phones.

## Live contract

| Item | Value |
|------|-------|
| Authoritative sheet | **LEADS** |
| Epoch display | **05.08.2026** (Europe/Moscow) |
| Events companion | LEAD_EVENTS (reporting/history; not a second stats source of truth) |
| Help line | `/stats` — статистика с 05.08.2026 |
| Stats node hash | `169CA3D4766B81A4` |
| PATCH-RECEIPT | Stats updated; sheet=LEADS |

## Checks

| Check | Result |
|-------|--------|
| No CLEAN-as-authoritative claim in refreshed Stats | pass |
| No PII dumps in stats surface | pass |
| Epoch preserved from Phase 3F.2 baseline | pass |

## Result

- [x] Stats text + LEADS epoch accepted
