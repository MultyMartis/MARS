# SITE-001 W3VIS Rollback Execution v1

**Type:** T1 rollback execution — W3VIS-01A + W3VIS-01B reversal  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Authorization:** Operator decision — **ROLLBACK APPROVED** (task drift — PDP hero hierarchy not requested)  
**Rollback tier:** **T1** — OCPilot incremental file restore  
**Prior execution:** [SITE-001-W3VIS-01A-EXECUTION-v1.md](SITE-001-W3VIS-01A-EXECUTION-v1.md) · [SITE-001-W3VIS-01B-EXECUTION-v1.md](SITE-001-W3VIS-01B-EXECUTION-v1.md)

**Production:** **NOT TOUCHED**  
**Beget global backup:** **NOT USED**

---

## Execution summary

| Step | Status | Notes |
|------|--------|-------|
| 1. Locate rollback package | **DONE** | `pre-w3vis-01a-20260609-0517` |
| 2. Verify backup integrity | **DONE** | Manifest + 2 CSS files; SHA-256 recorded |
| 3. Restore original files (FTP STOR) | **DONE** | 2/2 files — `css/main.css`, `css/media.css` |
| 4. Clear system cache | **DONE** | HTTP 200 |
| 5. Clear modification cache | **DONE** | HTTP 200 |
| 6. Clear image cache | **DONE** | HTTP 200 |
| 7. Refresh modification cache | **DONE** | HTTP 200 |
| 8. HTTP verification | **DONE** | **9/9** URLs **PASS** |
| 9. Live CSS marker check | **DONE** | W3VIS absent · W3UX-C1 present |
| 10. Execution report | **DONE** | This document |

**Evidence (local, not git):** `.recovery-temp/site-001-w3vis-rollback-result.json` · `.recovery-temp/site-001-w3vis-rollback-execute.py`

---

## Rollback source

| Field | Value |
|-------|--------|
| Backup ID | `pre-w3vis-01a-20260609-0517` |
| Location | `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\pre-w3vis-01a-20260609-0517\` |
| Manifest | `BACKUP-MANIFEST.md` — **present** |
| Tier | **T1** — incremental file restore (pre-W3VIS-01A baseline) |
| Effect | Removes **both** W3VIS-01A and W3VIS-01B CSS blocks (01B was appended after 01A) |

### Backup integrity

| File | Bytes (disk) | SHA-256 | W3VIS-01A | W3VIS-01B | W3UX-C1 | W3V2 |
|------|--------------|---------|-----------|-----------|---------|------|
| `css__main.css` | 126 268 | `b99118a26683dea7e2b2b8d47d7d741ff84651630fa308f3f86a8849ec2724ce` | absent | absent | present | present |
| `css__media.css` | 33 733 | `fe27d5de8658e2c5c8681087f437048da66879da7c529f9e7d62b06e5cd136d8` | absent | absent | present | present |

---

## Files restored

| # | Remote path | Restored bytes (UTF-8) | Scope |
|---|-------------|------------------------|-------|
| 1 | `css/main.css` | 118 851 | Pre-W3VIS-01A — W3-V · W3UX-C1 · W3V2 blocks retained |
| 2 | `css/media.css` | 31 485 | Pre-W3VIS-01A responsive blocks retained |

**Not touched:** Phase 1 · DB · Twig · PHP · JS · admin · SEO · routes · content

---

## CSS markers removed

| Marker | File(s) | Post-rollback |
|--------|---------|---------------|
| `SITE-001 W3VIS-01A PDP Hero Surface System` | `main.css`, `media.css` | **ABSENT** (live + restored) |
| `SITE-001 W3VIS-01B PDP Commercial Authority` | `main.css`, `media.css` | **ABSENT** (live + restored) |
| `/* END W3VIS-01A PDP Hero Surface System */` | `main.css` | **ABSENT** |
| `/* END W3VIS-01A responsive */` | `media.css` | **ABSENT** |
| `/* END W3VIS-01B PDP Commercial Authority */` | `main.css` | **ABSENT** |
| `/* END W3VIS-01B responsive */` | `media.css` | **ABSENT** |

---

## Cache actions

| Action | Result |
|--------|--------|
| System cache | **OK** — 200 |
| Modification cache | **OK** — 200 |
| Image cache | **OK** — 200 |
| Modification refresh | **OK** — 200 |

---

## Verification matrix

| # | Label | URL | HTTP | Layout markers | W3VIS absent | Pass |
|---|-------|-----|------|----------------|--------------|------|
| 1 | homepage | `/` | 200 | СИБКАР · main.css | **YES** | **PASS** |
| 2 | about | `/about` | 200 | СИБКАР · main.css | **YES** | **PASS** |
| 3 | contact | `/contact/` | 200 | СИБКАР · main.css | **YES** | **PASS** |
| 4 | used_catalog | `/cars/` | 200 | catalog_item · main.css | **YES** | **PASS** |
| 5 | used_brand | `/cars/bmw/` | 200 | search_wrap · main.css | **YES** | **PASS** |
| 6 | new_catalog | `/auto/` | 200 | catalog_item · main.css | **YES** | **PASS** |
| 7 | new_brand | `/auto/haval/` | 200 | search_wrap · main.css | **YES** | **PASS** |
| 8 | used_pdp | `/audi-a1-2012-s-probegom-149-000-km-799` | 200 | car_main_info · main.css | **YES** | **PASS** |
| 9 | new_pdp | `/baic-bj40-new` | 200 | new_car_main_info · main.css | **YES** | **PASS** |

### Live CSS probe (`/css/main.css`)

| Check | Result |
|-------|--------|
| Bytes | **118 851** (matches pre-W3VIS-01A baseline) |
| W3VIS-01A marker | **ABSENT** |
| W3VIS-01B marker | **ABSENT** |
| W3UX-C1 marker | **PRESENT** |
| W3V2 marker | **PRESENT** |
| W3-V marker | **PRESENT** |
| PHP / Twig errors on probed pages | **NONE** |

---

## W3UX-C1 preservation check

| Criterion | Result |
|-----------|--------|
| `W3UX-C1 Used Catalog Card Density` block in live `main.css` | **PASS** |
| `W3UX-C1` responsive block in live `media.css` | **PASS** (in restored backup) |
| `.used_catalog` scoped rules retained | **PASS** — backup verified pre-W3VIS |
| Used catalog `/cars/` HTTP 200 + `catalog_item` | **PASS** |
| Used brand `/cars/bmw/` HTTP 200 | **PASS** |

W3UX-C1 density wave **unchanged** — rollback baseline was captured immediately before W3VIS-01A write.

---

## Pre vs post rollback comparison

| Metric | Post-W3VIS-01B (pre-rollback) | After rollback | Match pre-W3VIS-01A |
|--------|------------------------------|----------------|---------------------|
| `main.css` live bytes | ~136 663 | **118 851** | **YES** |
| W3VIS-01A marker | present | **absent** | **YES** |
| W3VIS-01B marker | present | **absent** | **YES** |
| W3UX-C1 marker | present | **present** | **YES** |
| PDP hero hierarchy | W3VIS unified L2 surface | **pre-W3VIS layout/CSS** | **YES** |

---

## Operator decision context

| Field | Value |
|-------|--------|
| Decision | **ROLLBACK APPROVED** |
| Waves reverted | W3VIS-01A · W3VIS-01B |
| Reason | Task drift — operator requested **global palette / visual tone refresh** across whole site; implementation incorrectly changed PDP hero hierarchy |
| Method | OCPilot T1 incremental restore only |
| Next focus | **Global Palette Refresh** — site-wide tone; separate discovery/charter required |

---

## Notes

- Single T1 restore to `pre-w3vis-01a-20260609-0517` removes both W3VIS waves because 01B was layered on 01A.
- W3-V and W3V2 blocks remain active in restored CSS — not in rollback scope.
- Backup package retained at external storage for audit trail.
