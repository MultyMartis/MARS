# ACTOR SNAPSHOT PERSISTENCE v1

On successful applied transition, preserve:

- opaque actor_ref
- actor_role_snapshot at action time
- actor_display_snapshot (safe label)
- transition timestamp
- transition action / new status

## Storage

- CLEAN: existing opaque actor fields (manager_status_updated_by, assigned_to / spam_by)
- LEAD_EVENTS detail JSON: includes actor, actor_role, actor_display, source=telegram_callback
- Telegram card text: final Кем: line is the human-visible snapshot

## Immutability

Later name/username/role changes must not rewrite historical LEAD_EVENTS rows or prior card snapshots.
Idempotent/conflict callbacks must not append a second applied snapshot event.
