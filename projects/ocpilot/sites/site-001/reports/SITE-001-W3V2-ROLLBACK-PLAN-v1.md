# SITE-001 W3V2 Rollback Plan v1

**Type:** Rollback plan instance — W3V2 Visual Identity Refresh  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`

---

## Pre-change snapshot

| Artifact | Location | Confirmed |
|----------|----------|-----------|
| **W3V2 file backup** | `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\pre-w3v2-20260609-0451\` | **DONE** |
| **Manifest** | `BACKUP-MANIFEST.md` in same folder | **DONE** |
| **Working copy** | `.recovery-temp/site-001-w3v2-work/` | **DONE** |

**Backed-up files:** `css/main.css`, `css/media.css`

---

## T1 — W3V2 wave rollback

| Field | Detail |
|-------|--------|
| **Trigger** | Verification FAIL; contrast regression; operator rejects visual direction |
| **Action** | FTP `STOR` restore of 2 CSS files from `pre-w3v2-20260609-0451` |
| **Alternative** | Remove `SITE-001 W3V2 Visual Identity Refresh` block + `:root` W3V2 tokens from `main.css`; remove W3V2 block from `media.css` |
| **Post-restore** | Clear system + modification + image cache |
| **Verify** | 7/7 URLs — visual matches pre-W3V2 baseline |
| **Time target** | Same session |

---

## T2 / T3

Per [SITE-001-W1-ROLLBACK-PLAN-v1.md](SITE-001-W1-ROLLBACK-PLAN-v1.md) — full TEST restore or emergency halt if T1 insufficient.

---

## Rollback status

**NOT REQUIRED** — execution passed verification (see [SITE-001-W3V2-DECISION-v1.md](SITE-001-W3V2-DECISION-v1.md)).
