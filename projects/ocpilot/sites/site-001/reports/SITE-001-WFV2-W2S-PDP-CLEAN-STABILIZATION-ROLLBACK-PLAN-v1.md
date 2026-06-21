# SITE-001 WF-V2-W2S PDP Clean Stabilization Rollback Plan v1

**Type:** T1 rollback procedure  
**Date:** 2026-06-10  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** TEST only — `https://sibcar.new-site.space/`  
**Change request:** CR-SITE-001-WFV2-W2S-2026-06-10

---

## Trigger conditions

Execute T1 rollback when any of:

1. Operator verdict: W2-S = FAIL (not cleaner, only less decorated)  
2. Used PDP regression — modals, forms, calculator, or layout break  
3. W2S CSS leaks to non-used pages  
4. Header, catalog, or new PDP visually changed  
5. Verification matrix < 8/8 PASS  

---

## Recovery point

**Backup ID:** `pre-wfv2-w2s-pdp-clean-YYYYMMDD-HHMM`  
**Path:** `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\pre-wfv2-w2s-pdp-clean-YYYYMMDD-HHMM\`

| Remote path | Local backup name |
|-------------|-------------------|
| `catalog/view/theme/auto/template/product/product.twig` | `catalog__view__theme__auto__template__product__product.twig` |
| `css/main.css` | `css__main.css` |
| `css/media.css` | `css__media.css` |

---

## T1 procedure

### Step 1 — Restore files (FTP STOR)

Upload all 3 files from backup directory to TEST FTP root paths (same remote paths as backup manifest).

### Step 2 — Clear caches (Admin)

1. System cache  
2. Modification cache  
3. Image cache  
4. Modification refresh  

### Step 3 — Verify rollback

| Check | Expect |
|-------|--------|
| `wfv2-clean-pdp` on used PDP | **ABSENT** |
| `wfv2-flat-pdp` on used PDP | **PRESENT** (W2 baseline restored) |
| WF-V2-W2S CSS block in `main.css` | **ABSENT** |
| WF-V2-W2 CSS block in `main.css` | **PRESENT** |
| 8-URL verification matrix | **PASS** |
| Modals + dropdowns | **PASS** |

### Step 4 — Document

Record rollback execution in operator channel. Do not commit unless explicitly authorized.

---

## Fallback baseline

If W2-S backup is corrupt, restore from prior W2 checkpoint:

`pre-wfv2-w2-flat-pdp-20260610-0304`

---

## Rollback markers to remove (manual CSS edit alternative)

If partial rollback needed, remove from `main.css`:

```
/* WF-V2-W2S Clean Used PDP Stabilization */
…through…
/* END WF-V2-W2S Clean Used PDP Stabilization — main */
```

And from `media.css`:

```
/* WF-V2-W2S Clean Used PDP Stabilization — responsive */
…through…
/* END WF-V2-W2S Clean Used PDP Stabilization — responsive */
```

Remove `wfv2-clean-pdp` class from `product.twig` commercial stage wrapper.

---

## Authorization

Rollback: **AUTHORIZED** for TEST at operator request.  
Production rollback: **NOT AUTHORIZED** without separate approval.
