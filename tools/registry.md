# MARS — Tool Registry v0

**Status:** **documented** — **contract only**. This file defines the **logical** fields for **tool** rows in the MARS **Tool Layer** and **example** **planned** entries. It does **not** implement a registry service, database, or MCP server. Per [../AGENTS.md](../AGENTS.md), **no** runnable tool host is claimed unless code exists elsewhere in-repo.

**Version:** v0. Revisable per [../governance/versioning-model.md](../governance/versioning-model.md) and [../governance/master-build-map.md](../governance/master-build-map.md).

**SAFE UNKNOWN:** Machine schema (JSON Schema URIs, OpenAPI refs), exact permission strings per deployment, and wire format for registry sync remain **TBD** until a later artefact or implementation.

---

## 1. Purpose

- Give a **single** **vocabulary** for **tool identity**, **classification**, **risk**, **permissions**, and **schema** references so **agents**, **control plane**, **Execution Bridge**, and **security** docs stay aligned.
- Support **Stage 9** **documentation** only; **normative** pairing with [tool-contract-v0.md](tool-contract-v0.md), [tool-execution-model-v0.md](tool-execution-model-v0.md), [tool-safety-model-v0.md](tool-safety-model-v0.md), [../security/approval-gates.md](../security/approval-gates.md), and [../governance/system-signals-dictionary.md](../governance/system-signals-dictionary.md).

---

## 2. Row schema (v0 logical fields)

Each **tool** row **must** be describable with the following fields (human tables today; future machine export **should** preserve the same semantics).

| Field | Description |
|-------|-------------|
| **tool_id** | Stable string identifier (e.g. `mars.tool.example.read_repo_file`); **unique** within the registry namespace for the project or **global** MARS catalog when adopted. |
| **name** | Human-readable short name. |
| **type** | One of: **`api`** (HTTP/RPC service), **`script`** (invoked script / CLI), **`internal`** (in-process or same-trust-boundary helper), **`integration`** (third-party connector, MCP-style surface, external SaaS). |
| **status** | One of: **`planned`** (design only), **`draft`** (contract under review), **`active`** (approved for use under stated conditions), **`deprecated`** (no new use; migration path documented). |
| **allowed_agents** | Which **agent** **roles** or **registry** **ids** may invoke this tool (list, pattern, or `—` if **policy** defers to [../agents/registry.md](../agents/registry.md) + permissions only). **SAFE UNKNOWN** until rows are bound. |
| **required_permissions** | References to [../security/permissions-v0.md](../security/permissions-v0.md) capability tokens (e.g. `read`, `execute`, `write`, `external-call`) — **list** or **explicit** **`none`** for read-only internal tools. |
| **risk_level** | **`low`** / **`medium`** / **`high`** per [tool-safety-model-v0.md](tool-safety-model-v0.md); **must** align with **approval_required** and [../security/threat-model-v0.md](../security/threat-model-v0.md) **category** **3** (tool abuse). |
| **input_schema_ref** | URI or path to **input** **schema** (e.g. future `schemas/tools/…` or OpenAPI fragment); **`TBD`** allowed only for **`planned`** tools with **SAFE UNKNOWN** called out in the row **notes**. |
| **output_schema_ref** | URI or path to **output** **schema**; same **`TBD`** rule as inputs. |
| **side_effects** | **`no`** — no durable or external mutation beyond logs explicitly scoped as non-authoritative; **`yes`** — **must** include a **short** **description** (what mutates, which systems). **No** **hidden** side effects: if **yes**, **description** is **mandatory**. |
| **approval_required** | **`yes`** / **`no`** — whether **NEED HUMAN APPROVAL** (or equivalent gate) **must** fire before **first** **side-effecting** **invocation** per [../security/approval-gates.md](../security/approval-gates.md). **High** **risk_level** **must** be **`yes`** in v0 unless **explicit** **governance** **exception** is recorded in [../governance/risk-register.md](../governance/risk-register.md). |

---

## 3. Tool lifecycle (governance)

Normative **state** **progression** for a tool **definition** (documentation and future registry rows):

```text
proposed → validated → approved → active → deprecated
```

| Stage | Meaning |
|-------|---------|
| **proposed** | Author proposes a row; **status** in row schema may remain **`planned`** or **`draft`**. |
| **validated** | **Schemas**, **side_effects**, **permissions**, and **risk_level** reviewed for consistency with [tool-safety-model-v0.md](tool-safety-model-v0.md) and [../security/threat-model-v0.md](../security/threat-model-v0.md). |
| **approved** | **Governance** / **security** **sign-off** (process **SAFE UNKNOWN**); row may move toward **`active`**. |
| **active** | **Invocable** under documented constraints; **`status`** = **`active`**. |
| **deprecated** | **No** new bindings; **`status`** = **`deprecated`**; consumers **must** migrate. |

**Skipping** **stages** **without** **recorded** **rationale** **is** **out** **of** **scope** for **v0** **compliance** **narrative**.

---

## 4. Example tools (**planned** — illustrative only)

| tool_id | name | type | status | allowed_agents | required_permissions | risk_level | input_schema_ref | output_schema_ref | side_effects | approval_required |
|---------|------|------|--------|----------------|----------------------|------------|------------------|-------------------|--------------|-------------------|
| `mars.tool.example.read_repo_file` | Read repository file | `internal` | `planned` | `researcher`, `coder` (example) | `read` | `low` | `TBD` | `TBD` | **no** — read-only file read within declared roots | `no` |
| `mars.tool.example.http_get_metadata` | HTTP GET (metadata) | `integration` | `planned` | `researcher` | `read`, `external-call` | `medium` | `TBD` | `TBD` | **yes** — network egress; response size/cache effects | `yes` |
| `mars.tool.example.run_ci_script` | Run CI helper script | `script` | `planned` | `builder` | `execute` | `medium` | `TBD` | `TBD` | **yes** — subprocess execution, workspace artefacts | `yes` |
| `mars.tool.example.memory_upsert` | Curated memory upsert | `internal` | `planned` | `memory_agent` | `write` | `high` | `TBD` | `TBD` | **yes** — durable memory mutation per [../memory/memory-write-policy-v0.md](../memory/memory-write-policy-v0.md) | `yes` |
| `mars.tool.example.deploy_preview` | Deploy preview environment | `api` | `planned` | `deployer` | `write`, `external-call` | `high` | `TBD` | `TBD` | **yes** — external infra; billable resources; possible data paths | `yes` |

**Honesty:** These rows are **not** implemented tools; they exist to **exercise** the schema and **risk** / **approval** columns.

---

## 5. Relation to other artefacts

| Artefact | Relation |
|----------|----------|
| [tool-contract-v0.md](tool-contract-v0.md) | **Invocation** **envelope** **and** **outputs** **must** **cite** **registry** **tool_id** **and** **fields** **above**. |
| [tool-safety-model-v0.md](tool-safety-model-v0.md) | **risk_level**, **side_effects**, **approval_required** **normative** **interpretation**. |
| [../agents/registry.md](../agents/registry.md) | **allowed_agents** **resolves** **against** **catalog** **rows** **(design)**. |
| [../mars-runtime/execution-bridge-v0.md](../mars-runtime/execution-bridge-v0.md) | **Executor** **categories** **(API,** **Scripts,** **…)** **map** **to** **tool** **types** **at** **bridge** **handoff** **(see** [tool-execution-model-v0.md](tool-execution-model-v0.md)**)**. |
| [../governance/dependency-map.md](../governance/dependency-map.md) | **Entity** **`tool_registry`**. |

---

## 6. Changelog (documentation)

| Date | Change |
|------|--------|
| 2026-04-27 | **Tool** **Registry** **v0** — row schema, lifecycle, **five** **planned** **examples**, **cross**-**refs**. |

---

*End of MARS Tool Registry v0.*
