# SITE-001 W2 Change Request v1 — W3-C Footer Reduction

**Status:** **READY FOR EXECUTION** — operator task authorization  
**Type:** Formal change request — Phase 2 first write wave  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`

---

## Request

| Field | Value |
|-------|-------|
| **ID** | CR-SITE-001-W3C-2026-06-09 |
| **Site ID** | SITE-001 |
| **Phase** | W3-C — Footer Reduction |
| **Charter** | [SITE-001-W2-WRITE-CHARTER-v1.md](SITE-001-W2-WRITE-CHARTER-v1.md) |
| **Visual spec** | [SITE-001-W2-VISUAL-SPECIFICATION-v1.md](SITE-001-W2-VISUAL-SPECIFICATION-v1.md) §9 |
| **Rollback plan** | [SITE-001-W3C-ROLLBACK-PLAN-v1.md](SITE-001-W3C-ROLLBACK-PLAN-v1.md) |
| **Checkpoint** | `site-001-phase1-stable-2026-06` |

---

## Objective

Reduce footer visual weight by **40–60%** on TEST without redesign: compress spacing, collapse long legal blocks behind expander, densify catalog link columns, preserve branding/contacts/legal/SEO links.

---

## Business reason

Footer currently dominates viewport on many pages (~11 KB rendered HTML, repeated 50px vertical gaps). Phase 2 goal VG-04 requires compliance preserved with lower scroll depth.

---

## Affected components

| Component | Change summary |
|-----------|----------------|
| `footer.twig` | Restructure legal blocks into `<details>` expander; entity + policy links remain visible; remove inline style on loan-terms link |
| `css/main.css` | Reduce footer padding, menu title size, link margins, column count 6→4; add legal collapse styles |
| `css/media.css` | Tighter mobile footer spacing; catalog columns 3→2 on small screens |

**Not affected:** header, catalog templates, PDP, DB, extensions, third-party scripts.

---

## Verification

| URL | Check |
|-----|-------|
| `/` | Footer height ↓; contacts present |
| `/about` | Legal links present |
| `/contact/` | Callback CTA works (modal trigger) |
| `/cars/` | Manufacturer links present |
| `/auto/` | Manufacturer links present |
| Used PDP | Footer global shell intact |
| New PDP | Footer global shell intact |

---

## Rollback

T1 — restore 3 files from `pre-w3c-20260609-0259` backup (see rollback plan).

---

## Approval

| Role | Status | Date |
|------|--------|------|
| Write approver (**Андрей**) | **AUTHORIZED** — operator task | 2026-06-09 |
| Backup executed | **YES** — pre-w3c-20260609-0259 | 2026-06-09 |
