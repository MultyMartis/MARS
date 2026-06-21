# SITE-001 WF-V2-W3 PDP Layout Recomposition Rollback Plan v1

**Type:** Rollback plan instance — WF V2 Wave 3 Layout Recomposition  
**Date:** 2026-06-10  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`

---

## Context

| Field | Value |
|-------|-------|
| **Change request ID** | CR-SITE-001-WFV2-W3-2026-06-10 |
| **Charter** | [SITE-001-WFV2-W3-LAYOUT-RECOMPOSITION-WRITE-CHARTER-v1.md](SITE-001-WFV2-W3-LAYOUT-RECOMPOSITION-WRITE-CHARTER-v1.md) |
| **Pre-change baseline** | WF-V2-W2A PDP Anatomy Rebuild |
| **Parent rollback** | W2A backup `pre-wfv2-w2a-pdp-anatomy-rebuild-20260610-0401` |

---

## Pre-change snapshot (WF-V2-W3)

| Artifact | Location |
|----------|----------|
| **WF-V2-W3 backup** | `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\pre-wfv2-w3-layout-recomposition-YYYYMMDD-HHMM\` |
| **Manifest** | Same folder: `BACKUP-MANIFEST.md` |
| **Working copy** | `.recovery-temp/site-001-wfv2-w3-work/` |

**Backed-up files:**

1. `catalog/view/theme/auto/template/product/product.twig`
2. `css/main.css`
3. `css/media.css`

---

## T1 — WF-V2-W3 wave rollback

| Field | Detail |
|-------|--------|
| **Trigger** | W3 verification FAIL; hero/offer regression; catalog/homepage leak; operator approves T1 |
| **Action** | FTP `STOR` restore from `pre-wfv2-w3-layout-recomposition-YYYYMMDD-HHMM/` |
| **Files** | `product.twig`, `main.css`, `media.css` |
| **Alternative (CSS-only partial)** | Remove WF-V2-W3 CSS blocks between markers; restore twig if DOM changed |
| **Post-restore** | Clear system + modification + image cache; refresh modifications |
| **Verify** | 8-URL matrix; W2A markers on used PDP; W3 markers absent |
| **Time target** | Same session |

---

## T2 — Full TEST restore

| Field | Detail |
|-------|--------|
| **Trigger** | Multi-wave failure; T1 insufficient; approver authorizes T2 |
| **Action** | Beget panel restore — **operator only** |
| **Note** | Do **not** use Beget global restore without explicit operator authorization |

---

## T3 — Emergency halt

| Field | Detail |
|-------|--------|
| **Trigger** | Live breakage beyond TEST scope |
| **Action** | Halt writes; operator notification; no further FTP until triage |
