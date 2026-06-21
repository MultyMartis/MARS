# MARS Website Factory - Initialization Governance

**Status:** **documented** - Website Factory initialization governance and human-supervised clean-start discipline only.  
**Not:** runtime bootstrapper, autonomous workspace cleaner, build daemon, orchestration engine, or automatic source-lock enforcement.

**Core principle:** implementation quality starts before code changes.  
A rebuild that begins from stale state, unclear source authority, or missing bootstrap evidence is already drifting.

**Related layers:** [source-interpretation-governance.md](source-interpretation-governance.md), [knowledge-provenance-governance.md](knowledge-provenance-governance.md), [operational-workflow-governance.md](operational-workflow-governance.md), [context-survivability-governance.md](context-survivability-governance.md), [implementation-reliability-governance.md](implementation-reliability-governance.md), [workspace-reset-governance.md](workspace-reset-governance.md), [reconstruction-bootstrap-governance.md](reconstruction-bootstrap-governance.md).  
**Forge findings category:** `INITIALIZATION FINDINGS`.

---

## 1. Purpose

Initialization Governance formalizes the pre-build discipline required before Forge or a frontend operator starts reconstruction, repair, or first-screen production.

It governs:

- clean-start discipline;
- implementation bootstrap;
- source-lock-before-build;
- initialization survivability;
- reconstruction initialization;
- authority initialization;
- pre-build governance;
- initialization integrity.

It does not tell a project how to build a page. It tells operators when a build is allowed to start without laundering ambiguity into implementation.

---

## 2. Required Initialization State

| Requirement | Meaning |
|-------------|---------|
| **Production mode declared** | `production_mode: PIXEL_PERFECT \| TEMPLATE_ART` in LOC-ZONE passport — **STOP** if undeclared per [website-factory-production-modes-charter-v1.md](website-factory-production-modes-charter-v1.md) |
| **Clean-start discipline** | Active workspace, source version, allowed assets, and forbidden residue are named before implementation. |
| **Implementation bootstrap** | Operator records enough initial state for another operator to reproduce the starting assumptions. |
| **Source-lock-before-build** | Active source authority is established before layout, styling, responsive, or asset decisions. |
| **Authority initialization** | Source, project pack, human decision, and existing code authority are separated. |
| **Pre-build governance** | Known constraints, unknowns, escalation triggers, and reset needs are identified before production work. |
| **Initialization survivability** | The starting state remains understandable after context compression, session handoff, or partial rebuild. |

---

## 3. Canonical Rules

- Do not start implementation from “whatever is open” without a named active source.
- Do not treat existing workspace code as source authority until lineage is checked.
- Do not let stale partials, old hero experiments, or previous rebuild attempts silently define the new baseline.
- Do not continue when source, workspace, or authority state is contradictory; record **SAFE UNKNOWN** or request HITL.
- Record initialization findings when clean-start, authority, source lock, or workspace state affects implementation confidence.
- Keep initialization lightweight: enough to prevent contamination, not a ceremony that blocks obvious safe work.

---

## 4. Anti-Patterns

| Anti-pattern | Why it is drift |
|--------------|-----------------|
| **Cold start by assumption** | Work begins before source, workspace, and authority are named. |
| **Workspace-as-truth** | Existing files override the approved source because they are convenient. |
| **Stale hero bootstrap** | Old first-screen implementation becomes hidden foundation for a rebuild. |
| **Source lock after styling** | Visual choices are made before the active source is established. |
| **Initialization theater** | A long checklist is filled without answering what is safe to build from. |
| **Authority laundering** | A prior agent summary or old code is treated as approved authority. |

---

## 5. Drift Patterns

- **Bad initialization drift** - the run starts from an unclear or contaminated baseline.
- **Bootstrap ambiguity drift** - operators cannot tell which source, assets, or workspace state are active.
- **Authority initialization drift** - source, old implementation, project memory, and human decisions blur together.
- **Initialization survivability erosion** - another session cannot reconstruct the starting state.

---

## 6. Triumph V3 Lesson

Triumph V3 showed that full-screen reconstruction can fail before the first implementation edit when the operator inherits stale hero logic, unclear asset authority, and ambiguous “first screen” scope.

The reusable lesson is governance-only: first-screen rebuilds need a clean initialization record before production work. This is not a Triumph implementation template.

---

## 7. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Active source is unnamed | Cannot prove what governs implementation. |
| Workspace residue is not audited | Cannot prove old code will not contaminate the rebuild. |
| Existing code authority is unclear | Cannot tell whether code is baseline, residue, or rejected attempt. |
| Asset authority is missing | Cannot safely use or transform media. |
| First-screen ownership is merged | Cannot decide whether header, hero, background, overlay, or conversion layer owns a decision. |

**Action:** stop, reset, map authority, or continue only with explicit bounded assumptions.

---

## 8. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-18 | Initial Initialization Governance layer from Triumph V3 battle-test lessons; documentation only. |
