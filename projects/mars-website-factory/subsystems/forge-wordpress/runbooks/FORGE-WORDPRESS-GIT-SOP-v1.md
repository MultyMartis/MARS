# Forge WordPress — Git SOP v1

**ID:** FW-RB-04  
**Status:** ACTIVE  
**Date:** 2026-08-18  
**Extends:** [FORGE-WORDPRESS-GIT-WORKFLOW-v1](../capability/protocols/FORGE-WORDPRESS-GIT-WORKFLOW-v1.md)  
**Does not override** MARS `.cursorrules` / AGENTS.md  
**Evidence:** FP-0002 P14+ clean-worktree checkpoints

---

## Model

- One MARS monorepo  
- Dirty main is **expected**  
- Foreign WIP is **out of scope**  
- Checkpoints: **clean worktree** from `origin/mars/canonical-post-recovery` (or task-authorized branch)  
- Stage **exact paths only**  
- Secret scan required  
- Commit and push are **separate** unless the task authorizes both  
- Never: `git add .` / `-A` / `commit -a` / reset / stash / clean / broad pull on dirty main  

If local HEAD is **ahead** of origin with unrelated commits: do **not** push them to ship WP Forge docs. Use a worktree based on **origin**, cherry-pick/copy allowlisted files, push **fast-forward** from origin.

---

## Production code checkpoints

Same as docs: allowlist theme/plugin/ACF/docs; exclude tokens, Storage, runtime data, client credentials, INCOMING binaries unless chartered.

---

*FW-RB-04 v1.*
