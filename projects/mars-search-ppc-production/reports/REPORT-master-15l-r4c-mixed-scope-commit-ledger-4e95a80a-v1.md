# REPORT — MASTER-15L-R4c Mixed-Scope Commit Ledger 4e95a80a

**Date:** 2026-07-05  
**Lane:** Search PPC Production — mixed-scope commit ledger  
**Volume:** AI WS (`X:`) — verified  
**Branch context:** `mars/canonical-post-recovery`

## 1. Status

- **Status:** FORWARD_ONLY_REMEDIATION
- **Commit:** `4e95a80aa68377aacf8fa19a8cacff29c19b3719`
- **Subject:** FP-0002: seed home content
- **Remote state:** already pushed to `origin/mars/canonical-post-recovery`
- **Remediation choice:** no revert, no split, no history rewrite, no force push

## 2. Incident summary

Commit `4e95a80a` mixed two lanes in a single commit:

- **Corvonero C2a** — `.tools` hardening (14 scripts under `.tools/corvonero-*`)
- **FP-0002 D8-B** — home content seed evidence pack (35 workspace files)

The intended C2a subject was:

> C2a: harden Corvonero .tools helpers

The intended C2a commit was never created as a separate commit. The process defect is **scope/message contamination**: one commit subject and message describe FP-0002 work while Corvonero C2a tooling changes were bundled in the same diff.

Tree content was validated in MASTER-15L-R4b and is **not** being reverted.

## 3. Corvonero C2a content in commit

The following 14 paths were present in commit `4e95a80a`:

- `.tools/corvonero-checkpoint-archive.ps1`
- `.tools/corvonero-checkpoint-build.ps1`
- `.tools/corvonero-checkpoint-git.ps1`
- `.tools/corvonero-checkpoint-receipts.ps1`
- `.tools/corvonero-commander-import-patch-v1.cjs`
- `.tools/corvonero-commander-review-xlsx-w1-v1.py`
- `.tools/corvonero-commander-template-recovery-v1.py`
- `.tools/corvonero-production-extensions-final-checkpoint-v1.py`
- `.tools/corvonero-export-wave-1-v1.py`
- `.tools/corvonero-export-wave-2-roman-docx-v1.py`
- `.tools/corvonero-final-landing-page-copy-checkpoint-v1.py`
- `.tools/corvonero-final-p1-search-ads-checkpoint-v1.py`
- `.tools/corvonero-pre-export-backup-v1.py`
- `.tools/corvonero-commander-five-campaign-split-v1.py`

**Validation (MASTER-15L-R4b):**

- approved 14 paths present
- JSON snapshots excluded
- Phoenix refs absent
- old C/D/E refs absent
- canonical X refs present
- `CORVONERO_OPERATOR_GATE` present in all 14
- C2c hold language present in Commander-family scripts
- no scripts were run
- no Direct/Yandex/account mutation
- no Storage/Localhost mutation

## 4. FP-0002 content in commit

- **35 FP-0002 workspace files** — V9-06D8-B home content seed evidence pack
- Composition: docs/evidence/validation JSON/small screenshots
- Coherent and accepted in-tree pending any separate FP-0002 operator review
- Documents prior Localhost seed evidence; commit itself did not perform new mutation
- Untracked runner artifacts were **not** part of commit

## 5. Risk assessment

| Risk | Level |
|------|-------|
| Semantic history contamination | medium |
| C2a charter non-compliance | medium |
| Revert/split risk in dirty repo | high |
| History rewrite/force-push | prohibited by default |
| Corvonero script content integrity (post-validation) | low |
| FP-0002 evidence integrity (post-validation) | low |

## 6. Remediation decision

- **Decision:** FORWARD_ONLY_REMEDIATION
- No revert/split now.
- No force push.
- Future archaeology must treat `4e95a80a` as a **mixed-scope commit**.
- Future Corvonero C2a references should point to **this ledger** when explaining why there is no separate C2a commit.

## 7. Forward controls

- Future commits must enforce **single-lane scoped staging**.
- Before execution waves, ahead-list and staged diff must be empty.
- Mixed-scope commits on canonical branch require **immediate ledger/reconciliation**.
- Revert/split requires explicit operator charter and dry-run plan.
- C2b/C2c must **not** assume C2a was a clean standalone commit; they must cite this ledger.

## 8. Final confirmation

- This ledger is **documentation-only**.
- It does **not** authorize running scripts.
- It does **not** authorize Commander import, Direct launch, account mutation, advertising start, Storage export execution, Storage mutation, Localhost mutation, or Yandex/API access.
- It does **not** change tree content except this ledger file.
