# Forge WordPress

**Canonical name:** Forge WordPress  
**Operator alias:** WP Forge  
**Class:** Website Factory subsystem  
**Lifecycle:** **FOUNDATION**  
**Runtime status:** **EXCLUDED**  
**Agent registration:** **NOT REGISTERED** (`AG-WP-001` remains internal seed only)  
**project_id:** **NOT CREATED** (subsystem under `mars-website-factory`)

---

## What this is

Documentation-first **WordPress implementation subsystem** of MARS Website Factory. It is the canonical methodology home for transforming an **approved Website Factory frontend package** into a **WordPress implementation package** for downstream handoff to **WPilot** (controlled operations).

**Entity creation does not mean implementation capability is operational.**

---

## Status (FW-03 complete)

```text
FW-00 — COMPLETE
FW-01 — COMPLETE
FW-02 — COMPLETE
FW-03 — COMPLETE
FW-04 — NEXT
Architecture: DOCUMENTED
Methodology: BASELINE v1
Contracts: BASELINE v1
Standards: BASELINE v1
Tooling design: BASELINE v1
Validation design: BASELINE v1
Templates: BASELINE v1
Implementation capability: NOT STARTED
```

---

## Position in the pipeline

```text
Website Factory
    → approved frontend package
Forge WordPress
    → WordPress implementation package
WPilot
    → controlled WordPress operations
```

Human remains the final authority. Production runtime and autonomous deployment are **excluded**.

---

## Start here

| Document | Purpose |
|----------|---------|
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Session navigation and current state |
| [FORGE-WORDPRESS-ARCHITECTURE-v1.md](FORGE-WORDPRESS-ARCHITECTURE-v1.md) | Layer model L1–L10 |
| [FORGE-WORDPRESS-PROJECT-LIFECYCLE-v1.md](FORGE-WORDPRESS-PROJECT-LIFECYCLE-v1.md) | FWP-01–FWP-12 stages |
| [FORGE-WORDPRESS-ARCHITECTURAL-DECISIONS-v1.md](FORGE-WORDPRESS-ARCHITECTURAL-DECISIONS-v1.md) | Core FW-01 decisions |
| [FORGE-WORDPRESS-IDENTITY-v1.md](FORGE-WORDPRESS-IDENTITY-v1.md) | Identity and classification |
| [FORGE-WORDPRESS-SCOPE-AND-BOUNDARIES-v1.md](FORGE-WORDPRESS-SCOPE-AND-BOUNDARIES-v1.md) | Scope and exclusions |
| [FORGE-WORDPRESS-ECOSYSTEM-POSITION-v1.md](FORGE-WORDPRESS-ECOSYSTEM-POSITION-v1.md) | Ecosystem relationships |
| [roadmap.md](roadmap.md) | Subsystem stages |
| [reports/](reports/) | Stage inputs, decision records |

---

## FW-02 contracts and standards

| Area | Document |
|------|----------|
| Register | [registries/FORGE-WORDPRESS-CONTRACTS-AND-STANDARDS-REGISTER-v1.md](registries/FORGE-WORDPRESS-CONTRACTS-AND-STANDARDS-REGISTER-v1.md) |
| Compliance matrix | [FORGE-WORDPRESS-FW-02-COMPLIANCE-MATRIX-v1.md](FORGE-WORDPRESS-FW-02-COMPLIANCE-MATRIX-v1.md) |
| Factory handoff | [contracts/WEBSITE-FACTORY-TO-FORGE-WORDPRESS-HANDOFF-CONTRACT-v1.md](contracts/WEBSITE-FACTORY-TO-FORGE-WORDPRESS-HANDOFF-CONTRACT-v1.md) |
| WPilot handoff | [contracts/FORGE-WORDPRESS-TO-WPILOT-HANDOFF-CONTRACT-v1.md](contracts/FORGE-WORDPRESS-TO-WPILOT-HANDOFF-CONTRACT-v1.md) |
| Templates | [templates/](templates/) |

---

## FW-03 tooling and validation design

| Area | Document |
|------|----------|
| Local environment | [FORGE-WORDPRESS-LOCAL-ENVIRONMENT-DECISION-v1.md](FORGE-WORDPRESS-LOCAL-ENVIRONMENT-DECISION-v1.md) |
| Repository model | [FORGE-WORDPRESS-REPOSITORY-AND-FILESYSTEM-MODEL-v1.md](FORGE-WORDPRESS-REPOSITORY-AND-FILESYSTEM-MODEL-v1.md) |
| Gulp integration | [FORGE-WORDPRESS-GULP-INTEGRATION-MODEL-v1.md](FORGE-WORDPRESS-GULP-INTEGRATION-MODEL-v1.md) |
| Tool registry | [registries/FORGE-WORDPRESS-TOOL-REGISTRY-v1.md](registries/FORGE-WORDPRESS-TOOL-REGISTRY-v1.md) |
| Command model | [FORGE-WORDPRESS-COMMAND-AND-OPERATION-MODEL-v1.md](FORGE-WORDPRESS-COMMAND-AND-OPERATION-MODEL-v1.md) |
| Safe commands | [FORGE-WORDPRESS-SAFE-COMMAND-POLICY-v1.md](FORGE-WORDPRESS-SAFE-COMMAND-POLICY-v1.md) |
| Validation runners | [FORGE-WORDPRESS-VALIDATION-RUNNER-ARCHITECTURE-v1.md](FORGE-WORDPRESS-VALIDATION-RUNNER-ARCHITECTURE-v1.md) |
| Visual regression | [FORGE-WORDPRESS-VISUAL-REGRESSION-DESIGN-v1.md](FORGE-WORDPRESS-VISUAL-REGRESSION-DESIGN-v1.md) |
| Security validation | [FORGE-WORDPRESS-SECURITY-VALIDATION-DESIGN-v1.md](FORGE-WORDPRESS-SECURITY-VALIDATION-DESIGN-v1.md) |
| Packaging | [FORGE-WORDPRESS-PACKAGING-AND-RELEASE-DESIGN-v1.md](FORGE-WORDPRESS-PACKAGING-AND-RELEASE-DESIGN-v1.md) |
| Pilot tooling profile | [FORGE-WORDPRESS-PILOT-TOOLING-PROFILE-v1.md](FORGE-WORDPRESS-PILOT-TOOLING-PROFILE-v1.md) |
| Decision record | [reports/FORGE-WORDPRESS-FW-03-TOOLING-DECISION-RECORD-v1.md](reports/FORGE-WORDPRESS-FW-03-TOOLING-DECISION-RECORD-v1.md) |
| FW-04 input | [reports/FORGE-WORDPRESS-FW-04-PILOT-INTAKE-INPUT-v1.md](reports/FORGE-WORDPRESS-FW-04-PILOT-INTAKE-INPUT-v1.md) |

---

## FW-01 methodology pack

| Area | Document |
|------|----------|
| Capabilities | [FORGE-WORDPRESS-CAPABILITY-MODEL-v1.md](FORGE-WORDPRESS-CAPABILITY-MODEL-v1.md) |
| Implementation modes | [FORGE-WORDPRESS-IMPLEMENTATION-MODES-v1.md](FORGE-WORDPRESS-IMPLEMENTATION-MODES-v1.md) |
| Artifacts | [FORGE-WORDPRESS-PROJECT-ARTIFACT-MODEL-v1.md](FORGE-WORDPRESS-PROJECT-ARTIFACT-MODEL-v1.md) |
| Roles | [FORGE-WORDPRESS-ROLE-AND-AGENT-MODEL-v1.md](FORGE-WORDPRESS-ROLE-AND-AGENT-MODEL-v1.md) |
| Tooling (classes) | [FORGE-WORDPRESS-TOOLING-ARCHITECTURE-v1.md](FORGE-WORDPRESS-TOOLING-ARCHITECTURE-v1.md) |
| Validation WV0–WV9 | [FORGE-WORDPRESS-VALIDATION-ARCHITECTURE-v1.md](FORGE-WORDPRESS-VALIDATION-ARCHITECTURE-v1.md) |
| Human control | [FORGE-WORDPRESS-HUMAN-CONTROL-MODEL-v1.md](FORGE-WORDPRESS-HUMAN-CONTROL-MODEL-v1.md) |
| Handoff boundaries | [FORGE-WORDPRESS-HANDOFF-BOUNDARIES-v1.md](FORGE-WORDPRESS-HANDOFF-BOUNDARIES-v1.md) |
| Research adaptation | [FORGE-WORDPRESS-RESEARCH-ADAPTATION-REGISTER-v1.md](FORGE-WORDPRESS-RESEARCH-ADAPTATION-REGISTER-v1.md) |
| Research register | [FORGE-WORDPRESS-RESEARCH-REGISTER-v1.md](FORGE-WORDPRESS-RESEARCH-REGISTER-v1.md) |

---

## Historical seed

Internal agent seed **AG-WP-001** remains the LOC-ZONE foundation source:

[workspaces/website-factory-operations/internal-agent-seeds/AG-WP-001-forge-wordpress/](../../../../workspaces/website-factory-operations/internal-agent-seeds/AG-WP-001-forge-wordpress/)

Research Base v1: [research/README.md](../../../../workspaces/website-factory-operations/internal-agent-seeds/AG-WP-001-forge-wordpress/research/README.md)

---

## Parent

[Website Factory README](../../README.md) · [OPERATIONAL-INDEX](../../OPERATIONAL-INDEX.md) · registry `mars-website-factory`

---

*Foundation + architecture v1. Not runtime. Not a registered agent. Not production WordPress capability.*
