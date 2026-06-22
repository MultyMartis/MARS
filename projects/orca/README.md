# ORCA

Operational Research & Campaign Architecture (ORCA) is a practical, human-supervised PPC operational toolkit for live review, campaign preparation, and evidence-aware decision support inside the MARS ecosystem.

ORCA helps operators run fast PPC review loops: mobile SERP review, landing mismatch detection, CTA review, semantic cleanliness review, aggregator pressure review, mobile friction analysis, and short operational reporting before any human platform action.

## What ORCA Is

- Human-supervised PPC operational toolkit.
- Live operational copilot for PPC review sessions.
- Practical review framework for SERP, landing, semantic, CTA, and mobile checks.
- Documentation-first operating model for repeatable campaign preparation and QA.

## What ORCA Is Not

- Not an autonomous PPC optimizer.
- Not a bidding engine.
- Not a runtime.
- Not an orchestration system.
- Not an AI ad manager.
- Not a campaign launch tool.

## Phase 1 Scope

Phase 1 defines the minimum documentation needed to operate ORCA manually with AI assistance:

- PPC project intake.
- SERP and competitor research.
- Semantic collection and clustering.
- Campaign and ad group architecture.
- Ad copy drafting.
- Direct Commander style export package preparation.
- QA gates before platform use.

All outputs require human review before use in Yandex.Direct, Google Ads, or any other advertising system.

## Document Map

Start here for operator navigation:

- `OPERATIONAL-INDEX.md` - **live-first** entry point for fast PPC sessions (default).
- **ORCA Intelligence Foundation v0** — intake, project contracts, evidence, campaign modes, artifacts, research, Factory bridge. Index section: [OPERATIONAL-INDEX.md § ORCA Intelligence Foundation v0](OPERATIONAL-INDEX.md#orca-intelligence-foundation-v0). Principles: [orca-operational-principles-v0.md](orca-operational-principles-v0.md).
- **Incoming intake** — raw packs: `incoming/orca/<project-id>-raw-pack/`; architecture: [intake/orca-universal-intake-architecture-v0.md](intake/orca-universal-intake-architecture-v0.md).
- **Campaign modes** — [campaign-modes/orca-campaign-mode-architecture-v0.md](campaign-modes/orca-campaign-mode-architecture-v0.md).
- `operator-entrypoints-v1.md` - **task-shaped** starts (new project, pilot) — **not** live-session default.
- `live-pilot/` - live review session shape and stop rules.
- `starter-core/` - smallest useful set of live review paths.
- `current-state-v1.md` - concise current-state map, exclusions, risks, and next step.
- `operator-entrypoints-v1.md` - where to start by operator task.
- `doc-map-v1.md` - compact map of ORCA documentation layers.

Core documentation:

- `system-overview.md` - ORCA purpose, layers, supervision, and boundaries.
- `phase-1-architecture.md` - minimal viable Phase 1 architecture and excluded areas.
- `agents/` - role definitions for human-supervised ORCA subagents.
- `workflows/` - documented workflows for research, semantics, generation, export, and QA.
- `contracts/` - input and output contracts for handoffs between workflow steps.
- `research/` - SERP, competitor, and review analysis methodology.
- **PPC Semantic Intelligence — world practice research (2026-06)** — analytical source only; operator decisions D1–D7: [research/ppc-semantic-intelligence/world-practice-2026-06/README.md](research/ppc-semantic-intelligence/world-practice-2026-06/README.md).
- **ORCA Semantic Intelligence Architecture v1** — target multi-stage architecture (SI-01–SI-17); ADR **APPROVED — IMPLEMENTATION NOT STARTED**; checkpoint `f17c270`: [architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-ADR-v1.md](architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-ADR-v1.md).
- **ORCA Semantic Intelligence Taxonomy & Schema v1 (P0-B)** — **APPROVED — IMPLEMENTATION NOT STARTED**; checkpoint `3151953`: [semantic-intelligence/README.md](semantic-intelligence/README.md).
- **ORCA Semantic Annotation Guideline v1 (P0-C)** — **APPROVED — IMPLEMENTATION NOT STARTED** (checkpoint `78b0557`, C1–C7): [semantic-intelligence/annotation/README.md](semantic-intelligence/annotation/README.md).
- **ORCA Universal Semantic Benchmark Charter v1 (P0-D)** — **PROPOSED — ON HOLD** (capability recovery audit v1); uncommitted: [semantic-intelligence/benchmark/README.md](semantic-intelligence/benchmark/README.md). Audit: [audits/triumph-to-orca-capability-recovery-v1/](audits/triumph-to-orca-capability-recovery-v1/). Next gate: operator audit review → integration stage → amended P0-D.
- `semantic/` - intent, clustering, geo modifier, negative keyword, and semantic quality rules.
- `qa/` - PPC semantic, campaign structure, landing match, and ad relevance QA.
- `methodology/` - PPC research, campaign architecture, intent, offer, and landing methodology.
- `patterns/` - reusable local-service, SERP, offer, and aggregator pattern references.
- `pilot-cases/` - pilot templates, execution flow, and bounded pilot case records.
- `observations/` - observation model, normalization, SERP, semantic, landing, and regional rules.
- `intelligence/` - documented market pressure, local intent, trust, aggregator, and maturity models.
- `evidence/` - evidence discipline, strength, traceability, reliability, and human validation rules.
- `evolution/` - market, SERP, commercial pattern, seasonal, and regional distortion tracking.
- `contradictions/` - contradiction tracking, volatility, conflicting observation, and unstable pattern rules.
- `confidence/` - confidence governance, update, decay, repeatability, and reliability models.
- `live-observations/` - manual live observation workflows, methods, checklists, templates, and examples.
- `heuristics/` - human-supervised strategic heuristics and evidence requirements.
- `heuristic-mapping/` - evidence-to-heuristic traceability and revision discipline.
- `review/` - operational, methodology, evidence, heuristic, pilot, drift, and anti-mythology review.
- `reports/` - lightweight live-session and MVP usefulness report templates.
- `governance/` - local ORCA boundaries, SAFE UNKNOWN, anti-bloat, and live-review rules.

SAFE UNKNOWN: no separate `evidence-records/` layer is present in this tree at the time of this README update.

## Current Status

Documentation-first, Phase 1 draft with a live-first starter core for human-supervised PPC operational review.

No ORCA runtime, autonomous campaign manager, bidding automation, optimization engine, or production orchestration exists in this pack.

## Ecosystem Relationships (canonical visibility)

| System | Relationship |
|--------|--------------|
| **MIG** | Upstream acquisition lane. ORCA consumes **human-approved** market groundtruth handoffs; ORCA does not claim MIG acquisition ownership. |
| **Website Factory** | Optional downstream implementation lane. ORCA can produce strategy/semantic handoff artifacts, but ORCA remains operable without Factory when source is an existing client site. |
| **WPilot / OCPilot** | External implementation systems. No direct ORCA runtime ownership; relationships are boundary and handoff-oriented. |
| **MARS governance / survivability** | ORCA consumes honesty, boundary, and safe-execution discipline; governance does not execute ORCA workflows. |
