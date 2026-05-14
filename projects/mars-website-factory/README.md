# MARS Website Factory — project documentation pack

**project_id:** `mars-website-factory`  
**Status:** **planned** — **strategic, documentation-first** direction inside the MARS ecosystem.  
**Not claimed:** a single bot, a single runtime agent, autonomous studio, or production-ready automation.

## What this is

A **target architecture** for a **multi-agent, contract-driven** website production system: intake → strategy → IA → blueprints → wireframes → design → frontend production → QA → human approval → delivery. Execution in Phase 1 remains **human-supervised** and **prompt-driven** (see `../../governance/execution-model.md`).

## Production project packs

| Project | Pack |
|---------|------|
| Triumph Manipulator Landing | [`../triumph-manipulator-landing/README.md`](../triumph-manipulator-landing/README.md) — MARS project documentation + [`../../workspaces/triumph-manipulator-landing/`](../../workspaces/triumph-manipulator-landing/) local frontend workspace placeholder |

**Triumph filesystem map (active V2 workspace vs V1, design vs implementation, shared icons):** [`../triumph-manipulator-landing/V2-CANONICAL-STATE.md`](../triumph-manipulator-landing/V2-CANONICAL-STATE.md).

**Operational map (short):** [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) — canonical entry points by concern; **not** a duplicate of the full index below.

## Pack index

| Document | Purpose |
|----------|---------|
| [system-overview.md](system-overview.md) | Vision, boundaries, relation to MARS core |
| [layer-map.md](layer-map.md) | Seven target layers, agents, artifacts, gates, risks |
| [agent-map.md](agent-map.md) | Planned agent roles (registry alignment) |
| [registries.md](registries.md) | Planned knowledge modules; **delivered v0:** [site-type-registry-v0.md](site-type-registry-v0.md), [block-registry-v0.md](block-registry-v0.md) |
| [site-type-registry-v0.md](site-type-registry-v0.md) | **Site Type Registry v0** — classification layer for strategy, SEO, UX, blocks, frontend, QA |
| [block-registry-v0.md](block-registry-v0.md) | **Block Registry v0** — section semantics, compatibility with site types, orchestration-facing fields (documentation only) |
| [page-blueprint-contract-v0.md](page-blueprint-contract-v0.md) | **Page Blueprint Contract v0** — normalized page orchestration fields (strategy → SEO → UX → design → frontend → QA) |
| [design-handoff-contract-v0.md](design-handoff-contract-v0.md) | **Design Handoff Contract v0** — blueprint → visual production requirements (design layer); no automated Figma claim |
| [frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md) | **Frontend Handoff Contract v0** — blueprint/design → static frontend production requirements (Gulp-oriented) |
| [page-blueprint-qa-checklist-v0.md](page-blueprint-qa-checklist-v0.md) | **Page Blueprint QA Checklist v0** — blueprint-level validation categories and escalation |
| [website-factory-workflow-v0.md](website-factory-workflow-v0.md) | **Website Factory Workflow v0** — canonical orchestration stages, artifact flow, QA/HITL escalation (**documentation only**) |
| [first-operational-runbook-v0.md](first-operational-runbook-v0.md) | **First Operational Runbook v0** — human-driven execution hub; **not** runtime, **not** automation ([reference-run-sequence-v0.md](reference-run-sequence-v0.md), [operator-lane-model-v0.md](operator-lane-model-v0.md), [human-supervision-model-v0.md](human-supervision-model-v0.md), [project-execution-checkpoints-v0.md](project-execution-checkpoints-v0.md), [reference-run-artifact-flow-v0.md](reference-run-artifact-flow-v0.md), [reference-run-failure-recovery-v0.md](reference-run-failure-recovery-v0.md), [reference-run-reporting-v0.md](reference-run-reporting-v0.md)) |
| [operational-template-overview-v0.md](operational-template-overview-v0.md) | **Operational Templates Layer v0 — overview** — reusable Markdown shells for project types, reviews, delivery gates, and operator sessions; index of `*-template-v0.md`; **not** runtime automation, **not** executable workflows, **not** orchestration daemons |
| [reference-cases/triumph-manipulator-landing/reference-case-overview-v0.md](reference-cases/triumph-manipulator-landing/reference-case-overview-v0.md) | **Reference Execution Case #1 — Triumph Manipulator Landing (v0)** — end-to-end **documentation-first** simulated run (intake → delivery readiness); **not** a built website, **not** runtime orchestration |
| [artifact-architecture-overview-v0.md](artifact-architecture-overview-v0.md) | **Artifact Architecture Layer v0** — workflow vs artifact vs payload vs contract; orchestration/HITL/Validator alignment (**conceptual only**) |
| [artifact-types-v0.md](artifact-types-v0.md) | **Artifact types v0** — lifecycle, mutability, HITL, QA ties per artifact class |
| [page-objective-model-v0.md](page-objective-model-v0.md), [cta-semantics-v0.md](cta-semantics-v0.md), [trust-semantics-v0.md](trust-semantics-v0.md) | **Page objective, CTA, trust** — normalized semantics (no performance guarantees) |
| [section-payload-model-v0.md](section-payload-model-v0.md) | **Section payload model v0** — per-section semantic fields (not implementation JSON) |
| [seo-intent-model-v0.md](seo-intent-model-v0.md), [conversion-intent-model-v0.md](conversion-intent-model-v0.md) | **SEO / conversion intent** — intent dimensions and escalation triggers |
| [frontend-artifact-model-v0.md](frontend-artifact-model-v0.md) | **Frontend artifact model v0** — static build artifacts vs handoff/production docs |
| [qa-result-payloads-v0.md](qa-result-payloads-v0.md) | **QA result payloads v0** — conceptual QA output fields and Validator relationship |
| [prompt-standards-overview-v0.md](prompt-standards-overview-v0.md) | **Prompt Standards Layer v0 — overview** (operational discipline; **not** a prompt engine) |
| [prompt-structure-standard-v0.md](prompt-structure-standard-v0.md) | **Prompt structure standard v0** — normalized sections, prompt variants (minimal / production / HITL / QA / frontend) |
| [agent-prompt-behavior-v0.md](agent-prompt-behavior-v0.md) | **Agent prompt behavior v0** — behavioral rules (no fabrication, escalation, artifact-first) |
| [cursor-execution-standard-v0.md](cursor-execution-standard-v0.md) | **Cursor execution standard v0** — prompt → execute → report loop, git safety, target folder / agent mode |
| [reporting-standard-v0.md](reporting-standard-v0.md) | **Reporting standard v0** — REPORT format and lane variants (doc / frontend / QA / migration / validation) |
| [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md) | **HITL prompt boundary v0** — mandatory gates, escalation triggers, “no fake autonomous approval” |
| [safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md) | **SAFE UNKNOWN prompt rules v0** — assumption discipline, fabrication forbidden, GOOD vs BAD examples |
| [artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md) | **Artifact transfer prompt rules v0** — immutability, approval inheritance, revisions, QA inheritance |
| [qa-prompt-rules-v0.md](qa-prompt-rules-v0.md) | **QA prompt rules v0** — evidence-based QA, no fake approvals, blocker / waiver, Validator relationship |
| [frontend-prompt-discipline-v0.md](frontend-prompt-discipline-v0.md) | **Frontend prompt discipline v0** — Gulp-oriented source-first rules, SCSS modularity, data-* JS, no `dist/` edits |
| [execution-semantics-overview-v0.md](execution-semantics-overview-v0.md) | **Execution Semantics Layer v0 — overview** — operational methodology for stage / artifact / approval / QA / delivery lifecycle; **not** a scheduler / queue / runtime |
| [stage-state-model-v0.md](stage-state-model-v0.md) | **Stage state model v0** — conceptual states, transitions, ownership, freeze / reopen / invalidation |
| [artifact-state-model-v0.md](artifact-state-model-v0.md) | **Artifact state model v0** — lifecycle, mutable/immutable regions, lineage, replacement philosophy, approval inheritance |
| [approval-semantics-v0.md](approval-semantics-v0.md) | **Approval semantics v0** — scope, partial / conditional / inheritance / expiration / revocation; HITL-anchored |
| [revision-semantics-v0.md](revision-semantics-v0.md) | **Revision semantics v0** — scope, lineage, ownership, impact, freeze breaking, QA reset, history |
| [regeneration-semantics-v0.md](regeneration-semantics-v0.md) | **Regeneration semantics v0** — partial / full / safe / unsafe; boundaries; triggers; dependency-aware; HITL-anchored |
| [dependency-invalidation-v0.md](dependency-invalidation-v0.md) | **Dependency invalidation v0** — upstream/downstream propagation across blueprint / design / SEO / frontend; partial rerun |
| [orchestration-signals-v0.md](orchestration-signals-v0.md) | **Orchestration signals v0** — signal source, propagation, escalation, resolution, lifecycle; tied to system signals dictionary |
| [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md) | **QA gating semantics v0** — gate lifecycle, blocker / pass / fail / conditional / waiver, freeze, delivery blocking, HITL override |
| [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md) | **Delivery lifecycle v0** — candidate, pre-delivery validation, release approval, export package, handoff, rollback, archive, post-delivery revision |
| [reference-project-model-v0.md](reference-project-model-v0.md) | **Reference Project Layer v0 — model** — reference / production / sandbox / migration / demo; conceptual fields; **SAFE UNKNOWN** for storage and engines |
| [reference-project-artifact-tree-v0.md](reference-project-artifact-tree-v0.md) | **Reference Project Layer v0 — artifact tree** — Intake→Delivery lineage, inheritance, freeze, supersede vs revision, per-stage upstream/downstream/QA/HITL |
| [reference-project-lifecycle-v0.md](reference-project-lifecycle-v0.md) | **Reference Project Layer v0 — lifecycle** — project states, entry/exit, blocking, invalidation, QA, HITL (**documentation only**, not a state engine) |
| [reference-project-hitl-governance-v0.md](reference-project-hitl-governance-v0.md) | **Reference Project Layer v0 — HITL governance** — approval / rejection / freeze / reopen / waiver / escalation; forbids self-approval and fake delivery acceptance |
| [reference-project-qa-matrix-v0.md](reference-project-qa-matrix-v0.md) | **Reference Project Layer v0 — QA matrix** — stage × required/blocking/optional/HITL QA; waivers, inheritance, invalidation resets |
| [reference-delivery-package-v0.md](reference-delivery-package-v0.md) | **Reference Project Layer v0 — delivery packages** — blueprint/design/frontend/QA/export/RC/delivery candidate semantics |
| [multi-page-orchestration-v0.md](multi-page-orchestration-v0.md) | **Reference Project Layer v0 — multi-page orchestration** — site graph, clusters, internal linking, cannibalization, page vs site QA (**no automation claims**) |
| [semantic-relationship-overview-v0.md](semantic-relationship-overview-v0.md) | **Semantic Relationship Layer v0 — overview** — semantic object, relationship, inheritance, propagation, invalidation, authority, freeze, drift, consistency (**documentation only** — **not** a graph database, **not** a vector engine, **not** a runtime / orchestration semantic engine, **not** autonomous reasoning) |
| [semantic-object-model-v0.md](semantic-object-model-v0.md) | **Semantic Relationship Layer v0 — object model** — canonical semantic objects (`cta_object`, `trust_object`, `seo_intent`, `conversion_goal`, `offer_object`, `geo_object`, `service_entity`, `faq_entity`, `proof_entity`, `navigation_entity`), ownership, lineage, supersede, drift |
| [cross-artifact-semantics-v0.md](cross-artifact-semantics-v0.md) | **Semantic Relationship Layer v0 — cross-artifact** — Blueprint, Design, Frontend, QA, Delivery; mismatch, drift, downgrade, freeze break |
| [semantic-dependency-rules-v0.md](semantic-dependency-rules-v0.md) | **Semantic Relationship Layer v0 — dependency rules** — hard/soft/semantic/visual/trust/SEO/nav/cluster dependencies; severity; partial rerun; **SAFE UNKNOWN** |
| [semantic-inheritance-v0.md](semantic-inheritance-v0.md) | **Semantic Relationship Layer v0 — inheritance** — site → cluster → page → section → component; overrides; **inheritance ≠ runtime propagation** |
| [semantic-consistency-rules-v0.md](semantic-consistency-rules-v0.md) | **Semantic Relationship Layer v0 — consistency** — CTA/trust/SEO/nav/offer/geo + design/frontend/QA consistency; severity; escalation; delivery blocking |
| [site-semantic-graph-v0.md](site-semantic-graph-v0.md) | **Semantic Relationship Layer v0 — site semantic graph (conceptual)** — page relations, authority flows, GEO trees, clusters, SEO neighborhoods; **not** a graph store |
| [semantic-freeze-semantics-v0.md](semantic-freeze-semantics-v0.md) | **Semantic Relationship Layer v0 — freeze** — frozen objects, approvals, inherited freezes, reopen, supersede, rollback, delivery/QA/HITL implications |
| [semantic-qa-rules-v0.md](semantic-qa-rules-v0.md) | **Semantic Relationship Layer v0 — semantic QA** — scope, finding classes, evidence, severity, blocking, waivers, **SAFE UNKNOWN** |
| [artifact-bus-overview-v0.md](artifact-bus-overview-v0.md) | **Artifact Bus Layer v0 — overview** — transfer, publish, consume, route, lineage, authority, freeze, invalidation, stale/orphan (**documentation only** — **not** a queue, **not** an event bus, **not** runtime transport) |
| [artifact-envelope-model-v0.md](artifact-envelope-model-v0.md) | **Artifact Bus Layer v0 — envelope model** — normalized fields, immutable/mutable regions, supersede, stale/orphan envelopes |
| [artifact-routing-rules-v0.md](artifact-routing-rules-v0.md) | **Artifact Bus Layer v0 — routing rules** — allowed/forbidden/partial/revision/rollback/invalidation/QA/delivery routes; authority; freeze |
| [artifact-transfer-semantics-v0.md](artifact-transfer-semantics-v0.md) | **Artifact Bus Layer v0 — transfer semantics** — inheritance, invalidation, downgrade, freeze break, partial transfer |
| [artifact-lineage-semantics-v0.md](artifact-lineage-semantics-v0.md) | **Artifact Bus Layer v0 — lineage semantics** — parent/child/sibling/supersede/rollback/branch/frozen lineage; drift; invalidation; orphaning |
| [artifact-publication-semantics-v0.md](artifact-publication-semantics-v0.md) | **Artifact Bus Layer v0 — publication semantics** — draft/review/approved/frozen/revoked/deprecated/archived; authority; visibility |
| [artifact-consumption-rules-v0.md](artifact-consumption-rules-v0.md) | **Artifact Bus Layer v0 — consumption rules** — consume/reject/invalidate/reopen/partial; stale/orphan/invalid consumption |
| [artifact-governance-rules-v0.md](artifact-governance-rules-v0.md) | **Artifact Bus Layer v0 — governance rules** — immutability, revision/rollback/freeze/delivery governance; forbids silent replacement / hidden revision / fake approval inheritance / hidden invalidation |
| [delivery-bus-semantics-v0.md](delivery-bus-semantics-v0.md) | **Artifact Bus Layer v0 — delivery bus semantics** — release/delivery candidate, export/QA packages, freeze, invalidation, rollback, post-delivery revision; authorities (**not** CI/CD automation) |
| [artifact-transfer-qa-rules-v0.md](artifact-transfer-qa-rules-v0.md) | **Artifact Bus Layer v0 — transfer QA rules** — stale/orphan route, lineage, approval/freeze/semantic/delivery mismatch; severity; blocking; waivers; **SAFE UNKNOWN** |
| [validation-runtime-overview-v0.md](validation-runtime-overview-v0.md) | **Validation Runtime Model v0** — validation semantics, methodology, lifecycle tokens, evidence/result/failure/waiver/escalation/consistency vocabulary, honesty boundary; linked [validation-lifecycle-v0.md](validation-lifecycle-v0.md), [validator-execution-model-v0.md](validator-execution-model-v0.md), [validation-evidence-model-v0.md](validation-evidence-model-v0.md), [validation-result-semantics-v0.md](validation-result-semantics-v0.md), [validation-failure-semantics-v0.md](validation-failure-semantics-v0.md), [validation-waiver-semantics-v0.md](validation-waiver-semantics-v0.md), [validation-escalation-model-v0.md](validation-escalation-model-v0.md), [validation-consistency-model-v0.md](validation-consistency-model-v0.md), [validation-runtime-boundary-v0.md](validation-runtime-boundary-v0.md); **documentation only** — **not** a validator engine, **not** CI/background validation, **not** Lighthouse/crawl automation, **not** autonomous enforcement |
| [workflow-map.md](workflow-map.md) | End-to-end flow, HITL, Cursor vs future runtime |
| [layer-map.md](layer-map.md) §8 | **Artifact Bus Layer v0** — cross-cutting placement (bus = documentation semantics, **not** runtime transport) |
| [qa-validation-model.md](qa-validation-model.md) | QA lanes and Validator integration |
| [frontend-production-model.md](frontend-production-model.md) | Gulp-oriented production model (legacy-aligned) |
| [design-layer-model.md](design-layer-model.md) | Design artifacts and agent boundaries |
| [seo-marketing-layer.md](seo-marketing-layer.md) | SEO/marketing strategy and QA |
| [roadmap.md](roadmap.md) | Phased evolution (0–7) |
| [system-integration-check-v1.md](system-integration-check-v1.md) | **System integration check v1** — cross-layer audit, drift/contradiction log, minimal fixes record |
| [migration-strategy.md](migration-strategy.md) | How this pack relates to legacy Web-GPT ideas and other projects |
| [implementation-phase-1.md](implementation-phase-1.md) | First doc-only deliverables |
| [safe-unknown-boundary.md](safe-unknown-boundary.md) | Honesty boundary — no false implementation claims |

## Registry

Authoritative project row: [`../../registry/project-registry.md`](../../registry/project-registry.md).

**Agent identities:** stable planned **`agent_id`** rows in [`../../agents/registry.md`](../../agents/registry.md) §4.1; **v0 agent cards** for all listed factory roles in [`../../agents/cards/`](../../agents/cards/) (documentation-only, **not** runtime). **SoT** for extended per-role prose remains **[`agent-map.md`](agent-map.md)**. Factory **`entity_id`** rows: [`../../governance/dependency-map.md`](../../governance/dependency-map.md) §4 (`mars_website_factory`, `website_factory_*`, `website_factory_workflow_v0`, `website_factory_semantic_relationship_layer_v0`, `website_factory_artifact_bus_layer_v0`).

## Related MARS artifacts (existing)

- Agent catalog: [`../../agents/registry.md`](../../agents/registry.md) — **Gulp Frontend Agent**, **Validator Agent** (documented as **legacy-bridge** / **planned**).
- Execution flow: [`../../workflows/execution-flow.md`](../../workflows/execution-flow.md).
- Legacy Gulp profile (imported): [`../../web-gpt-sources/04_agents.md`](../../web-gpt-sources/04_agents.md) (embedded gulp-frontend-agent section).
- Capability / web tasks (imported core draft): [`../../web-gpt-sources/03_core.md`](../../web-gpt-sources/03_core.md) — Page generation, frontend coding rows.

---

*Last updated: 2026-05-13 — **Operational Templates Layer v0** ([operational-template-overview-v0.md](operational-template-overview-v0.md) + linked `*-template-v0.md`): reusable documentation shells aligned with workflow, artifact bus, execution semantics, validation model, and reference case #1; **not** automation or runtime generation. **Reference Execution Case #1** ([reference-cases/triumph-manipulator-landing/reference-case-overview-v0.md](reference-cases/triumph-manipulator-landing/reference-case-overview-v0.md)): Triumph Manipulator Landing — full artifact chain (intake → validation → REPORT); **not** production build. **First Operational Runbook v0** ([first-operational-runbook-v0.md](first-operational-runbook-v0.md)): human-supervised reference execution (R01–R15, checkpoints, lanes, reporting); **not** runtime, **not** automation, **not** hidden orchestration. **System integration check v1** ([system-integration-check-v1.md](system-integration-check-v1.md)): cross-layer consistency audit; roadmap / implementation-phase-1 phase-numbering clarification; execution-model link in roadmap Phase 5. **Validation Runtime Model v0** ([validation-runtime-overview-v0.md](validation-runtime-overview-v0.md) + linked validation docs): validation semantics, lifecycle, evidence, results, honesty boundary — **documentation only** (**not** validator engine, **not** CI/background workers). **Artifact Bus Layer v0** doc hardening: [artifact-bus-overview-v0.md](artifact-bus-overview-v0.md) (**artifact state propagation**), [artifact-routing-rules-v0.md](artifact-routing-rules-v0.md) (**Frontend QA fail → invalidates Delivery Candidate** shorthand), [layer-map.md](layer-map.md) §8, [artifact-governance-rules-v0.md](artifact-governance-rules-v0.md) (AGENTS link). Bus layer remains **documentation only** — **not** a queue, **not** an event bus, **not** runtime transport. Earlier 2026-05-12 notes: Semantic Relationship Layer v0, Reference Project Layer v0; 2026-05-11: Execution Semantics, Prompt Standards, Artifact Architecture, workflow v0, agent cards, registries — all documentation only.*
