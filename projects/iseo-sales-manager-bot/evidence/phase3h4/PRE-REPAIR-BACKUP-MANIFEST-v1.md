# PRE-REPAIR BACKUP MANIFEST v1 — Phase 3H.4

**Purpose:** Immutable rollback anchor before observability repair patches.  
**Storage location:** `git-sync-iseo-sm-phase3h4-20260806-185304/runtime/backups/pre-repair/` (raw private; not committed)

## Workflow exports (sha256 only)

| Workflow | sha256 |
|---|---|
| Operational.dev | `73DCB2DE6B01A4AADAD761CA735131D7C0F569F51049D806568E851C16D6E56E` |
| Admin.dev | `24318EA9B0EE4B601C4C304204BBD816527793FAE92C7970DD174CB228C1AFB7` |

## Scope

- Same workflow IDs; in-place Code node patches only
- No new workflows
- Temporary webhook nodes introduced during deploy window then removed; final Admin node count restored to **85**

## Validation

- Hashes recorded before Admin Reminder Commands / Status / Health patch
- Hashes recorded before Operational Update Last Success / Runtime State heartbeat patch
