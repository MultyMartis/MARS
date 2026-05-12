# Website Factory runbook — Triumph Manipulator Landing (initial)

Human / Cursor-assisted execution outline for future layout and build work. This is **not** an automated workflow engine; it mirrors factory discipline without claiming runtime orchestration.

## Flow

1. **Confirm design handoff** — verify design artifacts and approvals against the Design Handoff Contract; record status in `design-handoff-status.md`.
2. **Confirm frontend handoff** — verify blueprint/design → frontend prerequisites per Frontend Handoff Contract; update `frontend-handoff-status.md`.
3. **Prepare local frontend workspace** — use `workspaces/triumph-manipulator-landing/` per [frontend-workspace.md](frontend-workspace.md); no `dist/` in MARS.
4. **Inspect target Gulp project** — read `package.json`, Gulp tasks, folder conventions; align with [agents/frontend-gulp-agent/](../../agents/frontend-gulp-agent/).
5. **Implement sections one by one** — source-first; map to blueprint sections; avoid scope drift.
6. **Run build** — reproduce clean build locally; capture logs if troubleshooting.
7. **Run frontend QA** — use agent QA checklist and factory QA discipline; update `qa-status.md` with evidence (no fake passes).
8. **Report** — use MARS REPORT format; cite changed paths, unknowns, and blockers.
9. **HITL review** — human approval before any “done” or delivery claim.
10. **Checkpoint** — git checkpoint **only** if explicitly approved per project git rules (not default for routine steps).

## Linked factory documents

- [first-operational-runbook-v0.md](../mars-website-factory/first-operational-runbook-v0.md)
- [website-factory-workflow-v0.md](../mars-website-factory/website-factory-workflow-v0.md)
- [frontend-handoff-contract-v0.md](../mars-website-factory/frontend-handoff-contract-v0.md)
