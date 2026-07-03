# MARS Agent Quality

**Status:** `MINIMAL_V1`  
**Maturity:** `active / minimal v1`  
**Mode:** `HUMAN_INVOKED` / `NOT_AUTOMATED`

## What This Is

MARS Agent Quality is a minimal operational reliability layer for structuring agent work, task prompts, REPORT review, failure records, and quality gates.

This package consolidates already existing operational surfaces into a small usable layer under `projects/mars-agent-quality/`.

This is an operational reliability layer, not an autonomous runtime.

## What This Is Not

- `EXCLUDED`: Not a runtime implementation.
- `EXCLUDED`: Not Remote Operations Layer.
- `EXCLUDED`: Not a global governance wave.
- `EXCLUDED`: Not a refactor of MARS.
- `EXCLUDED`: Not automatic enforcement.
- `EXCLUDED`: Not proof that any agent, validator, orchestrator, storage adapter, or remote operator exists.

This does not create automatic enforcement.

## Current Maturity

`MINIMAL_V1`: documentation surfaces only.

The layer is ready for human-invoked use in future Cursor/Web-GPT tasks, but it does not claim automation, interception, runtime policy enforcement, or autonomous task quality control.

## Relationship To Survivability / GitGuard

AQ-01 reuses Survivability concepts: scope lock, protected zones, destructive operation boundaries, halt protocol, SAFE UNKNOWN, and human-invoked validators.

It does not replace `projects/mars-survivability/`.

GitGuard remains a referenced/future helper surface where documented. AQ-01 does not claim GitGuard is active automatic enforcement.

## Relationship To Remote Operations Layer

Remote Operations Layer is a future/applied consumer, not part of AQ-01.

This package may be used later to structure Remote Operations Layer task contracts, failure records, and report gates, but AQ-01 does not authorize remote operations.

Remote operations require a separate ROL charter.

## Relationship To Programme Parent Chats

AQ-01 may be referenced by programme parent chats as a reusable quality surface.

This does not replace programme OPERATIONAL-INDEX files.

Programme-specific authority remains with the programme's own index, lifecycle, registry, task starter, and operator decisions.

## Allowed Use

- Structure future agent task prompts.
- Check REPORT completeness.
- Record failure patterns.
- Define stop conditions and evidence requirements.
- Support human-invoked quality review before downstream programme work.

## Excluded Claims

- Roadmap is not implementation proof.
- Report is not Git persistence proof.
- Build PASS is not Visual PASS.
- Cache is not checkpoint.
- Documented policy is not automatic enforcement.
- Task completion text is not proof without evidence.

## Entry Points

- `OPERATIONAL-INDEX.md`
- `contracts/agent-contract-v1.md`
- `templates/task-starter-v1.md`
- `gates/report-quality-gate-v1.md`
- `templates/failure-record-template-v1.md`
- `checklists/execution-guard-checklist-v1.md`
