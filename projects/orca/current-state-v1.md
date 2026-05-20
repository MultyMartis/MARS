# ORCA Current State v1

## ORCA Status

ORCA is a documentation-first, human-supervised PPC research and campaign architecture system inside the MARS repository.

It currently describes operating methods, roles, contracts, evidence discipline, observations, heuristics, heuristic mapping, and operational review. It does not prove a production runtime or autonomous PPC system exists.

## What Exists Now

- Phase 1 architecture and system overview.
- Agent role documentation for research, semantic, architecture, generation, export, QA, and strategy support.
- Workflow documentation for SERP research, semantics, campaign generation, export, and QA.
- Contracts for project input, SERP output, semantic clusters, campaign structure, and export packages.
- Research, semantic, QA, methodology, pattern, pilot, observation, intelligence, evidence, evolution, contradiction, confidence, live-observation, heuristic, heuristic-mapping, and review documentation layers.
- Templates, checklists, and fictional examples in several ORCA layers.

## Still Only Planned or Not Proven

- Runtime execution of ORCA agents.
- Automated campaign publishing.
- Automated bidding or optimization.
- Live market validation.
- Telemetry-backed review.
- Autonomous evidence collection.
- Autonomous heuristic evolution.
- Production orchestration.

## Explicitly Excluded

- Autonomous advertising AI.
- Self-learning PPC system.
- Browser automation.
- Scraping pipeline.
- Dashboards or telemetry systems.
- Deployment infrastructure.
- Runtime orchestration.
- Automatic governance.

## Active Documentation Layers

- Core: `README.md`, `system-overview.md`, `phase-1-architecture.md`.
- Operators: `operator-entrypoints-v1.md`, `doc-map-v1.md`, `current-state-v1.md`.
- Roles and process: `agents/`, `workflows/`, `contracts/`.
- Research and PPC logic: `research/`, `semantic/`, `qa/`, `methodology/`, `patterns/`.
- Evidence and reality discipline: `evidence/`, `observations/`, `live-observations/`, `contradictions/`, `confidence/`, `evolution/`.
- Strategic intelligence: `intelligence/`, `heuristics/`, `heuristic-mapping/`.
- Review and anti-drift: `review/`.

## Recommended Operator Entry Points

- **Live PPC session (default):** `OPERATIONAL-INDEX.md` → one Starter Core row → stop (see FAST PATH in index).
- New operator orientation: `README.md` → this file → `OPERATIONAL-INDEX.md` (not a full doc-map pass).
- Task-shaped deep link (secondary): `operator-entrypoints-v1.md` when INDEX does not list the concern.
- New PPC project: start with `contracts/project-input-contract-v0.md` and `workflows/serp-research-workflow-v0.md`.
- Pilot case: start with `pilot-cases/README.md` and `pilot-cases/pilot-execution-flow-v1.md`.
- Live SERP review: start with `live-observations/README.md`.
- Evidence and confidence review: start with `evidence/evidence-discipline-model-v1.md` and `confidence/confidence-governance-model-v1.md`.
- Heuristic review: start with `heuristic-mapping/README.md` and `review/README.md`.

## Current Highest Risks

- Documentation sprawl may reduce operator usability.
- Multiple review layers can create duplicated effort if entry points are unclear.
- Stale examples or patterns may be mistaken for current market evidence.
- Heuristics may be over-applied outside region, niche, device, or season boundaries.
- Confident wording may imply more implementation maturity than the repository proves.

## Next Practical Step

Run one human-reviewed ORCA pilot using the operator entry points, then update only the documents that proved useful or confusing.

## SAFE UNKNOWN

- No separate `evidence-records/` directory was found.
- No production ORCA runtime was verified.
- No live market validation was performed for this current-state map.
- No autonomous review, telemetry, or orchestration capability is evidenced by these documents.
