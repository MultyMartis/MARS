# SITE-001 W3-C Rollback Execution v1

**Type:** T1 rollback execution — W3-C Footer Reduction reversal  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Authorization:** Operator decision — **ROLLBACK APPROVED** (visual direction not accepted)  
**Rollback plan:** [SITE-001-W3C-ROLLBACK-PLAN-v1.md](SITE-001-W3C-ROLLBACK-PLAN-v1.md) — **T1**  
**Prior execution:** [SITE-001-W3C-EXECUTION-v1.md](SITE-001-W3C-EXECUTION-v1.md)

**Production:** **NOT TOUCHED**  
**Beget global backup:** **NOT USED**

---

## Execution summary

| Step | Status | Notes |
|------|--------|-------|
| 1. Locate rollback package | **DONE** | `pre-w3c-20260609-0259` |
| 2. Verify backup integrity | **DONE** | Manifest + 3 files; SHA-256 recorded |
| 3. Restore original files (FTP STOR) | **DONE** | 3/3 files |
| 4. Clear system cache | **DONE** | HTTP 200 |
| 5. Clear modification cache | **DONE** | HTTP 200 |
| 6. Clear image cache | **DONE** | HTTP 200 |
| 7. Refresh modification cache | **DONE** | HTTP 200 |
| 8. HTTP verification | **DONE** | **7/7** URLs **PASS** |
| 9. Execution report | **DONE** | This document |

**Evidence (local, not git):** `.recovery-temp/site-001-w3c-rollback-result.json` · `.recovery-temp/site-001-w3c-rollback-execute.py`

---

## Rollback source

| Field | Value |
|-------|--------|
| Backup ID | `pre-w3c-20260609-0259` |
| Location | `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\pre-w3c-20260609-0259\` |
| Manifest | `BACKUP-MANIFEST.md` — **present** |
| Tier | **T1** — incremental file restore |

### Backup integrity

| File | Bytes (disk) | SHA-256 |
|------|--------------|---------|
| `catalog__view__theme__auto__template__common__footer.twig` | 20 487 | `ddc2a6c43cb38daf7e5923810cf7f887a049014c6f35f9d1264b9298ab914b59` |
| `css__main.css` | 111 200 | `24f52a1eac1ad622e1004d342c51941f5fa03185017f16a4ff9df7885b496e4a` |
| `css__media.css` | 32 521 | `591bc6f0ce6e36f6626d22689d48e11c63f1c5a33585245a8f15695682b07c02` |

---

## Files restored

| # | Remote path | Restored bytes | Scope |
|---|-------------|----------------|-------|
| 1 | `catalog/view/theme/auto/template/common/footer.twig` | 20 078 | Pre-W3C expanded legal blocks |
| 2 | `css/main.css` | 104 417 | Pre-W3C footer spacing (`50px` stack) |
| 3 | `css/media.css` | 30 330 | Pre-W3C mobile footer rules |

**Not touched:** DB · logos · SEO · YML · SMTP · other templates

---

## Cache actions

| Action | Result |
|--------|--------|
| System cache | **OK** — 200 |
| Modification cache | **OK** — 200 |
| Image cache | **OK** — 200 |
| Modification refresh | **OK** — 200 |

---

## Verification results

| URL | HTTP | Footer bytes | Links | W3-C removed | Pass |
|-----|------|--------------|-------|--------------|------|
| `/` | 200 | 11 080 | 89 | **YES** | **PASS** |
| `/about` | 200 | 11 080 | 89 | **YES** | **PASS** |
| `/contact/` | 200 | 11 080 | 89 | **YES** | **PASS** |
| `/cars/` | 200 | 11 080 | 89 | **YES** | **PASS** |
| `/auto/` | 200 | 11 080 | 89 | **YES** | **PASS** |
| `/cars/bmw/` (used category/PDP shell) | 200 | 11 080 | 89 | **YES** | **PASS** |
| `/auto/haval/` (new category/PDP shell) | 200 | 11 080 | 89 | **YES** | **PASS** |

### Checklist

| Check | Result |
|-------|--------|
| Footer restored to pre-W3C baseline | **PASS** — `wsp_footer__legal_details` absent; footer bytes match pre-change (11 080) |
| No broken layout | **PASS** — all URLs HTTP 200 |
| No missing links | **PASS** — 89 footer links on all probes |
| No missing contacts | **PASS** — phone, WhatsApp, address, callback CTA present |
| No missing legal content | **PASS** — policy links, entity block, copyright present |
| No PHP errors | **PASS** |
| No Twig errors | **PASS** |

---

## Pre vs post rollback comparison

| Metric | W3-C (post-change) | After rollback | Match pre-W3C |
|--------|-------------------|----------------|---------------|
| Footer HTML bytes | 11 228 | **11 080** | **YES** |
| `wsp_footer__legal_details` | present | **absent** | **YES** |
| Footer links | 89 | **89** | **YES** |
| `main.css` bytes (uploaded) | 105 636 | **104 417** | **YES** |

---

## Operator decision context

| Field | Value |
|-------|--------|
| Decision | **ROLLBACK APPROVED** |
| Reason | Visual direction not accepted |
| Method | OCPilot T1 incremental restore only |

---

## Notes

- Automated script verified 5 core URLs; category PDP shells `/cars/bmw/` and `/auto/haval/` verified in follow-up probe (same footer signature).
- Independent product PDP URLs remain sparse on TEST; category shells carry global footer — same approach as W3-C execution.
- Backup package retained at external storage for audit trail; no Beget panel restore invoked.
