# REPORT — ISEO-SU SITE OPS SECURITY SECRET ROTATION AND FINAL MARS CLEANUP 01

## 1. Execution Summary

Completed a two-phase site-ops wave for `i-seo.su`: rotated the active form HMAC secret out of tracked source into a production-local PHP authority, validated form behavior with isolated test routing, then pruned project-owned i-seo workspace/worktree residue and reconciled the project brain/docs without touching unrelated open technical work.

## 2. Environment Preflight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume | `AI WS` (X:) |
| Branch | `mars/canonical-post-recovery` |
| Staged at start | empty |
| Project-owned iseo staged at start | empty |
| Project-owned iseo untracked scratch at start | 0 in tracked project locus |
| Foreign WIP | present outside `iseo-su-site-ops`; preserved |
| Current worktrees | inventoried before cleanup |

## 3. HMAC Security Risk

Tracked current source previously contained an active form HMAC secret literal in `production-source/forms/iseo-form-config.php`. Because the value had entered Git, it was treated as compromised and rotated.

## 4. Previous Secret Architecture

The tracked shared config stored recipients, test mode, thresholds, and the active HMAC secret together. Shared server validation code consumed that value for timing-token signing/verification and duplicate/rate-linked fingerprints.

## 5. New Secret Authority

New authority model:

- tracked config: null placeholder + local secret path
- active runtime authority: `.iseo-form-runtime/iseo-form-secrets.local.php`
- protection: `.iseo-form-runtime/.htaccess`
- failure mode: fail closed for HMAC-protected submission behavior if the secret file is unavailable

## 6. Secret Rotation

- generated a cryptographically strong replacement secret locally
- wrote it to local build artifact only
- deployed it to the production-local PHP authority file
- did not print the old or new secret value

## 7. Current Tracked Source Verification

Post-remediation tracked source state:

- active HMAC secret literal in current tracked tree: NO
- tracked config now holds `hmac_secret => null`
- tracked source scan for high-entropy HMAC-style literal in forms source: no active match found
- example secret file contains placeholder only

## 8. Production Deployment

Production mutation scope:

1. `iseo-form-config.php`
2. `iseo-form-security.php`
3. `iseo-form-token.php`
4. `.iseo-form-runtime/.htaccess`
5. `.iseo-form-runtime/iseo-form-secrets.local.php`

Each upload was followed by readback/checksum verification. Scoped rollback receipts live under `X:\AI MARS\local\sites\iseo-su-production\_hmac-rotation-01\`.

## 9. Form Security Validation

| Check | Result |
|-------|--------|
| token endpoint available after rotation | PASS |
| public token payload limited to `{t,s,id}` | PASS |
| representative valid submission under isolated test mode | PASS |
| invalid HMAC negative test | PASS |
| missing required data negative test | PASS |
| secret file direct web access blocked | PASS |

## 10. Isolated Mail Test

Validation used the existing isolated test-mode facility:

- effective recipient during test: `im.work@mail.ru` only
- normal production recipients active during test: NO
- representative valid callback submit: accepted
- invalid HMAC mail count: 0
- missing-required-data mail count: 0

## 11. Production Recipient Restoration

Final production routing state:

- `test_mode`: OFF
- final production recipient: `nikel007i33@yandex.ru` only
- operator mailbox left in production recipient set: NO

## 12. Git History Assessment

Historical revoked secret material remains in earlier commits for `production-source/forms/iseo-form-config.php`.

- OLD SECRET MATERIAL IN HISTORY: YES
- OLD SECRET STILL ACTIVE: NO
- HISTORY REWRITE PERFORMED: NO
- classification: `HISTORICAL_REVOKED_SECRET`

## 13. Workspace Census

Reviewed:

- project locus `projects/iseo-su-site-ops\`
- local runtime tails under `X:\AI MARS\local\sites\iseo-su-production\`
- storage backup/evidence root `X:\AI MARS STORAGE\iseo-su-site-ops\`
- i-seo sync/worktree tails under `X:\AI MARS STORAGE\git-sync-iseo-su-*`

## 14. Scratch Cleanup

Removed only safe project-owned tails:

- 3 empty stale `git-sync-iseo-su-*` directories
- no project docs/content sources were deleted

## 15. Backup Census

Reviewed backup/evidence collections:

- current HMAC rotation rollback set
- 9 glossary DB backup directories
- tech/SEO raw evidence directory

No mass deletion of backup collections was performed because the reviewed stored sets remain unique or materially useful.

## 16. Backup Cleanup

Backups removed: 0

Reason: no reviewed backup set was proven to be a disposable duplicate with equal recovery value.

## 17. Worktree Cleanup

Removed clean obsolete i-seo worktrees:

1. `git-sync-iseo-su-all-forms-mail-acceptance-02-20260821-024352`
2. `git-sync-iseo-su-docs-consolidation`
3. `git-sync-iseo-su-form-recipient-restore-01`
4. `git-sync-iseo-su-mail-acceptance-02-tip-20260821-024504`

## 18. Documentation Reconciliation

Updated authorities:

- `ISEO-SU-CURRENT-STATE-v1.md`
- `ISEO-SU-PRODUCTION-ARCHITECTURE-KNOWLEDGE-BASE-v1.md`
- `ISEO-SU-FORM-SECURITY-AND-ANTISPAM-BASELINE-v1.md`
- `ISEO-SU-PROTECTED-ZONES-v1.md`
- `OPERATIONAL-INDEX.md`
- `ISEO-SU-SITE-OPS-ARTIFACT-REGISTER-v1.md`
- `ISEO-SU-SITE-OPS-SAFE-UNKNOWN-REGISTER-v1.md`

## 19. Open Work Reconciliation

Security remediation closed:

- tracked active HMAC secret risk -> CLOSED / ROTATED / REMOVED FROM CURRENT TREE

Open technical work preserved:

1. root sitemap repair
2. static sitemap maintenance strategy
3. blog relative image-path fix
4. remaining tech/SEO audit backlog review/fix

## 20. SAFE UNKNOWN

SAFE UNKNOWN remains non-blocking and was reviewed. Historical revoked HMAC secret residue is treated as known historical risk, not SAFE UNKNOWN.

## 21. Local Git Persistence

This task requires selective staging only for `iseo-su-site-ops` tracked changes created by the rotation/cleanup wave. Foreign WIP outside the project locus remains excluded.

## 22. Remote Sync

Remote sync must be completed only after the scoped commit via a clean sync worktree based on current `origin/mars/canonical-post-recovery`. No force push and no history rewrite are authorized.

## 23. Final Workspace State

- project-owned tracked source now free of active HMAC secret literal
- project-owned i-seo untracked scratch in the repository locus remains 0
- obsolete clean i-seo worktrees removed
- historical backup/evidence collections retained where still useful

## 24. Production Mutations

Yes — bounded to form security files and protected runtime secret authority only. No sitemap/blog-image/SEO/Metrika/glossary/CAPTCHA work was started.

## 25. Remaining Risks

- revoked old secret still exists in Git history
- SMTP/mail transport details remain a named SAFE UNKNOWN when handlers are not otherwise changed
- open technical SEO backlog remains unchanged and out of scope

## 26. Final Decision

Security remediation and final workspace cleanup are complete once selective Git persistence and clean-worktree remote sync finish. The active production secret is no longer in current tracked source and production form security remains operational.

## 27. Stop Condition

Stop after:

- active HMAC secret rotation
- local-only secret migration
- form validation
- current tracked-source hygiene
- history assessment without rewrite
- project scratch cleanup
- safe backup review
- obsolete worktree cleanup
- documentation reconciliation
- scoped Git persistence
- remote sync
- final clean-state verification
