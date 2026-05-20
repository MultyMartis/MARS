# Triumph Manipulator Landing — MARS project pack

This folder is the **MARS project documentation pack** for the real landing initiative **Triumph / Manipulator Landing**. It coordinates **MARS Website Factory** workflows and the **Frontend Gulp Agent** operational pack.

## What this is **not**

- Production frontend source tree (HTML/SCSS/JS build sources live outside this pack unless explicitly approved).
- MARS runtime code or agent executables.
- A deployed website or hosting artifact.
- A CMS implementation or embedded editor configuration.

## What this **is**

- **Project governance** folder: passport, handoff status, QA posture, SAFE UNKNOWN ledger.
- **Website Factory** reference / production project anchor (contracts and workflow alignment).
- **Coordination point** for design → frontend execution (human / Cursor-assisted).
- **Link surface** for the Frontend Gulp Agent pack and factory contracts.

## Key paths in this pack

| Document | Role |
|----------|------|
| [design/README.md](design/README.md) | Design folder map — `v1/` vs `v2/` vs `shared-assets/`; version isolation |
| [V3-BATTLE-TEST-CHARTER.md](V3-BATTLE-TEST-CHARTER.md) | V3 Forge battle-test charter — full rebuild from V1 source authority; V2 lessons only |
| [V3-GOVERNANCE-MODE.md](V3-GOVERNANCE-MODE.md) | V3 adaptive governance mode, escalation, SAFE UNKNOWN, HITL, compression |
| [V3-SOURCE-AUTHORITY.md](V3-SOURCE-AUTHORITY.md) | V3 source authority: V1 primary, approved lessons secondary, V2 implementation not authority |
| [V3-SUCCESS-CRITERIA.md](V3-SUCCESS-CRITERIA.md), [V3-FAILURE-CONDITIONS.md](V3-FAILURE-CONDITIONS.md), [V3-EXECUTION-BOUNDARIES.md](V3-EXECUTION-BOUNDARIES.md) | V3 success/failure boundaries and execution constraints |
| [project-passport.md](project-passport.md) | Canonical project identity and lifecycle fields |
| [frontend-workspace.md](frontend-workspace.md) | Where local frontend work is expected to happen |
| [website-factory-runbook.md](website-factory-runbook.md) | Initial operational flow for layout / build work |
| [frontend-agent-brief.md](frontend-agent-brief.md) | Seed brief for a separate Frontend Gulp Agent chat |
| [design-handoff-status.md](design-handoff-status.md) | Design gate status |
| [frontend-handoff-status.md](frontend-handoff-status.md) | Frontend gate status |
| [qa-status.md](qa-status.md) | QA posture |
| [safe-unknown.md](safe-unknown.md) | Consolidated unknowns |
| [equipment-prices quarantine (V2)](design/v2/validation/equipment-prices-quarantine.md) | Fleet block **off homepage**; validation-page status |

## V3 battle-test preparation

V3 is prepared as a **Forge doctrine battle test** and **operational proof attempt**: full rebuild from V1 source authority, with V2 used only for approved lessons, drift references, and known-failure references. It does **not** authorize implementation, production release, or inheritance from V2 CSS / structure / patches.

## Website Factory and agent links

- **Reference case (documentation-first):** [MARS Website Factory — Triumph Manipulator Landing reference case](../mars-website-factory/reference-cases/triumph-manipulator-landing/)
- **Frontend Gulp Agent pack:** [agents/frontend-gulp-agent/README.md](../../agents/frontend-gulp-agent/README.md)
- **Gulp Frontend Agent card (v0):** [agents/cards/gulp-frontend-agent-v0.md](../../agents/cards/gulp-frontend-agent-v0.md)
- **Frontend Handoff Contract v0:** [frontend-handoff-contract-v0.md](../mars-website-factory/frontend-handoff-contract-v0.md)
- **Frontend production model:** [frontend-production-model.md](../mars-website-factory/frontend-production-model.md)
- **First Operational Runbook v0:** [first-operational-runbook-v0.md](../mars-website-factory/first-operational-runbook-v0.md)

## Registry

Authoritative **project_id** row: [`../../registry/project-registry.md`](../../registry/project-registry.md).
