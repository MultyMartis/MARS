# WordPress Project Closeout and Freeze Pattern (from E63)

**Reusable release pattern** for Forge Proger WordPress projects in the MARS monorepository.  
**Reference implementation:** FP-0002 V9-06E63 Stable v1.

Primary report: `REPORTS/REPORT-FP-0002-V9-06E63-STABLE-V1-CLOSEOUT.md`.

---

## 1. Closeout sequence (ordered gates)

| Step | Action | FP-0002 evidence |
|------|--------|------------------|
| 1 | Operator acceptance of current result | E63: closeout requested; accepted baseline doc |
| 2 | Runtime canonization (promote protected files) | `v9-style.css`, `fp02-search.css`, `v9-shell.js` → DIFF 0 |
| 3 | Pre-release backup | `v9-06e63-before-stable-v1-closeout-20260718-003355` |
| 4 | Tail ledger with dispositions | `REPORTS/evidence/v9-06e63-stable-v1-closeout/tail-ledger.md` |
| 5 | ACF source/runtime disposition | `REPORTS/STABLE-V1/ACF-SOURCE-RUNTIME-DISPOSITION-…` |
| 6 | Release validation | routes, viewports, lint, duplicate IDs, forms local |
| 7 | Stable release documentation set | `REPORTS/STABLE-V1/*` + freeze marker |
| 8 | Authoritative freeze | `v9-stable-v1-near-production-freeze-20260718-004137` |
| 9 | Git allowlist (exact paths) | 798 paths; 336 foreign WIP excluded |
| 10 | Clean worktree from remote tip | `X:\AI MARS STORAGE\git-sync-fp0002-e63-stable-v1-20260718-004331\repo` |
| 11 | Exact-file copy allowlist → commit | Content commit `d1befe9b…` |
| 12 | Safe normal push (no force) | Remote tip `9d5dcc28…` |
| 13 | Post-push verification | `ls-remote` / log ancestry |
| 14 | Deferred production checklist | `PRE-PRODUCTION-CHECKLIST-…` |

Production deployment remains a **separate** charter.

---

## 2. MARS monorepository constraints

| Constraint | Why | E63 response |
|------------|-----|--------------|
| Dirty main is not a release worktree | Foreign WIP + unrelated M | Exact copy to clean worktree |
| Foreign WIP must be excluded | Selective staging contract | `GIT-EXCLUDED-FOREIGN-WIP.txt` |
| Force push forbidden | Shared canonical branch | Normal push only |
| Content release commit ≠ final remote tip | Closeout docs / follow commits may land after | Document both SHAs |
| Dirty main HEAD may stay dirty | Expected | Do not reset/clean main |

E63 numbers:

- Dirty main HEAD before wave: `7443c4e9256101a95d756b5a3c01cd4e827f0713`
- Remote before: `29c07d210169ff273d69e7b5f9000d84c1c097b1`
- Content release: `d1befe9b8bfc8688f2f286998ec048e6be49beb6`
- Final remote tip: `9d5dcc285eb45c827231bfe89c7611fb84e850d2`

---

## 3. Formulation discipline

Use precise labels:

- **Stable local near-production baseline** — OK for E63.
- **Production ready / deployed** — only after production checklist + deploy charter.

Never imply SMTP, indexing, or demo-clean content are done if deferred.

---

## 4. Reusable release checklist

### Product readiness

- [ ] Operator acceptance recorded
- [ ] Runtime→source promote complete; product DIFF 0 for theme/plugin scope
- [ ] Pre-release backup OK + DB hash
- [ ] Tail ledger: every open item DISPOSED
- [ ] ACF disposition documented (no broad sync)
- [ ] Validation pack attached
- [ ] Authoritative freeze OK + rollback notes
- [ ] Release manifest + accepted baseline + deferred + pre-prod checklist

### Git readiness

- [ ] Exact allowlist generated (no `git add .`)
- [ ] Secrets scan clean
- [ ] Foreign WIP exclusion list
- [ ] Clean worktree based on `origin/<canonical-branch>` tip
- [ ] Commit message scoped to project
- [ ] Push non-force
- [ ] Verify remote SHA
- [ ] Dirty main untouched (no reset/clean/stash)

### After push

- [ ] Update PROJECT-STATUS
- [ ] Point operators to freeze path + release docs
- [ ] Schedule Experience Pack / cleanup docs before disk cleanup

---

## 5. Human supervision required

- Accepting Stable despite deferred tails
- Allowlist review for accidental foreign paths
- Push timing relative to other monorepo work
- Tag policy (E63 deferred WP tag convention)
- Any production cutover

---

## 6. What not to do

- Commit Stable from dirty main with mixed WIP
- `git pull` / rebase / reset on dirty main to “make push easy”
- Force push
- Broad ACF JSON sync as closeout shortcut
- Delete freezes immediately after push
- Claim production deployment implicitly
