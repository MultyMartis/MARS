# Forge WordPress — Implementation Capability Pack

**Version:** v1  
**Stage:** FW-04  
**Date:** 2026-06-22  
**Type:** Prompt-driven human-supervised execution pack for Cursor Agent and Web-GPT

---

## What this is

The **implementation capability home** for Forge WordPress. It contains reusable specialist profiles, skills, validators, protocols, and task templates that operators invoke through Cursor Agent — **not** an autonomous runtime.

```text
approved frontend
    → specialist + skills + validators
    → local WordPress implementation
    → validation
    → release candidate
    → WPilot handoff
```

Human supervision is **required** at every gate.

---

## What this is not

- Not an autonomous agent runtime
- Not a production deployment system
- Not a registered MARS agent (`AG-WP-001` remains seed)
- Not a `project_id` container
- Not WordPress core or vendor distribution

---

## Start here

| Document | Purpose |
|----------|---------|
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Capability navigation and readiness |
| [primary-specialist/FORGE-WORDPRESS-IMPLEMENTATION-SPECIALIST-v1.md](primary-specialist/FORGE-WORDPRESS-IMPLEMENTATION-SPECIALIST-v1.md) | Primary working profile |
| [protocols/FORGE-WORDPRESS-SPECIALIST-EXECUTION-CONTRACT-v1.md](protocols/FORGE-WORDPRESS-SPECIALIST-EXECUTION-CONTRACT-v1.md) | Mandatory execution cycle |
| [task-templates/FORGE-WORDPRESS-CURSOR-TASK-TEMPLATE-v1.md](task-templates/FORGE-WORDPRESS-CURSOR-TASK-TEMPLATE-v1.md) | Reusable Cursor task shell |
| [task-templates/FORGE-WORDPRESS-PROMPT-PACK-v1.md](task-templates/FORGE-WORDPRESS-PROMPT-PACK-v1.md) | Ready prompt starters |
| [FORGE-WORDPRESS-CAPABILITY-READINESS-MATRIX-v1.md](FORGE-WORDPRESS-CAPABILITY-READINESS-MATRIX-v1.md) | Readiness status |

---

## Pack structure

```text
capability/
├── README.md
├── OPERATIONAL-INDEX.md
├── FORGE-WORDPRESS-CAPABILITY-READINESS-MATRIX-v1.md
├── primary-specialist/
├── skills/           FW-SK-01 … FW-SK-14
├── validators/       FW-V-01 … FW-V-07
├── protocols/
├── task-templates/
└── reports/
```

---

## Lifecycle

```text
FOUNDATION / PRE-OPERATIONAL
```

Prompt-driven capability is **DOCUMENTED** after FW-04. **OPERATIONAL** status requires FW-05 synthetic validation pass.

---

## Parent subsystem

[../README.md](../README.md) · [../OPERATIONAL-INDEX.md](../OPERATIONAL-INDEX.md) · [../roadmap.md](../roadmap.md)

---

*Capability pack v1 — FW-04 Implementation Capability Construction.*
