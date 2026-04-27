# MARS — Tool Contract v0

**Status:** **documented** — **contract only**. Defines the **standard** **documentation** **envelope** for a **single** **tool** **invocation**: inputs, outputs, **signals**, and **obligations** relative to **failure**, **permissions**, and **approval** **gates**. **No** SDK, **no** wire format implementation in this repository for Phase 1.

**Version:** v0. Revisable per [../governance/versioning-model.md](../governance/versioning-model.md) and [../governance/master-build-map.md](../governance/master-build-map.md).

---

## 1. Purpose

- Align **tool** **calls** with the **Execution** **Bridge** **output** **facets** (**result**, **status**, **artifacts**, **signals**) per [../mars-runtime/execution-bridge-v0.md](../mars-runtime/execution-bridge-v0.md) **§4**.
- Bind **tool**-level **success** / **failure** / **partial** **classification** to [../workflows/failure-model-v0.md](../workflows/failure-model-v0.md) **without** **contradiction**.
- Ensure **canonical** **system** **signals** per [../governance/system-signals-dictionary.md](../governance/system-signals-dictionary.md) **§2** — **no** informal synonyms in normative tables.

---

## 2. Input envelope (normative v0)

| Field | Required | Description |
|-------|----------|-------------|
| **tool_id** | **yes** | Identifier from [registry.md](registry.md); **UNKNOWN** if missing or unregistered. |
| **parameters** | **yes** | **Logical** payload; **must** conform to **input_schema_ref** for the **tool** when **schema** **exists**. **SAFE UNKNOWN** if schema **TBD** — callers **must** **label** **unvalidated** **slices** **honestly**. |
| **context** | **no** | Optional **correlation** and **policy** **handles**: e.g. **`task_id`**, **`project_id`**, **executor** **hints**, **attachment** **pointers** — aligned with [../mars-runtime/execution-bridge-v0.md](../mars-runtime/execution-bridge-v0.md) **§3.3** **Context**. |
| **run_id** | **yes** | **Correlation** **id** for the **workflow** **run**; **must** align with [../storage/runtime-state-store-v0.md](../storage/runtime-state-store-v0.md) **and** **bridge** **expectations**. |

**Permissions** — Before **accepting** a call for **execution**, the **documented** **control** **path** **must** verify the **invoking** **actor** holds **required_permissions** from the **registry** row ([registry.md](registry.md)). **Violation** → **SECURITY RISK**; **do** **not** **silent** **fallback**.

**Approval gates** — If **approval_required** is **`yes`** for the **tool** (or **composite** **rule** from [../security/approval-gates.md](../security/approval-gates.md)), **execution** **must** **not** **proceed** **until** **NEED HUMAN APPROVAL** **is** **resolved** (**pause** / **resume** / **abort** per [../mars-runtime/execution-bridge-v0.md](../mars-runtime/execution-bridge-v0.md) **§7**). **Bypass** is **forbidden** in **contract** **interpretation**.

---

## 3. Output envelope (normative v0)

| Field | Required | Description |
|-------|----------|-------------|
| **result** | **no** (may be empty) | Primary **payload**; **structured** or **opaque** per **output_schema_ref** when defined. |
| **artifacts** | **no** | **Named** **outputs** (paths, URIs) **linked** to **`task_id`** / **`run_id`** where **persistence** **applies** — same **spirit** as **bridge** **§4** **artifacts**. |
| **status** | **yes** | One of: **`success`**, **`failure`**, **`partial`** — **must** **map** **honestly** to **failure** **types** in [../workflows/failure-model-v0.md](../workflows/failure-model-v0.md) **(e.g.** **partial** ↔ **partial completion**). |
| **signals** | **yes** (list, may be empty) | Zero or more **canonical** **names** from [../governance/system-signals-dictionary.md](../governance/system-signals-dictionary.md) **§2** **titles** (e.g. **`UNKNOWN`**, **`SAFE UNKNOWN`**, **`NEED HUMAN APPROVAL`**, **`SECURITY RISK`**, **`STRUCTURE CHANGE`**). **MUST** **emit** **at** **least** **one** **signal** **when** **policy** **or** **honesty** **requires** **it**; **silent** **omission** **of** **required** **signals** **is** **out** **of** **scope** **for** **conformant** **documentation**. |

---

## 4. Normative rules (v0)

1. **MUST follow failure-model-v0** — **Retries**, **abort**, **escalate**, **fallback**, **idempotency**, and **SECURITY RISK** **→** **escalate** **apply** **per** [../workflows/failure-model-v0.md](../workflows/failure-model-v0.md); **tool** **invocation** **is** **a** **step** **subject** **to** **that** **model**.
2. **MUST emit signals** — **Outcomes** **that** **trigger** **dictionary** **definitions** **must** **carry** **the** **matching** **signal** **(s)** **on** **the** **tool** **output** **envelope** **and** **must** **propagate** **through** **the** **Execution** **Bridge** **(see** [../mars-runtime/execution-bridge-v0.md](../mars-runtime/execution-bridge-v0.md) **§6)**.
3. **MUST respect permissions** — **Missing** **or** **insufficient** **permissions** → **`UNKNOWN`** **or** **`SECURITY RISK`** **per** **dictionary**; **not** **ad-hoc** **strings**.
4. **MUST NOT bypass approval gates** — **Side-effecting** **or** **gated** **tools** **require** **documented** **HITL** **resolution** **before** **effects** **commit** **when** [../security/approval-gates.md](../security/approval-gates.md) **or** **registry** **`approval_required`** **says** **so**.

---

## 5. Memory writes (boundary)

A **tool** **that** **persists** **to** **MARS** **memory** **(not** **runtime** **state** **alone)** **must** **also** **satisfy** [../memory/memory-write-policy-v0.md](../memory/memory-write-policy-v0.md) **§2–§4**; **registry** **side_effects** **must** **disclose** **intent** **to** **write** **durable** **knowledge**.

---

## 6. Relation to other artefacts

| Artefact | Relation |
|----------|----------|
| [registry.md](registry.md) | **tool_id** **and** **policy** **columns** **are** **authoritative** **for** **static** **tool** **metadata**. |
| [tool-execution-model-v0.md](tool-execution-model-v0.md) | **How** **invocation** **rides** **the** **Execution** **Bridge** **and** **stores** **state**. |
| [tool-safety-model-v0.md](tool-safety-model-v0.md) | **risk_level** **and** **side_effects** **classification**. |
| [../security/threat-model-v0.md](../security/threat-model-v0.md) | **Tool** **abuse** **and** **external** **integration** **categories**. |

---

## 7. Changelog (documentation)

| Date | Change |
|------|--------|
| 2026-04-27 | **Tool** **Contract** **v0** — input/output **envelope**, **rules**, **memory** **boundary**, **cross**-**refs**. |

---

*End of MARS Tool Contract v0.*
