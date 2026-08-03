# ACCESS_EVENTS MAPPING REPAIR v1

**Defect class:** Append ACCESS_EVENTS read `$json.*` after Upsert ACCESS_CONTROL. Upsert responses can inject numeric metadata (e.g. updated row counts such as `42`) into role/status fields.

**Repair:** Append ACCESS_EVENTS expressions now reference `$('Prepare Access Upsert').first().json.*` exclusively.

| Field | Expression source |
|---|---|
| ts / opaque_user_ref / event | Prepare Access Upsert |
| prior_role / prior_status / new_role / new_status | Prepare Access Upsert |
| actor_ref / source / outcome / detail | Prepare Access Upsert |

cellFormat=RAW retained. Canonical headers unchanged: ts, opaque_user_ref, event, prior_role, prior_status, new_role, new_status, actor_ref, source, outcome, detail.
