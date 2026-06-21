# SITE-001 W4 Used PDP Rollback Plan v1

**Type:** Rollback plan instance — W4 Used PDP Structural Visual Slice  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`

---

## Context

| Field | Value |
|-------|-------|
| **Change request ID** | CR-SITE-001-W4-2026-06-09 |
| **Charter** | [SITE-001-W4-USED-PDP-WRITE-CHARTER-v1.md](SITE-001-W4-USED-PDP-WRITE-CHARTER-v1.md) |
| **Parent rollback tiers** | [SITE-001-W1-ROLLBACK-PLAN-v1.md](SITE-001-W1-ROLLBACK-PLAN-v1.md) T1–T3 |
| **Checkpoint baseline** | `site-001-phase1-stable-2026-06` |

---

## Pre-change snapshot (W4)

| Artifact | Location | Confirmed |
|----------|----------|-----------|
| **W4 file backup** | `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\pre-w4-20260609\` | **YES** — 2026-06-09 |
| **Manifest** | Same folder: `BACKUP-MANIFEST.md` | **YES** |
| **Working copy** | `.recovery-temp/site-001-w4-work/` | **YES** |

**Backed-up files:**

1. `catalog/view/theme/auto/template/product/product.twig`
2. `css/main.css`
3. `css/media.css`

---

## T1 — W4 wave rollback

| Field | Detail |
|-------|--------|
| **Trigger** | W4 verification FAIL; used PDP layout break; regression on non-PDP URLs; operator approves T1 |
| **Action** | FTP `STOR` restore of 3 files from `pre-w4-20260609/` |
| **Post-restore** | Clear system + modification cache; refresh modifications |
| **Verify** | Used PDP matches pre-W4 baseline; `/cars/`, `/`, `/about`, `/contact/` unchanged |
| **Time target** | Same session |

---

## T2 — Full TEST restore

| Field | Detail |
|-------|--------|
| **Trigger** | Multi-wave failure; T1 insufficient; approver authorizes T2 |
| **Action** | Beget panel restore to Phase 1 checkpoint or latest full backup |
| **Expected result** | TEST matches chosen checkpoint |

---

## T3 — Emergency halt

| Field | Detail |
|-------|--------|
| **Trigger** | Scope breach (PHP/JS/DB touched); security incident; environment mismatch |
| **Action** | STOP all writes; preserve backups; approver decides T1 vs T2 |

---

## Verification after rollback

| Check | Pass |
|-------|------|
| Used PDP loads without PHP/twig errors | ☐ |
| No `w4-used-*` classes in live HTML | ☐ |
| `/cars/` catalog cards unchanged | ☐ |
| Homepage loads | ☐ |
| `/about`, `/contact/` load | ☐ |
| Rollback recorded in execution REPORT | ☐ |

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-09 | **CREATED** — W4 rollback bound to CR-SITE-001-W4-2026-06-09 |

*SITE-001 W4 Rollback Plan v1 — planning instance.*
