# MARS Survivability — Operational Safety Domain

**Status:** **documented** — human-operated safety layer design and audit artefacts.  
**Not:** runtime enforcement, policy engine, automated GitGuard product, or filesystem sandbox implementation.

**Lane:** B (Governance / Survivability / Operational Hardening)  
**Registry:** `mars-survivability` — [registry/project-registry.md](../../registry/project-registry.md)  
**Audit:** MARS Survivability & Safe Execution Audit v1 (2026-05-23)

---

## Purpose

Centralize **survivability**, **safe execution**, **destructive-operation policy**, and **Cursor-agent risk** documentation after the context-drift / destructive-delete incident class.

This domain **does not** replace:

- [AGENTS.md](../../AGENTS.md) and [.cursorrules](../../.cursorrules) (repo-wide agent discipline)
- [governance/operational-survivability.md](../../governance/operational-survivability.md) (Phase S3 baseline)
- [tools/tool-safety-model-v0.md](../../tools/tool-safety-model-v0.md) (tool risk taxonomy)
- Website Factory governance under `projects/mars-website-factory/`

It **extends** them with incident-informed contracts, protocols, registries, and scorecards.

---

## Structure

| Path | Role |
|------|------|
| [reports/](reports/) | Incident analysis, drills (D-01/D-02), S1 checkpoint, scorecard |
| [tools/](tools/) | Validator, helpers, observability (human-invoked CLI) |
| [contracts/](contracts/) | Normative policies (destructive ops, GitGuard evolution direction) |
| [protocols/](protocols/) | Safe execution layer, Website Factory production rules |
| [registries/](registries/) | Protected zones, forbidden patterns (human-maintained) |
| [guardrails/](guardrails/) | Cursor/agent prompt and session guardrails |
| [templates/](templates/) | Mandatory agent task and snapshot manifest templates |
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Navigation hub — **start here** for G0–G4 ops |
| [QUICKSTART.md](QUICKSTART.md) | Practical operator flows — pre-agent, snapshot, rollback, emergency |

---

## Canonical artefacts (v1)

| Document | Path |
|----------|------|
| Incident analysis | [reports/incident-analysis-cursor-agent-context-drift-v1.md](reports/incident-analysis-cursor-agent-context-drift-v1.md) |
| Destructive operations policy | [contracts/destructive-operations-policy-v1.md](contracts/destructive-operations-policy-v1.md) |
| Safe execution layer | [protocols/safe-execution-layer-v1.md](protocols/safe-execution-layer-v1.md) |
| GitGuard evolution | [contracts/gitguard-survivability-evolution-v1.md](contracts/gitguard-survivability-evolution-v1.md) |
| Website Factory hardening | [protocols/website-factory-safe-production-rules-v1.md](protocols/website-factory-safe-production-rules-v1.md) |
| Cursor agent risk analysis | [reports/cursor-agent-operational-risk-analysis-v1.md](reports/cursor-agent-operational-risk-analysis-v1.md) |
| Survivability scorecard | [reports/mars-survivability-scorecard-v1.md](reports/mars-survivability-scorecard-v1.md) |
| Protected zones registry | [registries/protected-zones-registry-v1.md](registries/protected-zones-registry-v1.md) |
| Agent guardrails index | [guardrails/cursor-agent-guardrails-v1.md](guardrails/cursor-agent-guardrails-v1.md) |
| Operational safety rules (G0) | [guardrails/cursor-operational-safety-rules-v1.md](guardrails/cursor-operational-safety-rules-v1.md) |
| Safe agent task template (G0) | [templates/safe-agent-task-template-v1.md](templates/safe-agent-task-template-v1.md) |
| Snapshot manifest standard (G0) | [protocols/snapshot-manifest-standard-v1.md](protocols/snapshot-manifest-standard-v1.md) |
| Agent risk classes (G0) | [contracts/agent-operation-risk-classes-v1.md](contracts/agent-operation-risk-classes-v1.md) |
| Operational index (G0–G1) | [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) |
| Enforcement registry (G1) | [registries/enforcement-rules-registry-v1.md](registries/enforcement-rules-registry-v1.md) |
| Operational halt protocol (G1) | [protocols/operational-halt-protocol-v1.md](protocols/operational-halt-protocol-v1.md) |
| Chat drift protocol (G1) | [protocols/chat-context-drift-protocol-v1.md](protocols/chat-context-drift-protocol-v1.md) |
| Safe prompt library (G1) | [guardrails/safe-prompt-pattern-library-v1.md](guardrails/safe-prompt-pattern-library-v1.md) |
| Website Factory enforcement (G1) | [contracts/website-factory-enforcement-v1.md](contracts/website-factory-enforcement-v1.md) |
| GitGuard system entry (G1) | [registries/gitguard-system-entry-v1.md](registries/gitguard-system-entry-v1.md) |
| Preflight checklist (G1) | [templates/survivability-preflight-checklist-v1.md](templates/survivability-preflight-checklist-v1.md) |

---

## GitGuard posture

**GitGuard** is named in [governance/system-entity-model.md](../../governance/system-entity-model.md) but has **no** `projects/gitguard/` pack in-repo ([governance/mars-reality-index-v0.md](../../governance/mars-reality-index-v0.md)). Evolution direction is specified in [contracts/gitguard-survivability-evolution-v1.md](contracts/gitguard-survivability-evolution-v1.md) as **design contract only**.

---

## Operator rule (v1)

Before any **destructive** or **wide-blast-radius** filesystem or git operation in AGENT mode: read [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) → [contracts/destructive-operations-policy-v1.md](contracts/destructive-operations-policy-v1.md) and [protocols/safe-execution-layer-v1.md](protocols/safe-execution-layer-v1.md). Default = **refuse** unless explicit human instruction + scope lock + snapshot plan exist.
