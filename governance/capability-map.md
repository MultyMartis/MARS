# MARS — Capability Map (governance)

**Status:** **documented** — describes **intended** system capabilities and **logical** mappings. It does **not** assert that a capability is **implemented**; verify against repository contents and `AGENTS.md` status rules.

**Version:** v0.

---

## 1. Purpose

The **Capability Map** lists what MARS is **designed** to do (at the system level) and how those capabilities connect—**in documentation**—to **agents**, **workflows**, and **tools**. Gaps or future items are explicit **SAFE UNKNOWN** or “planned” where appropriate.

---

## 2. System capabilities (intended, not a shipping checklist)

| ID | Capability | Short description | Evidence / contract (in-repo) |
|----|------------|-------------------|-------------------------------|
| C1 | **Task orchestration** | Bind prompts to structured tasks, plan, route, execute, validate, report, log (target design). | `../workflows/execution-flow.md`, `../workflows/workflow-v0.md` |
| C2 | **Control Plane coordination** | Orchestration role: state, dispatch, handoffs, signals (target). | `../control-plane/contract.md`, `../control-plane/components.md` |
| C3 | **Agent role management** | Catalog of agent **roles** with cards, status, permissions. | `../agents/registry.md`, `../agents/agent-card-template.md` |
| C4 | **Agent definition lifecycle** | Gated path to create/update **agent** definitions and registry (Agent Builder / Factory **design**). | `../agents/agent-factory-v0.md`, `../agents/agent-builder-contract.md` |
| C5 | **Policy & quality signals** | System signals (UNKNOWN, SAFE UNKNOWN, HITL, security, structure change) in contracts. | `../workflows/task-contract-v0.md`, `../control-plane/contract.md` |
| C6 | **Memory, storage, observability (target layers)** | Target documentation for memory, storage, security, eval, observability **layers**. | `../memory/README.md`, `../storage/README.md`, `../security/README.md`, `../observability/README.md` |
| C7 | **Interfaces & human workflow** | Interface layer and **human** involvement where documented. | `../interfaces/README.md`, charter in `../web-gpt-sources/01_system.md` |
| C8 | **Documentation governance** | Consistent terms, roadmaps, migration, terminology mapping. | `../web-gpt-sources/01_system.md` (terminology table), `../web-gpt-sources/13_migration.md`, `../web-gpt-sources/14_roadmap.md` |
| C9 | **Execution dispatch** | **Execution Bridge Contract** v0: orchestration → executors, bridge I/O and failure facets (Stage 8.5 P0; **documentation** only). | `../mars-runtime/execution-bridge-v0.md`; [master-build-map.md](master-build-map.md) Stage 8.5; [dependency-map.md](dependency-map.md) `execution_bridge` |
| C10 | **State persistence** | **Runtime State Store Contract** v0: durable task/run state records and facets (Stage 8.5 P0; **documentation** only). | `../storage/runtime-state-store-v0.md`; [master-build-map.md](master-build-map.md) Stage 8.5; [dependency-map.md](dependency-map.md) `runtime_state_store` |
| C11 | **Recovery planning** | **Recovery Playbooks** v0 plus **Self-Heal** v0 (plan-only), **approval gates**, and risk-register alignment (Stage 8.5 P0; **documentation** only). | `../interfaces/recovery-playbooks-v0.md`, `../interfaces/self-heal-v0.md`, `../security/approval-gates.md`; [master-build-map.md](master-build-map.md) Stage 8.5; [risk-register.md](risk-register.md) RISK-V0-0013; [dependency-map.md](dependency-map.md) `recovery_playbooks`, `self_heal` |
| C12 | **Memory write governance** | **Memory Write Policy** v0 — who may write what, when; pairs with guardrails/permissions (Stage 8.5 P0; **documentation** only). | `../memory/memory-write-policy-v0.md`; [master-build-map.md](master-build-map.md) Stage 8.5; [dependency-map.md](dependency-map.md) `memory_write_policy` |
| C13 | **Checkpoint / resume** | **Checkpoint / Resume Protocol** v0 over state and workflow boundaries; pairs with **Failure Handling Model** v0 (Stage 8.5 P0; **documentation** only). | `../storage/checkpoint-resume-protocol-v0.md`, `../workflows/failure-model-v0.md`; [master-build-map.md](master-build-map.md) Stage 8.5; [dependency-map.md](dependency-map.md) `checkpoint_resume_protocol`, `failure_model` |
| C14 | **Threat review** | **Threat Model** v0 — MARS-native extension before Tool-layer documentation; feeds [risk-register.md](risk-register.md) (Stage 8.5 P0; **documentation** only). | `../security/threat-model-v0.md`; [master-build-map.md](master-build-map.md) Stage 8.5; [dependency-map.md](dependency-map.md) `threat_model` |

**Implementation honesty:** A row in this table is **not** a claim of runnable code, services, or deployed agents.

---

## 3. Mapping: capability → agents → workflows → tools

Use this as a **logical** matrix for traceability. **Agents** and **tools** are **as documented** in registry and tool docs; not all are realized.

| Capability | Typical **agent roles** (from `../agents/registry.md` and cards) | **Workflows** / stages | **Tools** (concepts) |
|------------|--------------------------------------------------------------------|------------------------|------------------------|
| C1 Task orchestration | Planner-oriented behavior, specialists invoked at **execute** (e.g. Coding, Research, Documentation) | Stages: `prompt` → `task` → `plan` → `route` → `execute` → `validate` → `report` → `log` per `../workflows/execution-flow.md` | LLM, file/git/scaffold tools as permitted by future **Tool** layer; **SAFE UNKNOWN** per environment |
| C2 Control Plane | **Not** a single “agent” — **orchestrator** in design; Validator where routed | Same flow; Control Plane “owns” orchestration **when it exists** | Policy hooks, future dispatch APIs |
| C3 Agent role management | **Agent Builder** (definition), all **registered** roles as catalog entries | `workflow-v0` relation to `required_agents` on **Task** | N/A (registry is documentation-first) |
| C4 Agent definition lifecycle | **Agent Builder**, **Validator** where policy requires | Factory **off** normal user task path; `STRUCTURE_CHANGE` / `UNKNOWN` in contracts | N/A (process + docs) |
| C5 Policy & quality | **Validator** (e.g. legacy FlyCheck successor), security-oriented checks | `validate` stage, signals at all stages | Guardrail/tool policy (future) |
| C6–C8 Cross-cutting | Varies by layer | Roadmap and migration **docs** | External systems per **System Boundaries** (see `system-boundaries.md`) |
| C9–C14 Runtime readiness | **Validator** / **security**-oriented roles where gated; orchestration for dispatch | **Stage 8.5** P0 **documented** before **Stage 9** in [master-build-map.md](master-build-map.md); workflow **validate** / **log** | Stage 8.5 P0 contracts **documented** (`execution-bridge-v0`, `runtime-state-store-v0`, `failure-model-v0`, `checkpoint-resume-protocol-v0`, `memory-write-policy-v0`, `threat-model-v0`, `recovery-playbooks-v0`); runnable engines and Tool-layer catalogs remain **planned** / **SAFE UNKNOWN** per `../AGENTS.md` |

**Rules:**

- A **capability** may be **partially** covered by documentation only.
- **Workflows** in v0 are **contracts**; they do not imply a running engine.
- **Tools** are referenced generically; concrete tool catalogs live under `../tools/README.md` and related docs **when present**.

---

## 4. Relation to other governance artifacts

- **Terminology** — `../web-gpt-sources/01_system.md` (terminology table).
- **System registry (concept)** — aligned with **Project / System Registry** in legacy→MARS mapping: `../web-gpt-sources/13_migration.md`.
- **Entity passports (concept)** — **agent** identity and bounds are expressed in **agent cards** (`../agents/agent-card-template.md`); a separate “entity passport” file may or may not exist; do not assume without path proof.
- **Execution path today** — see `execution-model.md` (Web-GPT → Cursor; future runtime / n8n / agents).

---

## 5. SAFE UNKNOWN

- Which **tool** names are **authoritative** for a given host environment — **unknown** until a machine-readable catalog ships.
- **Exact** **role** list for production — **registry**-bound; out-of-date docs are always possible.

---

## 6. Changelog (documentation)

| Version | Date | Notes |
|---------|------|--------|
| v0 | 2026-04-27 | Initial governance capability map. |
| v0 | 2026-04-27 | **C9–C14** — Stage **8.5** **P0** **runtime** **readiness** **documented**: **Evidence** column links to `../mars-runtime/execution-bridge-v0.md`, `../storage/runtime-state-store-v0.md`, `../workflows/failure-model-v0.md`, `../storage/checkpoint-resume-protocol-v0.md`, `../memory/memory-write-policy-v0.md`, `../security/threat-model-v0.md`, `../interfaces/recovery-playbooks-v0.md` (plus governance cross-refs); §3 matrix — P0 **documented**, not **TBD**. |
