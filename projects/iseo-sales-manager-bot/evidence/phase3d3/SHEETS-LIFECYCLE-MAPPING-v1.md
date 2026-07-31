# SHEETS LIFECYCLE MAPPING v1

| Workflow | Node | Tab | Operation | Result |
|----------|------|-----|-----------|--------|
| OPS | Append or Update CLEAN v2 | lead_clean_v2 | upsert | schema+lifecycle fields |
| Admin | Update CLEAN Lifecycle | lead_clean_v2 | update by lead_id | manager action |
| Admin | Append LEAD_EVENTS Callback | LEAD_EVENTS | append | immutable |
| Admin | Read CLEAN for Callback/Leads | lead_clean_v2 | read | present |

Headers extended 52→65. CONFIG message_format_version=sm-msg-v2; manager_action_user_ids seeded from admin list.
