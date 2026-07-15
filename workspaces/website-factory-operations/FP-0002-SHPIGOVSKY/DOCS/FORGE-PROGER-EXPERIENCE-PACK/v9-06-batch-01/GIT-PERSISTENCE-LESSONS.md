# Git / Persistence Lessons — MARS Monorepo (FP-0002)

**Status:** experience documentation only

---

## Model

- One Git repository: `X:\AI MARS`
- Canonical branch: `mars/canonical-post-recovery`
- Many projects share history (FP-0002, MetaBOT, OCPilot, etc.)
- Foreign WIP constantly present — **must not** be staged, restored, cleaned, or reset casually

---

## Hard rules (as practiced)

1. Exact path staging only — `git add -- <paths>`
2. **Never** `git add .` / `git add -A` / `git commit -a`
3. No reset/clean/stash of dirty main to “make push easy”
4. No force push
5. Commit and push are separate waves unless charter says otherwise
6. Base commit for gates = **ancestor**, not necessarily HEAD equality
7. Read `git ls-remote` before push; confirm remote tip ancestry
8. If remote tip is not ancestor → clean worktree merge method
9. If merge conflicts → STOP and report
10. Watch postcommit evidence tail loops — include evidence in allowlist when possible

---

## Clean worktree divergence resolve (proven pattern)

When remote advanced with other project commits:

```text
git ls-remote origin mars/canonical-post-recovery
→ remote_hash
git merge-base --is-ancestor remote_hash HEAD
→ if NO:
   git worktree add <clean-path> remote_hash
   (in worktree) git merge <local-commit-or-HEAD>
   if conflicts → STOP
   else git push origin HEAD:mars/canonical-post-recovery
   verify remote tip
   remove worktree
```

Never mutate dirty main with pull/rebase for this purpose.

---

## What went well

- E38–E51 large selective persistence without foreign WIP contamination
- Divergence resolve merge published FP-0002 commits without force
- Freeze-before-persist culture kept runtime safe during Git chaos

---

## What should be automated later (not now)

- Ahead-commit path classifier (fp0002 vs metabot vs ocpilot)
- Ancestry push gate script
- Allowlist generator from freeze manifests
- Postcommit evidence bundling checklist

These remain **helpers ideas** — not shipped orchestration.
