# REPORT — FP-0002 V9-06E40 HOME ADMIN EDITABLE BLOCKS EXPANSION

## 1. Safety preflight

| Check | Value |
|---|---|
| Volume | X: |
| Label | AI WS |
| Repository | X:\AI MARS |
| Branch | mars/canonical-post-recovery |
| HEAD | 1b7cda593165eb4a7b8b745d6b416b18fcbcc7f2 |
| Staged files before | (empty) |
| WIP count only | ~721–730 (foreign monorepo WIP; MetaBOT commits ahead of origin) |
| Runtime/source canon detected | YES — `WORDPRESS/` → runtime `shpigovsky` / `shpigovsky-core` / `acf-json` |
| Commit allowed | NO |
| Result | PASS (local bounded writes only; commit skipped) |

## 2. Backup

| Item | Value |
|---|---|
| Backup path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e40-home-admin-editable-blocks-before-20260714-010957` |
| DB dump | `mars_wp_fp0002.sql` (1 583 355 bytes; `--no-tablespaces`; hash prefix `F7ABCA130E19BEE6`) |
| Theme backup/hash | theme / 632 files |
| Plugin backup/hash | plugin / 22 files |
| ACF JSON backup/hash | acf-json / 9 files |
| Home meta export before | `exports/home-meta-before.tsv` |
| Home ACF group export before | `exports/home-acf-groups-before.tsv` |
| Home admin inventory before | `exports/home-admin-inventory-before.txt` (20 fields pre-E40) |
| Home frontend snapshot before | `snapshots/home-before.html` (HTTP 200, 186 111 bytes) |
| Media mapping before | `media-map/media-mapping-before.json` |
| Result | PASS |

## 3. Pre-implementation audit

| Area | Finding |
|---|---|
| Home page ID/template | Page `#4` front page; `front-page.php` + `template-parts/home/*` |
| Home partials audited | recovery-intro, treatment-prevention, gallery, why-us, staff-photo, clinic-landscape, recovery-life, genotyping, videos (+ helpers) |
| Existing Home ACF group | `group_fp02_page_home` — 20 fields after E39; PHP local + DB `#639` |
| Existing orphan/meta reused | No prior `home_why_us*` / `home_videos*` / `home_genotyping*` / benefits / gallery mode meta; existing recovery heading/leads preserved |
| Blocks missing admin controls | benefits list; treatment heading/lead; gallery modes; why-us; staff/landscape; recovery-life; genotyping; videos |
| Media/video assets found | Theme assets only pre-E40; ML attachments created on seed `#1238–1243` |
| Files to change | FieldGroups.php, RepeaterValidation.php, home-fallbacks.php, home-helpers.php, 8 Home partials, ACF JSON, validation runners, report/evidence, status docs |
| Source/runtime differences | Pre-task hashes matched for audited Home files; post-task MATCH for all changed deliverables |

## 4. Content extraction and seeding

| Block | Element | Current source | ACF field | Seeded | Result | Notes |
|---|---|---|---|---|---|---|
| recovery-intro | benefits (6) | fallbacks | `home_recovery_intro_benefits` + enabled | yes | PASS | |
| treatment | heading/lead | hardcoded | `home_treatment_prevention_*` | yes | PASS | Accordion automated |
| gallery | mode/count/selected | new | `home_gallery_*` | yes | PASS | default random/12 |
| why-us | heading/lead/body/links | hardcoded | `home_why_us_*` | yes | PASS | |
| staff | image | theme asset | `home_staff_photo_image` | yes | PASS | ML #1238 |
| landscape | image | theme asset | `home_clinic_landscape_image` | yes | PASS | ML #1239 |
| recovery-life | content/stages | hardcoded | `home_recovery_life_*` | yes | PASS | E36 CSS untouched |
| genotyping | full block | hardcoded | `home_genotyping_*` | yes | PASS | Home only |
| videos | 2 clips + posters | theme assets | `home_videos_*` | yes | PASS | ML #1240–1243 |

Evidence: `REPORTS/evidence/v9-06e40-home-current-content-extraction.csv`

## 5. ACF fields added/updated

| Field | Type | Section | Default/seed | i18n-ready | Result | Notes |
|---|---|---|---|---|---|---|
| (see CSV) | mixed | Home group | seeded | yes (`shpigovsky-core`) | PASS | Top-level count 20 → **55** |

Evidence: `REPORTS/evidence/v9-06e40-home-acf-fields-added.csv`

**Toggle model:** list-level `home_<block>_<list>_enabled` (default on) + per-row `item_enabled` (default on). Gallery uses display mode instead of a simple on/off.

## 6. Block implementation

| Requirement | Implementation | Result | Notes |
|---|---|---|---|
| Recovery intro benefits editable | ACF repeater + toggle; partial reads ACF/fallback | PASS | |
| Treatment heading/lead editable | ACF text/textarea; accordion unchanged | PASS | |
| Gallery settings | mode all/random/selected; helper selection | PASS | `shuffle()` per request |
| Why-us editable | heading/lead/body/links + toggles | PASS | |
| Staff photo editable | ACF image → ML | PASS | |
| Clinic landscape editable | ACF image → ML | PASS | |
| Recovery life content/stages editable | heading/highlight/intro/stages + toggles | PASS | |
| Genotyping editable | full Home block fields | PASS | treated once |
| Videos Media Library editable | file+poster repeater | PASS | fancybox preserved |
| Repeatable toggles | list + item toggles on touched repeaters | PASS | |

## 7. Gallery settings validation

| Mode | Expected | Actual | Result | Notes |
|---|---|---|---|---|
| all | all eligible services | 18 | PASS | |
| random | N services, default 12 | helper 12 | PASS | HTML class count 13 = 12 slides + `__slider` prefix match |
| selected | selected services only | 3 of 3 | PASS | empty → random fallback; restored |

Evidence: `REPORTS/evidence/v9-06e40-home-gallery-settings-validation.csv`

**Eligibility:** published `service`, depth-1, `service_show_on_home_gallery` (default true). Draft/trash excluded. Image helper/fallback unchanged.

## 8. Media/video validation

| Block | Field | Attachment/media | URL | Frontend render | Result |
|---|---|---|---|---|---|
| Staff photo | `home_staff_photo_image` | #1238 | `/uploads/2026/07/shpigovsky-staff-group.webp` | YES | PASS |
| Clinic landscape | `home_clinic_landscape_image` | #1239 | `/uploads/2026/07/shpigovsky-clinic-landscape-1.webp` | YES | PASS |
| Videos | `home_videos_items` | #1240–1243 | interview + center mp4/posters | YES | PASS |

Evidence: `REPORTS/evidence/v9-06e40-home-media-fields-validation.csv`

## 9. Home admin validation

| Check | Expected | Actual | Result |
|---|---|---|---|
| Home edit loads | yes | ACF group publish `#1244`; `acf_get_fields` = 55 | PASS |
| New fields visible | yes | benefits/gallery/why-us/staff/life/geno/videos present | PASS |
| Fields in frontend order | yes | order follows front-page partial sequence | PASS |
| Labels in Russian | yes | RU source strings | PASS |
| Strings i18n-ready | yes | `__()` + `shpigovsky-core` | PASS |
| Seeded values present | yes | meta spot-check PASS | PASS |
| Save validation | no errors | repeater max limits extended; no required blockers | PASS |

**Note:** Prior DB group `#639` (20 fields) and import duplicate `#1153` trashed; single publish Home group `#1244` with 55 child fields. Plugin also registers local JSON/PHP group.

## 10. Home frontend validation

| Check | Expected | Actual | Result |
|---|---|---|---|
| Home HTTP | 200 | 200 | PASS |
| Visual preserved | yes | structure/classes preserved; assets now ML URLs | PASS |
| New ACF fields render | yes | markers present for all target blocks | PASS |
| Gallery slider works | yes | `data-gallery-slider` present; 12 random slides | PASS |
| Videos render | yes | uploads mp4 hrefs in HTML | PASS |
| No broken media | yes | staff/landscape/videos uploads URLs | PASS |
| No debug/test text | yes | `imsc42` = 0 | PASS |

## 11. Regression validation

| Route | HTTP | Result | Notes |
|---|---:|---|---|
| `/` | 200 | PASS | |
| `/uslugi/` | 200 | PASS | |
| `/blog/` | 200 | PASS | |
| `/specyalisty/` | 200 | PASS | |
| `/o-centre/` | 200 | PASS | |
| `/kontakty/` | 200 | PASS | |

## 12. Source/runtime sync

| File | Source path | Runtime path | Hash match | Result |
|---|---|---|---|---|
| FieldGroups.php | `WORDPRESS/plugins/.../FieldGroups.php` | runtime plugin | YES | PASS |
| RepeaterValidation.php | `WORDPRESS/plugins/.../RepeaterValidation.php` | runtime plugin | YES | PASS |
| home-fallbacks.php | `WORDPRESS/theme/.../home-fallbacks.php` | runtime theme | YES | PASS |
| home-helpers.php | `WORDPRESS/theme/.../home-helpers.php` | runtime theme | YES | PASS |
| Home partials (8) | `template-parts/home/*` | runtime theme | YES | PASS |
| group_fp02_page_home.json | `WORDPRESS/acf-json/` | runtime acf-json | YES | PASS |
| v9-style.css (operator) | n/a (unchanged vs E40 backup) | runtime vs backup | YES | PASS |

## 13. Git result

| Item | Value |
|---|---|
| Staged before | empty |
| Staged after | empty |
| Commit attempted | NO |
| Commit hash | NO |
| Commit skipped reason | Local Home admin expansion task; persistence handled separately |
| Push attempted | NO |

**Classification (read-only):**
- **Intended FP-0002:** FieldGroups, RepeaterValidation, home helpers/fallbacks, Home partials, ACF JSON, validation/v9-06e40*, REPORTS/evidence/report, PROJECT-STATUS, SOURCE-AUTHORITY
- **Runtime-only:** mirrored theme/plugin/acf-json under `X:\MARS-Localhost\...`
- **DB:** Home postmeta seeds; ACF group `#1244`; trash `#639`/`#1153`; attachments `#1238–1243`
- **Media:** 6 new attachments from theme assets
- **Foreign WIP:** remaining monorepo dirty tree (~730 lines); not touched

## 14. Risk register

| Risk | Severity | Status | Recommended handling |
|---|---|---|---|
| Home ACF group ID changed `#639`→`#1244` | medium | mitigated | Documented; single publish group; JSON/PHP authority |
| Gallery random changes per request | low | accepted | Local prototype; document; optional stable seed later |
| Media Library duplicates if re-seeded | low | mitigated | `_fp02_source_md5` reuse meta |
| Admin UI shows both local JSON + DB group | low | watch | ACF sync UI; keep JSON + PHP aligned |
| Unpushed MetaBOT commits on branch | info | noted | Out of scope; no git reconciliation |

## 15. Final verdict

PASS

V9-06E40 Home admin editable blocks expansion:
COMPLETE

Recovery intro benefits:
PASS

Treatment heading/lead:
PASS

Gallery settings:
PASS

Why-us editable:
PASS

Staff/landscape images:
PASS

Recovery life editable:
PASS

Genotyping editable:
PASS

Videos Media Library:
PASS

Repeatable toggles:
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

V9-06E40 Home admin editable blocks expansion performed:
YES

DB writes:
>20 (Home meta seeds + ACF group import/dedup + 6 media attachments)

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
