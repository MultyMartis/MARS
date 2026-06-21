# SITE-001 W3-V Rollback Plan v1

**Type:** Rollback plan instance — W3-V Visual Layer Refresh  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`

---

## Context

| Field | Value |
|-------|-------|
| **Change request ID** | CR-SITE-001-W3V-2026-06-09 |
| **Charter** | [SITE-001-W3V-WRITE-CHARTER-v1.md](SITE-001-W3V-WRITE-CHARTER-v1.md) |
| **Parent rollback tiers** | [SITE-001-W1-ROLLBACK-PLAN-v1.md](SITE-001-W1-ROLLBACK-PLAN-v1.md) T1–T3 |
| **Checkpoint baseline** | `site-001-phase1-stable-2026-06` |

---

## Pre-change snapshot (W3-V)

| Artifact | Location | Confirmed |
|----------|----------|-----------|
| **W3-V file backup** | `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\pre-w3v-<timestamp>\` | **At execution** |
| **Manifest** | Same folder: `BACKUP-MANIFEST.md` | **At execution** |
| **Working copy** | `.recovery-temp/site-001-w3v-work/` (local, not git) | **At execution** |

**Backed-up files:**

1. `css/main.css`
2. `css/media.css`

---

## T1 — W3-V wave rollback

| Field | Detail |
|-------|--------|
| **Trigger** | W3-V verification FAIL; layout shift; broken CSS; operator approves T1 |
| **Action** | FTP `STOR` restore of 2 CSS files from `pre-w3v-*` backup |
| **Alternative** | Remove W3-V marker block `SITE-001 W3-V Visual Layer Refresh` from `main.css` + restore `media.css` |
| **Post-restore** | Clear system + modification cache |
| **Verify** | `/`, `/about`, `/contact/`, `/cars/`, `/auto/` — visual matches pre-W3-V baseline |
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
| **Trigger** | Wrong environment; credential exposure; operator STOP |
| **Action** | Halt writes; confirm host; escalate to T2 after approver sign-off |

---

## Rollback verification checklist

- [ ] Footer structure unchanged from pre-W3-V baseline
- [ ] Header/navigation intact
- [ ] Catalog cards render without overlap
- [ ] PDP price and CTA buttons visible
- [ ] Forms present and functional (modal triggers)
- [ ] No W3-V CSS marker block in live `main.css` (after T1 restore)
