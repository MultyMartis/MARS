# MARS — Tool Call Log v0

**Status:** **documented** — contract for **per-invocation** tool records. Not a database schema, log file format, or in-repo tool telemetry.

**Version:** v0. Revisable per [governance/versioning-model.md](../governance/versioning-model.md) and [governance/master-build-map.md](../governance/master-build-map.md).

**SAFE UNKNOWN:** Deduplication keys, binary payload storage, and encryption at rest for `input_ref` and `output_ref` are not specified in v0.

---

## 1. Purpose

The **tool call log** is the SoT (at the documentation level) for **which** tool ran **under** **which** run and agent, **what** inputs and outputs were **referenced** (not necessarily inlined), and **how** the call **ended** (status, **signals**, **side** **effects** flags, **approval** linkage). It is the **observability** counterpart to the **static** [../tools/tool-contract-v0.md](../tools/tool-contract-v0.md) and **safety** metadata in the registry, and it must align with **HITL** in [../security/approval-gates.md](../security/approval-gates.md).

No in-repo log writer or collection pipeline exists; this file defines field semantics only.

---

## 2. Tool call log fields (v0)

| Field | Meaning |
|-------|--------|
| **call_id** | Stable **unique** identifier for a single **invocation** of a **tool** within the operational system (format TBD). |
| **run_id** | Binds the call to a [run-history-v0.md](run-history-v0.md) run. |
| **tool_id** | Must match a row in [../tools/registry.md](../tools/registry.md) and align with [../tools/tool-contract-v0.md](../tools/tool-contract-v0.md). |
| **agent_id** | Invoking **agent** identity (registry-aligned; [../agents/registry.md](../agents/registry.md) and [../tools/tool-agent-binding-v0.md](../tools/tool-agent-binding-v0.md)). |
| **input_ref** | Opaque or typed **reference** to call **inputs** (e.g. artifact handle, id, bridge envelope) — not necessarily the raw **payload** in the log row. |
| **output_ref** | Opaque or typed **reference** to call **outputs**; aligns with [../storage/artifact-management-v0.md](../storage/artifact-management-v0.md) and bridge results. |
| **status** | **Outcome** of the **invocation** in terms **compatible** with the **Tool** **contract** and [../workflows/failure-model-v0.md](../workflows/failure-model-v0.md) (e.g. success, failure, denied, need approval). |
| **side_effects** | Declared or observed **side** **effect** class per [../tools/tool-safety-model-v0.md](../tools/tool-safety-model-v0.md) and registry; supports audit of destructive or memory-writing paths. |
| **approval_ref** | When the call is **gated,** a **link** to the **human** **decision** **artefact** or **id** (see [../security/approval-gates.md](../security/approval-gates.md)). Empty or — when not applicable. |
| **signals** | System **signal** **names** **(canonical** v0) **or** **counts** from [governance/system-signals-dictionary.md](../governance/system-signals-dictionary.md) emitted in relation to this call (e.g. PASS, FAIL, NEED HUMAN APPROVAL, SECURITY RISK). |

---

## 3. Relation to [../tools/tool-contract-v0.md](../tools/tool-contract-v0.md)

- The **envelope,** **validation,** and **return** **facets** of a **call** are **defined** in the **tool** **contract**; the **log** **row** is the **durable** **or** **projected** **“what** **was** **invoked** and **with** **what** **outcome**” for operators.
- **Mismatches** (logged `tool_id` **vs** actual **behaviour)** are **RISK** **class** (see [governance/risk-register.md](../governance/risk-register.md)) and **Self**-**Audit** [../interfaces/self-audit-v0.md](../interfaces/self-audit-v0.md) scope.

---

## 4. Relation to [../security/approval-gates.md](../security/approval-gates.md)

- **High**-**risk,** **destructive,** or **compliance**-**sensitive** **invocations** **require** **documented** **HITL** per **approval** **gates.**
- **`approval_ref`** is **mandatory** in **narrative** when **`approval_required`** (registry / safety model) **or** the **routed** path **imposes** **HITL**; **omission** of **an** **approval** **ref** for **such** **a** **call** **is** **a** **governance** **gap,** not **an** **implicit** **waiver**.

---

*End of Tool Call Log v0.*
