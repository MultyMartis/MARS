# `security` — Security / Guardrails (MARS)

## Purpose

This folder holds **Security / Guardrails v0** as **system contracts only**: policies, permissions vocabulary, approval gates, and I/O validation expectations **in prose**. It corresponds to the **Security / Guardrails** layer in architecture narratives (`../web-gpt-sources/02_architecture.md`, `../web-gpt-sources/09_security.md` when present) and to **Stage 8** prep in `../governance/master-build-map.md`.

## Documents (v0)

| File | Description |
|------|-------------|
| [guardrails-v0.md](guardrails-v0.md) | Guardrails purpose, layer relations, input/output validation, injection awareness, **SAFE UNKNOWN**, no hallucination, no silent failure, **activation invariant**. |
| [permissions-v0.md](permissions-v0.md) | Scopes (**read**, **write**, **execute**, **external-call**), entity-level permissions, **no default superuser**, passport declarations. |
| [approval-gates.md](approval-gates.md) | **NEED HUMAN APPROVAL** conditions (filesystem, structure, external APIs, storage/PII, agent CRUD, side-effect tools). |
| [threat-model-v0.md](threat-model-v0.md) | Threat Model v0 — purpose, eight threat categories (injection, secrets, tool abuse, exfiltration, memory write, retry/duplicate, integration, false-implementation claim), layer mapping, related system signals, mitigation references, and risk register ids (Stage 8.5 P0; documentation only). |

## Relation to MARS architecture

- **Identity** and **authorization** enforcement are **not** implemented here; contracts attach expectations to **Control Plane** routing, **Workflow** tasks/signals, **Agent Registry** / **Agent Factory**, future **Tool** layer, and **Introspection** honesty rules.
- **Introspection** consumers should read [guardrails-v0.md](guardrails-v0.md) alongside `../interfaces/introspection-v0.md` for **anti-fabrication** alignment.

## Status

**Documentation / planned contract only** — there is **no** security **runtime**, **policy engine**, **enforcement** code, **secrets**, **sandbox**, or **ACL implementation** in this directory. Adding **security tools** or **runtime policies** is **out of scope** for v0 contracts unless a later stage explicitly introduces them with evidence in-tree.

---

## Signals (relation to Security / Guardrails)

MARS v0 **system signals** are **canonically** defined in [../governance/system-signals-dictionary.md](../governance/system-signals-dictionary.md) and referenced from tasks in `../workflows/task-contract-v0.md` §3. This table states how **Security / Guardrails** treats each signal (design-time and intended runtime semantics).

| Signal | Meaning in security / guardrails context |
|--------|------------------------------------------|
| **UNKNOWN** | **Binding missing** (e.g. agent not in registry, permission not declared) — **do not** proceed with guessed identity or access; resolve registry/passport state first. Aligns with **fail closed** routing. |
| **SAFE UNKNOWN** | **Honest uncertainty** — no invention; may still **block** or require clarification. Distinct from “approved to proceed silently.” See `../governance/universal-entity-operations.md` §6. |
| **NEED HUMAN APPROVAL** | **HITL required** per [approval-gates.md](approval-gates.md) or task **hitl_gates**; automation must not **finalize** gated effects until satisfied. |
| **SECURITY RISK** | **Policy violation**, suspected **injection**, **scope escape**, or **dangerous** route — **must not** continue **unchallenged**; resolution path is **product-defined** (block, escalate, narrow scope). |
| **STRUCTURE CHANGE** | **Structural** mismatch (layout, impossible **required_agents**, wrong **scope_in**) — replan or **human** architectural decision; often overlaps filesystem / project-tree **approval** concerns. (Legacy `STRUCTURE_CHANGE` → [dictionary](../governance/system-signals-dictionary.md) §3.) |

**Emitters:** When an implementation exists, **Control Plane** is the **orchestrated** source of truth for **emission** (`../workflows/task-contract-v0.md` §3 note). Until then, humans and editors apply these signals **discursively** per `../AGENTS.md` closeout.

---

## Activation rule (summary)

No entity may be **active** without **passport**, **registry entry**, **permissions** (explicit), and **validation rules** — see [guardrails-v0.md](guardrails-v0.md) §10 and [permissions-v0.md](permissions-v0.md) §4.

---

## SAFE UNKNOWN

Live **enforcement** of this folder’s contracts, **credential** storage, and **production** **SOC** processes are **not** provable from markdown alone — state **SAFE UNKNOWN** for operational guarantees unless another in-repo artifact proves them.
