# MARS — Universal Entity Operations v0

**Status:** **documented** — **specification only**. No code, no runtime, no new dependencies. This file defines a **universal** model of **entity-level** operations to align **Self-Describe**, **Self-Check**, **Self-Audit**, **Self-Migrate**, **Capability Discovery**, and **Risk Review** across MARS **Core** and all **subsystems** before a full system audit.

**Version:** v0. Revisable per [versioning-model.md](versioning-model.md).

---

## 1. Purpose

- Provide a **single vocabulary** for “what an entity is” and “what we can do to it at documentation / governance level” before automated enforcement exists.
- Ensure **Self-Describe** (see [../interfaces/introspection-v0.md](../interfaces/introspection-v0.md), [../interfaces/self-describe-modes.md](../interfaces/self-describe-modes.md)) is applicable not only to **MARS Core** but to every **entity type** listed below, including where the **in-repo** source of truth is split across **governance**, **registries**, **workflows**, **Control Plane** contracts, **Agent Factory** / **Agent Registry**, and **integration** docs.
- Distinguish **documented architecture**, **planned implementation**, and **legacy imported** material per [../AGENTS.md](../AGENTS.md); never treat missing evidence as a green light.

MARS v0 already has named surfaces that this model draws together: **governance** (this folder), **registries** (e.g. agents, projects), **logs** (lifecycle), **Control Plane** and **Workflow** contracts, **Agent Registry** / **Agent Factory**, and **Introspection** / **Self-Describe** v0. Universal **entity** operations are the **checklist and vocabulary** so the same self-governance **operations** in §4 can apply to any entity type in §2. Specification only: no **shipped** **enforcement** in-repo.

---

## 2. Supported entity types (normative)

| Type | Meaning (v0) |
|------|--------------|
| **system** | MARS as a whole: scope, phase, boundaries, honesty statements. |
| **subsystem** | A named in-architecture area (e.g. Control Plane surface, workflow layer, interface layer) with a defined boundary. |
| **agent** | A role/definition in the agent catalog: identity, permissions, tool scope (per [../agents/registry.md](../agents/registry.md) and [../agents/agent-card-template.md](../agents/agent-card-template.md)). |
| **workflow** | A documented process or contract: stages, tasks, signals (e.g. [../workflows/](../workflows/)). |
| **tool** | A callable tool or integration endpoint as described in contracts / capability map (not “implemented” unless the repo shows it). |
| **project** | A work package / track with identity in the project registry ([../registry/project-registry.md](../registry/project-registry.md)). |
| **integration** | A connection to an external system or service (documented contract, credentials policy, data flow) — in-repo or **SAFE UNKNOWN** for live behavior. |
| **storage** | A durable store or data plane concept (databases, buckets, vector stores) as **documented** in architecture / storage docs; live topology is **SAFE UNKNOWN** unless listed in-repo. |
| **model** | An LLM or model endpoint identity (name, version policy, routing) as **documented**; provider-specific runtime state is **SAFE UNKNOWN** unless proved in-repo. |

**Note:** A given thing may map to **multiple** types (e.g. a “workflow” entry that is also a “subsystem” concern). Operations **SHOULD** declare **primary** entity type and **secondary** tags in audit/check scope.

---

## 3. Common facets (every entity)

For **v0 documentation governance**, every entity of the types in §2 is expected to be **describable** in terms of the following facets. Where a facet is **not** present in the repo, the correct output is **SAFE UNKNOWN** (not invention).

| Facet | Description |
|-------|-------------|
| **Passport** | Stable **identity** and **human- and machine-readable** record: `entity_id` (or equivalent), type, name, **owner** / **steward**, scope, and pointers to the **source-of-truth** files. *In-repo today*, **agent** passports align with **agent cards**; other types use the closest **registry row** + linked doc, or a **governance-defined** identity block. |
| **Registry entry** | A **row or record** in a named **registry** (system catalog, agent registry, project registry, tool list, etc.) that makes the entity **discoverable** and **versioned** in documentation space. |
| **Lifecycle events** | **Documented** transitions (and optional **log** row in [../logs/lifecycle-log.md](../logs/lifecycle-log.md) when the process is tracked there). **Operational** histories not in-repo → **SAFE UNKNOWN**. |
| **Status** | A **governance-allowed** value (e.g. planned, documented, active, deprecated) consistent with [state-model.md](state-model.md) / relevant registry where applicable. |
| **Version** | **Entity** version or **compatibility** tag per [versioning-model.md](versioning-model.md) (and subsystem-specific addenda if any). |
| **Risks** | **Known** security, data, or operational **risks** as **stated in docs** — or **empty** with **SAFE UNKNOWN** for unassessed areas. |
| **Validation rules** | **Normative** checks that the entity is **well-formed** (fields present, cross-links valid, no false implementation claims, terminology alignment). [Self-Check v0](../interfaces/self-check-v0.md) instantiates a **light** ruleset. |

**Truth boundary:** A **passport** or **registry** field **MUST NOT** assert **implementation** of runtime, RAG, or live integrations unless the repository or an attached evidence trail supports it (see [../AGENTS.md](../AGENTS.md)).

---

## 4. Universal operations (normative)

These are **logical operations** at **entity** granularity. They may be **manual** (review), **assisted** (checklists in docs), or **future automated**; **v0** specifies **what** they mean, not that code exists.

| Operation | Definition |
|-----------|------------|
| **SELF DESCRIBE** | **Materialize a truthful** description of the entity by **reading** only **bound** sources of truth (same spirit as the **Self-Describe Engine** in [../interfaces/introspection-v0.md](../interfaces/introspection-v0.md)). Modes in [../interfaces/self-describe-modes.md](../interfaces/self-describe-modes.md) apply; **ENTITY** / **PROJECT** resolve against registries. **Applies to all types in §2.** |
| **SELF CHECK** | **Quick** consistency check: passport, registry, status, ownership layer, **related docs**, **no false** implementation claim. Output and rules: [../interfaces/self-check-v0.md](../interfaces/self-check-v0.md). |
| **SELF AUDIT** | **Deeper** pass over entity **and dependencies**: terminology, registry, lifecycle, versioning, **security/permissions**, missing SoT links. Output: [../interfaces/self-audit-v0.md](../interfaces/self-audit-v0.md). |
| **SELF MIGRATE** | **Planned** operation: align entity metadata, registry rows, and **lifecycle** records with a **target** phase, schema, or version **per** [versioning-model.md](versioning-model.md) and migration / roadmap docs. Produces a **change plan** and **staged** log entries when executed (implementation **out of scope** for v0 spec). |
| **CAPABILITY DISCOVERY** | **Enumerate** what the entity is **allowed** or **designed** to do, mapped to the **capability map** ([capability-map.md](capability-map.md)) and **Control Plane** / **workflow** contracts. **Distinguish** *documented capability* vs *shipped code*. |
| **RISK REVIEW** | Structured review of **Risks** facet + dependency risks; can feed [../governance/](../governance/) updates, **RISK** **signals** in [../workflows/](../workflows/) vocabulary, and audit **findings**. |

**Ordering (recommended):** **SELF CHECK** (fast gate) → **SELF DESCRIBE** (communication) or **CAPABILITY DISCOVERY** (scope) → **RISK REVIEW** / **SELF AUDIT** (deeper) → **SELF MIGRATE** (when **change** is **required** and **evidence** exists).

---

## 5. Relation to existing v0 art

| Artifact | Role relative to this spec |
|----------|----------------------------|
| [../control-plane/contract.md](../control-plane/contract.md) | **Subsystem**-level and **entity**-level **policies** may **reference** these operations as **intended** **interface** to governance truth. |
| [../workflows/](../workflows/) | **Workflow** **entities** use the same **facets**; **signals** in outputs align with **workflow** **signal** vocabulary. |
| [../agents/](../agents/) | **Agent** **registry** and **Factory** v0 are **default** SoT for **agent**-typed entities. |
| [../observability/README.md](../observability/README.md) | **Lifecycle** **events** may mirror **operational** concerns; **v0** doc layer **MUST** not conflate **documented** **log** rows with **live** telemetry. |

---

## 6. SAFE UNKNOWN

If **any** of passport, registry, lifecycle, version, or **risk** assessment is **not** provable from **in-repo** (or **explicit** external SoT **linked** in docs), operations **MUST** emit **SAFE UNKNOWN** for that slice — **not** a **PASS** and **not** a **fabricated** detail.

---

*Last updated: Universal Entity Operations v0 (documentation-only; no implementation claim).*
