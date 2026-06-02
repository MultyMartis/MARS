# External Access Runtime (EAR)

**Classification:** MARS shared infrastructure — **documentation only**  
**Version:** v1 foundation  
**Status:** architecture and contracts; **not** a running system in this repository

---

## What EAR is

**External Access Runtime (EAR)** is the designated **supervised access acquisition layer** for external systems (hosted sites, CMS admin, file hosts, database exports).

EAR:

- **Collects** evidence into a **Snapshot Package**
- Operates under **human approval (HITL)**
- Defaults to **read-only**

EAR does **not**:

- Analyze site business logic
- Make remediation decisions
- Modify production or test sites (v1)
- Run autonomously without operator control

---

## Document map

| Document | Purpose |
|----------|---------|
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Navigation hub |
| [EAR-CHARTER-v1.md](EAR-CHARTER-v1.md) | Mission and authority |
| [EAR-SCOPE-v1.md](EAR-SCOPE-v1.md) | In-scope capabilities (conceptual) |
| [EAR-NON-GOALS-v1.md](EAR-NON-GOALS-v1.md) | Explicit exclusions |
| [EAR-GLOSSARY-v1.md](EAR-GLOSSARY-v1.md) | Terms |
| [EAR-ARCHITECTURE-v1.md](EAR-ARCHITECTURE-v1.md) | Layer model |
| [EAR-MODES-v1.md](EAR-MODES-v1.md) | Mode 0–3 semantics |
| [EAR-CONNECTION-TYPES-v1.md](EAR-CONNECTION-TYPES-v1.md) | Connector families |
| [EAR-SNAPSHOT-CONTRACT-v1.md](EAR-SNAPSHOT-CONTRACT-v1.md) | Output package |
| [EAR-SECURITY-MODEL-v1.md](EAR-SECURITY-MODEL-v1.md) | Secrets, HITL, read-only |
| [EAR-ROADMAP-v1.md](EAR-ROADMAP-v1.md) | Phased evolution (no dates) |

---

## Relationship to other MARS layers

| Layer | Relationship |
|-------|----------------|
| [shared/external-access-patterns/](../external-access-patterns/README.md) | Channel **patterns** (browser, FTP, PMA) — EAR **orchestrates acquisition semantics**, not duplicate pattern text |
| [projects/ocpilot/](../../projects/ocpilot/) | First consumer candidate — SITE-001 paused pending EAR direction |
| [projects/wpilot/](../../projects/wpilot/) | Future consumer — **not modified** in EAR v1 foundation |
| [governance/external-system-boundaries.md](../../governance/external-system-boundaries.md) | Boundary discipline — EAR stays external-facing, human-operated |

---

## First operational evidence

Freeze and lessons: [projects/ocpilot/freeze/site-001-pre-runtime-bridge/](../../projects/ocpilot/freeze/site-001-pre-runtime-bridge/)

---

## Truth statement

No EAR runtime, connectors, scripts, or automation are claimed to exist in-repo unless future commits add them under explicit human charter. This folder is **document-first architecture only**.
