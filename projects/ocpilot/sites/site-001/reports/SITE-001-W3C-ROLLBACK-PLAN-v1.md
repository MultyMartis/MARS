# SITE-001 W3-C Rollback Plan v1

**Type:** Rollback plan instance — W3-C Footer Reduction  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`

---

## Context

| Field | Value |
|-------|-------|
| **Change request ID** | CR-SITE-001-W3C-2026-06-09 |
| **Charter** | [SITE-001-W2-WRITE-CHARTER-v1.md](SITE-001-W2-WRITE-CHARTER-v1.md) |
| **Parent rollback tiers** | [SITE-001-W1-ROLLBACK-PLAN-v1.md](SITE-001-W1-ROLLBACK-PLAN-v1.md) T1–T3 |
| **Checkpoint baseline** | `site-001-phase1-stable-2026-06` |

---

## Pre-change snapshot (W3-C)

| Artifact | Location | Confirmed |
|----------|----------|-----------|
| **W3-C file backup** | `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\pre-w3c-20260609-0259\` | **YES** — 2026-06-09 |
| **Manifest** | Same folder: `BACKUP-MANIFEST.md` | **YES** |
| **Working copy** | `.recovery-temp/site-001-w3c-work/` (local, not git) | **YES** |

**Backed-up files:**

1. `catalog/view/theme/auto/template/common/footer.twig`
2. `css/main.css`
3. `css/media.css`

---

## T1 — W3-C wave rollback

| Field | Detail |
|-------|--------|
| **Trigger** | W3-C verification FAIL; layout breakage; missing legal links; operator approves T1 |
| **Action** | FTP `STOR` restore of 3 files from `pre-w3c-20260609-0259/` |
| **Post-restore** | Clear system + modification cache; refresh modifications |
| **Verify** | `/`, `/about`, `/contact/` — footer matches pre-W3-C baseline |
| **Time target** | Same session |

---

## T2 — Full TEST restore

| Field | Detail |
|-------|--------|
| **Trigger** | Multi-wave failure; T1 insufficient; approver authorizes T2 |
| **Action** | Beget panel restore to **pre-W1** or latest full backup; or cumulative Phase 2 restore when available |
| **Expected result** | TEST matches chosen checkpoint |

---

## T3 — Emergency halt

| Field | Detail |
|-------|--------|
| **Trigger** | Wrong environment; credential exposure; operator STOP |
| **Action** | Halt writes; confirm host; escalate to T2 after approver sign-off |

---

## Rollback verification checklist

- [ ] Footer logo + phone + WhatsApp + address visible
- [ ] Policy links `/privacy-policy/`, `/user-agreement/`, `/cookie-files-policy/`
- [ ] Copyright line present
- [ ] Manufacturer lists in footer menu
- [ ] Popup forms still present in footer.twig (pre-change behavior)
