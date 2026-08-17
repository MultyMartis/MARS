# RAW ACCESS CALLBACK TRACE v1

## PASS (33304)

1. Telegram Trigger callback_query  
2. Normalize: `sm:i:` → raw_source  
3. Read Authorization Config OK  
4. Read ACCESS_CONTROL OK  
5. Check User Authorization: admin + active + manager_action_authorized  
6. IF Authorized true  
7. Resolve / RAW / Handle: raw_inspected, event manager_raw_source_viewed  
8. Answer: «Исходная заявка»

## DENIED (33500)

1–2. same  
3. Read Authorization Config → error item `invalid_grant`  
4. Read ACCESS_CONTROL → error item `invalid_grant`  
5. Check User Authorization: registry_read_ok=false, config_read_ok=false, deny_reason=registry_unavailable, auth_role=public  
6. IF Authorized false  
7. IF Deny Is Callback true  
8. Answer Callback Deny **hardcoded** «Недостаточно прав для изменения статуса.»  
9. Handle Callback **not executed** — raw payload never consulted  

**Divergence node:** Sheets reads feeding Check User Authorization, then Answer Callback Deny text.
