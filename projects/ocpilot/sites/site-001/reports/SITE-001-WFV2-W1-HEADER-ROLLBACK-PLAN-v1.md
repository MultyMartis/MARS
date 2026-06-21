# SITE-001 WF-V2-W1 Hybrid Header Rollback Plan v1

**Type:** Rollback plan instance — WF V2 Wave 1 Hybrid Header  
**Date:** 2026-06-10  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`

---

## Context

| Field | Value |
|-------|-------|
| **Change request ID** | CR-SITE-001-WFV2-W1-2026-06-10 |
| **Charter** | [SITE-001-WFV2-W1-HEADER-WRITE-CHARTER-v1.md](SITE-001-WFV2-W1-HEADER-WRITE-CHARTER-v1.md) |
| **Pre-change baseline** | Visual Baseline V1 — W5-A/S header + W5-C PDP |
| **Parent rollback** | W5-C backup `pre-w5c-commercial-stage-20260610-0002` (PDP only) |

---

## Pre-change snapshot (WF-V2-W1)

| Artifact | Location |
|----------|----------|
| **WF-V2-W1 backup** | `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\pre-wfv2-w1-header-YYYYMMDD-HHMM\` |
| **Manifest** | Same folder: `BACKUP-MANIFEST.md` |
| **Working copy** | `.recovery-temp/site-001-wfv2-w1-work/` |

**Backed-up files:**

1. `catalog/view/theme/auto/template/common/header.twig`
2. `css/main.css`
3. `css/media.css`

---

## T1 — WF-V2-W1 wave rollback

| Field | Detail |
|-------|--------|
| **Trigger** | WF-V2-W1 verification FAIL; header not visually closer to V2 concept; overlap/sticky regression; W5-C PDP regression; operator approves T1 |
| **Action** | FTP `STOR` restore from `pre-wfv2-w1-header-YYYYMMDD-HHMM/` |
| **Files** | `header.twig`, `main.css`, `media.css` |
| **Alternative (CSS-only partial)** | Remove WF-V2-W1 CSS block between markers; restore header.twig if twig changed |
| **Post-restore** | Clear system + modification + image cache; refresh modifications |
| **Verify** | 8-URL matrix; W5-C markers on used PDP; W5-A/S header restored |
| **Time target** | Same session |

---

## T2 — Full TEST restore

| Field | Detail |
|-------|--------|
| **Trigger** | Multi-wave failure; T1 insufficient; approver authorizes T2 |
| **Action** | Beget panel restore — **operator only** |
| **Note** | Do **not** use Beget global restore without explicit operator authorization |

---

## Post-rollback state

Visual Baseline V1 header (W5-A/S graphite shell) restored. W5-C Used PDP **unchanged** (product.twig not in scope).
