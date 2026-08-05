# COMMAND AUTHORIZATION v1

**Function:** `authorizePendingCommand({ auth_role, status, command })` in `implementation/runtime-libs/pending-leads-lib.mjs`.

## Role/status precedence

1. `role === 'revoked'` or `status === 'revoked'` → denied (`reason=revoked`), checked **first** — revoked always overrides.
2. `role === 'pending'` or `status === 'pending'` → denied (`reason=pending`).
3. `role === 'public'` or `role === 'blocked'` → denied (`reason=denied`).
4. Otherwise resolved against the command class below.

This is the same ACCESS_CONTROL precedence already documented in `architecture/ADMIN-COMMAND-CONTRACT-v1.md` and `implementation/ADMIN-WORKFLOW-PATCH-SPEC-v1.md` §3D.5.1 — Phase 3F.1 does not introduce a second authorization model.

## Command classes

| Class | Commands | Allowed roles |
|---|---|---|
| Staff read | `/pending_count`, `/pending_leads`, `/reminder_status` | active Admin, active moderator |
| Admin config | `/pending_leads_test`, `/reminder_on`, `/reminder_off`, `/reminder_time`, `/reminder_timezone`, `/reminder_min` | active Admin only |

Any command not in either set returns `{ allowed: false, reason: 'unknown' }`.

## Matrix proven (harness #16–21, live acceptance)

| Actor | `/pending_count` | `/pending_leads` | `/reminder_status` | `/pending_leads_test` | `/reminder_time` |
|---|---|---|---|---|---|
| Admin (active) | allow | allow | allow | allow | allow |
| Moderator (active) | allow | allow | allow | **deny** | **deny** |
| Revoked | deny | deny | deny | deny | deny |
| Public/pending | deny | deny | deny | deny | deny |

## Live acceptance evidence

- Admin/moderator/revoked paths were each exercised live against the real ACCESS_CONTROL snapshot.
- `reminder_status` returned "disabled" for a moderator (safe, no config leak beyond current status).
- `/reminder_time` with an invalid value was rejected (no CONFIG write) for Admin.
- A moderator attempting a config-class command was denied.
- A revoked identity was denied across the staff-read class.

*Related: [PENDING-COUNT-ACCEPTANCE-v1.md](PENDING-COUNT-ACCEPTANCE-v1.md), [REMINDER-CONFIG-CONTRACT-v1.md](REMINDER-CONFIG-CONTRACT-v1.md).*
