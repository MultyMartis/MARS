# Forge WordPress — Capability Model v1

**Document type:** Capability registry (methodology)  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-01

**Rule:** FW-01 defines capabilities and future ownership — **no skills or agents are created**.

---

## 1. Status vocabulary

| Status | Meaning |
|--------|---------|
| **METHODOLOGY ONLY** | Documented process; human executes manually |
| **FUTURE SKILL** | Reusable Cursor skill candidate (FW-02+ design) |
| **FUTURE AGENT** | Registered agent candidate — requires promotion charter |
| **VALIDATOR** | Independent validation role — must not implement same artifact |
| **HUMAN ONLY** | No automation target in Phase 1 |
| **DEFERRED** | Explicitly postponed pending evidence or FW-03 |

---

## 2. First-level capabilities

| Capability | FW-01 status | Risk | Human approval | Future owner |
|------------|--------------|------|----------------|--------------|
| Inspect frontend package | METHODOLOGY ONLY | Low | Report review | FUTURE SKILL: `fw-frontend-package-inspect` |
| Build WordPress implementation plan | METHODOLOGY ONLY | Medium | **Required** (WAD gate) | Forge WordPress Architect (human) |
| Classify editable regions | METHODOLOGY ONLY | Medium | **Required** | FUTURE SKILL: `fw-editable-regions-classify` |
| Design content model | METHODOLOGY ONLY | **High** | **Required** | Content Modeler (human) + FUTURE SKILL assist |
| Map frontend blocks to WordPress surfaces | METHODOLOGY ONLY | Medium | **Required** | FUTURE SKILL: `fw-block-wp-mapping` |
| Design theme architecture | METHODOLOGY ONLY | Medium | **Required** | Theme Implementation Specialist |
| Design functionality plugin boundary | METHODOLOGY ONLY | Medium | **Required** | Theme Implementation Specialist |
| Design ACF architecture | METHODOLOGY ONLY | Medium | **Required** (if ACF mode) | Content Modeler |
| Design CPT/taxonomy model | METHODOLOGY ONLY | **High** | **Required** | Content Modeler |
| Design admin UX | METHODOLOGY ONLY | Medium | **Required** | Admin UX Specialist |
| Prepare plugin register | METHODOLOGY ONLY | **High** | **Required** | Forge WordPress Architect |
| Generate implementation specification | METHODOLOGY ONLY | Medium | **Required** (blocking) | FUTURE SKILL: `fw-impl-spec-compile` |
| Implement locally (theme/plugin code) | DEFERRED | **High** | **Required** per change set | FUTURE AGENT: primary implementation specialist |
| Validate implementation (WV chain) | METHODOLOGY ONLY | **High** | **Required** at WV blockers | VALIDATOR roles + FUTURE SKILL runners |
| Compare frontend and WordPress rendering | METHODOLOGY ONLY | Medium | **Required** (PIXEL_PERFECT) | Visual Parity Validator |
| Package release candidate | DEFERRED | Medium | **Required** | FUTURE SKILL: `fw-release-package` |
| Prepare WPilot handoff | METHODOLOGY ONLY | **High** | **Required** (blocking) | WPilot Handoff Reviewer (HUMAN ONLY gate) |

---

## 3. Capability clusters (minimal system)

Research and MARS alignment converge on a **minimal** model:

```text
One primary implementation specialist (future — human first)
  + specialized reusable skills (mapping, spec compile, QA runners)
  + independent validators (must not self-validate)
  + human approval at every gate
```

| Cluster | Capabilities | Phase 1 |
|---------|--------------|---------|
| **Architecture** | Plan, WAD, plugin register, handoff prep | METHODOLOGY ONLY |
| **Modeling** | Content model, ACF, CPT, admin UX | METHODOLOGY ONLY |
| **Implementation** | Local code generation | DEFERRED → FW-05 pilot |
| **Validation** | WV0–WV9 | METHODOLOGY ONLY + VALIDATOR |
| **Operations bridge** | WPilot handoff | HUMAN ONLY reviewer |

---

## 4. Explicit non-capabilities (FW-01)

| Not a Forge WordPress capability | Owner |
|----------------------------------|-------|
| Frontend design/implementation | Website Factory |
| Production deployment | WPilot / operator |
| Live site maintenance | WPilot |
| Autonomous agent runtime | **EXCLUDED** |
| MARS Forge overlay behavior | MARS Forge agent |

---

## 5. Risk classes

| Class | Examples | Default control |
|-------|----------|-----------------|
| **R1 Low** | Manifest inspection | Report only |
| **R2 Medium** | Template mapping, theme structure | Human approval |
| **R3 High** | Content model, plugins, security, handoff | Blocking gate + independent validator where applicable |
| **R4 Critical** | Production access, DB migration, credential use | **PROHIBITED** in Forge WordPress |

---

## 6. Related documents

- [FORGE-WORDPRESS-ROLE-AND-AGENT-MODEL-v1.md](FORGE-WORDPRESS-ROLE-AND-AGENT-MODEL-v1.md)
- [FORGE-WORDPRESS-ARCHITECTURE-v1.md](FORGE-WORDPRESS-ARCHITECTURE-v1.md)
- [FORGE-WORDPRESS-HUMAN-CONTROL-MODEL-v1.md](FORGE-WORDPRESS-HUMAN-CONTROL-MODEL-v1.md)

---

*Capability model v1 — no skills or agents registered.*
