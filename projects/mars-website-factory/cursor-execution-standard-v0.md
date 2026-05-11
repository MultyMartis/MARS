# MARS Website Factory — Cursor Execution Standard v0

**Status:** **documentation only** — how factory prompts are **executed in Cursor** under human supervision in Phase 1. **Not** a Cursor extension, **not** a daemon, **not** an automation engine, **not** evidence that Cursor enforces any of these rules by itself.

**Version:** v0.

**Related:** [prompt-standards-overview-v0.md](prompt-standards-overview-v0.md), [prompt-structure-standard-v0.md](prompt-structure-standard-v0.md), [agent-prompt-behavior-v0.md](agent-prompt-behavior-v0.md), [reporting-standard-v0.md](reporting-standard-v0.md), [frontend-prompt-discipline-v0.md](frontend-prompt-discipline-v0.md), [website-factory-workflow-v0.md](website-factory-workflow-v0.md), [`../../governance/execution-model.md`](../../governance/execution-model.md), [frontend-production-model.md](frontend-production-model.md), [`../../AGENTS.md`](../../AGENTS.md), [`../../mars-runtime/execution-bridge-v0.md`](../../mars-runtime/execution-bridge-v0.md).

---

## 1. Purpose

Phase 1 execution of the Website Factory happens **in Cursor**, under **human supervision** ([`../../governance/execution-model.md`](../../governance/execution-model.md)). This standard defines how a structured prompt is **executed and reported** without crossing the documentation-only boundary.

The standard binds three pieces:

1. **Prompt** structure ([prompt-structure-standard-v0.md](prompt-structure-standard-v0.md)).
2. **Execution loop** inside Cursor (this document).
3. **REPORT** structure ([reporting-standard-v0.md](reporting-standard-v0.md)).

---

## 2. The prompt → execute → report loop

```text
prompt (structured)
     │
     ▼
target folder block         (where files may change)
     │
     ▼
agent mode block            (AGENT vs ASK)
     │
     ▼
git safety rules            (status pre-check, no `git add .`)
     │
     ▼
execution                   (file edits, read tools, lint checks)
     │
     ▼
verification                (re-read, lint, build smoke if applicable)
     │
     ▼
REPORT                      (created / updated / SAFE UNKNOWN / git status)
     │
     ▼
HITL / next prompt
```

This loop maps to the legacy operational shorthand **prompt → execute → report** ([workflow-map.md](workflow-map.md) §“Prompt → execute → report”) and to the richer MARS chain `prompt → task → plan → route → execute → validate → report → log` ([`../../workflows/execution-flow.md`](../../workflows/execution-flow.md)) — but **without** claiming the richer chain is automated in this repo.

---

## 3. Target folder block

Every factory prompt names a **target folder block** — the set of paths the prompt is allowed to read or modify.

Rules:

- Target paths are **explicit**: `projects/mars-website-factory/...`, `agents/cards/...`, `governance/...`.
- A prompt **without** a target folder block is **incomplete** — the agent must refuse or request one.
- Forbidden zones (e.g. `mars-runtime/*`, generated `dist/`) must be **named** when relevant ([frontend-prompt-discipline-v0.md](frontend-prompt-discipline-v0.md)).
- Cross-folder edits require a **STRUCTURE CHANGE** flag if not anchored in the prompt.

The target folder block is the **filesystem expression of `scope.in` / `scope.out`** ([prompt-structure-standard-v0.md](prompt-structure-standard-v0.md) §2.3).

---

## 4. Agent mode block

Every prompt names an **agent mode**:

| Mode | When to use | Constraints |
|------|-------------|-------------|
| **AGENT** | Direct file edits, multi-step tasks, contract drafting. | Honors target folder block, git safety, REPORT discipline. |
| **ASK** | Read-only exploration, design Q&A, audit pre-checks. | No file edits; no git operations. |

Notes:

- If the prompt does not name a mode, default to the **safer** mode (ASK).
- Switching modes mid-execution requires a **REPORT** entry and (where scope changes) a HITL escalation.

This block is the operational expression of the agent’s behavioral rules ([agent-prompt-behavior-v0.md](agent-prompt-behavior-v0.md)).

---

## 5. Git safety rules

Default posture for factory tasks: **no commits, no pushes** unless the prompt explicitly asks for them, per [`../../AGENTS.md`](../../AGENTS.md).

Mandatory checks before any file change in AGENT mode:

1. **Pre-check** — run `git status --short` and capture the output.
2. **Expected leftovers** — the prompt must enumerate leftover paths that are acceptable (e.g. runtime experiments in `mars-runtime/*` or in-flight integration drafts).
3. **Hard stop** — if unexpected paths appear, **STOP** and emit **NEED HUMAN APPROVAL**; do not proceed.
4. **No `git add .`** — staging must be **explicit per path**.
5. **No silent commits** — commits require explicit ask.
6. **No silent pushes** — pushes require explicit ask.
7. **No `--no-verify`** unless the prompt explicitly requests it.

If a commit is requested:

- Stage **only** the paths produced by this prompt.
- Use a commit message that names the artifact class (e.g. “MARS Website Factory prompt standards layer v0”).
- Run `git status` post-commit and include it in the REPORT.

If a push is requested:

- Push to the named remote/branch only.
- Record commit hash and push status in the REPORT.

---

## 6. REPORT structure

Every prompt run produces a **REPORT** ([reporting-standard-v0.md](reporting-standard-v0.md)) starting with the heading:

```text
# REPORT — <task or stage name>
```

Mandatory sections (subset; full list in the reporting standard):

- **Created files**
- **Updated files**
- **Artifact changes** (artifact_id and class)
- **QA changes** (if any)
- **SAFE UNKNOWN** notes
- **Risks**
- **Git status** (post-edit)
- **Runtime exclusions** (paths intentionally left untouched, e.g. `mars-runtime/*`)
- **Push status** (only if a push happened; otherwise “not requested”)
- **Verification results** (lint, build smoke, link check — only if performed)

A run without a REPORT is **not** a valid factory execution.

---

## 7. No silent file changes

- Every changed path is listed in the REPORT.
- Edits outside the target folder block are forbidden without an explicit scope change.
- “Helpful” formatting passes, lint-fix waves, or import reordering across other files are **uncontrolled expansion** ([agent-prompt-behavior-v0.md](agent-prompt-behavior-v0.md) §2.9).
- If the editor or linter rewrote a file (e.g. EOL normalization), call it out under **SAFE UNKNOWN** or **Verification results**.

---

## 8. No hidden staging

- Staging must be **explicit per path**: `git add path1 path2 ...`.
- `git add .`, `git add -A`, `git add -u` are **forbidden** by default.
- Pre-existing leftover paths (e.g. `mars-runtime/adapters/...`, `mars-runtime/runtime/...`, `projects/seo-content-agent/integrations/...`) must **never** be staged unless the prompt explicitly targets them.

If the runtime status drift surfaces during a factory prompt:

- emit **SAFE UNKNOWN** in the REPORT,
- do **not** “tidy” runtime files,
- escalate to the human operator.

---

## 9. No fake “done”

“Done” for a factory prompt means **all** of:

1. Produced artifacts match the named contract ([prompt-structure-standard-v0.md](prompt-structure-standard-v0.md) §2.8).
2. REPORT lists created/updated files, SAFE UNKNOWN, risks, git status.
3. Runtime exclusions are explicit.
4. Downstream QA / HITL is **not preempted** (no auto-approval, no auto-waiver).
5. Honesty rules are observed: no fake CI green, no fake deploy claim, no fake automation claim.

Anything less is **draft** or **partial** and must be reported as such.

---

## 10. Verification expectations

Verification depends on what was produced:

| Artifact class | Verification (Phase 1, human-supervised) |
|----------------|-------------------------------------------|
| Markdown documentation | Link references resolve; cross-doc consistency; lint pass for editor-applied rules. |
| Page Blueprint document | Contract fields present per [page-blueprint-contract-v0.md](page-blueprint-contract-v0.md); IDs cross-referenced with IA. |
| Design / Frontend handoff | Required fields present per contract; SAFE UNKNOWN for export tooling. |
| Frontend source | `gulp build` (or agreed task) runs locally **if** the local environment supports it; otherwise SAFE UNKNOWN. |
| QA report | Categories, evidence, severity, waiver flags, HITL flags filled. |
| Approval artifact | HITL signed record — agent **never** produces this alone. |

Verification that requires CI, deploy, or external services is **SAFE UNKNOWN** until those exist ([safe-unknown-boundary.md](safe-unknown-boundary.md)).

---

## 11. Checkpoint philosophy

Per [`../../AGENTS.md`](../../AGENTS.md):

- **GIT CHECKPOINT NEEDED** is **not default**.
- Use it **only** for major milestones (full prompt-standards layer added, full registry layer added, etc.) per `web-gpt-sources/04-workflows__git-rules.md`.
- Most factory tasks finish without a checkpoint suggestion.
- A checkpoint is **never** silent: it is an explicit ask, an explicit commit, an explicit REPORT entry.

---

## 12. Documentation vs runtime boundaries

Cursor’s role in the factory is to:

- read and write **documentation, contracts, and source-first frontend files**;
- run **local build commands** when requested and supported;
- emit honest REPORTs.

Cursor’s role is **not** to:

- run a MARS daemon;
- dispatch to specialist agents automatically;
- bind tasks to a Control Plane;
- substitute for HITL.

The future **Execution Bridge** ([`../../mars-runtime/execution-bridge-v0.md`](../../mars-runtime/execution-bridge-v0.md)) **may** wire Cursor prompt bundles to richer task lifecycles. Until that exists, Cursor remains a **prompt-driven** surface ([safe-unknown-boundary.md](safe-unknown-boundary.md)).

---

## 13. Tie to existing MARS execution model

| Concept in this standard | Anchor in MARS |
|---------------------------|----------------|
| prompt → execute → report loop | [`../../workflows/execution-flow.md`](../../workflows/execution-flow.md) (subset) |
| Target folder block | [`../../AGENTS.md`](../../AGENTS.md) “File operations” |
| Agent mode block | Cursor AGENT/ASK conventions; [agent-map.md](agent-map.md) |
| Git safety | [`../../AGENTS.md`](../../AGENTS.md) “Commits” + `web-gpt-sources/04-workflows__git-rules.md` |
| REPORT discipline | [`../../AGENTS.md`](../../AGENTS.md) “Task closeout” + [reporting-standard-v0.md](reporting-standard-v0.md) |
| Documentation vs runtime | [`../../governance/execution-model.md`](../../governance/execution-model.md), [safe-unknown-boundary.md](safe-unknown-boundary.md) |

---

## 14. Tie to Website Factory frontend production and Gulp Frontend Agent

- Frontend execution prompts run **inside Cursor** today; the **Gulp Frontend Agent** is a **legacy-bridge documented role** ([agent-map.md](agent-map.md), [frontend-production-model.md](frontend-production-model.md)), not an automated process in this repo.
- Frontend-specific Cursor expectations are in [frontend-prompt-discipline-v0.md](frontend-prompt-discipline-v0.md): source-first edits, modular SCSS, no `dist/` patches, data-attribute hooks, scoped JS.
- Build success in Cursor is **local** and **human-supervised**; CI status is **SAFE UNKNOWN** unless explicit evidence exists.

---

## 15. Non-claims (explicit)

This standard does **not** imply:

- a Cursor extension or daemon enforces these rules,
- factory agents exist as live processes,
- Cursor automatically routes prompts between stages,
- Cursor binds artifacts to a Control Plane,
- any HITL gate can be satisfied by Cursor without a human.

It **does** imply:

- the human operating Cursor is the executor;
- they are responsible for prompt structure, target folder block, git safety, REPORT discipline, and HITL escalation;
- everything else is **SAFE UNKNOWN** until governance documents say otherwise.

---

## 16. Revision history

| Date | Change |
|------|--------|
| 2026-05-11 | **v0** — initial Cursor execution standard for the Website Factory (documentation only). |
