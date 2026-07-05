# REPORT — FP-0002 V9-06D9-A VISUAL PARITY AUDIT

**Date:** 2026-07-05  
**Task:** V9-06D9-A Visual Parity Audit  
**Verdict:** FAIL  
**Operator authorization:** YES

---

## 1. Safety preflight

- Volume: X
- Label: AI WS
- Repository: `X:\AI MARS`
- Branch: mars/canonical-post-recovery
- Local HEAD: `ed009cbb808e01afa8c9d194c426621b5e7b0c94`
- Local short HEAD: `ed009cbb`
- Remote HEAD: `ed009cbb808e01afa8c9d194c426621b5e7b0c94`
- Remote short HEAD: `ed009cbb`
- Ahead: 0
- Behind: 0
- Foreign WIP: Present unstaged/untracked (D8 helpers, Corvonero, recovery temps) — not staged
- Pre-existing staged files: none
- Strict HEAD gate: **PASS_WITH_HEAD_NOTE** — required D8-G HEAD `4a22b701` is ancestor; actual HEAD +1 commit (`C2c: harden Corvonero…`); local/remote synced 0/0
- Result: PASS_WITH_HEAD_NOTE

## 2. Authorization and scope

- Operator authorization: YES
- Task mode: READ-ONLY VISUAL PARITY AUDIT
- Runtime delivery: NOT_PERFORMED
- Source changes: 0 (docs/evidence only)
- Runtime file writes: 0
- DB writes: 0
- ACF writes: 0
- Native content writes: 0
- Options writes: 0
- Menu changes: 0
- Redirects: 0
- Object changes: 0
- Rewrite/permalink changes: NO
- Theme/source changes: 0
- Plugin source changes: 0
- ACF JSON changes: 0
- V9 src/dist changes: 0
- Media uploads: 0
- Documentation/evidence writes: YES (D9-A scope only)
- Result: PASS

## 3. Static/runtime audit setup

- Static V9 root: `X:\AI MARS\workspaces\fp-0002-shpigovsky-v9\dist\`
- Static URL: `http://127.0.0.1:9876/`
- Runtime URL: `http://shpigovsky.test/`
- Browser: Google Chrome headless (puppeteer-core)
- Viewports: desktop 1440×900, mobile 390×844, deviceScaleFactor 1
- Screenshots captured: 18/18 required
- Result: PASS

## 4. Home section transfer audit

| Section | Static source/selector | Runtime match | Status | Severity | Likely root cause | Recommended repair |
|---|---|---|---|---|---|---|
| Hero | `.intro-section > section.hero` | partial (no image) | TRANSFERRED_BUT_VISUALLY_DEGRADED | CRITICAL | ACF image not seeded | D9-C |
| home-recovery-intro | `section.home-recovery-intro` | no | MISSING_FROM_WP_TEMPLATE | HIGH | D7-B wave scope | D9-D |
| founder-quote | `section.founder-quote` | no | MISSING_FROM_WP_TEMPLATE | HIGH | Not ported | D9-D |
| home-treatment-prevention | `section.home-treatment-prevention` | yes | TRANSFERRED_AND_VISIBLE | MEDIUM | Media gaps | D9-E |
| home-gallery | `section.home-gallery` | no | TRANSFERRED_BUT_EMPTY | HIGH | ACF not seeded D8-B | D9-D |
| home-why-us | `section.home-why-us` | no | MISSING_FROM_WP_TEMPLATE | HIGH | Not ported | D9-D |
| home-staff-photo | `section.home-staff-photo` | no | MISSING_FROM_WP_TEMPLATE | MEDIUM | Not ported | D9-D |
| home-feature-grid | `section.home-feature-grid` | yes | TRANSFERRED_AND_VISIBLE | LOW | OK | — |
| clinic-landscape | `section.clinic-landscape` | no | MISSING_FROM_WP_TEMPLATE | MEDIUM | Not ported | D9-D |
| home-recovery-life | `section.home-recovery-life` | no | MISSING_FROM_WP_TEMPLATE | HIGH | Not ported | D9-D |
| reviews | `section.reviews` | no | MISSING_FROM_WP_TEMPLATE | HIGH | Not ported | D9-D |
| home-rehabilitation-requirements | `section.home-rehabilitation-requirements` | no | MISSING_FROM_WP_TEMPLATE | MEDIUM | Not ported | D9-D |
| home-rehabilitation-program | `section.home-rehabilitation-program` | yes | TRANSFERRED_AND_VISIBLE | MEDIUM | Image gaps | D9-E |
| home-genotyping | `section.home-genotyping` | no | MISSING_FROM_WP_TEMPLATE | MEDIUM | Not ported | D9-D |
| comfort | `section.comfort` | no | MISSING_FROM_WP_TEMPLATE | MEDIUM | Not ported | D9-D |
| home-videos | `section.home-videos` | no | MISSING_FROM_WP_TEMPLATE | MEDIUM | Not ported | D9-D |
| specialists | `section.specialists` | no | MISSING_FROM_WP_TEMPLATE | HIGH | Not ported | D9-D |
| home-articles | `section.home-articles` | no | TRANSFERRED_BUT_EMPTY | MEDIUM | No posts | D9-D |
| faq | `section.faq` | yes | TRANSFERRED_AND_VISIBLE | LOW | OK | — |
| final-form | `section.final-form` | yes | TRANSFERRED_AND_VISIBLE | LOW | OK | — |

**Counts:** Static 20 sections → Runtime 6 sections.

## 5. Home hero parity audit

- Static hero image: `/assets/img/hero/hero-main.png` — present, 620px height
- Runtime hero image: **absent** — no `hero__media` in DOM
- Static overlay: photo + `.hero__panel` central title
- Runtime overlay: panel only on empty/light background
- Static hero height: 620px
- Runtime hero height: 620px (same CSS box)
- Static CTA: Записаться на консультацию
- Runtime CTA: Заказать звонок (D8-A options)
- Static title/pill: Шпиговский дом + tagline pill
- Runtime title/pill: same text, no photo context
- Asset load status: static 200; runtime hero PNG 404; not requested in HTML
- ACF/image dependency: `home_hero_slides[0].image` — empty; D8-B normalize failed
- Likely root cause: **ACF_IMAGE_NOT_SEEDED** + **ASSET_NOT_DELIVERED**
- Severity: **CRITICAL**
- Recommended repair: **D9-C**

## 6. Header/nav computed typography diff

| Item | Property | Static | Runtime | Match | Likely visual impact |
|---|---|---|---|---:|---|
| header root | font-family | Inter, system-ui… | Inter, system-ui… | yes | Low if fonts load |
| header root | font-weight | 300 | 300 | yes | — |
| header root | font-size | 18px | 18px | yes | — |
| header root | color | rgb(71,83,113) | rgb(71,83,113) | yes | — |
| nav Отзывы | font-size | 16px | 16px | yes | — |
| nav Отзывы | font-weight | 400 | 400 | yes | — |
| nav Отзывы | line-height | 20px | 20px | yes | — |
| nav Отзывы | letter-spacing | normal | normal | yes | — |
| nav Отзывы | color | rgb(71,83,113) | rgb(71,83,113) | yes | — |
| nav Отзывы | -webkit-font-smoothing | antialiased | antialiased | yes | — |
| Inter 300 woff2 | loaded URL/status | 200 | **404** `/assets/fonts/…` | no | **HIGH** synthesis |
| Inter 400 latin woff2 | status | 200 | **404** | no | **HIGH** |
| Inter 500 woff2 | status | 200 | **404** | no | **HIGH** |
| Inter 400 cyrillic | theme path | n/a | 200 (unused by CSS) | — | CSS path bug |
| parent opacity/transform | all header | 1 / none | 1 / none | yes | — |
| device scale factor | — | 1 | 1 | yes | — |

Nav structure: static mega-menu vs WP flat menu — **structural mismatch** (not typography tokens).

## 7. Global typography / asset / font audit

| Asset/token | Static | Runtime | Match | Issue |
|---|---|---|---:|---|
| Primary CSS | style.css + vendor | v9-style.css only | no | Missing Swiper/Fancybox |
| Inter font requests | 11/11 OK | 5/10 fail | no | Root `/assets/` 404 |
| Body font-size | 18px | 18px | yes | — |
| Body font-weight | 300 | 300 | yes | — |
| Body color | rgb(71,83,113) | rgb(71,83,113) | yes | — |
| Hero PNG | 200 | not in DOM | no | Not seeded |
| Home screenshot size | ~1.48 MB | ~46 KB | no | Density collapse |

## 8. Visual difference register

| Area | Static state | Runtime state | Severity | Root cause | Repair type |
|---|---|---|---|---|---|
| Hero | Photo + overlay | Empty panel | CRITICAL | ACF/media | HERO_ASSET_REPAIR |
| Sections | 20 | 6 | CRITICAL | Template scope | TEMPLATE_HTML_PORT |
| Fonts | All load | 5×404 | HIGH | CSS paths | FONT_ASSET_REPAIR |
| Nav | Mega-menu | Flat WP menu | HIGH | Menu seed | CONTENT_REVIEW |
| Gallery | 4 slides | Hidden | HIGH | ACF empty | ACF_SEED_REQUIRED |
| Density | Rich imagery | Sparse text | CRITICAL | Combined | D9-D/E |

## 9. WordPress template transfer trace

| V9 section/partial | WP template/partial | Code exists | Data exists | Rendered | Root cause | Repair |
|---|---|---:|---:|---:|---|---|
| hero | home/hero.php | yes | no | degraded | ACF image | D9-C |
| home-recovery-intro | — | no | no | no | Not ported | D9-D |
| home-gallery | home/gallery.php | yes | no | no | ACF empty | D9-D |
| home-feature-grid | home/feature-grid.php | yes | yes | yes | OK | — |
| faq | home/faq.php | yes | yes | yes | OK | — |
| @font-face | v9-style.css | yes | n/a | broken | Path 404 | D9-B |

## 10. Repair plan

| Task | Objective | Files suspected | Mutation type | DB write | Runtime delivery | Risk | Acceptance |
|---|---|---|---|---:|---:|---|---|
| D9-C | Photo hero | hero.php, ACF, media | ACF+MEDIA | yes | yes | LOW-MED | hero__media visible |
| D9-B | Font parity | v9-style.css | CSS paths | no | yes | MED | woff2 all 200 |
| D9-D | Missing sections | front-page.php, partials | TEMPLATE+ACF | yes | yes | HIGH | ≥18 sections |
| D9-E | Density/vendor | assets.php | enqueue/CSS | partial | yes | MED | screenshot density |
| D9-F | Secondary pages | hub/service | audit+repair | TBD | yes | MED | hub parity |

## 11. Documentation changes

| File | Action | Reason |
|---|---|---|
| reports/FP-0002-V9-06D9A-VISUAL-PARITY-AUDIT-REPORT-v1.md | CREATE | Main audit report |
| architecture/FP-0002-V9-06D9A-*.md (8 files) | CREATE | Architecture audit pack |
| validation/v9-06d9a-visual-parity-audit/*.json | CREATE | Machine evidence |
| validation/v9-06d9a-visual-parity-audit/screenshots/*.png | CREATE | Visual evidence |
| WORDPRESS/README.md | UPDATE | D9-A status |
| WORDPRESS/SOURCE-AUTHORITY.md | UPDATE | D9-A provenance |
| PROJECT-STATUS.md | UPDATE | Phase status |

## 12. Git checkpoint

- Exact staged files: (see commit)
- Staged list inspected after staging: YES
- Broad staging detected: NO
- Runtime files staged: NO
- Runtime snapshots staged: NO
- DB dumps staged: NO
- Theme source staged: NO
- Plugin source staged: NO
- ACF JSON staged: NO
- V9 src/dist staged: NO
- Helper/temp files staged: NO
- Secrets staged: NO
- Screenshot files staged: YES (18 PNG)
- Commit: (pending)
- Commit hash: (pending)
- Push: (pending)
- Local HEAD: ed009cbb
- Remote HEAD: ed009cbb
- Result: (pending)

## 13. Final verdict

**FAIL**

V9-06D9-A Visual Parity Audit:
**COMPLETE**

Runtime delivery:
NOT_PERFORMED

Source changes:
docs/evidence only

Runtime file writes:
0

DB writes:
0

ACF writes:
0

Theme/source changes:
0

Plugin source changes:
0

ACF JSON changes:
0

V9 src/dist changes:
0

Static/runtime screenshots:
**COMPLETE**

Home section transfer:
**FAIL**

Home hero parity:
**FAIL**

Header/nav typography parity:
**PARTIAL**

Global font/asset parity:
**FAIL**

Repair required:
**YES**

Recommended next phase:
**CREATE_V9_06D9C_HOME_HERO_PARITY_REPAIR_TASK**

## 14. Recommended next action

**CREATE_V9_06D9C_HOME_HERO_PARITY_REPAIR_TASK**

---

## Evidence index

- `validation/v9-06d9a-visual-parity-audit/static-runtime-audit-setup.json`
- `validation/v9-06d9a-visual-parity-audit/screenshot-manifest.json`
- `validation/v9-06d9a-visual-parity-audit/home-section-transfer-audit.json`
- `validation/v9-06d9a-visual-parity-audit/home-hero-parity-audit.json`
- `validation/v9-06d9a-visual-parity-audit/header-nav-computed-style-diff.json`
- `validation/v9-06d9a-visual-parity-audit/global-typography-asset-font-audit.json`
- `validation/v9-06d9a-visual-parity-audit/visual-difference-register.json`
- `validation/v9-06d9a-visual-parity-audit/wp-template-transfer-trace.json`
- `validation/v9-06d9a-visual-parity-audit/visual-parity-repair-plan.json`
- `validation/v9-06d9a-visual-parity-audit/final-verdict.json`
