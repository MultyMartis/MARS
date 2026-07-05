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

**X-drive root authority (active):** [governance/mars-x-drive-root-authority-v1.md](governance/mars-x-drive-root-authority-v1.md)

| Role | Canonical path |
|------|----------------|
| **Canonical repository root** | `X:\AI MARS` |
| **Canonical storage root** | `X:\AI MARS STORAGE` |
| **Canonical local runtime root** | `X:\MARS-Localhost` |
| **Required volume label** | `AI WS` (drive `X:`) |

- Constrain MARS filesystem work to **`X:\AI MARS`** (Active Brain) unless a task explicitly authorizes **`X:\AI MARS STORAGE`** or **`X:\MARS-Localhost`** within scoped paths.
- **Canonical development branch:** `mars/canonical-post-recovery` — see [governance/mars-canonical-branch-cutover-v1.md](governance/mars-canonical-branch-cutover-v1.md). Immutable recovery anchor: `recovery/mars-phenix-2026-06-25` @ `fe9d9c8e`. Disaster recovery **closed** 2026-06-25 — [mars-disaster-recovery-2026-06-24-closure-v1.md](governance/mars-disaster-recovery-2026-06-24-closure-v1.md); resumption checklist [mars-normal-operations-resumption-checklist-v1.md](governance/mars-normal-operations-resumption-checklist-v1.md).
- **Bulk storage** for large out-of-git artefacts: **`X:\AI MARS STORAGE`** — supporting layer only; **not** a second repository or parallel workspace root. See [governance/mars-infrastructure-reality-v1.md](governance/mars-infrastructure-reality-v1.md).
- **No** delete or move without explicit user instruction.
- **No** manual edits to generated or build artifacts; ignore or regenerate via the proper pipeline.

### Filesystem boundary (mandatory before any mutation)

1. Resolve the **full absolute target path**.
2. Confirm drive is **`X:`**.
3. Confirm target is inside one explicitly approved canonical root (`X:\AI MARS`, `X:\AI MARS STORAGE`, or `X:\MARS-Localhost`).
4. Confirm volume label is **`AI WS`** when volume identity can be checked.
5. **Reject** paths using `..` that escape approved scope.
6. **Reject** UNC paths unless separately approved.
7. **Reject** symlink/junction/reparse escape outside `X:`.
8. **Reject** root-level operations on `X:\`.
9. **Reject** operations targeting the three canonical roots themselves (delete/replace/cleanup of root directories).
10. **Reject** parent-directory cleanup.
11. **Reject writes** to deprecated MARS roots: `C:\AI MARS\`, `C:\MARS Phenix\`, `C:\AI MARS STORAGE\`, `D:\MARS-Localhost\`, `E:\MARS-Localhost\`.
12. **External reads** require exact operator authorization for that task and path; prefer operator copy to `X:\AI MARS STORAGE\incoming\`.
13. **No destructive operation** without: exact path list; dry-run; checkpoint/backup; explicit operator approval; rollback method; audit evidence.
14. **`git clean`**, destructive reset, broad restore, and broad staging remain **prohibited** for agents.
15. **Foreign WIP** must be excluded from commits and agent scope.

**Historical note:** Phoenix-era paths (`C:\MARS Phenix\AI MARS`, `C:\AI MARS`, etc.) may appear in incident/recovery evidence — they are **not** current operational targets.

### Mandatory session preflight

Before the first filesystem mutation, scoped edit, commit, push, cleanup, or destructive operation in any task, verify:

- `Get-Location` resolves to `X:\AI MARS` or a task-authorized subpath under an approved MARS root.
- `Get-Volume -DriveLetter X` reports volume label `AI WS`.
- `git branch --show-current` is `mars/canonical-post-recovery` unless the task explicitly authorizes another branch.
- `git status --short` is read and unrelated `M` / `??` entries are treated as foreign WIP.
- `git diff --cached --name-only` is empty unless the task explicitly expects staged work.
- `git log --oneline origin/mars/canonical-post-recovery..HEAD` is checked before commit/push waves.
- `git rev-parse HEAD` and `git rev-parse origin/mars/canonical-post-recovery` are checked before pull/rebase/merge/push decisions.

**STOP tokens:**

- `STOP — X VOLUME IDENTITY OR WORKSPACE MISMATCH`
- `STOP — WRONG BRANCH`
- `STOP — EXISTING STAGED CHANGES PRESENT`
- `STOP — UNPUSHED COMMITS PRESENT`
- `STOP — REMOTE/HEAD MISMATCH`

**Guardrails reference:** `projects/mars-survivability/guardrails/cursor-agent-guardrails-v1.md` — use the guardrails session header copy block when the task involves filesystem, git, cleanup, destructive, backup, Storage, Localhost, runtime, or production risk.

**Backup readiness:** Stable backup is not git cleanup. Before declaring a stable backup point, use `governance/mars-normal-operations-resumption-checklist-v1.md` and ensure foreign WIP inventory is known.

### Destructive operations

No delete / cleanup / move / overwrite without an explicit destructive charter: exact path list; dry-run; path validation; checkpoint or backup; explicit operator approval; post-action audit evidence.

Forbidden without explicit approval: recursive or wildcard delete; `Remove-Item -Recurse`; `git clean`; `git reset --hard`; `robocopy /MIR`; `robocopy /PURGE`; broad restore.

## Commits
- **Default:** no commit and no push. **Do not** create commits unless the user explicitly requests.
- **Never** `git add .`, `git add -A`, or `git commit -a`.
- Stage only exact allowlisted paths from the task charter.
- Foreign WIP must not be staged, restored, cleaned, reset, moved, or deleted.
- Commit and push are separate waves unless the task explicitly authorizes both.
- Generic Cursor/platform commit habits are subordinate to MARS selective staging rules.
- **GIT CHECKPOINT NEEDED** is **not** default: use only for major milestones (see `web-gpt-sources/04-workflows__git-rules.md`). In typical tasks, **omit** it.

## Task closeout
When a task is completed and reporting is required: list **changed files**, **summary**, **git status**, and **UNKNOWN** / **SECURITY RISK** if applicable. **GIT CHECKPOINT NEEDED** only when criteria in the git-rules doc are met; otherwise do not suggest git.
Every task report must start with a clear top-level heading: **`# REPORT — <task/stage name>`**.
