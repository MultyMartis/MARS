# Forge WordPress — Operational Index

**Subsystem:** Forge WordPress (WP Forge)  
**Parent:** [MARS Website Factory](../../OPERATIONAL-INDEX.md)  
**Lane:** B — Website Factory architecture and documentation

---

## Current state

```text
FW-00 — COMPLETE
FW-01 — COMPLETE
FW-02 — COMPLETE
FW-03 — COMPLETE
FW-04 — COMPLETE
FW-05 — COMPLETE (PROVEN WITH LIMITATIONS)
FW-05R — COMPLETE (PROVEN WITH LIMITATIONS)
FW-06A — COMPLETE (FP-0002 local foundation)
FW-06A.1 — COMPLETE (FP-0002 foundation closure)
FW-06B — WAITING FOR FRONTEND PRODUCTION PASS
FW-07A — COMPLETE (AG-WP-001 foundation)
FW-07B — COMPLETE (AG-WP-001 typed operations)
FW-07C — Safety Preflight — COMPLETE (2026-06-25)
FW-07C-0 — Enforcement Foundation — IMPLEMENTED_AND_VALIDATED_IN_REPO (2026-06-26)
FW-07C-1 — Local Read-Only Harness — BLOCKED_BY_RUNTIME_BINDING_PREFLIGHT
Architecture: DOCUMENTED
Contracts: BASELINE v1
Standards: BASELINE v1
Tooling design: BASELINE v1
Validation design: BASELINE v1
Templates: BASELINE v1
Prompt-driven implementation capability: PROVEN WITH LIMITATIONS (live synthetic)
Primary specialist profile: PROVEN (live synthetic)
Skills: PROVEN WITH LIMITATIONS
Validators: PROVEN (live reports)
Synthetic validation: COMPLETE (FWS-0001 static + live)
Local environment: PROVEN WITH LIMITATIONS (MLI Profile A)
Local Laragon profile: ENABLED (MLI-03) — Laragon at E:\MARS-Localhost\laragon
FW-05R — COMPLETE (PROVEN WITH LIMITATIONS)
FW-06B — WAITING FOR FRONTEND PRODUCTION PASS
Operator WV6: PENDING
Direct local domain: PASS (FP-0002 — FW-06A.1)
Synthetic source: TRACKED (Git whitelist)
Agent registration: REGISTERED (AG-WP-001 — draft; NOT RUNTIME-ACTIVE)
Client pilot: NOT STARTED — WordPress foundation READY; theme integration LOCKED until FW-06B
```

| Field | Value |
|-------|-------|
| **Lifecycle** | **FOUNDATION / PRE-OPERATIONAL** |
| **Runtime** | **EXCLUDED** |
| **Agent** | **REGISTERED** (`AG-WP-001` — `draft`; **NOT RUNTIME-ACTIVE**) |
| **project_id** | **NOT CREATED** |

---

## Session routing — Core Run

| Concern | Start here |
|---------|------------|
| **Implementation capability (FW-04)** | [capability/OPERATIONAL-INDEX.md](capability/OPERATIONAL-INDEX.md) |
| **AG-WP-001 agent pack (FW-07A)** | [agents/README.md](agents/README.md) |
| **Primary specialist** | [capability/primary-specialist/FORGE-WORDPRESS-IMPLEMENTATION-SPECIALIST-v1.md](capability/primary-specialist/FORGE-WORDPRESS-IMPLEMENTATION-SPECIALIST-v1.md) |
| **Prompt pack** | [capability/task-templates/FORGE-WORDPRESS-PROMPT-PACK-v1.md](capability/task-templates/FORGE-WORDPRESS-PROMPT-PACK-v1.md) |
| **Architecture overview** | [FORGE-WORDPRESS-ARCHITECTURE-v1.md](FORGE-WORDPRESS-ARCHITECTURE-v1.md) |
| **Contracts register** | [registries/FORGE-WORDPRESS-CONTRACTS-AND-STANDARDS-REGISTER-v1.md](registries/FORGE-WORDPRESS-CONTRACTS-AND-STANDARDS-REGISTER-v1.md) |
| **Tool registry** | [registries/FORGE-WORDPRESS-TOOL-REGISTRY-v1.md](registries/FORGE-WORDPRESS-TOOL-REGISTRY-v1.md) |
| **AG-WP-001 operation registry** | [registries/FORGE-WORDPRESS-AG-WP-001-OPERATION-REGISTRY-v1.md](registries/FORGE-WORDPRESS-AG-WP-001-OPERATION-REGISTRY-v1.md) + [operations/ag-wp-001/operations-v1.json](operations/ag-wp-001/operations-v1.json) |
| **AG-WP-001 contract validator** | [tools/validate-ag-wp-001-operation-contracts.mjs](tools/validate-ag-wp-001-operation-contracts.mjs) |
| **Compliance matrix** | [FORGE-WORDPRESS-FW-02-COMPLIANCE-MATRIX-v1.md](FORGE-WORDPRESS-FW-02-COMPLIANCE-MATRIX-v1.md) |
| **Local environment** | [FORGE-WORDPRESS-LOCAL-ENVIRONMENT-DECISION-v1.md](FORGE-WORDPRESS-LOCAL-ENVIRONMENT-DECISION-v1.md) — **consumes** [MLI WordPress profile](../../../mars-localhost-infrastructure/MARS-LOCALHOST-CONSUMER-MODEL-v1.md) |
| **Shared localhost** | [projects/mars-localhost-infrastructure/OPERATIONAL-INDEX.md](../../../mars-localhost-infrastructure/OPERATIONAL-INDEX.md) — Forge does **not** own `E:\MARS-Localhost` |
| **Gulp integration** | [FORGE-WORDPRESS-GULP-INTEGRATION-MODEL-v1.md](FORGE-WORDPRESS-GULP-INTEGRATION-MODEL-v1.md) |
| **Validation runners** | [FORGE-WORDPRESS-VALIDATION-RUNNER-ARCHITECTURE-v1.md](FORGE-WORDPRESS-VALIDATION-RUNNER-ARCHITECTURE-v1.md) |
| **Pilot tooling** | [FORGE-WORDPRESS-PILOT-TOOLING-PROFILE-v1.md](FORGE-WORDPRESS-PILOT-TOOLING-PROFILE-v1.md) |
| **Project lifecycle** | [FORGE-WORDPRESS-PROJECT-LIFECYCLE-v1.md](FORGE-WORDPRESS-PROJECT-LIFECYCLE-v1.md) |
| **FW-05 input** | [reports/FORGE-WORDPRESS-FW-05-LOCAL-ENABLEMENT-AND-SYNTHETIC-VALIDATION-INPUT-v1.md](reports/FORGE-WORDPRESS-FW-05-LOCAL-ENABLEMENT-AND-SYNTHETIC-VALIDATION-INPUT-v1.md) |
| **Capability readiness** | [capability/FORGE-WORDPRESS-CAPABILITY-READINESS-MATRIX-v1.md](capability/FORGE-WORDPRESS-CAPABILITY-READINESS-MATRIX-v1.md) |

---

## FW-04 capability pack

| # | Document |
|---|----------|
| 1 | [capability/README.md](capability/README.md) |
| 2 | [capability/primary-specialist/FORGE-WORDPRESS-IMPLEMENTATION-SPECIALIST-v1.md](capability/primary-specialist/FORGE-WORDPRESS-IMPLEMENTATION-SPECIALIST-v1.md) |
| 3 | [capability/protocols/FORGE-WORDPRESS-SPECIALIST-EXECUTION-CONTRACT-v1.md](capability/protocols/FORGE-WORDPRESS-SPECIALIST-EXECUTION-CONTRACT-v1.md) |
| 4 | [capability/skills/](capability/skills/) — 14 skills |
| 5 | [capability/validators/](capability/validators/) — 7 validators |
| 6 | [capability/task-templates/FORGE-WORDPRESS-PROMPT-PACK-v1.md](capability/task-templates/FORGE-WORDPRESS-PROMPT-PACK-v1.md) |
| 7 | [capability/reports/FORGE-WORDPRESS-SYNTHETIC-TEST-CASE-SPEC-v1.md](capability/reports/FORGE-WORDPRESS-SYNTHETIC-TEST-CASE-SPEC-v1.md) |
| 8 | [capability/reports/FORGE-WORDPRESS-AG-WP-001-PROMOTION-DECISION-v1.md](capability/reports/FORGE-WORDPRESS-AG-WP-001-PROMOTION-DECISION-v1.md) |

---

## FW-03 tooling design pack

| # | Document |
|---|----------|
| 1 | [FORGE-WORDPRESS-LOCAL-ENVIRONMENT-DECISION-v1.md](FORGE-WORDPRESS-LOCAL-ENVIRONMENT-DECISION-v1.md) |
| 2 | [FORGE-WORDPRESS-REPOSITORY-AND-FILESYSTEM-MODEL-v1.md](FORGE-WORDPRESS-REPOSITORY-AND-FILESYSTEM-MODEL-v1.md) |
| 3 | [FORGE-WORDPRESS-GULP-INTEGRATION-MODEL-v1.md](FORGE-WORDPRESS-GULP-INTEGRATION-MODEL-v1.md) |
| 4 | [FORGE-WORDPRESS-COMMAND-AND-OPERATION-MODEL-v1.md](FORGE-WORDPRESS-COMMAND-AND-OPERATION-MODEL-v1.md) |
| 5 | [FORGE-WORDPRESS-SAFE-COMMAND-POLICY-v1.md](FORGE-WORDPRESS-SAFE-COMMAND-POLICY-v1.md) |
| 6 | [FORGE-WORDPRESS-VALIDATION-RUNNER-ARCHITECTURE-v1.md](FORGE-WORDPRESS-VALIDATION-RUNNER-ARCHITECTURE-v1.md) |
| 7 | [FORGE-WORDPRESS-CODE-QUALITY-PROFILE-v1.md](FORGE-WORDPRESS-CODE-QUALITY-PROFILE-v1.md) |
| 8 | [FORGE-WORDPRESS-VISUAL-REGRESSION-DESIGN-v1.md](FORGE-WORDPRESS-VISUAL-REGRESSION-DESIGN-v1.md) |
| 9 | [FORGE-WORDPRESS-ACCESSIBILITY-AND-PERFORMANCE-PROFILE-v1.md](FORGE-WORDPRESS-ACCESSIBILITY-AND-PERFORMANCE-PROFILE-v1.md) |
| 10 | [FORGE-WORDPRESS-SECURITY-VALIDATION-DESIGN-v1.md](FORGE-WORDPRESS-SECURITY-VALIDATION-DESIGN-v1.md) |
| 11 | [FORGE-WORDPRESS-PACKAGING-AND-RELEASE-DESIGN-v1.md](FORGE-WORDPRESS-PACKAGING-AND-RELEASE-DESIGN-v1.md) |
| 12 | [FORGE-WORDPRESS-FUTURE-SKILL-MODEL-v1.md](FORGE-WORDPRESS-FUTURE-SKILL-MODEL-v1.md) — superseded by capability skills |
| 13 | [FORGE-WORDPRESS-FUTURE-VALIDATOR-MODEL-v1.md](FORGE-WORDPRESS-FUTURE-VALIDATOR-MODEL-v1.md) — superseded by capability validators |
| 14 | [FORGE-WORDPRESS-PILOT-TOOLING-PROFILE-v1.md](FORGE-WORDPRESS-PILOT-TOOLING-PROFILE-v1.md) |
| 15 | [reports/FORGE-WORDPRESS-LOCAL-TOOLING-CAPABILITY-AUDIT-v1.md](reports/FORGE-WORDPRESS-LOCAL-TOOLING-CAPABILITY-AUDIT-v1.md) |
| 16 | [reports/FORGE-WORDPRESS-FW-03-TOOLING-DECISION-RECORD-v1.md](reports/FORGE-WORDPRESS-FW-03-TOOLING-DECISION-RECORD-v1.md) |

---

## FW-02 contracts

| ID | Document |
|----|----------|
| FW-C-01 | [contracts/WEBSITE-FACTORY-TO-FORGE-WORDPRESS-HANDOFF-CONTRACT-v1.md](contracts/WEBSITE-FACTORY-TO-FORGE-WORDPRESS-HANDOFF-CONTRACT-v1.md) |
| FW-C-02 | [contracts/FORGE-WORDPRESS-PROJECT-INTAKE-CONTRACT-v1.md](contracts/FORGE-WORDPRESS-PROJECT-INTAKE-CONTRACT-v1.md) |
| FW-C-03 | [contracts/FORGE-WORDPRESS-TO-WPILOT-HANDOFF-CONTRACT-v1.md](contracts/FORGE-WORDPRESS-TO-WPILOT-HANDOFF-CONTRACT-v1.md) |

---

## FW-02 standards

| ID | Document |
|----|----------|
| FW-S-01 | [standards/FORGE-WORDPRESS-CONTENT-MODELING-STANDARD-v1.md](standards/FORGE-WORDPRESS-CONTENT-MODELING-STANDARD-v1.md) |
| FW-S-02 | [standards/FORGE-WORDPRESS-ACF-ARCHITECTURE-STANDARD-v1.md](standards/FORGE-WORDPRESS-ACF-ARCHITECTURE-STANDARD-v1.md) |
| FW-S-03 | [standards/FORGE-WORDPRESS-THEME-ARCHITECTURE-STANDARD-v1.md](standards/FORGE-WORDPRESS-THEME-ARCHITECTURE-STANDARD-v1.md) |
| FW-S-04 | [standards/FORGE-WORDPRESS-FUNCTIONALITY-PLUGIN-STANDARD-v1.md](standards/FORGE-WORDPRESS-FUNCTIONALITY-PLUGIN-STANDARD-v1.md) |
| FW-S-05 | [standards/FORGE-WORDPRESS-ADMIN-UX-STANDARD-v1.md](standards/FORGE-WORDPRESS-ADMIN-UX-STANDARD-v1.md) |
| FW-S-06 | [standards/FORGE-WORDPRESS-PLUGIN-GOVERNANCE-STANDARD-v1.md](standards/FORGE-WORDPRESS-PLUGIN-GOVERNANCE-STANDARD-v1.md) |
| FW-S-07 | [standards/FORGE-WORDPRESS-CODING-AND-SECURITY-STANDARD-v1.md](standards/FORGE-WORDPRESS-CODING-AND-SECURITY-STANDARD-v1.md) |
| FW-S-08 | [standards/FORGE-WORDPRESS-VALIDATION-STANDARD-v1.md](standards/FORGE-WORDPRESS-VALIDATION-STANDARD-v1.md) |

---

## Templates

| Pack | Path |
|------|------|
| FW-02 templates (13) | [templates/](templates/) — FW-T-01–13 |
| FW-03 templates (5) | FW-T-14–18 — mapping, impl spec, validation plan, lessons, tooling audit |

---

## FW-01 document index

| # | Document |
|---|----------|
| 1 | [FORGE-WORDPRESS-ARCHITECTURE-v1.md](FORGE-WORDPRESS-ARCHITECTURE-v1.md) |
| 2 | [FORGE-WORDPRESS-CAPABILITY-MODEL-v1.md](FORGE-WORDPRESS-CAPABILITY-MODEL-v1.md) |
| 3 | [FORGE-WORDPRESS-IMPLEMENTATION-MODES-v1.md](FORGE-WORDPRESS-IMPLEMENTATION-MODES-v1.md) |
| 4 | [FORGE-WORDPRESS-ARCHITECTURAL-DECISIONS-v1.md](FORGE-WORDPRESS-ARCHITECTURAL-DECISIONS-v1.md) |
| 5 | [FORGE-WORDPRESS-PROJECT-LIFECYCLE-v1.md](FORGE-WORDPRESS-PROJECT-LIFECYCLE-v1.md) |
| 6 | [FORGE-WORDPRESS-PROJECT-ARTIFACT-MODEL-v1.md](FORGE-WORDPRESS-PROJECT-ARTIFACT-MODEL-v1.md) |
| 7 | [FORGE-WORDPRESS-ROLE-AND-AGENT-MODEL-v1.md](FORGE-WORDPRESS-ROLE-AND-AGENT-MODEL-v1.md) |
| 8 | [FORGE-WORDPRESS-TOOLING-ARCHITECTURE-v1.md](FORGE-WORDPRESS-TOOLING-ARCHITECTURE-v1.md) |
| 9 | [FORGE-WORDPRESS-VALIDATION-ARCHITECTURE-v1.md](FORGE-WORDPRESS-VALIDATION-ARCHITECTURE-v1.md) |
| 10 | [FORGE-WORDPRESS-HUMAN-CONTROL-MODEL-v1.md](FORGE-WORDPRESS-HUMAN-CONTROL-MODEL-v1.md) |
| 11 | [FORGE-WORDPRESS-HANDOFF-BOUNDARIES-v1.md](FORGE-WORDPRESS-HANDOFF-BOUNDARIES-v1.md) |
| 12 | [FORGE-WORDPRESS-RESEARCH-ADAPTATION-REGISTER-v1.md](FORGE-WORDPRESS-RESEARCH-ADAPTATION-REGISTER-v1.md) |
| 13 | [reports/FORGE-WORDPRESS-FW-01-DECISION-RECORD-v1.md](reports/FORGE-WORDPRESS-FW-01-DECISION-RECORD-v1.md) |

---

## Foundation documents (FW-00)

| Document | Purpose |
|----------|---------|
| [FORGE-WORDPRESS-IDENTITY-v1.md](FORGE-WORDPRESS-IDENTITY-v1.md) | Identity |
| [FORGE-WORDPRESS-SCOPE-AND-BOUNDARIES-v1.md](FORGE-WORDPRESS-SCOPE-AND-BOUNDARIES-v1.md) | Scope |
| [FORGE-WORDPRESS-ECOSYSTEM-POSITION-v1.md](FORGE-WORDPRESS-ECOSYSTEM-POSITION-v1.md) | Ecosystem |
| [FORGE-WORDPRESS-RESEARCH-REGISTER-v1.md](FORGE-WORDPRESS-RESEARCH-REGISTER-v1.md) | Evidence |

---

## Research base

| Source | Index |
|--------|-------|
| AG-WP-001 seed | [research README](../../../../workspaces/website-factory-operations/internal-agent-seeds/AG-WP-001-forge-wordpress/research/README.md) |
| AG-WP-001 promotion | [capability/reports/FORGE-WORDPRESS-AG-WP-001-PROMOTION-DECISION-v1.md](capability/reports/FORGE-WORDPRESS-AG-WP-001-PROMOTION-DECISION-v1.md) |
| Adaptation register | [FORGE-WORDPRESS-RESEARCH-ADAPTATION-REGISTER-v1.md](FORGE-WORDPRESS-RESEARCH-ADAPTATION-REGISTER-v1.md) |

---

## Parent Website Factory

- Pack: [projects/mars-website-factory/README.md](../../README.md)
- Navigation: [projects/mars-website-factory/OPERATIONAL-INDEX.md](../../OPERATIONAL-INDEX.md)
- Layer: **Candidate WordPress Implementation Layer** — [layer-map.md](../../layer-map.md) §9
- Factory handoff: [frontend-handoff-contract-v0.md](../../frontend-handoff-contract-v0.md)

---

## WPilot boundary

Forge WordPress **produces** packages. **WPilot operates** sites — [FORGE-WORDPRESS-TO-WPILOT-HANDOFF-CONTRACT-v1.md](contracts/FORGE-WORDPRESS-TO-WPILOT-HANDOFF-CONTRACT-v1.md) · [projects/wpilot/OPERATIONAL-INDEX.md](../../../wpilot/OPERATIONAL-INDEX.md)

WPilot does **not** own theme/content architecture.

---

## First probable pilot

**FP-0002 — Shpigovsky.ru** — FW-06A foundation **READY** on `shpigovsky.test`; frontend integration **HOLD**; see [projects/fp-0002/](projects/fp-0002/).

---

## Next authorized stage

```text
FW-06B — Approved Frontend Intake (FP-0002) — WAITING
FW-07B — AG-WP-001 Typed Operations — PLANNED (not auto-start)
```

---

*Last updated: 2026-06-24 — FW-07A AG-WP-001 foundation complete.*
