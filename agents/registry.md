# MARS — Agent Registry v0 (planned contract)

**Status:** **planned** — **contract and catalog content** only. No API, no database, no running registry service. This document defines *what* a registry would hold and *how* agent cards are structured; **implementation** is out of scope for v0.

**Version:** v0 (initial contract snapshot; cards may be revised without implying prior code existed).

---

## 1. Purpose: Agent Registry / Agent Catalog

The **Agent Registry** (used interchangeably with **Agent Catalog** in v0) is the **authoritative, human- and machine-readable catalog** of **agent roles** known to MARS: identity, purpose, boundaries, I/O, tools, permissions, and lifecycle state.

**Why it exists (v0):**

- **Control Plane** (see `../control-plane/contract.md`) needs a **stable, policy-addressable** list of roles to **route** and **hand off** work.
- **Security** needs to evaluate **what** each agent may do.
- **Operations** needs to see **which** agent definitions are real vs **planned** or **deprecated**.

The registry **does not** implement agents; it **describes** them. Executable agents would live in implementation packages **later**; v0 is **documentation-only** in this repository.

---

## 2. Agent status values (v0, normative)

| Status | Meaning |
|--------|---------|
| **planned** | Role is **accepted in the catalog**; no implementation in-repo; design may change. |
| **draft** | Card in active editing; not yet stable for routing or policy. |
| **legacy-bridge** | Maps a **legacy** or imported concept to a v0 MARS role; may carry transitional constraints. |
| **active** | **Planned** state for a **supported** in-production or in-pilot implementation — **in v0 this remains documentation-only** until real code and ops prove *active*; do **not** mark *active* without that evidence. |
| **deprecated** | Role is being phased out; new runs should not target it; migration path should be on the card. |

**Honesty rule:** Until the repository contains real agent runtimes, **all** v0 cards should default to **planned** or **draft** / **legacy-bridge**; **active** is reserved for when the implementation exists and the team agrees to the label (see `registry.md` + git practice).

---

## 3. Required fields (agent card v0)

Each agent in the registry is described by a **card** (see `agent-card-template.md`). v0 **requires** these fields:

| Field | v0 role |
|-------|--------|
| **name** | Unique catalog name (stable id for routing references). |
| **type** | e.g. specialist, builder, guard, orchestration-helper; free text or enum TBD at implementation. |
| **purpose** | One-paragraph *why* this role exists. |
| **responsibilities** | What the agent is **meant** to do within MARS. |
| **non-responsibilities** | What the agent **must not** do (avoids “god agent”). |
| **inputs** | What it accepts (logical contract; formats TBD). |
| **outputs** | What it returns or produces (artifacts, decisions). |
| **tools** | Tool ids / classes it may use (per policy, often empty in v0). |
| **permissions** | Scopes, model/tool/routes allowed. |
| **limitations** | Known failure modes, context window, latency, or policy caps. |
| **workflow** | How it is typically invoked in runs (e.g. after plan step, HITL). |
| **validation** | How success/quality is checked. |
| **changelog** | History of **card** changes (not product releases). |

**SAFE UNKNOWN** applies to any sub-field not yet decided.

---

## 4. Initial documented agents (v0)

Summaries only; each card is intended to be expanded in-repo using `agent-card-template.md`.

| name | default status (v0) | one-line role |
|------|----------------------|---------------|
| **Agent Builder** | planned / legacy-bridge | Decomposes product intent into other agent definitions and card updates (successor to **Factory Engineer** idea). |
| **Validator Agent** | planned / legacy-bridge | Validates outputs, policies, and structural constraints (aligns with **FlyCheck** legacy). |
| **Gulp Frontend Agent** | legacy-bridge | Specialist for frontend/build pipelines; **remains a legacy specialist profile** in the catalog, not a claim of in-repo Gulp code. |
| **Memory Agent** | planned | Curates, retrieves, and summarizes **memory** surfaces for other agents. |
| **Research Agent** | planned | Gathers, compares, and cites information from allowed sources. |
| **Coding Agent** | planned | Produces and edits code within policy and handoff from Control Plane. |
| **Documentation Agent** | planned | Produces and maintains user-facing and internal documentation artifacts. |

---

## 5. Relation to Control Plane

Per `../control-plane/contract.md`:

- The **Control Plane** **reads** the **registry** (when implemented, from a registry service or the **same logical catalog** bound at deploy time) to know **which agent roles exist**, their **ids**, and **constraints**.
- The **Control Plane** **routes** work by **agent role** (and plan step), and filters by **status** and **permissions** (e.g. it must not route to `deprecated` unless a migration run explicitly allows; **draft** is not for production routing in v0 intent).
- The registry **does not** replace the **Control Plane** state machine; it is **metadata** the router uses with **Security** and **planner** outputs.

v0: **read-only** relationship in design — the registry is **not** self-modifying during a run in v0; **Agent Builder** card changes are **out-of-band** (human- or batch-driven).

---

## 6. Relation to legacy naming

| Legacy (documented) | v0 MARS card |
|---------------------|-------------|
| **Factory Engineer** | **Agent Builder** (conceptual successor) |
| **FlyCheck** | **Validator Agent** (conceptual successor) |
| **Gulp Frontend Agent** | **Same** name, kept as **legacy specialist** profile; see card **limitations** and **status**; no automatic claim of implementation. |

**SAFE UNKNOWN** for any other legacy name until mapped on a card.

---

## 7. Implementation honesty

- This directory has **no** source code; only Markdown contracts.
- Control Plane and Agent Registry v0 are **separate** documents: **Control Plane** owns orchestration; **this registry** owns *who* the agents *are* on paper.

**Document set:** `README.md`, `registry.md` (this file), `agent-card-template.md`.
