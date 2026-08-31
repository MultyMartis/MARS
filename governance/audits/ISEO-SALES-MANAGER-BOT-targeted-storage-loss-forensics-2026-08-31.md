# REPORT — i-SEO Sales Manager Bot Targeted Storage Loss Forensics

## 1. Final forensic verdict

`CONFIRMED LOSS — NO RESTORE NEEDED`

Physical copies of one named untracked acceptance pack are gone with the deleted `reminder-live-accept` STORAGE contour. Later promoted waves, surviving natural-acceptance WIP, Git objects/refs, and `incoming\iseo-sales-manager-bot\**` backups cover production, rollback of current deploy, and credentials. Targeted filesystem undelete is **not** justified.

## 2. Production/canonical health

| Item | Value |
|------|--------|
| Process-line | ISEO-SALES-MANAGER-BOT — TARGETED FORENSICS FOR CONFIRMED/POSSIBLE STORAGE LOSS — NO RESTORE |
| Mode | Agent — Cursor Auto (READ-ONLY except audit/report writes) |
| Workspace | `X:\AI MARS` |
| Volume | `X:` / **`AI WS`** |
| Session branch | `mars/canonical-post-recovery` |
| Authority tip (origin) | `13b3830541f421a452b21bf08eea2e5963b1b23c` — `docs(iseo-sales-manager-bot): record natural reminder card forensic` |
| Local `HEAD` at audit | `4ad1cf7a…` (ahead of origin with unrelated `iseo-report-hub` doc commits) — **origin tip used as canonical truth**; no fetch/reset/pull |
| Tracked project integrity | Prior loss-assessment: 1454/1454; recent wave REPORT/evidence dirs present on disk + tip |
| Production depends on deleted STORAGE-only files? | **NO** → `CURRENT PRODUCTION SOURCE INTACT` |

**LOCAL-REF CHECK ONLY — NO FETCH / NO PRUNE / NO RESTORE**

Input audits used: storage-hygiene loss assessment 2026-08-31; MASTER-19C/D/E/F/G (2026-08-25).

---

## 3. Confirmed reminder-live-accept loss

### Contour

| Fact | Value |
|------|--------|
| Path | `X:\AI MARS STORAGE\git-sync-iseo-sm-reminder-live-accept-20260821` |
| Nested root | `...\repo` |
| Branch | `agent/iseo-sm-reminder-live-accept` |
| Historical HEAD | `76037630` (promoted; reachable from origin tip) |
| Historical dirty | **DIRTY(2)** = **0 modified + 2 untracked** (MASTER-19D §5.2; MASTER-19G) |
| Disk now | **ABSENT** (confirmed) |

### Exact missing items (reconstructed)

| Missing item | Type | Last known path | Known content/purpose | Surviving equivalent | Materiality | Recoverability |
|---|---|---|---|---|---|---|
| Live-final acceptance REPORT | Untracked file | `...\repo\projects\iseo-sales-manager-bot\reports\REPORT-iseo-sales-manager-bot-reminder-live-final-acceptance-v1.md` | Final live-reminder acceptance write-up for 2026-08-21 wave | **None** for that exact file. Related: tip `REPORT-...-reminder-recovery-dedupe-navigation-v1.md` @ HEAD lineage `76037630`; later natural pack in worktree; later tip evidence under `group-filter-and-test-cleanup` / `natural-reminder-action-card-fix` | `USEFUL_ACCEPTANCE_EVIDENCE` → treated as `FORENSIC_ONLY` after supersession | `UNRECOVERABLE FROM CURRENT LOGICAL SOURCES` (no transcript of full report body found); filesystem undelete would be required for exact bytes |
| Live-final acceptance evidence dir | Untracked directory | `...\repo\projects\iseo-sales-manager-bot\evidence\current-stabilization\reminder-live-final-acceptance\` | Acceptance evidence pack for same wave | **None** for that exact tree. Related evidence families on tip + natural worktree pack | Same | Same |

### Prove loss vs directory absence

| Question | Answer |
|----------|--------|
| Physical copy lost? | **YES** — both items absent from project FS, canon tip, and `incoming\...\reminder-live-accept-20260821-local\` |
| Unique information lost? | **YES (narrow)** — exact acceptance narrative/receipt of that pack. **NO** for production implementation (HEAD `76037630` promoted) |
| Later committed elsewhere? | REPORT/evidence **never** appear on tip tree |
| Equivalent later acceptance? | **YES** — surviving `reminder-final-natural-acceptance` WIP; tip natural/group/keyboard/card packs |
| Superseded by later acceptance? | **YES** (operational program continued through 2026-08-26…08-31 waves) |
| Quoted/transcribed in another report? | **Not proven** (no surviving full-body transcript located) |
| Interim stub only? | No — MASTER-19D/G treated as real acceptance pack |
| Private backup only? | No — project report/evidence under SMB locus |

Distinction:

- `PHYSICAL COPY LOST` — **YES** for both dirty items  
- `UNIQUE INFORMATION LOST` — **YES** for that pack’s text/artifacts only; **NO** for live product behavior

### Related survivor (not a substitute for the named pack)

`X:\AI MARS STORAGE\incoming\iseo-sales-manager-bot\reminder-live-accept-20260821-local\` **EXISTS** with readiness/probe JSON + scripts (`READINESS-PROBE.json`, `EXEC-SANITIZED-EXTRACT.json`, probes). It does **not** contain the REPORT or `reminder-live-final-acceptance/` evidence tree.

---

## 4. Dirty WIP contours

### 4.1 `...\git-sync-iseo-sm-current-stabilization-20260820-234315`

| Fact | Value |
|------|--------|
| Historical | DIRTY(12) = 6 modified + 6 untracked; HEAD `dd59de28`; branch `agent/iseo-sm-current-stabilization` |
| Known dirty content | Modified: index/runbooks/baseline/limitations (family). Untracked: `evidence/current-stabilization/`, `CLEAN-DUPLICATE-SOURCE-FORENSIC-v1.md`, closeout report, `maintenance/` (MASTER-19D/G) |
| Disk | ABSENT |
| Later coverage | Full CLEAN-duplicate forensic **promoted** (`a6b3dceb` + tip `evidence/.../clean-duplicate-source-forensic/` + REPORT). Later soak/group/keyboard/card waves promoted separately |
| Unique unaccounted? | Exact byte-level dirty deltas of the 6 modified tracked files **UNKNOWN**; primary named unique forensic claim **promoted** |
| Classification | **`SAFE_SUPERSEDED`** (functional/forensic primary) with residual **`POSSIBLE_LOSS_REMAINS`** only for unproven interim runbook edits — materiality LOW |

### 4.2 `...\git-sync-iseo-sm-phase3h101-20260820-215441`

| Fact | Value |
|------|--------|
| Historical | DIRTY(5) = 2 modified + 3 untracked; HEAD `321f0b8f`; branch `agent/iseo-sm-phase3h101-natural-acceptance` |
| Known dirty | Natural-acceptance report + evidence + index/limitations mods (names not porcelain-dumped beyond class) |
| Disk | ABSENT |
| Later coverage | No `phase3h101` / that pack on tip. Surviving **later** natural pack: `worktrees\iseo-smb-reminder-final-natural-01\...reminder-final-natural-acceptance\` + REPORT (DIRTY(2) still present). Tip holds post-window natural evidence in group-filter / natural-reminder-action-card packs |
| Unique unaccounted? | Interim 2026-08-20 natural-acceptance pack itself — **physical loss likely**; purpose superseded |
| Classification | **`SAFE_SUPERSEDED`** (program) / **`CONFIRMED_FORENSIC_LOSS`** (interim pack copy) — restore value **LOW** |

### 4.3 `...\git-sync-iseo-sm-phase3f2-20260805-213600`

| Fact | Value |
|------|--------|
| Historical | DIRTY(3) = 3 modified tracked + 0 untracked; HEAD `989f49f4` |
| Known dirty | phase3f2 evidence/harness/acceptance docs (tracked dirty) |
| Disk | ABSENT |
| Later coverage | Tip has full `evidence/phase3f2/**`, `evidence/phase3f2-1/**`, `evidence/phase3f2-2/**`, and phase3f2 REPORT family |
| Unique unaccounted? | Unproven dirty deltas vs tip blobs only |
| Classification | **`SAFE_SUPERSEDED`** |

### 4.4 `...\git-sync-iseo-sm-phase3h732-20260810-183429`

| Fact | Value |
|------|--------|
| Historical | DIRTY(29) = 0 modified + 29 untracked under `evidence/phase3h732/` (exec/node/harness/backup dumps) |
| Disk | ABSENT |
| Later coverage | Tip tracks **20** `evidence/phase3h732/**` files + REPORT + implementation/patches/harness. Extra untracked dumps beyond the 20 **not** proven identical or present |
| Unique unaccounted? | Possible extra forensic dump files |
| Classification | **`CONFIRMED_FORENSIC_LOSS`** (possible extra dumps) + product **`SAFE_SUPERSEDED`** — restore value **LOW** |

### 4.5 `...\git-sync-iseo-sm-phase3h41-20260806-200401`

| Fact | Value |
|------|--------|
| Historical | DIRTY(1) = 1 modified tracked repair report; HEAD `0d29cc24` |
| Disk | ABSENT |
| Later coverage | Tip: `REPORT-...-phase3h4-1-last-processed-status-repair-v1.md`, `evidence/phase3h4-1/**`, `implementation/LAST-PROCESSED-STATUS-READBACK-REPAIR-v1.md`, harness/patch |
| Unique unaccounted? | Dirty delta vs tip report only |
| Classification | **`SAFE_SUPERSEDED`** |

### Contour rollup

| Contour | Final classification |
|---------|----------------------|
| current-stabilization | `SAFE_SUPERSEDED` (+ low residual possible interim edits) |
| phase3h101 | `SAFE_SUPERSEDED` / `CONFIRMED_FORENSIC_LOSS` (interim pack) |
| phase3f2 | `SAFE_SUPERSEDED` |
| phase3h732 | `CONFIRMED_FORENSIC_LOSS` (extra dumps) + product safe |
| phase3h41 | `SAFE_SUPERSEDED` |

Cleared **SAFE** (functional): **5/5**. Materially concerning for restore: **0**.

---

## 5. KEEP sidecars

Deleted historical wrappers (MASTER-19E/F/G KEEP):

1. `X:\AI MARS STORAGE\git-sync-iseo-sm-phase3h73-20260810-163310`  
2. `X:\AI MARS STORAGE\git-sync-iseo-sm-phase3h731-20260810-171316`  
3. `X:\AI MARS STORAGE\git-sync-iseo-sm-phase3h71-20260810-154145`  
4. `X:\AI MARS STORAGE\git-sync-iseo-sm-phase3h72-20260810-161345`  

Historical contents (sanitized): `private\n8n-api.env`, `runtime\backups\` Admin/Operational JSON, residual scripts (~5.8–7.5 MB each). Disk now: **ABSENT**.

### Credential continuity

| Question | Answer |
|----------|--------|
| Another current usable credential contour known? | **YES** — `X:\AI MARS STORAGE\incoming\iseo-sales-manager-bot\phase3h8-local\private\n8n-api.env` (existence only; values **not** read; validity not tested) |
| Classification | `SECRET_COPY_LOST_BUT_CURRENT_CREDENTIAL_EXISTS` |

### Workflow backup continuity

| Family | Newer equivalent? | Canonical reconstruct? | Live match claim | Unique? | Classification |
|--------|-------------------|------------------------|------------------|---------|----------------|
| phase3h7x PRE/POST Admin/Operational JSON | **YES** — many under `incoming\iseo-sales-manager-bot\**` (e.g. natural-reminder 2026-08-31 Admin.dev PRE/POST; group-filter; keyboard; canonical-card; card-status-sync; phase3h* locals). Counts observed this audit: Admin PRE≈21, Admin POST≈20, Operational PRE≈1 | **YES** for behavior via tip patches/implementation | Current-wave PRE/POST exist for latest Admin.dev deploy | Old trees unique as **historical** copies | `REDUNDANT_BACKUP_LOSS` + `ROLLBACK_REDUNDANCY_DEGRADED` (older exact JSON gone; current rollback not sole-copy lost) |

Secret values printed: **0**.

---

## 6. Wrong-phase-rollback

| Fact | Value |
|------|--------|
| Exact path | `X:\AI MARS STORAGE\git-sync-iseo-sm-wrong-phase-rollback-20260825` (`...\repo`) |
| Phase | Mistaken **docs-only** “final knowledge consolidation” then revert |
| Branch | `tmp/iseo-sm-wrong-phase-rollback-20260825` (registry; prunable) |
| Historical HEAD | `f7d3ad80` — `revert(iseo-sales-manager): undo wrong-chat final knowledge consolidation` (reverts `08a9f568`) |
| Dirty at last known | Not recorded as DIRTY in MASTER-19G (clean later clone used for rollback) |
| Intended target | Restore tree to pre-`08a9f568` (`4af27901` equivalence for SMB docs) while keeping stable baseline `35819a63` |
| Disk contour | ABSENT |
| Supersession | **Both** `08a9f568` and `f7d3ad80` are **ancestors of origin tip**; revert already in canonical history |
| Surviving archive | `incoming\...\wrong-chat-knowledge-consolidation-rollback-20260825\` with README, ROLLBACK-NOTES, COMMIT-METADATA, DIFF-STAT, CHANGED-FILES, `WRONG-PHASE.patch` |
| Unique production recovery value lost? | **NO** (docs-only; runtime untouched; patch archived) |
| Classification | **`SAFE_PROMOTED`** / **`SAFE_SUPERSEDED`** (worktree copy redundant) |

Prior `NEEDS FORENSICS` cleared.

---

## 7. Git object survival

| SHA | Object type | Resolvable | Ancestor of origin tip | Refs | Patch/content | Lost? |
|-----|-------------|------------|------------------------|------|---------------|-------|
| `9a69ef08` | commit | **YES** | NO | `refs/heads/agent/iseo-smb-card-status-sync` (+ worktree survives) | `patch-id` **identical** to promoted `5d08ed07` | **NO** — Git content survives; functionally promoted |
| `5b479f6e` | commit | **YES** | NO | local + `origin/agent/iseo-sm-phase3h7-missed-lead-reopen` | showable; phase3h7 product docs/impl on tip (evolved) | **NO** — objects/refs survive |

**Unpromoted Git commit lost?** **NO.**

---

## 8. Recent promoted-wave continuity

| Wave | Implementation present | REPORT present | Evidence present | Canonical commits reachable |
|------|------------------------|----------------|------------------|-----------------------------|
| group-filter + legacy test cleanup | YES (impl + tip patches lineage) | YES `REPORT-...-group-filter-and-legacy-test-cleanup-v1.md` | YES `evidence/.../group-filter-and-test-cleanup/` (21 files on disk) | YES `12327f1d` |
| CLEAN duplicate source fix | YES | YES `REPORT-...-clean-duplicate-source-forensic-fix-v1.md` | YES `.../clean-duplicate-source-forensic/` (16) | YES `a6b3dceb` |
| duplicate-All keyboard fix | YES | YES `REPORT-...-keyboard-duplicate-all-fix-v1.md` | YES `.../keyboard-duplicate-all-fix/` (15) | YES `4daeb3b2` |
| canonical card reconciliation | YES (unification patches) | YES `REPORT-...-canonical-lead-card-unification-v1.md` + GIT-RECONCILIATION evidence | YES `.../canonical-lead-card-unification/` (32) | YES `dc2509d4`, `41596231` |
| natural reminder action-card fix | YES (natural-reminder patches) | YES `REPORT-...-natural-reminder-action-card-fix-v1.md` | YES `.../natural-reminder-action-card-fix/` (14) | YES `a68932dd`, `31e4fe0a`, `13b38305` |

Missing canonicalized production fix: **NONE** (HIGH severity not raised).

Surviving STORAGE contour at tip: `X:\AI MARS STORAGE\git-sync-iseo-sm-natural-reminder-action-card-20260831-141343` (CLEAN @ `13b38305`).

---

## 9. Rollback capability

| Classification | `ROLLBACK_DEGRADED` (historical KEEP trees gone) but **current-wave rollback intact** |
|----------------|----------------------------------------------------------------------------------------|
| Current Admin.dev PRE/POST | Present under `incoming\...\natural-reminder-action-card-fix-20260831-local\backups\` |
| Broader incoming PRE/POST lattice | Present across phase locals / card / group-filter / keyboard |
| Canonical reconstruct | YES via tip implementation/patches |
| Sole current-deploy rollback copy lost? | **Not proven** |

---

## 10. Credential continuity

| Check | Result |
|-------|--------|
| Old sidecar env copies | Deleted with KEEP wrappers |
| Alternate known | **YES** (`phase3h8-local\private\n8n-api.env`) |
| Values read / printed | **0** |
| Sole usable credential lost? | **NO evidence** |
| Token still valid | SAFE UNKNOWN (not tested) |
| Verdict | Credential continuity **YES** (existence); `CURRENT_CREDENTIAL_CONTINUITY_UNKNOWN` only for live validity |

---

## 11. Material-loss matrix

| Lost item/path | Unique info lost? | Materiality | Surviving equivalent | Restore value | Recommendation |
|---|---|---|---|---|---|
| `REPORT-...-reminder-live-final-acceptance-v1.md` | YES (pack text) | `USEFUL_ACCEPTANCE_EVIDENCE` / `FORENSIC_ONLY` | Later natural + tip wave evidence; tip recovery REPORT | **LOW** | `ACCEPT LOSS — NO RESTORE` |
| `evidence/.../reminder-live-final-acceptance/` | YES (pack artifacts) | Same | Same + incoming readiness probes (partial, not equivalent) | **LOW** | `ACCEPT LOSS — NO RESTORE` |
| current-stabilization dirty runbook deltas | UNKNOWN / likely interim | `FORENSIC_ONLY` | Promoted CLEAN forensic + later waves | **LOW** | No restore |
| phase3h101 natural-acceptance pack | Likely YES (interim pack) | `FORENSIC_ONLY` | Later natural worktree + tip natural evidence | **LOW** | No restore |
| phase3f2 dirty deltas | Unproven | `REDUNDANT_COPY` | Tip phase3f2 evidence/reports | **LOW** | No restore |
| phase3h732 extra untracked dumps | Possible | `FORENSIC_ONLY` | 20 tracked tip evidence files | **LOW** | No restore |
| phase3h41 dirty report delta | Unproven | `REDUNDANT_COPY` | Tip phase3h4-1 report/evidence/impl | **LOW** | No restore |
| KEEP sidecar trees (4) | Historical env/JSON copies | `REDUNDANT_COPY` / rollback redundancy | incoming credential + newer PRE/POST | **LOW** | No restore |
| wrong-phase-rollback worktree | NO | `REDUNDANT_COPY` | Git history + incoming patch archive | **LOW** | No restore |
| Git SHAs `9a69ef08` / `5b479f6e` | NO | N/A | Objects/refs present | N/A | N/A |

---

## 12. Items proven SAFE despite physical deletion

- All MASTER-19 SMB-1 clean clones / empty skeletons  
- Post-19 promoted wave worktrees (group-filter, CLEAN-dup, keyboard, card unification/reconcile) — HEADs ancestors of tip  
- phase3h7 unique-tip contour directory — objects/refs remain; product on tip  
- card-status unique SHA — worktree + identical patch to `5d08ed07`  
- wrong-phase-rollback contour — revert already on tip; patch archived in incoming  
- KEEP wrapper **trees** as sole current credential/current PRE/POST — **not** sole sources  

---

## 13. Items confirmed lost but acceptable

- Live-final acceptance REPORT + evidence directory (physical + unique pack text)  
- Likely phase3h101 interim natural-acceptance pack  
- Possible phase3h732 extra untracked dumps  
- Historical KEEP sidecar directory copies  

All: **`ACCEPT LOSS — NO RESTORE`** for practical stabilization.

---

## 14. Items recommended for targeted restore

**None.**

(If curator later wants forensic completeness only: optional search for live-final pack — still not required for operations.)

---

## 15. Items requiring filesystem-level recovery

**None justified.** Exact live-final bytes are only recoverable via undelete/shadow copy — **not recommended** given supersession and LOW restore value.

---

## 16. Current project readiness

`Can normal i-SEO Sales Manager Bot stabilization continue without restore?`

**YES**

Supporting survivors: origin tip `13b38305`; natural-reminder STORAGE contour; natural-final worktree acceptance WIP; card-status worktree; incoming backup/credential lattice.

---

## 17. Safety

| Counter | Value |
|--------:|------:|
| restored | **0** |
| recreated | **0** |
| Git mutations | **0** |
| production mutations | **0** |
| Telegram messages | **0** |
| ACCESS changes | **0** |
| AI calls | **0** |
| `reset` / `stash` / `clean` / `gc` / `worktree prune` / `add` / `commit` / `push` / `pull` | **0** |
| secret values printed | **0** |

Only writes: this audit + project-local companion report.

---

## 18. Recommended next action

**ONE action:** Profile Curator records `ACCEPT LOSS — NO RESTORE` for the live-final acceptance pack and clears the post-hygiene loss incident for i-SEO Sales Manager Bot — resume normal stabilization from origin tip `13b38305` / surviving worktrees; no recovery charter.

---

`FORENSICS COMPLETE — NO RESTORE`
