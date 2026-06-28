# FP-0002 V8 — Universalization Roadmap v1

**Date:** 2026-06-28  
**Prerequisite:** CF-003 COMPLETE  
**Status:** PLAN ONLY — no implementation in this pass

---

## Completed

| Wave | Family | Result |
|------|--------|--------|
| 1 | CF-003 internal-page-nav | COMPLETE — commit `361502bf` |

---

## Recommended sequence

| Wave | Family | Priority | Pages | Risk | Operator gate |
|------|--------|----------|------:|------|---------------|
| 2 | CF-004 founder quote | P1 | 5 | Low HTML/CSS; no JS | Charter wave 2 |
| 3 | CF-011 dark CTA band wrappers | P1 | 3 | Medium CSS (page-scoped duplicates) | After CF-004 or parallel if scoped |
| 4 | CF-012 program block modifiers | P1 | 3 | Medium CSS | Collapse redundant modifiers |
| 5 | CF-005 specialists | P1 | 3 | Low | Rename only |
| 6 | CF-006 comfort gallery | P1 | 5 | Low–medium | Retire unused services-comfort-v2 |
| 7 | CF-008 FAQ | P1 | 5 | Low JS (accordion) | Verify accordion init |
| 8 | CF-009 final form | P1 | 5 | Low | Form mask hooks |
| 9 | CF-007 reviews | P1 | 3 | Medium JS (Swiper) | Slider config audit |
| 10 | CF-010 clinic landscape | P2 | 3 | Low | Remove leaf modifier class |
| — | CF-013 inner hero | P2 | HOLD | Already shared on 3 templates | No wave unless Home unification requested |
| — | CF-015 home gallery | HOLD | 1 | Unknown until O-Centre | Defer |

---

## Next wave: CF-004 Founder Quote

**Reason**

1. Already on all four canonical templates + legacy `uslugi.html`
2. Page-specific `home-` prefix is architecturally wrong
3. No Swiper/Fancybox dependency
4. Direct reuse for O-Centre editorial blocks

**Expected files (future wave — not started)**

- Rename partial: `home-founder-quote.html` → neutral name (TBD)
- Rename root class: `.home-founder-quote` → neutral family (TBD)
- Update includes on: `index.html`, `uslugi-v2.html`, `usluga-podrazdel-v1.html`, `usluga-konechnaya-v1.html`
- Consolidate SCSS block under neutral root
- Retire `home-founder-quote` class entirely
- Browser QA on all affected pages desktop + mobile

**Content parameters to preserve**

- `modalSource`
- `founderQuoteModifierClass` (only if `--variant-b` remains visually distinct)

**Operator gate**

Explicit approval to start Wave 2 before any rename.

---

## O-Centre position

O-Centre (`o-centre-v1.html`) is **DEFERRED**. Universalization waves 2–10 prepare shared neutral families that O-Centre should consume via includes — not re-copy.

Do not start O-Centre implementation until operator charters it separately.

---

## V7 / deployment

- V7: immutable — no changes
- Deploy ZIP: not created
- Deployment: not performed
- WordPress: not started
