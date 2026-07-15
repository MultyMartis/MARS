# REPORT — FP-0002 V9-06D9-C HOME HERO PARITY REPAIR

**Date:** 2026-07-05  
**Task:** V9-06D9-C Home Hero Parity Repair  
**Verdict:** PASS  
**Operator authorization:** YES

---

## 1. Safety preflight

- Volume: X
- Label: AI WS
- Repository: `X:\AI MARS`
- Branch: mars/canonical-post-recovery
- Local HEAD: `c9daf9670659f52e4a5eb0ec3e2f8e8a599919de`
- Local short HEAD: `c9daf967`
- Remote HEAD: `c9daf9670659f52e4a5eb0ec3e2f8e8a599919de`
- Remote short HEAD: `c9daf967`
- Ahead: 0
- Behind: 0
- Foreign WIP: Present unstaged/untracked (recovery temps, D8/D9 helpers, v7/v8 WIP) — not staged
- Pre-existing staged files: none
- Strict HEAD gate: **PASS**
- Result: **PASS**

## 2. Authorization and scope

- Operator authorization: YES
- Task mode: SOURCE/THEME REPAIR + BOUNDED RUNTIME DELIVERY
- Runtime delivery: PERFORMED
- Source/theme changes: YES (2 PHP + 1 PNG)
- Runtime file writes: 3
- DB writes: 0
- ACF writes: 0
- Home hero ACF writes: 0
- Other Home writes: 0
- Service/Hub/Contacts writes: 0
- Options writes: 0
- Menu writes: 0
- Rewrite/permalink changes: NO
- Plugin source changes: 0
- ACF JSON changes: 0
- V9 src/dist changes: 0
- Media uploads: 0
- Documentation/evidence writes: YES
- Result: **PASS**

## 3. Baseline hero audit

| Area | Static V9 | Runtime before | Issue | Severity |
|---|---|---|---|---|
| Hero image | `/assets/img/hero/hero-main.png` HTTP 200 | absent; not in DOM | ACF_IMAGE_NOT_SEEDED + ASSET_NOT_DELIVERED | CRITICAL |
| `hero__media` DOM | present | absent | template gated on empty ACF image | CRITICAL |
| Overlay/panel | photo + `.hero__panel` | panel on empty/light bg | no media layer | CRITICAL |
| CTA | Записаться на консультацию | Заказать звонок (D8-A option) | label delta out of D9-C scope | LOW |
| Desktop height | 620px | 620px | CSS box OK; content degraded | MED |
| Mobile hero | photo + panel | panel only | same root cause | HIGH |

## 4. Implementation plan

| Change | Source file | Runtime target | DB write needed | Reason | Risk |
|---|---|---|:---:|---|---|
| Hero PNG asset | `assets/img/hero/hero-main.png` | `.../assets/img/hero/hero-main.png` | NO | Deliver V9 hero media in theme | LOW |
| Fallback helper | `inc/home-helpers.php` | `.../inc/home-helpers.php` | NO | Theme asset when ACF empty | LOW |
| Hero template wiring | `template-parts/home/hero.php` | `.../template-parts/home/hero.php` | NO | Render `hero__media` | LOW |

## 5. Source/theme hero repair

| Item | Before | After | Source | Result |
|---|---|---|---|---|
| Theme hero PNG | absent | present (3.8 MB, SHA256 match V9) | `fp-0002-shpigovsky-v9/src/img/hero/` | PASS |
| `shpigovsky_get_home_hero_image_fallback()` | n/a | returns theme URI | `inc/home-helpers.php` | PASS |
| `hero__media` render | omitted when ACF empty | rendered via fallback | `template-parts/home/hero.php` | PASS |
| D4/D8 title/tagline | present | preserved | ACF/text defaults | PASS |

## 6. DB/ACF handling

**NO_DB_WRITE**

- DB checkpoint: not required
- Dry-run: not performed
- Field written: none
- Old state: `home_hero_slides[0].image` empty
- New state: unchanged (empty)
- Result: **PASS** — theme fallback sufficient

## 7. Runtime delivery

- Delivery mode: BOUNDED_COPY
- Runtime target(s): active `wp-content/themes/shpigovsky/` only (charter `app/public` path absent)
- Files copied: 3
- Deletes: 0
- Mirror/purge: NO
- Checksum/source-target verification: SHA256 match all 3 files
- Result: **PASS**

## 8. Post-repair validation

| Check | Result | Notes |
|---|---|---|
| Route smoke (7 routes) | ALL_200 | Home, Hub, 4 services, Contacts |
| `hero__media` present | PASS | runtime DOM |
| Hero image HTTP | 200 | `.../themes/shpigovsky/assets/img/hero/hero-main.png` |
| Panel/title/tagline/CTA | PASS | readable over photo |
| Desktop hero not empty | PASS | photo visible |
| Mobile hero | PASS | acceptable |
| No ACF leakage | PASS | |
| Other Home sections | unchanged | no D9-D transfer |

## 9. Screenshots

| Screenshot | Captured | Result |
|---|---:|---|
| before-static-home-hero-desktop.png | YES | PASS |
| before-static-home-hero-mobile.png | YES | PASS |
| before-runtime-home-hero-desktop.png | YES | PASS |
| before-runtime-home-hero-mobile.png | YES | PASS |
| static-home-hero-desktop-reference.png | YES | PASS |
| static-home-hero-mobile-reference.png | YES | PASS |
| runtime-home-hero-desktop-after-d9c.png | YES | PASS |
| runtime-home-hero-mobile-after-d9c.png | YES | PASS |
| runtime-home-desktop-after-d9c.png | YES | PASS |
| runtime-home-mobile-after-d9c.png | YES | PASS |
| runtime-services-hub-desktop-after-d9c.png | YES | PASS |
| runtime-service-74-desktop-after-d9c.png | YES | PASS |
| runtime-contacts-desktop-after-d9c.png | YES | PASS |

## 10. No-scope-drift

- DB writes: 0
- ACF writes: 0
- Home hero ACF writes: 0
- Other Home writes: 0
- Service/Hub/Contacts writes: 0
- Options writes: 0
- Menu writes: 0
- Rewrite flush: NO
- Object changes: 0
- Media uploads: 0
- Plugin changes: 0
- Runtime deletes: 0
- V9 src/dist changes: 0
- Secrets/API keys: 0
- Result: **PASS**

## 11. Documentation changes

| File | Action | Reason |
|---|---|---|
| `WORDPRESS/reports/FP-0002-V9-06D9C-HOME-HERO-PARITY-REPAIR-REPORT-v1.md` | created | Task report |
| `WORDPRESS/architecture/FP-0002-V9-06D9C-*.md` (6 files) | created | Architecture evidence |
| `WORDPRESS/validation/v9-06d9c-home-hero-parity-repair/*` | created | Validation JSON + screenshots |
| `WORDPRESS/README.md` | updated | Phase status |
| `WORDPRESS/SOURCE-AUTHORITY.md` | updated | D9-C authority note |
| `FP-0002-SHPIGOVSKY/PROJECT-STATUS.md` | updated | Project status |

## 12. Git checkpoint

- Exact staged files: D9-C theme source (3), docs, validation JSON, screenshots only
- Staged list inspected: YES
- Runtime files staged: NO
- Plugin source staged: NO
- ACF JSON staged: NO
- V9 src/dist staged: NO
- DB dumps staged: NO
- Helper/temp files staged: NO
- Secrets staged: NO
- Commit: `2c57654265abeff240d565d045a9d1b6a8790910`
- Commit hash: `2c576542`
- Push: YES
- Local HEAD: `2c57654265abeff240d565d045a9d1b6a8790910`
- Remote HEAD: synced after push
- Result: **PASS**

## 13. Final verdict

**PASS**

V9-06D9-C Home Hero Parity Repair: **COMPLETE**

Runtime delivery: **PERFORMED**

Source/theme changes: **3**

Runtime file writes: **3**

DB writes: **0**

ACF writes: **0**

Home hero ACF writes: **0**

Other Home writes: **0**

Service/Hub/Contacts writes: **0**

Options writes: **0**

Menu writes: **0**

Home hero media parity: **PASS**

Hero image HTTP: **200**

Hero visual parity: **PASS**

Route smoke: **ALL_200**

No-scope-drift: **PASS**

Recommended next phase: **CREATE_V9_06D9D_HOME_FULL_SECTION_TRANSFER_TASK**

## 14. Recommended next action

**CREATE_V9_06D9D_HOME_FULL_SECTION_TRANSFER_TASK**

## 15. Final safety statement

Target folder:  
X:\AI MARS

Volume:  
AI WS / X:

Runtime:  
X:\MARS-Localhost\sites\wordpress\projects\shpigovsky

V9-06D9-C Home Hero Parity Repair performed:  
YES

Runtime delivery performed:  
YES

Source/theme changes:  
3

Runtime file writes:  
3

Database writes:  
0

ACF writes:  
0

Home hero ACF writes:  
0

Other Home writes:  
0

Service writes:  
0

Services Hub writes:  
0

Contacts writes:  
0

Options writes:  
0

Menu writes:  
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
