# MARS — Threat Model v0

**Status:** documented — MARS-native threat taxonomy and traceability for design-time review. No runtime scanner, no machine schema, and no in-repo enforcement for Phase 1. Aligns with [governance/dependency-map.md](../governance/dependency-map.md) entity `threat_model`, [governance/risk-register.md](../governance/risk-register.md), and [governance/system-signals-dictionary.md](../governance/system-signals-dictionary.md).

**Version:** v0. Revisable per [governance/versioning-model.md](../governance/versioning-model.md) and [governance/master-build-map.md](../governance/master-build-map.md) Stage 8.5.

---

## 1. Purpose

- Name cross-cutting threat classes for MARS as documented (agents, control plane, workflows, Execution Bridge, state store, memory, future Tool-layer contracts) so risk rows, signals, and contracts stay aligned before and after runtime implementation exists.
- Tie each class to layers (per [governance/capability-map.md](../governance/capability-map.md) and architecture packs), canonical system signals, and mitigation pointers in existing v0 security and workflow documents.
- Complement [guardrails-v0.md](guardrails-v0.md), [permissions-v0.md](permissions-v0.md), [approval-gates.md](approval-gates.md), and Stage 8.5 P0 contracts (Execution Bridge, Runtime State Store, Failure Model, Memory Write Policy, Checkpoint/Resume) without claiming in-repo enforcement.

**SAFE UNKNOWN:** This file does not enumerate all possible attacks. Absence of a category for a given hazard does not mean the hazard is absent in the real world. New integrations, Tool surfaces, or runtime code may require new categories or [risk-register.md](../governance/risk-register.md) rows per its §2.

**Honesty (normative):** MARS v0 is documentation-first; [AGENTS.md](../AGENTS.md) applies to all outputs, including inferences of “what is implemented” from threat discussion. See category 8.

---

## 2. Scope and out of scope

| In scope (v0) | Out of scope (v0) |
|---------------|-------------------|
| Categories, layer mapping, related signals, pointers to mitigation docs and risk ids | CVSS, live pentest playbooks, WAF rules, key-rotation SOPs |
| Cross-links to P0 Stage 8.5 contracts and governance artefacts | Code or config under `tools/`, `models/`, or a separate runtime tree |
| Triggers for updating [risk-register.md](../governance/risk-register.md) when a hazard materialises in review | Automated detection, SIEM playbooks, live SOC tooling |

---

## 3. Threat categories (v0)

For each row, affected layers are illustrative. Concrete scope and mitigation must be taken from cited documents and [risk-register.md](../governance/risk-register.md) rows, not from this file alone. Signal names are canonical from [governance/system-signals-dictionary.md](../governance/system-signals-dictionary.md) §2 (e.g. `SECURITY RISK` — space, not an underscore token).

---

### 1) Prompt injection

| Facet | Content |
|--------|---------|
| **Description** | Untrusted or adversarial input (user prompts, documents, tool or bridge return shapes) subverts goals — e.g. jailbreak narratives, indirect injection via retrieved text, or instruction hiding in RAG or memory. Documented design hazard; this repo does not claim a running MARS planner or model. |
| **Affected layers** | Interface (inputs); Control Plane (routing, goal binding); Workflow / Task (scope, planner outputs); Memory / RAG; Tool layer (Stage 9, planned). |
| **Related signals** | `SECURITY RISK`, `UNKNOWN` (missing passport or policy binding), `STRUCTURE CHANGE` (injection forces impossible task decomposition). |
| **Mitigation references** (non-exhaustive) | [guardrails-v0.md](guardrails-v0.md) (injection, output validation); [permissions-v0.md](permissions-v0.md) (scoping); [workflows/execution-flow.md](../workflows/execution-flow.md), [mars-runtime/execution-bridge-v0.md](../mars-runtime/execution-bridge-v0.md) (stage boundaries); [memory/memory-write-policy-v0.md](../memory/memory-write-policy-v0.md) (what may re-enter context). |
| **Related risk IDs** (from [risk-register.md](../governance/risk-register.md) §8) | RISK-V0-0003 (narrative honesty); RISK-V0-0006 (RAG and external data paths); RISK-V0-0007 (PII in durable memory from tainted ingestion); RISK-V0-0008 through RISK-V0-0010 (state, retry, checkpoint in design when injection could drive tool-like or bridge-like behaviour); RISK-V0-0012 (register anchor for tool-facing hazards). |

---

### 2) Secret leakage

| Facet | Content |
|--------|---------|
| **Description** | API keys, tokens, connection strings, or other credentials appear in durable artefacts (docs, logs, registries, RAG chunks, over-broad self-describe) or in unreviewed pasted output, increasing unauthorised reuse or lateral abuse. |
| **Affected layers** | Governance / logs; registries; interfaces / introspection; memory / RAG; integrations; Model layer (future) for provider creds. |
| **Related signals** | `SECURITY RISK`, `NEED HUMAN APPROVAL` (rotation, registry change), `SAFE UNKNOWN` (unclear whether a value is secret). |
| **Mitigation references** | [guardrails-v0.md](guardrails-v0.md); [approval-gates.md](approval-gates.md); [memory/memory-write-policy-v0.md](../memory/memory-write-policy-v0.md) (prohibited content); [registry/project-registry.md](../registry/project-registry.md) (v0: no raw secrets in rows, by convention). |
| **Related risk IDs** | RISK-V0-0003, RISK-V0-0004 (unreviewed large change sets), RISK-V0-0006, RISK-V0-0007, RISK-V0-0008 (sensitive blobs in `errors` / state in design). |

---

### 3) Tool abuse

| Facet | Content |
|--------|---------|
| **Description** | Excessive or unauthorised use of MCP, tools, or bridge-emitted tool-like side effects: unbounded retries, side-effect calls without approval, or tool chains that violate entity passport or task scope (documented hazard before enforcement). |
| **Affected layers** | Tool (Stage 9); Control Plane; Task / Workflow; Execution Bridge; security (permissions, gates). |
| **Related signals** | `SECURITY RISK`, `UNKNOWN` (no permitted path), `NEED HUMAN APPROVAL` (gated side effects). |
| **Mitigation references** | [permissions-v0.md](permissions-v0.md) (execute, external-call); [approval-gates.md](approval-gates.md) (side-effect tools); [workflows/failure-model-v0.md](../workflows/failure-model-v0.md) (idempotency, retry ceiling); [mars-runtime/execution-bridge-v0.md](../mars-runtime/execution-bridge-v0.md) (failure modes, outputs). |
| **Related risk IDs** | RISK-V0-0005, RISK-V0-0006, RISK-V0-0008 through RISK-V0-0010 (duplication and boundaries), RISK-V0-0012. |

---

### 4) Data exfiltration

| Facet | Content |
|--------|---------|
| **Description** | Unintended export of project or operator data (including PII) via RAG synthesis, tool return channels, or self-describe or introspection modes that are not scoped, per documentation and process. |
| **Affected layers** | Interface; introspection; memory / RAG; integrations; Model. |
| **Related signals** | `NEED HUMAN APPROVAL`, `SECURITY RISK`, `SAFE UNKNOWN` (scope not verified in-repo). |
| **Mitigation references** | [interfaces/self-describe-modes.md](../interfaces/self-describe-modes.md); [introspection-v0.md](../interfaces/introspection-v0.md) (SoT); [memory/memory-write-policy-v0.md](../memory/memory-write-policy-v0.md); [approval-gates.md](approval-gates.md) (PII, external). |
| **Related risk IDs** | RISK-V0-0006, RISK-V0-0007, RISK-V0-0008, RISK-V0-0003. |

---

### 5) Unsafe memory write

| Facet | Content |
|--------|---------|
| **Description** | Durable knowledge (memory / RAG as designed) is written in violation of retention, writer role, or content rules — e.g. stale or adversarial facts, or wrong `project_id` (design and future enforcement gap per RISK-V0-0005). |
| **Affected layers** | Memory; Task (scope, scope_in); agent (writer roles); governance and registry. |
| **Related signals** | `NEED HUMAN APPROVAL` (PII, sensitive), `SECURITY RISK` (policy), `CONTEXT MIGRATION NEEDED` (index / version skew). |
| **Mitigation references** | [memory/memory-write-policy-v0.md](../memory/memory-write-policy-v0.md); [permissions-v0.md](permissions-v0.md); [registry/project-registry.md](../registry/project-registry.md); [storage/checkpoint-resume-protocol-v0.md](../storage/checkpoint-resume-protocol-v0.md) (pairing with memory policy). |
| **Related risk IDs** | RISK-V0-0007, RISK-V0-0011, RISK-V0-0008 (durable run state vs long-term memory separation). |

---

### 6) Unsafe retry / duplicate action

| Facet | Content |
|--------|---------|
| **Description** | Idempotency gaps, double submit, or replayed checkpoints after partial side effects, including HITL pickup ambiguity (Failure Model, Checkpoint/Resume, RISK-V0-0009, RISK-V0-0010). |
| **Affected layers** | Workflow; Execution Bridge; Runtime State Store; Control Plane. |
| **Related signals** | `STRUCTURE CHANGE` (replan after duplicate), `SECURITY RISK` (integrity on retry), `NEED HUMAN APPROVAL` (duplicate and side effect), `SAFE UNKNOWN` (dedup format not fixed in v0). |
| **Mitigation references** | [workflows/failure-model-v0.md](../workflows/failure-model-v0.md); [storage/checkpoint-resume-protocol-v0.md](../storage/checkpoint-resume-protocol-v0.md); [storage/runtime-state-store-v0.md](../storage/runtime-state-store-v0.md). |
| **Related risk IDs** | RISK-V0-0008, RISK-V0-0009, RISK-V0-0010. |

---

### 7) External integration risk

| Facet | Content |
|--------|---------|
| **Description** | Unreviewed or underspecified third-party endpoints, credential storage, and data exit paths, per [risk-register.md](../governance/risk-register.md) §7.3. Includes MCP or model routing when live contracts are scoped. |
| **Affected layers** | Integrations; Tool; Model; Control Plane; security (gates). |
| **Related signals** | `UNKNOWN` (no allowed route), `NEED HUMAN APPROVAL` (gated external path), `SAFE UNKNOWN` (topology not in repo), `SECURITY RISK` (escape). |
| **Mitigation references** | [risk-register.md](../governance/risk-register.md) §7; [approval-gates.md](approval-gates.md); [guardrails-v0.md](guardrails-v0.md); [governance/dependency-map.md](../governance/dependency-map.md). |
| **Related risk IDs** | RISK-V0-0005, RISK-V0-0006, RISK-V0-0007, RISK-V0-0008. |

---

### 8) False implementation claim

| Facet | Content |
|--------|---------|
| **Description** | A narrative or artefact states that MARS (or a subsystem) is implemented, deployed, or active in a way not evidenced in this repository or a named SoT, violating [AGENTS.md](../AGENTS.md) and RISK-V0-0003 — including self-describe oversell, or documents that imply defences exist in code when they do not. |
| **Affected layers** | All (especially governance, interfaces, security, memory, runtime narrative). |
| **Related signals** | `SAFE UNKNOWN` (honest gap), `SECURITY RISK` (dishonest or governance-integrity claim). |
| **Mitigation references** | [AGENTS.md](../AGENTS.md) (documented / planned / legacy split); [interfaces/self-check-v0.md](../interfaces/self-check-v0.md); [interfaces/self-audit-v0.md](../interfaces/self-audit-v0.md). |
| **Related risk IDs** | RISK-V0-0003 (primary), RISK-V0-0005 (runtime and enforcement gap honesty). |

---

## 4. Changelog (documentation)

| Date | Change |
|------|--------|
| 2026-04-27 | Threat Model v0 — purpose, eight categories, layers, signals, mitigation references, risk id ties. Honesty. No code or enforcement. |

---

*End of MARS Threat Model v0.*
