# Agent card — WordPress Implementation Agent (v1)

**Documentation-first:** **`draft`** — registered agent foundation in MARS Agent Registry §4.1; **not** autonomous runtime, **not** a deployed agent service, **not** production WordPress administrator. Execution is **human + Cursor/Codex** per AG-WP-001 contracts and [FORGE-WORDPRESS-IMPLEMENTATION-SPECIALIST-v1.md](../../projects/mars-website-factory/subsystems/forge-wordpress/capability/primary-specialist/FORGE-WORDPRESS-IMPLEMENTATION-SPECIALIST-v1.md).

---

| Field | Value |
|--------|--------|
| **agent_id** | `wordpress_implementation_agent` |
| **legacy_seed_id** | `AG-WP-001` |
| **display_name** | WordPress Implementation Agent |
| **status** | `draft` (registered FW-07A; **not** `active`; **not** runtime-active) |
| **layer** | Website Factory / Forge WordPress |
| **parent_system** | `mars_website_factory` |
| **subsystem** | `forge_wordpress` |

---

## capability_links

- [AG-WP-001 agent pack](../../projects/mars-website-factory/subsystems/forge-wordpress/agents/README.md) — canonical contracts
- [AG-WP-001 agent card (subsystem)](../../projects/mars-website-factory/subsystems/forge-wordpress/agents/AG-WP-001-WORDPRESS-IMPLEMENTATION-AGENT-CARD-v1.md)
- [Forge WordPress OPERATIONAL-INDEX](../../projects/mars-website-factory/subsystems/forge-wordpress/OPERATIONAL-INDEX.md)
- [FORGE-WORDPRESS-IMPLEMENTATION-SPECIALIST-v1.md](../../projects/mars-website-factory/subsystems/forge-wordpress/capability/primary-specialist/FORGE-WORDPRESS-IMPLEMENTATION-SPECIALIST-v1.md) — prompt-driven profile
- [Agent registry §4.1](../registry.md)

---

## primary_responsibilities

- Convert operator-approved frontend into maintainable WordPress implementation under explicit contracts
- Inspect approved frontend handoff; propose architecture (mode, theme/functionality split, content model)
- Implement approved theme/plugin artifacts locally with validation and rollback checkpoints
- Prepare operator review and handoff packages

---

## non_goals

- Unrestricted production WordPress administration
- Autonomous deployment, plugin installation, or SQL/filesystem operations
- Visual redesign or modification of approved frontend source
- Self-approval of high-risk output
- Runtime activation without FW-07B+ charter

---

## upstream_inputs

- Frontend Production Pass; approved Git commit; [AG-WP-001-APPROVED-FRONTEND-INPUT-CONTRACT-v1.md](../../projects/mars-website-factory/subsystems/forge-wordpress/agents/AG-WP-001-APPROVED-FRONTEND-INPUT-CONTRACT-v1.md)
- Website Factory handoff FW-C-01; FW-06B intake when authorized

---

## downstream_outputs

- WordPress theme/plugin source; content model; QA package — [AG-WP-001-WORDPRESS-IMPLEMENTATION-OUTPUT-CONTRACT-v1.md](../../projects/mars-website-factory/subsystems/forge-wordpress/agents/AG-WP-001-WORDPRESS-IMPLEMENTATION-OUTPUT-CONTRACT-v1.md)

---

## permissions

| Scope | Authority |
|-------|-----------|
| Production mutation | **NONE** |
| Local source (R2) | Plan + checkpoint + operator |
| Local runtime (R3) | Explicit operator approval |
| MLI structural changes | **NONE** |

---

## pilot_eligibility

**CONDITIONAL** — FP-0002 blocked until Frontend Production Pass + FW-06B. See [AG-WP-001-FP-0002-PILOT-READINESS-MAP-v1.md](../../projects/mars-website-factory/subsystems/forge-wordpress/agents/AG-WP-001-FP-0002-PILOT-READINESS-MAP-v1.md).

---

## changelog

| Date | Note |
|------|------|
| 2026-06-24 | FW-07A — initial registration as `draft`; foundation contracts |

---

*Catalog card v1 — mirrors subsystem AG-WP-001 pack.*
