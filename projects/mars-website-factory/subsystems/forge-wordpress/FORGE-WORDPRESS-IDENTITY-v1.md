# Forge WordPress — Identity v1

**Document type:** Subsystem identity  
**Version:** v1  
**Date:** 2026-06-22  
**Lifecycle:** FOUNDATION (FW-00)

---

## Canonical identity

| Field | Value |
|-------|-------|
| **Canonical name** | Forge WordPress |
| **Operator alias** | WP Forge |
| **Class** | Website Factory subsystem |
| **Domain** | WordPress implementation |
| **Lifecycle** | **FOUNDATION** |
| **Execution model** | Human-supervised, documentation-first |
| **Parent** | MARS Website Factory (`mars-website-factory`) |
| **Upstream** | Approved Website Factory frontend package |
| **Downstream** | WPilot (controlled WordPress operations) |
| **First probable pilot** | FP-0002 — Shpigovsky.ru |
| **Pilot implementation status** | **NOT STARTED** |

---

## Status fields (honesty)

| Field | Value |
|-------|-------|
| **Runtime status** | **EXCLUDED** |
| **Autonomous deployment** | **EXCLUDED** |
| **Agent registration** | **ABSENT** — `AG-WP-001` is internal seed only |
| **project_id** | **ABSENT** — not a separate MARS project row |
| **Implementation capability** | **NOT OPERATIONAL** |

---

## Mission (foundation-level)

Forge WordPress is the Website Factory subsystem responsible for **future** transformation of approved static frontend deliverables into **production-quality WordPress implementation** (theme architecture, functionality plugin boundary, content modeling, templates, admin UX planning, QA-gated handoff).

At FOUNDATION lifecycle:

- identity, scope, ecosystem position, and research register exist;
- architecture, contracts, tooling, and pilots are **not** authorized by this document alone;
- no WordPress code, theme, plugin, or ACF schema is claimed.

---

## Distinction from similarly named entities

| Name | Relationship |
|------|--------------|
| **MARS Forge** | **Different entity** — thin frontend overlay on Gulp foundation; **not** Forge WordPress |
| **WPilot** | **Different entity** — WordPress **operations** reference implementation; downstream of Forge WordPress deliverables |
| **AG-WP-001** | **Historical/internal seed** — foundation source in LOC-ZONE; **not** a registered agent |

---

## Entity honesty statement

**Entity creation does not mean implementation capability is operational.**

Foundation documents describe **intent, boundaries, and evidence** — not shipped WordPress production, not autonomous agents, not production deployment.

---

## Canonical paths

| Artifact | Path |
|----------|------|
| Subsystem home | `projects/mars-website-factory/subsystems/forge-wordpress/` |
| Internal seed | `workspaces/website-factory-operations/internal-agent-seeds/AG-WP-001-forge-wordpress/` |
| Research Base v1 | `.../research/AG-WP-001-GLOBAL-WORDPRESS-DEVELOPMENT-RESEARCH-v1.md` |

---

## Related documents

- [FORGE-WORDPRESS-SCOPE-AND-BOUNDARIES-v1.md](FORGE-WORDPRESS-SCOPE-AND-BOUNDARIES-v1.md)
- [FORGE-WORDPRESS-ECOSYSTEM-POSITION-v1.md](FORGE-WORDPRESS-ECOSYSTEM-POSITION-v1.md)
- [FORGE-WORDPRESS-RESEARCH-REGISTER-v1.md](FORGE-WORDPRESS-RESEARCH-REGISTER-v1.md)
- [roadmap.md](roadmap.md)

---

*Identity v1 — FW-00. Not an agent card. Not a registry row.*
