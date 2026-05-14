# Terminology boundaries (anti semantic drift)

**Status:** **documented** — **stabilization** aid. Aligns with [../../AGENTS.md](../../AGENTS.md), [../execution-model.md](../execution-model.md), [../../README.md](../../README.md), [../master-build-map.md](../master-build-map.md), [../runtime-registry-boundaries.md](../runtime-registry-boundaries.md). **Website Factory** terms: cross-pack only — see [../../projects/mars-website-factory/README.md](../../projects/mars-website-factory/README.md), [../../projects/mars-website-factory/operator-lane-model-v0.md](../../projects/mars-website-factory/operator-lane-model-v0.md) (do not merge WF scope into MARS core sentences without labeling **project pack**).

---

## Core distinctions

| Term | Meaning in MARS (this repo) | Typical confusion |
|------|----------------------------|-------------------|
| **Runtime** | **Future** MARS process/services **or** colloquial “execution environment” — must be disambiguated. **Experimental R1:** narrow JS under `mars-runtime/` per [../../mars-runtime/README.md](../../mars-runtime/README.md). | Treating R1 as **full** runtime or conflating with **external** runtimes (e.g. n8n in a pilot). |
| **Governance** | Markdown **control** docs under `governance/` (+ honesty rules in AGENTS): boundaries, maps, models — **not** executable enforcers. | “Governance **enforced** automatically.” |
| **Orchestration** | **Contracts** and roadmap stages for **execution orchestration** ([../master-build-map.md](../master-build-map.md) Stage 13 naming) — **planned** as product; optional **external** engines (e.g. n8n) in execution model. | “MARS orchestrates” without naming **human/editor** or **external** engine. |
| **Execution bridge** | **Handoff** layer between MARS **semantics** and a **concrete runner**; conceptual + contract SoT in `mars-runtime/execution-bridge-v0.md` per [../execution-model.md](../execution-model.md) §4. | Any single script **is** the whole bridge **product**. |
| **Workflow** | **MARS-native** task/workflow **contracts** (`workflows/`). | A vendor workflow **is** the MARS workflow layer without boundary note. |
| **Runbook** | Human **procedure** (e.g. Website Factory operator runbooks in `projects/mars-website-factory/`). | Runbook steps **imply** MARS core automation. |
| **Agent** | **Role** in registry/cards (**documentation**); future dispatch target if runtime exists ([../execution-model.md](../execution-model.md)). | “Agent” = **LLM session** = **MARS agent instance** without context. |
| **Operational template** | **Website Factory** (and similar packs): repeatable **human-operated** patterns — **project-scoped** templates. | MARS **core** operational guarantee. |
| **Validator** | In Website Factory: **validation** roles/models over artifacts ([../../projects/mars-website-factory/validator-execution-model-v0.md](../../projects/mars-website-factory/validator-execution-model-v0.md)) — **documentation** for pilot process. | Repo-wide **automatic** validation engine. |
| **Documentation layer** | Markdown contracts, maps, README honesty — **primary** Phase 1 deliverable. | Documentation **equals** shipped behaviour. |
| **Experimental implementation** | Small in-tree code paths (R1) proving **narrow** integration shapes — **not** full stack. | Evidence of **one** file = **all** stages implemented. |
| **Operationally verified** | **Human-controlled** repo/editor operations ([../../README.md](../../README.md)); not MARS **automated** verification. | “MARS verified production.” |

---

## Lane hint (no expansion)

- **MARS core** vocabulary: `governance/`, `workflows/`, `interfaces/`, `agents/`, `control-plane/`, `mars-runtime/` **contracts + R1**.
- **Website Factory** vocabulary: under `projects/mars-website-factory/` — **strategic planned**, **documentation-first** website production system; **not** MARS runtime replacement.

---

## SAFE UNKNOWN

- Future official glossary file location if terminology splits by **program** vs **repo**.
- Exact **consumer** naming for every external runner (customer-specific).

---

*Keep paragraphs short; update when execution model or master map **normative** terms change.*
