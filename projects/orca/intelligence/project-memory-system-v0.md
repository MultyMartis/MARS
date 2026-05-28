# ORCA Project Memory System v0

## Status

**PRE-IMPLEMENTATION FOUNDATION** — operator-maintained learning log per project.

Not institutional memory AI. Not auto-learning from ad platform APIs. Not performance guarantees.

## Purpose

Capture **what worked and what failed** on a specific PPC + landing engagement so future sessions do not repeat moderation mistakes, weak hooks, or disproven structures.

## Location

```
projects/orca/projects/<project-id>/logs/memory/
```

Or consolidated file:

```
projects/orca/projects/<project-id>/PROJECT-MEMORY.md
```

Triumph equivalent (until migrated): session notes in `ppc/triumph-manipulator/` run folders and `runs/*/README.md` — **do not duplicate** without operator merge.

## Memory Categories

| Category | Record when |
|----------|-------------|
| `what_worked` | Operator confirms positive pattern (CTR, call quality, approval — with evidence level) |
| `moderation_failures` | Ad/platform rejection, policy fix required |
| `good_hooks` | Headlines / offers that passed review and performed acceptably |
| `bad_hooks` | Rejected, weak CTR, misleading, or correction required |
| `ctr_observations` | Directional notes — **not** authoritative analytics without export proof |
| `landing_performance` | Bounce, call rate, form rate — human-reported or analytics snapshot |
| `failed_strategies` | Architectures abandoned with reason |
| `winning_structures` | Campaign/group structures worth repeating in same niche |

## Entry Schema (recommended)

```yaml
memory_id: mem-001
date: 2026-05-21
category: moderation_failures
mode: search
evidence: operator-confirmed
summary: "Headline X rejected — excessive superlative"
detail: |
  Platform message: ...
  Fix applied: ...
safe_unknown: []
supersedes: null
```

## Evidence Rules

- Performance claims require `verified` or `operator-confirmed` and source (export date, analytics screenshot id).
- `ai-derived` performance stories **forbidden** in memory without export attachment.
- Contradicting entries: keep both, link `supersedes`, note market change.

## HITL Cadence

- **After** import, launch, or meaningful traffic slice — operator adds entry (optional but recommended).
- **Before** new campaign wave — read memory file (2-minute scan).
- **Monthly** — mark stale entries `historical` if niche shifted.

## Relationship to Project Memory vs Global ORCA

| Scope | Location |
|-------|----------|
| Project-specific | `PROJECT-MEMORY.md` / `logs/memory/` |
| Cross-project patterns | Parent `projects/orca/observations/`, `heuristics/` — human curated |

Project memory does not auto-promote to global heuristics without separate review.

## What Memory Is Not

- Training data pipeline for autonomous optimizer.
- Proof of ROAS or CPA.
- Replacement for Yandex.Direct reporting.

## SAFE UNKNOWN

- Unified memory schema JSON — **not in v0**.
- Sync from ad platform — **not claimed**; manual export attachment only.

## Related Documents

- [orca-research-layer-v0.md](../research/orca-research-layer-v0.md)
- [evidence-classification-system-v0.md](../evidence/evidence-classification-system-v0.md)
- [orca-operational-principles-v0.md](../orca-operational-principles-v0.md)
