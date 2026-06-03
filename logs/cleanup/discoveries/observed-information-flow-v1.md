# Observed Information Flow v1

**Date:** 2026-06-03  
**Lane:** B — MARS Cleanup Wave 2B  
**Type:** **Observed Information Flow** (documentation observation — **not** a subsystem)

---

## Flow (observed in MARS practice)

```text
Incoming
    ↓
IdeaBox
    ↓
Program / Project
    ↓
GitGuard
    ↓
Lifecycle Log
    ↓
Registry
    ↓
Archive
```

---

## What this is

| Property | Value |
|----------|-------|
| **Nature** | Operator-observed **information gradient** across existing surfaces |
| **Evidence** | Wave 2 cross-system review, census, program intake patterns |
| **Binding** | **None** — no orchestration, no runtime routing |

---

## What this is NOT

- **Not** a MARS subsystem or `project_id`
- **Not** runtime, orchestration, or architecture layer
- **Not** mandatory pipeline — steps may be skipped (e.g. direct program creation; no IdeaBox; no lifecycle evt for minor work)
- **Not** Knowledge Center or Cold Brain automation

---

## Stage notes (one line each)

| Stage | Surface | Trust / role |
|-------|---------|--------------|
| **Incoming** | `incoming/**` | Untrusted external drops until triage |
| **IdeaBox** | `continuity/**` | Optional human-authored incubation |
| **Program / Project** | `projects/*` | Operational pack SoT after promotion |
| **GitGuard** | `mars-survivability` / GitGuard entry | Pre-mutation survivability advisory |
| **Lifecycle Log** | `logs/lifecycle-log.md` | Durable governance events (optional for all work) |
| **Registry** | `registry/project-registry.md` | Current identity rows |
| **Archive** | `archive/`, Storage Layer | Retired bulk after decision |

---

## Related evidence

- [wave-2-cross-system-review-v1.md](wave-2-cross-system-review-v1.md) §3 Operator Evidence & Intake Lane (conceptual only)
- Wave 2B alignment actions: `logs/cleanup/actions/*-alignment-v1.md`, `gitguard-registration-v1.md`

---

*Observed information flow v1 — documentation only; Wave 2B.*
