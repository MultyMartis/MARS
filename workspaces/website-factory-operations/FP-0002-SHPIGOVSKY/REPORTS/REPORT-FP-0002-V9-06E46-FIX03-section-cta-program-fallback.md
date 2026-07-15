# REPORT — FP-0002 V9-06E46-FIX03 SECTION CTA CLEANUP AND PROGRAM FALLBACK

## 1. Safety preflight

| Check | Value |
|---|---|
| Volume | X: |
| Label | AI WS |
| Repository | X:\AI MARS |
| Branch | mars/canonical-post-recovery |
| HEAD | 8341f5690827df2c43d4f552132f9ca56426cfb7 |
| Staged files before | (empty) |
| WIP count only | 796 |
| Runtime/source canon detected | YES — FP-0002 WORDPRESS + local shpigovsky runtime (`http://shpigovsky.test`) |
| Home frozen state untouched | YES (home `template-parts/home/*` hash match vs FIX03 backup; HTML gallery link dynamic variance only) |
| Services hub frozen visual untouched | YES (`/uslugi/` HTML fingerprint match before/after) |
| Commit allowed | NO |
| Result | PASS (note: HEAD ahead of origin — no commit/push attempted) |

## 2. Backup

| Item | Value |
|---|---|
| Backup path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e46-fix03-section-cta-program-fallback-before-20260714-234056\` |
| DB dump | `mars_wp_fp0002.sql` (~3.0MB; SHA256 56B7D8141284DEFA5BDAC3725786EEB6A075E65421CE6DDB72F3EE1BA954431B) |
| Theme backup/hash | copied; aggregate md5 `265cdafec628e4a2879579ef31f09de3` |
| Plugin backup/hash | copied; aggregate md5 `1be72b9bb90a57c56908cb442abd66ea` |
| ACF JSON backup/hash | copied; aggregate md5 `946cd387d3b9d240dd03f9ff207fe55a` |
| Section ACF export before | `acf-group_fp02_service_section_parity-before.json` |
| #73/#77/#84 meta export before | `meta/postmeta-73-77-84-section-before.tsv` |
| Program/CTA exports before | `exports/cta-program-meta-before.tsv`, `exports/program-cta-values-before.json` |
| Frontend snapshots before | `/`, `/uslugi/`, `/uslugi/zavisimosti/`, `#77`, `#84` routes |
| Admin inventory before | `admin/admin-73-fields-before.json` (57 fields; CTA present) |
| Result | PASS |

## 3. CTA cleanup

| Item | Before | After | Frontend impact | Result | Notes |
|---|---|---|---|---|---|
| CTA admin section | 5. CTA «Раздел услуги» | removed from parity group | none | PASS | Renumbered former 6–15 → 5–14 |
| CTA toggle | visible `section_mid_cta_visible` | removed/hidden from UI | none (still default ON) | PASS | Meta kept; stack still gates mid-cta |
| CTA source of truth | notice pointed here but was ineffective for content | Structured Sections `cta_title`/`cta_text`/`cta_button_label` + site `phone_primary` via `shpigovsky_get_service_cta_band` / `mid-cta.php` | mid-cta still renders | PASS | See CTA audit CSV |

## 4. Program fallback behavior

| Field/block | Before behavior | After behavior | Empty fallback | Partial value handling | Result | Notes |
|---|---|---|---|---|---|---|
| Текст нижней ссылки программы | `shpigovsky_section_text` already user-wins; demo often stored as value | same helper + clearer instructions/placeholder | FE «подробнее о программе» | user text only | PASS | #73 keeps operator value `… ТЕСТ` |
| Intro программы repeater | empty/corrupt meta → legacy Lorem; empty rows could confuse with legacy | meaningful rows only; managed empty → demo (skip legacy fight); unmanaged → legacy → demo | demo paragraphs | no demo padding | PASS | #73 re-seeded 2 legacy rows (FE unchanged) |

Helper tests (`v9-06e46-fix03-fallback-helper-tests.json`): empty / partial / filled **PASS** on temporary `#77` meta (restored/cleaned after).

## 5. Admin validation

| Check | Expected | Actual | Result |
|---|---|---|---|
| #73 edit loads | yes | group loads; 55 fields | PASS |
| CTA dead block removed | yes | CTA_LEFT=0 | PASS |
| Program intro visible | yes | `section_program_intro_items` | PASS |
| Lower link text visible | yes | `section_program_footer_label` | PASS |
| No demo replacement warning issue | yes | instructions clarified | PASS |
| Save validation | no errors | `update_field` seed OK | PASS |
| #77/#84 compatible | yes | no #73 content copy; #77 cleaned after helper tests | PASS |

## 6. Frontend validation

| Check | Expected | Actual | Result |
|---|---|---|---|
| `/uslugi/zavisimosti/` HTTP | 200 | 200 | PASS |
| Visual preserved | yes | program + mid-cta present | PASS |
| Program intro preserved | yes | 2 Lorem intros | PASS |
| Lower link text correct | yes | `подробнее о программе ТЕСТ` | PASS |
| CTA frontend not broken | yes | `#service-subdivision-start` present | PASS |
| No debug/test text | yes | no `USER_*` leak | PASS |

## 7. Other section pages validation

| Route | HTTP | Result | Notes |
|---|---:|---|---|
| `/uslugi/psihicheskoe-zdorovie/` | 200 | PASS | demo/fallback safe |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` | 200 | PASS | demo/fallback safe |

## 8. Frozen pages validation

| Page | Expected | Actual | Result |
|---|---|---|---|
| Home `/` | unchanged | home templates hash match backup; HTML gallery link dynamic variance only | PASS |
| Services hub `/uslugi/` | unchanged | HTML fingerprint match | PASS |

## 9. Regression validation

| Route | HTTP | Result | Notes |
|---|---:|---|---|
| `/` | 200 | PASS | |
| `/uslugi/` | 200 | PASS | |
| `/uslugi/zavisimosti/` | 200 | PASS | |
| `/uslugi/psihicheskoe-zdorovie/` | 200 | PASS | |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` | 200 | PASS | |
| `/uslugi/lechenie-narkoticheskoy-zavisimosti/` (#314) | 200 | PASS | |
| `/uslugi/lechenie-alkogolnoy-zavisimosti/` (#74) | 200 | PASS | |
| `/uslugi/depressiya/` | 200 | PASS | |
| `/blog/` | 200 | PASS | |
| `/specyalisty/` | 200 | PASS | |
| `/o-centre/` | 200 | PASS | |
| `/kontakty/` | 200 | PASS | |

## 10. Source/runtime sync

| File | Source path | Runtime path | Hash match | Result |
|---|---|---|---|---|
| ServiceSectionParity.php | WORDPRESS/plugins/.../ServiceSectionParity.php | wp-content/plugins/... | YES | PASS |
| service-section-helpers.php | WORDPRESS/theme/.../inc/ | wp-content/themes/.../inc/ | YES | PASS |
| group_fp02_service_section_parity.json | WORDPRESS/acf-json/ | wp-content/acf-json/ | YES | PASS |

## 11. Documentation/evidence

| File | Action | Result | Notes |
|---|---|---|---|
| REPORT-FP-0002-V9-06E46-FIX03-section-cta-program-fallback.md | created | PASS | this file |
| SERVICE-SECTION-ADMIN-PARITY-MODEL-v1.md | updated | PASS | FIX03 section |
| PROJECT-STATUS.md | updated | PASS | |
| SOURCE-AUTHORITY.md | updated | PASS | |
| v9-06e46-fix03-section-cta-control-audit.csv | created | PASS | |
| v9-06e46-fix03-program-fallback-behavior-audit.csv | created | PASS | |
| v9-06e46-fix03-admin-validation.csv | created | PASS | |
| v9-06e46-fix03-frontend-validation.csv | created | PASS | |
| v9-06e46-fix03-fallback-helper-tests.json | created | PASS | empty/partial/filled |
| v9-06e46-fix03-regression.csv | created | PASS | |

## 12. Git result

| Item | Value |
|---|---|
| Staged before | (empty) |
| Staged after | (empty) |
| Commit attempted | NO |
| Commit hash | NO |
| Commit skipped reason | Local service section CTA/fallback fix; persistence handled separately |
| Push attempted | NO |

### Git classification (read-only)

| Class | Paths / notes |
|---|---|
| Intended FP-0002 E46-FIX03 | `ServiceSectionParity.php`, `service-section-helpers.php`, `group_fp02_service_section_parity.json`, FIX03 REPORT + evidence CSVs, model/status/authority docs |
| Runtime-only | copies under `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky\` (not in git) |
| DB changes | `#73` intro repeater seed (count + row texts); transient `#77` test metas cleaned |
| Media changes | none |
| Docs/evidence | FIX03 report + evidence under FP-0002 REPORTS |
| Foreign WIP | large unrelated WIP (~796); not staged/touched |

## 13. Risk register

| Risk | Severity | Status | Recommended handling |
|---|---|---|---|
| `section_mid_cta_visible` meta remains without UI | low | accepted | Keep legacy meta; optional future hard always-on |
| `#73` footer/heading still contain operator `ТЕСТ` suffix | low | known | Operator can clear/rename in admin |
| Nature/stages FIX02 repeaters still empty meta on #73 | medium (pre-existing) | open | Separate FIX04 if admin should mirror FE for those blocks |
| Home HTML non-byte-identical (gallery links) | low | accepted | Same class of variance as FIX02 |

## 14. Final verdict

PASS

V9-06E46-FIX03 Section CTA cleanup / program fallback:
COMPLETE

CTA dead block removal:
PASS

Program fallback behavior:
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

## 15. Recommended next action

OPERATOR_REVIEW_REQUIRED

## 16. Final safety statement

Target folder:
X:\AI MARS

V9-06E46-FIX03 Section CTA cleanup / program fallback performed:
YES

Home frozen state touched:
NO

Services hub frozen visual touched:
NO

DB writes:
1 durable (#73 `section_program_intro_items` seed; plus cleaned transient helper-test metas on #77)

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
