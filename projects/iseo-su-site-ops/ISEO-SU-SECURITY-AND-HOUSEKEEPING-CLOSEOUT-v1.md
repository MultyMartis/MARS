# ISEO-SU SECURITY AND HOUSEKEEPING CLOSEOUT v1

## 1. Status

COMPLETE — active form HMAC secret rotated, removed from current tracked source, production authority moved to local-only PHP file, project-owned i-seo workspace tails pruned, and documentation reconciled.

## 2. HMAC Security Remediation

- tracked `production-source/forms/iseo-form-config.php` no longer contains an active HMAC literal
- shared server loader now reads HMAC authority from production-local runtime file
- token issuance and validation fail closed if the local secret file is unavailable

## 3. Current Secret Authority

- active runtime authority: `.iseo-form-runtime/iseo-form-secrets.local.php`
- tracked example only: `production-source/forms/iseo-form-secrets.example.php`
- Git status for real secret file: untracked / local-only / not committed

## 4. Form Validation State

- representative valid submission under isolated test mode: PASS
- invalid HMAC negative test: PASS
- missing required data negative test: PASS
- token endpoint after rotation: healthy and returns public signed payload only

## 5. Production Recipient

Final production recipient state:

- `test_mode`: OFF
- production recipient: `nikel007i33@yandex.ru` only
- operator test mailbox in production recipients: NO

## 6. Git History Risk

Historical revoked HMAC secret material remains in Git history from earlier commits. Because the value is rotated and no longer active, this is classified as `HISTORICAL_REVOKED_SECRET`, not an active production blocker. No history rewrite was performed.

## 7. Workspace Cleanup

Cleanup focused only on project-owned i-seo tails:

- removed 4 obsolete clean i-seo sync worktrees
- removed 3 empty stale `git-sync-iseo-su-*` directories
- retained historical glossary/SEO backup collections and current HMAC rollback receipts

## 8. Scratch Removed

- `X:\AI MARS STORAGE\git-sync-iseo-su-final-closeout`
- `X:\AI MARS STORAGE\git-sync-iseo-su-final-stabilization`
- `X:\AI MARS STORAGE\git-sync-iseo-su-recipient-remove-tech-seo-audit-01`

## 9. Backups Retained

- current HMAC rotation rollback set: `X:\AI MARS\local\sites\iseo-su-production\_hmac-rotation-01\`
- glossary DB backup collections under `X:\AI MARS STORAGE\iseo-su-site-ops\glossary-db-backups\`
- tech/SEO audit raw evidence under `X:\AI MARS STORAGE\iseo-su-site-ops\tech-seo-audit-01\`

## 10. Backups Removed

None. Historical backup collections were not mass-pruned because they remain unique or still serve as milestone rollback/evidence sets.

## 11. Worktrees Removed

1. `X:\AI MARS STORAGE\git-sync-iseo-su-all-forms-mail-acceptance-02-20260821-024352\repo`
2. `X:\AI MARS STORAGE\git-sync-iseo-su-docs-consolidation\repo`
3. `X:\AI MARS STORAGE\git-sync-iseo-su-form-recipient-restore-01`
4. `X:\AI MARS STORAGE\git-sync-iseo-su-mail-acceptance-02-tip-20260821-024504\repo`

## 12. Documentation Updated

- `ISEO-SU-CURRENT-STATE-v1.md`
- `ISEO-SU-PRODUCTION-ARCHITECTURE-KNOWLEDGE-BASE-v1.md`
- `ISEO-SU-FORM-SECURITY-AND-ANTISPAM-BASELINE-v1.md`
- `ISEO-SU-PROTECTED-ZONES-v1.md`
- `OPERATIONAL-INDEX.md`
- `ISEO-SU-SITE-OPS-ARTIFACT-REGISTER-v1.md`
- `ISEO-SU-SITE-OPS-SAFE-UNKNOWN-REGISTER-v1.md`
- `ISEO-SU-FORM-HMAC-SECRET-ROTATION-EVIDENCE-v1.md`

## 13. Current Open Technical Work

OPEN_TECH:

1. root sitemap repair
2. static sitemap maintenance strategy
3. blog relative image-path fix
4. remaining tech/SEO audit backlog review/fix

## 14. Deferred Work

- optional Git history rewrite for revoked secret residue only if a separate repository exposure/policy charter requires it
- WPilot 6D bridge/read-only smoke remains separate and still gated

## 15. Git Local State

At closeout drafting time, only task-owned `iseo-su-site-ops` changes from this charter are intended for selective staging. Foreign WIP outside the project locus remains preserved and out of scope.

## 16. Git Remote State

Remote sync is part of this task wave and must occur only after selective staging/commit via a clean sync worktree. No force push, no history rewrite.

## 17. Production Mutations

Actual production mutation set for this task:

- `iseo-form-config.php`
- `iseo-form-security.php`
- `iseo-form-token.php`
- `.iseo-form-runtime/.htaccess`
- `.iseo-form-runtime/iseo-form-secrets.local.php`

## 18. Final Decision

- HMAC secret rotated: YES
- active secret removed from current tracked source: YES
- production secret local-only: YES
- form anti-spam regression: NONE
- project-owned workspace tails reduced: YES
- foreign WIP preserved: YES
