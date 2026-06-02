# EAR Runtime Charter v1

**Type:** Engineering program charter (foundation) — **not** implementation authorization  
**Date:** 2026-06-02  
**Program:** EAR Runtime Program v1  
**Status:** Foundation charter — **Engineering Charter** (implementation) still required before code

---

## Mission

Deliver **human-operated, contract-conformant** acquisition helpers that implement the frozen EAR Architecture for **Mode 2 Connected Read-Only** (and supporting offline assembly paths where in backlog), producing **Evidence Packages** and **Published Snapshots** for downstream consumers — without replacing consumer analysis or bypassing HITL gates.

---

## Purpose

| Goal | Description |
|------|-------------|
| **Implement contracts** | Turn normative architecture ([shared/external-access-runtime/](../../shared/external-access-runtime/)) into chartered connectors and tooling |
| **Enable PILOT-001 path** | Support SITE-001 TEST connected acquisition when **Execution** is separately authorized |
| **Separate layers** | Keep acquisition mechanics out of OCPilot/WPilot/Factory codebases |
| **Status honesty** | Record implementation truth in [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) |

---

## Consumers (who uses Runtime output)

Runtime **produces** artifacts; consumers **analyze** them.

| Consumer | Platform | Runtime relationship |
|----------|----------|----------------------|
| **OCPilot** | OpenCart / ocStore | Primary v1 reference consumer — published snapshots for audit (e.g. SITE-001 Run 5) |
| **WPilot** | WordPress | **Future** — no v1 implementation commitment; architecture references WPilot for harmonization only |
| **Website Factory** | Multi-site production | **SAFE UNKNOWN** — may consume snapshots later; not owned by Runtime |
| **Landing Pilot** | Landing / static | **SAFE UNKNOWN** — future |
| **Operator** | Human | Runs helpers, approves Validate/Publish, holds credentials |

See architecture: [EAR-FUTURE-CONSUMERS-v1.md](../../shared/external-access-runtime/EAR-FUTURE-CONSUMERS-v1.md), [EAR-OCPILOT-INTEGRATION-v1.md](../../shared/external-access-runtime/EAR-OCPILOT-INTEGRATION-v1.md).

---

## Expected outcomes (Runtime Program success)

When the program is **mature for v1 pilot support** (not claimed at foundation):

1. **R1–R5** backlog items implemented per [EAR-RUNTIME-BACKLOG-v1.md](EAR-RUNTIME-BACKLOG-v1.md) and authoritative architecture backlog.
2. PILOT-001 can execute connected read-only acquisition under **Execution Authorization** with contract-shaped logs and artefacts.
3. Published Level 1 OpenCart snapshot is **OCPilot intake compatible** per consumer guide.
4. No credentials in git; fail-closed behavior per connector failure model.
5. Architecture contracts unchanged without **Architecture Amendment Charter**.

---

## Relationship to EAR Architecture

| Rule | Detail |
|------|--------|
| **Authority** | Architecture layer is **frozen** — [freeze/EAR-RUNTIME-TRANSITION-v1/](../../shared/external-access-runtime/freeze/EAR-RUNTIME-TRANSITION-v1/) |
| **Conformance** | Runtime implements; architecture defines **what** and **why** |
| **Amendments** | Normative changes require **Architecture Amendment Charter** — not runtime PRs |
| **Location** | Architecture docs remain in `shared/external-access-runtime/` |
| **Boundary** | [EAR-RUNTIME-BOUNDARY-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BOUNDARY-v1.md) |

---

## Relationship to OCPilot

| Aspect | Boundary |
|--------|----------|
| **Invariant** | `Operator → EAR Runtime → Published Snapshot → OCPilot` |
| **OCPilot does not** | Invoke connectors, live-pull evidence, or replace EAR acquisition |
| **EAR Runtime does not** | Run audit diffs, Run 5 logic, or operations-layer deployment |
| **Integration doc** | [EAR-OCPILOT-INTEGRATION-v1.md](../../shared/external-access-runtime/EAR-OCPILOT-INTEGRATION-v1.md) |
| **Bridge context** | [projects/ocpilot/freeze/site-001-pre-runtime-bridge/](../ocpilot/freeze/site-001-pre-runtime-bridge/) |

First reference pilot: **PILOT-001** (architecture package under shared `pilots/`).

---

## Relationship to WPilot

| Aspect | Boundary |
|--------|----------|
| **v1 focus** | OpenCart / Mode 2 SFTP path for OCPilot reference pilot |
| **WPilot** | Documented as **future consumer** — WordPress connectors and mapping **not** in Runtime v1 backlog |
| **Shared contract** | Generic snapshot/evidence semantics may later harmonize — Phase 4+ architecture roadmap |
| **No merge** | Runtime v1 does not modify WPilot repositories |

---

## Relationship to future consumers

Runtime v1 engineering is **OpenCart-first** because architecture maturity and PILOT-001 align with OCPilot. Future consumers (Factory, Landing Pilot, additional CMS) consume the **same published snapshot contract** where possible; platform-specific acquisition expands via **future runtime charters** and architecture amendments — not implicit scope in v1.

---

## Engineering charter (next human gate)

This document is the **foundation charter** for project placement. **Implementation** requires a separate human-approved **EAR Runtime v1 Engineering Charter** that:

- References freeze date and `EAR-RUNTIME-TRANSITION-v1`
- Names in-scope backlog items (typically starting with **R1**)
- Defines language/stack, repo layout under `runtime/`, and credential handling
- States PILOT-001 Execution remains **not authorized** until separate gate

Recommended sources: [EAR-NEXT-STAGE-v1.md](../../shared/external-access-runtime/freeze/EAR-RUNTIME-TRANSITION-v1/EAR-NEXT-STAGE-v1.md), [EAR-RUNTIME-HANDOFF-v1.md](../../shared/external-access-runtime/freeze/EAR-RUNTIME-TRANSITION-v1/EAR-RUNTIME-HANDOFF-v1.md).

---

## Truth statement

**No** runtime code, connector, or live access session exists in this project at foundation. Charter existence ≠ Runtime Program **STARTED** per [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md).
