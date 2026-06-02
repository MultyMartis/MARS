# EAR Charter v1

**Subsystem:** External Access Runtime (EAR)  
**Authority:** Human-operated MARS shared infrastructure (documentation)  
**Effective:** 2026-06-01 (foundation freeze)

---

## Mission

Provide a **supervised access acquisition layer** for external systems so consumer pilots (OCPilot, WPilot, future Factory programs) receive **standardized Snapshot Packages** instead of ad-hoc files and screenshots.

---

## Core purpose

EAR exists to **collect evidence** from external systems under operator control.

| EAR does | EAR does not |
|----------|----------------|
| Acquire files, metadata, and access logs into a snapshot | Analyze business rules or audit findings |
| Enforce read-only default in v1 | Modify site code, DB, or config |
| Reference secrets outside git | Store raw passwords in repository |
| Document connection types and risks | Imply autonomous 24/7 access |
| Support HITL approval gates | Bypass human target confirmation |

---

## Design principles

1. **Separation of concerns** — Acquisition ≠ analysis.
2. **Consumer safety** — Consumers read snapshots; never raw credential stores.
3. **Evidence honesty** — Missing data → `safe-unknown` in package, not fabrication.
4. **Mode discipline** — v1 targets **Mode 2 (Connected Read Only)**; write modes deferred.
5. **Pattern reuse** — Align with [external-access-patterns](../external-access-patterns/README.md), do not fork per pilot.
6. **No stealth automation** — Any future helper is human-chartered and visible.

---

## Authority model

| Role | Authority |
|------|-----------|
| Operator | Approves target, environment, channel, and snapshot publish |
| Human charter | Approves phase transitions (see [EAR-ROADMAP-v1.md](EAR-ROADMAP-v1.md)) |
| Consumer (e.g. OCPilot) | Consumes snapshot read-only; produces audit/analysis artifacts |
| Agent (Cursor) | Works from snapshot and repo docs only; no autonomous external login |

---

## Success criteria (v1 documentation phase)

- Layer model agreed: Operator → EAR → Snapshot → Consumer
- Snapshot contract defined
- Modes 0–2 specified; Mode 3 explicitly forbidden in v1
- Security model forbids secrets in git
- OCPilot freeze captures SITE-001 lesson without downgrading **READY FOR AUDIT**

**Not** a success criterion for v1 docs: working connectors, CLI, or CI jobs.

---

## Originating evidence

SITE-001 (Автосалон СИБКАР), Run 5 initialization — artifact acquisition identified as primary bottleneck. See [projects/ocpilot/freeze/site-001-pre-runtime-bridge/](../../projects/ocpilot/freeze/site-001-pre-runtime-bridge/LESSONS-LEARNED-v1.md).

---

## SAFE UNKNOWN

- Hosting for future EAR helpers (repo path, external tooling root) — undefined until Phase 2 charter.
- Legal/compliance review per jurisdiction — outside this charter.
