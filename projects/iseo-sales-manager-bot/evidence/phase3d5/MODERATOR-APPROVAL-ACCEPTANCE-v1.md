# MODERATOR APPROVAL ACCEPTANCE v1

Syntax: `/moderator_add ABC123`

Behavior:
- resolve one pending identity by opaque code;
- reject blocked;
- reject Admin targets;
- set role=moderator status=active + approved_at/by;
- append ACCESS_EVENTS moderator_approved;
- reply without raw IDs;
- notify subject: `Вам выданы права модератора. Используйте /start.`
- repeated approval idempotent.

Harness 15–16 **PASS**.
