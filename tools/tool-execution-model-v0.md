# MARS — Tool Execution Model v0

**Status:** **documented** — **contract only**. Describes **how** **tool** **invocations** **relate** **to** **the** **Execution** **Bridge**, **durable** **runtime** **state**, **checkpoints**, **and** **the** **Failure** **Handling** **Model**. **No** runner, **no** queue, **no** MCP host in-repo for Phase 1.

**Version:** v0. Revisable per [../governance/versioning-model.md](../governance/versioning-model.md) and [../governance/master-build-map.md](../governance/master-build-map.md).

---

## 1. Purpose

- Place **tool** **steps** **inside** **the** **same** **execution** **story** **as** **other** **bridge** **executors** ([../mars-runtime/execution-bridge-v0.md](../mars-runtime/execution-bridge-v0.md) **§2**): **API**, **Scripts**, **internal** helpers, **and** **integrations** **map** **to** **executor** **categories** **at** **dispatch** **time** **(documentation)**.
- Separate **what** **must** **land** **in** **the** **Runtime** **State** **Store** **vs** **what** **may** **append** **to** **the** **lifecycle** **log** **(governance)** **per** **layer** **SoT**.

---

## 2. Tool invocation via Execution Bridge

1. **Control** **Plane** **/** **workflow** **selects** **a** **plan** **step** **that** **names** **a** **tool_id** **(or** **resolves** **one)** **consistent** **with** [../workflows/workflow-v0.md](../workflows/workflow-v0.md) **and** [../workflows/task-contract-v0.md](../workflows/task-contract-v0.md).
2. **The** **bridge** **assembles** **Task** **+** **Plan** **slice** **+** **Context** **per** [../mars-runtime/execution-bridge-v0.md](../mars-runtime/execution-bridge-v0.md) **§3**, **including** **`run_id`** **and** **policy** **references** **(guardrails,** **gates**).
3. **Tool** **adapter** **(future** **implementation)** **maps** **the** **step** **to** **[tool-contract-v0.md](tool-contract-v0.md)** **input** **envelope** **and** **returns** **the** **output** **envelope** **(result,** **artifacts,** **status,** **signals**).
4. **Bridge** **output** **facets** **must** **not** **drop** **signals** **required** **by** [../mars-runtime/execution-bridge-v0.md](../mars-runtime/execution-bridge-v0.md) **§6** **when** **propagating** **to** **persistence** **or** **reporting**.

**Unsupported** **executor** **or** **unmapped** **tool** **type** **must** **surface** **`UNKNOWN`** **or** **`SAFE UNKNOWN`** **per** **bridge** **§2**, **not** **silent** **fallback**.

---

## 3. Synchronous vs asynchronous execution

| Mode | Definition (v0) | Notes |
|------|-----------------|-------|
| **Sync** | **Caller** **blocks** **until** **tool** **output** **envelope** **is** **available** **or** **timeout** **failure** **fires**. | **Timeout** **is** **a** **first-class** **failure** **type** **([../workflows/failure-model-v0.md](../workflows/failure-model-v0.md)** **§2** **/** **bridge** **§5**). |
| **Async** | **Invocation** **returns** **a** **handle** **(job** **id,** **callback** **token** **—** **`SAFE UNKNOWN`** **format)** **before** **terminal** **outcome** **is** **known**. | **State** **store** **must** **record** **pending** **step** **/** **job** **correlation** **under** **`run_id`** **when** **persistence** **is** **required** **([../storage/runtime-state-store-v0.md](../storage/runtime-state-store-v0.md))**. |

**Partial** **outcomes** **during** **async** **work** **use** **`status`** **`partial`** **and** **failure** **taxonomy** **per** **Failure** **Model**; **resume** **rules** **apply** **(§4)**.

---

## 4. Interaction with Runtime State Store and checkpoint / resume

| Concern | Contract |
|---------|----------|
| **Runtime State Store** | **Updates** **to** **`state`**, **`results`**, **`errors`**, **and** **append-only** **streams** **follow** [../storage/runtime-state-store-v0.md](../storage/runtime-state-store-v0.md) **§3–§6**; **tool** **outputs** **map** **into** **`results`** **/** **`errors`** **consistent** **with** **bridge** **§4**. |
| **Checkpoint / Resume** | **Checkpoint** **records** **at** **tool** **boundaries** **when** **policy** **requires** **durable** **resume** **points** **—** [../storage/checkpoint-resume-protocol-v0.md](../storage/checkpoint-resume-protocol-v0.md) **§2–§4**; **`step`** **must** **identify** **the** **plan** **position** **including** **tool** **invocation**. |
| **Failure Model** | **Retry**, **abort**, **escalate**, **fallback** **and** **idempotency** **obligations** **are** **delegated** **to** [../workflows/failure-model-v0.md](../workflows/failure-model-v0.md) **—** **this** **file** **does** **not** **redefine** **numeric** **caps** **or** **backoff**. |

---

## 5. Retry rules (delegation)

- **All** **retry** **semantics** **(max** **attempts,** **when** **retry** **is** **forbidden,** **STRUCTURE** **CHANGE** **after** **replan,** **SECURITY** **RISK** **→** **escalate)** **are** **normative** **in** [../workflows/failure-model-v0.md](../workflows/failure-model-v0.md) **§3–§4**.
- **Tool** **layer** **adds** **only** **the** **obligation** **that** **orchestration** **treats** **each** **tool** **invocation** **as** **a** **step** **subject** **to** **those** **rules** **and** **§5** **idempotency** **(duplicate** **tool** **calls**).

---

## 6. Idempotency expectations

- **Design** **must** **assume** **at-least-once** **delivery** **unless** **a** **tool** **is** **proven** **idempotent** **or** **carries** **deduplication** **/ idempotency** **tokens** **per** [../workflows/failure-model-v0.md](../workflows/failure-model-v0.md) **§5** **and** [../storage/checkpoint-resume-protocol-v0.md](../storage/checkpoint-resume-protocol-v0.md) **§4**.
- **Concrete** **token** **formats** **—** **`SAFE UNKNOWN`** **until** **Stage** **9+** **or** **implementation** **fixes** **them**.

---

## 7. Logging: lifecycle-log vs runtime state

| Surface | Use for tool execution (v0) |
|---------|---------------------------|
| **[../logs/lifecycle-log.md](../logs/lifecycle-log.md)** | **Governance** **events**: **registry** **lifecycle** **transitions**, **material** **policy** **changes**, **gate** **outcomes** **when** **map** **authority** **requires** **logging** — **not** **per**-**invocation** **telemetry** **by** **default**. |
| **Runtime State Store** | **Per-run** **facts**: **invocation** **status**, **errors**, **checkpoint** **metadata**, **pointers** **to** **artifacts** **needed** **for** **resume** **and** **audit** **of** **execution**. |

**Do** **not** **use** **lifecycle** **log** **as** **a** **substitute** **for** **`results`** **/** **`errors`** **for** **run** **replay** **when** **the** **Runtime** **State** **Store** **is** **the** **SoT** **for** **execution** **durability**.

---

## 8. Changelog (documentation)

| Date | Change |
|------|--------|
| 2026-04-27 | **Tool** **Execution** **Model** **v0** — **bridge** **mapping**, **sync/async**, **state** **/** **checkpoint** **/** **failure** **pairing**, **retry** **delegation**, **idempotency**, **logging** **split**. |

---

*End of MARS Tool Execution Model v0.*
