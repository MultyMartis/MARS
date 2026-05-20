# 02 — Current operational state (migration v0)

**As-of:** snapshot for migration export generation. **Always re-verify** with `git status --short -uall` in the live repo.

---

## Active lanes (canonical)

From `governance/parallel-cursor-chat-work-mode-v0.md` (**Parallel Cursor Chat Work Mode v0**):

| Lane | Role | Typical paths |
|------|------|----------------|
| **Lane A** | Production execution | `workspaces/*`, client/project delivery docs, frontend sources, design assets tied to implementation |
| **Lane B** | MARS core | `governance/*`, `registry/*`, `agents/*`, `projects/mars-website-factory/*`, architecture/workflow docs per scope |
| **Runtime** | Explicit runtime-scoped work only | `mars-runtime/*` (adapters, tests) — **never** mix casually with production commits |

**Third lane** is **not** a second app — it is **discipline inside one repo**: classify paths before editing.

---

## Dirty tree classification (template from latest status)

**Runtime (`mars-runtime/*`):** modified adapter and test files (e.g. `mars-runtime/adapters/seo-content-agent-adapter.js`, `mars-runtime/runtime/run-seo-content-agent-test.js`) — treat as **Runtime lane** leftovers until reverted, stashed, or explicitly committed under a **runtime-only** commit.

**Production (`workspaces/*`, `projects/triumph-manipulator-landing/design/*`):** extensive **Triumph** landing changes under `workspaces/triumph-manipulator-landing/` (src, dist, svg, scss, partials); **untracked** design pack under `projects/triumph-manipulator-landing/design/` (`v1/`, `v2/`, `shared-assets/`, notes).

**Legacy leftovers (`projects/seo-content-agent/integrations/*`):** e.g. untracked `projects/seo-content-agent/integrations/n8n-mars-bridge-map-code.txt` — **legacy** tree; canonical MetaBOT docs live under `projects/metabot-seo-content-agent/` per governance.

**Also present (classify explicitly in each session):** large **untracked** tree under `shared/assets/icon-libraries/Font Awesome Pro 5.15.4/` — **production-adjacent shared assets** / licensing-sensitive; **not** in the three template lanes above: classify as **Production** or **UNKNOWN** until the operator decides ownership and commit lane.

**Total paths (approx.):** `git status --short -uall` line count was **~995** at export time (mostly untracked font library files).

---

## Parallel Cursor Chat Work Mode v0 (summary)

- One Cursor app, **one** working copy, **multiple** chats.  
- **Not** defined: chat memory isolation, automatic routing, queues.  
- **Is** defined: human naming, path scope, **forbidden cross-lane edits**, REPORT lane checks.

---

## Current git discipline

- Default: **no commit**, **no push** (`AGENTS.md`).  
- **Never** `git add .` / `git add -A` / `git commit -a` (`parallel-cursor-chat-work-mode-v0.md`).  
- Stage **explicit paths**; verify `git diff --cached --name-only` matches **one** commit lane.  
- **GIT CHECKPOINT NEEDED** only for rare milestones (`web-gpt-sources/04-workflows__git-rules.md`).

---

## Current operational priorities (from repo posture)

1. **Website Factory** — maintain doc coherence (workflow v0, runbook, validation **model**, templates).  
2. **Frontend operationalization** — Triumph workspace + **Frontend Gulp Agent** workflow in **Lane A**.  
3. **Triumph production lane** — landing implementation, handoffs, QA docs in `projects/triumph-manipulator-landing/`.

---

## Known leftovers / risks

- **Mixed lane dirt:** runtime + production + large vendor assets untracked → high risk of wrong-lane commit if not classified.  
- **Legacy vs canonical SEO:** do not extend `projects/seo-content-agent/` as canonical; use `projects/metabot-seo-content-agent/`.  
- **SAFE UNKNOWN:** whether `mars-runtime` adapter code matches live external endpoints.

---

## Operational continuity rule for new chat

On first message in the new chat: **re-run** `git status`, **state active lane**, **list forbidden paths** for that lane — do **not** assume a clean tree.
