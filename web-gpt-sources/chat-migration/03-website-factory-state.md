# 03 — Website Factory state (migration v0)

**Canonical index:** `projects/mars-website-factory/workflow-map.md`, `projects/mars-website-factory/README.md`.  
**Capability id:** **C16** (`governance/capability-map.md`). **Stage:** **16** pilot documentation (`governance/master-build-map.md`).

---

## Workflow v0

- **`website-factory-workflow-v0.md`:** canonical **high-level production chain** (intake → … → delivery) — **documentation only**; **not** a workflow engine.  
- **`workflow-map.md`:** diagram / HITL alignment companion; maps factory stages to `workflows/execution-flow.md` concepts **narratively**.

## Artifact architecture

- **`artifact-architecture-overview-v0.md`** and linked v0 docs: normalized **artifact vocabulary** (objectives, CTAs, sections, SEO/conversion intent, frontend artifacts, QA payload **concepts**).  
- **EXISTS:** Markdown contracts.  
- **NOT:** Executable JSON schemas, enforced runtime validation.

## Execution semantics

- **Execution Semantics Layer v0** (`execution-semantics-overview-v0.md`, stage/artifact state, approval, revision, regeneration, dependency invalidation, orchestration **signals**, QA gating, delivery lifecycle).  
- **IS:** Operational methodology + **runtime-preparation architecture** (words on disk).  
- **IS NOT:** Runtime engine, scheduler, queue, daemon.

## Semantic relationship layer

- Cross-artifact semantics, inheritance, consistency, freeze vocabulary (`semantic-relationship-overview-v0.md` + linked).  
- **IS NOT:** Graph DB, vector engine, autonomous semantic reasoning.

## Artifact bus

- **Artifact Bus Layer v0** (envelope, routing, lineage, publication/consumption, transfer QA).  
- **IS:** Document-first **movement discipline**.  
- **IS NOT:** Kafka/Rabbit queue, async event engine, message broker.

## Validation runtime **model**

- **`validation-runtime-overview-v0.md`** + linked (lifecycle, evidence, result, failure, waiver, escalation, consistency, **boundary** doc).  
- **IS:** Vocabulary for honest validation reporting.  
- **IS NOT:** Validator service, CI worker, Lighthouse/crawl automation.

## Operational templates

- **`operational-template-overview-v0.md`** + `*-template-v0.md`: reusable Markdown **shells** for sessions, reviews, delivery gates.  
- **IS NOT:** Generated Task pipelines, n8n graphs, executable workflows.

## Reference execution case

- **`reference-cases/triumph-manipulator-landing/`:** documentation-first **simulated** end-to-end case.  
- **IS NOT:** Assertion of shipped production site or hidden automation.

## Operational runbooks

- **`first-operational-runbook-v0.md`:** human execution layer **R01–R15**, checkpoints **C01–C08**, operator lanes — **not** automation.

## QA philosophy

- **`qa-validation-model.md`:** Validator + specialist QA lanes; **explicit** “no claim automated QA runs today”.  
- **SAFE UNKNOWN** row for missing engines (visual regression, Lighthouse in-repo, etc.).

## Delivery philosophy

- Delivery readiness via **gates**, **HITL**, **REPORT**, and **delivery lifecycle** docs — human-owned **readiness**, not autonomous deploy.

---

## EXISTS (evidence: files in-repo)

| Area | Status |
|------|--------|
| Workflow + layer map + runbook + reference case | **Doc pack present** |
| Registries (site type, block) v0 | **Markdown** |
| Agent cards under `agents/cards/` | **Documentation** |
| Triumph project pack + workspace | **Project + `workspaces/triumph-manipulator-landing/`** |

## PLANNED (governance wording)

| Area | Notes |
|------|--------|
| Control Plane scheduling, persisted Task state | **Target** in contracts |
| Real validator tooling / CI integration | **TBD** |
| Full legacy → MetaBOT migration cleanup | Stage 16 “missing” |

## SAFE UNKNOWN

- Whether specific **automation** will attach to validation or artifact bus **first**.  
- Exact **runtime** shape for Website Factory when/if Phase 2+ code lands.  
- Completeness of **experimental** `mars-runtime` vs external MetaBOT/n8n.
