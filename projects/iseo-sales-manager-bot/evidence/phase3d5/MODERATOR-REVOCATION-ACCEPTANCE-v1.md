# MODERATOR REVOCATION ACCEPTANCE v1

Syntax: `/moderator_remove ABC123`

Behavior:
- cannot remove Admin via moderator command;
- status=revoked; keep row;
- immediate callback denial;
- ACCESS_EVENTS moderator_revoked;
- notify subject: `Рабочие права модератора отозваны.`

Harness 17–19 **PASS**.
