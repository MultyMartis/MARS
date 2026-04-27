# MARS — Permissions v0 (system contract)

**Status:** **documented contract only** — vocabulary and rules for **authorization design** and **passport fields**. **No** ACL runtime, IAM product integration, or enforced policy engine exists in this repository as proof (see [README.md](README.md)).

**Version:** v0.

---

## 1. Purpose

**Permissions v0** defines **scopes**, **entity types** to which scopes attach, and **declaration rules** so that the **Control Plane** can **fail closed** on routing (`../workflows/execution-flow.md`) and so **Agent Factory** / **Agent Builder** reviews have a **shared vocabulary**.

---

## 2. Permission scopes (v0)

Scopes are **orthogonal**; an entity may hold **several** with **explicit** listing only (no implicit “full access”).

| Scope | Meaning (contract) |
|-------|---------------------|
| **read** | Observe **in-bounds** resources: files, registry rows, logs, introspection outputs, read-only APIs **as declared** in passport/constraints. |
| **write** | Mutate **in-bounds** artifacts: files, registry (where policy allows), task state, documentation **as declared**. Excludes **external-call** unless also granted. |
| **execute** | Run **computation** that does **not** by itself imply external side effects: local transforms, in-process tools, **sandboxed** execution **as declared**. Tooling that hits the network or third-party systems needs **external-call** in addition where applicable. |
| **external-call** | Egress to **network**, **third-party APIs**, **webhooks**, or **non-repo** services. Highest scrutiny; ties to **NEED HUMAN APPROVAL** when side effects or PII apply ([approval-gates.md](approval-gates.md)). |

**Note:** Exact **granularity** (per-path, per-bucket, per-model) is **implementation**; v0 requires that **effective** permission for a step be **derivable** from declared passport + task **constraints**.

---

## 3. Entity-level permissions

Permissions are **declared per entity** in that entity’s **passport** (agent **card** field `permissions` per `../agents/agent-card-template.md`; analogous fields for other types when defined).

| Entity | Declaration locus |
|--------|-------------------|
| **agent** | Agent card **`permissions`** + **`tools`**; row in `../agents/registry.md`. |
| **workflow** | Workflow docs / future workflow registry — **SAFE UNKNOWN** for machine-enforceable workflow ACL until a workflow registry contract exists. |
| **tool** | Future **Tool Registry** (Stage 9 in `../governance/master-build-map.md`); until then, tool permissions are **only** as stated in docs and agent cards. |
| **integration** | Integration contract docs; live credentials and endpoints remain **SAFE UNKNOWN** unless explicitly documented in-repo per governance. |

---

## 4. Rules (normative v0)

### 4.1 No default superuser

- There is **no** v0 role that implies **unlimited** read/write/execute/external-call.
- **Omission** of a scope means **denied** for purposes of **contract interpretation** (fail closed at design time; future runtime should match).

### 4.2 Permissions must be declared in the entity passport

- Every **permission** an entity is expected to exercise **must** appear in its **passport** (or linked addendum **named** from the passport).
- **Broad** grants (“any API”, “all repos”) are **discouraged**; if documented for legacy analysis only, they **must** be labeled **high risk** and paired with **NEED HUMAN APPROVAL** in operational guidance.

### 4.3 Active agent requires explicit permissions

- An agent with **status: active** (registry/card semantics) **must** have a **non-empty**, **explicit** **`permissions`** section describing scopes (and limitations). “TBD” or blank effective permissions → **not activatable** under [guardrails-v0.md](guardrails-v0.md) §10.
- **Routing** must not select an agent for a step whose required capability is **not** covered by declared permissions + task **constraints**.

---

## 5. Relation to other documents

| Document | Relation |
|----------|----------|
| `../agents/agent-builder-contract.md` | Permission and tool reviews on create/update. |
| `../agents/agent-factory-v0.md` | Outcomes when permissions change. |
| `../workflows/task-contract-v0.md` | **constraints**, **risk_level**, **hitl_gates** interact with effective permission. |
| `../control-plane/contract.md` | Router/Dispatcher expectations (fail closed). |
| [approval-gates.md](approval-gates.md) | When **external-call** / **write** triggers **NEED HUMAN APPROVAL**. |

---

## 6. SAFE UNKNOWN

Machine-readable permission **enforcement**, delegation chains, and **temporary elevation** are **SAFE UNKNOWN** at repo level until specified in a runtime + tests. This file is the **v0 authorization vocabulary** for documentation and design reviews.
