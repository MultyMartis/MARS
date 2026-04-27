# MARS — Tool Validation Rules v0

**Status:** **documented** — **contract only**. Enumerates what **must** be **checked** before a **tool** **call** is **admitted** (or **reaches** **commit** of **side** **effects**) in **conformant** MARS **documentation** and **expected** **future** **control** **plane** **behaviour**. **No** **schema** **validator** or **policy** **engine** in **this** **repository** (Phase **1**).

**Version:** v0. Revisable per [../governance/versioning-model.md](../governance/versioning-model.md) and [../governance/master-build-map.md](../governance/master-build-map.md).

---

## 1. Purpose

- **Standardize** the **pre**-**invocation** checks (inputs, **authorisation,** **risk** **envelope**) across [registry.md](registry.md), [tool-contract-v0.md](tool-contract-v0.md), [tool-agent-binding-v0.md](tool-agent-binding-v0.md), and [tool-permission-enforcement-v0.md](tool-permission-enforcement-v0.md).
- **Define** a **small** **vocabulary** of **validation** **outcomes:** **PASS,** **FAIL,** **NEED** **HUMAN** **APPROVAL** — so **planners,** **bridge** **narrative,** and **signals** (see [../governance/system-signals-dictionary.md](../governance/system-signals-dictionary.md) **§2**) **stay** **aligned**.

---

## 2. What must be validated before a tool call (v0)

### 2.1 Input schema

- **When** the **tool** **row** or **contract** cites **`input_schema_ref`**, the **proposed** **`parameters`** **must** **conform** (documentation-**time** **review;** **future** **runtime** — **schema** **validate** **where** **schema** **exists**).
- If **`input_schema_ref`** is **`TBD`**, or **schema** is **unavailable,** the **check** **cannot** be **strong**-**pass** on **structure** — **document** as **partial** or **emit** **`UNKNOWN`**, **`SAFE UNKNOWN`**, or **structured** **honesty** on the **envelope** per [tool-contract-v0.md](tool-contract-v0.md) (do **not** **treat** as **silent** **PASS** on **unknown** **shape**).

### 2.2 Permissions

- The **tool**'s `required_permissions`, the **agent**'s **granted** **scopes,** and **applicable** **Task** **constraints** are **evaluated** per [tool-permission-enforcement-v0.md](tool-permission-enforcement-v0.md).
- On **mismatch,** **validation** **fails** (**FAIL** — see **§3**), with **DENY+signal,** not **soft** **warning** (unless a **governance**-**approved** **degraded** **read**-**only** **path** **exists,** which is **not** **normative** in **v0**).

### 2.3 Risk level

- The **registry** **`risk_level`** (and **related** **columns:** `side_effects`, `approval_required`) **must** be **consistent** with [tool-safety-model-v0.md](tool-safety-model-v0.md) and with the **Task** / **run** **risk** **envelope** (see [../security/approval-gates.md](../security/approval-gates.md) + [../workflows/task-contract-v0.md](../workflows/task-contract-v0.md); **exact** **composition** of “incompatible” is **governed** by **those** **contracts,** not **redefined** **here**).
- If the **proposed** **call** **requires** **HITL** before **side** **effects,** **validation** does **not** **return** **PASS** as “ready to mutate” — it **returns** **NEED** **HUMAN** **APPROVAL** (see **§3**), until the **gate** is **resolved** (pause / resume / abort per [../mars-runtime/execution-bridge-v0.md](../mars-runtime/execution-bridge-v0.md) **§7**).

---

## 3. Outcomes: PASS, FAIL, NEED HUMAN APPROVAL

| Outcome | When it applies (v0) | Expected continuation (documentation) |
|---------|------------------------|--------------------------------------|
| **PASS** | **Input** (schema or **acceptable** **honest** **partial** per **§2.1**), **permissions,** and **risk** / **gate** **posture** all **satisfied** for **admitting** the **side**-**effecting** or **non**-**gated** **call** as **designed**. | **Proceed** to **bridge**-**level** **dispatch** (Execution **Bridge**); **emit** **required** **signals** on **completion** per [tool-contract-v0.md](tool-contract-v0.md) (none of **this** is **runnable** in **Phase** **1** **repo**). |
| **FAIL** | **Schema** **rejection,** **permission** **mismatch,** **undeclared** **tool** for **agent,** **invalid** **tool** **id,** or **incompatible** **policy** that is **not** an **approval** **class** (see [tool-agent-binding-v0.md](tool-agent-binding-v0.md), [tool-permission-enforcement-v0.md](tool-permission-enforcement-v0.md)). | **Do** **not** **invoke;** **DENY+signal** (e.g. **SECURITY** **RISK,** **UNKNOWN,** **STRUCTURE** **CHANGE** if **replan** **needed**); per [../workflows/failure-model-v0.md](../workflows/failure-model-v0.md) (no **substitute** for **missing** **permissions**). |
| **NEED HUMAN APPROVAL** | **Registry** / **approval**-**gates** **rules** **require** **HITL** before **proceeding** (e.g. **`approval_required`**, **high** **risk,** **external** **PII,** per [../security/approval-gates.md](../security/approval-gates.md); **not** a **FAIL** of **base** **eligibility,** but a **pause** **state**). | **Do** **not** **commit** **side** **effects** until **cleared;** **bridge** / **workflow** **pause** + **resume** **narrative** per [../mars-runtime/execution-bridge-v0.md](../mars-runtime/execution-bridge-v0.md) and [tool-workflow-integration-v0.md](tool-workflow-integration-v0.md) (documentation). **Emit** **canonical** **NEED** **HUMAN** **APPROVAL** where **dictionary** **applies** (see [../governance/system-signals-dictionary.md](../governance/system-signals-dictionary.md)). |

**NEED** **HUMAN** **APPROVAL** is a **distinct** **outcome** from **FAIL:** the **second** **permits** a **controlled** **pause** / **approval** **path;** the **first** **stops** or **escalates** the **invalid** **attempt** (unless **re**-**routed** as **STRUCTURE** **CHANGE**).

---

## 4. Where validation runs in the path

- **Logically,** **validation** (this **document**'s **bundle**) **runs** **after** **route** (agent and **tool** **candidates** **known**) and **before** / **at** the **point** the **Execution** **Bridge** **accepts** a **commit**-**relevant** **invocation,** per [tool-workflow-integration-v0.md](tool-workflow-integration-v0.md) (explicit **step,** **bridge** **transit,** **checkpoint** **aware**). **Re**-**validation** **may** **occur** on **resume** if **policy** or **state** **changed**.

---

## 5. Relation to other artefacts

| Artefact | Relation |
|----------|----------|
| [../governance/system-signals-dictionary.md](../governance/system-signals-dictionary.md) | **Names** for **emitted** **signals** (**FAIL,** **approval,** **honesty**). |
| [tool-workflow-integration-v0.md](tool-workflow-integration-v0.md) | **Placement** in **execute** + **bridge** (§4 of **that** **file** **pairing**). |
| [../security/approval-gates.md](../security/approval-gates.md) | **When** **HITL** **→** **NEED** **HUMAN** **APPROVAL** (not **FAIL** on **clean** **base** **checks**). |

---

## 6. Changelog (documentation)

| Date | Change |
|------|--------|
| 2026-04-27 | **Tool** **Validation** **Rules** v0 — **input** / **permissions** / **risk** **checks,** **PASS** / **FAIL** / **NEED** **HUMAN** **APPROVAL,** **placement** (Stage **9.5**). |

---

*End of MARS Tool Validation Rules v0.*
