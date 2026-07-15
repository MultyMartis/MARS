# REPORT — FP-0002 V9-06E46-FIX05 SECTION DEMO DATA AND NO TEMPLATE FALLBACK

## 1. Safety preflight

| Check | Value |
|---|---|
| Volume | X: |
| Label | AI WS |
| Repository | X:\AI MARS |
| Branch | mars/canonical-post-recovery |
| HEAD | 8341f5690827df2c43d4f552132f9ca56426cfb7 |
| Staged files before | (empty) |
| WIP count only | 798 |
| Runtime/source canon detected | YES — FP-0002 `WORDPRESS/` + local `http://shpigovsky.test` |
| Home frozen state untouched | YES |
| Services hub frozen visual untouched | YES |
| Commit allowed | NO |
| Result | PASS (note: HEAD ahead of origin — no commit/push; foreign WIP left untouched) |

## 2. Backup

| Item | Value |
|---|---|
| Backup path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e46-fix05-section-demo-data-no-template-fallback-before-20260715-004351\` |
| DB dump | `mars_wp_fp0002.sql` (~3.06MB; SHA256 `201DA9CCCF09DBB627BF0B2A54D81DD2BA298D0A3F4129B97179A0B17D9973F7`; `--no-tablespaces`) |
| Theme backup/hash | copied; aggregate md5 `5bfa27a2ac170f7ff66c366f665548ce` |
| Plugin backup/hash | copied; aggregate md5 `327d46c0e19e4265449691231c8dbc06` |
| ACF JSON backup/hash | copied; aggregate md5 `ffa9d4e5a5b153f6de266d55b6cd81b5` |
| Section ACF export before | `acf-group_fp02_service_section_parity-before.json` + source group dump |
| #73/#77/#84 meta export before | `meta/postmeta-73-77-84-section-before.tsv` (517 rows) |
| Home/image source exports before | `exports/home-image-sources-before.tsv` (landscape `#1239`, staff `#1238`); media search; zavisimosti image srcs |
| Frontend snapshots before | `/`, `/uslugi/`, `#73/#77/#84` routes under `frontend/` |
| Result | PASS |

## 3. Template fallback audit

| Block | Fallback before | ACF field after | Seeded | Remaining fallback | Result | Notes |
|---|---|---|---|---|---|---|
| Dependencies chrome | PHP static heading/lorem | `section_dependencies_*` | yes (#77/#84); #73 preserved | emergency only | PASS | Children list still automatic CPT |
| Nature | PHP neuro/geno/cards | `section_nature_*` | yes | emergency helpers | PASS | #73 operator strings preserved |
| Program intros | demo PHP | `section_program_intro_items` | yes empty pages | emergency | PASS | #73 intros preserved |
| Stages | Structured/theme | `section_stages_items` | yes | emergency + legacy stages | PASS | seeded from resolved FE |
| Approach text/cards | PHP | `section_approach_*` | yes empty | emergency | PASS | |
| Team image | theme asset | `section_team_image` | `#1238` | emergency theme | PASS | Home meta untouched |
| Corridor image | theme asset | `section_corridor_image` | `#1709` | emergency theme | PASS | ML attachment from theme copy |
| Landscape | section field (FIX04) | `section_clinic_landscape_image` | already `#1239` | emergency theme | PASS | |
| Comfort/Reviews/Specialists/Founder/Final form | shared/global | visibility only | n/a | intentional automatic | PASS | documented |

## 4. Seeded demo/content fields

| Post | Field | Before | Seeded value/source | Existing value preserved | Result | Notes |
|---|---|---|---|---|---|---|
| #73 | most text/repeaters | meaningful/demo/ТЕСТ/000101 | n/a | YES | PASS | not overwritten |
| #73 | `section_nature_text_blocks` | empty | legacy-resolved neuro/geno | n/a | PASS | seeded |
| #73 | `section_stages_items` | empty | structured stages | n/a | PASS | seeded |
| #73 | `section_team_image` | empty | `#1238` | n/a | PASS | |
| #73 | `section_corridor_image` | empty | `#1709` | n/a | PASS | |
| #77/#84 | empty section parity fields | empty | shared FE demo | n/a | PASS | ~60 estimated empty→seed writes across 3 posts |
| #77/#84 | images | empty | `#1238` / `#1709` / `#1239` | n/a | PASS | |

See `REPORTS/evidence/v9-06e46-fix05-seeded-fields.csv`.

## 5. Section image fields

| Image block | Before source | New/current field | Seeded image ID | Home dependency removed | Frontend unchanged | Result |
|---|---|---|---:|---|---|---|
| Территория клиники | `section_clinic_landscape_image` (FIX04) | section_clinic_landscape_image | 1239 | YES (already) | YES (same uploads URL) | PASS |
| Команда | theme `staff-group.webp` | section_team_image | 1238 | YES (ACF primary; Home meta untouched) | YES (same image asset via uploads) | PASS |
| Коридор | theme `interior-corridor.webp` | section_corridor_image | 1709 | YES | YES (same image via uploads copy) | PASS |

## 6. Admin wording cleanup

| Wording area | Before | After | Result | Notes |
|---|---|---|---|---|
| Dependencies / nature / program / stages / approach instructions | «Если пусто — fallback шаблона…» | «Заполнено демо-контентом… / аварийный резерв» | PASS | |
| Corridor/team image instructions | theme asset wording | section-specific + emergency reserve | PASS | |
| Landscape notice | «Не берётся с главной» + theme reserve | ACF page SoT + emergency reserve (no Home-as-normal) | PASS | |
| Admin probe bad-wording list | 20 fallback phrases (before) | 0 matches for forbidden cues | PASS | evidence admin JSON |

## 7. Admin validation

| Check | Expected | Actual | Result |
|---|---|---|---|
| #73 edit loads | yes | parity group loads; 55 fields | PASS |
| Territory image filled | yes | `#1239` | PASS |
| Team image filled | yes | `#1238` | PASS |
| Corridor image filled | yes | `#1709` | PASS |
| No Home-as-primary wording | yes | no bad cue matches | PASS |
| No normal template fallback wording | yes | cleaned | PASS |
| Classic editor hidden | yes | service CPT hide helpers/hooks from FIX04 remain | PASS |
| Save validation | no errors | `update_field` seed OK | PASS |
| #77/#84 compatible | yes | seeded; no fatal | PASS |

## 8. Frontend validation

| Check | Expected | Actual | Result |
|---|---|---|---|
| `/uslugi/zavisimosti/` HTTP | 200 | 200 | PASS |
| Visual preserved | yes | same image assets; #73 operator text retained | PASS |
| Territory image unchanged | yes | uploads landscape-1.webp | PASS |
| Team image unchanged | yes | same staff-group asset (now via uploads/ACF) | PASS |
| Corridor image unchanged | yes | same corridor asset (now via uploads/ACF) | PASS |
| No broken empty blocks | yes | team/corridor/landscape present | PASS |
| No debug/test text newly introduced | yes | no FIX05 leak; #73 existing ТЕСТ/000101 preserved | PASS |

Resolve evidence (#73): `acf:section_team_image`, `acf:section_corridor_image` (not emergency theme).

## 9. Other section pages validation

| Route | HTTP | Result | Notes |
|---|---:|---|---|
| `/uslugi/psihicheskoe-zdorovie/` | 200 | PASS | ACF images via uploads |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` | 200 | PASS | ACF images via uploads |

## 10. Frozen pages validation

| Page | Expected | Actual | Result |
|---|---|---|---|
| Home `/` | unchanged | HTTP 200; Home staff `#1238` / landscape `#1239` untouched | PASS |
| Services hub `/uslugi/` | unchanged | HTTP 200; no section-image work on hub | PASS |

## 11. Regression validation

| Route | HTTP | Result | Notes |
|---|---:|---|---|
| `/` | 200 | PASS | |
| `/uslugi/` | 200 | PASS | |
| `/uslugi/zavisimosti/` | 200 | PASS | |
| `/uslugi/psihicheskoe-zdorovie/` | 200 | PASS | |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` | 200 | PASS | |
| `/uslugi/lechenie-narkoticheskoy-zavisimosti/` (#314) | 200 | PASS | |
| `/uslugi/lechenie-alkogolnoy-zavisimosti/` (#74) | 200 | PASS | |
| `/uslugi/psihicheskoe-zdorovie/depressiya/` (#78) | 200 | PASS | |
| `/blog/` | 200 | PASS | |
| `/specyalisty/` | 200 | PASS | |
| `/o-centre/` | 200 | PASS | |
| `/kontakty/` | 200 | PASS | |

## 12. Source/runtime sync

| File | Source path | Runtime path | Hash match | Result |
|---|---|---|---|---|
| ServiceSectionParity.php | `WORDPRESS/plugins/shpigovsky-core/src/Fields/ServiceSectionParity.php` | runtime plugin | YES | PASS |
| service-section-helpers.php | `WORDPRESS/theme/shpigovsky/inc/service-section-helpers.php` | runtime theme | YES | PASS |
| team-stats.php | `WORDPRESS/theme/shpigovsky/template-parts/service/team-stats.php` | runtime theme | YES | PASS |
| group_fp02_service_section_parity.json | `WORDPRESS/acf-json/` | `wp-content/acf-json/` | YES | PASS |

Operator CSS `v9-style.css` SHA256 unchanged: `C858903FF42CE4F949799BBF374B070E7B238C60909C7C7E73CA06B2A46EF5A9`.

## 13. Documentation/evidence

| File | Action | Result | Notes |
|---|---|---|---|
| REPORT-FP-0002-V9-06E46-FIX05-section-demo-data-no-template-fallback.md | created | PASS | this file |
| SERVICE-SECTION-ADMIN-PARITY-MODEL-v1.md | updated | PASS | FIX05 section |
| PROJECT-STATUS.md | updated | PASS | |
| WORDPRESS/SOURCE-AUTHORITY.md | updated | PASS | |
| v9-06e46-fix05-section-template-fallback-audit.csv | created | PASS | |
| v9-06e46-fix05-section-acf-completeness-audit.csv | created | PASS | |
| v9-06e46-fix05-section-image-source-audit.csv | created | PASS | |
| v9-06e46-fix05-seeded-fields.csv | created | PASS | |
| v9-06e46-fix05-admin-validation.csv | created | PASS | |
| v9-06e46-fix05-frontend-validation.csv | created | PASS | |

## 14. Git result

| Item | Value |
|---|---|
| Staged before | (empty) |
| Staged after | (empty) |
| Commit attempted | NO |
| Commit hash | NO |
| Commit skipped reason | Local service section demo data/no fallback fix; persistence handled separately |
| Push attempted | NO |

### Git classification (read-only)

| Class | Paths / notes |
|---|---|
| Intended FP-0002 E46-FIX05 source | `ServiceSectionParity.php`, `service-section-helpers.php`, `team-stats.php`, `group_fp02_service_section_parity.json`, model/status/source-authority, FIX05 report + evidence |
| Runtime-only | mirrored under `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky\wp-content\...` |
| DB changes | ~60 ACF field seeds on `#73/#77/#84` |
| Media changes | corridor attachment `#1709` created from theme asset (staff/landscape reused existing) |
| Docs/evidence | REPORTS + DOCS updates |
| Foreign WIP | remaining ~798 WIP / other untracked REPORTS history — untouched |

## 15. Risk register

| Risk | Severity | Status | Recommended handling |
|---|---|---|---|
| Emergency PHP fallbacks still exist for unseeded future section pages | low | accepted | keep as safety net; seed on create |
| `#77/#84` share zavisimosti-oriented demo copy | medium | accepted by charter | Olga/operator replace per page |
| Team image reuses Home ML id `#1238` | low | accepted | Home meta untouched; section field independent |
| Corridor URL moved theme→uploads | low | accepted | same visual file |
| Unpushed commits ahead of origin | medium | noted | no commit/push this task |

## 16. Final verdict

PASS

V9-06E46-FIX05 Section demo data / no template fallback:
COMPLETE

Backup:
PASS

Template fallback dependency removal:
PASS

Demo data seeding:
PASS

Section image fields:
PASS

Admin wording cleanup:
PASS

Admin validation:
PASS

Base page frontend preserved:
PASS

Other section pages preserved:
PASS

Services hub frozen visual untouched:
PASS

Home frozen state untouched:
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

## 17. Recommended next action

OPERATOR_REVIEW_REQUIRED

## 18. Final safety statement

Target folder:
X:\AI MARS

V9-06E46-FIX05 Section demo data / no template fallback performed:
YES

Home frozen state touched:
NO

Services hub frozen visual touched:
NO

DB writes:
60

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
