# MARS Website Factory — Validation Runtime Model v0 — overview

**Status:** **documentation only** — **semantic and governance vocabulary** for how validation is **reasoned about**, **evidenced**, **gated**, and **human-supervised** across the Website Factory pack. **Not** an executable runtime, **not** a validator engine, **not** orchestration code.

**Version:** v0.

**Related:** [validation-lifecycle-v0.md](validation-lifecycle-v0.md), [validator-execution-model-v0.md](validator-execution-model-v0.md), [validation-evidence-model-v0.md](validation-evidence-model-v0.md), [validation-result-semantics-v0.md](validation-result-semantics-v0.md), [validation-failure-semantics-v0.md](validation-failure-semantics-v0.md), [validation-waiver-semantics-v0.md](validation-waiver-semantics-v0.md), [validation-escalation-model-v0.md](validation-escalation-model-v0.md), [validation-consistency-model-v0.md](validation-consistency-model-v0.md), [validation-runtime-boundary-v0.md](validation-runtime-boundary-v0.md); [execution-semantics-overview-v0.md](execution-semantics-overview-v0.md), [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md), [qa-validation-model.md](qa-validation-model.md), [qa-result-payloads-v0.md](qa-result-payloads-v0.md), [semantic-qa-rules-v0.md](semantic-qa-rules-v0.md), [artifact-transfer-qa-rules-v0.md](artifact-transfer-qa-rules-v0.md), [website-factory-workflow-v0.md](website-factory-workflow-v0.md), [orchestration-signals-v0.md](orchestration-signals-v0.md), [prompt-standards-overview-v0.md](prompt-standards-overview-v0.md), [semantic-relationship-overview-v0.md](semantic-relationship-overview-v0.md), [artifact-bus-overview-v0.md](artifact-bus-overview-v0.md); [`../../governance/system-signals-dictionary.md`](../../governance/system-signals-dictionary.md), [`../../AGENTS.md`](../../AGENTS.md), [safe-unknown-boundary.md](safe-unknown-boundary.md).

---

## 1. Purpose

The **Validation Runtime Model v0** names **shared meaning** for:

- **validation semantics** — what “validated” may mean at a gate without implying automation;
- **validator methodology** — how cross-cutting review is framed relative to specialist QA;
- **validation graph philosophy** — treating consistency as **documented relationships** between artifacts and semantic objects, **not** as a stored graph engine;
- **QA runtime conceptual model** — lifecycle **tokens** and **handoffs** aligned with execution semantics and workflow v0, **without** a background QA service;
- **evidence model** — classes of proof, staleness, and **SAFE UNKNOWN**;
- **validation result model** — verdicts, severity, scope, blocking, confidence;
- **HITL validation governance** — who may close, waive, or escalate;
- **validation orchestration semantics** — how validation **fits** stages, signals, and artifact bus movement in **documentation** — **not** hidden orchestration.

It **connects** (as **documentation alignment**, not code wiring):

| Adjacent layer | Role in validation model |
|----------------|---------------------------|
| **Execution Semantics Layer v0** | Stage / artifact / approval / freeze / invalidation behavior that makes validation **timely** or **stale** |
| **Artifact Layer** | What is being validated (types, contracts, envelopes) |
| **Semantic Relationship Layer v0** | Cross-artifact meaning, consistency, dependency, freeze — inputs to **semantic** validation reasoning |
| **Prompt Standards Layer v0** | How prompts require evidence, REPORT shape, and HITL escalation |
| **QA Layer** | Lanes, payloads, gating — see [qa-validation-model.md](qa-validation-model.md), [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md) |
| **Workflow Layer** | [website-factory-workflow-v0.md](website-factory-workflow-v0.md) stages and MARS `execution-flow` **validate** alignment |
| **Agent Layer** | **Validator Agent** vs specialist QA roles per [`../../agents/registry.md`](../../agents/registry.md) — **documentation** |
| **Artifact Bus Layer v0** | Transfer, publication, consumption, transfer-QA — validation **at boundaries** |

---

## 2. Boundaries

This model **is**:

- vocabulary and rules for **authors, reviewers, and future contracts**;
- explicit **non-claims** so Phase 1 stays honest per [AGENTS.md](../../AGENTS.md).

This model **is not**:

- a shipped validator;
- CI, Lighthouse, crawlers, or deployment checks;
- a queue, scheduler, daemon, or distributed worker fabric for validation.

---

## 3. Validation philosophy

1. **Evidence-first** — no pass narrative without cited evidence class per [validation-evidence-model-v0.md](validation-evidence-model-v0.md); gaps → **SAFE UNKNOWN** or **UNKNOWN** per [`../../governance/system-signals-dictionary.md`](../../governance/system-signals-dictionary.md).
2. **HITL authority** — terminal governance actions (approval to ship, waivers that unblock delivery, revocation) remain **human-anchored** per [reference-project-hitl-governance-v0.md](reference-project-hitl-governance-v0.md) and [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md).
3. **Specialist depth + Validator breadth** — specialists own lane depth; **Validator** owns cross-cutting policy/task fit as **documented** in [qa-validation-model.md](qa-validation-model.md) (still **not** “autonomous enforcement”).
4. **Semantic graph as documentation** — “graph” means **relationships we can point to in prose and tables**, not a graph database (aligned with [semantic-relationship-overview-v0.md](semantic-relationship-overview-v0.md), [site-semantic-graph-v0.md](site-semantic-graph-v0.md)).
5. **Phase 1 = operational discipline** — teams **simulate** this model in Cursor/human workflow; nothing here **runs** by itself.

---

## 4. Validator role (documentation)

The **Validator Agent** is the **planned** cross-cutting role for structural/policy alignment with the **validate** stage in [`../../workflows/execution-flow.md`](../../workflows/execution-flow.md). In this model:

- the Validator **may** appear in narratives, matrices, and prompts;
- the Validator **does not** imply an always-on service, auto-merge, or auto-ship.

---

## 5. SAFE UNKNOWN enforcement

- Any field, tool, storage, or wire format **not** evidenced in-repo remains **SAFE UNKNOWN** in validation outputs (see [safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md), [safe-unknown-boundary.md](safe-unknown-boundary.md)).
- **SAFE UNKNOWN** is **not** a waiver, **not** auto-approval, **not** permission to fabricate SoT.

---

## 6. Explicit prohibitions (normative for this pack)

This documentation **must not** be read as authorizing:

| Forbidden | Meaning |
|-----------|---------|
| **Autonomous validator runtime** | No claim that validators run continuously or unattended |
| **Hidden execution engine** | No shadow step that “validates” without traceable evidence and ownership |
| **Auto-repair** | Findings may recommend fixes; **no** automatic mutation of artifacts or repos |
| **Auto-approval** | Passing a gate **requires** explicit human or contract-defined acceptance where HITL applies |
| **Auto-waiver** | Waivers are explicit, scoped, and attributed — see [validation-waiver-semantics-v0.md](validation-waiver-semantics-v0.md) |
| **Self-healing orchestration** | Recovery and heal semantics elsewhere are **plan-only** for MARS core; they **do not** extend to autonomous Website Factory validation |

---

*Last updated: 2026-05-12.*
