# FP-0002 V8 — Universalization Roadmap v1

**Date:** 2026-06-28  
**Prerequisite:** CF-003 COMPLETE  
**Status:** PLAN ONLY — no implementation in this pass

---

## Completed

| Wave | Family | Result |
|------|--------|--------|
| 1 | CF-003 internal-page-nav | COMPLETE — commit `361502bf` |
| 2 | CF-004 founder-quote | COMPLETE — pending commit |

---

## Recommended sequence

| Wave | Family | Priority | Pages | Risk | Operator gate |
|------|--------|----------|------:|------|---------------|
| 3 | CF-011 dark CTA band wrappers | P1 | 3 | Medium CSS (page-scoped duplicates) | Charter wave 3 |
| 4 | CF-012 program block modifiers | P1 | 3 | Medium CSS | Collapse redundant modifiers |
| 5 | CF-005 specialists | P1 | 3 | Low | Rename only — **next wave** |
| 6 | CF-006 comfort gallery | P1 | 5 | Low–medium | Retire unused services-comfort-v2 |
| 7 | CF-008 FAQ | P1 | 5 | Low JS (accordion) | Verify accordion init |
| 8 | CF-009 final form | P1 | 5 | Low | Form mask hooks |
| 9 | CF-007 reviews | P1 | 3 | Medium JS (Swiper) | Slider config audit |
| 10 | CF-010 clinic landscape | P2 | 3 | Low | Remove leaf modifier class |
| — | CF-013 inner hero | P2 | HOLD | Already shared on 3 templates | No wave unless Home unification requested |
| — | CF-015 home gallery | HOLD | 1 | Unknown until O-Centre | Defer |

---

## Completed wave: CF-004 Founder Quote

**Result:** COMPLETE

- Partial: `src/partials/sections/founder-quote.html`
- Root class: `.founder-quote`
- Retired: `home-founder-quote` (partial, classes, label id)
- Consumers: 5 pages
- Visual parity: PASS (before/after crop comparison)

---

## Next wave: CF-005 Specialists

**Reason**

1. Shared on Home + two internal service templates
2. Page-specific `home-` prefix is architecturally wrong
3. Lower risk than CF-011/CF-012 CSS collapse waves

**Operator gate**

Explicit approval to start Wave 3 (CF-005) before any rename.

---

## CF-004 archive (plan reference)

<details>
<summary>Original CF-004 plan (superseded)</summary>

- Rename partial: `home-founder-quote.html` → `founder-quote.html` — **DONE**
- Rename root class: `.home-founder-quote` → `.founder-quote` — **DONE**
- Update includes on all five consumer pages — **DONE**
- Retire `home-founder-quote` entirely — **DONE**
- Browser QA desktop + mobile — **DONE**

</details>

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
