# REPORT — FP-0002 V9-06E41-FIX01 HERO HEIGHT AND REHABILITATION PROGRAM INTRO

## 1. Safety preflight

| Check | Value |
|---|---|
| Volume | X: |
| Label | AI WS |
| Repository | X:\AI MARS |
| Branch | mars/canonical-post-recovery |
| HEAD | d6a7ac6904e230f8f5298430a7b46392a6d0fffe |
| Staged files before | (empty) |
| WIP count only | ~743–746 (foreign monorepo WIP; unrelated MetaBOT / other lanes) |
| Runtime/source canon detected | YES — patch runtime-current first; sync runtime → `WORDPRESS/` |
| Commit allowed | NO |
| Result | PASS (local bounded writes only; commit skipped; no git reconciliation) |

## 2. Backup

| Item | Value |
|---|---|
| Backup path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e41-fix01-hero-height-rehab-intro-before-20260714-024847\` |
| DB dump | `mars_wp_fp0002.sql` (2 399 259 bytes; `--no-tablespaces`; hash prefix `EC007F5B1BDEC974`) |
| Theme backup/hash | theme / 633 files; CSS hash prefix `390095ED96B4A295` (pre-change) |
| Plugin backup/hash | plugin / 22 files; FieldGroups prefix `40E5F69F223B1A29` (pre-change) |
| ACF JSON backup/hash | acf-json / 9 files; home JSON prefix `FB4E61942AA49D2C` (pre-change) |
| Home meta export before | `exports/home-meta-before.tsv` |
| Home ACF group export before | `exports/home-acf-group-before.json` + field inventory TSV |
| Hero slides/settings export before | `exports/home-hero-slides-before.tsv` + `home-hero-settings-before.tsv` (2 slides; titles «Шпиговский дом 1» / «Шпиговский дом 2») |
| Rehabilitation program export before | `exports/home-rehab-program-before.tsv` + `rehab-intro-defaults-before.json` |
| Home snapshot before | `snapshots/home-before.html` (HTTP 200, 168 024 bytes) |
| Result | PASS |

## 3. Hero audit

| Area | Finding |
|---|---|
| Hero render source | `template-parts/home/hero.php` (runtime + source) |
| Hero CSS source | `assets/css/v9-style.css` — `.hero--home` + E41 slider rules |
| Slider JS source | `assets/js/v9-shell.js` — `initHomeHeroSlider` (Swiper) |
| Current slide count | 2 |
| Second slide | «Шпиговский дом 2» |
| Collapse cause | E41 rule grouped `.hero--home-slider` with children under `height:100%`. Class sits on the **same** element as `.hero--home`, so `height:100%` overrode `height:70vh` → section collapsed to text/content height (~355px measured). Absolute `.hero__media` does not contribute to flow height. |
| Files to change | `v9-style.css` (remove section from `height:100%` group + force Swiper wrapper/slide fill + content padding); `v9-shell.js` (`autoHeight: false`) |

## 4. Rehabilitation program audit

| Area | Finding |
|---|---|
| Render source | `template-parts/home/rehabilitation-program.php` |
| Current editable fields | visibility toggle only (`home_rehab_program_visible`) |
| Missing fields | head / lead / intro_1 / intro_2 (were hardcoded in template) |
| Program parent page | `/o-centre/programma-lecheniya/` — page ID `#13` |
| Program edit URL | `…/wp-admin/post.php?post=13&action=edit` (built via `admin_url()`, no hardcoded host in source) |
| Existing notice | plain text: cards automatic from program pages; home show/hide only |
| Files to change | `FieldGroups.php`, `group_fp02_page_home.json`, `rehabilitation-program.php`, `admin-home-acf.css` |
| Evidence artifact | `REPORTS/evidence/v9-06e41-fix01-rehab-program-fields-audit.csv` |

## 5. Hero height implementation

| Requirement | Implementation | Result | Notes |
|---|---|---|---|
| Multi-slide height restored | Removed `.hero--home-slider` from `height:100%` selector group; kept 70vh on `.hero--home` | PASS | Desktop measured **620px** at 1440×900 (= responsive `max-height` at ≤1440) |
| Inner vertical padding | `.hero--home-slider .hero__content` padding-block `clamp(24px, 4vh, 48px)` | PASS | Scoped to multi-slide only |
| First slide preserved | Markup/settings unchanged | PASS | «Шпиговский дом 1» |
| Second slide visible | Swiper next → «Шпиговский дом 2» | PASS | Playwright click |
| Nav/settings preserved | autoplay/arrows/dots attrs + UI | PASS | 2 arrows, 2 dots |
| Mobile not broken | 390px viewport | PASS | height 465px; no fatal/collapse below content |

## 6. Rehabilitation program admin fields

| Field | Type | Seeded value preview | Render target | Result | Notes |
|---|---|---|---|---|---|
| `home_rehabilitation_program_head` | text | Программа центра включает 4&nbsp;направления | `.home-rehabilitation-program__heading` inside `__head` | PASS | i18n label «Программа — заголовок» |
| `home_rehabilitation_program_lead` | textarea | Не&nbsp;просто снимаем симптомы… | `.home-rehabilitation-program__lead` | PASS | |
| `home_rehabilitation_program_intro_1` | textarea | Каждый человек приходит… | first `.home-rehabilitation-program__intro` | PASS | |
| `home_rehabilitation_program_intro_2` | textarea | Программа реабилитации выстраивается… | second `.home-rehabilitation-program__intro` | PASS | |
| (directions) | automatic | n/a | `.home-rehabilitation-program__directions` | PASS | 4 cards; links HTTP 200 |

Render uses `shpigovsky_home_text_or_fallback()` + `wp_kses_post()`.

## 7. Admin notice implementation

| Requirement | Implementation | Result | Notes |
|---|---|---|---|
| Phrase bold | `<strong class="fp02-acf-notice-danger">…</strong>` | PASS | |
| Phrase red | `.fp02-acf-notice-danger { color:#c9251d; font-weight:700 }` in `admin-home-acf.css` | PASS | |
| Program page link | `<a href="%s">программы лечения</a>` inside strong | PASS | |
| Link target valid | `admin_url('post.php?post=13&action=edit')` when page resolved; else `home_url('/o-centre/programma-lecheniya/')` | PASS | edit URL HTTP 302 (login gate) |
| i18n-ready | `sprintf( __( '…%s…', 'shpigovsky-core' ), esc_url( $url ) )` + `esc_html => 0` | PASS | helper `home_rehab_program_source_notice_message()` |

## 8. Home frontend validation

| Check | Expected | Actual | Result |
|---|---|---|---|
| Home HTTP | 200 | 200 | PASS |
| Hero height | restored | 620px desktop (was ~355px) | PASS |
| Second slide visible | yes | yes (DOM + next click) | PASS |
| Hero settings work | yes | autoplay/arrows/dots attrs + UI | PASS |
| Rehab head/lead/intro from ACF | yes | meta seeded + template reads ACF | PASS |
| Direction cards automatic | yes | 4 links → program children, all 200 | PASS |
| Visual preserved | yes | section structure unchanged | PASS |

## 9. Home admin validation

| Check | Expected | Actual | Result |
|---|---|---|---|
| Home edit loads | yes | ACF group `#1338` local=php, 74 fields | PASS |
| New fields visible | yes | 4 fields rendered in ACF wrap probe | PASS |
| Values seeded | yes | head length 78; all four non-empty | PASS |
| Notice styled | yes | HTML + CSS class present in render | PASS |
| Notice link valid | yes | contains `post.php?post=13` | PASS |
| Save validation | no errors | fields are optional text/textarea + existing toggle | PASS |

## 10. Regression validation

| Route | HTTP | Result | Notes |
|---:|---:|---|---|
| `/` | 200 | PASS | no fatal |
| `/uslugi/` | 200 | PASS | no fatal |
| `/blog/` | 200 | PASS | no fatal |
| `/specyalisty/` | 200 | PASS | no fatal |
| `/o-centre/` | 200 | PASS | no fatal |
| `/kontakty/` | 200 | PASS | no fatal |

## 11. Source/runtime sync

| File | Source path | Runtime path | Hash match | Result |
|---|---|---|---|---|
| `v9-style.css` | `WORDPRESS/theme/shpigovsky/assets/css/v9-style.css` | `wp-content/themes/shpigovsky/assets/css/v9-style.css` | YES | PASS |
| `v9-shell.js` | `WORDPRESS/theme/shpigovsky/assets/js/v9-shell.js` | `…/assets/js/v9-shell.js` | YES | PASS |
| `admin-home-acf.css` | `WORDPRESS/theme/shpigovsky/assets/css/admin-home-acf.css` | `…/assets/css/admin-home-acf.css` | YES | PASS |
| `rehabilitation-program.php` | `WORDPRESS/theme/shpigovsky/template-parts/home/rehabilitation-program.php` | runtime twin | YES | PASS |
| `FieldGroups.php` | `WORDPRESS/plugins/shpigovsky-core/src/Fields/FieldGroups.php` | runtime twin | YES | PASS |
| `group_fp02_page_home.json` | `WORDPRESS/acf-json/group_fp02_page_home.json` | `wp-content/acf-json/…` | YES | PASS |

## 12. Git result

| Item | Value |
|---|---|
| Staged before | (empty) |
| Staged after | (empty) |
| Commit attempted | NO |
| Commit hash | NO |
| Commit skipped reason | Local E41 fix; persistence handled separately |
| Push attempted | NO |

**Git classification (read-only):** intended FIX01 paths under FP-0002 `WORDPRESS/` + REPORTS + status docs; runtime/DB outside git; large foreign monorepo WIP (~746 lines) untouched.

## 13. Risk register

| Risk | Severity | Status | Recommended handling |
|---|---|---|---|
| ACF message field `name` empty in some ACF loads | Low | Accepted | Same pattern as other Home message notices; identified by `key` |
| Orphan ACF field posts during failed upsert cycle | Medium | Mitigated | Duplicate parent=0 posts deleted when twin under `#1338` existed |
| Responsive max-height changes hero at ≤1440 | Info | By design | Pre-existing; 620px is correct single-slide parity at that viewport |
| Local domain appears in exported ACF JSON message URL | Low | Accepted | PHP rebuilds URL via `admin_url()` / `home_url()`; JSON is sync snapshot |

## 14. Final verdict

PASS

V9-06E41-FIX01 Hero height / Rehabilitation program intro:
COMPLETE

Hero height:
PASS

Rehabilitation program fields:
PASS

Admin notice:
PASS

Home frontend preserved:
PASS

Home admin validation:
PASS

Regression:
PASS

Source/runtime sync:
PASS

Operator CSS preserved:
PASS

Git commit:
SKIPPED

No foreign project work:
PASS

Recommended next phase:
OPERATOR_REVIEW_REQUIRED

## 15. Recommended next action

OPERATOR_REVIEW_REQUIRED

## 16. Final safety statement

Target folder:
X:\AI MARS

V9-06E41-FIX01 Hero height / Rehabilitation program intro performed:
YES

DB writes:
4 Home meta seeds + ACF group #1338 field sync/orphan cleanup

Source changes:
YES

Runtime delivery:
YES

WordPress changes:
YES

Media Library changes:
NO

Backup created:
YES

Git mutation:
NO

Git commit:
NO

Git push:
NO

Reset:
NO

Rebase:
NO

Stash:
NO

Cleanup:
NO

Foreign project work:
NO

Operator runtime CSS preserved:
YES

FP-0002 product contaminated:
NO

WPilot confused with OCPilot:
NO

Secrets committed:
0
