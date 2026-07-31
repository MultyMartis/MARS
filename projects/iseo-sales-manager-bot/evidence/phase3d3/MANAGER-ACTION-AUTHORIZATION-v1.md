# MANAGER ACTION AUTHORIZATION v1

CONFIG keys: `admin_user_ids`, `manager_action_user_ids`.  
Phase 3D.3: manager list falls back to admin allowlist (operator only).  
Olya enrollment deferred — not auto-added; not on admin allowlist.  
Unauthorized callback: no Sheets mutation; answer «Доступ запрещён.»

## Future Olya enrollment
1. Olya opens bot/manager chat  
2. Controlled enrollment / identity resolve  
3. Explicit operator approval  
4. Add to `manager_action_user_ids` only (not admin)
