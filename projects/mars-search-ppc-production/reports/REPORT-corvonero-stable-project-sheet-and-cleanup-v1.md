# REPORT — Corvonero stable project sheet and cleanup v1

**Date:** 2026-08-12  
**Programme:** mars-search-ppc-production  
**Project:** CorvoNero / Корво Неро  
**Operator mode:** human-operated Cursor charter  
**Git checkpoint this task:** **NO / NOT PERFORMED**

---

## Verdict

```
CORVONERO STABLE PROJECT SHEET AND CLEANUP:
PASS

Stable sheet:
CREATED

XLSX sheets:
10/10

Artifact index:
CREATED

Cleanup:
EXECUTED_SCOPED_TOOLS_ONLY

Deleted files:
3

Backup:
CREATED

Campaign package:
UNCHANGED

Legal DOCX:
UNCHANGED

Landing DOCX:
UNCHANGED

Client materials:
UNCHANGED

Reports:
PRESERVED

Foreign WIP:
PRESERVED

Git checkpoint:
NOT PERFORMED
```

---

## 1. Environment verification (preflight)

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Drive | `X:` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD (at task start) | `6d16de0e70082a664784025c134932671ed1ab18` |
| `origin/mars/canonical-post-recovery` | `a14a97c9fbb797d01477b7b08a546380c71ef080` |
| Unpushed commits | Present (foreign iSEO/report-hub lineage) — **PRESERVED**, not pushed/pulled |
| Staged changes | Present (~699 foreign client-ops paths) — **PRESERVED**, not touched |
| This task pull/reset/clean/stash/restore | **NOT RUN** |
| Schedulers / runtime jobs | **NOT STARTED** |

**STOP signals observed (documented, not acted on for foreign WIP):**

- `EXISTING STAGED CHANGES PRESENT` — foreign client-ops; out of scope
- `UNPUSHED COMMITS PRESENT` — foreign iSEO; out of scope
- `REMOTE/HEAD MISMATCH` — no pull/push performed

Corvonero-scoped Storage writes + repo reference creation + exact `.tools` temporary helper deletion proceeded under this charter while preserving foreign WIP.

---

## 2. Git status — Corvonero-relevant before

Untracked Corvonero `.tools` helpers present before cleanup (subset):

- `.tools/corvonero-landing-prelaunch-scan-v1.py`
- `.tools/corvonero-landing-scan-result-v1.json`
- `.tools/corvonero-legal-pages-docx-pack-v1.py`
- `.tools/corvonero-checkpoint-inventory.json`
- `.tools/corvonero-pre-export-backup-summary.json`
- (+ other `corvonero-*` helpers kept)

Also present: legal-pages refs, prior REPORT-corvonero-* files, historical authority JSON (foreign-to-this-wave Corvonero WIP preserved).

---

## 3. Stable sheet package created

**Storage directory:**

`X:\AI MARS STORAGE\exports\corvonero\CORVONERO-STABLE-PROJECT-SHEET-2026-08-12\`

| File | Role |
|------|------|
| `01-CORVONERO-STABLE-PROJECT-SHEET-v1.xlsx` | Stable workbook (10 sheets) |
| `01-CORVONERO-STABLE-PROJECT-SHEET-v1.md` | Human-readable stable sheet |
| `CORVONERO-STABLE-PROJECT-MANIFEST-v1.json` | Package manifest |
| `CORVONERO-STABLE-PROJECT-SHA256SUMS-v1.txt` | SHA256 sums |

**XLSX sheets (10/10):** Dashboard, Current State, Campaign Package, Landing Pages, Legal Pages, Performance Snapshot, Decisions, Open Items, Artifact Index, Cleanup.

**Repository references (no XLSX in Git):**

- `projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-STABLE-PROJECT-SHEET-v1.md`
- `projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-STABLE-PROJECT-SHEET-v1.json`

Builder/validator helpers left only under Storage package (`_build_stable_sheet_and_cleanup_v1.py`, `_validate_v1.py`) — not Git.

---

## 4. Current Corvonero state recorded

| Field | Value |
|-------|-------|
| Current state | OPERATIONAL / LAUNCHED / PERFORMANCE_OBSERVATION |
| Launch / import / adjustment | **OPERATOR_REPORTED** |
| Authority | V2.6 |
| Deployable | V2.6.2 |
| Package path | `X:\AI MARS STORAGE\exports\corvonero\CORVONERO-CAMPAIGN-V2.6.2-FINAL-2026-06-30\` |
| Structure | 10 campaigns / 71 groups / 926 keyword placements / 71 ads |
| Site | https://lk.corvonero.ru/ |
| Entity | ИП Никифоров Роман Вадимович |
| Email | contact@corvonero.ru |
| Phone | +7 (383) 390-29-28 (from 2026-07-10 prelaunch scan) |
| Direct actual | **SAFE UNKNOWN** (no local Direct export found) |
| Legal | 4 DOCX; email cleaned; review **NOT COMPLETED**; publication **SAFE UNKNOWN** |
| Landing | Prelaunch 5/5 **READY_WITH_WARNINGS** (2026-07-10); current live **SAFE UNKNOWN** |
| Performance | Preliminary OPERATOR_REPORTED; exact final statistics **pending** |
| Closure checkpoint | `2e7daa32833dec6b15cca3d321833054d4597e72` |

### Preliminary performance (operator/chat — not invented metrics)

- First two leads moved into deal — OPERATOR_REPORTED
- ~3 phone leads may exist outside Metrica — OPERATOR_REPORTED / approximate
- Stronger directions: сопровождение 1С / техподдержка / ошибки 1С; маркировка / Честный знак; программист 1С Новосибирск
- Weaker / not yet confirmed: интеграции 1С; доработка/разработка 1С; удалённый программист 1С; удалённая маркировка
- Local final statistics files in approved roots: **none found**

---

## 5. Artifact inventory summary

Important artifacts indexed in the stable sheet (Git + Storage):

- Semantic authority V2.6 (Git)
- Deployable V2.6.2 package (Storage)
- Client approval pack (Storage)
- Final + Roman landing DOCX packs (Storage)
- Legal DOCX pack + prelaunch scan (Storage)
- Current artifact index, cleanup inventory, problem register, lessons learned (Git)
- Reports under `projects/mars-search-ppc-production/reports/`
- MIG semantic runs under `X:\AI MARS STORAGE\mig\corvonero\`
- This stable sheet package (Storage)

---

## 6. Cleanup dry-run / execution

### Allowed delete scope

Only:

- `X:\AI MARS\.tools\corvonero-*.py`
- `X:\AI MARS\.tools\corvonero-*.json`

and only when clearly temporary.

### Dry-run eligible (charter-known temporary helpers)

1. `X:\AI MARS\.tools\corvonero-landing-prelaunch-scan-v1.py`
2. `X:\AI MARS\.tools\corvonero-landing-scan-result-v1.json`
3. `X:\AI MARS\.tools\corvonero-legal-pages-docx-pack-v1.py`

### Backup (created before deletion)

`X:\AI MARS STORAGE\backups\search-ppc\CORVONERO-CLEANUP-PREDELETE-2026-08-12-213432\`

Contains:

- `.tools/` copies of the three files
- `CORVONERO-CLEANUP-PREDELETE-MANIFEST-v1.json`
- `CORVONERO-CLEANUP-PREDELETE-SHA256SUMS-v1.txt`
- `README-CORVONERO-CLEANUP-PREDELETE-v1.md`

SHA256 verified copy-before-unlink for each file. Deletion via Python `os.unlink` on exact files only (no `Remove-Item`, no directory deletes).

### Deleted exact files (3)

| Path | SHA256 | Backup |
|------|--------|--------|
| `.tools/corvonero-landing-prelaunch-scan-v1.py` | `e1e46395e132a99eb4794c68e6e0e992af39c652f6d41dd194141d34966d358e` | backup `.tools/` copy |
| `.tools/corvonero-landing-scan-result-v1.json` | `0477a5daddc05771615c0563b817e7b62a08417743dafcd8d229f39882fa322c` | backup `.tools/` copy |
| `.tools/corvonero-legal-pages-docx-pack-v1.py` | `eaf562f77409550b9469ee160fe5be712a7899f9a9effd8f2ecdd2ac22fb6d60` | backup `.tools/` copy |

### Kept `.tools/corvonero-*` (16) — inventory only

Classified as `CLEANUP_CANDIDATE_REQUIRES_OPERATOR_APPROVAL` or `SAFE_UNKNOWN_KEEP` (not deleted):

- checkpoint `*.ps1` / inventory JSON
- commander / export / final checkpoint `*.py` / `*.cjs`
- `corvonero-pre-export-backup-summary.json`
- `corvonero-pre-export-backup-v1.py`
- etc.

### Storage export temp files

Prior `_review-temp-*`, `_extract-*`, `_test-*` under `exports/corvonero/` inventoried as **CLEANUP_CANDIDATE_REQUIRES_OPERATOR_APPROVAL** — **Kept** (outside this-task delete allowlist).

---

## 7. What was not touched

- Campaign package V2.6.2
- Legal DOCX pack contents
- Landing DOCX packs
- Client approval materials
- Stable HTML client materials
- All `REPORT-corvonero-*` reports
- Storage backups (except new cleanup backup creation)
- Yandex Direct / Commander
- Live website (no rescan)
- Foreign staged WIP / unpushed commits
- No stage / commit / push

---

## 8. SAFE UNKNOWN items

- Direct actual campaign state (no local export)
- Current live landing state (not rescanned)
- Current published legal page status (was 404 on 2026-07-10; not rescanned)
- Exact final advertising statistics
- Metrica/goals current proof
- Exact dates of Direct upload/launch/adjustment
- Whether remaining `.tools/corvonero-*` helpers are still needed for reproduction

---

## 9. Validation

| Check | Result |
|-------|--------|
| Stable XLSX exists / readable | PASS |
| Sheets 10/10 | PASS |
| Manifest + SHA256 | PASS (sums match) |
| Repo references created | PASS |
| Cleanup backup if deletion | PASS |
| Deleted only exact `.tools/corvonero-*` files | PASS (3 files) |
| No directories deleted | PASS |
| Storage export packages unchanged | PASS |
| Reports preserved | PASS |
| Foreign WIP preserved | PASS (staged count still present) |
| Git checkpoint | NOT PERFORMED |

---

## 10. Git status after (Corvonero-scoped)

**New untracked (this task):**

- `projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-STABLE-PROJECT-SHEET-v1.md`
- `projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-STABLE-PROJECT-SHEET-v1.json`
- `projects/mars-search-ppc-production/reports/REPORT-corvonero-stable-project-sheet-and-cleanup-v1.md` (this file)

**Removed from working tree (were untracked; now deleted after backup):**

- `.tools/corvonero-landing-prelaunch-scan-v1.py`
- `.tools/corvonero-landing-scan-result-v1.json`
- `.tools/corvonero-legal-pages-docx-pack-v1.py`

**Still present untracked Corvonero `.tools` (kept):**

- `.tools/corvonero-checkpoint-inventory.json`
- `.tools/corvonero-pre-export-backup-summary.json`
- (+ tracked/other kept helpers as applicable)

**Classification:**

| Class | Paths |
|-------|-------|
| Stable sheet repo references | `CORVONERO-STABLE-PROJECT-SHEET-v1.md`, `.json` |
| Stable report | this REPORT |
| Cleanup backup | Storage only (not Git) |
| Deleted `.tools` files | 3 exact temporary helpers |
| Unrelated WIP | foreign staged client-ops + unpushed iSEO — **PRESERVED** |

**Staging / commit / push:** none.

---

## 11. Next safe operational gate (recorded, not executed)

1. Final statistics + Direct reconciliation export
2. Legal review completion + publication confirmation (or live legal scan)
3. Optional operator approval for broader cleanup candidates (Storage `_temp` + remaining `.tools` helpers)
4. Optional selective Git checkpoint for Corvonero stable sheet refs + this report only (separate charter)
