# Canonical terminology registry

**Status:** **documented** — stabilization aid only.  
**Version:** v0 (terminology stabilization).  
**Authority:** [AGENTS.md](../AGENTS.md) > [web-gpt-sources/mars-v2/](../web-gpt-sources/mars-v2/) > this file.  
**Not:** a glossary product, ontology, meta-taxonomy, or automated enforcement layer.

---

## Core anti-mythology principle

**Registry row ≠ deployed system.**

A row in `agents/registry.md`, `tools/registry.md`, `registry/project-registry.md`, or any governance catalog describes **documented intent or classification**. It is **not** evidence that a process, service, orchestrator, validator engine, or factory stage runs autonomously in this repository.

| Requires before “exists / runs” claims | Insufficient alone |
|----------------------------------------|-------------------|
| Cited in-repo paths and described behavior | Registry presence |
| Human REPORT with scope and lane | Chat agreement |
| Operator-verified external config | Filenames implying runtime |

---

## Classification vocabulary (use these)

| Label | Meaning |
|-------|---------|
| **OPERATIONAL** | Currently used in **real human-supervised** workflows (Cursor, Web-GPT packaging, explicit git, REPORT). |
| **EXPERIMENTAL** | Narrow in-tree probes (e.g. R1 `mars-runtime/**/*.js`); isolated; not production proof. |
| **CONCEPTUAL** | Contract / vocabulary / architecture documentation without shipped product. |
| **FUTURE** | Direction that may be built later; **no** roadmap commitment implied. |
| **BOUNDARY ONLY** | Describes limits and handoff semantics; not a deployed MARS product. |
| **EXCLUDED** | Out of canonical MARS work or wrong tree for extension. |
| **HISTORICAL** | Legacy import or superseded material kept for reference. |

**Avoid** the label **PLANNED** in new stabilization prose (psychological roadmap commitment). Prefer **CONCEPTUAL**, **FUTURE**, **BOUNDARY ONLY**, or **EXPERIMENTAL**.

**Avoid** “target architecture” → prefer **conceptual architecture vocabulary**.

---

## Operational (meta-term)

| Field | Value |
|-------|-------|
| **term** | operational |
| **classification** | OPERATIONAL (when qualified) |
| **allowed usage** | “Operational **today**” = used in **human-supervised** production or core doc workflows with explicit lane, scope, and REPORT. Website Factory runbooks, parallel chat lanes, governance maintenance. |
| **forbidden usage** | **operational = automated**; **operational = runtime running**; **operational = orchestrator active** without path proof. |
| **evidence requirement** | Named workflow (runbook, lane doc, operator habit) + recent human execution trace; not registry row alone. |
| **operational status** | **OPERATIONAL** as discipline vocabulary; **not** an automation flag. |

---

## Term entries

### runtime

| Field | Value |
|-------|-------|
| **classification** | CONCEPTUAL (product) · **EXPERIMENTAL** (R1 only) · **FUTURE** (full MARS runtime) |
| **allowed usage** | “MARS runtime” as **future** process layer; “R1 experimental runtime **sketch**” with `mars-runtime/` path citation; “external runtime” (n8n, host OS) with **external** qualifier. |
| **forbidden usage** | “MARS runtime is **live** / **deployed** / **scheduling work**” without evidence; R1 JS as **full** runtime; conflating `mars-runtime/` contracts with running daemons. |
| **evidence requirement** | For in-repo claims: list `mars-runtime/**/*.js` entrypoints + manual invocation only; deny queue/worker pool unless files prove them. |
| **operational status** | Contracts **CONCEPTUAL**; R1 scripts **EXPERIMENTAL**; fleet runtime **FUTURE**. |

### orchestrator

| Field | Value |
|-------|-------|
| **classification** | CONCEPTUAL · **FUTURE** (MARS) · possible **EXTERNAL** (vendor) |
| **allowed usage** | `execution-orchestrator-v0.md` as **conceptual** contract; external engine “orchestrates **its** workflows” with system named. |
| **forbidden usage** | “MARS orchestrator **runs** Factory stages”; “orchestrator **dispatches** agents” in-repo without R1 scope proof. |
| **evidence requirement** | Contract path or external operator verification; not workflow map narrative alone. |
| **operational status** | **Not operational** as MARS product. |

### control plane

| Field | Value |
|-------|-------|
| **classification** | CONCEPTUAL (`control-plane/`) · **FUTURE** implementation |
| **allowed usage** | Documentation under `control-plane/contract.md`, `components.md`; “control plane **contracts**”. |
| **forbidden usage** | “Implemented control plane”; “enforces policy repo-wide”; “deployed control plane”. |
| **evidence requirement** | Executable enforcement code path + scope; else **CONCEPTUAL** only. |
| **operational status** | **CONCEPTUAL** in-repo. |

### validator

| Field | Value |
|-------|-------|
| **classification** | OPERATIONAL (human/checklist role) · CONCEPTUAL (models) · **not** deployed engine |
| **allowed usage** | Website Factory **Validator role** — human-operated gates per pack docs; “validation **semantics**”; checklist / REPORT validation. |
| **forbidden usage** | “Validator **service** running”; “automatic PASS”; repo-wide validation engine without path. |
| **evidence requirement** | Who validated, what artifact, what rule doc; not signal name alone. |
| **operational status** | **OPERATIONAL** as **human process**; **no** autonomous validator runtime evidenced. |

### artifact

| Field | Value |
|-------|-------|
| **classification** | OPERATIONAL (git/docs deliverables) · CONCEPTUAL (lifecycle labels) |
| **allowed usage** | Files, markdown packs, REPORT outputs, staged handoffs with lifecycle labels per `artifact-lifecycle-rules.md`. |
| **forbidden usage** | “Artifact bus **delivers** events”; immutable artifact **without** human promotion rules cited. |
| **evidence requirement** | Path + lifecycle label + lane; registry mention ≠ artifact existence. |
| **operational status** | **OPERATIONAL** as file/deliverable discipline. |

### artifact bus

| Field | Value |
|-------|-------|
| **classification** | CONCEPTUAL · BOUNDARY ONLY |
| **allowed usage** | Factory / workflow **vocabulary** for handoff semantics (documentation only). |
| **forbidden usage** | Message bus, queue, graph DB, pub/sub, or “bus **running**”. |
| **evidence requirement** | If claimed as code: cite integration module; else forbid runtime wording. |
| **operational status** | **CONCEPTUAL** only. |

### execution bridge

| Field | Value |
|-------|-------|
| **classification** | BOUNDARY ONLY · CONCEPTUAL · **EXPERIMENTAL** (narrow JS handoff) |
| **allowed usage** | `mars-runtime/execution-bridge-v0.md` SoT; “bridge **translates** task semantics to a **named runner** (Cursor, webhook)”. |
| **forbidden usage** | “Bridge **product deployed**”; any single script = entire bridge platform. |
| **evidence requirement** | Contract file + optional R1 script scope; external URL config operator-verified. |
| **operational status** | Contract **BOUNDARY ONLY**; R1 handoff **EXPERIMENTAL**. |

### workflow engine

| Field | Value |
|-------|-------|
| **classification** | CONCEPTUAL · **FUTURE** · EXTERNAL (n8n etc.) |
| **allowed usage** | MARS `workflows/` **contracts**; external workflow product named explicitly. |
| **forbidden usage** | “MARS workflow engine **executes** tasks”; map stage order = engine running. |
| **evidence requirement** | Running process logs or service definition outside docs. |
| **operational status** | **Not operational** in MARS core. |

### orchestration

| Field | Value |
|-------|-------|
| **classification** | CONCEPTUAL · BOUNDARY ONLY · EXTERNAL |
| **allowed usage** | “Orchestration **semantics** / **signals**” (dictionary); external system orchestrates **its** graphs. |
| **forbidden usage** | “MARS orchestrates production”; “automatic coordination” without human/editor named. |
| **evidence requirement** | Name **who/what** orchestrates (human, Cursor, n8n, FUTURE runtime). |
| **operational status** | Vocabulary **OPERATIONAL**; engine **not** MARS-operational. |

### agent

| Field | Value |
|-------|-------|
| **classification** | CONCEPTUAL (registry role) · OPERATIONAL (human reads card) · **FUTURE** (dispatch) |
| **allowed usage** | `agent_id` + card under `agents/cards/` as **documentation role**; “operator acts as / follows **agent** pack”. |
| **forbidden usage** | “Agent **instance running**”; LLM session = MARS agent without qualifier; registry row = live agent. |
| **evidence requirement** | Card path + human execution context; not `agents/registry.md` row alone. |
| **operational status** | Cards **OPERATIONAL** as guides; autonomous agents **FUTURE** / **EXCLUDED** claims. |

### registry

| Field | Value |
|-------|-------|
| **classification** | OPERATIONAL (human-maintained catalogs) · **not** runtime service |
| **allowed usage** | `agents/registry.md`, `tools/registry.md`, `registry/project-registry.md` as **governance catalogs**; edit with human resolution per `registry-source-of-truth.md`. |
| **forbidden usage** | “Registry **syncs** runtime”; “registry **enforces**”; R1 `tool-registry.js` overrides governance rows. |
| **evidence requirement** | **Registry row ≠ deployed system** (core principle); cite SoT doc on conflict. |
| **operational status** | Markdown registries **OPERATIONAL** (maintenance); sync engine **FUTURE** / absent. |

### experimental

| Field | Value |
|-------|-------|
| **classification** | EXPERIMENTAL |
| **allowed usage** | R1 scripts, `tools/` pilots, isolated probes per `experiment-classification.md`; REPORT required. |
| **forbidden usage** | Experimental path cited as **platform proof** or governance truth. |
| **evidence requirement** | Paths + manual run + lane; isolation from core claims. |
| **operational status** | Label for **bounded** probes only. |

### conceptual

| Field | Value |
|-------|-------|
| **classification** | CONCEPTUAL |
| **allowed usage** | Contracts, maps, state models, boundary docs without executable product. |
| **forbidden usage** | “Conceptual **and deployed**” without downgrade; using as excuse to skip evidence when code exists. |
| **evidence requirement** | N/A for existence claims; cite contract path for vocabulary only. |
| **operational status** | Default for most `governance/`, `workflows/`, `control-plane/` artefacts. |

### deployed

| Field | Value |
|-------|-------|
| **classification** | EXTERNAL or project-specific · rarely in-repo MARS core |
| **allowed usage** | Customer site, n8n instance, CI — **outside** MARS core with operator verification. |
| **forbidden usage** | “MARS deployed”; “Factory deployed”; registry `status` cell = live deployment. |
| **evidence requirement** | URL/config/output from operator; not project-registry row alone. |
| **operational status** | **Not** a default MARS core claim. |

### automation

| Field | Value |
|-------|-------|
| **classification** | EXTERNAL · EXPERIMENTAL (narrow scripts) · **FUTURE** |
| **allowed usage** | External CI/n8n; explicit human-triggered scripts; “**no** MARS core automation” honesty. |
| **forbidden usage** | Hidden stage advancement; governance enforcement automation; “factory automates” without scope. |
| **evidence requirement** | Scheduler/cron/worker path or deny; HITL and REPORT remain visible. |
| **operational status** | Core production loop is **human-supervised**, not automated. |

### coordination

| Field | Value |
|-------|-------|
| **classification** | OPERATIONAL (human/lane discipline) · CONCEPTUAL (signals) |
| **allowed usage** | Parallel chat lanes, explicit handoffs, operator approvals; signal **names** in dictionary. |
| **forbidden usage** | “Automatic agent coordination”; implicit multi-agent sync without bridge/runner named. |
| **evidence requirement** | Charter + lane doc; name coordinator (human vs external). |
| **operational status** | **OPERATIONAL** via human discipline only. |

---

### GitGuard

| Field | Value |
|-------|-------|
| **classification** | **REGISTERED** cross-cutting survivability concept (**OPERATIONAL** human-operated implementation) |
| **type (documentation)** | **Repository Survivability Layer** — advisory framework under `projects/mars-survivability/` |
| **authority** | Human operator; human-invoked validator/helpers |
| **purpose** | Checkpoint, freeze, rollback, baseline visibility; backup intelligence; release traceability — **not** autonomous enforcement |
| **allowed usage** | Pre-destructive checks; snapshot discipline; rollback map maintenance; cross-link to lifecycle/releases |
| **forbidden usage** | Autonomous backup product; `project_id` without charter; `projects/gitguard/` pack implied as shipped; replacement for git hosting |
| **evidence requirement** | [../projects/mars-survivability/registries/gitguard-system-entry-v1.md](../projects/mars-survivability/registries/gitguard-system-entry-v1.md); [../logs/cleanup/actions/gitguard-registration-v1.md](../logs/cleanup/actions/gitguard-registration-v1.md) |
| **operational status** | **REGISTERED** Wave 2B — **not** separate registry row |

---

### IdeaBox

| Field | Value |
|-------|-------|
| **classification** | **OPERATIONAL** (human-operated filesystem discipline) |
| **type (documentation)** | **Incubation Layer** (optional) — filesystem-backed continuity workflow; use when idea exists but implementation is deferred |
| **authority** | **Human-operated** — operator chooses paths, edits, merges, deletions; Cursor assists only when instructed |
| **purpose** | Continuity across sessions, idea capture, operational memory hygiene — via explicit markdown, not implicit state |
| **allowed usage** | Record notes under `continuity/**`; use protocols/templates as conventions; reference as **optional** incubation — **direct** program/governance creation remains valid |
| **forbidden usage** | “IdeaBox remembers”; autonomous agent memory; hidden runtime state; automatic governance or registry mutation; orchestration or semantic-graph narratives tied to IdeaBox |
| **evidence requirement** | Cited markdown paths under `continuity/`; chat markers (`/ideabox`, etc.) **≠** executed commands |
| **operational status** | **OPERATIONAL** as **discipline + docs** only — **not** a shipped MARS subsystem |

---

## Cross-references (no expansion)

- [enforcement/terminology-boundaries.md](enforcement/terminology-boundaries.md) — lane hints  
- [runtime-registry-boundaries.md](runtime-registry-boundaries.md) — three registry kinds  
- [reality-vs-mythology-warnings.md](reality-vs-mythology-warnings.md) — drift patterns  

*Update this registry only when stabilization requires a new high-risk term; do not grow into a framework.*
