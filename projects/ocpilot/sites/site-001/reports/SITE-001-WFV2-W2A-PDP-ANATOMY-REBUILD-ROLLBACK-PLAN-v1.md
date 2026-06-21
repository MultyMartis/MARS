# SITE-001 WF-V2-W2A PDP Anatomy Rebuild Rollback Plan v1

**Type:** T1 rollback instance — WF V2 Wave 2-A  
**Date:** 2026-06-10  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** TEST — `https://sibcar.new-site.space/`  
**Backup ID pattern:** `pre-wfv2-w2a-pdp-anatomy-rebuild-YYYYMMDD-HHMM`

---

## Trigger conditions

| Condition | Action |
|-----------|--------|
| 8/8 URL verify **FAIL** | T1 immediate |
| Commercial stage anatomy broken (missing H1, trust, hero) | T1 |
| Equipment/Credit grid breaks forms or calculator | T1 |
| Reviews or lcd_display in wrong order breaking layout | T1 |
| Operator HITL rejects anatomy rebuild | T1 |

---

## T1 procedure

1. Locate backup folder: `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\pre-wfv2-w2a-pdp-anatomy-rebuild-*`
2. FTP **STOR** restore:

| Local backup file | Remote path |
|-------------------|-------------|
| `catalog__view__theme__auto__template__product__product.twig` | `catalog/view/theme/auto/template/product/product.twig` |
| `css__main.css` | `css/main.css` |
| `css__media.css` | `css/media.css` |

3. Admin cache clear: system · modification · image · modification refresh
4. Re-run 8-URL verification matrix
5. Confirm markers: `wfv2-clean-pdp` **YES** · `wfv2-anatomy-pdp` **NO**

**Note:** `header.twig` is backed up for safety but **not modified** by W2A — restore only if accidentally changed.

---

## T2 fallback (pre-W2A baseline)

If T1 backup corrupt or missing:

Restore from WF-V2-W2S checkpoint: `pre-wfv2-w2s-pdp-clean-20260610-0330`

Files: `product.twig`, `main.css`, `media.css`

---

## Post-rollback state

| Element | Expected |
|---------|----------|
| H1 | Above commercial stage in `w4-1-pdp-top` |
| Reviews | Between equipment and credit |
| Credit car image | Present in `used_car__credit__slider` |
| `lcd_display.product` | Between trust and equipment |
| Layer 3 grid | Absent |

---

## Evidence

Record in execution report: backup ID, restore timestamp, post-rollback 8/8 matrix, screenshot path.

*SITE-001 WF-V2-W2A PDP Anatomy Rebuild Rollback Plan v1*
