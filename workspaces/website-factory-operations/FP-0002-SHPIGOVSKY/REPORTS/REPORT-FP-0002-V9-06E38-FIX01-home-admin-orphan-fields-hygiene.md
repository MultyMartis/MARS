# REPORT — FP-0002 V9-06E38-FIX01 HOME ADMIN ORPHAN FIELDS HYGIENE

## 1. Safety preflight

| Check | Value |
|---|---|
| Volume | X: |
| Label | AI WS |
| Repository | X:\AI MARS |
| Branch | mars/canonical-post-recovery |
| HEAD | ee0c46532a5fbf41a3cfc9d7f755a1341f529a55 |
| Staged files before | (empty) |
| WIP count only | ~713–714 (foreign monorepo WIP; MetaBOT commits ahead of origin) |
| Runtime/source canon detected | YES — `WORDPRESS/` source → runtime `shpigovsky` / `shpigovsky-core` / `acf-json` |
| Commit allowed | NO |
| Result | PASS (local bounded writes only; commit skipped) |

## 2. Backup

| Item | Value |
|---|---|
| Backup path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e38-fix01-home-admin-orphan-hygiene-before-20260713-193615` |
| DB dump | `mars_wp_fp0002.sql` (2 315 852 bytes; `--no-tablespaces`) |
| Theme backup/hash | theme / `cf85cd6ec2a80961` (631 files) |
| Plugin backup/hash | plugin / `1c5778d387123ede` (21 files) |
| ACF JSON backup/hash | acf-json / `ca2ec93b70ace11f` (9 files) |
| Home meta export before | `exports/home-meta-before.tsv` |
| Home ACF DB groups export before | `exports/home-acf-groups-before.tsv`, `exports/home-acf-fields-before.tsv`, `exports/all-acf-groups-before.tsv` |
| Home admin inventory before | `exports/home-admin-inventory-before.txt` |
| Home snapshot before | `snapshots/home-before.html` (HTTP 200) |
| E38 classification copy | `classification/v9-06e38-home-acf-field-classification.csv` |
| Result | PASS |

## 3. E38 classification review

| Artifact | Path | Rows | Result |
|---|---|---:|---|
| E38 classification input | `REPORTS/evidence/v9-06e38-home-acf-field-classification.csv` | 22 | PASS — used as starting point; confirmed vs DB + render |
| E38-FIX01 classification output | `REPORTS/evidence/v9-06e38-fix01-home-acf-field-classification-after.csv` | 31 | PASS |

## 4. Pre-implementation audit

| Area | Finding |
|---|---|
| Home page ID/template | Page `#4` (`glavnaya`); `show_on_front=page`; ACF location `page_type == front_page` |
| Canonical Home ACF group | PHP/JSON `group_fp02_page_home` (`FieldGroups::page_home`) — local registration + acf-json |
| Duplicate Home ACF DB groups | **4 publish** posts same key: `#114`, `#483`, `#581`, `#639` |
| Orphan live fields found | `home_faq_heading`, `home_recovery_intro_*`, `home_articles_heading` (primary Home SoT); `home_specialists_heading` / `home_comfort_*` / `home_reviews_heading` (fallback after options/blocks) |
| Confirmed dead fields found | `home_blog_teaser_enabled` — **zero** theme reads; confirmed unused |
| Automated block fields found | Gallery CPT notice (E38); specialists/articles/comfort/reviews need notices; services accordion already retired E32 |
| `home_blog_teaser_enabled` usage | Unused by theme; meta was `1`; retire from admin |
| Files to change | `FieldGroups.php`, `group_fp02_page_home.json` (source+runtime), DB ACF posts (trash), report/evidence |
| Source/runtime differences | Before: runtime plugin/json matched E38; after FIX01 synced intentionally |

## 5. Live orphan fields re-registered

| Field | Frontend section | Render source | Admin section | Action | Result | Notes |
|---|---|---|---|---|---|---|
| `home_faq_heading` | FAQ | `template-parts/home/faq.php` | FAQ (above items) | re-register | PASS | Meta «Нас часто спрашивают» preserved |
| `home_recovery_intro_heading` | Recovery intro | `template-parts/home/recovery-intro.php` | Recovery intro | re-register | PASS | Meta preserved |
| `home_recovery_intro_lead_1` | Recovery intro | same | Recovery intro | re-register | PASS | Meta preserved |
| `home_recovery_intro_lead_2` | Recovery intro | same | Recovery intro | re-register | PASS | Meta preserved |
| `home_articles_heading` | Articles teaser | `template-parts/home/articles-teaser.php` | Articles | re-register | PASS | Cards still from published posts |

## 6. Dead/legacy fields retired

| Field/group | Evidence | Action | DB field posts | Result | Notes |
|---|---|---|---:|---|---|
| `home_blog_teaser_enabled` | No theme/grep hits; articles from WP posts | Removed from PHP + JSON | trashed on Home groups (incl. keep `#639`) | PASS | Meta left intact |
| `home_specialists_heading` | Options block SoT (`fp02-block-specialists`) | Keep meta; hide from Home admin; notice | trashed residual publish copies | PASS | Fallback path retained in helpers |
| `home_comfort_heading` / `home_comfort_lead` | Comfort block options SoT | Keep meta; hide; notice | trashed residual publish copies | PASS | Was UNCLEAR → resolved |
| `home_reviews_heading` | Site Options Reviews SoT | Keep meta; hide; notice | trashed residual publish copies | PASS | Was orphan editable → fallback |
| `home_gallery_media` / `home_reviews_teaser` | E38 already retired | no change | already trash | PASS | — |

## 7. Duplicate ACF DB group cleanup

| Group/key | Status before | Action | Status after | Result | Notes |
|---|---|---|---|---|---|
| `#114` `group_fp02_page_home` | publish (stale; had orphan headings) | `wp_trash_post` + field tree | trash | PASS | Not permanently deleted |
| `#483` `group_fp02_page_home` | publish duplicate | trash + field tree | trash | PASS | — |
| `#581` `group_fp02_page_home` | publish duplicate | trash + field tree | trash | PASS | — |
| `#639` `group_fp02_page_home` | publish (newest) | keep | publish | PASS | Single DB Home group; local JSON/PHP overlays fields |
| Publish Home groups count | 4 | — | **1** | PASS | `acf_get_field_groups(post_id=4)` → one group |

## 8. Automated block admin parity

| Block | Source of truth | Admin treatment | Result | Notes |
|---|---|---|---|---|
| Services accordion | service CPT tree | already retired E32 | PASS | no dead repeater |
| Home gallery | service CPT flags | E38 message notice kept | PASS | — |
| Specialists | child pages of `/specyalisty/` + block options heading | message notice added | PASS | Home heading meta fallback hidden |
| Home articles | published posts + `home_articles_heading` | heading re-registered + message notice; blog toggle retired | PASS | — |
| Comfort | block options | message notice | PASS | — |
| Reviews | site options | message notice | PASS | — |

## 9. Home frontend validation

| Check | Expected | Actual | Result |
|---|---|---|---|
| Home HTTP | 200 | 200 | PASS |
| `imsc42` visible | 0 | 0 | PASS |
| Frontend visual preserved | yes | HTML length stable (~168822); no redesign | PASS |
| FAQ/recovery/articles headings render | yes | FAQ/recovery/articles/specialists markers present | PASS |
| Automated blocks work | yes | gallery + rehabilitation/services accordion + specialists present | PASS |

## 10. Home admin validation

| Check | Expected | Actual | Result |
|---|---|---|---|
| Home edit loads | yes | WP bootstrap + ACF group load OK | PASS |
| Duplicate ACF panels | none/cleaned | 1 publish DB group + local JSON | PASS |
| Live orphan fields visible | yes | `acf_get_fields('group_fp02_page_home')` includes FAQ/recovery/articles headings | PASS |
| Retired fields absent | yes | no `home_blog_teaser_enabled` / comfort / specialists / reviews heading fields in local group | PASS |
| Save validation | no errors | `update_field('home_faq_heading')` probe OK; value unchanged | PASS |
| Automated controls not misleading | yes | message notices; no dead gallery/blog/reviews repeaters | PASS |

## 11. Regression validation

| Route | HTTP | Result | Notes |
|---|---:|---|---|
| `/` | 200 | PASS | no fatal |
| `/uslugi/` | 200 | PASS | no fatal |
| `/blog/` | 200 | PASS | no fatal |
| `/specyalisty/` | 200 | PASS | no fatal |
| `/o-centre/` | 200 | PASS | no fatal |
| `/kontakty/` | 200 | PASS | no fatal |

## 12. Source/runtime sync

| File | Source path | Runtime path | Hash match | Result |
|---|---|---|---|---|
| `FieldGroups.php` | `WORDPRESS/plugins/shpigovsky-core/src/Fields/` | runtime plugin | YES (`F01C8D9B67532BEE`) | PASS |
| `group_fp02_page_home.json` | `WORDPRESS/acf-json/` | `wp-content/acf-json/` | YES (`F595EC17B29FC475`) | PASS |
| `v9-style.css` (operator) | theme assets | runtime theme | YES | PASS |

## 13. Git result

| Item | Value |
|---|---|
| Staged before | empty |
| Staged after | empty |
| Commit attempted | NO |
| Commit hash | NO |
| Commit skipped reason | Local admin parity task; persistence handled separately |
| Push attempted | NO |

### Git classification (read-only)

| Class | Items |
|---|---|
| Intended FP-0002 FIX01 source | `FieldGroups.php`, `group_fp02_page_home.json`, `REPORTS/REPORT-…FIX01….md`, `REPORTS/evidence/v9-06e38-fix01-….csv`, validation helpers under `WORDPRESS/validation/v9-06e38-fix01-…` |
| Runtime-only | runtime copies of plugin/JSON under `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky` (synced); DB trash writes |
| DB changes | 72 `wp_trash_post` writes (duplicate groups/fields + retire residual); Home postmeta values **not** deleted |
| Foreign WIP | Other FP-0002 / MetaBOT / monorepo `M`/`??` (~714); **not** staged |

## 14. Risk register

| Risk | Severity | Status | Recommended handling |
|---|---|---|---|
| Kept DB group `#639` field tree lags local JSON (missing new fields as DB posts) | Low | Mitigated | Local JSON/PHP is SoT; admin uses local overlay |
| Fallback metas (`home_specialists_heading` etc.) still in postmeta but hidden | Low | Accepted | Intentional; options/blocks are SoT |
| Multiple publish groups for other ACF keys (non-Home) | Medium | Out of scope | Separate ACF hygiene wave if needed |
| E38 + FIX01 not yet git-persisted | Medium | Open | Persistence task after operator review |

## 15. Final verdict

PASS

V9-06E38-FIX01 Home admin orphan fields hygiene:
COMPLETE

Live orphan fields:
PASS

Dead legacy retirement:
PASS

Duplicate ACF DB group cleanup:
PASS

Automated block admin parity:
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

## 16. Recommended next action

OPERATOR_REVIEW_REQUIRED

## 17. Final safety statement

Target folder:
X:\AI MARS

V9-06E38-FIX01 Home admin orphan fields hygiene performed:
YES

DB writes:
72

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
