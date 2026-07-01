# FP-0002 V8 — Known Limitations and Deferred Work v1

**Date:** 2026-07-01  
**Baseline:** Operator-approved stable frontend — limitations below are **not** baseline defects unless marked BLOCKER.

---

## Acceptable for static client demo (07C)

| Limitation | Notes |
|------------|-------|
| Placeholder article slug `nazvanie-stati` | Demo-safe |
| Related cards link to same fixture | Demo-safe |
| Blog archive placeholder excerpts | Demo-safe with label in manifest |
| Non-functional forms | Visual-only acceptable |
| `robots: noindex, nofollow` on most pages | Demo posture |
| Not all Excel pages built | 07C assembly addresses |
| Services mobile TECHNICAL_SMOKE_PASS | Acceptable if layout usable |
| Internal link TODOs in article copy | Document in manifest |

---

## Demo limitations (document for client)

| Item | Status |
|------|--------|
| Forms do not submit | BY DESIGN until backend |
| No CMS admin | Static HTML package |
| No search | DEFERRED |
| No pagination | DEFERRED |
| Single blog article fixture | Template demonstration |
| Lorem ipsum in service leaf program block | PLACEHOLDER content |

---

## Placeholder content / URLs

| Item | Location |
|------|----------|
| Article slug | `/blog/nazvanie-stati/` |
| Related article hrefs | All → same slug |
| Canonical URLs | `shpigovsky.ru` — may not match static filenames |
| TEMPORARY_SEO_COPY | Home meta description |

---

## Missing CMS behavior

| Feature | Phase |
|---------|-------|
| Dynamic blog listing | WordPress |
| Related posts query | WordPress |
| TOC auto-generation | WordPress |
| Review/blog pagination | WordPress |
| Menu from CMS | WordPress |
| Media library | WordPress |

---

## Missing pages (vs design / Excel)

| Page | Status |
|------|--------|
| Legal hub | NOT_IMPLEMENTED — 07C disposition |
| 404 | NOT_IMPLEMENTED — 07C disposition |
| Additional service leaves | NOT_IMPLEMENTED — template reuse in 07C |
| Genotyping leaf | NOT_IMPLEMENTED |
| Review detail | DEFERRED |
| Specialists archive | DEFERRED (home section only) |

---

## Polish deferred (explicitly expected)

| Area | Owner |
|------|-------|
| Spacing / typography fine-tuning | Operator manual polish |
| Copy corrections | Operator |
| Image / caption refinement | Operator |
| Animation / micro-interactions | Later MARS pass |
| Accessibility polish | Later |
| Performance optimization | Later |
| Final SEO / content review | Later |

---

## WordPress / production

| Item | Status |
|------|--------|
| Forge WordPress theme integration | NOT STARTED |
| Form backend | NOT STARTED |
| Production deployment | NOT STARTED |
| ACF field schema finalization | DEFERRED to WP phase |

---

## Historical documentation conflicts

| Stale claim | Current truth |
|-------------|---------------|
| O-Centre REJECTED in audit docs | Baseline lists STABLE_PREVIOUSLY_APPROVED |
| V7 as active workspace | V8 is active |
| Blog article unfinished | OPERATOR_APPROVED Pass 06 |

Reconciled in [documentation-drift-reconciliation.md](documentation-drift-reconciliation.md).

---

## Not defects in stable baseline

- Operator polish not yet performed  
- Excel page count > implemented page count  
- Static demo package not yet assembled (07C)  
- WordPress not integrated  

---

*Limitations register — Phase 07B.*
