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
FW-03 — NEXT
Architecture: DOCUMENTED
Methodology: BASELINE v1
Contracts: BASELINE v1
Standards: BASELINE v1
Templates: BASELINE v1
Implementation capability: NOT STARTED
```

| Field | Value |
|-------|-------|
| **Lifecycle** | **FOUNDATION** |
| **Runtime** | **EXCLUDED** |
| **Agent** | **NOT REGISTERED** — seed `AG-WP-001` only |
| **project_id** | **NOT CREATED** |

---

## Session routing — Core Run

| Concern | Start here |
|---------|------------|
| **Architecture overview** | [FORGE-WORDPRESS-ARCHITECTURE-v1.md](FORGE-WORDPRESS-ARCHITECTURE-v1.md) |
| **Contracts register** | [registries/FORGE-WORDPRESS-CONTRACTS-AND-STANDARDS-REGISTER-v1.md](registries/FORGE-WORDPRESS-CONTRACTS-AND-STANDARDS-REGISTER-v1.md) |
| **Compliance matrix** | [FORGE-WORDPRESS-FW-02-COMPLIANCE-MATRIX-v1.md](FORGE-WORDPRESS-FW-02-COMPLIANCE-MATRIX-v1.md) |
| **Project lifecycle** | [FORGE-WORDPRESS-PROJECT-LIFECYCLE-v1.md](FORGE-WORDPRESS-PROJECT-LIFECYCLE-v1.md) |
| **FW-03 input** | [reports/FORGE-WORDPRESS-FW-03-TOOLING-AND-VALIDATION-DESIGN-INPUT-v1.md](reports/FORGE-WORDPRESS-FW-03-TOOLING-AND-VALIDATION-DESIGN-INPUT-v1.md) |

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

## FW-02 templates

| Pack | Path |
|------|------|
| Project artifact templates (13) | [templates/](templates/) |

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

**FP-0002 — Shpigovsky.ru** — visibility only; WordPress **NOT STARTED**; eligibility **FW-04**.

---

## Next authorized stage

```text
FW-03 — Tooling and Validation Design
```

---

*Last updated: 2026-06-22 — FW-02 Contracts and Standards complete.*
