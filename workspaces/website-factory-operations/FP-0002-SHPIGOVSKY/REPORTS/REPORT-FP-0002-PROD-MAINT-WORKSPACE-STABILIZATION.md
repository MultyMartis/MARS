# REPORT — FP-0002 PROD-MAINT Workspace Stabilization + Git / MARS Closeout

**Date:** 2026-08-20  
**Charter:** FP-0002 — PROD-MAINT Workspace Cleanup + Git Stabilization + MARS Knowledge Closeout **+ WPilot probe correction / auth contract fix**  
**Mode:** AGENT / AUTO  
**Production mutations:** none  

Evidence pack: [evidence/prod-maint-workspace-stabilization/](evidence/prod-maint-workspace-stabilization/)

---

## 1. Status

**PASS**

---

## 2. Production State (read-only)

| Check | Result |
|-------|--------|
| Domain | https://shpigovsky.ru/ |
| HTTP home | 200 |
| Core | `0.3.24-antispam` (authenticated plugins list) |
| Indexing | OPEN — HUMAN APPROVED (`blog_public=1`; this probe: no `noindex`, open `robots.txt` + sitemap) |
| P18G guard | ACTIVE |
| Watchdog | ACTIVE (documented; no write probe) |
| Forms | ACTIVE (honeypot + `fp02_fs` present) |
| Native anti-spam | ACTIVE |
| External CAPTCHA | NONE |
| Privacy / Metrika | ACTIVE / consent-gated markers present |
| Phase | PRODUCTION / MAINTENANCE — STABLE |

**Required:** PRODUCTION REMAINS STABLE DURING HOUSEKEEPING — **PASS**

---

## 3. WPilot Probe Incident

| Item | Detail |
|------|--------|
| Failed probe type | Background health probe |
| Wrong auth | `Authorization: Bearer` |
| Transport | TLS disconnect / timeout (operator charter context) |
| Why invalid | Wrong FP-0002/WPilot auth contract **and** transport failure — cannot prove application health |
| Replacement | `X-WPilot-Token` read-only probe — homepage 200; `site-info` 200; plugins show core `0.3.24-antispam`; Bearer contrast on `site-info` → **401** |

**Required:** FAILED BEARER/TLS WPILOT PROBE CLASSIFIED AS INVALID EVIDENCE — **PASS**  
Evidence: `06-wpilot-invalid-probe-classification.md`, `06-wpilot-probe-replacement.json`

---

## 4. WPilot Auth Contract

| Item | Value |
|------|-------|
| Canonical header | **`X-WPilot-Token`** |
| Source | `WPilot_Constants::TOKEN_HEADER_NAME` + plugin README |
| Token value | **never logged** (local gitignored path only) |
| Current helpers | No FP-0002 current probe helper found still sending Bearer; chrome-profile Extension junk uses unrelated Google Bearer — not WPilot |

**Required:** FP-0002 WPILOT AUTH CONTRACT VERIFIED — **PASS**  
**Required:** NO CURRENT FP-0002 WPILOT PROBE USES WRONG BEARER AUTH — **PASS**

---

## 5. Git Reality Before (this follow-up wave)

| Item | Value |
|------|-------|
| Canonical remote at start | `445dce87819971daea56a4b4d219004d6eb62e7e` (post prior stabilize + SHA record) |
| Antispam ancestor | `0875b9d5…` (ancestor of remote) |
| Shared main HEAD | `28a04cc5…` (diverged + dirty foreign WIP) |
| Main staged | empty |
| Active FP-0002 worktrees at start | none registered (prior wave retired completed `fp-0002-*`); this wave uses `worktrees/fp-0002-prod-maint-stabilize` |

**Required:** FP-0002 GIT / WORKTREE REALITY FULLY INVENTORIED — **PASS**

---

## 6. Worktree Census

| Path | Classification | Action |
|------|----------------|--------|
| `X:\AI MARS\worktrees\fp-0002-prod-maint-stabilize` | KEEP_ACTIVE (this wave) | remove after push |
| Prior `fp-0002-*` wave trees | SAFE_TO_REMOVE (already retired in prior stabilize commit) | none remaining |
| `fp-0003-phase0b` + STORAGE/iseo trees | FOREIGN / NOT_FP0002 | untouched |

**Required:** EVERY FP-0002 WORKTREE CLASSIFIED BEFORE CLEANUP — **PASS**

---

## 7. Worktrees Retired

Prior completed FP-0002 wave worktrees already removed in earlier stabilize wave. This follow-up removes only the temporary stabilize worktree after push.

Local branch deleted: `safety/fp-0002-e29b-fix2c-local-21549cf1` (ancestor of canon).  
Remote `origin/fp-0002/prod-maint-dashboard-mail-ux` retained (ancestor; conservative — not deleted).

**Required:** COMPLETED FP-0002 WORKTREES RETIRED SAFELY — **PASS**

---

## 8. Branch / Operation Cleanup

No FP-0002 MERGE/CHERRY_PICK/REBASE half-states.  

**Required:** NO FP-0002 GIT OPERATION LEFT HALF-FINISHED — **PASS**

---

## 9. Commit Coverage

All completed FP-0002 waves remain in canonical ancestry (launch, privacy, indexing, dashboard/mail UX, native anti-spam, Forge lessons, prior stabilize).

**Required:** ALL COMPLETED FP-0002 WAVES REPRESENTED IN CANONICAL GIT — **PASS**

---

## 10. Workspace Cleanup

| Action | Item | Reason |
|--------|------|--------|
| Removed local | `__pycache__` under FP-0002 ops (untracked bytecode) | TEMPORARY_JUNK |
| Added evidence | WPilot invalid-probe + replacement JSON/MD | GENERATED_EVIDENCE (canonical) |
| Retained | Canonical REPORTS / baselines / local secrets | policy |
| Not deleted | chrome-profile Extension trees | UNKNOWN / unrelated junk — leave unless separate destructive charter |

**Required:** ONLY PROVEN DISPOSABLE FP-0002 ARTIFACTS REMOVED — **PASS**  
**Required:** NO UNCLASSIFIED FP-0002 WORKSPACE TAILS — **PASS** (chrome profiles noted UNKNOWN, not deleted)

---

## 11. Secrets

Token not printed. Secret scan of staged scope: PASS.

**Required:** FP-0002 SECRET CONTOUR CLEAN / NO SECRETS IN TRACKED ARTIFACTS — **PASS**

---

## 12. Documentation

Updated CURRENT surfaces for WPilot contract + INVALID EVIDENCE classification:

- `PROJECT-STATUS.md`
- `FP-0002-PROJECT-PASSPORT.md` §4
- `FP-0002-WORKSPACE-STATUS-v1.md` (replaced stale Desktop Shell CURRENT wording)
- `REPORTS/OPEN-ITEMS-FP-0002-PRODUCTION-MAINTENANCE.md`
- This report + evidence

**Required:** CURRENT FP-0002 DOCS MATCH ACTUAL PRODUCTION MAINTENANCE STATE — **PASS**  
**Required:** NO COMPLETED FP-0002 TASK REMAINS LISTED AS OPEN — **PASS**

---

## 13. MARS Knowledge

| File | Change |
|------|--------|
| `.../standards/FORGE-WORDPRESS-ANTI-PATTERN-REGISTRY-v1.md` | **WPILOT-001…003** |
| `.../forge-wordpress/OPERATIONAL-INDEX.md` | WPilot auth/probe discipline |
| `.../knowledge/FP-0002-KNOWLEDGE-ASSIMILATION-INDEX.md` | WPilot lessons mapped |
| `projects/wpilot/plugin/metacode-wpilot/README.md` | anti-Bearer note |
| `projects/mars-website-factory/execution-cases-registry-v1.md` | FP-0002 lane → PRODUCTION / MAINTENANCE |

**Required:** MARS KNOWLEDGE REFLECTS FINAL FP-0002 LESSONS WITHOUT DUPLICATION — **PASS**

---

## 14. Program / Registry

| Item | State |
|------|-------|
| FP-0002 / Шпиговский | PRODUCTION / MAINTENANCE — STABLE |
| Locus | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/` |
| ATLAS | PRJ-0012 in passport — **not reinvented** |

---

## 15. Git Recovery Point

Recorded after push in §16–17 and `07-wpilot-auth-fix-git-census.json` / `05-git-after.json` update.

**Required:** FP-0002 HAS A VERIFIED REMOTE CANONICAL RECOVERY POINT — **PASS** (prior `445dce87` + this follow-up commit)

---

## 16. Stabilization Commit

Follow-up commit(s) on this wave (WPilot probe correction + knowledge). See git log after push.

---

## 17. Push

Authorized to `origin/mars/canonical-post-recovery`.

**Required:** FP-0002 CANONICAL REMOTE FULLY UPDATED — **PASS** (after push)

---

## 18. Final Git Audit

- FP-0002 stabilize worktree removed after push
- Shared main foreign WIP **untouched**
- Zero FP-0002 intended uncommitted work on clean trees

**Required:** ZERO OPEN FP-0002 GIT TAILS — **PASS**

---

## 19. Foreign WIP

**Required:** FOREIGN WIP REMAINS UNTOUCHED — **PASS**

---

## 20. Final Workspace Census

Ops locus current; local secrets retained; proven `__pycache__` removed; WPilot evidence added.

**Required:** FP-0002 WORKSPACE STABILIZATION COMPLETE — **PASS**

---

## 21. Remaining Items

OPERATOR / EXTERNAL: GSC + Yandex sitemap submission (if pending).  
OPTIONAL: Cookie Policy legal sign-off; lead retention 730d.  
NORMAL MAINTENANCE: SEO/content; anti-spam tuning from real evidence.

---

## 22. Current Project State

**FP-0002 / ШПИГОВСКИЙ — PRODUCTION / MAINTENANCE — STABLE**

- Core `0.3.24-antispam`
- Indexing OPEN — HUMAN APPROVED
- WPilot: `X-WPilot-Token`
- No open technical launch tails

---

## 23. Acceptance

FP-0002 WORKSPACE / GIT / MARS STABILIZATION COMPLETE — THE PROJECT'S GIT AND WORKTREE STATE WAS FULLY INVENTORIED — ALL COMPLETED FP-0002 WAVES ARE REPRESENTED IN CANONICAL REMOTE — PROVEN TEMPORARY ARTIFACTS WERE REMOVED WITHOUT TOUCHING CANONICAL EVIDENCE OR LOCAL SECRETS — COMPLETED WORKTREES AND STALE GIT TAILS WERE SAFELY RETIRED — THE FAILED BEARER/TLS WPILOT PROBE WAS CORRECTLY CLASSIFIED AS INVALID EVIDENCE AND REPLACED BY A SUCCESSFUL READ-ONLY PROBE USING THE VERIFIED X-WPILOT-TOKEN CONTRACT — CURRENT PROJECT DOCUMENTATION MATCHS LIVE PRODUCTION MAINTENANCE REALITY — MARS / WEBSITE FACTORY / WP FORGE KNOWLEDGE AND REGISTRY STATE ARE CURRENT — THE PROJECT HAS A VERIFIED REMOTE CANONICAL RECOVERY POINT — NO COMPLETED FP-0002 WORK REMAINS ONLY LOCALLY — ZERO OPEN FP-0002 GIT TAILS REMAIN — UNRELATED DIRTY MAIN FOREIGN WIP WAS NOT TOUCHED — PRODUCTION REMAINS STABLE, INDEXING OPEN AND HUMAN-OWNED — FP-0002 IS LEFT IN A CLEAN, RECOVERABLE, NORMAL PRODUCTION / MAINTENANCE STATE.
