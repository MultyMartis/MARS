# FP-0002 V9-06E16 — Next Step Recommendation

**Wave:** V9-06E16  
**Verdict:** PASS  
**Date:** 2026-07-07

## Recommended next action

**CREATE_V9_06E17_SITE_SETTINGS_IA_SKELETON_TASK**

## Rationale

1. Operator approved E15 baseline and requested backup before further changes — E16 backup complete.
2. Requirements 01–03 all depend on stable admin IA before field migration or cleanup.
3. Site Settings restructure is lowest-risk first implementation step: register subpages without moving renderers.
4. Reusable blocks batch (E18), service clone (E19), and obsolete page trash (E20) should follow the sequence in `FP-0002-V9-06E16-FUTURE-IMPLEMENTATION-SEQUENCE-v1.md`.

## Operator decisions deferred

- Whether to relocate **Отзывы** from top-level menu under **Повторяемые блоки** (recommended in architecture plan).
- Whether genotipirovanie hub DEMO maps should be removed when page ID 9 is trashed (E20 + small source task).

## Do not start yet

- Service duplicate implementation
- Obsolete page delete/trash
- Reusable block renderer migration without E17 skeleton
