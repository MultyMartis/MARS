# MARS — Agent instructions (AGENTS.md)

**Project:** MARS (Multi-Agent Runtime System)  
**Repository role:** main documentation / design source for Phase 1; **not** a proof of a running multi-agent system unless the tree contains real implementation.

## Non-negotiables
1. **Status honesty** — Never state that implementation (runtime, agents, adapters, RAG, orchestration) **exists** unless files in-repo demonstrate it.
2. **Three-way split** — When discussing design or roadmap, keep separate: **documented architecture** vs **planned implementation** vs **legacy imported** (e.g. Web-GPT pack) material.
3. **SAFE UNKNOWN** — If evidence is missing, say so clearly; do not fill gaps with assumptions.
4. **Locale** — Prefer **Russian** for user-facing explanations and project-facing docs when appropriate. Cursor/agent prompts may remain **English**.

**Post–Cycle 8 ecosystem state (2026-05-19):** Cycles 1–8 complete — structural stabilization and survivability baseline **achieved**; governance **frozen** in **maintenance mode**; default work is **operational-first** (lane OPERATIONAL-INDEX, REPORT, HITL). **Canonical reference:** [governance/mars-operational-evolution-state-after-cycles-1-8-v0.md](governance/mars-operational-evolution-state-after-cycles-1-8-v0.md). **Do not** default to governance expansion or full-catalog reads; new governance waves require **explicit human charter**.

**Governance enforcement (documentation):** Human-readable anti-drift aids live under `governance/enforcement/` (check catalog, forbidden-claim cues, terminology boundaries, optional future validation strategy). **Not** automated enforcement, **not** a policy engine, **not** runtime code.

**Registry and identity discipline (documentation):** Phase S2 hygiene under `governance/` — [registry-architecture.md](governance/registry-architecture.md), [registry-source-of-truth.md](governance/registry-source-of-truth.md), [identity-and-naming-rules.md](governance/identity-and-naming-rules.md), [external-system-boundaries.md](governance/external-system-boundaries.md). Human-maintained clarity only; **no** registry engine, **no** sync, **no** runtime identity product claimed.

**Operational survivability (documentation):** Phase S3 under `governance/` — start [operational-survivability.md](governance/operational-survivability.md); linked entropy, onboarding, operator load, continuity, and stabilization-vs-expansion guides. Human discipline and documentation patterns only; **not** operational automation, **not** continuity persistence beyond committed artifacts.

**Execution contract stabilization (documentation):** Phase S4 under `governance/` — start [execution-contracts-overview.md](governance/execution-contracts-overview.md); task envelope, execution phase vocabulary, artifact lifecycle, validation-chain semantics, execution-boundary clarification. Contracts describe **human-operated** and **Cursor-layer** work; **not** orchestration products, **not** workflow engines, **not** autonomous validation or lifecycle automation.

**Operational tooling boundaries (documentation):** Phase S5 under `governance/` — start [operational-tooling-overview.md](governance/operational-tooling-overview.md); [tooling-boundary-rules.md](governance/tooling-boundary-rules.md), [tooling-escalation-warnings.md](governance/tooling-escalation-warnings.md). Lightweight helpers and scripts **assist** humans; **not** a tooling platform, **not** hidden automation, **not** governance enforcement as product.

**Controlled operationalization (documentation):** Phase S6 under `governance/` — start [controlled-operationalization.md](governance/controlled-operationalization.md); [interoperability-semantics.md](governance/interoperability-semantics.md), [human-execution-guarantees.md](governance/human-execution-guarantees.md), [operationalization-maturity-levels.md](governance/operationalization-maturity-levels.md), [operational-helper-classification.md](governance/operational-helper-classification.md), [operationalization-drift-warnings.md](governance/operationalization-drift-warnings.md). Describes how **real** helpers and **semi-structured** interoperability may evolve **governance-first** and **human-operated**; **not** orchestration, **not** autonomous runtime, **not** operational automation as product.

**Operational experiment framework (documentation):** Phase S7 under `governance/` — start [operational-experiments-overview.md](governance/operational-experiments-overview.md); [experiment-classification.md](governance/experiment-classification.md), [experiment-evidence-rules.md](governance/experiment-evidence-rules.md), [experiment-to-pattern-transition.md](governance/experiment-to-pattern-transition.md), [experimental-isolation-rules.md](governance/experimental-isolation-rules.md), [operational-lessons-and-postmortems.md](governance/operational-lessons-and-postmortems.md). Defines **human-reviewed** operational experimentation, evidence discipline, isolation from governance truth, and experiment→pattern transitions — **not** an automated experiment platform, **not** runtime proof, **not** orchestration.

**Reality audit framework (documentation):** Cross-cutting **human-operated** review semantics under `governance/` — start [reality-audit-framework.md](governance/reality-audit-framework.md); [reality-audit-questions.md](governance/reality-audit-questions.md), [operational-friction-semantics.md](governance/operational-friction-semantics.md), [deprecation-and-pruning-semantics.md](governance/deprecation-and-pruning-semantics.md), [governance-usefulness-review.md](governance/governance-usefulness-review.md), [reality-vs-mythology-warnings.md](governance/reality-vs-mythology-warnings.md). Supports **operational reality**, usefulness, friction, and drift reflection — **not** governance certification, **not** runtime validation, **not** telemetry or monitoring products.

## File operations
- Constrain filesystem work to **`C:\AI MARS`** for MARS work (canonical workspace root).
- **Bulk storage** for large out-of-git artefacts: **`C:\AI MARS STORAGE`** — supporting layer only; **not** a second repository or parallel workspace root. See [governance/mars-infrastructure-reality-v1.md](governance/mars-infrastructure-reality-v1.md).
- **No** delete or move without explicit user instruction.
- **No** manual edits to generated or build artifacts; ignore or regenerate via the proper pipeline.

## Commits
- **Default:** no commit and no push. **Do not** create commits unless the user explicitly requests.
- **GIT CHECKPOINT NEEDED** is **not** default: use only for major milestones (see `web-gpt-sources/04-workflows__git-rules.md`). In typical tasks, **omit** it.

## Task closeout
When a task is completed and reporting is required: list **changed files**, **summary**, **git status**, and **UNKNOWN** / **SECURITY RISK** if applicable. **GIT CHECKPOINT NEEDED** only when criteria in the git-rules doc are met; otherwise do not suggest git.
Every task report must start with a clear top-level heading: **`# REPORT — <task/stage name>`**.
