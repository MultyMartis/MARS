# Forge WordPress — Architectural Decisions v1

**Document type:** Decision record (FW-01 core)  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-01

**Classification key:** ADOPT | ADAPT | DEFER | REJECT | SAFE UNKNOWN

---

## 4.1 Theme vs functionality

| Field | Decision |
|-------|----------|
| **Decision** | **ADOPT** — presentation belongs to theme; persistent content model and business functionality must not depend on theme activation. |
| **Research evidence** | Plugin Handbook CPT-in-plugin; 10up scaffold; VIP Git-only custom code |
| **MARS evidence** | [FORGE-WORDPRESS-SCOPE-AND-BOUNDARIES-v1.md](FORGE-WORDPRESS-SCOPE-AND-BOUNDARIES-v1.md); ecosystem position |
| **Adaptation** | Proportionality rule: simple brochure sites may use a **minimal** functionality plugin (or must-use plugin) — custom plugin **not mandatory** when content model is trivial and documented in WAD |
| **Resulting rule** | **R-TF-01:** Theme = presentation templates, assets, enqueue, template hierarchy. **R-TF-02:** CPT, taxonomies, ACF registrations, business hooks → functionality plugin (or chartered must-use plugin). **R-TF-03:** Complexity must match project — no boilerplate plugin for single-page static sites without editorial model. |

---

## 4.2 Classic, hybrid, and block architecture

| Field | Decision |
|-------|----------|
| **Decision** | **ADAPT** — no single global mode; per-project WAD selects per-section surfaces. |
| **Research evidence** | Three production models (block / classic / theme+plugin); Block Bindings; Interactivity API |
| **MARS evidence** | Factory Gulp HTML-first pipeline; PIXEL_PERFECT mode; FP-0002 pilot context |
| **Adaptation** | Factory-native default = **classic/hybrid theme** carrying approved frontend assets; block surfaces only where WAD justifies |
| **Resulting rule** | **R-ARCH-01:** WAD must include decision matrix scores (see implementation modes §6). **R-ARCH-02:** Full block theme (FSE) requires explicit WAD waiver — not default. **R-ARCH-03:** Section-level mapping in `BLOCK-TO-WP-MAPPING` is mandatory. |

**Decision matrix criteria (WAD required):**

| Criterion | Weight notes |
|-----------|--------------|
| Visual fidelity | High for PIXEL_PERFECT |
| Editor needs | Drives ACF vs blocks |
| Content reuse | Favors functionality plugin + ACF |
| Project complexity | Higher → stronger separation |
| Hosting | Shared hosting favors lean PHP theme |
| Maintenance | Favors version-controlled JSON + Git |
| WPilot compatibility | Favors Factory-native custom |
| Team competence | Windows + Cursor + Gulp baseline |

---

## 4.3 ACF position

| Field | Decision |
|-------|----------|
| **Decision** | **ADAPT** — ACF is **preferred pragmatic layer**, not mandatory system-wide law. |
| **Research evidence** | ACF Local JSON, Blocks, WP-CLI sync, Abilities integration |
| **MARS evidence** | No ACF in repo yet; human-supervised greenfield; shared hosting typical |
| **Adaptation** | Mode A/B default to ACF when editorial fields needed; core-only meta acceptable for trivial models with WAD note |
| **Resulting rule** | **R-ACF-01:** ACF Local JSON **required** when ACF is used. **R-ACF-02:** ACF schema version-controlled in functionality plugin or `acf-json/` path declared in spec. **R-ACF-03:** Projects without ACF must document alternative in WAD (core meta, block attributes only). **R-ACF-04:** ACF Pro dependency declared in plugin register — human approval. |

---

## 4.4 Version control

| Field | Decision |
|-------|----------|
| **Decision** | **ADOPT** — mandatory version control for all implementation artifacts. |
| **Research evidence** | VIP Git-only; ACF Local JSON; PR-gated QA |
| **MARS evidence** | GitGuard patterns; MARS Git checkpoint discipline |
| **Adaptation** | WordPress implementation may live in project repo under LOC-ZONE or dedicated repo — layout FW-02 |
| **Resulting rule** | **R-VC-01:** Theme code in Git. **R-VC-02:** Custom plugin code in Git. **R-VC-03:** ACF schema in Git. **R-VC-04:** Build config (npm/composer) in Git. **R-VC-05:** Implementation specifications and validation results in Git (docs/ or reports/). **R-VC-06:** Database and uploads are **not** SoT — export/import via chartered process only. |

---

## 4.5 Dev and production boundary

| Field | Decision |
|-------|----------|
| **Decision** | **ADOPT** — local/DEV first; production mutation belongs to WPilot or separately chartered release. |
| **Research evidence** | Sandbox-first; assistive vs runtime agent distinction |
| **MARS evidence** | WPilot DEV-only RC5; no production credentials in repo |
| **Adaptation** | Windows local stack (Local WP, wp-env, Playground) — tooling choice deferred FW-03 |
| **Resulting rule** | **R-ENV-01:** No direct production coding in Forge WordPress. **R-ENV-02:** No unrestricted production credentials in agent/skill context. **R-ENV-03:** L8 implementation = local/DEV only. **R-ENV-04:** Deployment = WPilot handoff or operator charter — not autonomous. **R-ENV-05:** Content/media import on production = WPilot or operator with backup-first. |

---

## 4.6 Admin UX — curated editor

| Field | Decision |
|-------|----------|
| **Decision** | **ADOPT** — curated editor principle. |
| **Research evidence** | Content-only editing; block locking; DataForm/DataViews |
| **MARS evidence** | Factory freeze discipline; operator visual approval law |
| **Adaptation** | Editorial freedom is **project-scoped** in ADMIN-UX-MAP — default = minimal editable surface |
| **Resulting rule** | **R-UX-01:** Only declared fields/sections are editable. **R-UX-02:** Structure and visual constraints protected (locking, ACF placement, disallow arbitrary blocks where not chartered). **R-UX-03:** Editor freedom **opt-in** per WAD — never default-open. **R-UX-04:** WPilot handoff must include frozen vs editable zone map. |

---

## Additional FW-01 decisions

### Agent vs skill family

| Field | Decision |
|-------|----------|
| **Decision** | **ADAPT** — defer agent registration; skill-first for FW-02–FW-04 |
| **Resulting rule** | **R-AGENT-01:** `AG-WP-001` remains internal seed. **R-AGENT-02:** One primary implementation specialist agent is **candidate** for FW-05 pilot charter — not registered in FW-01. |

### Source repository model

| Field | Decision |
|-------|----------|
| **Decision** | **DEFER** detailed layout to FW-02 Theme/Functionality standards |
| **Resulting rule** | **R-REPO-01:** Minimum = separable theme + functionality plugin directories; mono-repo acceptable for pilots. |

### Dev environment stack

| Field | Decision |
|-------|----------|
| **Decision** | **DEFER** tool selection to FW-03 — candidate classes in tooling architecture |
| **Resulting rule** | **R-DEV-01:** Must support Windows; must not require Docker as mandatory (ADAPT from research). |

### WordPress Abilities / MCP

| Field | Decision |
|-------|----------|
| **Decision** | **DEFER** — sandbox/dev only if adopted in FW-03+ |
| **Resulting rule** | **R-MCP-01:** No production Abilities/MCP exposure without separate security charter. |

### FP-0002 eligibility

| Field | Decision |
|-------|----------|
| **Decision** | **SAFE UNKNOWN** — pilot eligibility remains conditional on frontend readiness + operator charter (FW-04) |
| **Resulting rule** | **R-PILOT-01:** FP-0002 is probable pilot evidence only; FW-01 does not authorize implementation. |

---

## Rejected approaches (FW-01)

| Approach | Classification | Reason |
|----------|----------------|--------|
| Page builders as Factory-native default | **REJECT** | Incompatible with Gulp pixel pipeline ownership |
| Autonomous production deploy | **REJECT** | MARS execution model |
| Theme-embedded CPT for portable content | **REJECT** | WordPress + research consensus |
| Headless as default Mode A | **REJECT** | WPilot + shared hosting alignment |
| Enterprise CI/Docker as mandatory | **REJECT** | Unproven MARS operator need — candidate only |

---

## Related documents

- [FORGE-WORDPRESS-RESEARCH-ADAPTATION-REGISTER-v1.md](FORGE-WORDPRESS-RESEARCH-ADAPTATION-REGISTER-v1.md)
- [reports/FORGE-WORDPRESS-FW-01-DECISION-RECORD-v1.md](reports/FORGE-WORDPRESS-FW-01-DECISION-RECORD-v1.md)

---

*Architectural decisions v1 — FW-01 baseline. FW-02 converts to standards and contracts.*
