# Profile number stability

**Phase:** 3G.2  
**Status:** FILLED  
**Sanitized labels only:** ADMIN_A · MOD_A · MOD_B_REVOKED · MOD_C_REVOKED  
**Forbidden in this file:** Telegram IDs, workbook IDs, secrets, emails, phones.

## Proof after mutations

Live acceptance exercised on profile **№3 (MOD_A)**:

1. `/reply_name_set 3 Михаил` — name write path exercised
2. `/reply_name_disable 3` — personalization OFF; name Михаил retained
3. `/reply_profile 3` readback while disabled
4. `/reply_name_enable 3` — personalization restored ON
5. Final `/reply_profile 3` + Sheets readback

## Invariants held

| Invariant | Result |
|-----------|--------|
| MOD_A remains number **3** | pass |
| ADMIN_A=1, MOD_B_REVOKED=2, MOD_C_REVOKED=4 unchanged | pass |
| MOD_A role stays moderator | pass |
| MOD_A status stays active | pass |
| access roles changed by name commands | **0** |
| renumbered existing profiles | **0** |
| historical reply snapshots modified | **0** (harness #27) |

Final MOD_A: name **Михаил**, enabled **true**, number **3**.

## Result

- [x] Numbers stable across set/enable/disable
- [x] Access role/status untouched by name commands
