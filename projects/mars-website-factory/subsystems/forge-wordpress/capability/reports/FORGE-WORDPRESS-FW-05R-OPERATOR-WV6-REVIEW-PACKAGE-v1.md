# Forge WordPress FW-05R — Operator WV6 Review Package v1

**Document type:** Operator visual review package  
**Version:** v1  
**Date:** 2026-06-23  
**Case:** FWS-0001  
**Operator gate:** **PENDING** — no visual approval recorded in this task

---

## Purpose

Compact review package for operator **WV6** (visual parity / acceptance). Automated FW-V-05 and Playwright comparison reports exist separately; this package defines what the operator should inspect and how to record a decision.

**Important:** Task authorization («Ок, утверждаю») for FW-05R closure **does not** constitute WV6 visual acceptance.

---

## Live URLs

**Note:** Direct browser URLs require hosts elevation (see [FORGE-WORDPRESS-FW-05R-DIRECT-DOMAIN-CLOSURE-v1.md](FORGE-WORDPRESS-FW-05R-DIRECT-DOMAIN-CLOSURE-v1.md)). Until elevation, use Host header or MLI documented workaround.

| Page | URL |
|------|-----|
| Homepage | `http://fws-0001.test/` |
| Services archive | `http://fws-0001.test/services/` |
| Service single (canonical) | `http://fws-0001.test/services/testovaya-usluga/` |
| Contacts | `http://fws-0001.test/contacts/` |

**Hosts elevation (operator, elevated PowerShell):**

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "D:\MARS-Localhost\tools\hosts\add-mli-host.ps1"
ipconfig /flushdns
```

---

## Static baseline (reference build)

```text
workspaces/forge-wordpress-synthetic/FWS-0001/FRONTEND/dist/
```

Rebuild if needed (local only, not tracked in Git):

```powershell
cd "C:\AI MARS\workspaces\forge-wordpress-synthetic\FWS-0001\FRONTEND"
npm ci
npm run build
```

Open `dist/index.html`, `dist/services.html`, `dist/service-single.html`, `dist/contacts.html` for side-by-side comparison.

---

## Required visual checks

Inspect **live WordPress** against static baseline and design intent:

| # | Area | Focus |
|---|------|-------|
| 1 | Header | Logo, nav, responsive menu trigger |
| 2 | Hero | Title, subtitle, CTA, background |
| 3 | Typography | Headings, body, hierarchy |
| 4 | Section spacing | Vertical rhythm, container width |
| 5 | Cards | Service cards on home and archive |
| 6 | Archive layout | `/services/` grid and headings |
| 7 | Single service layout | `/services/testovaya-usluga/` |
| 8 | Contacts | Contact block, form stub |
| 9 | FAQ | Accordion block (if visible on reviewed pages) |
| 10 | Footer | Links, copyright, layout |

### Viewports

| Viewport | Width | Check |
|----------|-------|-------|
| Desktop | 1440 | Full layout, no overflow |
| Tablet | 1024 | Grid collapse, nav |
| Mobile | 390 | Responsive menu, no horizontal scroll |

### Quality gates

- No broken images or missing critical assets
- No obvious layout overflow
- Responsive menu functional
- Documented automated deviations from [FWS-0001-WORDPRESS-VISUAL-PARITY-v1.md](../../../../../workspaces/forge-wordpress-synthetic/FWS-0001/VALIDATION/reports/FWS-0001-WORDPRESS-VISUAL-PARITY-v1.md) reviewed

---

## Decision model

Record one outcome after review:

| Decision | Meaning |
|----------|---------|
| **PASS** | Visual parity acceptable for synthetic capability proof |
| **PASS WITH ACCEPTED DEVIATIONS** | Known deviations documented and accepted |
| **REQUIRES FIXES** | Blocking visual issues — return to Forge fix cycle |

**Current recorded status:**

```text
Operator WV6: PENDING
```

Do **not** update to PASS until operator provides explicit visual approval in a separate decision record or task input.

---

## Supporting evidence (read-only)

| Document | Path |
|----------|------|
| FW-05R master report | [FORGE-WORDPRESS-FW-05R-LIVE-SYNTHETIC-VALIDATION-REPORT-v1.md](FORGE-WORDPRESS-FW-05R-LIVE-SYNTHETIC-VALIDATION-REPORT-v1.md) |
| Visual parity (automated) | `workspaces/forge-wordpress-synthetic/FWS-0001/VALIDATION/reports/FWS-0001-WORDPRESS-VISUAL-PARITY-v1.md` |
| FW-V-05 live | `workspaces/forge-wordpress-synthetic/FWS-0001/VALIDATION/reports/FWS-0001-FW-V-05-VISUAL-PARITY-LIVE-v1.md` |
| Issue register | `workspaces/forge-wordpress-synthetic/FWS-0001/VALIDATION/reports/FWS-0001-ISSUE-AND-FIX-REGISTER-v1.md` |

---

## Limitations (not WV6 blockers for capability proof)

| Limitation | Status |
|------------|--------|
| ACF Pro workflow | **NOT PROVEN** — ACF Free profile only |
| Direct `fws-0001.test` hosts | **PENDING ELEVATION** |
| Populate script automation | Documented gap — manual population used |

---

*Operator WV6 review package v1 — human gate separate from FW-05R closure checkpoint.*
