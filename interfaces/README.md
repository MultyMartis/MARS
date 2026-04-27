# `interfaces`

## Purpose

Reserved for **user and system entrypoints**: chat, admin, CLI, bots, HTTP API, webhooks, IDE-style channels — the **Interface Layer** in `web-gpt-sources/02_architecture.md` and `web-gpt-sources/11_interfaces_runtime.md`.

## Relation to MARS architecture

Documents the planned Interface Layer contracts. Feeds the **Control Plane** and must respect **Security** and **Observability** concerns when implemented.

## Introspection, Self-Describe, Self-Check, Self-Audit, and Self-Heal (v0)

**Documented** — specification only (no code, no prompts, no runtime, no config):

| Document | Description |
|----------|-------------|
| [introspection-v0.md](introspection-v0.md) | Introspection System purpose, Interface Layer role, relations to registry / governance / logs / workflow / memory, Self-Describe Engine inputs, data sources, output rules, update rule. |
| [self-describe-modes.md](self-describe-modes.md) | Modes: FULL, SHORT, DEBUG, ENTITY, PROJECT — scope and **SAFE UNKNOWN** behavior. |
| [self-check-v0.md](self-check-v0.md) | **Self-Check** v0: quick entity-level **consistency** (passport, registry, status, `owner_layer`, related docs, no false implementation claim); **PASS** / **FAIL** / **NEED REVIEW** and outputs (specification only). |
| [self-audit-v0.md](self-audit-v0.md) | **Self-Audit** v0: deeper review over entity and documented **dependencies**; **normative** checks and result shape. See [universal-entity-operations.md](../governance/universal-entity-operations.md). |
| [self-heal-v0.md](self-heal-v0.md) | **Self-Heal** v0: **plan-only** recovery / fix **plans** from Self-Check, Self-Audit, Risk Register, Dependency Map, and Lifecycle Log; outputs, recovery types, approvals, and system-signal handling (specification only; **no** execution or auto-fix). |
| [recovery-playbooks-v0.md](recovery-playbooks-v0.md) | **Recovery** **Playbooks** v0: approved recovery **patterns** (triggers, allowed and forbidden actions, required approval, related signals) paired with Self-Heal; seven playbook types including documentation fix, path correction, registry repair, risk escalation, memory write correction, execution failure recovery, and security incident escalation (documentation only). |

**Universal** **entity** model (types, **facets**, **operations**): [governance/universal-entity-operations.md](../governance/universal-entity-operations.md).

---

## Status

**Planned** for general interface implementations — the **v0** contracts above are **documented** only; other entrypoints remain placeholder until implemented.
