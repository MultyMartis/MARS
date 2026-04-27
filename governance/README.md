# MARS — Governance

**Status:** **documented** — system-level **control** documents: boundaries, execution, state, versioning, and the **capability** map. These files **govern** how MARS is described; they are **not** a substitute for `../AGENTS.md` honesty about **documented** vs **planned** vs **legacy** **imported** material.

---

## Governance addenda (this folder)

| Document | Description |
|----------|-------------|
| [master-build-map.md](master-build-map.md) | **Primary roadmap / build order** (v0): stages 0–16, **doc vs planned-implementation** posture, **dependencies**, **audit blockers**, and rules for logging build-order changes to `../logs/` (until replaced by a formal project tracker). |
| [dependency-map.md](dependency-map.md) | v0 directed **dependencies** between system-level **contract** **entities** (`entity_id` → `depends_on`, `dependency_type`, `reason`, `risk_if_broken`); **maintenance** **rules**; **SAFE** **UNKNOWN** for unmapped edges. Prerequisite for **Self-Heal** / **Tool** / **Model** / **runtime** **documentation** alongside [risk-register.md](risk-register.md) (see [master-build-map](master-build-map.md)). |
| [risk-register.md](risk-register.md) | v0 **Risk** **Register**: purpose, **when** to add/update rows, **fields** and **enums**, relations to **dependency** **map**, **signals**, **guardrails**, **lifecycle** **log**; **normative** rules for **SECURITY** **RISK**, **NEED** **HUMAN** **APPROVAL**, **integrations**, and **runtime** **reviews**; seed **risks**. **Governance** **Foundation**; prerequisite for **Tool** / **Model** / **runtime** **documentation** per **master** **build** **map**. |
| [capability-map.md](capability-map.md) | System **capabilities** and **logical** mapping: capability → **agents** → **workflows** → **tools** (no **implementation** claims). |
| [system-boundaries.md](system-boundaries.md) | What is **inside** MARS (design / repo) vs **outside** (external systems) and **responsibility** borders. |
| [execution-model.md](execution-model.md) | How work runs **today** (Web-GPT → Cursor) and **future** surfaces (runtime, n8n, **agents**); **Execution Bridge** concept. |
| [state-model.md](state-model.md) | **Task**, **workflow run**, and **agent registry** **states** and **allowed** **transitions**. |
| [versioning-model.md](versioning-model.md) | System vs **entity** versions, **contract** **changes**, **compatibility** **rules**. |
| [universal-entity-operations.md](universal-entity-operations.md) | **Universal** vocabulary for **entity**-level **Self-Describe**, **Self-Check**, **Self-Audit**, **Self-Migrate**, **capability** **discovery**, and **Risk** **Review**; **types**, **common** **facets**, and relation to [../interfaces/introspection-v0.md](../interfaces/introspection-v0.md) (specification only). |
| [system-signals-dictionary.md](system-signals-dictionary.md) | Canonical v0 system **signal** **names** and **alias** / **STRUCTURE** **policy**; **referenced** from [master-build-map](master-build-map.md), [dependency-map](dependency-map.md), and **workflow** / **task** **contracts** (documentation). |

---

## Linked governance inputs (elsewhere in the repo)

**Established** artifacts (paths relative to `governance/`) that governance documents reference:

| Topic | Location |
|-------|----------|
| **Terminology map** (legacy → MARS) | [../web-gpt-sources/01_system.md](../web-gpt-sources/01_system.md) (section `terminology-map.md`) |
| **Entity** identity / “passport”-style **content** (agent **cards**) | [../agents/agent-card-template.md](../agents/agent-card-template.md) — per-role **definition** template. No `entity-passport.md` in this repository; **analog** is the **card**. **SAFE UNKNOWN** for out-of-tree passports. |
| **System / Agent** **Registry** (catalog) | [../agents/registry.md](../agents/registry.md) |
| **Lifecycle** / run history **(concept)** | [../web-gpt-sources/10_observability_eval.md](../web-gpt-sources/10_observability_eval.md), [../web-gpt-sources/13_migration.md](../web-gpt-sources/13_migration.md) (maps **Lifecycle** **log** to **target** **layers**); [../observability/README.md](../observability/README.md) |
| **Roadmap** / **phases** | [../web-gpt-sources/14_roadmap.md](../web-gpt-sources/14_roadmap.md) |
| **Task** and **execution** **flow** (contracts) | [../workflows/task-contract-v0.md](../workflows/task-contract-v0.md), [../workflows/execution-flow.md](../workflows/execution-flow.md), [../workflows/workflow-v0.md](../workflows/workflow-v0.md) |
| **Control Plane** | [../control-plane/contract.md](../control-plane/contract.md), [../control-plane/components.md](../control-plane/components.md) |
| **Top-level** **project** **rules** | [../AGENTS.md](../AGENTS.md), [../README.md](../README.md) |

---

*Last updated: dependency map v0, risk register v0, system signals dictionary (v0 index), master build map v0; other governance addenda v0 as listed above.*
