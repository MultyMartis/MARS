# Service Admin — Hidden Legacy Groups (E62C)

Operator request (V9-06E62C): hide from Service edit screens:

1. `group_fp02_service_structured_sections` — Service — Structured Sections  
2. `group_fp02_service_relationships` — Service — Relationships / Related Services  

## Implementation

- PHP local groups remain registered for field-key / frontend compatibility.
- `active => false` on both groups.
- `filter_service_parity_groups_by_role` always excludes both keys on Service CPT screens.
- Comment in source: *Hidden from Service admin by operator request in V9-06E62C; data retained for rollback/frontend compatibility.*

## Data / frontend

- Saved postmeta is **not** deleted.
- Theme helpers may still read `intro_text`, `signs_items`, `programme_items`, `stages`, `cta_*`, `manual_related_services`.
- Prefer role-specific parity groups (`service_general` / `section`) for ongoing editing.

## ACF JSON

Source JSON copies marked `active: false`. These files are historically source-only vs runtime and were **not** broadly synced in E62C.
