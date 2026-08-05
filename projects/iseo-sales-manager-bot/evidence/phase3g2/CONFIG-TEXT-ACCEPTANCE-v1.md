# Config text acceptance

**Phase:** 3G.2  
**Status:** FILLED  
**Sanitized labels only:** ADMIN_A · MOD_A · MOD_B_REVOKED · MOD_C_REVOKED  
**Forbidden in this file:** Telegram IDs, workbook IDs, secrets, emails, phones.

## Live posture

- `/config` Admin-only; allowlisted non-secret keys.
- Russian operator labels.
- Config Summary node hash `E63CAB8F8847262D` (PATCH-RECEIPT).
- No API keys, credentials, workbook IDs, or Telegram IDs in operator-facing text.

## Checks

| Check | Result |
|-------|--------|
| Allowlisted keys only | pass (contract) |
| Russian labels | pass |
| No secrets in acceptance artifacts | pass |

## Result

- [x] Config text accepted
