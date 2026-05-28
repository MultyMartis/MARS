# Website Factory — operational index (stabilization)

**Purpose:** One short map so operators and agents can find **canonical** docs without treating every `*-v0.md` as equally “entry level.” **Not** a full inventory (see [README.md](README.md) Pack index for the wide table).

**Wave 1 normalization (2026-05-20):** Prefer **[frontend-operator-quickstart-v1.md](frontend-operator-quickstart-v1.md)** for onboarding; **[wave1-operational-entity-map-v1.md](wave1-operational-entity-map-v1.md)** · **[wave1-operational-topology-v1.md](wave1-operational-topology-v1.md)** · **[section-replacement-contract-v1.md](section-replacement-contract-v1.md)** · **[frontend-foundation-blueprint-v1.md](frontend-foundation-blueprint-v1.md)**; Forge modes — **[forge-operational-modes-v1.md](../../agents/mars-forge/forge-operational-modes-v1.md)** (Lite default).

**Wave 2 foundation systems (2026-05-20):** Implementation standards — **[foundation-systems/README.md](foundation-systems/README.md)** (tokens, responsive, forms, modals, JS lifecycle, motion, conversion blocks). **Not** default governance reading.

**Wave 3 reference implementation (2026-05-20):** Real `src/` — **[workspaces/website-factory-reference-v1/](../../workspaces/website-factory-reference-v1/)** · [golden-implementation-slice-v1.md](golden-implementation-slice-v1.md) · Forge [foundation-lite-checklist.md](../../agents/mars-forge/foundation-lite-checklist.md).

**Wave 4 production acceleration (2026-05-21):** Adoption + blocks + onboarding — **[onboarding-flow-v1.md](onboarding-flow-v1.md)** · **[foundation-adoption-charter-v1.md](foundation-adoption-charter-v1.md)** · **[foundation-adoption-rules-v1.md](foundation-adoption-rules-v1.md)** · **[operational-examples/golden-report-examples-v1.md](operational-examples/golden-report-examples-v1.md)** · **[section-swap-demo-flow-v1.md](section-swap-demo-flow-v1.md)** · **[reference-workspace-qa-flow-v1.md](reference-workspace-qa-flow-v1.md)** · **[implementation-extraction-discipline-v1.md](implementation-extraction-discipline-v1.md)**. Reference blocks: `pricing`, `social_proof`, `sticky_cta`, `contact_block`.

**Wave 5 production hardening (2026-05-21):** Adoption + extraction + QA consolidation — **[workspaces/_template-client-v1/](../../workspaces/_template-client-v1/)** · **[operational-qa-entry-v1.md](operational-qa-entry-v1.md)** · **[adoption-validation-flow-v1.md](adoption-validation-flow-v1.md)** · **[visual-regression-workflow-v1.md](visual-regression-workflow-v1.md)** · **[production-hardening-rules-v1.md](production-hardening-rules-v1.md)** · **[legacy-migration-path-v1.md](legacy-migration-path-v1.md)** · **[operational-examples/wave5-extraction-report-faq-v1.md](operational-examples/wave5-extraction-report-faq-v1.md)**. Reference block added: `faq` (real extract from Triumph V2).

**Wave 6 production consolidation (2026-05-21):** Controlled reuse — **[operational-consolidation-map-v1.md](operational-consolidation-map-v1.md)** · **[curated-library-index-v1.md](curated-library-index-v1.md)** · **[block-quality-tiers-v1.md](block-quality-tiers-v1.md)** · **[freeze-discipline-v1.md](freeze-discipline-v1.md)** · **[registry-sync-discipline-v1.md](registry-sync-discipline-v1.md)** · **[pilot-adoption-flow-v1.md](pilot-adoption-flow-v1.md)** · extractions [pricing](operational-examples/wave6-extraction-report-pricing-v1.md) · [cases](operational-examples/wave6-extraction-report-cases-v1.md). Reference: `pricing` re-extracted (commercial cards); `cases` added.

**Session routing (Tier 0–3):** [survivability-canonical-entrypoint-model-v0.md](../../governance/survivability-canonical-entrypoint-model-v0.md) — **Tier 2** live navigation for Factory; open **Core Run** first; **Extended** only when the task needs a governance triad.

| Tier | Use when |
|------|----------|
| **0** | New to repo — [README.md](../../README.md), [AGENTS.md](../../AGENTS.md) |
| **1** | Ecosystem / reality question — one router from governance (topology or reality index) |
| **2** | **This file** — one **Core Run** row per session; pack identity in [README.md](README.md) |
| **3** | Individual `*-governance.md`, drift taxonomies, Forge specialist checklists — on demand |

---

## Canonical entry

- **[operational-consolidation-map-v1.md](operational-consolidation-map-v1.md)** — **Wave 6 single routing layer** (blocks, extraction, QA, freeze, pilot).
- **[onboarding-flow-v1.md](onboarding-flow-v1.md)** — **Wave 4–5 ordered path** (new operator / workspace / task).
- **[operational-qa-entry-v1.md](operational-qa-entry-v1.md)** — **Wave 5 single QA surface** (default after build). **RU commercial:** [ru-landing-qa-preset-v1.md](ru-landing-qa-preset-v1.md). **Anti-drift invariants:** [frontend-production-invariants-v1.md](frontend-production-invariants-v1.md).
- **[frontend-operator-quickstart-v1.md](frontend-operator-quickstart-v1.md)** — frontend SoT, workspace, Forge Lite, forbidden paths.
- **[README.md](README.md)** — pack identity, honesty boundary, **Pack index** (full list; search / archival — not default session read).

---

## Core Run (default session)

Open **one row** below unless the task explicitly needs Extended governance.

| Concern | Where to start |
|---------|----------------|
| **Architecture / layers** | [system-overview.md](system-overview.md), [layer-map.md](layer-map.md) |
| **Workflow / human run** | [first-operational-runbook-v0.md](first-operational-runbook-v0.md) → [website-factory-workflow-v0.md](website-factory-workflow-v0.md), [workflow-map.md](workflow-map.md) |
| **Design → implementation law** | [design-governance-layer.md](design-governance-layer.md), [canonical-implementation-pack-architecture.md](canonical-implementation-pack-architecture.md) |
| **Frontend & Forge** | **See [Frontend & Forge](#frontend--forge-canonical-once)** — Gulp foundation + Forge overlay + factory contracts |
| **Triumph Manipulator (active client)** | [`projects/triumph-manipulator-landing/TRIUMPH-V6-CURRENT-FRONTEND-RULES.md`](../triumph-manipulator-landing/TRIUMPH-V6-CURRENT-FRONTEND-RULES.md) · workspace `workspaces/triumph-manipulator-landing-v6/` · rollout [`V6-PAGE-ROLLOUT-PLAN.md`](../triumph-manipulator-landing/V6-PAGE-ROLLOUT-PLAN.md) |
| **Foundation systems (Wave 2)** | [foundation-systems/README.md](foundation-systems/README.md) — tokens → conversion blocks; use when implementing shared SCSS/JS |
| **Reference workspace (Wave 3–6)** | [workspaces/website-factory-reference-v1/](../../workspaces/website-factory-reference-v1/) — foundations + 9 blocks; [golden-implementation-slice-v1.md](golden-implementation-slice-v1.md); library [curated-library-index-v1.md](curated-library-index-v1.md) |
| **Wave 4–6 adoption, QA, freeze** | [_template-client-v1](../../workspaces/_template-client-v1/) · [pilot-adoption-flow-v1.md](pilot-adoption-flow-v1.md) · [freeze-discipline-v1.md](freeze-discipline-v1.md) · [operational-qa-entry-v1.md](operational-qa-entry-v1.md) · [adoption-validation-flow-v1.md](adoption-validation-flow-v1.md) · [registry-sync-discipline-v1.md](registry-sync-discipline-v1.md) |
| **Semantics / artifacts / QA payloads** | [artifact-architecture-overview-v0.md](artifact-architecture-overview-v0.md), [execution-semantics-overview-v0.md](execution-semantics-overview-v0.md), [page-blueprint-qa-checklist-v0.md](page-blueprint-qa-checklist-v0.md) |
| **Reporting & Cursor discipline** | [reporting-standard-v0.md](reporting-standard-v0.md), [cursor-execution-standard-v0.md](cursor-execution-standard-v0.md) |
| **Runtime assumptions (honesty)** | [safe-unknown-boundary.md](safe-unknown-boundary.md); repo-wide **Phase 1** — [execution-model.md](../../governance/execution-model.md), [AGENTS.md](../../AGENTS.md) — **no** in-pack execution engine |
| **Governance / registry** | [registry/project-registry.md](../../registry/project-registry.md) (`mars-website-factory`), [agents/registry.md](../../agents/registry.md) §4.1, [agent-input-contracts.md](../../governance/agent-input-contracts.md) |

---

## Frontend & Forge (canonical once)

**Canonical relationship (do not re-derive from scattered READMEs):** [frontend-legacy-and-foundation-map-v0.md](../../governance/frontend-legacy-and-foundation-map-v0.md) — **`gulp_frontend_agent`** = foundation SoT; **MARS Forge** = **thin overlay only**, **not** parallel SoT. If Forge is silent, **foundation wins**.

| Layer | Start here |
|-------|------------|
| **Gulp foundation** | [agents/frontend-gulp-agent/README.md](../../agents/frontend-gulp-agent/README.md) → [workflow.md](../../agents/frontend-gulp-agent/workflow.md) |
| **Factory contracts** | [frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md), [frontend-production-model.md](frontend-production-model.md), [frontend-production-rules-v0.md](frontend-production-rules-v0.md), [frontend-production-invariants-v1.md](frontend-production-invariants-v1.md), [frontend-prompt-discipline-v0.md](frontend-prompt-discipline-v0.md) |
| **Forge overlay** | [forge-operational-modes-v1.md](../../agents/mars-forge/forge-operational-modes-v1.md) (**Lite default**) → [AGENT.md](../../agents/mars-forge/AGENT.md), [workflow.md](../../agents/mars-forge/workflow.md), [qa-checklist.md](../../agents/mars-forge/qa-checklist.md) |

**Extended frontend governance** (source interpretation, tokens, cadence, responsive, visual/composition): [Extended reference](#extended--deep-reference) below — Forge specialist checklists are indexed in [agents/mars-forge/README.md](../../agents/mars-forge/README.md), not duplicated here.

---

## Extended / deep reference

**Not default reading** — Extended rows are **Tier 3** semantics. If you opened Extended without a Core Run row or contract citation, **stop** and return to [Core Run](#core-run-default-session).

**Forge checklists:** full overlay index — [agents/mars-forge/README.md](../../agents/mars-forge/README.md). **Design-governance agent role:** [agents/design-governance-agent.md](../../agents/design-governance-agent.md).

Open a **domain row** only when Core Run or a contract citation requires it.

### Semantics, source & design implementation

| Domain | Factory docs |
|--------|----------------|
| **Source interpretation** | [source-interpretation-governance.md](source-interpretation-governance.md), [source-confidence-model.md](source-confidence-model.md), [source-ambiguity-taxonomy.md](source-ambiguity-taxonomy.md) |
| **Design system intent** | [design-system-intent-governance.md](design-system-intent-governance.md), [ui-weight-distribution-model.md](ui-weight-distribution-model.md), [cta-philosophy-governance.md](cta-philosophy-governance.md) |
| **Design token intelligence** | [design-token-intelligence-governance.md](design-token-intelligence-governance.md), [token-semantic-layer-model.md](token-semantic-layer-model.md), [token-drift-taxonomy.md](token-drift-taxonomy.md) |
| **Implementation reliability** | [implementation-reliability-governance.md](implementation-reliability-governance.md), [frontend-stability-model.md](frontend-stability-model.md), [implementation-drift-taxonomy.md](implementation-drift-taxonomy.md), [frontend-production-invariants-v1.md](frontend-production-invariants-v1.md) |
| **Visual intent (human read)** | [visual-reconciliation-layer.md](visual-reconciliation-layer.md), [visual-drift-taxonomy.md](visual-drift-taxonomy.md) |
| **Cadence / rhythm** | [canonical-vertical-cadence-system.md](canonical-vertical-cadence-system.md), [cadence-tier-model.md](cadence-tier-model.md), [typography-rhythm-governance.md](typography-rhythm-governance.md), [russian-no-word-splitting-typography-v1.md](russian-no-word-splitting-typography-v1.md), [ru-landing-qa-preset-v1.md](ru-landing-qa-preset-v1.md), [vertical-rhythm-governance.md](vertical-rhythm-governance.md) |
| **Responsive intent** | [responsive-intent-governance.md](responsive-intent-governance.md), [mobile-composition-preservation.md](mobile-composition-preservation.md), [responsive-collapse-taxonomy.md](responsive-collapse-taxonomy.md) |
| **Icon semantics / FA** | [font-awesome-governance-layer.md](font-awesome-governance-layer.md) |
| **Composition vs DOM** | [compositional-structure-awareness.md](compositional-structure-awareness.md), [composition-drift-taxonomy.md](composition-drift-taxonomy.md) |

### Strategic intent, reconstruction & initialization

| Domain | Factory docs |
|--------|----------------|
| **Strategic / business continuity** | [strategic-intent-governance.md](strategic-intent-governance.md), [business-intent-continuity-model.md](business-intent-continuity-model.md), [strategic-drift-taxonomy.md](strategic-drift-taxonomy.md) |
| **Design intent transfer / fidelity** | [design-intent-transfer-governance.md](design-intent-transfer-governance.md), [reconstruction-fidelity-model.md](reconstruction-fidelity-model.md), [reconstruction-drift-taxonomy.md](reconstruction-drift-taxonomy.md) |
| **Initialization / workspace reset** | [initialization-governance.md](initialization-governance.md), [workspace-reset-governance.md](workspace-reset-governance.md), [reconstruction-bootstrap-governance.md](reconstruction-bootstrap-governance.md), [reconstruction-asset-lifecycle-governance.md](reconstruction-asset-lifecycle-governance.md) |

### Layout, commercial visual & page continuity

| Domain | Factory docs |
|--------|----------------|
| **Layout shell / first-screen** | [layout-shell-governance.md](layout-shell-governance.md), [first-screen-decomposition-model.md](first-screen-decomposition-model.md), [background-ownership-governance.md](background-ownership-governance.md) — **HEADER != HERO** |
| **Commercial / atmosphere / section language** | [commercial-density-governance.md](commercial-density-governance.md), [commercial-landing-pressure-model.md](commercial-landing-pressure-model.md), [atmosphere-continuity-governance.md](atmosphere-continuity-governance.md), [section-language-governance.md](section-language-governance.md), [beautification-drift-governance.md](beautification-drift-governance.md) |
| **Rhythm / footer / iconography / overlay** | [full-page-cadence-continuity-governance.md](full-page-cadence-continuity-governance.md), [contextual-footer-governance.md](contextual-footer-governance.md), [semantic-iconography-governance.md](semantic-iconography-governance.md), [overlay-focal-balance-governance.md](overlay-focal-balance-governance.md) |

*Forge QA integration for layout/commercial/rhythm/terminal findings: [agents/mars-forge/qa-checklist.md](../../agents/mars-forge/qa-checklist.md).*

### Interaction, accessibility, QA & agents

| Domain | Factory docs |
|--------|----------------|
| **Interaction / motion** | [interaction-intent-governance.md](interaction-intent-governance.md), [interaction-behavior-taxonomy.md](interaction-behavior-taxonomy.md), [motion-restraint-model.md](motion-restraint-model.md) |
| **UI state / behavioral consistency** | [state-behavioral-consistency-governance.md](state-behavioral-consistency-governance.md), [ui-state-taxonomy.md](ui-state-taxonomy.md), [interaction-state-integrity-model.md](interaction-state-integrity-model.md) |
| **Accessibility intent** | [accessibility-intent-governance.md](accessibility-intent-governance.md), [operational-accessibility-model.md](operational-accessibility-model.md), [accessibility-drift-taxonomy.md](accessibility-drift-taxonomy.md) |
| **QA confidence** | [qa-confidence-governance.md](qa-confidence-governance.md), [verification-evidence-model.md](verification-evidence-model.md), [qa-drift-taxonomy.md](qa-drift-taxonomy.md) |
| **Human escalation / boundaries** | [human-escalation-governance.md](human-escalation-governance.md), [decision-boundary-model.md](decision-boundary-model.md), [escalation-drift-taxonomy.md](escalation-drift-taxonomy.md) |
| **Multi-agent coordination** | [multi-agent-coordination-governance.md](multi-agent-coordination-governance.md), [agent-responsibility-boundary-model.md](agent-responsibility-boundary-model.md), [multi-agent-drift-taxonomy.md](multi-agent-drift-taxonomy.md) |
| **Content density** | [content-density-governance.md](content-density-governance.md), [information-pressure-model.md](information-pressure-model.md), [content-overload-taxonomy.md](content-overload-taxonomy.md) |

### Operations, survivability & meta-governance

| Domain | Factory docs |
|--------|----------------|
| **Temporal evolution / project drift** | [temporal-evolution-governance.md](temporal-evolution-governance.md), [project-drift-survivability-model.md](project-drift-survivability-model.md), [evolution-drift-taxonomy.md](evolution-drift-taxonomy.md) |
| **Production readiness / delivery** | [production-readiness-governance.md](production-readiness-governance.md), [delivery-survivability-model.md](delivery-survivability-model.md), [production-drift-taxonomy.md](production-drift-taxonomy.md) |
| **Knowledge provenance / lineage** | [knowledge-provenance-governance.md](knowledge-provenance-governance.md), [source-lineage-model.md](source-lineage-model.md), [provenance-drift-taxonomy.md](provenance-drift-taxonomy.md) |
| **Context survivability** | [context-survivability-governance.md](context-survivability-governance.md), [context-compression-integrity-model.md](context-compression-integrity-model.md), [context-drift-taxonomy.md](context-drift-taxonomy.md) |
| **Failure recovery / resilience** | [failure-recovery-governance.md](failure-recovery-governance.md), [operational-resilience-model.md](operational-resilience-model.md), [recovery-drift-taxonomy.md](recovery-drift-taxonomy.md) |
| **Cross-project transfer** | [cross-project-transfer-governance.md](cross-project-transfer-governance.md), [knowledge-transfer-compatibility-model.md](knowledge-transfer-compatibility-model.md), [transfer-drift-taxonomy.md](transfer-drift-taxonomy.md) |
| **Organizational memory** | [organizational-memory-governance.md](organizational-memory-governance.md), [institutional-knowledge-model.md](institutional-knowledge-model.md), [knowledge-memory-drift-taxonomy.md](knowledge-memory-drift-taxonomy.md) |
| **Governance minimalism / complexity** | [governance-minimalism.md](governance-minimalism.md), [complexity-control-model.md](complexity-control-model.md), [governance-bloat-taxonomy.md](governance-bloat-taxonomy.md) |
| **Prioritization / risk weighting** | [governance-prioritization.md](governance-prioritization.md), [risk-weighting-model.md](risk-weighting-model.md), [prioritization-drift-taxonomy.md](prioritization-drift-taxonomy.md) |
| **Adaptive / context-sensitive discipline** | [adaptive-governance.md](adaptive-governance.md), [context-sensitive-discipline-model.md](context-sensitive-discipline-model.md), [adaptive-drift-taxonomy.md](adaptive-drift-taxonomy.md) |
| **Governance economics / cost** | [governance-economics.md](governance-economics.md), [operational-cost-awareness-model.md](operational-cost-awareness-model.md), [governance-cost-drift-taxonomy.md](governance-cost-drift-taxonomy.md) |
| **Cognitive load / review ergonomics** | [cognitive-load-governance.md](cognitive-load-governance.md), [review-ergonomics-model.md](review-ergonomics-model.md), [cognitive-drift-taxonomy.md](cognitive-drift-taxonomy.md) |
| **Governance compression / modes** | [governance-compression-governance.md](governance-compression-governance.md), [operational-modes-model.md](operational-modes-model.md), [compression-drift-taxonomy.md](compression-drift-taxonomy.md) |
| **Governance evolution** | [governance-evolution-governance.md](governance-evolution-governance.md), [self-refinement-model.md](self-refinement-model.md), [evolutionary-drift-taxonomy.md](evolutionary-drift-taxonomy.md) |
| **Meta-governance integrity** | [meta-governance-integrity.md](meta-governance-integrity.md), [governance-architecture-model.md](governance-architecture-model.md), [meta-governance-drift-taxonomy.md](meta-governance-drift-taxonomy.md) |
| **Trust calibration** | [trust-calibration-governance.md](trust-calibration-governance.md), [governance-credibility-model.md](governance-credibility-model.md), [trust-drift-taxonomy.md](trust-drift-taxonomy.md) |
| **Decision transparency / reasoning** | [decision-transparency-governance.md](decision-transparency-governance.md), [reasoning-visibility-model.md](reasoning-visibility-model.md), [reasoning-drift-taxonomy.md](reasoning-drift-taxonomy.md) |
| **Operational workflow / execution discipline** | [operational-workflow-governance.md](operational-workflow-governance.md), [execution-discipline-model.md](execution-discipline-model.md), [workflow-drift-taxonomy.md](workflow-drift-taxonomy.md) |
| **Terminal survivability / shell** | [terminal-survivability-governance.md](terminal-survivability-governance.md), [shell-compatibility-model.md](shell-compatibility-model.md), [encoding-drift-taxonomy.md](encoding-drift-taxonomy.md) |

### Integrations & dependency map

| Domain | Where |
|--------|--------|
| **Future WordPress / WPilot** | [../wpilot/metacode-wpilot-plugin-concept.md](../wpilot/metacode-wpilot-plugin-concept.md), [../wpilot/metacode-wpilot-plugin-mvp-roadmap.md](../wpilot/metacode-wpilot-plugin-mvp-roadmap.md) — **planned only**; Factory-native WordPress preferred; legacy builders = compatibility mode |
| **MARS dependency spine** | [dependency-map.md](../../governance/dependency-map.md) §4 |

---

## Reference case (example only)

- [reference-cases/triumph-manipulator-landing/reference-case-overview-v0.md](reference-cases/triumph-manipulator-landing/reference-case-overview-v0.md) — **documentation-first** simulated run; **not** production delivery proof.
- [../triumph-manipulator-landing/V3-BATTLE-TEST-CHARTER.md](../triumph-manipulator-landing/V3-BATTLE-TEST-CHARTER.md) — **V3 Forge battle-test preparation**; full rebuild from V1 source authority, V2 lessons only, documentation-only until implementation is explicitly opened.

---

*Last updated: 2026-05-24 — Triumph V5 incident lessons: [frontend-production-invariants-v1.md](frontend-production-invariants-v1.md) (breakpoints, FAQ, build/dist).*
