# MARS — Master Build Map v0

**Status:** **documented** — **roadmap and build-order source only**. This file does **not** describe shipped runtime, services, or automation. It classifies **documentation**, **contracts**, and **planned implementation** per [../AGENTS.md](../AGENTS.md).

**Version:** v0. Supersedes informal ordering only when a later version explicitly replaces this map. Revisable per [versioning-model.md](versioning-model.md).

---

## Authority and maintenance rules

1. **Primary roadmap** — Until a formal external project tracker is adopted, **`governance/master-build-map.md`** is the **primary** source for **development stage order**, **layer dependencies**, and **doc vs implementation** expectations for MARS in this repository.
1a. **Dependency map, Risk Register, Self-Heal, Runtime Readiness, and later layers (governance + interfaces)** — [dependency-map.md](dependency-map.md) (v0) is the **documentation**-only register of system-level entity → entity edges (vocabulary in §3 of that file). [risk-register.md](risk-register.md) (v0) is the **documentation**-only register of **explicit** **risks** (fields, enums, and rules in that file). [Self-Heal v0](../interfaces/self-heal-v0.md) is the **documentation**-only contract for **recovery** / **fix** **plans** (**plans only**; **no** execution or auto-fix). **Stage 8.5** **P0** **Runtime** **Readiness** **documentation** (including [Threat Model v0](../security/threat-model-v0.md) and [Recovery Playbooks v0](../interfaces/recovery-playbooks-v0.md)) is **complete** in-repo; **completing** that **P0** **set** is **not** a **waiver** for [AGENTS.md](../AGENTS.md) **or** a **claim** of **MARS** **runtime** in **this** **repository** (**RISK**-**V0**-**0005** **/ Stage** **8.5** **“what** **exists** **now**”). **Model**, **Execution** **bridge**, and **Runtime** **documentation** (stages **10**, **13**, **14**) **should** treat **8.5** **artefacts** as **normative** wherever **state**, **failure**, **memory** **writes**, **checkpoints**, **threats**, or **recovery** **semantics** **apply** (avoid **implicit** **gaps**). Before progressing **documentation** for **Tool** (Stage **9**), **Model** (Stage **10**), or **Runtime** (Stage **14**), **Self-Heal** **v0** **and** [Recovery Playbooks v0](../interfaces/recovery-playbooks-v0.md) should be read together with [Self-Heal v0](../interfaces/self-heal-v0.md) as the **SoT** for **pattern**-**bound** **recovery** **(plan**-**only** in **v0**). Before progressing **documentation** for **Tool** / **Model** layers, **Execution** **bridge**, or execution-facing **runtime** (stages **9**, **10**, **13**, **14**), **update** or re-confirm the **dependency** **map**, **review** or **update** the **Risk** **Register** per [risk-register.md](risk-register.md) **§7**, or append a lifecycle row with `NEED REVIEW` in the summary (see [dependency-map.md](dependency-map.md) §5). A new system-level SoT in a **named** track **requires** new or updated **rows** in the **dependency** **map**; **SECURITY** **RISK** and **integration** / **runtime** **rules** in the **Risk** **Register** **require** **register** **rows** **when** **those** **rules** **fire**.
2. **Build-order changes** — Any **material change** to the **ordered stages**, **dependency graph**, or **definition of “done”** for a stage **must** be recorded in **`logs/decision-log.md`** (when that file exists and is stable) **or** in **`logs/lifecycle-log.md`** with a clear **event_type** (e.g. `governance.build_map_revised`) and pointer to the governing markdown revision. **SAFE UNKNOWN:** `logs/decision-log.md` is **not** present in-repo as of map v0; use **`logs/lifecycle-log.md`** until a decision log is introduced.
3. **Honesty** — Stages marked **planned-implementation** have **no** in-repo proof of runnable code unless another file explicitly lists evidence. Do not treat this map as an implementation certificate.
4. **Consistency Fix gate** — **No progression** to **Stage 8** or **any later stage** until **all P0** issues from the **system audit** are **resolved** and the **system passes a re-check audit** (Stage **7.5** exit criteria).

---

## Audit findings — status after Stage 7.5 (2026-04-27)

The following **P0** audit items are **RESOLVED** (see **`logs/lifecycle-log.md`** event `evt-2026-0002`):

| Item | Resolution |
|------|------------|
| **Introspection path conflict** | **RESOLVED** — `interfaces/introspection-v0.md` §6 **default bindings** and related interface specs use **repository-root-relative** paths consistently; **system-registry** sources are unambiguous. |
| **Broken / ambiguous path references (interface scope)** | **RESOLVED** — `interfaces/` markdown links and path literals normalized to repository root (re-check 2026-04-27). |
| **Incomplete README layout** | **RESOLVED** — root [../README.md](../README.md) **Repository layout** table enumerates `governance/`, `registry/`, `logs/`, `interfaces/`, `workflows/`, `agents/`, `control-plane/`, `mars-runtime/`, `web-gpt-sources/`. |
| **Security wording ambiguity (`security/README.md`)** | **RESOLVED** — [../security/README.md](../security/README.md) states **documentation / planned contract only** and explicit absence of shipped runtime, policy engine, or enforcement code in Phase 1. |
| **Interface README role wording** | **RESOLVED** — [../interfaces/README.md](../interfaces/README.md) uses **documented / planned** contract language (no **“Implements”** layer claim); architecture pointers use **`web-gpt-sources/…`** paths. |

**Residual (non-blocking):**

| Severity | Note |
|----------|------|
| **P2** | Some **non-`interfaces/`** markdown (including links in this map) may still use **`../`** link style from an older convention; prefer **repository-root-relative** paths for new edits and when touching those files. |

---

## Stage overview (build order)

Stages are **sequential by dependency**. Later stages may **start** documentation in parallel only where **dependencies** allow; **implementation** must not skip **contracts** that upstream stages require.

| Order | Stage | Short name |
|------:|-------|------------|
| 0 | Source Pack / Identity | Identity |
| 1 | Cursor / Repo Rules | Rules |
| 2 | Governance Foundation | Governance |
| 3 | Registry / Logs / Entity Passports | Registry |
| 4 | Control Plane Contract | Control Plane |
| 5 | Agent Registry / Agent Factory | Agents |
| 6 | Workflow / Task Contract / State Model | Workflow |
| 7 | Interface / Introspection / Self-* Operations | Interface |
| 7.5 | Consistency Fix Pass | Fix Pass |
| 8 | Security / Guardrails / Permissions | Security |
| 8.5 | Runtime Readiness Contracts | Runtime readiness |
| 9 | Tool Registry / Tool Permissions | Tools |
| 10 | Model Layer / Provider Routing | Models |
| 11 | Storage / Memory / RAG | Storage / RAG |
| 12 | Observability / Evaluation | Observability |
| 13 | Execution Bridge / Runtime Starter | Execution bridge |
| 14 | Runtime Implementation | Runtime |
| 15 | External Integrations | Integrations |
| 16 | Pilot Project | Pilot |

---

## Stage 0 — Source Pack / Identity

| Field | Content |
|-------|---------|
| **Purpose** | Establish **what MARS is**, **phase**, **terminology**, and **legacy vs native** docs so all downstream contracts share vocabulary. |
| **Related folders** | [../web-gpt-sources/](../web-gpt-sources/), [../LICENSE.md](../LICENSE.md), [../README.md](../README.md) |
| **Status** | **done-docs** (pack + root README layout table per Stage 7.5) |
| **What exists now** | Numbered Web-GPT topic files `01_system.md`–`14_roadmap.md`; LICENSE; top-level README with phase, three-way split, and **Repository layout** table. |
| **What is missing** | Optional: deeper cross-index from README to every governance addendum; no **implementation** claims required. |
| **Next required action** | None blocking for layout; keep README aligned when top-level folders change. |
| **Dependencies** | None (foundation). |

---

## Stage 1 — Cursor / Repo Rules

| Field | Content |
|-------|---------|
| **Purpose** | Bind editor/agent behavior to **honesty**, **scope**, and **filesystem** constraints for this workspace. |
| **Related folders** | [../AGENTS.md](../AGENTS.md), [../.cursorrules](../.cursorrules), [../.gitignore](../.gitignore) |
| **Status** | **done-docs** |
| **What exists now** | AGENTS.md (non-negotiables, locale, commits, task closeout); `.cursorrules` aligned with Phase 1 doc-only stance. |
| **What is missing** | Optional: `.cursor/rules` if team adopts split rules; explicit link from `.cursorrules` to **master build map** (optional hygiene). |
| **Next required action** | None blocking; keep AGENTS.md in sync when governance **truth boundary** changes. |
| **Dependencies** | Stage 0 (identity / terminology references). |

---

## Stage 2 — Governance Foundation

| Field | Content |
|-------|---------|
| **Purpose** | System **boundaries**, **execution** narrative, **state**, **versioning**, **capabilities**, and **universal entity operations** vocabulary. |
| **Related folders** | [governance/](.) (this folder): [system-boundaries.md](system-boundaries.md), [execution-model.md](execution-model.md), [state-model.md](state-model.md), [versioning-model.md](versioning-model.md), [capability-map.md](capability-map.md), [universal-entity-operations.md](universal-entity-operations.md), [system-signals-dictionary.md](system-signals-dictionary.md), [dependency-map.md](dependency-map.md), [risk-register.md](risk-register.md) |
| **Status** | **done-docs** |
| **What exists now** | Full v0 governance addenda set; README indexes documents; [system-signals-dictionary.md](system-signals-dictionary.md) defines **canonical** v0 system **signal** **names** and **alias** policy; [dependency-map.md](dependency-map.md) (v0) registers system-level entity → entity dependencies (documentation only) with eight **types** (see that file) and **maintenance** **rules**; [risk-register.md](risk-register.md) (v0) registers **known** **risks**, **field** **schema**, **enums**, and **normative** **rules** tied to **signals** and **guardrails**; **Stage 8.5** **entity** rows for **runtime** **readiness**; see **Authority** §1a and Stages 8.5, 9, 10, 13–15 for when the **map** and **register** must be **updated** **(documentation**). |
| **What is missing** | Formal **decision log** file (`logs/decision-log.md`) for long-form ADR-style entries (optional; lifecycle log covers minimal events today). **SAFE UNKNOWN** for any **edge** not in the dependency **table** (see [dependency-map.md](dependency-map.md) §2). |
| **Next required action** | When build order changes, append a **lifecycle-log** row per **Authority** (§1–2). **Stage 8.5** **P0** **is** **documented** (2026-04-27, including [Threat Model v0](../security/threat-model-v0.md) and [Recovery Playbooks v0](../interfaces/recovery-playbooks-v0.md)). Before **Model** / **runtime** (stages **10**, **14**), confirm [Self-Heal v0](../interfaces/self-heal-v0.md) and [Recovery Playbooks v0](../interfaces/recovery-playbooks-v0.md) remain the **plan-only** recovery SoT. Before **Storage**/**RAG** **contracts** with **sensitive** **data**, or **external** **integrations**, re-open [dependency-map.md](dependency-map.md) (§5) **and** [risk-register.md](risk-register.md) (**§2–3**, **§7**). |
| **Dependencies** | Stages 0–1. |

---

## Stage 3 — Registry / Logs / Entity Passports

| Field | Content |
|-------|---------|
| **Purpose** | **Authoritative** rows for **projects** and **documented lifecycle events**; **passport-shaped** identity for agents (cards as in-repo analog). |
| **Related folders** | [../registry/](../registry/), [../logs/](../logs/), [../agents/agent-card-template.md](../agents/agent-card-template.md), [../agents/registry.md](../agents/registry.md) |
| **Status** | **done-docs** (project registry + lifecycle log + agent catalog pattern), **partial-docs** (no standalone `entity-passport.md`; governance README notes **SAFE UNKNOWN** for out-of-tree passports) |
| **What exists now** | `registry/project-registry.md`, `logs/lifecycle-log.md`, agent registry and card template. |
| **What is missing** | Dedicated **entity passport** schema file if required beyond agent cards; `logs/decision-log.md` not yet created. |
| **Next required action** | Replace example **project** row with real project ids when ready; keep lifecycle append-only discipline. |
| **Dependencies** | Stage 2 (state + versioning vocabulary). |

---

## Stage 4 — Control Plane Contract

| Field | Content |
|-------|---------|
| **Purpose** | Define **orchestration**, **routing**, and **policy** surfaces **without** implementing them. |
| **Related folders** | [../control-plane/](../control-plane/) |
| **Status** | **done-docs** |
| **What exists now** | `README.md`, `contract.md`, `components.md`. |
| **What is missing** | Executable control plane **planned-implementation** only. |
| **Next required action** | When runtime work starts, trace APIs in this contract before coding. |
| **Dependencies** | Stages 2–3 (governance + registries for ids and lifecycle). |

---

## Stage 5 — Agent Registry / Agent Factory

| Field | Content |
|-------|---------|
| **Purpose** | **Catalog** of agents and **factory** contract for creating agent **definitions** consistent with registry and governance. |
| **Related folders** | [../agents/](../agents/) |
| **Status** | **done-docs** |
| **What exists now** | `registry.md`, `agent-card-template.md`, `agent-factory-v0.md`, `agent-builder-contract.md`, folder README. |
| **What is missing** | **planned-implementation**: factory automation, runtime agent processes. |
| **Next required action** | Keep registry rows aligned with **state-model** and **versioning-model** when roles change. |
| **Dependencies** | Stages 2–4. |

---

## Stage 6 — Workflow / Task Contract / State Model

| Field | Content |
|-------|---------|
| **Purpose** | **Tasks**, **workflow runs**, **signals** (see [system-signals-dictionary.md](system-signals-dictionary.md) — e.g. **UNKNOWN**, **SAFE UNKNOWN**, **STRUCTURE CHANGE**), and execution **flow** documentation. |
| **Related folders** | [../workflows/](../workflows/), cross-ref [state-model.md](state-model.md) |
| **Status** | **done-docs** |
| **What exists now** | `task-contract-v0.md`, `workflow-v0.md`, `execution-flow.md`, `failure-model-v0.md`, workflows README. |
| **What is missing** | **planned-implementation**: orchestration engine, persistence of run state. |
| **Next required action** | Align workflow docs with **control-plane** contract when either side changes. |
| **Dependencies** | Stages 2, 4–5. |

---

## Stage 7 — Interface / Introspection / Self-* Operations

| Field | Content |
|-------|---------|
| **Purpose** | **Entrypoints** (chat, API, CLI, …) and **truthful** **Self-Describe** / **Self-Check** / **Self-Audit** specifications. |
| **Related folders** | [../interfaces/](../interfaces/) |
| **Status** | **done-docs** (v0 interface + introspection + self-* **contracts**); general product entrypoints remain **planned-implementation** |
| **What exists now** | `introspection-v0.md`, `self-describe-modes.md`, `self-check-v0.md`, `self-audit-v0.md`, `self-heal-v0.md`, README — **P0** path bindings **resolved** (Stage 7.5). |
| **What is missing** | Runnable **chat/API/CLI** implementations and prompts (**planned-implementation**); optional `logs/decision-log.md` for ADR-style notes. |
| **Next required action** | None blocking for v0 **documentation** contracts; implement entrypoints only when downstream stages allow. |
| **Dependencies** | Stages 2–3, 5–6 (SoT files introspection must read). |

---

## Stage 7.5 — Consistency Fix Pass

| Field | Content |
|-------|---------|
| **Purpose** | Resolve **inconsistencies** and **audit findings** surfaced by the **system audit** (introspection, references, terminology, and narrative alignment) so downstream **Security** and later contracts rest on a **coherent** doc surface. |
| **Scope** | **Introspection conflicts**; **broken references**; **terminology mismatches**; **README inconsistencies**; **wording ambiguities**. |
| **Related folders** | Cross-cutting: [../interfaces/](../interfaces/), [../README.md](../README.md), [../security/](../security/), [../registry/](../registry/), [governance/](.) — per finding, not all every time. |
| **Status** | **done-docs** — **Fix Pass v0** **completed**; **re-check audit** **completed** (2026-04-27); **Consistency Fix gate** **passed** (lifecycle event `evt-2026-0002`) |
| **What exists now** | **P0** items in **Audit findings — status after Stage 7.5** **resolved**; residual **P2** only (optional link-style cleanup outside `interfaces/`). |
| **What is missing** | Nothing **blocking** Stage **8** documentation; ongoing hygiene per **Residual** note above. |
| **Next required action** | Proceed with **Stage 8** native security contract work per that stage’s table; no further **7.5** gate actions required. |
| **Dependencies** | **Stage 7** (Interface / Introspection) — audit and introspection surfaces must exist before a formal **consistency** pass. |

**Progression:** advancing to **Stage 8+** requires the **Consistency Fix gate** in **Authority and maintenance rules** (P0 cleared + re-check audit). **Gate passed** 2026-04-27 — see **`logs/lifecycle-log.md`** (`evt-2026-0002`).

---

## Stage 8 — Security / Guardrails / Permissions

| Field | Content |
|-------|---------|
| **Purpose** | **Policies**, access rules, validation, PII, secrets, sandboxing — aligned with architecture docs. |
| **Related folders** | [../security/](../security/), [../web-gpt-sources/09_security.md](../web-gpt-sources/09_security.md), [risk-register.md](risk-register.md) (**cross-cutting** **risk** **posture**) |
| **Status** | **partial-docs** (README + legacy pack clear on **doc-only**; **MARS-native** security contract markdown still thin) |
| **What exists now** | Security folder README (documented / planned stance); extensive **legacy imported** security architecture in `web-gpt-sources`; [risk-register.md](risk-register.md) v0 seed rows for **honesty**, **runtime** **enforcement** **gap**, **compliance** **TBD**. |
| **What is missing** | MARS-native **contract** markdown that states **doc-only** vs **future controls** clearly; no policy engine in-repo. |
| **Next required action** | Expand **MARS-native** security contract files under `security/` and cross-link **AGENTS.md** truth boundary where helpful; keep **Risk** **Register** **security**/**compliance** rows current when **guardrails** or **permissions** **evolve**. |
| **Dependencies** | **Stage 7.5** **gate passed** after **lifecycle-log** closure (**`evt-2026-0002`**); Stages 2, 4 (control plane policy hooks), 7 (interface entrypoints). |

---

## Stage 8.5 — Runtime Readiness Contracts

| Field | Content |
|-------|---------|
| **Purpose** | Prepare MARS for **Tool**, **Model**, and **Runtime** work by **documenting** execution persistence, the **execution bridge** contract surface, **failure** handling, **memory write** rules, **checkpoint/resume**, a **threat model** extension, and **recovery playbooks** extension — **before** those layers assume behaviour that is not yet written down. **No** code, **no** new subsystem folders required by this stage **beyond** markdown contracts or governance extensions (**SAFE UNKNOWN** for exact filenames until authored). |
| **Scope** | **P0** (must be **documented** before **Stage 9**): **Execution Bridge Contract**; **Runtime State Store Contract**; **Failure Handling Model**; **Memory Write Policy**; **Checkpoint / Resume Protocol**; **Threat Model extension**; **Recovery Playbooks extension**. |
| **Related folders** | [governance/](.) (this folder): [master-build-map.md](master-build-map.md), [dependency-map.md](dependency-map.md), [risk-register.md](risk-register.md), [capability-map.md](capability-map.md), [execution-model.md](execution-model.md), [state-model.md](state-model.md); [../mars-runtime/](../mars-runtime/) (Execution Bridge v0); [../storage/](../storage/) (Runtime State Store v0, Checkpoint/Resume); [../memory/](../memory/) (Memory Write Policy v0); [../security/threat-model-v0.md](../security/threat-model-v0.md) (Threat Model v0; **guardrails** / **approval** **gates**); [../interfaces/self-heal-v0.md](../interfaces/self-heal-v0.md) and [../interfaces/recovery-playbooks-v0.md](../interfaces/recovery-playbooks-v0.md) (**plan**-**only** **recovery** **+** **playbook** **patterns**); cross-ref [../workflows/](../workflows/), [../control-plane/](../control-plane/) |
| **Status** | **done-docs** — **7** **of** **7** **Stage** **8.5** **P0** **contract** **files** **authored**; **no** in-repo **runtime** **(Phase** **1** **remains** **doc**-**first;** **RISK**-**V0**-**0005** **/ AGENTS** **honesty** **unchanged**). |
| **What exists now** | [../mars-runtime/execution-bridge-v0.md](../mars-runtime/execution-bridge-v0.md); [../storage/runtime-state-store-v0.md](../storage/runtime-state-store-v0.md); [../workflows/failure-model-v0.md](../workflows/failure-model-v0.md); [../storage/checkpoint-resume-protocol-v0.md](../storage/checkpoint-resume-protocol-v0.md); [../memory/memory-write-policy-v0.md](../memory/memory-write-policy-v0.md); [../security/threat-model-v0.md](../security/threat-model-v0.md); [../interfaces/recovery-playbooks-v0.md](../interfaces/recovery-playbooks-v0.md). [dependency-map.md](dependency-map.md) includes **`execution_bridge`**, **`runtime_state_store`**, **`failure_model`**, **`memory_write_policy`**, **`checkpoint_resume_protocol`**, **`threat_model`**, **`recovery_playbooks`**, **`self_heal`**, and related **edges**; [risk-register.md](risk-register.md) includes **RISK**-**V0**-**0008**–**0013**; [capability-map.md](capability-map.md) C9–C14. |
| **What is missing** | **In-repo** **enforcement,** **durable** **store** **implementations,** and **Tool** / **Model** / **Runtime**-**layer** **code** (see [AGENTS.md](../AGENTS.md))**;** machine schemas **out** of **scope** for **v0** **unless** **adopted** **later** **(SAFE** `UNKNOWN` **/ roadmap**). |
| **Next required action** | **Stage** **9** (Tool) **and** **later** **stages** per **build** **order**; **re**-**open** or **tighten** [risk-register.md](risk-register.md) **rows** (e.g. RISK**-**V0**-**0008, RISK**-**V0**-**0012) **and** [dependency-map.md](dependency-map.md) **when** **new** **surfaces** **land** (tools, runtime, integrations). **Explicit:** no **MARS** **runtime** **implementation** **in** **this** **repo** **in** **Phase** **1** (see [../AGENTS.md](../AGENTS.md)). |
| **Dependencies** | Stages **2**, **6**, **8** (vocabulary, workflow/task contracts, security baseline); [Self-Heal v0](../interfaces/self-heal-v0.md) remains the **plan-only** recovery SoT **alongside** [Recovery Playbooks v0](../interfaces/recovery-playbooks-v0.md) (**no** **contradiction**). |

**Stage 8.5 → 9 (normative, 2026-04-27):** **Stage 8.5** **P0** **Runtime** **Readiness** **documentation** is **complete**; **Tool**-layer **documentation** (**Stage 9**) **may** **proceed** subject to **Self-Heal** **v0,** [Recovery Playbooks v0](../interfaces/recovery-playbooks-v0.md), and **§1a** **map** / **register** **discipline** — **not** a **waiver** for **missing** **in-repo** **tools** / **enforcement** **(still** `planned-implementation` **/ SAFE** `UNKNOWN` **as** **appropriate**). |

**GAP Analysis — priority backlog (documentation planning only)**

| Tier | When | Items |
|------|------|--------|
| **P0** | **Met** **(Stage** **8.5,** **2026-04-27**)** | Execution Bridge; Runtime State Store; Failure Model; Memory Write Policy; Checkpoint / Resume; [Threat Model v0](../security/threat-model-v0.md); [Recovery Playbooks v0](../interfaces/recovery-playbooks-v0.md). |
| **P1** | **After P0**, before or during **runtime preparation** (documentation) | Schema Registry; Run ID / Correlation ID Model; Event Model / Event Log Contract; Prompt / Policy Version Registry; Human Review Queue Contract; Tool Lifecycle Management; Agent Runtime Status. |
| **P2** | **Later / advanced** | Simulation / Dry-Run Mode; Policy-as-Code Layer; Agent Reputation / Performance Scoring; Experiment / A-B Routing; Knowledge Freshness Monitor; Multi-Tenant Boundary Model. |

**Resolved in Stage 10 (Model Layer v0) — authoritative SoT:** **Context Budget Policy** ([../models/context-budget-policy-v0.md](../models/context-budget-policy-v0.md)) and **Cost / Token Budgeting Policy** ([../models/cost-token-budget-v0.md](../models/cost-token-budget-v0.md)) are **documented** under **Stage 10**; **do not** duplicate them as open **Stage 8.5** **P1** **GAP** backlog items. **Stage 10** remains **authoritative** for these contracts.

---

## Stage 9 — Tool Registry / Tool Permissions

| Field | Content |
|-------|---------|
| **Purpose** | **Tool** catalog, MCP/sandbox boundaries, **permission** model for agents invoking tools. |
| **Related folders** | [../tools/](../tools/), refs in [capability-map.md](capability-map.md), [../web-gpt-sources/07_tools_models.md](../web-gpt-sources/07_tools_models.md) |
| **Status** | **near-complete-docs** — **Tool** **Layer** **v0** **+** **Stage** **9.5** **integration** **contracts** **(documentation** **only**). **Label:** **Tool** **Layer** **v0** **+** **Integration** **defined**. **Residual:** **in-repo** **tool** **host** / **MCP** / **enforcement** **engine** **=** `planned-implementation` / **SAFE** **UNKNOWN** (see [../AGENTS.md](../AGENTS.md) + [risk-register.md](risk-register.md) **RISK**-**V0**-**0005**). |
| **What exists now** | [../tools/README.md](../tools/README.md) **(index** **+** **links)**; [../tools/registry.md](../tools/registry.md) **(row** **schema,** **lifecycle,** **planned** **examples)**; [../tools/tool-contract-v0.md](../tools/tool-contract-v0.md); [../tools/tool-execution-model-v0.md](../tools/tool-execution-model-v0.md); [../tools/tool-safety-model-v0.md](../tools/tool-safety-model-v0.md); **Stage** **9.5** **(integration** **&** **validation** **narrative** **only):** [../tools/tool-agent-binding-v0.md](../tools/tool-agent-binding-v0.md) **(agent** **↔** **`allowed_tools`**,** **permission** / **risk** **rules)**,** [../tools/tool-workflow-integration-v0.md](../tools/tool-workflow-integration-v0.md) **(workflow** / **execution**-**flow** **+** **bridge)**,** [../tools/tool-permission-enforcement-v0.md](../tools/tool-permission-enforcement-v0.md) **(permissions** **v0** **on** **tools)**,** [../tools/tool-validation-rules-v0.md](../tools/tool-validation-rules-v0.md) **(PASS** / **FAIL** / **NEED** **HUMAN** **APPROVAL** **)**. [dependency-map.md](dependency-map.md) **`tool_registry`**, **`tool_contract`**, **`tool_execution_model`**, **`tool_safety_model`**, **`approval_gates`**, **`tool_agent_binding`**, **`tool_workflow_integration`**, **`tool_permission_enforcement`**, **`tool_validation_rules`** **rows;** [risk-register.md](risk-register.md) **RISK**-**V0**-**0014**–**0020**. |
| **What is missing** | **In-repo** **tool** **host,** **adapters,** **JSON** **Schema** **files** **or** **OpenAPI** **refs** **where** **marked** **`TBD`**; **machine**-**readable** **registry** **export**; **sandbox** **/** **MCP** **wire** **contracts** **(later** **stages** **/** **implementation**). |
| **Next required action** | **When** **runtime** **or** **MCP** **work** **starts:** **implement** **only** **after** **schemas** **and** **enforcement** **design** **tighten** **—** **re**-**open** [risk-register.md](risk-register.md) **(**§**7**)** **and** [dependency-map.md](dependency-map.md) **(**§**5**)** **per** **new** **edges** **or** **hazards**; **keep** **Stage** **8.5** **P0** **contracts** **aligned** **(Execution** **Bridge,** **Failure** **Model,** **Memory** **Write** **Policy,** **Threat** **Model,** **Checkpoint**/**Resume**). **Explicit:** **no** **MARS** **tool** **runtime** **in** **this** **repo** **in** **Phase** **1** **unless** **evidenced** **elsewhere**. |
| **Dependencies** | **Stage 8.5** **(P0** **documented)**; Stages 5, 8; [Self-Heal v0](../interfaces/self-heal-v0.md); [Recovery Playbooks v0](../interfaces/recovery-playbooks-v0.md) (documentation — **no** **execution**). |

---

## Stage 10 — Model Layer / Provider Routing

| Field | Content |
|-------|---------|
| **Purpose** | **LLM** and **embedding** routing, **model** **identity**, **policy**, **context** **budgets**, **cost**/**token** **budgets** — **documentation** **only** **until** **implementation** **is** **evidenced**. |
| **Related folders** | [../models/](../models/) (**Model** **Layer** **v0** **SoT** **files** **below**), [../web-gpt-sources/07_tools_models.md](../web-gpt-sources/07_tools_models.md), [dependency-map.md](dependency-map.md), [risk-register.md](risk-register.md) |
| **Status** | **partial-docs** — **Stage** **10** **Model** **Layer** **v0** **contracts** **authored** **(markdown** **only**); **OpenRouter** **/** **other** **providers** **remain** **adapter** **options**, **not** **hardcoded** **sole** **backends** **in** **policy** **text**. **Residual:** **no** **in-repo** **provider** **adapter**, **no** **runtime** **router**, **no** **secrets**/**config** **or** **cost** **telemetry** **(see** **[../AGENTS.md](../AGENTS.md)** **+** **RISK**-**V0**-**0005**). |
| **What exists now** | [../models/README.md](../models/README.md); [../models/model-registry-v0.md](../models/model-registry-v0.md); [../models/model-policy-v0.md](../models/model-policy-v0.md); [../models/model-routing-v0.md](../models/model-routing-v0.md); [../models/context-budget-policy-v0.md](../models/context-budget-policy-v0.md); [../models/cost-token-budget-v0.md](../models/cost-token-budget-v0.md); [dependency-map.md](dependency-map.md) **`model_*`** **/** **`context_budget_policy`** **/** **`cost_token_budget`** **rows**; [risk-register.md](risk-register.md) **RISK**-**V0**-**0021**–**0025**; **imported** **legacy** **design** **in** **`web-gpt-sources`**. |
| **What is missing** | **Real** **provider** **adapter** **(implementation** **/** **repo** **evidence**); **runtime** **router** **implementation** **enforcing** **policy** **+** **budgets**; **secrets** **/** **configuration** **handling** **outside** **v0** **docs**; **cost** **/** **token** **telemetry** **and** **Stage** **12** **observability** **SoT** **(planned**-**implementation** **/** **SAFE** **UNKNOWN**). |
| **Next required action** | **When** **implementation** **starts:** **add** **adapters** **and** **enforcement** **only** **after** **schemas** **/** **telemetry** **plans** **tighten** **—** **re**-**open** [risk-register.md](risk-register.md) **(**§**7**)** **and** [dependency-map.md](dependency-map.md) **(**§**5**)** **per** **new** **edges** **or** **hazards**; **keep** **alignment** **with** **[Self-Heal** **v0**](../interfaces/self-heal-v0.md) **and** **[Recovery** **Playbooks** **v0**](../interfaces/recovery-playbooks-v0.md)** **(documentation**). |
| **Dependencies** | Stages 8, 8.5, 9 (permissions, **threat** **model**, **tool** **contracts**, **runtime** **readiness** **affect** **model**/**tool** **context**); [Self-Heal v0](../interfaces/self-heal-v0.md) (documentation — **no** execution or auto-fix). |

---

## Stage 11 — Storage / Memory / RAG

| Field | Content |
|-------|---------|
| **Purpose** | **Durable** stores, memory layer / memory contracts, **RAG** data paths — documented only until adapters exist. |
| **Related folders** | [../storage/](../storage/), [../memory/](../memory/), [../web-gpt-sources/06_memory.md](../web-gpt-sources/06_memory.md), [../web-gpt-sources/08_storage_rag.md](../web-gpt-sources/08_storage_rag.md) |
| **Status** | **partial-docs** — **Stage** **11** **v0** **contracts** **authored** **(markdown** **only);** **no** **backend,** **vector** **DB,** **object** **store,** **or** **RAG** **pipeline** **implemented** **in** **this** **repository** **(see** **[../AGENTS.md](../AGENTS.md)**). **Label:** **Storage** **/** **Memory** **/** **RAG** **design** **contracts** **v0** **(documentation** **only).** |
| **What exists now** | [../storage/README.md](../storage/README.md); [../memory/README.md](../memory/README.md); [../storage/storage-architecture-v0.md](../storage/storage-architecture-v0.md); [../storage/artifact-management-v0.md](../storage/artifact-management-v0.md); [../memory/memory-types-v0.md](../memory/memory-types-v0.md); [../memory/memory-retrieval-v0.md](../memory/memory-retrieval-v0.md); [../memory/memory-lifecycle-v0.md](../memory/memory-lifecycle-v0.md); [../memory/rag-architecture-v0.md](../memory/rag-architecture-v0.md); [../memory/knowledge-freshness-v0.md](../memory/knowledge-freshness-v0.md); **prior** **Stage** **8.5:** [../memory/memory-write-policy-v0.md](../memory/memory-write-policy-v0.md), [../storage/runtime-state-store-v0.md](../storage/runtime-state-store-v0.md), [../storage/checkpoint-resume-protocol-v0.md](../storage/checkpoint-resume-protocol-v0.md); [dependency-map.md](dependency-map.md) **Stage** **11** **entity** **rows**; [risk-register.md](risk-register.md) **RISK**-**V0**-**0026**–**0030**; **imported** **legacy** **in** **`web-gpt-sources`**. |
| **What is missing** | **Remaining** **(documentation** **/ **implementation** **—** **not** **evidenced** **in** **repo):** **backend** **selection** **(pluggable** **adapters** **still** **SAFE** **UNKNOWN**); **vector** **DB** **/ **index** **choice;** **storage** **APIs** **(machine** **contracts,** **adapters);** **RAG** **implementation** **(ingestion,** **embedding,** **indexer,** **enforcement).** |
| **Next required action** | **When** **adapters** **or** **runtime** **work** **starts:** **re**-**open** [risk-register.md](risk-register.md) **(**§**7**)** **and** [dependency-map.md](dependency-map.md) **(**§**5**)** **per** **new** **edges**; **keep** **Memory** **Write** **Policy** **and** **Model** **/ **Context** **contracts** **aligned** **with** **retrieval** **and** **RAG** **narratives**.** |
| **Dependencies** | Stages 8, 8.5 (memory write policy, runtime state), 10 (context **/** **model** **routing);** **registry** for project-scoped data ownership (Stage 3). |

---

## Stage 12 — Observability / Evaluation

| Field | Content |
|-------|---------|
| **Purpose** | **Observability** **(run,** **event,** **tool**-**call,** **audit)** and **Evaluation** **(evals,** **release** **gates,** **quality** **metrics);** **distinct** **from** [../logs/lifecycle-log.md](../logs/lifecycle-log.md) **(governance** **events) **(documentation) .** ** ** |
| **Related folders** | [../observability/](../observability/)**,** [../evaluation/](../evaluation/)**,** [../web-gpt-sources/10_observability_eval.md](../web-gpt-sources/10_observability_eval.md) **(imported) **(documentation) .** ** ** |
| **Status** | **partial-docs** **—** **v0** **markdown** **contracts;** **no** **runtime** **telemetry,** **eval** **runner,** **or** **dashboard** **(see** [../AGENTS.md](../AGENTS.md) **(documentation) ).** ** ** ** |
| **What exists now** | [../observability/run-history-v0.md](../observability/run-history-v0.md)**,** [../observability/event-model-v0.md](../observability/event-model-v0.md)**,** [../observability/tool-call-log-v0.md](../observability/tool-call-log-v0.md)**,** [../observability/audit-trail-v0.md](../observability/audit-trail-v0.md)**,** [../evaluation/evals-v0.md](../evaluation/evals-v0.md)**,** [../evaluation/release-gates-v0.md](../evaluation/release-gates-v0.md)**,** [../evaluation/quality-metrics-v0.md](../evaluation/quality-metrics-v0.md)**,** [../observability/README.md](../observability/README.md)**,** [../evaluation/README.md](../evaluation/README.md)**,** [dependency-map.md](dependency-map.md) **(Stage** **12) **(documentation) +** [risk-register.md](risk-register.md) **(RISK**-**V0**-**0031**–**0035) **(documentation) .** ** ** ** ** |
| **What is missing** (remaining) | **Real** **telemetry** **/ ** **collectors,** **eval** **runner,** **dashboard,** **alerting,** **immutable** **audit** **/ **compliance** **storage** **(not** **in**-**repo) **(documentation) .** ** ** ** ** ** |
| **Next required action** | **On** **runtime** **/ ** **instrumentation** **work: ** re**-**open** or **tighten** [risk-register.md](risk-register.md) **(§7) ** **+** [dependency-map.md](dependency-map.md) **(§5) ** **(documentation) .** ** ** ** ** ** ** ** |
| **Dependencies** | Stages **2** (signals), **6**–**7,** **8.5,** **9**–**11,** [dependency-map.md](dependency-map.md) **(Stage** **12) **(documentation) .** ** ** ** ** ** ** ** |

---

## Stage 13 — Execution Bridge / Runtime Starter

| Field | Content |
|-------|---------|
| **Purpose** | **Bridge** from current **human-in-the-loop** execution (e.g. Web-GPT → Cursor) to future **automated** runtime; **starter** topology docs. |
| **Related folders** | [execution-model.md](execution-model.md), [../mars-runtime/architecture-map.md](../mars-runtime/architecture-map.md), [../web-gpt-sources/11_interfaces_runtime.md](../web-gpt-sources/11_interfaces_runtime.md) |
| **Status** | **done-docs** (concept), **planned-implementation** (bridge code, starters) |
| **What exists now** | Execution model and repository **folder → layer** map; legacy runtime narrative. |
| **What is missing** | Runnable bridge **repository layout** (scripts/services) — **none** in-repo as Phase 1 doc stance. |
| **Next required action** | Define minimal **starter** checklist in `mars-runtime/` docs when Phase 2 opens; no code in map v0. **Documentation:** align **bridge** **artefacts** with **Stage 8.5** **Execution** **Bridge** **Contract** when that contract exists; keep [risk-register.md](risk-register.md) **runtime**-class rows current when the **bridge** story names **new** **hazards**. |
| **Dependencies** | **Stage 8.5** (**Execution** **Bridge** **Contract** **documented** — **or** **explicit** **SAFE** **UNKNOWN** **with** **lifecycle** **flag** **only** if **map** **exception** **is** **approved**); Stages 4–7, 12 (what must be observable when bridge runs). |

---

## Stage 14 — Runtime Implementation

| Field | Content |
|-------|---------|
| **Purpose** | **Processes**, workers, queues, deployment — the **running** shell of MARS. |
| **Related folders** | [../mars-runtime/](../mars-runtime/) |
| **Status** | **planned-docs** (placeholders), **planned-implementation** |
| **What exists now** | `README.md`, `architecture-map.md` only. |
| **What is missing** | All runtime **source**, config, IaC — **not** evidenced in repository. |
| **Next required action** | Begin only after Stages 4, 6–8, 13 contracts are stable enough to avoid rework. **Prerequisite (documentation):** [Self-Heal v0](../interfaces/self-heal-v0.md) (**plan-only** recovery discipline for **runtime**-class **issues** / **risks**); [dependency-map.md](dependency-map.md) must include **runtime**-relevant **entities** and **edges** when they are **staged** (§5); **risk** **review** per [risk-register.md](risk-register.md) **§7.4** with **register** **rows** **updated**. |
| **Dependencies** | Stages 4, 6, 8, **8.5**, 11–13; [Self-Heal v0](../interfaces/self-heal-v0.md) (documentation — **no** execution or auto-fix). |

---

## Stage 15 — External Integrations

| Field | Content |
|-------|---------|
| **Purpose** | **Third-party** systems, credentials, data flow, **integration** entity type per [universal-entity-operations.md](universal-entity-operations.md). |
| **Related folders** | Spreads across [../web-gpt-sources/](../web-gpt-sources/) (e.g. migration, tools); future `integrations/` or per-integration docs **SAFE UNKNOWN** until created. |
| **Status** | **partial-docs** (legacy + scattered references), **planned-docs** (central integration registry) |
| **What exists now** | Imported migration and tool docs; **governance** entity type **integration**. |
| **What is missing** | Single **integration catalog** in-repo; explicit **SAFE UNKNOWN** for live credentials and endpoints. |
| **Next required action** | Add integration appendix or registry when first real integration is scoped. **Prerequisite (documentation):** [risk-register.md](risk-register.md) **§7.3** (**new** **external** **integration** **risk** **review**). |
| **Dependencies** | Stages 8–11, 14 (where integrations attach in running system). |

---

## Stage 16 — Pilot Project

| Field | Content |
|-------|---------|
| **Purpose** | **End-to-end** validation project with **acceptance** criteria spanning multiple layers. |
| **Related folders** | [../registry/project-registry.md](../registry/project-registry.md) (project row), [../web-gpt-sources/14_roadmap.md](../web-gpt-sources/14_roadmap.md) |
| **Status** | **planned-docs** (roadmap exists; pilot not declared beyond example registry row) |
| **What exists now** | Roadmap markdown; example `mars-core` row in project registry. |
| **What is missing** | Named pilot **charter**, success metrics, and **lifecycle** entries for pilot **phase transitions**. |
| **Next required action** | Register pilot as **project_id** and log **phase.transition** when governance agrees. |
| **Dependencies** | Stages 0–15 per pilot scope (typically requires **14** in scope for runtime-backed pilots). |

---

## Changelog (documentation)

| Date | Change |
|------|--------|
| 2026-04-27 | [Self-Heal v0](../interfaces/self-heal-v0.md) — **plan-only** recovery / fix **plans** from **Self-Check**, **Self-Audit**, **Risk** **Register**, **Dependency** **Map**, **Lifecycle** **Log**; **Authority** §1a; **Stages** **7** (artefact list), **9**, **10**, **14** **prerequisites** and **dependencies**; **no** execution or auto-fix. |
| 2026-04-27 | [risk-register.md](risk-register.md) v0 — explicit **risk** **register**; **Authority** §1a **paired** with **dependency** **map**; Stage **2** artefact list; **prerequisites** for Stages **9**, **10**, **11**, **14**, **15**; Stage **8** **cross**-**ref**; **signal**-driven **rules** (**SECURITY** **RISK**, **NEED** **HUMAN** **APPROVAL**, **integration**, **runtime**). |
| 2026-04-27 | [dependency-map.md](dependency-map.md) v0 — system-level entity **→** **entity** map (documentation only); **Authority** §1a; Stage 2 and stages 9, 10, 14 **prerequisites**; Self-Heal / Risk Register / Tool / Model / **runtime** (documentation) alignment. |
| 2026-04-27 | **Master Build Map v0** — stages 0–16, authority rules, audit blockers, dependency narrative. |
| 2026-04-27 | **Stage 7.5 — Consistency Fix Pass**; **Consistency Fix gate** (no Stage **8+** until P0 cleared + re-check audit); Stage **8** dependencies updated. |
| 2026-04-27 | **Stage 7.5 gate closed** — audit findings marked **RESOLVED**; Stages **7** / **7.5** / **8** status tables updated; **lifecycle-log** `evt-2026-0002` records gate pass. |
| 2026-04-27 | [system-signals-dictionary.md](system-signals-dictionary.md) v0 — **canonical** system signal vocabulary and **STRUCTURE** naming normalization. |
| 2026-04-27 | **Stage 8.5 — Runtime Readiness Contracts**; **GAP** **Analysis** **P0**/**P1**/**P2** **backlog**; **Stage 9** **gate** (**8.5** **P0** **before** **Tool** **docs**); **Authority** §1a **Runtime** **Readiness**; **Stages** **11**, **13** **cross**-**refs**; [dependency-map.md](dependency-map.md), [risk-register.md](risk-register.md), [capability-map.md](capability-map.md) **alignment**. |
| 2026-04-27 | **Stage** **8.5** **partial-docs** — [**Execution** **Bridge** **v0**](../mars-runtime/execution-bridge-v0.md), [**Runtime** **State** **Store** **v0**](../storage/runtime-state-store-v0.md) (**2**/ **7** **P0**); **dependency-map** / **risk-register** / **Stage** **8.5** **table** **updated**. |
| 2026-04-27 | **Stage** **8.5** **partial-docs** — [**Failure** **Handling** **Model** **v0**](../workflows/failure-model-v0.md), [**Checkpoint** / **Resume** **Protocol** **v0**](../storage/checkpoint-resume-protocol-v0.md) (**4**/**7** **P0**); **dependency-map** (**`failure_model`**, **`checkpoint_resume_protocol`**, **`execution_flow`**, **`state_model`** **edges**); **risk-register** **RISK**-**V0**-**0008**–**0010**; **Stage** **8.5** **table** **updated**. |
| 2026-04-27 | **Stage** **8.5** **partial-docs** — [**Memory** **Write** **Policy** **v0**](../memory/memory-write-policy-v0.md) (**5**/**7** **P0**); **dependency-map** **`memory_write_policy`** (incl. **`project_registry`**, **`lifecycle_log`**, **`runtime_state_store`**, **`checkpoint_resume_protocol`**) **+** **risk** **(e.g.)** **RISK**-**V0-0011**; **Stage** **8.5** **5**/7. |
| 2026-04-27 | **Stage** **8.5** **done-docs** **(7/7** **P0)** — [threat-model-v0.md](../security/threat-model-v0.md), [recovery-playbooks-v0.md](../interfaces/recovery-playbooks-v0.md); **Authority** **§1a** **(no** **8.5**-**P0** **block** **on** **Stage** **9** **doc**); **Stage** **9** **table** **unblocked**; **RISK**-**V0-0012/0013** **mitigated**; **runtime** **implementation** **still** **absent** **(AGENTS**). |
| 2026-04-27 | **Stage** **9** **partial-docs** — **Tool** **Layer** **v0** **([../tools/registry.md](../tools/registry.md),** **[../tools/tool-contract-v0.md](../tools/tool-contract-v0.md),** **[../tools/tool-execution-model-v0.md](../tools/tool-execution-model-v0.md),** **[../tools/tool-safety-model-v0.md](../tools/tool-safety-model-v0.md),** **[../tools/README.md](../tools/README.md))**; **dependency-map** **/** **risk-register** **updates**; **remaining** **work:** **tool** **runtime,** **schemas,** **MCP**/**adapter** **contracts** **(not** **Phase** **1** **in-repo** **unless** **evidenced**). |
| 2026-04-27 | **Stage** **9** **→** **near-complete-docs**; **Stage** **9.5** **(integration** **only) —** **[tool-agent-binding-v0.md](../tools/tool-agent-binding-v0.md),** **[tool-workflow-integration-v0.md](../tools/tool-workflow-integration-v0.md),** **[tool-permission-enforcement-v0.md](../tools/tool-permission-enforcement-v0.md),** **[tool-validation-rules-v0.md](../tools/tool-validation-rules-v0.md);** **label** **Tool** **Layer** **v0** **+** **Integration** **defined;** [dependency-map.md](dependency-map.md) **+** [risk-register.md](risk-register.md) **(RISK**-**V0**-**0018**–**0020**). |
| 2026-04-27 | **Stage** **10** **partial-docs** — **[../models/model-registry-v0.md](../models/model-registry-v0.md)**, **[../models/model-policy-v0.md](../models/model-policy-v0.md)**, **[../models/model-routing-v0.md](../models/model-routing-v0.md)**, **[../models/context-budget-policy-v0.md](../models/context-budget-policy-v0.md)**, **[../models/cost-token-budget-v0.md](../models/cost-token-budget-v0.md)**, **[../models/README.md](../models/README.md)**; [dependency-map.md](dependency-map.md) **Model** **Layer** **entities**; [risk-register.md](risk-register.md) **RISK**-**V0**-**0021**–**0025**; **remaining:** **provider** **adapters**, **runtime** **router**, **secrets**/**config**, **cost** **telemetry**. |
| 2026-04-28 | **Stage** **11** **partial-docs** — **storage**/**memory**/**RAG** **v0** **([../storage/storage-architecture-v0.md](../storage/storage-architecture-v0.md)**, **[../storage/artifact-management-v0.md](../storage/artifact-management-v0.md)**, **[../memory/memory-types-v0.md](../memory/memory-types-v0.md)**, **[../memory/memory-retrieval-v0.md](../memory/memory-retrieval-v0.md)**, **[../memory/memory-lifecycle-v0.md](../memory/memory-lifecycle-v0.md)**, **[../memory/rag-architecture-v0.md](../memory/rag-architecture-v0.md)**, **[../memory/knowledge-freshness-v0.md](../memory/knowledge-freshness-v0.md)**);** [dependency-map.md](dependency-map.md) **/** [risk-register.md](risk-register.md) **(RISK**-**V0**-**0026**–**0030);** **Stage** **11** **table** **updated** **(remaining** **work** **in** **map**).** |
| 2026-04-28 | **Stage** **12** **partial-docs** **—** **observability** + **evaluation** **v0;** **(Run** **History,** **Event** **Model,** **Tool** **Call** **Log,** **Audit** **Trail,** **Evals,** **Release** **Gates,** **Quality** **Metrics) **(documentation) +** [dependency-map.md](dependency-map.md) / [risk-register.md](risk-register.md) **(RISK**-**V0**-**0031**–**0035) **(documentation) .** ** |

---

*End of Master Build Map v0.*
