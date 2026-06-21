# SITE-001 W5-C Used PDP Rollback Plan v1

**Type:** T1 rollback instance — W5-C Used PDP Commercial Stage  
**Date:** 2026-06-10  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** TEST only  
**Backup ID:** `pre-w5c-commercial-stage-20260610-0002`

---

## Trigger conditions

Execute T1 rollback if any of:

1. Operator visual HITL rates used PDP impact **<7/10**
2. W5-C markers leak to homepage, catalog, or new PDP
3. W5-A header regression on verification URLs
4. Modal forms broken (fields, submit, checkbox, legal links)
5. PHP/Twig/JS visible errors on target PDP

---

## T1 procedure

| Step | Action |
|------|--------|
| 1 | FTP STOR restore from `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\pre-w5c-commercial-stage-20260610-0002\` |
| 2 | Files: `product.twig`, `main.css`, `media.css` |
| 3 | Admin: clear system + modification + image cache; refresh modifications |
| 4 | Verify 8-URL matrix — same as W5-C execution |
| 5 | Confirm W5-C CSS block absent from live `/css/main.css` |
| 6 | Confirm `w5c-commercial-stage` absent from used PDP HTML |

**header.twig:** backed up but **not modified** by W5-C — restore only if accidentally changed.

---

## Rollback files map

| Remote path | Backup local name |
|-------------|-------------------|
| `catalog/view/theme/auto/template/product/product.twig` | `catalog__view__theme__auto__template__product__product.twig` |
| `css/main.css` | `css__main.css` |
| `css/media.css` | `css__media.css` |

---

## Post-rollback state

Reverts to W5-A-S + W4 Used PDP baseline (pre-W5-C). W5-A header shell remains active.

---

## Evidence

Manifest: `BACKUP-MANIFEST.md` in backup folder  
Report: [SITE-001-W5-STABLE-BACKUP-v1.md](SITE-001-W5-STABLE-BACKUP-v1.md)

---

*SITE-001 W5-C Used PDP Rollback Plan v1 — TEST only.*
