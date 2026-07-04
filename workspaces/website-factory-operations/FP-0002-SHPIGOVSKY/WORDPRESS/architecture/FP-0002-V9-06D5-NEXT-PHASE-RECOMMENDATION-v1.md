# FP-0002 V9-06D.5 Next Phase Recommendation v1

**Date:** 2026-07-04  
**Phase:** V9-06D.5 → V9-06D.6 decision

## Recommended action

**CREATE_V9_06D6_TEMPLATE_INTEGRATION_PLANNING_TASK**

## Rationale

1. All required D.5 routes resolve HTTP 200 after rewrite-rule repair.
2. Service ID 74 regression PASS.
3. Template/render baseline is a non-blank V9-06B skeleton — ready for integration planning, not production visuals.
4. Full content migration is premature until V9 template integration plan defines which fields/partials render.
5. Page 6 / Service 73 path ownership is secondary debt and should not block D.6 planning (cleanup can follow or run in parallel as a separate micro-task if operator prioritizes).

## Not recommended now

| Action | Why not |
|---|---|
| CREATE_V9_06D6_TEMPLATE_REPAIR_TASK | No fatal/structural template failures |
| CREATE_CONTENT_MIGRATION_WAVE_TASK | Production content migration before template integration would write into inert partials |
| CREATE_PATH_OWNERSHIP_CLEANUP_TASK | Secondary debt only; not a D.5/D.6 planning blocker |
| OPERATOR_DECISION_REQUIRED | Clear next planning step exists |

## V9-06D.6 scope (planning only — not authorized here)

- Map V9 static routes/blocks to WordPress templates/partials
- Define service layout variant wiring (subdivision / leaf / alcohol-special)
- Define integration order (chrome → home → services hub → service singles → contacts)
- Explicitly exclude full production content migration and path cleanup unless operator expands charter

## Authorization status

V9-06D.6: **READY FOR OPERATOR REVIEW** — not authorized to start in this task.
