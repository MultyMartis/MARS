# SITE-001 WF-V2-W1 Hybrid Header Change Request v1

**Change request ID:** CR-SITE-001-WFV2-W1-2026-06-10  
**Date:** 2026-06-10  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Charter:** [SITE-001-WFV2-W1-HEADER-WRITE-CHARTER-v1.md](SITE-001-WFV2-W1-HEADER-WRITE-CHARTER-v1.md)  
**Rollback:** [SITE-001-WFV2-W1-HEADER-ROLLBACK-PLAN-v1.md](SITE-001-WFV2-W1-HEADER-ROLLBACK-PLAN-v1.md)

---

## Summary

Transition header from Visual Baseline V1 (W5-A graphite shell) to **WF V2 Hybrid Header**: light contact rail, dark primary band, light promo strip. Remove phone/WhatsApp duplication from primary band. Restore original logo. Subtractive CSS override block — no PHP/JS/DB.

---

## HITL decision

| Option | Status |
|--------|--------|
| Pure light header (spec `02`) | **REJECTED** |
| Current graphite W5-A header | **REJECTED** |
| **Hybrid** (light rail + dark band + light promo) | **APPROVED** |

---

## Files in scope

| Remote path | Change |
|-------------|--------|
| `catalog/view/theme/auto/template/common/header.twig` | Remove phone/WA from CTA cluster; add `wfv2-header` hooks; logo `img/logo.svg` |
| `css/main.css` | Append WF-V2-W1 block (~200 lines) |
| `css/media.css` | Append WF-V2-W1 responsive block |

---

## Functional preservation

- All menu links · «Услуги» dropdown · «Ещё» dropdown  
- Callback button + `#callback__FORM_popup` hook  
- Phone + WhatsApp links (contact rail + mobile offcanvas)  
- Mobile offcanvas logic  
- Static header (no sticky)

---

## Authorization

| Action | Status |
|--------|--------|
| TEST FTP write | **AUTHORIZED** (this CR) |
| Production | **NOT AUTHORIZED** |
| Commit / push | **NOT AUTHORIZED** |
