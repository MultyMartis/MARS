# MARS — Tool Safety Model v0

**Status:** **documented** — **contract only**. Defines **risk** **levels**, **mapping** **to** **human** **approval** **and** **security** **signals**, **and** **side-effect** **classification** **for** **tools**. **No** policy engine or sandbox implementation in-repo for Phase 1.

**Version:** v0. Revisable per [../governance/versioning-model.md](../governance/versioning-model.md) and [../governance/master-build-map.md](../governance/master-build-map.md).

---

## 1. Purpose

- Align **tool** **risk** **with** [../security/approval-gates.md](../security/approval-gates.md), [../governance/system-signals-dictionary.md](../governance/system-signals-dictionary.md) (**`NEED HUMAN APPROVAL`**, **`SECURITY RISK`**), **and** [../security/threat-model-v0.md](../security/threat-model-v0.md) **(tool** **abuse,** **external** **integration**).
- Require **explicit** **declaration** **of** **external** **calls** **and** **side** **effects** **in** [registry.md](registry.md) **—** **no** **hidden** **effects** **in** **contract** **interpretation**.

---

## 2. Tool risk levels (v0)

| Level | Meaning | Typical examples |
|-------|---------|------------------|
| **low** | **Read-only** **or** **non-mutating** **within** **declared** **trust** **boundary**; **no** **external** **egress** **by** **default**. | **Internal** **file** **read**, **schema** **validation** **without** **I/O**. |
| **medium** | **Bounded** **mutations** **or** **external** **calls** **with** **limited** **blast** **radius** **when** **gates** **and** **permissions** **hold**. | **HTTP** **GET** **to** **allowlisted** **host**, **script** **run** **in** **sandbox** **(design)**. |
| **high** | **Irreversible,** **wide** **blast** **radius,** **sensitive** **data** **paths,** **or** **privileged** **external** **effects**. | **Deploy,** **payment,** **bulk** **delete,** **durable** **PII** **write**, **privileged** **admin** **API**. |

---

## 3. Mapping to NEED HUMAN APPROVAL and SECURITY RISK

| Condition | Expected signal / gate behaviour (v0 documentation) |
|-----------|-----------------------------------------------------|
| **high** **risk_level** **tool** | **`approval_required`** **`yes`** **in** [registry.md](registry.md); **before** **first** **side-effecting** **use**, **`NEED HUMAN APPROVAL`** **per** [../security/approval-gates.md](../security/approval-gates.md) **and** [../governance/system-signals-dictionary.md](../governance/system-signals-dictionary.md). |
| **medium** **risk** **with** **external** **or** **write** **side** **effects** | **`NEED HUMAN APPROVAL`** **when** **approval** **gates** **§2** **apply** **(e.g.** **external** **API,** **storage** **writes**); **composite** **rule** **in** **approval-gates** **wins** **if** **stricter**. |
| **Policy** **violation,** **scope** **escape,** **suspected** **injection** **driving** **tool** **use** | **`SECURITY RISK`** **per** **dictionary**; **unattended** **retry** **/** **fallback** **that** **amplifies** **harm** **is** **forbidden** **per** [../workflows/failure-model-v0.md](../workflows/failure-model-v0.md) **§4**. |
| **Missing** **binding** **(unknown** **tool,** **missing** **permission** **declaration)** | **`UNKNOWN`** **(not** **`SAFE UNKNOWN`**) **when** **hard** **block** **—** **dictionary** **§2**. |

**Composite** **with** **task** **risk_level** — [../workflows/task-contract-v0.md](../workflows/task-contract-v0.md) **`risk_level`** **high** **is** **a** **strong** **signal** **for** **approval** **even** **when** **tool** **row** **is** **medium**; **exact** **product** **precedence** **`SAFE UNKNOWN`** **unless** **documented** **elsewhere**.

---

## 4. Side effects classification (v0)

Every **tool** **row** **must** **tag** **side** **effects** **using** **one** **primary** **class** **(plus** **notes** **as** **needed**):

| Class | Definition | Registry `side_effects` |
|-------|------------|-------------------------|
| **read-only** | **No** **durable** **mutation** **of** **MARS** **memory,** **runtime** **authoritative** **state,** **or** **external** **systems** **beyond** **ephemeral** **caches** **explicitly** **scoped** **as** **non-authoritative**. | **`no`** **+** **description** **optional** **(may** **state** **“read-only”)**. |
| **write** | **Mutates** **durable** **project** **or** **system** **state** **inside** **the** **trust** **boundary** **(files,** **internal** **DB,** **workflow** **state)** **without** **necessarily** **calling** **third** **parties**. | **`yes`** **+** **description** **mandatory**. |
| **external** | **Network** **or** **third-party** **integration** **(API,** **webhook,** **MCP** **server** **call** **—** **implementation** **`SAFE UNKNOWN`)**. | **`yes`** **+** **description** **must** **name** **egress** **class**; **`external-call`** **permission** **expected**. |
| **destructive** | **Deletes,** **irreversible** **crypto** **or** **billing** **actions,** **or** **mass** **unscoped** **writes** **that** **cannot** **be** **trivially** **rolled** **back.** | **`yes`** **+** **description** **mandatory**; **`risk_level`** **typically** **`high`**; **`approval_required`** **`yes`**. |

**Rules (normative v0):**

1. **High-risk** **tools** **require** **approval** **—** **§3** **and** [registry.md](registry.md) **`approval_required`**.  
2. **External** **calls** **must** **be** **declared** **—** **type** **`integration`** **or** **`api`** **with** **external** **side** **effect** **class** **and** **`external-call`** **in** **`required_permissions`** **when** **egress** **applies**.  
3. **No** **hidden** **side** **effects** **—** **if** **the** **tool** **does** **more** **than** **the** **row** **states,** **the** **row** **is** **non-conformant**; **consumers** **should** **treat** **as** **`SECURITY RISK`** **/** **`UNKNOWN`** **until** **corrected** **(design-time** **discipline).**

---

## 5. Relation to Memory Write Policy

**Tools** **that** **emit** **durable** **memory** **(semantic** **/** **episodic** **/** **project** **knowledge)** **must** **satisfy** [../memory/memory-write-policy-v0.md](../memory/memory-write-policy-v0.md) **and** **use** **side** **effect** **class** **`write`** **(or** **`destructive`** **for** **tombstone** **/** **purge** **paths)** **with** **explicit** **metadata** **obligations** **in** **the** **memory** **path** **documentation**.

---

## 6. Changelog (documentation)

| Date | Change |
|------|--------|
| 2026-04-27 | **Tool** **Safety** **Model** **v0** — **risk** **levels,** **signal** **mapping,** **side** **effect** **classes,** **rules,** **memory** **cross**-**ref**. |

---

*End of MARS Tool Safety Model v0.*
