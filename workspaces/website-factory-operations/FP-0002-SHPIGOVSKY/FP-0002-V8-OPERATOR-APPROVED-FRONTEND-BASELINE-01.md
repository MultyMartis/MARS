# FP-0002 V8 — Operator-Approved Frontend Baseline 01

**Document type:** Baseline closure record  
**Date:** 2026-07-01  
**Phase:** FP-0002 V8 Phase 07A  
**Branch:** `mars/canonical-post-recovery`  
**Parent stable baseline:** `eeab3d68e4e9333a55dcfbcb2732f22f6e5ab9a2` · tag `fp-0002-v8-blog-full-stable-01`  
**Intended tag:** `fp-0002-v8-operator-approved-frontend-stable-01`

---

## Baseline identity

Operator-approved freeze of the complete FP-0002 V8 static frontend before manual polish, Excel-driven client demo packaging, animation refinement, and Forge WordPress integration.

| Field | Value |
|-------|-------|
| Baseline name | FP-0002-V8-OPERATOR-APPROVED-FRONTEND-BASELINE-01 |
| Workspace | `workspaces/fp-0002-shpigovsky-v8/` |
| Visual authority | Operator-approved V8 working source |
| Build command | `npm run build` (Gulp clean build) |

---

## Included pages (10)

| Page | Source | Route | Desktop | Mobile |
|------|--------|-------|---------|--------|
| Home | `src/pages/index.html` | `/index.html` | OPERATOR_APPROVED | OPERATOR_APPROVED |
| O-Centre | `src/pages/o-centre.html` | `/o-centre.html` | STABLE_PREVIOUSLY_APPROVED | STABLE_PREVIOUSLY_APPROVED |
| Contacts | `src/pages/kontakty.html` | `/kontakty.html` | STABLE_PREVIOUSLY_APPROVED | STABLE_PREVIOUSLY_APPROVED |
| Reviews | `src/pages/otzyvy.html` | `/otzyvy.html` | STABLE_PREVIOUSLY_APPROVED | STABLE_PREVIOUSLY_APPROVED |
| Blog archive | `src/pages/blog.html` | `/blog.html` | STABLE_PREVIOUSLY_APPROVED | STABLE_PREVIOUSLY_APPROVED |
| Blog Article | `src/pages/blog/nazvanie-stati.html` | `/blog/nazvanie-stati.html` | OPERATOR_APPROVED | OPERATOR_APPROVED |
| Services hub | `src/pages/uslugi.html` | `/uslugi.html` | STABLE_PREVIOUSLY_APPROVED | TECHNICAL_SMOKE_PASS |
| Services v2 | `src/pages/uslugi-v2.html` | `/uslugi-v2.html` | STABLE_PREVIOUSLY_APPROVED | TECHNICAL_SMOKE_PASS |
| Service subdivision | `src/pages/usluga-podrazdel-v1.html` | `/usluga-podrazdel-v1.html` | STABLE_PREVIOUSLY_APPROVED | TECHNICAL_SMOKE_PASS |
| Service leaf | `src/pages/usluga-konechnaya-v1.html` | `/usluga-konechnaya-v1.html` | STABLE_PREVIOUSLY_APPROVED | TECHNICAL_SMOKE_PASS |

Prior per-page stable tags preserved: O-Centre `fp-0002-v8-o-centre-full-stable-01`, Contacts `fp-0002-v8-contacts-full-stable-01`, Reviews `fp-0002-v8-reviews-full-stable-01`, Blog archive `fp-0002-v8-blog-full-stable-01`.

---

## Blog Article approval (Pass 06)

- Unified hero: two-column desktop; mobile order image → H1 → meta → TOC → excerpt
- Semantic TOC: 5 anchors with red markers
- Separate excerpt block (WordPress-excerpt ready)
- Single `the_content()`-compatible body stream: 5 H2, 12 H3, 4 inline images
- Conclusion + founder quote (`founder-quote--variant-b`); `.blog-article-conclusion-label` absent
- 8 sources; 3 related cards (yoga, BOS, alcohol); compact CTA; shared footer
- One DOM for desktop and mobile

---

## Clean build

- **Result:** PASS (Gulp `cleanDist` + full pipeline, 2026-07-01)
- **Generated HTML pages:** 10
- **Evidence:** `X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\v8-operator-approved-baseline-closure-07a\build\`

---

## Known demo limitations

- Blog archive card excerpts contain temporary placeholder copy
- Related article links point to demo slug `/blog/nazvanie-stati/`
- Article body contains operator-noted future internal link placeholders
- Excel inventory reconciliation deferred to Phase 07C
- Services pages mobile polish may lag dedicated page passes

---

## Deferred work

| Phase | Scope |
|-------|-------|
| 07B | Full documentation and lessons learned |
| 07C | Excel-driven static client demo assembly |
| Later | Manual operator polish (spacing, copy) |
| Later | Animation and interaction refinement |
| Later | Forge WordPress integration |

---

## Recovery pack

`X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\FP-0002-V8-OPERATOR-APPROVED-FRONTEND-STABLE-01\`

---

## Related records

- [FP-0002-V8-WORDPRESS-READY-BASELINE-v1.md](FP-0002-V8-WORDPRESS-READY-BASELINE-v1.md)
- [FP-0002-PRIORITY-VISUAL-IMPLEMENTATION-PROTOCOL.md](FP-0002-PRIORITY-VISUAL-IMPLEMENTATION-PROTOCOL.md)
- V8 operational status: `workspaces/fp-0002-shpigovsky-v8/foundation/FP-0002-V8-OPERATIONAL-STATUS.md`
