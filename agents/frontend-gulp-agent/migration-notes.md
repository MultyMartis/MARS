# Migration notes — `agents/frontend-gulp-agent/`

## History

This folder **previously contained a full copied gulp-starter** repository (nested **`.git`**, **`node_modules`**, **`dist`**, **`src`**, **`package.json`**, **`package-lock.json`**, **`gulpfile.js`**, **`.codex`**, **`.cursorrules`**, and starter docs). That layout was **accidental** relative to MARS: an agent pack must not vendor a runnable starter, dependencies, generated output, or production source.

## Sanitization (operational doc pack)

The following were **removed from the MARS agent pack** to restore a documentation-only boundary:

- Nested `.git/`
- `node_modules/`
- `dist/`
- `src/`
- `package.json`, `package-lock.json`, `gulpfile.js`
- `.codex/`, `.cursorrules`

Starter-only root files that were **not** part of the declared pack manifest (`AGENTS.md` gulp-starter copy, `.gitignore`, empty or starter `docs/`) were also removed to avoid confusion with repository-level [`AGENTS.md`](../../AGENTS.md) and to keep the folder limited to **operational documentation**.

## Where the runnable project lives

A **real** gulp-starter (or successor stack) should live in a **dedicated project repository** or **operator workspace** outside this pack, versioned and built on its own lifecycle.

## Current state

This directory is now **operational documentation only** for **`gulp_frontend_agent`**: [`README.md`](README.md), [`AGENT.md`](AGENT.md), workflow/rules/checklists, and [`prompts/`](prompts/) / [`examples/`](examples/) placeholders for future curated snippets.

---

*No runtime enforcement — documentation only.*
