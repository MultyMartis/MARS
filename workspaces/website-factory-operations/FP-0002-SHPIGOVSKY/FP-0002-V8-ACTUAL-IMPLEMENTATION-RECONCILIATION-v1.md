# FP-0002 V8 — Actual Implementation Reconciliation v1

**Date:** 2026-07-01  
**Method:** V8 source inspection vs existing documentation  
**Baseline:** `eb47ebb4066252373e02d9e1095403d0ce6b6b22`

---

## Summary

| Metric | Value |
|--------|-------|
| Implemented pages (source) | **10** |
| Baseline record page count | **10** — MATCH |
| Blog article completion | OPERATOR_APPROVED — MATCH |
| Product source modified in 07B | **NO** |

---

## Page reconciliation

| Page | Source evidence | Doc evidence | Status | Action |
|------|-----------------|--------------|--------|--------|
| Home | `src/pages/index.html` | Baseline §Included | MATCH | Documented in page register |
| O-Centre | `src/pages/o-centre.html` | Baseline STABLE | MATCH | Reconcile stale REJECTED audit claims |
| Contacts | `src/pages/kontakty.html` | Baseline | MATCH | — |
| Reviews | `src/pages/otzyvy.html` | Baseline | MATCH | — |
| Blog archive | `src/pages/blog.html` | Baseline | MATCH | — |
| Blog Article | `src/pages/blog/nazvanie-stati.html` | Baseline Pass 06 | MATCH | Blog architecture doc |
| Services hub | `src/pages/uslugi.html` | Baseline | MATCH | Note v2 canonical |
| Services v2 | `src/pages/uslugi-v2.html` | Baseline | MATCH | — |
| Service subdivision | `src/pages/usluga-podrazdel-v1.html` | Baseline | MATCH | — |
| Service leaf | `src/pages/usluga-konechnaya-v1.html` | Baseline | MATCH | — |
| Legal hub | Not in `src/pages/` | Page inventory PG-010 | DOCUMENTATION_STALE | 07C disposition; not a defect |
| 404 | Not in `src/pages/` | Page inventory PG-011 | DOCUMENTATION_STALE | 07C disposition |

---

## Blog Article feature reconciliation

| Feature | Source count | Baseline claim | Status |
|---------|--------------|----------------|--------|
| TOC items | 5 | 5 | MATCH |
| H2 in body | 5 | 5 | MATCH |
| H3 in body | 12 | 12 | MATCH |
| Inline images | 4 | 4 | MATCH |
| Sources | 8 | 8 | MATCH |
| Related cards | 3 | 3 | MATCH |
| Mobile hero order | CSS reorder | Documented | MATCH |
| Excerpt separate | Yes | Yes | MATCH |
| Founder quote variant B | Yes | Yes | MATCH |

---

## Architecture reconciliation

| Claim | Source | Status | Action |
|-------|--------|--------|--------|
| Single `style.scss` | One file ~7k+ lines | MATCH | Frontend rules doc |
| `--radius-main` only | `:root` in style.scss | MATCH | Documented |
| `.block-whith-red-line` | Present | MATCH | Spelling exception doc |
| One DOM responsive | No mobile duplicate partials | MATCH | Lessons learned |
| V8 active workspace | `fp-0002-shpigovsky-v8/` | MATCH | Update stale V7 ACTIVE rows |
| V6 current | False | DOCUMENTATION_STALE | PROJECT-STATUS historical rows |

---

## Component reconciliation

| Item | Status | Action |
|------|--------|--------|
| 66 partials under `src/partials/` | Verified | Component register |
| 13 components | Verified | Component register |
| Shared header/footer | All 10 pages | MATCH |
| Modal on pages | grep confirms | MATCH |

---

## Build reconciliation

| Item | Evidence | Status |
|------|----------|--------|
| `npm run build` | gulp clean + pipeline | MATCH |
| 10 HTML outputs | Baseline build evidence | MATCH |
| Font Awesome bridge | gulpfile paths | MATCH |

---

## Implementation exceptions (documented, not defects)

| Exception | Status |
|-----------|--------|
| `uslugi.html` + `uslugi-v2.html` coexist | IMPLEMENTATION_EXCEPTION — documented |
| Service leaf Lorem program | IMPLEMENTATION_EXCEPTION — placeholder |
| O-Centre audit REJECTED vs baseline STABLE | DOCUMENTATION_STALE — baseline wins |

---

## Deferred (not missing implementation)

| Item | Status |
|------|--------|
| Excel full site in static pages | DEFERRED — 07C |
| WordPress | DEFERRED |
| Operator polish | DEFERRED |
| Pagination / search | DEFERRED |

---

## Required documentation actions (07B)

- [x] Implementation guide  
- [x] Page/route register  
- [x] Component register  
- [x] Asset register  
- [x] Blog architecture  
- [x] WordPress handoff map  
- [x] Drift reconciliation for V6/V7/O-Centre stale rows  

---

*Reconciliation complete — documentation updated to match `eb47ebb` source.*
