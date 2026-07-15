# REPORT — FP-0002 V9-06E34 SPECIALISTS CHILD PAGES AND AUTOMATIC SLIDER

## 1. Safety preflight

| Check | Value |
|---|---|
| Volume | `X:` |
| Label | `AI WS` |
| Repository | `X:\AI MARS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD | `c30d804866abb73ea3f6b30647c89d114e1c27b0` |
| Staged files before | empty |
| WIP count only | ~690 short-status lines (foreign monorepo WIP present) |
| Runtime CSS canon detected | YES — pre-task source/runtime hash MATCH for `v9-style.css`; additive E34 CSS applied on runtime then synced runtime→source |
| Commit allowed | NO — `STOP — REMOTE/HEAD MISMATCH` (`origin/mars/canonical-post-recovery`=`7fdd9d0c…`) + unpushed MetaBOT commits + foreign WIP |
| Result | PASS — preflight OK; writes allowed; commit blocked by policy |

## 2. Backup

| Item | Value |
|---|---|
| Backup path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e34-specialists-pages-slider-before-20260713-020509\` |
| DB dump | `mars_wp_fp0002.sql` (2 944 309 bytes, `--no-tablespaces`) |
| Theme backup/hash | `theme-shpigovsky/` — 629 files, content hash `df019e6d081421f3` |
| Plugin backup/hash | `plugin-shpigovsky-core/` — 21 files, content hash `51289cdf32180752` |
| ACF JSON hash/copy | `acf-json-source/` — 22 files, hash `c391c101bdf8ab18` (runtime theme has no `acf-json/` dir) |
| Specialists/page inventory before | `specialists-inventory-before.json` — parent #1030; children #1031–1033; ACF+static slider 5 rows (Sergey duplicated) |
| Slider source snapshot before | Home + `/specyalisty/` HTML snapshots; resolved cards from ACF repeater → static fixture |
| Result | PASS |

## 3. Pre-implementation audit

| Area | Finding |
|---|---|
| Specialists parent page | `#1030` «Специалисты» `/specyalisty/` template `page-templates/generic.php` publish |
| Existing child pages | `#1031` shipovsky «Сергей Шпиговский»; `#1032` kazakov «Казаков»; `#1033` kostyuk «Костюк» — all generic, no duplicates |
| Specialists slider source file | `template-parts/home/specialists.php` (+ `alcohol-direct-v9/specialists.php`, institutional/`subdivision-stack`) via `shpigovsky_get_specialists_cards()` |
| Specialists slider data source | Pre-E34: ACF `specialists_items` on `fp02-block-specialists` → fallback `shpigovsky_get_v9_specialists_cards()` (5 rows, Sergey×2) |
| Specialist image source | Theme assets `img/content/home-specialists/*.webp` |
| Obsolete manual/ACF data | ACF repeater was active source; retired from render + admin (message notice kept) |
| Files to change | `reusable-blocks-helpers.php`, home + alcohol specialists partials, `v9-style.css` (additive), `v9-static-content.php` (comment), `FieldGroups.php`, `group_fp02_block_specialists.json`, DB pages/meta/media |
| Source/runtime differences | Pre-task MATCH on target theme files; CSS patched runtime-first then synced |

## 4. Specialist data extracted from slider

| # | Name | Role/title | Description source | Image source | Existing page match | Action |
|---:|---|---|---|---|---|---|
| 1 | Сергей Юрьевич Шпиговский | Аддиктолог, интервенционист | slider role | `sergey-shpigovsky.webp` | `#1031` `/specyalisty/shipovsky/` | REUSE/UPDATE (dedupe 2nd static row) |
| 2 | Максим Михайлович Казаков | Психолог, преподаватель психологии, гештальт-терапевт | slider role | `maxim-kazakov.webp` | `#1032` `/specyalisty/kazakov/` | REUSE/UPDATE |
| 3 | Дарья Владимировна Костюк | Психолог, EMDR терапевт, телесно-ориентированный терапевт | slider role | `darya-kostyuk.webp` | `#1033` `/specyalisty/kostyuk/` | REUSE/UPDATE |
| 4 | Шапигузова Татьяна Андреевна | Сертифицированный гонг-мастер, звукотерапевт и преподаватель Кундалини йоги. | slider role | `tatyana-shapiguzova.webp` | none | CREATE |
| — | Сергей Юрьевич Шпиговский (2nd slider row) | same | static/ACF duplicate | same | `#1031` | SKIP (no duplicate page) |

## 5. Specialist pages created/updated

| Specialist | Action | Page ID | Parent ID | Slug | URL | Template | Image/featured | Menu order | Result |
|---|---|---:|---:|---|---|---|---|---:|---|
| Сергей Юрьевич Шпиговский | UPDATED | 1031 | 1030 | shipovsky | `/specyalisty/shipovsky/` | `page-templates/generic.php` | thumb **1092** | 10 | OK |
| Максим Михайлович Казаков | UPDATED | 1032 | 1030 | kazakov | `/specyalisty/kazakov/` | `page-templates/generic.php` | thumb **1094** | 20 | OK |
| Дарья Владимировна Костюк | UPDATED | 1033 | 1030 | kostyuk | `/specyalisty/kostyuk/` | `page-templates/generic.php` | thumb **1096** | 30 | OK |
| Шапигузова Татьяна Андреевна | CREATED | 1097 | 1030 | shapiguzova | `/specyalisty/shapiguzova/` | `page-templates/generic.php` | thumb **1098** | 40 | OK |

Also: ACF `specialists_all_link_url` updated from `/o-centre/` → `/specyalisty/`.

## 6. Slider automation

| Requirement | Implementation | Result | Notes |
|---|---|---|---|
| Query child pages of `/specyalisty/` | `shpigovsky_get_specialists_cards()` → `post_parent` #1030, publish, `menu_order` ASC, title ASC | PASS | |
| No manual static source | ACF repeater removed from render; static fixture kept only as seed/legacy comment | PASS | |
| Links to child pages | `.specialists__card-link` → child permalink | PASS | Home, `/o-centre/`, alcohol leaf |
| No duplicates | Unique by specialist identity; Sergey no longer duplicated | PASS | 4 cards |
| Visual classes preserved | `specialists__*` + Swiper markup unchanged aside from link wrapper | PASS | |
| Slider JS preserved | `initSpecialists` / `[data-specialists-slider]` untouched | PASS | |
| Image fallback | featured → `_shpigovsky_specialist_photo_asset` → `images/service-placeholder.svg` | PASS | featured set for all 4 |

## 7. Route validation

| Route | HTTP | Object ID | Template | Result | Notes |
|---|---:|---:|---|---|---|
| `/` | 200 | front page | front-page | PASS | slider 4 cards / 4 links |
| `/specyalisty/` | 200 | 1030 | generic.php | PASS | parent index (no slider on page itself) |
| `/specyalisty/shipovsky/` | 200 | 1031 | generic.php | PASS | |
| `/specyalisty/kazakov/` | 200 | 1032 | generic.php | PASS | |
| `/specyalisty/kostyuk/` | 200 | 1033 | generic.php | PASS | |
| `/specyalisty/shapiguzova/` | 200 | 1097 | generic.php | PASS | new |
| `/uslugi/` | 200 | hub | services-hub | PASS | |
| `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | 200 | 74 | service leaf | PASS | specialists slider 4/4 |
| `/o-centre/` | 200 | 11 | institutional | PASS | specialists slider 4/4 |
| `/o-centre/programma-lecheniya/` | 200 | 13 | generic.php | PASS | |
| `/blog/` | 200 | — | blog | PASS | |
| `/kontakty/` | 200 | — | contacts | PASS | |

## 8. Slider validation

| Page | Slider items | Expected source | Links 200 | Duplicates | JS OK | Result |
|---|---:|---|---|---|---|---|
| `/` | 4 | children of #1030 | 4/4 PASS | none | `data-specialists-slider` present; init unchanged | PASS |
| `/o-centre/` | 4 | same query | 4 links | none | same partial | PASS |
| Alcohol leaf service | 4 | same query | 4 links | none | alcohol-direct specialists partial | PASS |
| `/specyalisty/` | 0 | N/A (generic parent) | — | — | no slider expected | PASS |

## 9. Admin/page hierarchy validation

| Check | Expected | Actual | Result |
|---|---|---|---|
| Parent page | `/specyalisty/` | #1030 | PASS |
| Child count | equals unique slider specialists (4) | 4 | PASS |
| Templates | generic/pustyshka | all `page-templates/generic.php` | PASS |
| Order | matches slider order | 10/20/30/40 | PASS |
| No duplicates | yes | no title/slug duplicates | PASS |

## 10. Regression validation

| Route | HTTP | Result | Notes |
|---|---:|---|---|
| `/` | 200 | PASS | no fatal |
| `/specyalisty/` | 200 | PASS | |
| `/specyalisty/*` (4 children) | 200 | PASS | |
| `/uslugi/` | 200 | PASS | |
| `/o-centre/` | 200 | PASS | |
| `/o-centre/programma-lecheniya/` | 200 | PASS | |
| `/blog/` | 200 | PASS | |
| `/kontakty/` | 200 | PASS | |

## 11. Source/runtime sync

| File | Source path | Runtime path | Hash match | Result |
|---|---|---|---|---|
| `inc/reusable-blocks-helpers.php` | `WORDPRESS/theme/shpigovsky/...` | `wp-content/themes/shpigovsky/...` | yes | PASS |
| `inc/v9-static-content.php` | same | same | yes | PASS |
| `template-parts/home/specialists.php` | same | same | yes | PASS |
| `template-parts/service/alcohol-direct-v9/specialists.php` | same | same | yes | PASS |
| `assets/css/v9-style.css` | same | same | yes | PASS |
| `plugins/.../FieldGroups.php` | `WORDPRESS/plugins/shpigovsky-core/...` | runtime plugin | yes | PASS |
| `acf-json/group_fp02_block_specialists.json` | source authority only | N/A (no runtime theme acf-json) | source updated | PASS |

## 12. Git result

| Item | Value |
|---|---|
| Staged before | empty |
| Staged after | empty |
| Commit attempted | NO |
| Commit hash | — |
| Commit skipped reason | `STOP — REMOTE/HEAD MISMATCH` + unpushed MetaBOT commits + ~695 foreign/prior WIP lines; task forbids unsafe commit |
| Push attempted | NO |

## 13. Risk register

| Risk | Severity | Status | Recommended handling |
|---|---|---|---|
| Legacy ACF `specialists_items` option rows still in DB but unused | low | accepted | leave; render/admin retired; optional cleanup later |
| Media Library gained 4 specialist photo attachments | low | accepted | intentional featured-image seed from theme assets |
| Git persistence blocked | medium | open | operator review then bounded commit wave when remote/HEAD reconciled |
| `/specyalisty/` parent has no listing UI of children | low | accepted | out of scope; slider + child pages fulfill charter |
| Validator regex initially double-counted `specialists__card` vs `specialists__card-link` | info | mitigated | live HTML confirmed 4 cards |

## 14. Final verdict

PASS

V9-06E34 Specialists pages / automatic slider:
COMPLETE

Specialist child pages:
PASS

No duplicates:
PASS

Generic template:
PASS

Slider automation:
PASS

Slider links:
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

V9-06E34 Specialists pages / automatic slider performed:
YES

DB writes:
29

Source changes:
YES

Runtime delivery:
YES

WordPress changes:
YES

Media Library changes:
YES

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
