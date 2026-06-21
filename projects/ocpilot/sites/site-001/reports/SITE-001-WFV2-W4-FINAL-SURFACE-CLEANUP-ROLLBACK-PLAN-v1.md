# SITE-001 WF-V2-W4 Final Surface Cleanup Rollback Plan v1

**Type:** T1 rollback instance — WF V2 Wave 4 Used PDP Final Surface Cleanup  
**Date:** 2026-06-10  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** TEST — `https://sibcar.new-site.space/`  
**Change request:** CR-SITE-001-WFV2-W4-2026-06-10

---

## Trigger conditions

Execute T1 rollback if any of:

1. WF-V2-W4 verification matrix fails (8 URLs)  
2. Header or catalog regression detected  
3. Modal or form functional regression  
4. Operator visual gate fails — page still looks boxed  
5. Unrecoverable Twig/CSS error on PDP  

---

## Rollback procedure (T1)

### Step 1 — Identify backup

Locate latest pre-write backup:

```
C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\pre-wfv2-w4-final-surface-cleanup-YYYYMMDD-HHMM\
```

Verify `BACKUP-MANIFEST.md` lists 3 files.

### Step 2 — FTP restore

| Remote path | Restore from local name |
|-------------|-------------------------|
| `catalog/view/theme/auto/template/product/product.twig` | `catalog__view__theme__auto__template__product__product.twig` |
| `css/main.css` | `css__main.css` |
| `css/media.css` | `css__media.css` |

### Step 3 — Cache clear

OpenCart Admin → clear system + modification + image cache → refresh modifications.

### Step 4 — Verify rollback

| Check | Expected |
|-------|----------|
| Used PDP | `wfv2-layout-pdp` present · `wfv2-surface-pdp` **absent** |
| CSS | `WF-V2-W4 Final Surface Cleanup` **absent** from main.css + media.css |
| CSS | `WF-V2-W3 PDP Layout Recomposition` **present** |
| 8-URL matrix | All PASS |
| Modal | Opens and closes |

---

## Prior baselines

| Wave | Backup ID |
|------|-----------|
| WF-V2-W3 (immediate prior) | `pre-wfv2-w3-layout-recomposition-20260610-0413` |
| WF-V2-W2A | `pre-wfv2-w2a-pdp-anatomy-rebuild-20260610-0401` |

---

## CSS-only partial rollback

If twig is fine but CSS causes issues:

1. Remove WF-V2-W4 block from `main.css` (between W4 header comment and `/* END WF-V2-W4 Final Surface Cleanup — main */`)  
2. Remove WF-V2-W4 block from `media.css` (between W4 header comment and `/* END WF-V2-W4 Final Surface Cleanup — responsive */`)  
3. Cache clear + verify  

---

## Operator script

Automated rollback reference: `.recovery-temp/site-001-wfv2-w4-execute.py` (reverse upload from backup dir).

Manual: STOR 3 files from backup + admin cache clear.

---

## Post-rollback state

Site returns to **WF-V2-W3** baseline — layout recomposition intact, pre-W4 surface chrome restored.
