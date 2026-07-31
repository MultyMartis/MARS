# CANONICAL COMMAND INSTRUCTIONS v1

**Phase:** 3D.2.1

## Advertised commands (operator-facing)

- `/start`
- `/help`
- `/status`
- `/ai_status`
- `/health`
- `/stats`
- `/last_error`
- `/config`
- `/ai_on`
- `/ai_off`

## Not advertised (aliases may still normalize)

- `/aistatus`
- `/lasterror`
- `/aion`
- `/aioff`

## Surfaces checked

| Surface | Result |
|---------|--------|
| Admin Help node | Canonical only (`/ai_status`, …) |
| Phase 3D.2.1 readiness notice | Lists `/start` `/status` `/help` `/config` only |
| Normalize Command aliases | Retained internally; not shown in Help |

## Note on observed `/aistatus`

Help and Phase 3D.2 readiness already used `/ai_status`. Any operator-visible `/aistatus` was alias documentation or an older surface — not the live Help node after Phase 3D.2.
