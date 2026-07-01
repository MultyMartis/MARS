# Corvonero post-project closure checklist v1

**Project:** Corvonero Search PPC pilot  
**State:** CLIENT_FEEDBACK_PENDING  
**Authority:** V2.6 (unchanged)  
**Deployable:** V2.6.2 (unchanged)

## Phase A — Preflight

- [x] Drive X: volume AI WS confirmed
- [x] Repository `X:\AI MARS` on `mars/canonical-post-recovery`
- [x] HEAD recorded
- [x] Corvonero and unrelated WIP inventoried
- [x] No destructive git/filesystem operations

## Phase B — Backup

- [x] Immutable backup under `X:\AI MARS STORAGE\backups\search-ppc\`
- [x] Repository evidence ZIP
- [x] Storage delivery evidence ZIP
- [x] Git evidence files
- [x] Manifest + SHA256 sums
- [x] `BACKUP_VERIFIED: true`

## Phase C — Project freeze

- [x] `CORVONERO-CURRENT-ARTIFACT-INDEX-v1`
- [x] `CORVONERO-CLIENT-FEEDBACK-STATE-v1`
- [x] `CORVONERO-MANUAL-STABLE-ARTIFACTS-v1`
- [x] Historical V2.1–V2.6.1 marked SUPERSEDED / DO NOT IMPORT

## Phase D — Feedback wait

- [x] `CLIENT_FEEDBACK_PENDING` formalized
- [x] Feedback intake templates created
- [ ] Client response received (blocked on client)

## Phase E — Lessons and problems

- [x] Problem register complete
- [x] Lessons learned documented

## Phase F — Shared hardening

- [x] Semantic lifecycle extension
- [x] Classification controls
- [x] Architecture / ad / negative / package purity validators
- [x] Manual-stable guard
- [x] Artifact locator contract
- [x] Regression tests added

## Phase G — Documentation

- [x] Shared Search PPC standards updated/created
- [x] Storage current-deliverables index
- [x] Cleanup plan (inventory only)

## Explicitly NOT done (by design)

- [ ] Commander import
- [ ] Yandex Direct access / launch
- [ ] Semantic authority modification
- [ ] Client-sent file modification
- [ ] Cleanup execution (delete/move/archive)
- [ ] Git stage / commit / push

## Remaining blockers

1. Client feedback on ads and commercial claims
2. Landing-page copy approval (5 final + 5 Roman briefs)
3. Commander import reconciliation
4. Manual TXT negative import post-import
5. REMOTE NSO exclusion verification
6. Analytics setup confirmation
7. Launch authorization
