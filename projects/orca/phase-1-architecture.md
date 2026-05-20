# ORCA Phase 1 Architecture

## Minimal Viable Architecture

Phase 1 is a documentation-first operating architecture for human-supervised PPC preparation. It defines roles, workflows, and contracts for producing reviewable campaign artifacts.

It does not define a runtime, account integration, autonomous optimizer, bidding system, or live campaign manager.

## Required Operational Layers

- Project intake and constraints.
- SERP and competitor research.
- Semantic collection and cleaning.
- Semantic clustering and intent mapping.
- Campaign structure generation.
- Ad copy drafting.
- Export package preparation.
- PPC QA and human approval.

## Required Subagents

- ORCA Strategic Orchestrator.
- Yandex SERP Research Agent.
- Semantic Collector Agent.
- Cluster Builder Agent.
- Campaign Architecture Agent.
- Ad Copy Generator Agent.
- Direct Commander Export Agent.
- PPC QA Agent.

Subagents describe responsibilities for human-operated work. They are not autonomous workers connected to ad accounts.

## Workflows

- SERP research workflow.
- Semantic workflow.
- Campaign generation workflow.
- Direct Commander export workflow.
- QA workflow.

Each workflow produces artifacts that must be reviewed by a human before use.

## QA Gates

- Intake completeness check.
- Source reliability check.
- Keyword relevance check.
- Cluster coherence check.
- Campaign naming and structure check.
- Ad copy policy and brand check.
- Export column and format check.
- Final human approval check.

No campaign package is considered ready until QA notes are resolved or explicitly accepted by the human operator.

## Anti-Chaos Rules

- Do not mix research, generation, export, and QA in one uncontrolled step.
- Do not invent budgets, bids, landing pages, legal claims, or conversion targets.
- Do not treat competitor observations as verified strategy.
- Do not upload, activate, pause, or edit campaigns automatically.
- Do not claim performance improvement without evidence.
- Keep SAFE UNKNOWN visible in every handoff where facts are missing.

## Explicit Excluded Future Areas

The following are outside Phase 1:

- automatic bidding;
- autonomous campaign optimization;
- live account synchronization;
- budget reallocation;
- performance feedback loops;
- API-based campaign publishing;
- production orchestration runtime;
- hidden optimization services;
- autonomous A/B testing.

These areas may only be discussed as future ideas with clear human control and implementation evidence requirements.
