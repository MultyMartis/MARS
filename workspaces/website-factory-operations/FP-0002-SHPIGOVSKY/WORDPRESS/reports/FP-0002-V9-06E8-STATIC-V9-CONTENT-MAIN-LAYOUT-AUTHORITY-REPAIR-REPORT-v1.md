# REPORT — FP-0002 V9-06E8 STATIC V9 CONTENT + MAIN LAYOUT AUTHORITY REPAIR

**Date:** 2026-07-06 | **HEAD baseline:** `599adf76` (E7B) | **Verdict:** PARTIAL PASS

## Summary

Enforced static V9 as template authority for `/uslugi/`, `/kontakty/`, and alcohol service leaf layout. Added `inc/v9-static-content.php` with one-to-one V9 copy; repaired services hub content/CTA wrapper, contacts V9 layout (maps + photo), and alcohol leaf full section stack. **0 DB writes** (template fallbacks). **18 theme files** delivered to runtime. Automated route probe: all primary + regression routes HTTP 200.

## Key repairs

| Area | Fix |
|------|-----|
| `/uslugi/` | V9 group/child copy from `uslugi-v2.html`; `program-cta-band` container wrap; V9 program text |
| `/kontakty/` | Full V9 location cards + map PNG assets; rehabilitation interior photo |
| Alcohol leaf | Full `usluga-konechnaya-v1` stack: bordered-info, approach, landscape, corridor, specialists, founder, comfort, reviews |
| Hub CTAs | `Записаться на консультацию` / `узнать больше` from V9 (not site-option drift) |

## Evidence

`validation/v9-06e8-static-v9-content-main-layout-authority-repair/`

DB checkpoint: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e8-static-v9-content-main-layout-authority-repair-pre-20260706-230100\`

## Git

Commit authorized by task §22 — selective E8 files only.
