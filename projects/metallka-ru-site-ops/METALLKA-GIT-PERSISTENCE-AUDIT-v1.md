# METALLKA — Git Persistence Audit v1

**Programme:** METALLKA-RU-SITE-OPS  
**Wave:** PHASE 4C-P1 — PROJECT CORPUS GIT PERSISTENCE PREFLIGHT *(live state amended through P2/P3)*  
**Date:** 2026-07-27  
**Locus:** `projects/metallka-ru-site-ops/`  
**Mode:** Local Git / documentation persistence only — **no production contact**

---

## 1. Verdict (this wave)

| Field | Value |
|-------|-------|
| Tracking root cause | **A — NEW PROJECT CORPUS — NEVER COMMITTED** *(at P1; now object-persisted on temp branch)* |
| Secret audit | **PASS** (no real secret values in locus) |
| Raw-evidence boundary | **PASS** (bulk evidence remains under Storage) |
| Doc consistency (after minimal fixes) | **PASS** |
| Exact allowlist | **READY** — [METALLKA-GIT-PERSISTENCE-ALLOWLIST-v1.txt](METALLKA-GIT-PERSISTENCE-ALLOWLIST-v1.txt) |
| Staging / commit (P1) | **BLOCKED** (historical — foreign staged index) |
| Persistence strategy (P2) | **CLEAN WORKTREE** — commit on temp branch; no primary-index mutation |
| Safe commit (P2) | `980fa32008936d1bd1e52254f086e4616221f71e` on `mars/tmp-metallka-persistence-20260727-004959` |
| Canonical integration (P3) | **DEFERRED** — LEVEL B; dirty primary + untracked metallka collide with FF |

**P1 block reason (historical):** staged index was **not empty** at P1 start. **76** staged deletions under `projects/client-ops-reporting-bridge/` (foreign WIP). Gate §12 required empty staged index before metallka staging in the primary worktree. Foreign staged paths were **not** unstaged/modified by P1.

**P2 note:** Phase 4C-P2 selected clean-worktree persistence so the audited corpus can be committed without staging in the dirty primary worktree. Authoritative object: `980fa320` (57 metallka paths; parent `e9c9be59`).

**P3 note (2026-07-27):** Canonical integration readiness wave. Primary HEAD still `e9c9be59`. Staged index now **empty** (0). Index anomaly 76→0 classified primarily as **A** (foreign staged deletions became unstaged deletions for the observable client-ops set; currently **19** unstaged `D`, files absent on disk, still indexed). Historical count delta 76→19 retains residual **SAFE UNKNOWN** (not reconstructed). Clean-worktree FF proof of `980fa320` from `e9c9be59` **SUCCEEDED**; moving checked-out `mars/canonical-post-recovery` remains **unsafe** while primary is dirty and metallka exists as untracked on disk. P2 report = follow-up persistence candidate. Production / WPilot posture unchanged.

---

## 2. Environment snapshot (preflight)

| Check | Result |
|-------|--------|
| cwd | `X:\AI MARS` |
| Volume X: label | **AI WS** |
| Branch | `mars/canonical-post-recovery` |
| HEAD (before any metallka commit) | `e9c9be59f643e66970930e31339431acb8077b55` |
| Origin tip `origin/mars/canonical-post-recovery` | `dc1fa5c48255efd8819b1947408d82f67bf020ca` |
| Ahead / behind (before) | **ahead 123, behind 62** |
| Staged index at start | **NONEMPTY** — 76 foreign `D` paths (client-ops) |
| Metallka in staged index | **0** |
| Branch sync / pull / push | **NOT PERFORMED** |
| Production HTTP / WPilot | **0** |

---

## 3. Why the corpus was untracked

### Classification: **A — NEW PROJECT CORPUS — NEVER COMMITTED**

Evidence:

| Probe | Result |
|-------|--------|
| Files on disk under locus | **57** after this wave artefacts (was **55** at discovery) |
| `git ls-files -- projects/metallka-ru-site-ops/` | **0** |
| Untracked under locus (pre-audit artefacts) | **55** |
| `git check-ignore -v` on locus files / parents | **no ignore matches** |
| `git ls-files -v` assume-unchanged / skip-worktree for locus | **none** |
| `git log --all -- projects/metallka-ru-site-ops/` | **0 commits** |
| `git rev-list --all --count -- projects/metallka-ru-site-ops/` | **0** |
| Path on `origin/mars/canonical-post-recovery` | **absent** |

Not B/C/D/E/F: no conflicting history, no ignore-rule suppression, no index anomaly on this path, not a recovery ghost of a previously tracked tree.

**Operational explanation:** Phases 1.5 → 4C-R1 created the documentary corpus on disk while the MARS monorepo remained dirty with substantial foreign WIP; selective staging never included this locus.

---

## 4. Ignore / history analysis

- Parent `projects/` is tracked for other programmes; metallka is simply never added.
- `.gitignore` does **not** exclude `projects/metallka-ru-site-ops/`.
- Local secrets/token live under `/local/` (gitignored) — correctly outside this locus.
- No reconciliation against remote history required (path never existed in any examined ref).

---

## 5. Corpus inventory (summary)

| Metric | Count |
|--------|-------|
| Disk files at discovery | 55 |
| Tracked before | 0 |
| Untracked before | 55 |
| Ignored in locus | 0 |
| Extension | **100% `.md`** at discovery; allowlist adds `.txt` audit allowlist |
| Binaries / archives / dumps in locus | **0** |
| Approved commit candidates | **all enumerated locus files** (see allowlist) |
| Excluded from commit (inside locus) | **0** after audit |
| Explicit exclusions (outside locus) | local tokens/secrets; Storage evidence trees; foreign WIP |

### Per-file role class (all commit-candidate YES unless noted)

| Class | Paths (pattern) | Secret risk | Raw-evidence risk | Commit |
|-------|-----------------|-------------|-------------------|--------|
| Navigation / index | `README.md`, `OPERATIONAL-INDEX.md` | Low (doc refs only) | None | YES |
| Registers / baselines / charter | `METALLKA-*-v1.md` (non-report) | Low | None | YES |
| Phase reports | `reports/REPORT-*.md` | Low | Sanitized textual | YES |
| Persistence artefacts | `METALLKA-GIT-PERSISTENCE-AUDIT-v1.md`, `METALLKA-GIT-PERSISTENCE-ALLOWLIST-v1.txt` | None | None | YES |

Exact path enumeration: allowlist file (one path per line).

---

## 6. Secret audit

**Result: PASS**

Searched locus for password/token/Authorization/cookie/private-key/API-key style **value** patterns.

Findings:

- Header name `X-WPilot-Token` appears as **documentation** only.
- Paths such as `X:\AI MARS\local\tokens\wpilot-prod-metallka-ru.token` are **path references**; values not embedded.
- Mentions of Beget / WP Admin password status are **status labels**, not credential values.
- No `-----BEGIN … PRIVATE KEY-----`, no Bearer values, no cookie dumps.

Token file exists local-only and is gitignored via `.gitignore` `/local/`.

**If any real secret had been found:** STOP before staging (this wave already STOPPED for index gate).

---

## 7. Raw-evidence boundary audit

**Result: PASS**

Storage evidence present at:

`X:\AI MARS STORAGE\wpilot\evidence\metallka-ru-site-ops\`

Observed phase directories include: `phase-2b-discovery`, `phase-3b-change-0001`, `phase-3b-r1-change-0001`, `phase-4b-wpilot-rc6-install`, `phase-4b-fix01`, `phase-4c-gate-e`, `phase-4c-r1-gate-e-retry`.

Git locus contains charters, baselines, maps, registers, sanitized evidence docs, reports, indexes — **not** plugin directory copies, DB dumps, binary backups, credential files, or raw browser session stores.

---

## 8. Documentation consistency audit

### Live facts required (validated against OPERATIONAL-INDEX + CONNECTION-STATE + COMPATIBILITY + FIX01/4C-R1 reports)

| Fact | Status in current-state docs |
|------|------------------------------|
| WPilot build `0.3.0-RC6` | Present |
| i-seo code parity CONFIRMED | Present (FIX01) |
| `dev_confirmed` ON | Present |
| bridge ON | Present |
| write OFF | Present |
| authenticated protected reads PROVEN | Present (4C-R1) |
| public ping ≠ auth proof | Present |
| token local-only | Present |
| WPilot writes BLOCKED | Present |
| CHANGE 0001 COMPLETE / production validated | Present |
| Production source authority provisional | Preserved in baseline / charter posture |
| Historical BLOCKED runs visible | Preserved (4C Gate E, 3B auth block) |

### Minimal corrections made in this wave

| File | Change |
|------|--------|
| `README.md` | Stale Phase 1.5 “NOT CONNECTED” current-phase block → current 4C-R1 posture; Phase 1.5 non-claims marked historical |
| `METALLKA-SITE-OPS-CURRENT-BASELINE-v1.md` | Supersession banner; body left as Phase 1.5 historical snapshot |
| `METALLKA-ARTIFACT-REGISTER-v1.md` | Git persistence artefacts; persistence BLOCKED row; footer updated from stale 4C-R0-only closeout |
| `OPERATIONAL-INDEX.md` | Git persistence PREPARED/BLOCKED; reading-order links; HOLD for commit |

Historical reports **not** rewritten.

---

## 9. Exact commit allowlist

Authority file:

`projects/metallka-ru-site-ops/METALLKA-GIT-PERSISTENCE-ALLOWLIST-v1.txt`

Rules:

- One repository-relative path per line.
- File-level staging only (no blind `git add projects/metallka-ru-site-ops/`).
- Include audit + allowlist themselves once regenerated after final edits.

### Explicit exclusions

- Anything under `X:\AI MARS\local\`
- Anything under `X:\AI MARS STORAGE\`
- Any path outside `projects/metallka-ru-site-ops/`
- Foreign WIP (including staged client-ops deletions)

### Foreign WIP boundary

Substantial unrelated `M` / `D` / `??` elsewhere in the monorepo (including `.recovery-temp/`, client-ops, etc.) must remain untouched. This wave must not stage, restore, clean, or reset foreign paths.

---

## 10. Branch divergence warning

Local `mars/canonical-post-recovery` is **diverged** from origin (**ahead 123 / behind 62** at audit time).

Do **not** pull / rebase / merge / push to “make room” for metallka persistence.

When a future push is required, use the established MARS safe sync model (e.g. clean temporary worktree under `X:\AI MARS STORAGE\git-sync-*\repo`). **Not in this wave.**

Recommended commit subject (when gate passes):

```text
docs(metallka): persist site ops and wpilot production baseline
```

(Aligned with prior `docs(iseo-su): persist …` convention.)

---

## 11. Recommended commit strategy (next authorized wave)

**Superseded by P2/P3:** the 57-file corpus is already committed as `980fa320`. Do **not** create a parallel duplicate commit from dirty primary.

### Canonical integration prerequisite (P3 → next wave)

1. Keep authoritative object/branch: `980fa320` / `mars/tmp-metallka-persistence-20260727-004959`.
2. Integrate **only** when a normal path-safe mechanism can FF `mars/canonical-post-recovery` **without** rewriting foreign WIP/index — typically: temporary clean worktree at current canonical tip, FF-merge `980fa320`, then operator-approved primary sync that does not clobber untracked/dirty paths; **or** wait until primary worktree is clean enough that FF checkout of metallka paths does not collide with untracked files.
3. Do **not** use `update-ref` / force branch move on the dirty checked-out primary.
4. After canonical tip includes `980fa320`, persist follow-up docs (P2/P3 reports + audit/index/register deltas) via a **separate** scoped commit (clean worktree preferred).
5. **No push** unless separately authorized.

---

## 12. Production counters (this wave)

| Counter | Value |
|---------|-------|
| Production HTTP/API calls | **0** |
| WPilot REST calls | **0** |
| WPilot settings / writes / token / bridge changes | **0** |
| Content mutations | **0** |

---

## 13. Phase 4C-P3 live Git snapshot (amendment)

| Field | Value |
|-------|-------|
| Primary branch | `mars/canonical-post-recovery` |
| Primary HEAD | `e9c9be59f643e66970930e31339431acb8077b55` |
| Origin tip | `dc1fa5c48255efd8819b1947408d82f67bf020ca` |
| Ahead / behind | **123 / 62** |
| Staged | **0** |
| Safe commit | `980fa32008936d1bd1e52254f086e4616221f71e` |
| Temp branch | `mars/tmp-metallka-persistence-20260727-004959` |
| Corpus parity (57) | **EXACT MATCH** disk ↔ commit |
| Post-commit follow-up | P2 report (+ P3 report) pending persistence |
| Canonical integration | **DEFERRED** |
| Production | unaffected |

---

*METALLKA Git Persistence Audit v1 · root cause A · P1 BLOCKED · P2 safe commit 980fa320 · P3 canonical integration DEFERRED.*

## 15. Phase 4C-P4-R1 outcome (amendment)

| Field | Value |
|-------|-------|
| Expected base | `5c65ac8817e94ad146c7aee80d876b2290e65ef5` |
| Tip at promotion gate | `65ab3a973f94c51fccae03c9e48868b75293316b` |
| Rebased commit (temp) | `c781a55aae500a8f91502b8dba67fd506abc18c4` |
| Follow-up (temp) | `ac0f37b7f3b131e890e9ac81de37c65265c8aaa7` |
| Temp branch | `mars/tmp-metallka-rebased-20260727-011021` |
| Canonical promotion | **NOT PERFORMED** |
| Stop | `BLOCKED — CANONICAL HEAD ADVANCED DURING P4-R1` |
| Report | [reports/REPORT-METALLKA-SITE-OPS-PHASE-4C-P4-R1-CANONICAL-PROMOTION.md](reports/REPORT-METALLKA-SITE-OPS-PHASE-4C-P4-R1-CANONICAL-PROMOTION.md) |
| Next | **P4-R2** onto current tip |

---

## 16. Phase 4C-P4-R2 strategy correction (amendment)

**Does not invalidate** P1–P4-R1 historical conclusions. Those waves correctly recorded dirty-primary / rebase-race constraints.

| Field | Value |
|-------|-------|
| Abandoned approach | Promoting through dirty checked-out `mars/canonical-post-recovery` / chasing local canonical tip |
| Active Brain | `X:\AI MARS` — shared dirty monorepo; **INPUT SOURCE / READ-ONLY** for this Git wave |
| Foreign WIP | Out of scope (do not stage/restore/stash/clean/reset) |
| Persistence surface | `X:\AI MARS STORAGE\git-sync-*\repo` clean temporary worktrees |
| Integration authority | **`origin/mars/canonical-post-recovery`** (remote tip), not local canonical HEAD |
| Active strategy | Fresh scoped current-corpus snapshot commit whose parent = refreshed `REMOTE_BASE` |
| Historical provenance | `980fa320` / `c781a55a` / `ac0f37b7` preserved; **not** cherry-picked into canonical |
| Allowlist authority | [METALLKA-GIT-PERSISTENCE-ALLOWLIST-v2.txt](METALLKA-GIT-PERSISTENCE-ALLOWLIST-v2.txt) |
| Push | **NOT AUTHORIZED** in P4-R2 |

Recommended commit subject (P4-R2):

```text
docs(metallka): persist site ops and wpilot production baseline
```

*METALLKA Git Persistence Audit v1 · root cause A · P1 BLOCKED · P2–P4-R1 provenance · P4-R2 remote-canonical prep strategy.*
