# Forge WordPress Git Workflow v1

**Document type:** Git discipline for Forge WordPress implementation  
**Version:** v1  
**Stage:** FW-04

**Does not override global MARS git policy** — extends it for WordPress project work.

**Production checkpoint (2026-08-18):** dirty shared monorepo + clean worktree + exact-file staging — [FORGE-WORDPRESS-GIT-SOP-v1.md](../../runbooks/FORGE-WORDPRESS-GIT-SOP-v1.md). Never `git add .` / reset / stash / clean.

---

## Preflight status

Before any implementation task:

1. Record `git branch --show-current`
2. Record `git status --short` for awareness
3. Identify unrelated WIP — **do not stage**

---

## Selective scope

- Stage **only** files within declared allowed write scope
- Never stage unrelated projects, credentials, or recovery temp
- Never stage WordPress core, vendor, uploads, or DB dumps unless explicitly chartered

---

## Branch / worktree recommendation

For project implementation:

| Approach | When |
|----------|------|
| **Isolated branch** | Default for multi-session implementation |
| **Git worktree** | When parallel frontend + WordPress work on same repo |
| **Main branch** | **Discouraged** for implementation — operator decision only |

Branch naming suggestion: `forge-wp/<project-slug>/<stage>` — operator may override.

---

## Commit policy

| Rule | Value |
|------|-------|
| Automatic commit | **Forbidden** by default |
| Operator-approved checkpoint | Required for milestone commits |
| Commit message | Operator-provided or task-specified |
| Push | Only when operator explicitly requests |

FW-04 and typical capability tasks: **report git status; do not commit**.

---

## Exclusions (never commit)

| Artifact | Reason |
|----------|--------|
| `.env`, credentials, API keys | Security |
| `wp-config.php` with secrets | Security |
| `node_modules/`, vendor | Generated |
| WordPress core | Not project code |
| `uploads/` | Media — not source |
| Database dumps | Data boundary |
| Build caches | Generated |
| `.recovery-temp/` | Not authority |
| Validation screenshots (large binaries) | Optional — operator policy |

---

## Release tag policy

- Release tags are **operator-applied** after validation pass
- Suggested pattern: `forge-wp/<project-slug>/rc-<n>` — not automatic
- Tag only validated release manifest scope

---

## Checkpoint pattern (operator-initiated)

```text
1. git status — verify selective scope
2. git add <explicit paths only>
3. git diff --cached — operator review
4. git commit -m "<operator message>"
5. git push — only if authorized
```

---

## Related

- [FORGE-WORDPRESS-FILESYSTEM-SCOPE-CONTRACT-v1.md](FORGE-WORDPRESS-FILESYSTEM-SCOPE-CONTRACT-v1.md)
- [../../FORGE-WORDPRESS-REPOSITORY-AND-FILESYSTEM-MODEL-v1.md](../../FORGE-WORDPRESS-REPOSITORY-AND-FILESYSTEM-MODEL-v1.md)
- [../../../../web-gpt-sources/04-workflows__git-rules.md](../../../../web-gpt-sources/04-workflows__git-rules.md)

---

*Git workflow v1 — human-operated checkpoints only.*
