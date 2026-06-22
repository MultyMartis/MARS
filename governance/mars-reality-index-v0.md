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
| **WPilot** | ✓ reference DEV runtime (RC5) | — | production bridge; Sprint 3 (charter-gated) | ✓ WP/host | — | ✓ reference docs + maintenance policy |
| **MIG** | ✓ acquisition discipline | ✓ v0.1 spine | ✓ R1 boundary | ✓ n8n/self-host runtime lane | — | ✓ contracts + pack |
| **OCPilot** | ✓ OpenCart bridge discipline | — | ✓ sibling/family model | ✓ hosting/FTP/PMA | — | ✓ Phase 0+ |
| **MARS Localhost (MLI)** | — | — | ✓ shared localhost foundation | ✓ D: runtime zone | — | ✓ MLI-03 WordPress profile |
| **EAR Runtime** | — | ✓ R1 foundation code | ✓ acquisition helpers architecture alignment | ✓ connector targets (future) | — | ✓ engineering program docs |
| **MARS Survivability** | ✓ safety discipline | human-invoked helpers | ✓ contracts/protocols | — | — | ✓ hardening pack |
| **NOVA** | — | — | ✓ mobile methodology foundation | — | — | ✓ foundation v1 docs |
| **HomeGateway v4.ai** | — | — | ✓ personal operational cockpit concept (static-first) | — | — | ✓ draft/planning docs |
| **ATLAS** | ✓ population discipline | — | ✓ registry intent | — | — | ✓ foundation + population docs |
| **OPS** | ✓ back-office discipline | ✓ WF-01/WF-02 pilots | — | — | — | ✓ foundation + workflows |
| **GitGuard** | ✓ advisory + helpers | — | ✓ entity-model name | — | — | ✓ mars-survivability pack |
| **Continuity / IdeaBox** | ✓ incubation (optional) | — | protocols | — | — | ✓ not `project_id` |
| **Incoming** | ✓ active staging | — | hybrid placement | ✓ bulk (post-triage) | — | ✓ intake charter |
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

**Forge WordPress (subsystem):** **FOUNDATION** — WordPress implementation layer candidate; [subsystems/forge-wordpress/](../projects/mars-website-factory/subsystems/forge-wordpress/); **not** operational · **not** runtime · **not** registered agent.

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

**Search PPC Lifecycle v1 (2026-06-22):** `APPROVED — CHECKPOINTED` (`43c4271`) — [../projects/mars-search-ppc-production/MARS-SEARCH-PPC-PRODUCTION-LIFECYCLE-v1.md](../projects/mars-search-ppc-production/MARS-SEARCH-PPC-PRODUCTION-LIFECYCLE-v1.md). Wave 1 core **APPROVED — CHECKPOINTED** (`2b3020d`). Wave 1.1 entry-point wiring **IMPLEMENTED — OPERATOR REVIEW REQUIRED**. Wave 2 **BLOCKED PENDING WAVE 1.1 REVIEW**. Lifecycle gate + execution receipts implemented; **NOT OPERATIONAL**. Corvonero **FROZEN**; P0-I pilot **DIAGNOSTIC EVIDENCE**; P0-D **ON HOLD**.

---

## WPilot

| Bucket | Reality |
|--------|---------|
| **operational** | **Reference Implementation** on DEV — `v0.3.0-RC5` proven: content writes + authenticated REST connection tracking; authority `WPILOT-RC5-PROVEN-CONNECTION-RUNTIME-2026-06-19`; commit `648632acbdd42703427fd76a0cb1fd8d88641dcc`. RC5 development focus **closed**; maintenance reference. Sprint 3 **HOLD**. |
| **experimental** | In-repo plugin source under `projects/wpilot/plugin/metacode-wpilot/` (frozen baseline); live runtime on Beget DEV — external execution truth. |
| **conceptual** | Production bridge, Factory Mode A pipeline, Sprint 3 expansion — planned; require explicit HITL charter. |
| **external** | WordPress admin, Beget/hosting, live plugin on DEV — **outside** repo ownership. |
| **documentation-only** | Phase 1 operations, boundaries, final state, lifecycle, maintenance policy, RC5 ecosystem sync. |

**Not:** deploy bot, autonomous CMS agent, MARS runtime, production deployment claim, active MVP development target.

**Runtime maturity:** `proven_content_writes` + `proven_connection_runtime` (DEV only).

**Lifecycle:** Reference Implementation.

**SoT:** [../projects/wpilot/WPILOT-FINAL-STATE-RC5.md](../projects/wpilot/WPILOT-FINAL-STATE-RC5.md) · [../projects/wpilot/WPILOT-AUTHORITY-STATE-RC5.md](../projects/wpilot/WPILOT-AUTHORITY-STATE-RC5.md) · [../projects/wpilot/OPERATIONAL-INDEX.md](../projects/wpilot/OPERATIONAL-INDEX.md) · [../projects/wpilot/WPILOT-MAINTENANCE-POLICY-v1.md](../projects/wpilot/WPILOT-MAINTENANCE-POLICY-v1.md)

---

## HomeGateway v4.ai

| Bucket | Reality |
|--------|---------|
| **conceptual** | Personal Operational Cockpit model and ecosystem surface-layer role are defined at planning level. |
| **documentation-only** | `projects/homegateway-v4-ai/` is currently draft/planning documentation with static-first framing. |

**Not:** MARS runtime, control plane, autonomous agent, or deployed backend integration layer.

**SoT:** [../projects/homegateway-v4-ai/README.md](../projects/homegateway-v4-ai/README.md) · [../projects/homegateway-v4-ai/OPERATIONAL-INDEX.md](../projects/homegateway-v4-ai/OPERATIONAL-INDEX.md)

---

## MIG

| Bucket | Reality |
|--------|---------|
| **operational** | Human-supervised market groundtruth acquisition discipline (R1 intent) with explicit MIG → ORCA handoff contract and approval gate. |
| **experimental** | v0.1 session spine (Node.js + n8n export) implemented as narrow runtime slice. |
| **conceptual** | Full acquisition lifecycle beyond v0.1 remains planned. |
| **external** | Self-hosted n8n/runtime environment and providers remain external execution surfaces. |
| **documentation-only** | Contracts, boundaries, runbooks, and architecture docs are canonical in-repo visibility. |

**Not:** ORCA interpretation engine, Website Factory blueprint generator, CMS implementation lane, or autonomous handoff runtime.

**SoT:** [../projects/mig/README.md](../projects/mig/README.md) · [../projects/mig/OPERATIONAL-INDEX.md](../projects/mig/OPERATIONAL-INDEX.md) · [../projects/mig/contracts/mig-orca-handoff-contract-v0.md](../projects/mig/contracts/mig-orca-handoff-contract-v0.md)

---

## OCPilot

| Bucket | Reality |
|--------|---------|
| **operational** | Human-supervised OpenCart/ocStore operational discipline (audit, baselines, controlled change planning). |
| **conceptual** | Family/sibling model with WPilot and EAR-enabled intake patterns remains architecture-led. |
| **external** | Live OpenCart hosting, FTP/PMA/admin, and credentials remain outside MARS ownership. |
| **documentation-only** | Phase 0+ pack and run artifacts define process truth; runtime is not claimed. |

**Not:** WPilot child, autonomous ecommerce admin runtime, or EAR implementation owner.

**SoT:** [../projects/ocpilot/README.md](../projects/ocpilot/README.md) · [../projects/ocpilot/OPERATIONAL-INDEX.md](../projects/ocpilot/OPERATIONAL-INDEX.md)

**MLI pointer (2026-06-22):** OCPilot may consume OpenCart runtime profile on `D:\MARS-Localhost` — [../projects/mars-localhost-infrastructure/MARS-LOCALHOST-CONSUMER-MODEL-v1.md](../projects/mars-localhost-infrastructure/MARS-LOCALHOST-CONSUMER-MODEL-v1.md). No runtime migration in MLI-00.

---

## MARS Localhost Infrastructure (MLI)

| Bucket | Reality |
|--------|---------|
| **conceptual** | Shared localhost foundation — brain on `C:\AI MARS`, execution on `D:\MARS-Localhost`. |
| **external** | D: runtime tree is out-of-git; Laragon install is operator machine state. |
| **documentation-only** | MLI-03 **COMPLETE** — WordPress synthetic MLI-WP-SYN-001; OpenCart profile **NEXT** (MLI-04). |

**Not:** MARS brain, Git authority, production hosting, or proof that WordPress/OpenCart local profiles are validated.

**SoT:** [../projects/mars-localhost-infrastructure/OPERATIONAL-INDEX.md](../projects/mars-localhost-infrastructure/OPERATIONAL-INDEX.md) · [mars-infrastructure-reality-v1.md](mars-infrastructure-reality-v1.md)

**Next:** Forge WordPress **FW-05R** (parallel: MLI-04 OpenCart profile).

---

| Bucket | Reality |
|--------|---------|
| **experimental** | R1 foundation skeleton + config loader only under `projects/ear-runtime/runtime/`. |
| **conceptual** | Engineering roadmap (R1–R5), consumer boundaries, and architecture conformance model. |
| **documentation-only** | Program charters, non-goals, and transition decisions define visibility; no live connector/runtime proof. |

**Not:** EAR Architecture authority layer, OCPilot/WPilot consumer logic, or production acquisition runtime.

**SoT:** [../projects/ear-runtime/README.md](../projects/ear-runtime/README.md) · [../projects/ear-runtime/EAR-RUNTIME-STATE.md](../projects/ear-runtime/EAR-RUNTIME-STATE.md)

---

## MARS Survivability

| Bucket | Reality |
|--------|---------|
| **operational** | Human-operated survivability and safe-execution discipline with protocols, guardrails, drills, and checklists. |
| **experimental** | Human-invoked validator/helpers exist as tooling aids, not autonomous enforcement. |
| **conceptual** | GitGuard evolution remains design-contract direction until a dedicated project pack exists. |
| **documentation-only** | Contracts and protocols are normative docs, not policy engine code. |

**Not:** Replacement for governance survivability spine, ORCA/Factory execution runtime, or automated sandbox.

**SoT:** [../projects/mars-survivability/README.md](../projects/mars-survivability/README.md) · [../projects/mars-survivability/OPERATIONAL-INDEX.md](../projects/mars-survivability/OPERATIONAL-INDEX.md)

---

## NOVA

| Bucket | Reality |
|--------|---------|
| **conceptual** | Mobile/PWA production methodology foundation (RBM v1 complete) as Website Factory counterpart. |
| **documentation-only** | Foundation artifacts and status docs only; implementation and agent cards not started. |

**Not:** Runtime, orchestration product, or active operational system implementation.

**SoT:** [../projects/nova/README.md](../projects/nova/README.md) · [../projects/nova/NOVA-FOUNDATION-STATUS-v1.md](../projects/nova/NOVA-FOUNDATION-STATUS-v1.md)

---

## ATLAS

| Bucket | Reality |
|--------|---------|
| **operational** | Human-maintained **Business Reality Registry** under `projects/atlas/`: foundation complete; **documentation-layer population** Waves 1–6B + Agreement metadata layers **complete** (attestation registers under `population/`); consumer contracts for MIG, ORCA, Factory, WPilot, OCPilot, HomeGateway. |
| **documentation-only** | Normative foundation + population evidence — **no** persistence engine, APIs, CRM/ERP, or automated enforcement. |

**Not:** Runtime, storage product, MARS `project_id` SoT replacement, ORCA/MIG artifact owner, orchestration, or proof that all consumers bind ATLAS ids in daily work.

**SoT:** [../projects/atlas/foundation/ATLAS-REALITY-MODEL-v1.md](../projects/atlas/foundation/ATLAS-REALITY-MODEL-v1.md) · [OPERATIONAL-INDEX.md](../projects/atlas/OPERATIONAL-INDEX.md) · registry `atlas` (**planned**) · [../logs/atlas/atlas-registration-v1.md](../logs/atlas/atlas-registration-v1.md)

---

## OPS

| Bucket | Reality |
|--------|---------|
| **operational** | Human-supervised business operations discipline: reporting, document, approval, deadline, follow-up, and coordination workflows under `projects/ops/`; WF-01 and WF-02 **live binding pilots PARTIAL** (2026-06-10); alignment passes **documented**. |
| **documentation-only** | Foundation, data model, workflow architecture (WF-01–WF-06), mission layer, and registration evidence — **no** in-repo execution engine. |

**Not:** Runtime, infrastructure, authority domain, CRM/ERP, ATLAS implementation, orchestration, or automated evidence pull from MetaBOT/ORCA/MIG/WPilot/OCPilot.

**SoT:** [../projects/ops/README.md](../projects/ops/README.md) · [OPERATIONAL-INDEX.md](../projects/ops/OPERATIONAL-INDEX.md) · registry `ops` (**planned**) · [../logs/ops/ops-registration-v1.md](../logs/ops/ops-registration-v1.md)

---

## GitGuard

| Bucket | Reality |
|--------|---------|
| **operational** | **REGISTERED** **Repository Survivability Layer** — advisory + human-invoked helpers under [../projects/mars-survivability/](../projects/mars-survivability/) (G0–G4 documented; no autonomous product). |
| **conceptual** | Example **Program / Operational System** name in [system-entity-model.md](system-entity-model.md) — **implemented** via survivability pack, not separate `projects/gitguard/`. |

**Not:** `project_id` row, `projects/gitguard/` pack, or autonomous Backup/Checkpoint/Rollback product.

**SoT:** [../projects/mars-survivability/registries/gitguard-system-entry-v1.md](../projects/mars-survivability/registries/gitguard-system-entry-v1.md) · [../registry/project-registry.md](../registry/project-registry.md) (cross-cutting REGISTERED) · [ecosystem-topology-index.md](ecosystem-topology-index.md) § GitGuard · [../logs/cleanup/actions/gitguard-registration-v1.md](../logs/cleanup/actions/gitguard-registration-v1.md)

---

## Continuity / IdeaBox

| Bucket | Reality |
|--------|---------|
| **operational** | **Incubation Layer** (optional) — human-operated capture under `continuity/`; manual [master-index.md](../continuity/registry/master-index.md). |
| **documentation-only** | Protocols markdown — **not** persisted memory product. |

**Not:** `project_id` row; mandatory entry path; autonomous memory; semantic graph; governance auto-mutation.

**SoT:** [../continuity/README.md](../continuity/README.md) · [context-continuity-rules.md](context-continuity-rules.md) · [../logs/cleanup/actions/ideabox-alignment-v1.md](../logs/cleanup/actions/ideabox-alignment-v1.md)

---

## Incoming (ecosystem intake)

| Bucket | Reality |
|--------|---------|
| **operational** | **Active Incoming** in Active Brain — `incoming/mig/` operational; other subfolders = triage/stub/historical. |
| **external** | **Historical Bulk** toward Storage Layer / Cold Brain **after** operator triage — **not** moved in Wave 2B. |

**Not:** registry row, runtime pipeline, or trusted SoT.

**SoT:** [../incoming/README.md](../incoming/README.md) · [ecosystem-topology-index.md](ecosystem-topology-index.md) § Incoming · [../logs/cleanup/actions/incoming-hybrid-alignment-v1.md](../logs/cleanup/actions/incoming-hybrid-alignment-v1.md)

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
