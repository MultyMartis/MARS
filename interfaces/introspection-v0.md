# MARS — Introspection / Self-Describe v0

**Status:** **documented** — **specification only**. No code, no runtime, no prompt files, and no execution simulation. This document defines the **Introspection System** and the **Self-Describe Engine** as **design contracts** for a future dynamic layer.

**Version:** v0 (Interface Layer addendum; revisable per `governance/versioning-model.md`).

---

## 1. Purpose of the Introspection System

The **Introspection System** is the **authoritative design** for how MARS (and tools acting on its behalf) **answers questions about itself** using **only** evidence drawn from the **current repository and linked contracts** — not from memorized prose or static “about” text.

**Goals (v0):**

- Replace the legacy idea of **Self-Describe as a fixed prompt** with a **data-backed introspection contract**: *what* is read from **named sources of truth**, *how* it is combined, and *what* must be said when data is absent.
- Give the **Interface Layer** a single vocabulary for **FULL**, **SHORT**, **DEBUG**, **ENTITY**, and **PROJECT** views (see `interfaces/self-describe-modes.md`).
- Keep **documented architecture**, **planned implementation**, and **legacy imported** material distinguishable in any future consumer of this spec (aligns with `AGENTS.md`).

---

## 2. Role in the Interface Layer

Per `interfaces/README.md` in this folder, the Interface Layer covers **user and system entrypoints** (chat, admin, CLI, API, IDE channels). **Introspection v0** specifies that those entrypoints, when they offer “what is MARS / what is this entity / what is this project,” **must** treat **Self-Describe** as:

1. A **request classification** (input type → mode; see §5 and `interfaces/self-describe-modes.md`).
2. A **bounded read** over **named data sources** (§6).
3. A **composition policy** (§7) that forbids invention and requires **SAFE UNKNOWN** where files or fields do not exist.

**Introspection** is **not** the Control Plane, **not** the Workflow engine, and **not** a substitute for **Security** or **Observability** implementations. It is a **contract for truthful narration** of what the repo and governance already say.

---

## 3. Relation to other layers and folders

All path literals are relative to the **repository root**.

| Area | Relation to Introspection v0 |
|------|------------------------------|
| **Registry** (`agents/registry.md`, `agents/agent-card-template.md`, catalog entries) | **Primary** source for **agent roles**, **status**, **permissions**, and **entity-shaped** identity (agent **cards** as the in-repo analog to “passports”; see `governance/README.md`). **ENTITY** mode resolves against **entity-registry** semantics (cards + ids stable within the catalog). |
| **Project registry** (`registry/project-registry.md`) | **Source of truth** for **projects**: **project_id**, **status**, **phase**, **related_entities**, **last_updated**. **PROJECT** mode reads **only** this artifact for per-project facts; unresolved `<id>` → **SAFE UNKNOWN**. |
| **Governance** (`governance/`) | **Normative** boundaries: execution honesty, state vocabulary, versioning, capability map. Introspection **must** respect **governance** when describing what is “implemented” vs “planned” vs “legacy imported.” |
| **Lifecycle log** (`logs/lifecycle-log.md`) | **Source of truth** for **documented lifecycle events** (append-only table: **event_id**, **timestamp**, **entity_id**, **event_type**, **description**). **DEBUG** mode uses this file for event-level narration when present; **must not** claim events that are not recorded here. Operational run history / metrics remain governed by `governance/execution-model.md`, `observability/README.md` — if not in-repo, **SAFE UNKNOWN** for live telemetry. |
| **Workflow** (`workflows/`) | Describes **stages**, **task contract**, **signals** (**UNKNOWN**, **SAFE UNKNOWN**, etc.). Introspection uses workflow docs to describe **how work is supposed to flow**, not to assert a running orchestrator. |
| **Memory** (`memory/README.md`) | **Planned** layer for durable memory **services**; introspection states **only** what those docs say. **Project** identity is **not** defined here — **source of truth** for projects is `registry/project-registry.md`. Legacy / architecture discussion: `web-gpt-sources/06_memory.md`, `web-gpt-sources/13_migration.md`. |

**Control Plane** (`control-plane/`) and **Agent Factory** (`agents/agent-factory-v0.md`): Introspection **describes** their **documented contracts**; it does **not** expose live control state in v0 (no such state in-repo).

---

## 4. Self-Describe Engine (specified logical component)

The **Self-Describe Engine** is the **logical component** (future implementation) that **materializes** a response for a given **input type** by **reading** allowed **data sources** (paths in §6) and applying **output rules** (§7).

This repository **defines** the engine; it **does not** ship it.

---

## 5. Input types (normative)

Consumers map user or system requests to one of these **input types**:

| Input type | Meaning |
|------------|---------|
| **FULL** | Full-system introspection: scope, layers, governance summary, registry overview, workflow summary, honesty boundary (documented / planned / legacy). |
| **SHORT** | Compressed snapshot: what MARS is, current phase, where truth lives (paths), and pointers to deeper docs. |
| **DEBUG** | Implementation-adjacent **documentation** view: what exists in-repo vs planned; **signals** and **stages** from contracts; **issues** only if grounded in explicit doc statements or verifiable repo facts (e.g. missing expected file) — not speculative debugging. |
| **ENTITY** | Parameter **`<id>`** — description keyed to a **registry entity** (e.g. agent **name** / card id as defined in `agents/registry.md`). If **`<id>`** does not resolve to a card row or linked card file, output **SAFE UNKNOWN** for that id. |
| **PROJECT** | Parameter **`<id>`** — description keyed to a **project** row. **Source of truth** is `registry/project-registry.md`. The engine **must** read that file and return fields from the matching **project_id** row; if **`<id>`** matches no row, return **SAFE UNKNOWN** for project-specific fields while still allowed to cite **generic** architecture text from other docs when labeled as non-registry context. |

**Note:** Angle brackets denote **placeholders**; actual ids are **opaque strings** defined by future registries.

---

## 6. Data sources (normative ids)

These are **logical source ids** for implementers. Binding to concrete paths is **required** for any implementation; for **this repo today**, the **default binding** column states what exists.

| Source id | Role | Default binding in this repo (v0) |
|-----------|------|-------------------------------------|
| **system-registry** | Top-level system truth: phase, layout, boundaries. | `README.md`, `AGENTS.md`, `governance/system-boundaries.md`, `governance/capability-map.md`, `web-gpt-sources/01_system.md` (terminology), `web-gpt-sources/14_roadmap.md` |
| **entity-registry** | Catalog of agents / roles and cards. | `agents/registry.md`, `agents/agent-card-template.md`, individual card expansions if present |
| **project-registry** | Projects: ids, status, phase, related entities, last updated. | **Source of truth** is `registry/project-registry.md` — read this path for **PROJECT** mode and any project listing |
| **lifecycle-log** | Documented lifecycle / audit events (append-only). | **Source of truth** is `logs/lifecycle-log.md` — read this path for event-level facts; if an event is not recorded, it is **unknown** to this log (**SAFE UNKNOWN** when consumers ask for evidence) |
| **governance-documents** | Normative governance addenda. | `governance/*.md` (see `governance/README.md` index) |

Additional **source ids** are introduced only by **documenting** them in a future revision of this spec (per governance); until then, the **source of truth** paths in §6 are complete for v0.

---

## 7. Output rules (normative)

1. **No hallucinations** — Do not invent components, APIs, file paths, metrics, or agent behavior not supported by **read data** or explicitly marked **planned** / **legacy** in source text.
2. **SAFE UNKNOWN** — If a field, id, file, or store is missing, state **what** is unknown and **what** would verify it (path, registry version, implementation proof).
3. **No static text** — Responses **must** be **derivable** from current reads of the above sources (templates stored **outside** the answer path, e.g. in application code, are **not** “static text” inside the **Self-Describe output channel**; this repo **does not** add prompt files or canned paragraphs as product artifacts for v0).
4. **Three-way split** — When describing the system, preserve **documented architecture** vs **planned implementation** vs **legacy imported** (`AGENTS.md`).

---

## 8. Update rule

- Any **Self-Describe** result intended to represent MARS **must** be **regenerated** from **current** repository reads (or from a **snapshot** whose hash/version is disclosed). **Hardcoded descriptions** of the product **must not** replace or override source-backed sections.
- When **governance** or **registry** docs change, introspection consumers **should** reflect those changes on **next** generation without requiring a separate “about” document update cycle.

---

## 9. Explicit non-goals (v0)

- **No** new prompt files or static Self-Describe templates in `interfaces/` or elsewhere as part of this v0 spec.
- **No** simulation of execution, dispatch, or log tailing.
- **No** claim that a runtime **implements** this engine.

---

## 10. Document set

| File | Role |
|------|------|
| `interfaces/introspection-v0.md` | This file — system purpose, layer role, relations, engine contract, sources, output and update rules. |
| `interfaces/self-describe-modes.md` | Mode definitions: FULL, SHORT, DEBUG, ENTITY, PROJECT. |
| `interfaces/README.md` | Interface folder index including introspection entry points. |
| `registry/project-registry.md` | **Source of truth** for **projects**; required input for **PROJECT** mode. |
| `logs/lifecycle-log.md` | **Source of truth** for **documented lifecycle events**; required input when narrating logged events. |

---

## 11. Changelog (documentation)

| Date | Change |
|------|--------|
| 2026-04-27 | Initial **Introspection / Self-Describe v0** specification (documentation only). |
| 2026-04-27 | Aligned **data sources** with **sources of truth**: `registry/project-registry.md`, `logs/lifecycle-log.md`; **PROJECT** / **lifecycle** bindings updated; removed “no project file” v0 caveat. |
