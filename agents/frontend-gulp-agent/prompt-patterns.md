# Prompt patterns — Cursor (Gulp Frontend Agent)

Reusable **shapes** for frontend work. Replace `<TARGET_ROOT>`, `<HANDOFF_ID>`, and paths with real values. Keep prompts **one slice** per run when possible.

**Common footer for every pattern (append):**

- End with `# REPORT — <task>` per [`reporting.md`](reporting.md).
- State **git status** after edits; **Push status:** `not requested` unless told otherwise.
- List **Runtime exclusions** if any paths were intentionally untouched.

---

### 1. Audit target frontend project

| | |
|--|--|
| **Target folder** | `<TARGET_ROOT>` (open as workspace or subfolder). |
| **Agent mode** | Read-first / Ask if discovery only; Agent if cataloging files. |
| **Git safety** | No commits; no `git add .`; read `git status` if assessing cleanliness. |
| **Scope** | Map `src/` tree, build scripts, include pattern, SCSS entry, JS entry. |
| **Allowed files** | Read `package.json`, `gulpfile.*`, `README*`, `src/**` (read). |
| **Forbidden files** | Do not edit `dist/`; do not modify sources unless scope expands. |
| **QA** | N/A for read-only; note unverified scripts as **SAFE UNKNOWN**. |
| **REPORT** | Created/updated none; findings as lists; unknowns explicit. |

---

### 2. Implement one section

| | |
|--|--|
| **Target folder** | `<TARGET_ROOT>`. |
| **Agent mode** | Agent (edits allowed only under agreed `scope.in`). |
| **Git safety** | Stage nothing unless operator requests; never `git add .`. |
| **Scope** | Single `block_id` / one partial + SCSS (+ optional JS) per [`frontend-prompt-discipline-v0.md`](../../projects/mars-website-factory/frontend-prompt-discipline-v0.md). |
| **Allowed files** | Handoff-listed partials, SCSS partials, optional `src/js/modules/*`. |
| **Forbidden files** | `dist/*`, unrelated pages/sections, global tokens unless prompt allows. |
| **QA** | Run build if in scope; else **SAFE UNKNOWN** for build. |
| **REPORT** | §4.2 frontend lane — paths under `src/…`, verification results honest. |

---

### 3. Implement responsive fix

| | |
|--|--|
| **Target folder** | `<TARGET_ROOT>`. |
| **Agent mode** | Agent; minimal diff. |
| **Git safety** | Same as §2. |
| **Scope** | Breakpoint/overflow issue for named section only. |
| **Allowed files** | Named section SCSS + markup for that section if needed. |
| **Forbidden files** | Global resets unless handoff/HITL allows; no `dist/`. |
| **QA** | Spot-check viewports named in handoff **`responsive_rules`**. |
| **REPORT** | Include before/after summary; viewport notes; build if run. |

---

### 4. Add JS module

| | |
|--|--|
| **Target folder** | `<TARGET_ROOT>`. |
| **Agent mode** | Agent. |
| **Git safety** | Same as §2. |
| **Scope** | One behavior + **`data_attribute_hooks`** from handoff. |
| **Allowed files** | `src/js/modules/…`, entry init file if required by project. |
| **Forbidden files** | Inline script in HTML; new globals without note; `dist/`. |
| **QA** | Keyboard/focus checks if interactive; console clean on load. |
| **REPORT** | Hooks list; init path; tests performed. |

---

### 5. QA frontend build

| | |
|--|--|
| **Target folder** | `<TARGET_ROOT>`. |
| **Agent mode** | Agent or terminal-assisted. |
| **Git safety** | No unrelated file ops. |
| **Scope** | Run documented build + [`qa-checklist.md`](qa-checklist.md) subset. |
| **Allowed files** | Read-only except fixing **src** issues found by QA (if same prompt). |
| **Forbidden files** | `dist/` manual edits. |
| **QA** | Full checklist as timeboxed; failures enumerated. |
| **REPORT** | Treat as verification-heavy REPORT; recommendation pass/fail/conditional. |

---

### 6. Prepare report

| | |
|--|--|
| **Target folder** | N/A (prose only) or `<TARGET_ROOT>` for gathering paths. |
| **Agent mode** | Ask or Agent. |
| **Git safety** | Summarize `git status --short`; no staging. |
| **Scope** | Close a session after edits or audit. |
| **Allowed files** | N/A. |
| **Forbidden files** | N/A. |
| **QA** | N/A. |
| **REPORT** | Full [`reporting.md`](reporting.md) template + factory §4.2 fields. |

---

### 7. Safe checkpoint

| | |
|--|--|
| **Target folder** | `<TARGET_ROOT>`. |
| **Agent mode** | Human-led; Cursor may draft message only. |
| **Git safety** | **Only** after HITL: explicit `git add <paths>`; no `git add .`; no push unless requested. |
| **Scope** | Document intended commit scope in REPORT **before** commit. |
| **Allowed files** | Only approved paths. |
| **Forbidden files** | Secrets, `dist/`, unrelated refactors. |
| **QA** | Build + critical checklist green **or** risks accepted in writing. |
| **REPORT** | Include proposed commit summary; **Push status** explicit. |

---

## Preserved ideas (from legacy starter copy)

- Prefer **stable `data-*` hooks** over class-name-only coupling for behavior.
- **Progressive enhancement:** critical content not JS-gated; respect **`prefers-reduced-motion`** when adding motion.
- **Plugin discipline:** integrate only when needed; init from agreed entry; avoid fragile dynamic `import()` chains for **critical** UI without a verified load path.
