# MARS — Governance

**Status:** **documented** — system-level **control** documents: boundaries, execution, state, versioning, and the **capability** map. These files **govern** how MARS is described; they are **not** a substitute for `../AGENTS.md` honesty about **documented** vs **planned** vs **legacy** **imported** material.

---

## Governance addenda (this folder)

| Document | Description |
|----------|-------------|
| [master-build-map.md](master-build-map.md) | **Primary roadmap / build order** (v0): stages 0–16, **doc vs planned-implementation** posture, **dependencies**, **audit blockers**, and rules for logging build-order changes to `../logs/` (until replaced by a formal project tracker). |
| [dependency-map.md](dependency-map.md) | v0 directed **dependencies** between system-level **contract** **entities** (`entity_id` → `depends_on`, `dependency_type`, `reason`, `risk_if_broken`); **maintenance** **rules**; **SAFE** **UNKNOWN** for unmapped edges. Prerequisite for **Self-Heal** / **Tool** / **Model** / **runtime** **documentation** alongside [risk-register.md](risk-register.md) (see [master-build-map](master-build-map.md)). |
| [risk-register.md](risk-register.md) | v0 **Risk** **Register**: purpose, **when** to add/update rows, **fields** and **enums**, relations to **dependency** **map**, **signals**, **guardrails**, **lifecycle** **log**; **normative** rules for **SECURITY** **RISK**, **NEED** **HUMAN** **APPROVAL**, **integrations**, and **runtime** **reviews**; seed **risks**. **Governance** **Foundation**; prerequisite for **Tool** / **Model** / **runtime** **documentation** per **master** **build** **map**. |
| [capability-map.md](capability-map.md) | System **capabilities** and **logical** mapping: capability → **agents** → **workflows** → **tools** (no **implementation** claims). |
| [system-boundaries.md](system-boundaries.md) | What is **inside** MARS (design / repo) vs **outside** (external systems) and **responsibility** borders. |
| [execution-model.md](execution-model.md) | How work runs **today** (Web-GPT → Cursor) and **future** surfaces (runtime, n8n, **agents**); **Execution Bridge** concept. |
| [state-model.md](state-model.md) | **Task**, **workflow run**, and **agent registry** **states** and **allowed** **transitions**. |
| [versioning-model.md](versioning-model.md) | System vs **entity** versions, **contract** **changes**, **compatibility** **rules**. |
| [universal-entity-operations.md](universal-entity-operations.md) | **Universal** vocabulary for **entity**-level **Self-Describe**, **Self-Check**, **Self-Audit**, **Self-Migrate**, **capability** **discovery**, and **Risk** **Review**; **types**, **common** **facets**, and relation to [../interfaces/introspection-v0.md](../interfaces/introspection-v0.md) (specification only). |
| [system-signals-dictionary.md](system-signals-dictionary.md) | Canonical v0 system **signal** **names** and **alias** / **STRUCTURE** **policy**; **referenced** from [master-build-map](master-build-map.md), [dependency-map](dependency-map.md), and **workflow** / **task** **contracts** (documentation). |
| [runtime-registry-boundaries.md](runtime-registry-boundaries.md) | **Clarification:** governance registries vs **R1** experimental runtime lookups vs **external** catalogs — avoids **registry illusion**. |
| [registry-architecture.md](registry-architecture.md) | **Phase S2 — registry hygiene:** kinds of registries (governance, operational, R1, external, doc catalogs, lifecycle log, Website Factory); **registry presence ≠ runtime existence**. |
| [registry-source-of-truth.md](registry-source-of-truth.md) | **Phase S2:** precedence and conflict rules; runtime and README do not silently override governance; lifecycle log = events, not implementation truth; **human** resolution only. |
| [identity-and-naming-rules.md](identity-and-naming-rules.md) | **Phase S2:** minimal naming discipline (agents, workflows, adapters, tools, projects, Factory, bridges, experiments, governance). |
| [registry-entry-minimal-standard.md](registry-entry-minimal-standard.md) | **Phase S2:** lightweight minimum fields for **human-managed** registry rows (not schema-heavy, not DB-oriented). |
| [external-system-boundaries.md](external-system-boundaries.md) | **Phase S2:** MetaBOT (external multi-workflow) vs **in-repo** adapters vs legacy `seo-content-agent`; external IDs ≠ automatic MARS canonical entities. |
| **[enforcement/](enforcement/README.md)** | **Phase S1 — governance enforcement (documentation):** human-readable **anti-drift** catalog, **forbidden-claim** cues, **terminology** boundaries, **future optional** validation strategy — **not** runtime, **not** CI, **not** autonomous policy. |
| [operational-survivability.md](operational-survivability.md) | **Phase S3 — operational survivability (documentation):** human-operated evolving governance; continuity, anti-drift, anti-overload, anti-fragmentation, anti-fake-runtime posture — **not** automation, **not** orchestration. |
| [documentation-entropy-rules.md](documentation-entropy-rules.md) | **Phase S3:** when **not** to add docs, merge/deprecate/index patterns, entropy warning signs — human discipline only. |
| [onboarding-survivability.md](onboarding-survivability.md) | **Phase S3:** minimum reads, safe sequence, optional vs historical vs governance-critical — reduces overload and false runtime assumptions. |
| [operator-load-management.md](operator-load-management.md) | **Phase S3:** overload signals (lanes, workflows, prompts, governance fatigue) and **lightweight** mitigations — no tooling claims. |
| [context-continuity-rules.md](context-continuity-rules.md) | **Phase S3:** chat/session continuity, migration package, REPORT alignment, parallel-chat discipline — **no** automatic persistence. |
| [stabilization-vs-expansion.md](stabilization-vs-expansion.md) | **Phase S3:** when to stabilize vs expand; governance/survivability debt signals — discourages runaway layering and speculative futures-as-fact. |
| [execution-contracts-overview.md](execution-contracts-overview.md) | **Phase S4 — execution contract stabilization:** role of **execution contracts** as **governance semantics** (not runtime orchestration); maps **task**, **prompt**, **execution**, **REPORT**, **validation**, **artifact**, **lifecycle**, **registry**, **SAFE UNKNOWN**. |
| [task-envelope-standard.md](task-envelope-standard.md) | **Phase S4:** lightweight **task envelope** shape; separates governance contract, **planned** runtime payload, human instructions, external workflow payloads — no mandated schema file. |
| [execution-phase-model.md](execution-phase-model.md) | **Phase S4:** minimal **phase** vocabulary (intake → … → report, etc.); human narration only; aligns **REPORT** and [parallel-cursor-chat-work-mode-v0.md](parallel-cursor-chat-work-mode-v0.md); not an automation state machine. |
| [artifact-lifecycle-rules.md](artifact-lifecycle-rules.md) | **Phase S4:** **artifact** labels (draft, stabilized, deprecated, historical, experimental, …); when to merge/deprecate/archive; anti-drift — no storage engine, no automated lifecycle product. |
| [validation-chain-semantics.md](validation-chain-semantics.md) | **Phase S4:** meanings of **validation** (human, checklist, external CI, governance read, experimental, …); **validation mention ≠ automated validation exists**. |
| [execution-boundary-clarification.md](execution-boundary-clarification.md) | **Phase S4:** boundaries among governance docs, **Cursor** execution, **planned** runtime, external systems, Website Factory lane, adapters, bridges — **where execution happens today** vs modeled-only. |
| [operational-tooling-overview.md](operational-tooling-overview.md) | **Phase S5 — operational tooling boundaries:** role of **lightweight** helpers/validators/scanners/scripts; **not** orchestration, **not** hidden runtime. |
| [tooling-boundary-rules.md](tooling-boundary-rules.md) | **Phase S5:** where tooling stops vs runtime/orchestrator/daemon/workflow-engine semantics; red flags; **HITL** / **REPORT** alignment. |
| [experimental-tooling-status.md](experimental-tooling-status.md) | **Phase S5:** vocabulary for draft/experimental/local/operator utilities; **experimental ≠ runtime capability**. |
| [lightweight-script-guidelines.md](lightweight-script-guidelines.md) | **Phase S5:** safe patterns for small **manual** scripts; unsafe patterns; keep heavy product automation out of `governance/**`. |
| [adapter-and-bridge-boundaries.md](adapter-and-bridge-boundaries.md) | **Phase S5:** adapter vs system, bridge vs engine, integration vs ownership; aligns MetaBOT + S4 execution boundaries. |
| [tooling-escalation-warnings.md](tooling-escalation-warnings.md) | **Phase S5:** signals of tooling drift (hidden state, implicit scheduling, pseudo-control-plane); recommended **human** actions — **not** automated monitoring. |
| [controlled-operationalization.md](controlled-operationalization.md) | **Phase S6 — controlled operationalization:** governance-first semantics for **real** helpers and **semi-structured** interoperability; **not** autonomous runtime, **not** orchestration. |
| [operational-helper-classification.md](operational-helper-classification.md) | **Phase S6:** lightweight helper classes (formatter, validator, exporter, …), scope, danger zones, runtime-risk vocabulary — aligns S5 boundaries. |
| [interoperability-semantics.md](interoperability-semantics.md) | **Phase S6:** safe vs unsafe interoperability; explicit exports/envelopes/reports vs implicit coordination — **not** shared runtime product. |
| [operationalization-maturity-levels.md](operationalization-maturity-levels.md) | **Phase S6:** documentation-only → runtime-scoped experimental maturity labels — **no** fake production framing. |
| [human-execution-guarantees.md](human-execution-guarantees.md) | **Phase S6:** HITL integrity during operationalization (explicit initiation, visible execution, REPORT ownership) — **not** enforcement automation. |
| [operationalization-drift-warnings.md](operationalization-drift-warnings.md) | **Phase S6:** red flags toward pseudo-runtime, hidden orchestration, automation creep; stabilization / pause-expansion cues — **human** triage only. |
| [operational-experiments-overview.md](operational-experiments-overview.md) | **Phase S7 — operational experiment framework:** controlled operational probes, evidence-first evolution, experiment→pattern **without** auto-promote — **not** runtime product, **not** orchestration. |
| [experiment-classification.md](experiment-classification.md) | **Phase S7:** lightweight experiment types; acceptable scope, evidence expectations, runtime/governance risk, stabilization cues. |
| [experiment-evidence-rules.md](experiment-evidence-rules.md) | **Phase S7:** operational evidence states; rejects false equivalences (screenshots, single run, local script, experimental path as platform proof). |
| [experiment-to-pattern-transition.md](experiment-to-pattern-transition.md) | **Phase S7:** human-gated stabilization, repeatability, naming/doc cleanup, deprecation of failures, migration into canonical docs — **no** automated promotion. |
| [experimental-isolation-rules.md](experimental-isolation-rules.md) | **Phase S7:** separation from governance core, lane discipline, runtime-scoped/local handling, naming and visibility — anti-masquerade. |
| [operational-lessons-and-postmortems.md](operational-lessons-and-postmortems.md) | **Phase S7:** lightweight lessons/postmortem sections; failed experiments acceptable; **SAFE UNKNOWN** outcomes acceptable — **not** incident automation. |
| [reality-audit-framework.md](reality-audit-framework.md) | **Reality audit (documentation):** human-led operational reality / usefulness / friction / drift review — **not** certification, **not** runtime validation, **not** telemetry. |
| [reality-audit-questions.md](reality-audit-questions.md) | **Reality audit:** lightweight **human-reviewed** question groups (usefulness, friction, onboarding, helpers, mythology risk, …). |
| [operational-friction-semantics.md](operational-friction-semantics.md) | **Reality audit:** vocabulary for **healthy vs destructive** operational friction — diagnosis only. |
| [deprecation-and-pruning-semantics.md](deprecation-and-pruning-semantics.md) | **Reality audit:** normalize archive / merge / prune signals and **historical but not active** posture — aligns with S4 lifecycle labels. |
| [governance-usefulness-review.md](governance-usefulness-review.md) | **Reality audit:** how to judge governance **operational value** vs maintenance cost — qualitative dimensions only. |
| [reality-vs-mythology-warnings.md](reality-vs-mythology-warnings.md) | **Reality audit:** warning patterns when abstractions drift from evidence; corrective **human** actions — **not** automated claim detection. |

---

## Linked governance inputs (elsewhere in the repo)

**Established** artifacts (paths relative to `governance/`) that governance documents reference:

| Topic | Location |
|-------|----------|
| **Terminology map** (legacy → MARS) | [../web-gpt-sources/01_system.md](../web-gpt-sources/01_system.md) (section `terminology-map.md`) |
| **Entity** identity / “passport”-style **content** (agent **cards**) | [../agents/agent-card-template.md](../agents/agent-card-template.md) — per-role **definition** template. No `entity-passport.md` in this repository; **analog** is the **card**. **SAFE UNKNOWN** for out-of-tree passports. |
| **System / Agent** **Registry** (catalog) | [../agents/registry.md](../agents/registry.md) |
| **Lifecycle** / run history **(concept)** | [../web-gpt-sources/10_observability_eval.md](../web-gpt-sources/10_observability_eval.md), [../web-gpt-sources/13_migration.md](../web-gpt-sources/13_migration.md) (maps **Lifecycle** **log** to **target** **layers**); [../observability/README.md](../observability/README.md) |
| **Roadmap** / **phases** | [../web-gpt-sources/14_roadmap.md](../web-gpt-sources/14_roadmap.md) |
| **Task** and **execution** **flow** (contracts) | [../workflows/task-contract-v0.md](../workflows/task-contract-v0.md), [../workflows/execution-flow.md](../workflows/execution-flow.md), [../workflows/workflow-v0.md](../workflows/workflow-v0.md) |
| **Control Plane** | [../control-plane/contract.md](../control-plane/contract.md), [../control-plane/components.md](../control-plane/components.md) |
| **Top-level** **project** **rules** | [../AGENTS.md](../AGENTS.md), [../README.md](../README.md) |

---

*Last updated: Reality audit (documentation) — framework, questions, friction, pruning, usefulness review, mythology warnings (cross-cutting with S3–S7); Phase S7 — operational experiments / evidence / isolation / lessons; Phase S6 — controlled operationalization / interoperability / HITL guarantees / maturity / drift warnings; Phase S5 — operational tooling boundaries; Phase S4 — execution contract stabilization; Phase S3 — operational survivability; Phase S2 — registry / identity hygiene; Phase S1 — [enforcement/](enforcement/README.md); Phase S0 — [runtime-registry-boundaries.md](runtime-registry-boundaries.md); other governance addenda v0 as listed.*
