# MODERATOR LIFECYCLE UX SPEC v1

**Status:** IMPLEMENTED in Phase 3D.8.2 (was draft backlog in 3D.8.1)  
**Evidence:** `evidence/phase3d8-2/`

## Problem (resolved)

`/moderator_pending` previously showed only new pending access requests.  
Former moderators with `status=revoked` were invisible, so stable reactivation codes were hard to retrieve.

## `/moderator_pending` sections

### Ожидают подтверждения

New pending users.

### Права временно отозваны

Former moderators with `status=revoked`, including stable reactivation code and revoked date.

## Rules

- `/moderators` continues to show only **active** moderators
- Revoked former moderators retain their existing stable code
- `/moderator_add CODE` restores the same ACCESS_CONTROL row
- No duplicate identity row
- Public users are not mixed with former moderators
- Blocked users remain separate (not listed here)
- If pending list is empty but revoked users exist, command still returns the revoked section
- Admin help: `/moderator_pending — новые заявки и временно отозванные модераторы`

## Optional future

`/moderator_revoked` may be added later; not required while `/moderator_pending` covers the operator need.

## Non-goals

- No AI
- No automatic restore of Olya/Nikita
- No blocked-user admin surface in this command
