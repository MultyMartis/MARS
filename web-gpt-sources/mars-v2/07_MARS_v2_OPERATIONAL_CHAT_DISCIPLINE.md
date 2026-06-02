# MARS v2 — Operational chat discipline

**Status:** **CORE** / **OPERATIONAL**

---

## 1. PURPOSE

MARS v2 uses **multi-chat operational workflows**: role-separated chats, **lane isolation**, and **human-supervised orchestration**. Web-GPT plans and packages; Cursor/Codex executes on `C:\AI MARS`; the operator approves scope, git, and lane choice.

**Goal:** reduce **operational entropy** — prompt drift, markdown breakage, lane contamination, context collapse, and mythology leakage into execution.

**Rule:** one chat must **not** become a universal operational space. A single thread that mixes governance, runtime research, Factory methodology, frontend delivery, design generation, and validation increases failure rate and corrupts source priority.

**Post–Cycle 8:** default new chats to **operational delivery** (Factory / ORCA / Triumph / Frontend Production) — not **Governance** or **Validation** unless chartered. Governance chats are **maintenance mode**, not stabilization waves.

| Anti-pattern | Risk |
|--------------|------|
| Universal super-chat | Conflicting instructions, wrong-lane edits |
| Unlabeled chat | Scope creep, forbidden-path violations |
| Chat memory as SoT | Stale claims vs current repo |

---

## 2. CHAT TYPE SYSTEM

Every operational chat should declare **CHAT TYPE** at start (or in each task envelope). Chat type constrains **allowed scope**, **terminology**, **prompt style**, and **expected outputs**.

| Chat Type | Purpose |
| --------- | ------- |
| **Governance** | Architecture, governance phases, registry discipline, anti-drift |
| **Runtime Research** | `mars-runtime/` exploration only — boundary language, no product claims |
| **Website Factory** | Factory methodology, contracts, runbooks, pack discipline |
| **Frontend Production** | Implementation in workspaces / client project trees |
| **Design Production** | Visual generation, mockups, design-system alignment |
| **Validation** | Audits, review, reality checks, REPORT verification |
| **Migration** | Continuity, source-pack import, bootstrap hygiene |
| **External Systems** | MetaBOT, n8n, deploy hooks — outside MARS core claims |

**Chat type affects:**

| Dimension | Effect |
|-----------|--------|
| **Allowed scope** | Which paths and claim classes are in-bounds |
| **Terminology** | BOUNDARY ONLY vs OPERATIONAL vs PLANNED vs EXCLUDED |
| **Prompt style** | Planning density vs copy-safe execution prompts |
| **Expected outputs** | REPORT, audit table, prompt package, or doc delta only |

**Example declarations:**

- `CHAT TYPE: Governance` — may edit `governance/`, discuss S0–S7; must not implement Triumph landing HTML.
- `CHAT TYPE: Frontend Production` — may edit `workspaces/*`; must not rewrite governance truth.
- `CHAT TYPE: Runtime Research` — may read `mars-runtime/`; must not narrate shipped orchestration.

---

## 3. LANE SYSTEM

**Lanes** separate filesystem and commit risk in one repo (`C:\AI MARS`).

| Lane | Name | Typical scope |
|------|------|----------------|
| **Lane A** | Production delivery | `workspaces/*`, client `projects/<name>/*` (frontend/assets) |
| **Lane B** | MARS core | `governance/*`, `projects/mars-website-factory/*`, `agents/*`, `web-gpt-sources/mars-v2/*` |
| **Runtime lane** | R1 experiments only | `mars-runtime/` — narrow, explicit charter |

**Rule:** mixing lanes in **one execution batch** (one prompt → one REPORT cycle) increases operational risk. Prefer separate chats or explicit charter that names cross-lane intent and forbidden paths.

**Every operational chat should declare:**

```
ACTIVE LANE: A | B | Runtime
CHAT TYPE: <from section 2>
```

**Examples:**

| Declaration | Valid work |
|-------------|------------|
| `ACTIVE LANE: A` + `CHAT TYPE: Frontend Production` | Triumph workspace components, styles, assets policy |
| `ACTIVE LANE: B` + `CHAT TYPE: Governance` | Governance doc hygiene, registry wording |
| `ACTIVE LANE: Runtime` + `CHAT TYPE: Runtime Research` | Adapter experiment, README boundary check |
| `ACTIVE LANE: A` + `CHAT TYPE: Governance` | **Invalid** — wrong chat type for lane; re-scope or split chat |

**Wrong-lane work:** stop; escalate to operator; do not “fix forward” with broad semantic edits.

---

## 4. CONTEXT ISOLATION RULES

**One chat = one operational role** (primary). Secondary references are allowed; **execution** must stay in role.

| Chat role | Must not (default) |
|-----------|-------------------|
| Frontend Production | Redesign governance architecture; edit `governance/*` without charter |
| Governance | Drift into frontend implementation; edit `workspaces/*/src/**` |
| Runtime Research | Rewrite Website Factory contracts; claim production runtime |
| Design Production | Redefine execution model or runtime boundaries |
| Website Factory | Ship client landing code under guise of “methodology fix” |
| Validation | Expand scope into unchartered implementation |

**Why:** context isolation reduces **hallucination**, **lane contamination**, and **terminology drift** (e.g. PLANNED surfaces described as OPERATIONAL).

**Handoff pattern:** close chat A with REPORT → open chat B with lane/type declaration + fresh `git status` paste — do not assume B inherited A’s live tree state.

---

## 5. SOURCE PRIORITY MODEL

When instructions conflict, resolve in this order (highest wins):

| Priority | Source | Role |
|----------|--------|------|
| **P0** | `AGENTS.md` | Non-negotiable agent honesty, filesystem, git, REPORT |
| **P1** | MARS v2 source-pack (`web-gpt-sources/mars-v2/`) | Consolidated operational intelligence for Web-GPT |
| **P2** | Current repo docs | `governance/`, `README.md`, project indexes — authoritative detail |
| **P3** | Current task charter | User task message: scope, forbidden paths, commit intent |
| **P4** | Active repo evidence | Files on disk, `git status`, command output pasted by user |
| **P5** | Old chats / exports / snapshots | **Historical** — continuity only; re-verify before claims |

**Rule:** historical chats are **not** automatic source-of-truth. A prior REPORT may be wrong after another session edited the tree.

**SAFE UNKNOWN:** if P4 is missing, state unknown; do not upgrade P5 to P0.

---

## 6. CURSOR PROMPT FORMAT STANDARD

**CRITICAL:** prompts sent to Cursor/Codex must be **copy-safe**. Metadata stays **outside** the copy block; the prompt body is **plain text** suitable for one-click paste.

### Correct pattern (structure)

**Outside copy block (metadata — not pasted into agent body):**

📁 Target folder:
C:\AI MARS

🤖 Режим агента:
AGENT

ACTIVE LANE: A
CHAT TYPE: Frontend Production

**Copy-safe prompt body (inside a single fenced block for the human operator only — the body itself contains NO nested fences):**

    TASK — <short name>

    GOAL
    <one paragraph>

    SCOPE
    - allowed paths
  ...

When packaging for the user: provide **one** outer fence for the operator to copy **only the inner plain text**, or deliver the body as unformatted text after metadata lines.

### Forbidden in prompt bodies

| Forbidden | Why |
|-----------|-----|
| Nested markdown fences | Breaks copy; agent sees truncated instructions |
| Triple-backtick blocks inside prompts | Same |
| ` ```text ` … ` ``` ` wrappers inside body | Nesting corruption |
| Markdown-broken nesting | Partial execution, dropped sections |
| Giant markdown tables in prompts | Renderer breakage; hard to diff |
| Bash-style HEREDOC wrapping for operational prompts | Unnecessary; error-prone on Windows paste |

### Required in prompt bodies (when execution-bound)

- Explicit **forbidden paths**
- **ACTIVE LANE** and **CHAT TYPE** (or reference to charter)
- **Do NOT** list (commit policy, vendor exclusions, etc.)
- Single **REPORT** requirement if deliverable expected

**Clarification:** the prompt body is a **clean plain-text copy target**. Formatting discipline is operational infrastructure, not aesthetics.

---

## 7. PROMPT HYGIENE RULES

Prompt quality directly affects execution stability.

| Rule | Detail |
|------|--------|
| **Short sections** | Prefer labeled blocks (GOAL, SCOPE, DO NOT, OUTPUT) over prose walls |
| **Explicit forbidden paths** | Per lane: e.g. no `governance/*`, no `mars-runtime/**/*.js` as pack proof |
| **Explicit exclusions** | Vendor trees, `dist/`, wrong workspace — state once |
| **No mega-prompts by default** | Split governance vs implementation; split runtime vs delivery |
| **No duplicated instructions** | Repeating git rules three times creates contradictions |
| **No conflicting instructions** | Resolve against P0–P3 before send |
| **Dense operational wording** | Imperatives, paths, booleans — not narrative filler |
| **Separate concerns** | Governance chat packages policy; production chat packages files |
| **Runtime isolation** | Runtime research prompts must include BOUNDARY ONLY language |
| **Commit intent** | State “no commit unless asked” unless user explicitly orders commit |

**Mega-prompt exception:** only when user explicitly charters a large bounded migration — still require lane, forbidden paths, and REPORT.

---

## 8. REPORT FORMAT STANDARD

**REPORT** is the operational **closure mechanism** after execution (Cursor/Codex) or doc tasks when deliverable is required.

### Canonical shape

```
# REPORT — <task name>

## 1. What was done
<concise factual summary>

## 2. Files affected
- path
- path

## 3. SAFE UNKNOWN
<what was not verified; what would verify it — or "none">

## 4. Risks
<lane drift, partial work, git posture, security — or "none">

## 5. Next step
<single recommended operator action — or "none">
```

**Also include when applicable (per `AGENTS.md`):** git status summary, **SECURITY RISK**, explicit **no commit performed**.

**Not a REPORT:** motivational summary, architecture essay, or restating the entire prompt. REPORT closes **this** task batch.

---

## 9. REPO REALITY CHECKS

New chats have **zero** live repo awareness. Before major work or lane-sensitive edits:

### Required command (operator paste)

```
git status --short -uall
```

### Required declarations (chat or prompt metadata)

| Check | Question answered |
|-------|-------------------|
| **Lane declaration** | A / B / Runtime |
| **Scope declaration** | Allowed paths + task name |
| **Forbidden paths** | Explicit negatives |
| **Commit intent** | No commit / commit when done / checkpoint later |

**Clarify:** do not claim clean tree, merged branch, or “already fixed in repo” without P4 evidence in **this** chat.

**Pre-flight for cross-chat handoff:** prior REPORT + fresh `git status` + re-read P0–P2 for task type.

---

## 10. OPERATIONAL ANTI-CHAOS RULES

Summary discipline for all MARS v2 operational chats:

| Rule | Enforcement |
|------|-------------|
| **Stabilization before expansion** | Fix lane and scope before new features |
| **No fake runtime** | No schedulers, queues, or “MARS enforced” without file proof |
| **No hidden orchestration claims** | Human-supervised only; external systems named explicitly |
| **No giant rewrites without charter** | Scope explosion = stop and re-charter |
| **No cross-lane contamination** | One primary lane per batch |
| **No universal super-chat** | Split by CHAT TYPE |
| **No assumed prior context** | Re-verify git and files |
| **SAFE UNKNOWN over hallucination** | Missing evidence → unknown, not invention |
| **No vendor/pack pollution** | Font Awesome Pro, `dist/`, migration snapshots ≠ SoT |
| **Report normalization** | One REPORT format; operational closure |

**Operator default:** when chaos detected — pause execution, restate ACTIVE LANE + CHAT TYPE + source priority, request fresh `git status`, shrink prompt.

---

## Cross-references

| Topic | Pack file |
|-------|-----------|
| Project behavior | `00_MARS_v2_PROJECT_BEHAVIOR.md` |
| Execution loop | `02_MARS_v2_EXECUTION_MODEL.md` |
| Evidence / mythology | `03_MARS_v2_REALITY_AND_BOUNDARIES.md` |
| Bootstrap | `06_MARS_v2_BOOTSTRAP_AND_MIGRATION.md` |

*This file does not modify in-repo `governance/` — it extends the MARS v2 Web-GPT source-pack only.*
