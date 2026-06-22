# Forge WordPress — Human Control Model v1

**Document type:** Operation classification matrix  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-01

**Control classes:**

| Class | Meaning |
|-------|---------|
| **AUTO-LOCAL** | May run automatically on local/DEV without per-step approval |
| **AUTO-REPORT** | Automated run; human reviews report before progression |
| **APPROVAL** | Explicit human approval before action or merge |
| **DEV-ONLY** | Permitted only in local/DEV WordPress |
| **WPILOT-ONLY** | Forge WordPress must not execute — WPilot or chartered ops |
| **OPERATOR-ONLY** | Human operator outside agent scope |
| **PROHIBITED** | Not allowed in Forge WordPress scope |

---

## Operation matrix

| Operation | Class | Notes |
|-----------|-------|-------|
| **File generation** (docs/spec) | AUTO-REPORT | Commit requires review |
| **File generation** (PHP/theme) | APPROVAL | Post-spec only; merge gated |
| **Theme modifications** | DEV-ONLY + APPROVAL | Local/DEV; human merge |
| **ACF schema changes** | DEV-ONLY + APPROVAL | JSON in Git; sync reviewed |
| **CPT/taxonomy changes** | DEV-ONLY + APPROVAL | Functionality plugin only |
| **Plugin installation** (third-party) | APPROVAL | PLUGIN-REGISTER entry required |
| **Plugin removal** | APPROVAL | Regression check |
| **Database migrations** | DEV-ONLY | Production: **WPILOT-ONLY** |
| **Search-replace** (DB) | DEV-ONLY | Production: **PROHIBITED** in Forge |
| **Content import** | DEV-ONLY + APPROVAL | Production: **WPILOT-ONLY** |
| **Media import** | DEV-ONLY + APPROVAL | Production: **WPILOT-ONLY** |
| **Deployment** | **WPILOT-ONLY** | Forge produces package only |
| **Production access** | **PROHIBITED** | No unrestricted credentials |
| **Backup** | **WPILOT-ONLY** / OPERATOR-ONLY | WPilot backup-first precedent |
| **Rollback** | **WPILOT-ONLY** / OPERATOR-ONLY | Not Forge implementation |
| **Deletion** (files, content, plugins) | APPROVAL | Production: **WPILOT-ONLY** |
| **Security configuration** | APPROVAL | Production hardening: **WPILOT-ONLY** |
| **Git commit** | AUTO-REPORT | Selective scope; operator checkpoint |
| **Git push** | OPERATOR-ONLY | Not autonomous |
| **PHPCS / tests run** | AUTO-REPORT | Block on fail per WV |
| **Screenshot diff** | AUTO-REPORT | Human sign-off WV6 |
| **WP-CLI destructive** | **PROHIBITED** without APPROVAL | `db reset`, mass delete |
| **Playground / local site reset** | AUTO-LOCAL | Sandbox-first |

---

## Escalation

| Situation | Action |
|-----------|--------|
| Agent requests production credential | **STOP** — PROHIBITED |
| Validation fail | Block next stage — no waiver without human |
| Handoff incomplete | Block FWP-11 |
| WPilot scope creep into theme dev | Reject — boundary violation |

---

## Research alignment

| Research | Classification | Rule |
|----------|----------------|------|
| Human merge / PR gate | **ADOPT** | APPROVAL on implementation merge |
| Production credential boundary | **ADOPT** | PROHIBITED production access |
| Sandbox-first | **ADOPT** | DEV-ONLY for mutations |
| Typed operations (Abilities/MCP) | **DEFER** | If adopted: DEV-ONLY + APPROVAL |

---

## Related documents

- [FORGE-WORDPRESS-HANDOFF-BOUNDARIES-v1.md](FORGE-WORDPRESS-HANDOFF-BOUNDARIES-v1.md)
- [FORGE-WORDPRESS-ROLE-AND-AGENT-MODEL-v1.md](FORGE-WORDPRESS-ROLE-AND-AGENT-MODEL-v1.md)

---

*Human control model v1 — classification only.*
