# Decision — EAR Runtime Placement v1

**Type:** Architecture decision record (ADR)  
**Date:** 2026-06-02  
**Status:** **ACCEPTED**  
**Decision makers:** Human operator (MARS Lane B)  
**Context:** EAR Architecture Program **COMPLETE**; EAR Runtime Program **NOT STARTED**; runtime engineering must not begin without explicit placement.

---

## Problem statement

EAR Runtime will become an **engineering system** (connectors, evidence tooling, snapshot build/publish, validation helpers, pilots, releases). Before any implementation, MARS must decide **where** that system lives in the repository and how it relates to the frozen architecture tree in `shared/external-access-runtime/`.

---

## Alternatives considered

### A — `shared/external-access-runtime/runtime/`

| Pros | Cons |
|------|------|
| Colocated with contracts | Blurs **frozen architecture** with **mutable implementation** |
| Short paths to design docs | `shared/` reads as cross-cutting **governance/design** in MARS |
| | Harder to grant distinct roadmap, backlog state, releases |
| | Risk of architecture creep via code PRs in same tree |

### B — `C:\AI MARS STORAGE` (external tools tree)

| Pros | Cons |
|------|------|
| Matches bulk snapshot storage pattern | **Outside git** — poor traceability for source |
| Keeps secrets/artefacts off-repo | Not a MARS **project** — weak OPERATIONAL-INDEX integration |
| | Mixes **runtime source** with **consumer bulk data** |
| | No standard Lane B project charter placement |

### C — `projects/ear-runtime/` **(selected)**

| Pros | Cons |
|------|------|
| Clear **program boundary** parallel to `projects/ocpilot/`, `projects/mars-survivability/` | Requires cross-links to architecture (mitigated) |
| Room for roadmap, state, pilots, `runtime/` code | Two locations for "EAR" (documented split) |
| Architecture remains frozen in `shared/` | |
| Implementation honesty in dedicated STATE file | |
| Future tooling/releases under one OPERATIONAL-INDEX | |

---

## Decision

**Place EAR Runtime v1 engineering under `projects/ear-runtime/`.**

Architecture and governance remain authoritative in **`shared/external-access-runtime/`**.

---

## Reasoning

1. **Layer separation** — [EAR-RUNTIME-BOUNDARY-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BOUNDARY-v1.md) defines architecture (frozen) vs runtime (engineering). Separate top-level project enforces that socially and structurally.
2. **MARS project convention** — Engineering systems with roadmaps and implementation live under `projects/`, not `shared/`.
3. **Status honesty** — A dedicated [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) avoids implying runtime exists because architecture docs exist nearby.
4. **Pilot and release evolution** — Runtime execution pilots and versioned helpers need space without amending architecture freeze folders.
5. **External storage is for artefacts, not source** — `X:\AI MARS STORAGE\` remains appropriate for snapshots and quarantine per [EAR-STORAGE-MODEL-v1.md](../../shared/external-access-runtime/EAR-STORAGE-MODEL-v1.md), not for connector source code.

---

## Consequences

| Area | Consequence |
|------|-------------|
| **Architecture** | No normative move; backlog in `shared/.../EAR-RUNTIME-BACKLOG-v1.md` stays **authoritative** |
| **Runtime** | All future implementation defaults to `projects/ear-runtime/runtime/` unless charter states otherwise |
| **Indexes** | [shared/.../OPERATIONAL-INDEX.md](../../shared/external-access-runtime/OPERATIONAL-INDEX.md) links to runtime project; runtime index links back |
| **Freeze** | [freeze/FOUNDATION-START-v1/](freeze/FOUNDATION-START-v1/) records project birth |
| **Consumers** | OCPilot/WPilot unchanged — still consume published snapshots |
| **Agents** | AGENT tasks for runtime engineering should scope to `projects/ear-runtime/` + chartered paths |

---

## Future review triggers

Revisit this decision if **any** of the following occur:

| Trigger | Possible action |
|---------|-----------------|
| Multiple runtime platforms need separate repos (EAR vs WPilot runtime) | Split `projects/` or submodule charter |
| Runtime becomes large multi-language monorepo | Subfolder ADR under `runtime/` |
| Architecture and runtime must ship version-locked bundles | Document sync versioning — still keep layers separate |
| Org policy mandates all `shared/` implementations | Re-open ADR with migration plan |

**Default:** no review until Runtime v1 Engineering Charter is approved or PILOT-001 execution completes.

---

## Related documents

| Document | Path |
|----------|------|
| Runtime foundation freeze | [freeze/FOUNDATION-START-v1/README.md](freeze/FOUNDATION-START-v1/README.md) |
| Runtime charter | [EAR-RUNTIME-CHARTER-v1.md](EAR-RUNTIME-CHARTER-v1.md) |
| Architecture transition freeze | [shared/.../freeze/EAR-RUNTIME-TRANSITION-v1/](../../shared/external-access-runtime/freeze/EAR-RUNTIME-TRANSITION-v1/) |

---

## Truth statement

This decision records **repository placement** only. It does **not** authorize implementation, live access, or commits implying a running EAR runtime.
