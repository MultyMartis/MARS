# MARS — Execution Model (governance)

**Status:** **documented** — how work **runs** in practice vs how it may run **after** a runtime exists. This file does **not** claim an in-repo scheduler, queue, or MARS process manager.

**Version:** v0.

---

## 1. Purpose

The **execution model** answers: **who executes what, where, and in which order**—for **Phase 1 (documentation-first)** and for **future** automation. It complements `../workflows/execution-flow.md` (stages) by focusing on **hosts** and **bridges**.

---

## 2. How tasks are executed **today** (as documented): Web-GPT → Cursor

**Today** (per imported charter and project rules) the **live** path for “doing work on the repository” is **not** a MARS process inside this repo. It is:

1. **Web-GPT (or similar)** prepares instructions, context packaging, and prompts; **legacy** material describes **rules** and expectations for that side.
2. **Cursor (or compatible IDE + agent)** performs **filesystem** edits, runs **commands** in a **user-controlled** environment, and applies **user** prompts.

In short: **cognitive and planning** work may be prepared in one surface; **execution of edits and commands** in this repo is **on the developer machine** under **user** and **editor** control.

**Implication:** The **MARS** contracts (`../workflows/…`, `../control-plane/…`) are **target** shape; the **operational** execution path in Phase 1 is **Web-GPT → Cursor** (naming as in `../web-gpt-sources/01_system.md` manifest: Web-GPT prepares; **mass edits through Cursor**).

**Honesty:** This repository does **not** ship a MARS **daemon** that enforces the full `prompt → … → log` chain automatically.

---

## 3. Future execution surfaces (planned, not claimed)

| Surface | Role in the **intended** evolution |
|--------|------------------------------------|
| **MARS runtime** | A **future** process (or set of services) that implements **Control Plane** behavior: **task** binding, **plan**/**route**/**execute** with durable **state** and **logs** as in `../workflows/execution-flow.md`. |
| **n8n (or other workflow engine)** | **Optional** **orchestration** and integration layer for **external** triggers, retries, and integration with **non-IDE** systems. Not mandatory for MARS **semantics**; a possible **execution bridge** consumer. |
| **Agents (specialized roles)** | **When** a runtime exists, **agents** (per **Agent Registry**) become **dispatch** targets, not just documentation roles. |
| **Tools** | Exposed to the runtime/dispatcher with policy; see `../tools/README.md` for **concepts**—**no** single implemented catalog is asserted repo-wide. |

**Ordering:** The **roadmap** (`../web-gpt-sources/14_roadmap.md` and project phase statements) is authoritative for **when** the team **plans** to add implementation—**not** a guarantee of completion dates.

---

## 4. Execution Bridge (concept)

An **Execution Bridge** is a **translation and handoff** layer between:

- **MARS internal semantics** (task/workflow state, **signals**, **required_agents**, **Control Plane** decisions per contracts), and  
- **Concrete runners** (Cursor session, n8n workflow, HTTP worker, k8s job, CLI, **future** MARS runtime API).

**Responsibilities of the bridge (normative *intent*, not a spec of one implementation):**

| Concern | Bridge should… |
|--------|------------------|
| **Identity** | Map **task id** / **correlation id** across systems for **traceability** (aligns with **lifecycle** / run-history **concepts**). |
| **State handoff** | Pass enough context so the next hop knows **objective**, **scope**, **gates**, and **signals**; avoid silent **scope** expansion. |
| **Policy** | Respect **HITL** and **SECURITY** stops even when the downstream runner is “fully automated.” |
| **Failure** | Surface **UNKNOWN** / **STRUCTURE_CHANGE** as **escalation**, not silent retries, when contracts say so. |

**Examples of bridge *instances* (illustrative):** “MARS **task** record → n8n **webhook** payload”; “MARS plan step → **Cursor** prompt bundle”; “MARS **dispatch** → **runtime** worker.” **No** particular bridge is mandatory in v0 documentation.

**Relationship to `execution-flow.md`:** The **flow** defines **stages**; the **Execution Bridge** defines how a **stage** (especially **execute**) could **land** on a real **host**.

---

## 5. Contrast: workflow contract vs real executor

| Aspect | **Workflow/Control Plane (docs)** | **Web-GPT / Cursor (today)** |
|--------|------------------------------------|-----------------------------|
| **State store** | Spec’ed for **future** (State Manager in `../control-plane/components.md`) | **Editor** + human memory + chat history; no shared MARS DB. |
| **Registry** | `../agents/registry.md` is **source of truth for roles** in design | **Human** must interpret cards when choosing behavior. |
| **Logs** | **Planned** observability | Git history, local logs, optional IDE traces—**not** unified MARS run log. |

---

## 6. SAFE UNKNOWN

- Exact **wire format** for a future MARS **runtime** API.  
- Whether **n8n** is in scope for **your** team’s MARS **program** (optional by design in this file).

---

## 7. Changelog (documentation)

| Version | Date | Notes |
|---------|------|--------|
| v0 | 2026-04-27 | Initial execution model; Execution Bridge defined. |
