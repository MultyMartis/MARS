# MARS — Tool–Agent Binding v0

**Status:** **documented** — **contract only**. Specifies how **agents** **declare** which **tools** they may use, how that declaration **maps** to the **Tool Registry** and **safety** metadata, and **normative** **rules** for **consistency** with **permissions** and **risk** **level**. **No** runtime, **no** automatic binding service in this repository for Phase 1.

**Version:** v0. Revisable per [../governance/versioning-model.md](../governance/versioning-model.md) and [../governance/master-build-map.md](../governance/master-build-map.md).

**SAFE UNKNOWN:** Machine schema for agent cards, registry export format, and runtime enforcement of bindings remain **TBD** until specified elsewhere.

---

## 1. Purpose

- Make **agent → tool** **allowlists** **explicit** at **design** **time** so **routing**, **Control** **Plane** **narrative**, and **Tool** **Layer** **contracts** do not rely on **implicit** **capability**.
- Pair **agent** **declarations** with [registry.md](registry.md) **rows** (`allowed_agents`, `required_permissions`, `risk_level`) **without** **contradiction**.

---

## 2. How agents declare usable tools

- Each **agent** **definition** that may invoke tools **must** include an **allowlist** of **tool** **identities** the agent is **permitted** to **request** in **orchestrated** **execution** (documentation and future registry-backed cards).

- **Field name (v0):** **allowed_tools** — ordered or unordered list of **`tool_id`** **strings** matching [registry.md](registry.md) **(or** **empty** **if** **the** **agent** **never** **invokes** **tools**). **Alignment** **with** the **agent** **card** **section** **`tools`** in [../agents/agent-card-template.md](../agents/agent-card-template.md): the **card** **lists** the **same** **logical** **set** **as** **`allowed_tools`** **(naming** **`tools`** **on** **the** **card,** **mapping** **agent** **→** **`allowed_tools`** **in** **this** **document** **for** **orchestration** **clarity**).

- **Source** **of** **truth** for **which** **tools** **exist** and **their** **policy** **columns** is the **Tool** **Registry**; **agent** **cards** / **rows** in [../agents/registry.md](../agents/registry.md) **reference** **tool** **ids** **only** **as** **declared** **allowlists**, **not** **as** **a** **second** **tool** **catalogue**.

---

## 3. Mapping: agent → allowed_tools

| Concept | Description (v0) |
|---------|------------------|
| **agent** | Identified by **role** and/or **registry** **id** per [../agents/registry.md](../agents/registry.md) **(documentation)**. |
| **allowed_tools** | **Finite** **set** **of** **`tool_id`** **values** **from** **[registry.md](registry.md)** **(or** **empty).** **Any** **invocation** **not** **in** **this** **set** **is** **undeclared** **for** **that** **agent** **(see** **§4.3**). |
| **Cross-check** | For each **`tool_id`** **in** **`allowed_tools`**, the **registry** **row** **(when** **present)** **is** **consulted** **for** **`allowed_agents`**, **`required_permissions`**, **`risk_level`**, **and** **`approval_required`**. **Design** **must** **be** **consistent** **(see** **§4**). |

---

## 4. Normative rules

### 4.1 Tools must match permissions

- The **agent's** **effective** **granted** **permission** **scopes** **(see** [../security/permissions-v0.md](../security/permissions-v0.md) **and** **agent** **card** **`permissions`**) **must** **include** **every** **scope** **listed** **in** the **registry** **`required_permissions`** **for** **each** **tool** **in** **`allowed_tools`**, **unless** **the** **tool** **row** **explicitly** **allows** **narrower** **interpretation** **(documentation** **only;** **no** **default** **superuser** **per** **permissions** **v0** **§4.1**).
- If **a** **tool** **requires** **a** **scope** **the** **agent** **does** **not** **hold,** that **tool** **must** **not** **appear** **in** **`allowed_tools`** **for** **that** **agent,** **or** **the** **agent** **card** **must** **be** **corrected** **before** **the** **agent** **is** **routed** **to** **use** **that** **tool** **(fail** **closed** **at** **design** **time**; **future** **runtime** **should** **deny** **with** **a** **canonically** **named** **signal** **per** **[../governance/system-signals-dictionary.md](../governance/system-signals-dictionary.md)** **and** **[tool-permission-enforcement-v0.md](tool-permission-enforcement-v0.md)**).

### 4.2 Tools must match risk_level (composite)

- The **Task** (or **equivalent** **orchestrated** **context**) **may** **declare** a **risk** **envelope** **(e.g.** **task** **`risk_level`** per [../workflows/task-contract-v0.md](../workflows/task-contract-v0.md) **and** [../security/approval-gates.md](../security/approval-gates.md) **—** **exact** **composite** **rule** **is** **governed** **by** [tool-safety-model-v0.md](tool-safety-model-v0.md) **and** **approval** **gates**).
- If a **tool**'s registry `risk_level` or **composite** **rule** is **incompatible** with the **run**'s **risk** and **approval** **posture,** the **binding** is **invalid** for **that** **run** — **do** **not** **plan** **that** **tool** for **that** **Task** without **replanning,** **STRUCTURE** **CHANGE,** or **HITL** per **governing** **contracts** (documentation level).

### 4.3 Agent cannot use undeclared tools

- An **agent** **must** **not** **request** **or** **cause** **invocation** **of** **a** **`tool_id`** **that** **is** **not** **in** **its** **`allowed_tools`** **(including** **aliases** **/** **resolved** **ids** **—** **same** **logical** **tool**).
- **Undeclared** **use** **is** **a** **binding** **violation**; **in** **a** **future** **runtime,** **expected** **outcome** **is** **deny** **(no** **execution)** **and** **signal** **emission** **per** **validation** **and** **security** **contracts** **(see** **[tool-validation-rules-v0.md](tool-validation-rules-v0.md)**). **Silent** **fallback** **to** **another** **tool** **is** **out** **of** **scope** **for** **v0** **conformant** **documentation**.

---

## 5. Example mapping (illustrative)

| agent (role) | allowed_tools (examples) | Notes |
|--------------|---------------------------|--------|
| `coder` | `mars.tool.example.read_repo_file` | **read**-scoped; align **card** **`permissions`** with registry **`required_permissions`**. |
| `researcher` | `mars.tool.example.read_repo_file`, `mars.tool.example.http_get_metadata` | **Second** **tool** **adds** **`external-call`**; **agent** **`permissions`** **must** **include** **it**. |
| `memory_agent` | `mars.tool.example.memory_upsert` | **High** **risk**; **`approval_required`** **yes** **on** **registry** **row**; **Task** / **gate** **alignment** **required** **per** **[../security/approval-gates.md](../security/approval-gates.md)**. |

**Registry** **rows** **for** **these** **`tool_id`** **values** **are** **in** [registry.md](registry.md) **§4** **(planned** **examples** **only;** **not** **implemented** **tools**).

---

## 6. Relation to other artefacts

| Artefact | Relation |
|----------|----------|
| [registry.md](registry.md) | **Authoritative** **tool** **ids** **and** **`allowed_agents`**, **`required_permissions`**, **`risk_level`**. |
| [../agents/registry.md](../agents/registry.md) | **Agent** **identity** **and** **card** **shape**. |
| [../security/permissions-v0.md](../security/permissions-v0.md) | **Granted** **vs** **required** **permission** **scopes**. |
| [tool-permission-enforcement-v0.md](tool-permission-enforcement-v0.md) | **DENY** **+** **signal** **when** **binding** **or** **permission** **check** **fails**. |
| [tool-workflow-integration-v0.md](tool-workflow-integration-v0.md) | **Where** **`allowed_tools`** **is** **enforced** **relative** **to** **plan** / **execute** **steps**. |

---

## 7. Changelog (documentation)

| Date | Change |
|------|--------|
| 2026-04-27 | **Tool–Agent** **Binding** **v0** — **agent** **→** **`allowed_tools`**, **rules,** **example** **table,** **cross-refs** **(Stage** **9.5**). |

---

*End of MARS Tool–Agent Binding v0.*
