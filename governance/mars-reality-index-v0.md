# MARS — Reality index v0

**Status:** **documented** — compact operational visibility layer.  
**Version:** v0 (Structural Stabilization **Phase 2**).  
**Date:** 2026-05-19.  
**Authority:** [AGENTS.md](../AGENTS.md) > registries > this file.

**Tier 1 (reality / bucket routing only)** — use when the question is *what is operational vs conceptual today*; pick **one** Tier 1 router per session with [ecosystem-topology-index.md](ecosystem-topology-index.md) — **do not** read both indexes end-to-end in one session. **Tier model:** [survivability-canonical-entrypoint-model-v0.md](survivability-canonical-entrypoint-model-v0.md).

**Post–Cycle 8:** governance baseline **frozen** (maintenance mode); **operational systems primary** — [mars-operational-evolution-state-after-cycles-1-8-v0.md](mars-operational-evolution-state-after-cycles-1-8-v0.md).

**Is:** instant ecosystem reality orientation (what runs in human workflows **today** vs what is only written).  
**Is not:** roadmap, vision deck, registry engine, or proof of deployed product.

**Buckets:** `operational` · `experimental` · `conceptual` · `external` · `deprecated` · `documentation-only`

Re-verify session facts with `git status` and lane charter — this file is **not** telemetry.

---

## Quick matrix

| Domain | operational | experimental | conceptual | external | deprecated | documentation-only |
|--------|:-----------:|:------------:|:----------:|:--------:|:----------:|:------------------:|
| **Governance** | ✓ discipline | — | ✓ S1–S7 semantics | — | — | ✓ spine (not engine) |
| **Website Factory** | ✓ methodology | — | ✓ layers/bus | — | — | ✓ pack (~258 md) |
| **Forge** | ✓ doc pack | — | — | — | — | ✓ overlay QA |
| **Frontend production** | ✓ gulp lane | — | ✓ handoff law | ✓ real sites | — | ✓ contracts |
| **Runtime research** | — | ✓ R1 JS | ✓ contracts | — | — | ✓ maps |
| **MetaBOT** | ✓ ops docs | R1 adapter | boundaries | ✓ **n8n** | legacy tree | exports |
| **ORCA** | ✓ PPC toolkit | pilots | heuristics | ✓ ad/SERP UI | — | ✓ pack |
| **WPilot** | ✓ admin discipline | — | plugin bridge | ✓ WP/host | — | ✓ Phase 1 MVP |
| **GitGuard** | — | — | ✓ name only | **UNKNOWN** | — | entity-model example |
| **Continuity / IdeaBox** | ✓ capture | — | protocols | — | — | ✓ not `project_id` |
| **Triumph** | ✓ pack + workspace | V3 charter | reference case | hosting TBD | V2 drift refs | ✓ not deployed |

---

## Governance

| Bucket | Reality |
|--------|---------|
| **operational** | Human-maintained `governance/**` in **maintenance mode** (post–Cycle 8 freeze); Phases S1–S7 + reality-audit semantics; [enforcement/](enforcement/README.md) review aids; parallel Cursor lanes; master build map as **doc roadmap**. |
| **conceptual** | Execution contracts, operationalization, experiment framework — **semantics**, not engines. |
| **documentation-only** | Entire governance tree — **control prose**, not runtime enforcement or CI substitute. |
| **deprecated** | — |
| **external** | — |

**Not:** policy engine, autonomous validator, certification product, live ops dashboard.

**SoT:** [README.md](README.md) · [execution-model.md](execution-model.md) · [current-operational-state-v1.md](current-operational-state-v1.md) (deeper tables)

---

## Website Factory

| Bucket | Reality |
|--------|---------|
| **operational** | Human/Cursor methodology: workflow v0, runbook, OPERATIONAL-INDEX, agent cards (roles), HITL, Forge overlay pointers. |
| **conceptual** | Seven-layer story, artifact bus, validation **models**, semantic object vocabulary. |
| **documentation-only** | ~258 markdown files; governance triads; **no** in-pack execution engine. |
| **external** | Production HTML/SCSS in operator workspaces and customer hosting — **outside** pack SoT. |
| **deprecated** | — |

**Not:** autonomous factory, deployment platform, MARS runtime, proof that Triumph output = shipped Factory engine.

**SoT:** [../projects/mars-website-factory/README.md](../projects/mars-website-factory/README.md) · [OPERATIONAL-INDEX.md](../projects/mars-website-factory/OPERATIONAL-INDEX.md) · registry `mars-website-factory` (**planned**)

---

## Forge

| Bucket | Reality |
|--------|---------|
| **operational** | Doc pack `agents/mars-forge/` + card; phased pipeline, freeze, checklists for human QA. |
| **documentation-only** | Design precedent [mars-forge-operational-design-v0.md](mars-forge-operational-design-v0.md) — **historical** where it says “not created”. |
| **conceptual** | — |

**Not:** second Gulp SoT, build bot, pixel-perfect engine (v0), orchestration.

**SoT:** [../agents/mars-forge/README.md](../agents/mars-forge/README.md) · [mars-forge-transition-stabilization-v0.md](mars-forge-transition-stabilization-v0.md)

---

## Frontend production

| Bucket | Reality |
|--------|---------|
| **operational** | `frontend-gulp-agent` pack; Factory frontend contracts; `workspaces/*` as execution locus. |
| **conceptual** | Handoff contract, production rules, production model. |
| **external** | Customer repos, gulp-starter lineage, live builds — not owned by MARS core. |
| **documentation-only** | Consolidation maps under `governance/frontend-*`. |

**Not:** MARS-owned gulp-starter repo; workspace path as governance SoT.

**SoT:** [../agents/frontend-gulp-agent/README.md](../agents/frontend-gulp-agent/README.md) · [frontend-legacy-and-foundation-map-v0.md](frontend-legacy-and-foundation-map-v0.md)

---

## Runtime research (`mars-runtime/`)

| Bucket | Reality |
|--------|---------|
| **experimental** | Narrow R1: bridge, adapters, hand-invoked `node` scripts, run-state JSON. |
| **conceptual** | v0 contracts (queue, orchestrator, lifecycle, deployment) — **design only**. |
| **documentation-only** | Architecture map, README boundaries. |

**Not:** production orchestrator, scheduler, daemon, control plane implementation, E2E MARS automation.

**SoT:** [../mars-runtime/README.md](../mars-runtime/README.md) · [runtime-registry-boundaries.md](runtime-registry-boundaries.md)

---

## MetaBOT

| Bucket | Reality |
|--------|---------|
| **operational** | Canonical pack `projects/metabot-seo-content-agent/`; operator runbooks; registry **active**. |
| **external** | **n8n** graphs, Telegram, provider APIs — execution truth in live consoles. |
| **experimental** | `mars-runtime/adapters/*` — demo handoff only. |
| **deprecated** | `projects/seo-content-agent/` — **do not extend**. |
| **documentation-only** | Sanitized exports, integration contracts in-repo. |

**Not:** MARS core runtime; in-repo orchestration of MetaBOT.

**SoT:** [../projects/metabot-seo-content-agent/README.md](../projects/metabot-seo-content-agent/README.md) · [external-system-boundaries.md](external-system-boundaries.md)

---

## ORCA

| Bucket | Reality |
|--------|---------|
| **operational** | Human-supervised PPC toolkit: methodology, checklists, fast-path, live pilots under `projects/orca/`. |
| **conceptual** | Heuristics, semantic rules, report templates. |
| **external** | Ad platforms, SERP UI, customer landing pages. |
| **documentation-only** | Dense pack (~800+ md) — **workflow support**, not automation. |

**Not:** bidding engine, scheduler, validator daemon, MARS runtime component.

**SoT:** [../projects/orca/README.md](../projects/orca/README.md) · [OPERATIONAL-INDEX.md](../projects/orca/OPERATIONAL-INDEX.md) · registry **active**, runtime **excluded**

---

## WPilot

| Bucket | Reality |
|--------|---------|
| **operational** | Phase 1 MVP docs: backup/rollback discipline, QA templates, operator sequences. |
| **conceptual** | Plugin concept + MVP roadmap — **planned** bridge to Factory-native WordPress. |
| **external** | WordPress admin, Beget/hosting, DB awareness — **outside** repo. |
| **documentation-only** | Entire `projects/wpilot/` until plugin source appears in-tree. |

**Not:** deploy bot, autonomous CMS agent, MARS runtime.

**SoT:** [../projects/wpilot/README.md](../projects/wpilot/README.md) · [../projects/wpilot/plugin-mvp/reconciliation-map-v0.md](../projects/wpilot/plugin-mvp/reconciliation-map-v0.md)

---

## GitGuard

| Bucket | Reality |
|--------|---------|
| **conceptual** | Example **Program / Operational System** name in [system-entity-model.md](system-entity-model.md). |
| **documentation-only** | Taxonomy placeholder only. |

**Not:** registered project, live pack, or MARS integration — **SAFE UNKNOWN** until `projects/gitguard/` + registry row exist.

---

## Continuity / IdeaBox

| Bucket | Reality |
|--------|---------|
| **operational** | Human-operated capture under `continuity/`; manual [master-index.md](../continuity/registry/master-index.md). |
| **documentation-only** | Protocols markdown — **not** persisted memory product. |

**Not:** `project_id` row; autonomous memory; semantic graph; governance auto-mutation.

**SoT:** [../continuity/README.md](../continuity/README.md) · [context-continuity-rules.md](context-continuity-rules.md)

---

## Triumph (minimal)

| Bucket | Reality |
|--------|---------|
| **operational** | Project pack + workspace placeholders; V2 SoT stabilization docs; active human/Cursor frontend work possible in `workspaces/`. |
| **conceptual** | Factory reference case; V3 **battle-test charter** — doctrine validation, **not** production authorization. |
| **documentation-only** | Reference-case narrative under Factory; registry **planned**. |
| **external** | Deployed site / hosting — **SAFE UNKNOWN** without operator confirmation. |

**Not:** proof of Website Factory runtime; V3 ≠ approved implementation; V2 CSS/structure **not** authority for V3.

**SoT:** [../projects/triumph-manipulator-landing/README.md](../projects/triumph-manipulator-landing/README.md) · [V3-BATTLE-TEST-CHARTER.md](../projects/triumph-manipulator-landing/V3-BATTLE-TEST-CHARTER.md)

---

## Read order (60 seconds)

1. [AGENTS.md](../AGENTS.md)  
2. [mars-operational-evolution-state-after-cycles-1-8-v0.md](mars-operational-evolution-state-after-cycles-1-8-v0.md) (post–Cycle 8 posture)  
3. This file **or** [ecosystem-topology-index.md](ecosystem-topology-index.md) — **one** only  
4. Pack-local `OPERATIONAL-INDEX.md` for the lane you are in  

---

## Related Phase 2 artefacts

| Doc | Role |
|-----|------|
| [lifecycle-synchronization-review-v0.md](lifecycle-synchronization-review-v0.md) | History vs registry gaps |
| [website-factory-navigation-compression-strategy-v0.md](website-factory-navigation-compression-strategy-v0.md) | Factory nav compression |
| [runtime-mythology-pressure-review-v0.md](runtime-mythology-pressure-review-v0.md) | Terminology pressure |
| [cross-system-clarity-review-v0.md](cross-system-clarity-review-v0.md) | Boundary pairs |

*Reality index — orientation only; expand truth via registries and evidence paths, not new ontology layers.*
