# MARS — Run History v0

**Status:** **documented** — contract for **per-run** observability **records**; **not** a schema file, log format, or **implemented** storage.

**Version:** v0. Revisable per [governance/versioning-model.md](../governance/versioning-model.md) and [governance/master-build-map.md](../governance/master-build-map.md).

**SAFE UNKNOWN:** How run history is **materialised** in a **future** product (DB tables, object keys, event projection) is **unregistered** in-repo until a later contract or code evidences it.

---

## 1. Purpose

**Run history** is the **authoritative narrative** of what happened during a **workflow run** in execution terms: identity, time bounds, **status**, participants, **signal** **emissions** (vocabulary from [governance/system-signals-dictionary.md](../governance/system-signals-dictionary.md)), and **pointers** to **artefacts**. It is **distinct** from the **append-only governance** [../logs/lifecycle-log.md](../logs/lifecycle-log.md) (build-order, gate, and high-level process events).

Goals:

- **Correlate** a single `run_id` with **task**, **project**, and **workflow** **identifiers** for operators and audits.
- **Support** post-hoc **evaluation** and **incident** review without inventing facts (honesty per [../AGENTS.md](../AGENTS.md)).
- **Align** with **durable** execution state in the **Runtime State Store** ([../storage/runtime-state-store-v0.md](../storage/runtime-state-store-v0.md)) and **handoffs** in the **Execution Bridge** ([../mars-runtime/execution-bridge-v0.md](../mars-runtime/execution-bridge-v0.md)).

There is **no** **in-repo** **runtime** **logging** **implementation**; this file defines **documentation** **field** **semantics** **only**.

---

## 2. Run history fields (v0)

| Field | Meaning |
|-------|--------|
| **run_id** | Stable **identifier** of one **workflow** **run**; must **correlate** with the same token in the Runtime State Store and **bridge** **I/O** **(documentation)**. |
| **task_id** | The **Task** that **owns** the run, per [../workflows/task-contract-v0.md](../workflows/task-contract-v0.md). |
| **project_id** | **Authoritative** project scope, per [../registry/project-registry.md](../registry/project-registry.md). |
| **workflow_id** | **Workflow** **template** or **class** the run **instantiates**, per [../workflows/workflow-v0.md](../workflows/workflow-v0.md). |
| **status** | **Terminal** or **in-flight** run **outcome** in terms compatible with [../workflows/workflow-v0.md](../workflows/workflow-v0.md) and **state** [governance/state-model.md](../governance/state-model.md) **(documentation** **pairing**). |
| **started_at** | **Time** the run was **admitted** or **began** execution **(documentation** **—** no clock**/**TZ** **enforcement** **v0**). |
| **finished_at** | **Time** the run **ended** (success, failure, abort) **or** **empty** if not finished. |
| **involved_agents** | **Set** of **agent** **role** / **id** **values** that **participated** in the run **(registry**-**aligned,** [../agents/registry.md](../agents/registry.md))**. |
| **involved_tools** | **Set** of **`tool_id`** **values** **invoked** in the run **(see** [../tools/registry.md](../tools/registry.md))**. |
| **selected_models** | **Set** of **`model_id`** **(or** **equivalent** **routed** **identity)** **per** [../models/model-registry-v0.md](../models/model-registry-v0.md) and **routing** [../models/model-routing-v0.md](../models/model-routing-v0.md). |
| **signals** | **Ordered** or **set**-wise **emissions** of **named** **system** **signals** (canonical names in [governance/system-signals-dictionary.md](../governance/system-signals-dictionary.md)); may **compact** to **per**-**type** **counts** **(future** **telemetry** **convention,** **SAFE** **UNKNOWN** **v0**). |
| **artifacts** | **References** to **outputs** **(see** [../storage/artifact-management-v0.md](../storage/artifact-management-v0.md))** —** **URIs,** **handles,** or **ids** **that** **resolve** without embedding **content** in the **run** **history** **row** **itself** **(design**). |

---

## 3. Relation to Runtime State Store

- The **Runtime** **State** **Store** is the **SoT** for **durable** **per-run** / **per-task** **state** and **resumable** **facets** ([../storage/runtime-state-store-v0.md](../storage/runtime-state-store-v0.md)). **Run** **history** **(this** **contract)** is a **summary** or **view**-level **narrative** that should be **consistently** **derivable** from **(or** **indexable** **alongside**)** that **state** when **runtime** **exists** — it is **not** a second **authoritative** **governance** **log** (that **remains** the [append-only lifecycle log](../logs/lifecycle-log.md)).
- If run history and store **records** **disagree,** operators should **treat** the **durable** state store **(plus** raw **invocation** and **artefact** **evidence)** as **execution** SoT, and **treat** **gaps** as [risk register](../governance/risk-register.md) and [Self-Audit v0](../interfaces/self-audit-v0.md) scope (documentation).

---

## 4. Relation to lifecycle log

- **Lifecycle** log (**append**-**only,** [../logs/lifecycle-log.md](../logs/lifecycle-log.md)**):** **governance** **events** **(stage** **gates,** **map** **revisions,** **major** **adoptions**). **Run** **history** does **not** **replace** or **duplicate** that **purpose** — a **run** may **span** many **governance** **revisions**; a **single** **governance** **row** may **affect** no **runs.**
- **Material** **links** (e.g. “this **run** **touched** a **governed** **adoption**”**) **may** be **cited** **in** **either** **artefact** **by** **reference** **ids** **(v0: **narrative** **only**).

---

## 5. No runtime logging implementation (Phase 1)

- **No** **log** **shipper,** **index,** **database** **table,** or **exporter** **is** **specified** **or** **required** **in** this **repository** for **run** **history.**
- **Event**-**level** **emitters** are **covered** in [event-model-v0.md](event-model-v0.md) **(documentation);** **tool**-**scoped** **streams** in [tool-call-log-v0.md](tool-call-log-v0.md).

---

*End of Run History v0.*

