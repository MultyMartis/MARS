# SITE-001 W3ATMOSPHERE-01 Rollback Plan v1

**Type:** T1 rollback plan — W3ATMOSPHERE-01  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Tier:** **T1** (CSS restore only)

---

## Trigger conditions

- Visual success criteria < 3/5  
- Layout regression on verification URLs  
- Operator abort  
- Unexpected cache/CSS conflict  

---

## Rollback procedure (T1)

| Step | Action |
|------|--------|
| 1 | Locate backup folder `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\pre-w3atmosphere-01-YYYYMMDD-HHMM\` |
| 2 | Verify `BACKUP-MANIFEST.md` and files `css__main.css`, `css__media.css` |
| 3 | FTP STOR `css/main.css` from `css__main.css` |
| 4 | FTP STOR `css/media.css` from `css__media.css` |
| 5 | Clear OpenCart system, modification, image caches via admin |
| 6 | Refresh modification cache |
| 7 | Verify URLs: `/`, `/about`, `/contact/`, `/cars/`, `/cars/bmw/`, `/auto/`, `/auto/haval/` |
| 8 | Confirm absence of `W3ATMOSPHERE-01` marker in live CSS |

**No Beget global backup required.**

---

## Post-rollback state

Restores baseline: Phase 1 Stable + W3-V + W3V2 + W3UX-C1 (pre-atmosphere).

---

## Evidence

Backup manifest in backup folder · rollback execution report if invoked.
