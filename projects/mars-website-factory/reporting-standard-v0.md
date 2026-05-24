# MARS Website Factory — Reporting Standard v0

**Status:** **documentation only** — normalized **REPORT** format for factory prompt runs. **Not** an executable schema, **not** a runtime log format, **not** evidence of automated reporting.

**Version:** v0.

**Related:** [prompt-standards-overview-v0.md](prompt-standards-overview-v0.md), [cursor-execution-standard-v0.md](cursor-execution-standard-v0.md), [agent-prompt-behavior-v0.md](agent-prompt-behavior-v0.md), [safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md), [qa-prompt-rules-v0.md](qa-prompt-rules-v0.md), [qa-result-payloads-v0.md](qa-result-payloads-v0.md), [`../../AGENTS.md`](../../AGENTS.md).

**RU commercial landings:** use [ru-landing-qa-preset-v1.md](ru-landing-qa-preset-v1.md). Frontend/QA REPORT **PASS is not complete** without `RU TYPOGRAPHY / NO WORD-SPLITTING` verification.

---

## 1. Purpose

Every factory prompt run produces a **REPORT**. The REPORT is:

- the **evidence** that the prompt executed honestly,
- the **handoff** to QA, HITL, and downstream stages,
- the **anchor** for SAFE UNKNOWN, risks, and exclusions.

A factory run **without** a REPORT is **invalid**. This standard defines the **prose structure** of the REPORT and its **lane variants**.

---

## 2. Canonical REPORT header

Every REPORT begins with:

```text
# REPORT — <task or stage name>
```

This matches `AGENTS.md` (§“Task closeout”) and the factory convention used in prompt-issuing tasks.

Examples:

- `# REPORT — Website Factory prompt standards layer`
- `# REPORT — blueprint draft for /roof-inspection-moscow`
- `# REPORT — frontend QA for fh_roof_inspection_moscow_v1`

---

## 3. Mandatory sections

The following sections are **required** in every REPORT (omit only with a SAFE UNKNOWN note explaining why):

| Section | Content |
|---------|---------|
| **Created files** | Full repo-relative paths of new files. |
| **Updated files** | Full repo-relative paths of modified files. |
| **Artifact changes** | `artifact_id`s (or contract anchors) that changed, with class names per [artifact-types-v0.md](artifact-types-v0.md). |
| **QA changes** | QA artifacts produced or amended (none if not applicable). |
| **SAFE UNKNOWN** | List of unknowns / bounded assumptions ([safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md)). |
| **Risks** | Open risks; link to [`../../governance/risk-register.md`](../../governance/risk-register.md) rows when applicable. |
| **Git status** | Output of `git status --short` after edits. |
| **Runtime exclusions** | Paths intentionally untouched (e.g. `mars-runtime/*`, `projects/seo-content-agent/integrations/*`). |
| **Push status** | `not requested` / `pushed to <remote>/<branch>` / `failed: <reason>`. |
| **Verification results** | Lint, build smoke, link check, viewport spot-check — only for steps actually performed. |

Optional sections (when applicable):

- **Commit hash** — if a commit was created.
- **HITL flags** — if HITL escalation is required.
- **Validator status** — planned / not invoked / out of scope.

---

## 4. REPORT variants by lane

### 4.1 Documentation REPORT

Used for: contract files, semantic models, overview docs, governance cross-link updates.

Required:

- Created files, Updated files, SAFE UNKNOWN, Git status, Runtime exclusions, Push status.

Recommended:

- Artifact changes (when a new artifact class is added).
- Verification results (link sanity, cross-reference check).

Forbidden:

- Build / deploy claims (documentation-only).

### 4.2 Frontend implementation REPORT

Used for: frontend source-first edits per [frontend-prompt-discipline-v0.md](frontend-prompt-discipline-v0.md).

Required:

- Created files, Updated files (under `src/...`), Artifact changes (frontend handoff anchor), Verification results (`gulp build` outcome if run; viewport spot-check if performed), SAFE UNKNOWN (CI, hosting, exact build command), Git status, Runtime exclusions, Push status.
- **RU commercial landings:** `RU TYPOGRAPHY / NO WORD-SPLITTING — PASS | partial | FAIL | SAFE UNKNOWN` per [ru-landing-qa-preset-v1.md](ru-landing-qa-preset-v1.md).

Forbidden:

- Hand-edits to `dist/`.
- RU commercial landing QA **PASS** without RU typography / no word-splitting verification.
- Claims of CI green without evidence ([safe-unknown-boundary.md](safe-unknown-boundary.md)).
- Claims of deploy.

### 4.3 QA REPORT

Used for: QA prompts ([qa-prompt-rules-v0.md](qa-prompt-rules-v0.md)).

Required:

- Subject artifact_id, Lane (Design / SEO / Conversion / Frontend / Validator), Categories, Findings (per [qa-result-payloads-v0.md](qa-result-payloads-v0.md) field vocabulary), Severity rollup, HITL flags, SAFE UNKNOWN list, Recommendation (pass / fail / conditional), Verification results.
- **RU commercial Frontend QA:** `RU TYPOGRAPHY / NO WORD-SPLITTING` line required for **pass** recommendation.

Forbidden:

- Auto-waiver of blockers (waivers require HITL).
- Frontend QA **pass** on RU commercial landings without RU typography verification.
- Severity inflation/deflation without evidence.
- “Pass with reservations” without enumerated findings.

### 4.4 Migration REPORT

Used for: moves between legacy and canonical packs (e.g. SEO Content Agent → MetaBOT), file renames, deprecations.

Required:

- Source paths, Destination paths, Mapping notes (one-to-one, merged, dropped), SAFE UNKNOWN for unverified equivalents, Runtime exclusions, Git status, Push status.

Forbidden:

- Silent deletions; deletions must be enumerated and justified.
- Cross-project rewrites under a migration label.

### 4.5 Validation REPORT

Used for: Final Validation stage (S13) and governance consistency checks ([website-factory-workflow-v0.md](website-factory-workflow-v0.md) §S13).

Required:

- Inputs reviewed, Cross-lane findings, Consistency outcome, go / no-go recommendation, HITL flags, SAFE UNKNOWN, Git status (if any changes), Push status.

Forbidden:

- “Go” without enumerated cross-lane evidence.
- Hidden waivers.

---

## 5. Section semantics

### 5.1 Created files

- Each path on its own line.
- Repo-relative, forward slashes preferred for cross-platform consistency.
- If a file class is new (e.g. new contract), call it out under **Artifact changes**.

### 5.2 Updated files

- Same conventions as Created files.
- If a file was touched only for cross-reference, note it as **cross-reference update** in a parenthetical.

### 5.3 Artifact changes

- For each change, list:
  - artifact class (per [artifact-types-v0.md](artifact-types-v0.md));
  - artifact_id (when stable);
  - status (draft / approved / superseded).

### 5.4 QA changes

- QA artifacts only.
- Production REPORTs that did not produce QA leave this section as `none`.

### 5.5 SAFE UNKNOWN

- Each entry **must** be:
  - bounded (what it covers, what it does not),
  - sourced (what is missing),
  - resolvable (what artifact or decision would close it).
- Each entry mirrors the rules in [safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md).

### 5.6 Risks

- Open risks introduced or surfaced by the run.
- Link to [`../../governance/risk-register.md`](../../governance/risk-register.md) rows when applicable.

### 5.7 Git status

- Verbatim output of `git status --short` post-edit.
- Must show the **same expected leftovers** the prompt declared (or fewer) — anything extra is a finding.

### 5.8 Runtime exclusions

- Paths the prompt explicitly did **not** touch:
  - `mars-runtime/*` (unless task targets it),
  - `projects/seo-content-agent/integrations/*` (leftover legacy bridge artifacts),
  - generated `dist/*` (per [frontend-prompt-discipline-v0.md](frontend-prompt-discipline-v0.md)),
  - secret files.

### 5.9 Push status

- `not requested` — default.
- `pushed to origin/main` (or named remote/branch) — if explicitly requested.
- `failed: <reason>` — if a push was attempted and failed.

### 5.10 Verification results

- Verification that was **actually performed** in this run.
- “Not performed” is acceptable when bounded by **SAFE UNKNOWN**.
- Fabricated verifications are forbidden ([agent-prompt-behavior-v0.md](agent-prompt-behavior-v0.md) §2.1).

---

## 6. Anti-patterns

| Anti-pattern | Why forbidden | Honest alternative |
|--------------|---------------|---------------------|
| REPORT missing | No evidence trail. | Always emit a REPORT, even for trivial edits. |
| “Looks good” verification | Fabrication. | Either run the check and report it, or SAFE UNKNOWN. |
| Hidden file changes | Violates §3 / §7 of [cursor-execution-standard-v0.md](cursor-execution-standard-v0.md). | Enumerate every changed path. |
| Auto-waiver in QA REPORT | Bypasses HITL. | Emit **NEED HUMAN APPROVAL**. |
| “Pushed quietly” | Violates git safety. | Push only when asked; record commit hash + remote/branch. |
| Cross-lane mixing | Confuses downstream consumers. | One lane per REPORT; cross-link sibling REPORTs. |

---

## 7. Cross-link to AGENTS.md

[`../../AGENTS.md`](../../AGENTS.md) §“Task closeout” already requires:

- changed files,
- summary,
- git status,
- UNKNOWN / SECURITY RISK callouts,
- explicit `# REPORT — <task>` heading,
- GIT CHECKPOINT NEEDED **only** when criteria in `web-gpt-sources/04-workflows__git-rules.md` are met.

This standard is a **factory-specific extension** of those rules: the same vocabulary, plus artifact / QA / runtime exclusions / verification lanes specific to Website Factory.

---

## 8. Non-claims

- This document does **not** ship a REPORT parser, log sink, or storage layer.
- It does **not** assert any future runtime persists REPORTs.
- It does **not** claim REPORTs are validated by automation.

---

## 9. Revision history

| Date | Change |
|------|--------|
| 2026-05-11 | **v0** — initial reporting standard for the Website Factory (documentation only). |
