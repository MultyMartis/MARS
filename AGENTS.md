# MARS — Agent instructions (AGENTS.md)

**Project:** MARS (Multi-Agent Runtime System)  
**Repository role:** main documentation / design source for Phase 1; **not** a proof of a running multi-agent system unless the tree contains real implementation.

## Non-negotiables
1. **Status honesty** — Never state that implementation (runtime, agents, adapters, RAG, orchestration) **exists** unless files in-repo demonstrate it.
2. **Three-way split** — When discussing design or roadmap, keep separate: **documented architecture** vs **planned implementation** vs **legacy imported** (e.g. Web-GPT pack) material.
3. **SAFE UNKNOWN** — If evidence is missing, say so clearly; do not fill gaps with assumptions.
4. **Locale** — Prefer **Russian** for user-facing explanations and project-facing docs when appropriate. Cursor/agent prompts may remain **English**.

## File operations
- Constrain filesystem work to **`D:\AI MARS`** for MARS work.
- **No** delete or move without explicit user instruction.
- **No** manual edits to generated or build artifacts; ignore or regenerate via the proper pipeline.

## Commits
- **Do not** create commits unless the user requests (checkpoint rules may ask for a signal instead).

## Task closeout
When a task is completed and reporting is required: list **changed files**, **summary**, **git status**, and **UNKNOWN** / **SECURITY RISK** / **GIT CHECKPOINT NEEDED** if applicable.
