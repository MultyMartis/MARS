# D6D2-KILL-SWITCH-BASELINE

Token: **D6D2B_KILL_SWITCH_CLAIMS_ACCURATE**

| Field | Value |
|-------|-------|
| site_id | SITE-002 |
| producer identity | mars.client-ops.site-002.unattended-producer |
| mode | DRY_RUN |
| ENABLED authorized | NO |

Canonical safety:
- ENABLED not authorized
- missing kill switch fails closed
- malformed kill switch fails closed
- DRY_RUN mechanically prohibits delivery
- no hidden fallback enables sending

Live config instance is **not** committed; only sanitized contract/evidence.
