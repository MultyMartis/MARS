# MARS — Runtime State Store v0

**Status:** **documented** — **contract only**. This file defines **what** execution-related **state** must be **durable** for **audit**, **resume**, and **honest** reporting. It does **not** specify a database product, schema DDL, or running service. Per [../AGENTS.md](../AGENTS.md), **no** storage implementation is claimed unless adapters or code exist in-repo.

**Version:** v0. Revisable per [../governance/versioning-model.md](../governance/versioning-model.md) and [../governance/master-build-map.md](../governance/master-build-map.md).

---

## 1. Purpose

The **Runtime State Store** is the **normative persistence layer** for **execution-time** facts: enough **structured** history to **reconstruct** what happened on a **run**, **recover** after interruption **when** policy allows, and **avoid** silent loss or contradiction with [../governance/state-model.md](../governance/state-model.md).

It is **distinct** from:

- **[../logs/lifecycle-log.md](../logs/lifecycle-log.md)** — **governance** and **repository** lifecycle events (append-only **design** log).
- **Observability / metrics** (Stage 12) — **operational** telemetry; may **correlate** with **`run_id`** but **must not** replace **authoritative** **run** **state** **for** **resume** **semantics** **unless** **explicitly** **declared** **later**.

---

## 2. What must be stored (minimum logical record)

**SAFE UNKNOWN:** Physical schema, column names, and stores are **TBD** until implementation. The following **logical** **facets** are **required** by this contract for any **persisted** **run** **artefact** **that** **claims** **MARS** **compatibility**:

| Facet | Description |
|-------|-------------|
| **`task_id`** | Stable identifier per [../workflows/task-contract-v0.md](../workflows/task-contract-v0.md). |
| **`run_id`** | Correlates **all** records for one **workflow** **run** / **execution** **instance**. **SAFE UNKNOWN:** format (UUID, slug) until a **Run ID / Correlation ID Model** (Stage 8.5 P1 backlog) lands. |
| **`state`** | Current **task** and/or **run** **state** **consistent** **with** [../governance/state-model.md](../governance/state-model.md) **vocabulary** (e.g. task **T4** **executing**, run **executing**). |
| **`checkpoints`** | **Ordered** **checkpoint** **records** allowing **resume** **when** **Checkpoint / Resume Protocol** (Stage 8.5 P0 **TBD**) **defines** **boundaries**. Each checkpoint **must** be **immutable** **once** **written** **(append)** — see **§6**. |
| **`results`** | **Outputs** **linked** **to** **steps** **(result** **payloads**, **references** **to** **artifacts)** **compatible** **with** [../mars-runtime/execution-bridge-v0.md](../mars-runtime/execution-bridge-v0.md) **output** **contract**. |
| **`errors`** | **Structured** **failure** **information** **(classification**, **message**, **signal** **codes** **where** **applicable)** **aligned** **with** **failure** **taxonomy** **when** **Failure** **Handling** **Model** (Stage **8.5** **P0** **TBD**) **exists**. |

Implementations **may** store **additional** fields (timestamps, executor id, trace ids) **without** violating v0 **if** **minimum** **facets** **remain** **available**.

---

## 3. Lifecycle operations (documentation)

| Operation | Meaning |
|-----------|---------|
| **create** | **Initialize** a **new** **run** **record** **with** **`run_id`**, **`task_id`**, **initial** **`state`**, **and** **empty** **or** **bootstrap** **checkpoint** **metadata** **as** **policy** **requires**. |
| **update** | **Transition** **`state`**, **append** **results** **slices**, **or** **append** **errors** **without** **destroying** **prior** **committed** **facts** **(see** **§6)**. |
| **checkpoint** | **Append** an **immutable** **checkpoint** **record** **at** **approved** **boundaries** **(workflow** **/ execution-bridge** **alignment)**. |
| **finalize** | **Mark** **run** **or** **task** **terminal** **state** **(success**, **failure**, **cancelled)** **with** **no** **silent** **overwrite** **of** **prior** **history**. |

**Parked** and **resume** behaviour aligns with [../governance/state-model.md](../governance/state-model.md) **T10** **and** **Execution** **Bridge** **pause** **semantics** **([../mars-runtime/execution-bridge-v0.md](../mars-runtime/execution-bridge-v0.md))**.

---

## 4. Relations to other artefacts

| Artefact | Relation |
|----------|----------|
| **[../governance/state-model.md](../governance/state-model.md)** | **`state`** **fields** **and** **transitions** **in** **stored** **records** **must** **not** **contradict** **governance** **task**/**run** **states**. |
| **[../logs/lifecycle-log.md](../logs/lifecycle-log.md)** | **Governance** **events** (**gate** **pass**, **registry** **change**) **vs** **runtime** **durability** — **do** **not** **merge** **roles**; **major** **store** **policy** **changes** **may** **append** **a** **lifecycle** **row** **per** [../governance/master-build-map.md](../governance/master-build-map.md). |
| **[../mars-runtime/execution-bridge-v0.md](../mars-runtime/execution-bridge-v0.md)** | **Bridge** **outputs** (**result**, **status**, **artifacts**, **signals**) **map** **into** **stored** **results**/**errors**/**state** **updates**. |

---

## 5. Rules: no silent overwrite; append / versioning

1. **No silent overwrite** — **Committed** **history** **(checkpoints**, **append-only** **error**/**result** **streams)** **must** **not** **be** **replaced** **or** **erased** **without** **an** **explicit** **policy** **(e.g.** **retention**, **legal** **hold)** **documented** **outside** **this** **v0** **file**.
2. **Append-first** — **Updates** **that** **revise** **interpretation** **must** **append** **a** **new** **record** **or** **version** **pointer** **rather** **than** **mutating** **prior** **facts** **in** **place**.
3. **Versioning logic** — When **correcting** **errors**, **append** **a** **superseding** **entry** **that** **references** **the** **prior** **record** **id** **(logical** **or** **opaque)**; **SAFE UNKNOWN:** **exact** **mechanism** **until** **implementation**.

---

## 6. SAFE UNKNOWN — storage backend

- **Database**, **object** **store**, **filesystem** **layout**, **encryption**, **replication** — **not** **chosen** **by** **this** **contract**.
- **Retention**, **backup**, **disaster** **recovery** — **governance**/**risk** **register** **concerns**; **see** [../governance/risk-register.md](../governance/risk-register.md).

---

## 7. Changelog (documentation)

| Date | Change |
|------|--------|
| 2026-04-27 | **Runtime State Store v0** — purpose, stored facets, lifecycle, relations, overwrite rules, backend **SAFE UNKNOWN**. |

---

*End of Runtime State Store v0.*
