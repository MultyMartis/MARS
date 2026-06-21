# SITE-001 W4.1 Header & Hero Authority Rollback Plan v1

**Type:** Rollback plan instance — W4.1 Header & Hero Authority  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`

---

## Context

| Field | Value |
|-------|-------|
| **Change request ID** | CR-SITE-001-W4-1-2026-06-09 |
| **Charter** | [SITE-001-W4-1-HEADER-HERO-WRITE-CHARTER-v1.md](SITE-001-W4-1-HEADER-HERO-WRITE-CHARTER-v1.md) |
| **Parent rollback tiers** | [SITE-001-W1-ROLLBACK-PLAN-v1.md](SITE-001-W1-ROLLBACK-PLAN-v1.md) T1–T3 |
| **Checkpoint baseline** | W4 Used PDP accepted state |

---

## Pre-change snapshot (W4.1)

| Artifact | Location |
|----------|----------|
| **W4.1 stable backup** | `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\pre-w4-1-stable-YYYYMMDD-HHMM\` |
| **Manifest** | Same folder: `BACKUP-MANIFEST.md` |
| **Working copy** | `.recovery-temp/site-001-w4-1-work/` |

**Backed-up files:**

1. `catalog/view/theme/auto/template/common/header.twig`
2. `catalog/view/theme/auto/template/common/footer.twig`
3. `catalog/view/theme/auto/template/product/product.twig`
4. `css/main.css`
5. `css/media.css`

---

## T1 — W4.1 wave rollback

| Field | Detail |
|-------|--------|
| **Trigger** | W4.1 verification FAIL; visual impact <7/10; header/mobile break; W4 PDP regression; operator approves T1 |
| **Action** | FTP `STOR` restore from `pre-w4-1-stable-YYYYMMDD-HHMM/` |
| **Files** | `header.twig`, `product.twig`, `main.css`, `media.css` · `footer.twig` only if modified |
| **Post-restore** | Clear system + modification + image cache; refresh modifications |
| **Verify** | 9 URL matrix; W4 markers on used PDP; header functional |
| **Time target** | Same session |

---

## T2 — Full TEST restore

| Field | Detail |
|-------|--------|
| **Trigger** | Multi-wave failure; T1 insufficient; approver authorizes T2 |
| **Action** | Beget panel restore — **operator only**; not authorized in W4.1 task |
| **Note** | Do **not** use Beget global restore without explicit operator authorization |

---

## T3 — Emergency halt

Stop all writes; document state; await operator decision.

---

## Preserve on rollback

| Wave | Expect after T1 |
|------|-----------------|
| W4 Used PDP | Restored to pre-W4.1 state (W4 intact) |
| W3UX-C1 | Preserved |
| W3ATMOSPHERE | Preserved |
| Phase 1 checkpoint | Preserved |

*SITE-001 W4.1 Header & Hero Authority Rollback Plan v1*
