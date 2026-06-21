# SITE-001 W5-A Header Shell Recomposition Rollback Plan v1

**Type:** Rollback plan instance — W5-A Header Shell  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`

---

## Context

| Field | Value |
|-------|-------|
| **Change request ID** | CR-SITE-001-W5A-2026-06-09 |
| **Charter** | [SITE-001-W5A-HEADER-SHELL-WRITE-CHARTER-v1.md](SITE-001-W5A-HEADER-SHELL-WRITE-CHARTER-v1.md) |
| **Design authority** | [SITE-001-W5-FIRST-IMPRESSION-BLUEPRINT-v1.md](SITE-001-W5-FIRST-IMPRESSION-BLUEPRINT-v1.md) §2.1 |
| **Parent rollback tiers** | [SITE-001-W1-ROLLBACK-PLAN-v1.md](SITE-001-W1-ROLLBACK-PLAN-v1.md) T1–T3 |
| **Checkpoint baseline** | W4.1 deployed state (post-2026-06-09) |

---

## Pre-change snapshot (W5-A)

| Artifact | Location |
|----------|----------|
| **W5-A stable backup** | `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\pre-w5a-header-shell-YYYYMMDD-HHMM\` |
| **Manifest** | Same folder: `BACKUP-MANIFEST.md` |
| **Working copy** | `.recovery-temp/site-001-w5a-work/` |

**Backed-up files:**

1. `catalog/view/theme/auto/template/common/header.twig`
2. `css/main.css`
3. `css/media.css`

---

## T1 — W5-A wave rollback

| Field | Detail |
|-------|--------|
| **Trigger** | W5-A verification FAIL; 3-second test FAIL; header/mobile break; operator approves T1 |
| **Action** | FTP `STOR` restore from `pre-w5a-header-shell-YYYYMMDD-HHMM/` |
| **Files** | `header.twig`, `main.css`, `media.css` |
| **Post-restore** | Clear system + modification + image cache; refresh modifications |
| **Verify** | 8 URL matrix; W4 markers on used PDP; header functional; W4.1 state restored |
| **Time target** | Same session |

---

## T2 — W4.1 rollback (if W5-A regressed beyond W4.1 baseline)

| Field | Detail |
|-------|--------|
| **Trigger** | T1 restores W5-A pre-state but operator needs pre-W4.1 anatomy |
| **Action** | FTP restore from `pre-w4-1-stable-20260609-1506/` |
| **Files** | `header.twig`, `product.twig`, `main.css`, `media.css` |

---

## T3 — Emergency halt

Stop all writes; document state; await operator decision.

---

## Preserve on T1 rollback

| Wave | Expect after T1 |
|------|-----------------|
| W4 Used PDP | **Unchanged** — product.twig not modified in W5-A |
| W4.1 | Restored to pre-W5-A W4.1 deploy |
| W3UX-C1 · W3ATMOSPHERE | Preserved |
| Phase 1 checkpoint | Preserved |
