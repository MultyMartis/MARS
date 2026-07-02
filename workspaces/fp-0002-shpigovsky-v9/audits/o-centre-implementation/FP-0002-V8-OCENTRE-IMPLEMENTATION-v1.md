# FP-0002 V8 O-Centre Implementation v1

**Date:** 2026-06-29
**Verdict:** `FP0002_V8_OCENTRE_IMPLEMENTED_PENDING_OPERATOR_REVIEW`

## 1. Canonical anchors

| Anchor | SHA |
|---|---|
| Repository | `C:/MARS Phenix/AI MARS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD at start | `f17287372927531cf70d6a2dd0b1b8c28ac79e1e` |
| Manual polish | `472be1ab` |
| O-Centre charter | `62d24fa7` |
| Asset gate | `b49f0af3` / verify `f39d9b9d` |
| Content gate | `2cfe1964` |

## 2. Implemented composition (12 sections)

Hero · Subnav · Institutional narrative · Who we treat · Approach · Program · Mid CTA · Founder quote · Infrastructure · Guest CTA · Specialists · Reviews · Final form

Excluded: Steps/BLK-018, FAQ accordion, home-gallery, home-staff-photo, Lorem on O-Centre.

## 3. Reuse map

| Family | Partial | Mode |
|---|---|---|
| Hero | `services-inner-hero-v2.html` | Content parameters |
| Subnav | `internal-page-nav.html` | Content parameters |
| Who we treat | `services-category-section-v2.html` | Modifier `--o-centre-who-we-treat` |
| Program | `services-program-v2.html` | Content parameters + empty lead |
| CTA ×2 | `program-cta-band.html` | Content parameters |
| Founder | `founder-quote.html` | Direct reuse |
| Specialists | `specialists.html` | Section id |
| Reviews | `reviews.html` | Section id |
| Final form | `final-form.html` | Content parameters |

## 4. Unique components

| Partial | Root class |
|---|---|
| `institutional-narrative.html` | `.institutional-narrative` |
| `infrastructure-narrative.html` | `.infrastructure-narrative` |

Approach region: inline `.program-approach-band` in page (function-based; reuses `home-feature-grid` card pattern).

## 5. Build / QA

| Gate | Result |
|---|---|
| Baseline build | PASS |
| Implementation build | PASS |
| DOM (6 pages) | PASS |
| Content QA | PASS |
| Infrastructure assets 20/20 | PASS (HTTP 200) |
| main.js changed | NO |

## 6. Shared change

`services-program-v2.html`: `@@if (lead !== '')` — backward compatible.

## 7. Operator review

Preview: `http://127.0.0.1:4208/o-centre.html` (task QA server)
Status: **IMPLEMENTED_PENDING_OPERATOR_REVIEW**
Deployment: not performed.

## 8. Known gaps

- Full-page visual screenshots deferred to operator review (manifest in `data/FP-0002-V8-OCENTRE-SCREENSHOT-MANIFEST.json`).
- Backup ZIP captured after implementation tree (includes new page); pre-change recoverable from git parent tree for unchanged files.
