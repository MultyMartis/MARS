# Worktree classification (before cleanup)

| Path | Branch | HEAD | Ancestor of origin | Dirty | Classification | Planned action |
|------|--------|------|--------------------|-------|----------------|----------------|
| fp-0002-p18e-cd | agent/fp-0002-p18e-cd | a8ce4b2b | YES | YES (superseded WIP + test-results) | SAFE_TO_REMOVE (unique product work already in later canon) | remove --force after documenting |
| fp-0002-p18e-cd-closeout-sync | agent/fp-0002-p18e-cd-closeout-sync | 456ec127 | YES | NO | SAFE_TO_REMOVE | remove |
| fp-0002-p18e-ef | fp-0002-p18e-ef | c62b89d7 | YES | NO | SAFE_TO_REMOVE | remove |
| fp-0002-p18g-push | (detached) | 29707aeb | YES | NO | SAFE_TO_REMOVE | remove |
| fp-0002-p18g-push-v2 | fp-0002-p18g-push | 3aa0d6c8 | YES | YES (runtime intake refresh) | SAFE_TO_REMOVE | discard dirty intake; remove |
| fp-0002-p18h | fp-0002-p18h | 5e1218cd | YES | NO | SAFE_TO_REMOVE | remove |
| fp-0002-p18i | fp-0002-p18i | 13ef2788 | YES | YES (smoke.mjs + node_modules) | SAFE_TO_REMOVE | junk only; remove --force |
| fp-0002-p18j | fp-0002/prod-p18j-indexing-qa-noise | 588a78a3 | YES | NO | SAFE_TO_REMOVE | remove |
| fp-0002-prod-maint-antispam | fp-0002/prod-maint-native-antispam | 0875b9d5 | YES | NO | SAFE_TO_REMOVE | remove |
| fp-0002-prod-maint-p23 | fp-0002/prod-maint-dashboard-mail-ux | d5223ae0 | YES | YES (untracked receipt) | SAFE_TO_REMOVE | receipt optional; remove --force |
| fp-0002-prod-maint-stabilize | fp-0002/prod-maint-workspace-stabilize | e0d297e6→ | YES | this wave | KEEP_ACTIVE until push | keep then retire after push |
| fp-0003-phase0b | fp-0003-overseo-phase0b | f379d9ac | n/a | n/a | FOREIGN / NOT_FP0002 | KEEP |
| X:\AI MARS main | mars/canonical-post-recovery | 28a04cc5 | ahead+dirty foreign | YES | FOREIGN WIP host | DO NOT CLEAN |
