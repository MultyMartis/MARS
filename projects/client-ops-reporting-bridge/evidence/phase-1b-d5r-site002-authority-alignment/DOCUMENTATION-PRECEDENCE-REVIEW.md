# DOCUMENTATION-PRECEDENCE-REVIEW

| Authority | Claimed precedence / meaning | Consistent with code? | Current / legacy |
|-----------|------------------------------|-----------------------|------------------|
| `ARTIFACT-AUTHORITY-AND-PRECEDENCE.md` | `monitor-classification` primary classification; `changed-summary` metrics; `run-summary` execution metadata; classification mismatch → BLOCKED / SOURCE_ARTIFACT_CONFLICT; do not silently prefer one side | **Yes** with Client Ops normalizer; **Yes** that contradiction must block; intended Python equality aligns with “primary once conflicts resolved” | CURRENT (Phase 0A freeze) |
| `SITE-002-MVP-INTAKE.md` | Same family; documents known ONBOARDING vs NO_ACTION conflict class | Consistent with observed Storage artifacts | CURRENT |
| D4 `SITE002-SOURCE-AUTHORITY.md` | SOURCE_AUTHORITY_CONFIRMED; three-file family | Consistent | CURRENT |
| SITE-002 hardening report / tools README | Shared classification vocabulary; both files part of hardened contract; run-summary includes classification | Consistent with **Python** intent; **does not document** runner overwrite bug | CURRENT docs, **incomplete** wrt runner merge |
| SITE-002 runner.ps1 comments (“Merge monitor-written run-summary if present (richer fields)”) | Implies enriching with runner metadata while keeping monitor richness | **Code contradicts comment** — non-null runner defaults overwrite monitor classification | CURRENT code defect |
| D4/D5 adapter docs (pre-D5R) | Treat disagreement as conflict → BLOCKED | Correct fail-closed behavior | CURRENT; D5R clarifies **why** disagreement appears |
| Hypothetical “different semantic layers” interpretation | run-summary=health, monitor=action | **Rejected** by Python writer equality + internal metric contradiction | NOT a valid current contract |

## Stale / wrong documentation cues

1. Any implication that `run-summary.classification` is an independent health enum that may disagree with `monitor-classification` — **wrong** relative to Python emitter.
2. Runner comment “richer fields” without stating classification must be preserved from monitor — **misleading**.
3. D5 historical “systemic conflict” note remains factually true as observation; D5R upgrades it from unexplained conflict to confirmed runner generation bug.
