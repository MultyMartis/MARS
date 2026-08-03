# REPORT — ISEO SALES MANAGER BOT PHASE 3D.5 PUBLIC ACCESS AND MODERATOR REGISTRY

**Verdict:** PHASE 3D.5 COMPLETE — PUBLIC ACCESS AND MODERATOR REGISTRY READY

## Summary

Public informational `/start`/`/help` enabled; operational privileges moved to Sheets **ACCESS_CONTROL** registry with Admin commands to list/approve/revoke moderators without workflow code edits. Андрей remains sole Admin; Оля remains active moderator (not Admin). Callbacks authorize from registry. AI OFF. No new workflows. No client auto-messages. Sales-Manager-v2 inactive.

## Role model

public / moderator / admin / blocked — see evidence/phase3d5/PUBLIC-ACCESS-CONTRACT-v1.md and MODERATOR-ADMIN-ROLE-MATRIX-v1.md.

## ACCESS_CONTROL

Created + migrated (Admin + Olya). ACCESS_EVENTS seeded. SoT documented; CONFIG admin_user_ids bootstrap retained; manager_action_user_ids legacy fallback only.

## Public behavior

Contract texts accepted; staff-only + unknown + blocked denials harness PASS.

## Moderator approval/removal

`/moderators` `/moderator_pending` `/moderator_info` `/moderator_add` `/moderator_remove` — harness PASS including idempotent approve and Admin-protection on remove.

## Callback authorization

Registry-gated; deny text without CLEAN mutation on unauthorized.

## Olya status

Hash E6714550214106BA · moderator active · not Admin · @Ola4seo evidenced.

## Destination/button safety

Cards with buttons only to manager destination; public does not receive leads.

## Workflow states

| WF | Active |
|----|--------|
| Sales-Manager-v2 | false |
| Operational.dev | true |
| Admin.dev | true |

Gmail intake count: 1. Admin nodes ≈ 50. AI calls = 0 (provider disabled). Client messages = 0. New workflows = 0.

## Versions

- parser: sm-parser-v3.2
- message format: sm-msg-v2.2

## Tests

- Harness: 35/35 PASS
- Acceptance: 22/22 PASS

## Evidence

projects/iseo-sales-manager-bot/evidence/phase3d5/

## Git

Commit/push performed from clean worktree on origin/mars/canonical-post-recovery tip (see closeout).
