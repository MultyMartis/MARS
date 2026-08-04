# MODERATOR LIFECYCLE UX SPEC v1 DRAFT

**Status:** DRAFT backlog — not implemented in Phase 3D.8.1  
**Priority:** next appropriate admin UX phase after callback acceptance

## Problem

`/moderator_pending` shows only new pending access requests.  
Former moderators with `status=revoked` are invisible, so stable reactivation codes are hard to retrieve.

## Required `/moderator_pending` sections

### Ожидают подтверждения

New pending users (current behavior).

### Права временно отозваны

Former moderators with `status=revoked`, for example:

1. Пользователь  
   Код: ABC123  
   Права отозваны: …

## Rules

- `/moderators` continues to show only **active** moderators
- Revoked former moderators retain their existing stable code
- `/moderator_add CODE` restores the same ACCESS_CONTROL row
- No duplicate identity row
- Public users are not mixed with former moderators
- Blocked users remain separate
- If pending list is empty but revoked users exist, command still returns the revoked section

## Non-goals (this draft)

- No callback/lifecycle changes
- No AI
- No ACCESS_CONTROL schema redesign beyond display/query
