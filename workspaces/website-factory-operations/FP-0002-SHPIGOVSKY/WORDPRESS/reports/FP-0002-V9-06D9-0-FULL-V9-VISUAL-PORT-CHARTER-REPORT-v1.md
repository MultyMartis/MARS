# REPORT — FP-0002 V9-06D9-0 FULL V9 VISUAL PORT CHARTER

**Date:** 2026-07-05  
**Task:** V9-06D9-0 Full V9 Visual Port Charter & Repair Wave Plan  
**Verdict:** PASS  
**Operator authorization:** YES

---

## 1. Safety preflight

- Volume: X
- Label: AI WS
- Repository: `X:\AI MARS`
- Branch: mars/canonical-post-recovery
- Local HEAD: `bc2b9c3c97e3024d6954699ecb78b9e585e8e69a`
- Local short HEAD: `bc2b9c3c`
- Remote HEAD: `bc2b9c3c97e3024d6954699ecb78b9e585e8e69a`
- Remote short HEAD: `bc2b9c3c`
- Ahead: 0
- Behind: 0
- Foreign WIP: Present unstaged/untracked (recovery temps, D8/D9 helpers, Corvonero, v7/v8 WIP) — not staged
- Pre-existing staged files: none
- Strict HEAD gate: **PASS** — local HEAD = remote HEAD = `bc2b9c3c`
- Result: **PASS**

## 2. Authorization and interpretation

- Operator authorization: YES
- Task mode: READ-ONLY FULL VISUAL PORT PLANNING
- Current WP state interpreted as: **Deliberately lightweight MVP skeleton/content seed phase** — now upgrading to full V9 visual parity
- Full visual port now authorized: YES
- Runtime delivery: NOT_PERFORMED
- Source changes: docs/evidence only
- Runtime file writes: 0
- DB writes: 0
- ACF writes: 0
- Media uploads: 0
- Result: **PASS**

## 3. Static V9 full inventory summary

| Area | Static items | WP present | WP missing/degraded | Main class |
|------|---:|---:|---:|---|
| Global header/shell | 14 | 10 | 4 | HEADER_STRUCTURE_NOT_PORTED / ACF_NOT_SEEDED |
| Home sections | 20 | 6 | 14 | MISSING_TEMPLATE_PORT / ACF_NOT_SEEDED |
| Services Hub | 9 | 4 | 5 | INTENTIONAL_LIGHTWEIGHT_DEFERRED |
| Service leaf | 15+ | 10 | 5 | MISSING_TEMPLATE_PORT |
| Contacts | 3 | 2 | 1 | OPERATOR_DATA_REQUIRED |
| Fonts/vendor | 4 groups | 1 | 3 | FONT_PATH_NOT_REWRITTEN / VENDOR_ASSET_NOT_ENQUEUED |

## 4. Lightweight vs broken classification

| Mismatch | Class | Error or deferred | Required action |
|----------|-------|-------------------|-----------------|
| 12 home sections not ported | INTENTIONAL_LIGHTWEIGHT_DEFERRED | deferred | D9-D |
| Inter font 404 | BROKEN_ASSET_PATH | broken | D9-B CSS rewrite |
| Messenger icons absent | HEADER_STRUCTURE_NOT_PORTED | deferred | D9-B `#` fallback |
| Hero image missing | ACF_NOT_SEEDED | deferred | D9-C |
| Swiper/Fancybox missing | VENDOR_ASSET_NOT_ENQUEUED | broken | D9-B/F |
| WP menu ≠ V9 nav | WP_MENU_DATA_MISSING | deferred | D9-B menu |
| Gallery/articles hidden | INTENTIONAL_LIGHTWEIGHT_DEFERRED | deferred | D9-E |
| Contacts map/messengers | OPERATOR_DATA_REQUIRED | deferred | Operator URLs or `#` fallback |

## 5. Header full parity plan

| Header item | Static state | WP state | Required repair | Operator data needed |
|-------------|--------------|----------|-----------------|:---:|
| Desktop messengers (TG, WA) | 2 icons, href=# | absent | Source fallback or seed | 0 |
| Mobile messengers (TG, WA, Max) | 3 icons, href=# | absent | Source fallback or seed | 0 |
| Offcanvas messengers | 3 icons | absent | Same partial fix | 0 |
| Callback button | present | present | — | 0 |
| Phones (×2) | present | present (D8-A) | — | 0 |
| Search | present | present | — | 0 |
| Primary nav | V9 hardcoded links | flat WP menu | Menu seed/fallback | 0 |
| Inter fonts | 11/11 OK | 5/10 404 | Path rewrite | 0 |

**Messenger finding:** Static V9 uses placeholder `href="#"` icons. WP `messenger-links.php` exists but returns early when `social_links` empty (D8-A skip). Visual parity achievable without operator URLs.

## 6. Home full section transfer plan

| Section | WP state | Required repair | ACF needed | Media needed | Wave |
|---------|----------|-----------------|:-:|:-:|:-:|
| hero | degraded | media + seed | yes | yes | D9-C |
| home-recovery-intro | missing | new partial | yes | no | D9-D |
| founder-quote | missing | new partial | yes | yes | D9-D |
| home-treatment-prevention | partial | media | partial | yes | D9-E |
| home-gallery | empty | seed + Swiper | yes | yes | D9-D/E |
| home-why-us | missing | new partial | yes | yes | D9-D |
| home-staff-photo | missing | new partial | yes | yes | D9-D |
| home-feature-grid | present | — | no | no | — |
| clinic-landscape | missing | new partial | yes | yes | D9-D |
| home-recovery-life | missing | new partial | yes | yes | D9-D |
| reviews | missing | new partial | yes | yes | D9-D/E |
| home-rehabilitation-requirements | missing | new partial | yes | no | D9-D |
| home-rehabilitation-program | partial | media seed | yes | yes | D9-E |
| home-genotyping | missing | new partial | yes | yes | D9-D |
| comfort | missing | new partial | yes | yes | D9-D |
| home-videos | missing | new partial | yes | yes | D9-D |
| specialists | missing | new partial | yes | yes | D9-D/E |
| home-articles | empty | posts/fallback | partial | yes | D9-E |
| faq | present | — | no | no | — |
| final-form | present | — | no | no | — |

## 7. Asset/font/vendor parity plan

| Asset group | Issue | Required repair | Wave |
|-------------|-------|-----------------|------|
| Inter fonts | `/assets/fonts/` 404 | Theme-relative `@font-face` rewrite | D9-B |
| Swiper | not enqueued | Copy + enqueue CSS/JS | D9-B/F |
| Fancybox | not enqueued | Copy + enqueue CSS/JS | D9-B/F |
| Inputmask | not enqueued | CDN enqueue on forms | D9-F |
| Hero PNG | not in DOM | Theme/media delivery | D9-C |
| Home content images | gaps | Media library seed | D9-E |
| Social SVGs | in theme | already present | D9-B |

## 8. ACF/content/media requirement map

| Item | Source repair | ACF schema | DB seed | Media | Operator data | Review |
|------|:---:|:---:|:---:|:---:|:---:|:---:|
| Hero image | yes | no | yes | yes | no | no |
| Gallery | no | no | yes | yes | no | no |
| Reviews | yes | yes | yes | yes | no | yes |
| Specialists | yes | yes | yes | yes | no | yes |
| Articles | no | no | yes | yes | no | yes |
| Header messengers (visual) | yes | no | no | no | no | no |
| Header messengers (links) | no | no | yes | no | yes | no |
| Map URL | no | no | yes | no | yes | no |
| Legal IDs | no | no | yes | no | yes | yes |
| Service 74 copy | no | no | no | no | no | yes |
| FAQ copy | no | no | no | no | no | yes |

## 9. Full-port implementation wave plan

| Wave | Objective | Mutation type | Runtime delivery | DB checkpoint | Risk | Acceptance |
|------|-----------|---------------|:---:|:---:|:---:|------------|
| D9-B | Header/fonts/assets/messengers | source + runtime | yes | no | MED | Fonts 200; messengers visible |
| D9-C | Hero media/overlay | source + seed + media | yes | yes | LOW-MED | hero__media visible |
| D9-D | Home section port | source + ACF JSON | yes | no | HIGH | ≥18 sections |
| D9-E | Home content/media seed | DB + media | no | yes | MED | Sliders populated |
| D9-F | Vendor/density pass | source + runtime | yes | no | MED | Swiper/Fancybox work |
| D9-G | Secondary pages | source + partial seed | yes | yes | MED | Hub/service/contacts |
| D9-H | Full parity QA | docs | no | no | LOW | D9-A repeat PASS |
| D8-F | Admin UX (optional) | source | yes | no | LOW | After visual parity |

## 10. Next implementation recommendation

**CREATE_V9_06D9B_HEADER_FONT_ASSET_MESSENGER_REPAIR_TASK**

Inter font 404 affects every page and explains nav typography degradation. Messenger icons are missing because D8-A skipped empty `social_links`, while static V9 shows icons with `href="#"` — restorable via D9-B source fallback without inventing URLs. Vendor asset foundation belongs before gallery/reviews waves. Hero (D9-C) is wave 2 immediately after global shell repair. Operator explicitly flagged header messengers and font/menu mismatch.

## 11. Documentation changes

| File | Action | Reason |
|------|--------|--------|
| reports/FP-0002-V9-06D9-0-FULL-V9-VISUAL-PORT-CHARTER-REPORT-v1.md | CREATE | Main charter report |
| architecture/FP-0002-V9-06D9-0-*.md (9 files) | CREATE | Architecture pack |
| validation/v9-06d9-0-full-visual-port-charter/*.json (10 files) | CREATE | Machine evidence |
| WORDPRESS/README.md | UPDATE | D9-0 status |
| WORDPRESS/SOURCE-AUTHORITY.md | UPDATE | D9-0 provenance |
| FP-0002-SHPIGOVSKY/PROJECT-STATUS.md | UPDATE | Phase status |

## 12. Git checkpoint

- Exact staged files: (see commit)
- Staged list inspected: YES
- Runtime files staged: NO
- Source/theme/plugin files staged: NO
- ACF JSON staged: NO
- V9 src/dist staged: NO
- DB dumps staged: NO
- Helper/temp files staged: NO
- Secrets staged: NO
- Commit: (pending)
- Commit hash: (pending)
- Push: (pending)
- Local HEAD: bc2b9c3c
- Remote HEAD: bc2b9c3c
- Result: (pending)

## 13. Final verdict

**PASS**

V9-06D9-0 Full Visual Port Charter:
**COMPLETE**

Repair performed:
NO

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

Media uploads:
0

Full visual port required:
YES

Header/messenger repair required:
YES

Font/asset repair required:
YES

Home full section transfer required:
YES

Recommended next phase:
**CREATE_V9_06D9B_HEADER_FONT_ASSET_MESSENGER_REPAIR_TASK**

## 14. Final safety statement

Target folder:
X:\AI MARS

Volume:
AI WS / X:

Runtime:
X:\MARS-Localhost\sites\wordpress\projects\shpigovsky

V9-06D9-0 Full Visual Port Charter performed:
YES

Repair performed:
NO

Runtime delivery performed:
NO

Source changes:
docs-evidence-only

Runtime file writes:
0

Database writes:
0

ACF writes:
0

Native content writes:
0

Options writes:
0

Rewrite flush performed:
NO

Permalink/rewrite changed:
NO

Menus changed:
0

Redirects created:
0

Object create/delete:
0

Media uploads:
0

External API/API keys added:
NO

Production migration performed:
NO

V9 source changed:
NO

V9 dist changed:
NO

Theme source changed:
NO

Plugin source changed:
NO

ACF JSON changed:
NO

Plugin updates run:
0

Plugin installs run:
0

Plugin deletes run:
0

Helper committed:
NO

Secrets committed:
0

---

## Evidence index

- `validation/v9-06d9-0-full-visual-port-charter/static-v9-full-visual-inventory.json`
- `validation/v9-06d9-0-full-visual-port-charter/wp-current-visual-inventory.json`
- `validation/v9-06d9-0-full-visual-port-charter/lightweight-vs-broken-classification.json`
- `validation/v9-06d9-0-full-visual-port-charter/header-full-parity-plan.json`
- `validation/v9-06d9-0-full-visual-port-charter/home-full-section-transfer-plan.json`
- `validation/v9-06d9-0-full-visual-port-charter/asset-font-vendor-parity-plan.json`
- `validation/v9-06d9-0-full-visual-port-charter/acf-content-media-requirement-map.json`
- `validation/v9-06d9-0-full-visual-port-charter/full-port-implementation-wave-plan.json`
- `validation/v9-06d9-0-full-visual-port-charter/next-implementation-recommendation.json`
- `validation/v9-06d9-0-full-visual-port-charter/final-verdict.json`

## Authority consumed

- D9-A audit pack (`FP-0002-V9-06D9A-*`)
- D8-A…G seed/QA reports
- D7-B home template source report
- Static V9 `src/partials/layout/header.html`, `src/pages/index.html`
- WP theme `header.php`, `messenger-links.php`, `front-page.php`, `inc/assets.php`
