# MARS — Tool Permission Enforcement v0

**Status:** **documented** — **contract only**. **Maps** [../security/permissions-v0.md](../security/permissions-v0.md) **to** the **Tool** **Layer** (registry + agent passport) and **normatively** **states** **outcomes** when the **invocation** **actor** (agent) does **not** **satisfy** a **tool**'s `required_permissions`. **No** **ACL** **engine** in-repo; **enforcement** is **design**-**time** and **documented** **expected** **runtime** **shape** for **future** **work**.

**Version:** v0. Revisable per [../governance/versioning-model.md](../governance/versioning-model.md) and [../governance/master-build-map.md](../governance/master-build-map.md).

---

## 1. Purpose

- **Pin** the **vocabulary** **in** [permissions-v0.md](../security/permissions-v0.md) (scopes and declaration rules) **to** **concrete** **artefacts**: **tool** **→** **`required_permissions`**, **agent** **→** **`granted_permissions`** (agent **card** `permissions` / **passport** and **registry** **row** — see **§3**).
- **Define** **a** **single** **outcome** **on** **mismatch**: **DENY** **+** **signal** (see **§4**), **aligned** **with** [../governance/system-signals-dictionary.md](../governance/system-signals-dictionary.md) and [tool-contract-v0.md](tool-contract-v0.md).

---

## 2. How permissions v0 applies to tools

- **[permissions-v0.md](../security/permissions-v0.md) §2** lists scopes (`read`, `write`, `execute`, `external-call` — orthogonal, explicit, no default superuser).
- **Each** **tool** **row** **in** [registry.md](registry.md) **binds** **a** **tool** **to** the **set** **of** **scope** **tokens** **it** **requires** **to** **be** **used** **lawfully** (field **`required_permissions`**) **or** **explicit** `none` / **empty** **where** **permitted** **by** **that** **contract**.
- The **invocation** **actor** (typically an **active** **agent** **routed** **to** the **step**) is **described** **in** [../agents/agent-card-template.md](../agents/agent-card-template.md) and [../agents/registry.md](../agents/registry.md) with **`granted_permissions`** **interpreted** as the **card**'s `permissions` **section,** **normalized** **to** the **same** **v0** **scope** **names** as [permissions-v0.md](../security/permissions-v0.md) §2.

---

## 3. Mapping: tool and agent

| Side | Source (v0) | Field / locus | Meaning |
|------|-------------|--------------|---------|
| **Tool** | [registry.md](registry.md) | **`required_permissions`** | **List** **of** **v0** **scopes** (or **`none`**) **that** **must** **be** **covered** **to** **authorize** the **call** (design + future enforcement). |
| **Agent** | Agent **card** / [../agents/registry.md](../agents/registry.md) | **`permissions`** (= **granted_permissions** in this **doc**'s **table** **language**) | **Declares** **which** **scopes** this **agent** is **allowed** **to** **exercise** when **routed;** **must** **be** **explicit** **per** [permissions-v0.md](../security/permissions-v0.md) **§4.3** for **active** **agents**. |
| **Task** | [../workflows/task-contract-v0.md](../workflows/task-contract-v0.md) | **`scope_in`**, **`constraints`**, **`risk_level`** | **Narrow** or **raise** the **effective** **envelope;** **does** **not** **replace** **granted** / **required** **permissions** **comparison** — **takes** **both** **into** **account** **per** **governing** **docs** (fail **closed** on **conflict**). |

**`granted_permissions`** is the **agent**'s **declared** set; it is **not** **dynamically** **expanded** in **v0** **documentation** without **a** **recorded** **elevation** (which **remains** **SAFE** **UNKNOWN** for **machine** **behaviour** per [permissions-v0.md](../security/permissions-v0.md) **§6**).

---

## 4. Rule: mismatch = DENY + signal

- If, at the time of a **tool** **invocation** **decision**, **any** **scope** in the **tool**'s `required_permissions` is **not** **included** in the **agent**'s `granted_permissions` (intersected with **Task** **constraints** per **policy**), the **control** **path** **must** **DENY** (do **not** **proceed** **to** **commit** **side** **effects** on **behalf** of **this** **invocation**).
- **Denial** **must** **emit** **a** **canonical** **outcome** on the **documented** **envelope:** at **minimum** a **signal** on the **line** of **`SECURITY RISK`**, **`UNKNOWN`**, or **a** **dictionary**-**named** **equivalent** as **required** for **policy** (see [../governance/system-signals-dictionary.md](../governance/system-signals-dictionary.md) and [tool-contract-v0.md](tool-contract-v0.md) **output** **envelope**), and **must** **not** **silently** **substitute** **a** **weaker** **tool** or **drop** the **check** (per [tool-contract-v0.md](tool-contract-v0.md) **Rules**).
- Human-in-the-loop (NEED HUMAN APPROVAL) is **not** **a** **substitute** for **a** **missing** **base** **permission** in **v0** **contract** **interpretation:** **approval** **gates** (see [../security/approval-gates.md](../security/approval-gates.md)) **govern** **separate** **conditions**; MARS v0 **expects** **permission** **mismatch** to **DENY,** not “ask to elevate in place” without a **future,** **explicit** **elevation** **artefact** (SAFE **UNKNOWN**).

---

## 5. Relation to other artefacts

| Artefact | Relation |
|----------|----------|
| [../security/permissions-v0.md](../security/permissions-v0.md) | **Authoritative** **v0** **scope** **vocabulary** and **declaration** **rules**. |
| [../security/guardrails-v0.md](../security/guardrails-v0.md) | **Agent** **activatability** and **policy** **narrative** **aligned** with **grants** (documentation). |
| [registry.md](registry.md) | **Tool** **→** **`required_permissions`**. |
| [tool-agent-binding-v0.md](tool-agent-binding-v0.md) | **Agent** **→** **`allowed_tools`**; **pair** with **this** **file** for **full** **eligibility** (tool + permissions). |
| [tool-validation-rules-v0.md](tool-validation-rules-v0.md) | **Pre**-**call** **bundle** including **permission** **check;** **FAIL** when **deny** **condition** **holds** (see **that** **file** for **output** **labels**). |
| [../governance/dependency-map.md](../governance/dependency-map.md) | **Entity** **`tool_permission_enforcement`** **edges** (documentation-only **map**). |

---

## 6. Changelog (documentation)

| Date | Change |
|------|--------|
| 2026-04-27 | **Tool** **Permission** **Enforcement** v0 — mappings, DENY+signal, **cross-refs** (Stage **9.5**). |

---

*End of MARS Tool Permission Enforcement v0.*
