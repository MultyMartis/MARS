# REPORT — MARS Infra Runtime Split SITE-002

**Operation ID:** `MARS-INFRA-RUNTIME-SPLIT-SITE-002-01`  
**MARS infra run:** `MARS-INFRA-RUNTIME-SPLIT-01`  
**OCPilot reference:** Run **4.257** (infra)  
**Date:** 2026-07-10

> Canonical repo copy. Storage mirror: `X:\AI MARS STORAGE\mars-infrastructure\runtime-split\MARS-INFRA-RUNTIME-SPLIT-SITE-002-01\reports\MARS-INFRA-RUNTIME-SPLIT-SITE-002-01.md`

---

## 1. Scope

Move SITE-002 post-1C catalog monitor Windows Task Scheduler execution from dirty development worktree `X:\AI MARS` to clean sparse runtime checkout `X:\AI MARS STORAGE\runtime-checkouts\site-002-monitor\repo` @ `56f9bae7`. Update scheduled task action/working directory only. One manual verification run. No production mutation.

## 2. Operator approval

Approved after audit `MARS-GIT-TOPOLOGY-AND-RUNTIME-SAFETY-AUDIT-01`.

## 3. Pre-flight

- Authority: `56f9bae7` = `origin/mars/canonical-post-recovery` ✓
- Dirty main: `96a8f08f`, ahead 4 / behind 10, ~636 WIP entries — read-only ✓

## 4. Scheduled task before

`MARS_SITE_002_Post_1C_Catalog_Monitor` → runner under `X:\AI MARS`, WorkingDirectory `X:\AI MARS`.

## 5. Runtime checkout creation

Sparse clone (`projects/ocpilot` only) at `X:\AI MARS STORAGE\runtime-checkouts\site-002-monitor\repo`, HEAD `56f9bae7`. Full worktree failed on Windows long paths.

## 6. Runner path validation

Dry-run PASS. Runner uses dynamic `RepoRoot` from `$PSScriptRoot`.

## 7. Scheduled task action update

Action + WorkingDirectory → runtime checkout. Triggers/principal/settings unchanged. Required UAC elevation.

## 8. Manual scheduled run

`2026-07-10_20-17-16`, LastTaskResult **0**, ~99s.

## 9. Monitor result verification

| Metric | Value |
|--------|------:|
| repo_root | runtime checkout ✓ |
| onboarding_needs_count | 0 |
| classification | HYGIENE_REVIEW_REQUIRED |
| strict_garbage_hits | 0 |
| hygiene_flags | 0 |

## 10. Site safety check

No HTTP 500. `/kontakty` 404 accepted. Nested Lari 200. Flat `/lari` 301.

## 11. Final decision

CREATED_CLEAN + SCHEDULER COMPLETE + MONITOR PASS_UPDATED_RUNTIME

## 12. Production mutation summary

All counts **0**.

## 13. Scheduler mutation summary

One task; action/WD only.

## 14. Runtime checkout summary

Sparse clone created; dirty main untouched.

## 15. Git/worktree summary

Authority commit source; dirty main read-only.

## 16. Storage artifacts

`X:\AI MARS STORAGE\mars-infrastructure\runtime-split\MARS-INFRA-RUNTIME-SPLIT-SITE-002-01\`

## 17. SAFE UNKNOWN / blockers

Long-path worktree failure (mitigated); UAC for scheduler edit.

## 18. Final verdict

**MARS INFRA RUNTIME SPLIT SITE-002 COMPLETE — SCHEDULER DETACHED FROM DIRTY MAIN**

## 19. Next recommendation

Refresh runtime checkout on monitor tooling changes; never schedule from dirty main; optional main git-hygiene wave.

See also: [runtime-checkouts.md](../runtime-checkouts.md)
