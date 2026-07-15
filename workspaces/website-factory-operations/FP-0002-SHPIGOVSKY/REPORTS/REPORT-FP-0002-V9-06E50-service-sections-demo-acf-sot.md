# REPORT — FP-0002 V9-06E50 SERVICE SECTIONS DEMO ACF SOT

## 1. Safety preflight

| Check | Value |
|---|---|
| Volume | X: |
| Label | AI WS |
| Repository | X:\AI MARS |
| Branch | mars/canonical-post-recovery |
| HEAD | 8341f5690827df2c43d4f552132f9ca56426cfb7 |
| Staged files before | (empty) |
| WIP count only | 820 → 821 |
| Runtime/source canon detected | YES — FP-0002 `WORDPRESS/` + `http://shpigovsky.test` / `mars_wp_fp0002` |
| Home frozen state untouched | YES (gallery residual order only; no Home ACF writes) |
| Services hub frozen visual untouched | YES (`/uslugi/` fingerprint match vs backup) |
| Service pages preserved | YES |
| Section model preserved | YES (E50 SoT hardening only) |
| Commit allowed | NO |
| Result | PASS (note: HEAD ahead of origin — no commit/push; foreign WIP untouched) |

## 2. Backup

| Item | Value |
|---|---|
| Backup path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e50-service-sections-demo-acf-sot-before-20260715-222858\` |
| DB dump | `mars_wp_fp0002.sql` (3 765 251 B; SHA256 `2450CB3E5CEAFCE24C258AF2F7C6EF590D36DE4B1BAAF5123DD8C9F691F115B7`; `--no-tablespaces`) |
| Theme backup/hash | copied; tree SHA256 `4de6cb025d761fdb8793ba773ddd8dce05075ce3ddcc90cc1091cab706258eaf` |
| Plugin backup/hash | copied; tree SHA256 `d903090fa373976fd9c987f2fc0ad96755a5224331fd860a4a5ad3aa6088a603` |
| ACF JSON backup/hash | copied; tree SHA256 `21f2d03304dc5295109f3b46435bab27eae3f8bffc9f7539f03685c1fb698f3b` |
| Uploads inventory/copy | `uploads-inventory.txt` (134 files) |
| Section postmeta exports before | `meta/postmeta-{73,77,84}-before.tsv` + post_content |
| Service controls exports before | `meta/postmeta-{74,314,78,81,85}-before.tsv` + post_content |
| Frontend snapshots before | `/`, `/uslugi/`, 3 section routes, controls, `/blog/`, `/specyalisty/`, `/o-centre/`, `/kontakty/` under `frontend/` |
| Result | PASS |

## 3. Section demo ACF model summary

| Area | Value |
|---|---|
| Target pages | #73 / #77 / #84 |
| ACF group | `group_fp02_service_section_parity` |
| Normal frontend text source before | ACF + normal hardcoded template demo when empty (E46-FIX05 seeded many fields, but helpers/templates still injected demo) |
| Normal frontend text source after | Page ACF (seeded/demo/current); automatic children/shared blocks unchanged |
| Empty admin field behavior after | Optional text/cards/intro/support hide or empty-safe — **no demo inject** |
| Emergency fallback status | PHP `*_fallback()` helpers retained as **technical/legacy only**; not called on normal path |
| Admin help text status | Updated: demo already in fields; clear → may hide; emergency = technical reserve |

## 4. Hardcoded fallback audit

| File/block | Before | Action | After | Result | Notes |
|---|---|---|---|---|---|
| `service-section-helpers.php` resolvers | empty → demo arrays | convert_to_empty_behavior | empty → `array()` / legacy only | PASS | emergency funcs kept |
| `nature.php` / `team-stats.php` / `stages.php` | hardcoded chrome/cards | convert_to_empty_behavior | ACF only; hide optional empty | PASS | layout preserved when seeded |
| `children.php` deps chrome | static heading/lorem footer | remove_normal_fallback | ACF + fallback intro_text/hero_lead only | PASS | children list automatic |
| `program.php` lead Lorem | inject Lorem | remove_normal_fallback | ACF/hero_lead only | PASS | programme catalogue kept shared |
| `faq.php` section heading | default title always | convert_to_empty_behavior | empty heading allowed | PASS | leaf default unchanged |
| `service-helpers.php` subnav | «Зависимости» / «Природа зависимости» | convert_to_empty_behavior | ACF labels for deps/nature/approach | PASS | fixes wrong-section copy |
| Image theme assets | theme webp if empty | keep_emergency_only | unchanged | PASS | images `#1238/#1239/#1709` seeded |

## 5. Seeded fields summary

| Post ID | Title | Fields checked | Fields seeded | Existing values preserved | Images seeded | Result | Notes |
|---:|---|---:|---:|---|---|---|---|
| #73 | Зависимости | ~28 editable | 0 (forced) | YES (ТЕСТ/000101 kept) | already present | PASS | no overwrite of operator/test |
| #77 | Психическое здоровье | ~28 editable | ~6–8 | YES for non-dep demos | already present | PASS | section-specific headings/blocks |
| #84 | Расстройства пищевого поведения | ~28 editable | ~6–8 | YES (incl. test013 lead) | already present | PASS | section-specific headings/blocks |

CSV: `REPORTS/evidence/v9-06e50-section-seeded-fields.csv` (15 seeded / 69 preserved rows at seed wave; +2 nature-block neutralize writes in fixup).

## 6. Admin validation

| Page | Expected | Actual | Result | Notes |
|---|---|---|---|---|
| #73 | demo/current content in ACF | role=section, subdivision, ACF filled, test suffixes kept | PASS | |
| #77 | demo/current content in ACF | section-specific nature/approach/deps | PASS | |
| #84 | demo/current content in ACF | section-specific nature/approach/deps | PASS | |
| Service controls | preserved | role=service on #74/#314/#78/#81/#85 | PASS | no service mutations |

## 7. Frontend validation

| Route | Expected | Actual | Result | Notes |
|---|---|---|---|---|
| `/uslugi/zavisimosti/` | 200 + section ACF content | 200; nature/approach present | PASS | |
| `/uslugi/psihicheskoe-zdorovie/` | 200 + section ACF content | 200; no dependency-title copy | PASS | subnav now ACF-driven |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` | 200 + section ACF content | 200; no dependency-title copy | PASS | |

## 8. Empty field behavior validation

| Test | Expected | Actual | Result | Notes |
|---|---|---|---|---|
| Optional section text cleared temporarily | no hardcoded demo injected | `#77` `section_nature_lead` cleared → lead element absent/empty | PASS | temp clear + restore |
| Value restored | original visible | restored | PASS | |

## 9. Accepted/frozen pages validation

| Page | Expected | Actual | Result |
|---|---|---|---|
| Home `/` | unchanged | no Home ACF writes; gallery order residual only | PASS |
| Services hub `/uslugi/` | unchanged | whitespace-normalized fingerprint match vs backup | PASS |
| Service controls #74/#314/#78/#81/#85 | unchanged | roles/layout preserved; routes 200 | PASS |
| E49 services sample | preserved | 5 samples 200 | PASS |

## 10. Regression validation

| Route | HTTP | Result | Notes |
|---|---:|---|---|
| `/` | 200 | PASS | |
| `/uslugi/` | 200 | PASS | |
| section ×3 | 200 | PASS | |
| controls ×5 | 200 | PASS | |
| E49 samples ×5 | 200 | PASS | |
| `/blog/` `/specyalisty/` `/o-centre/` `/kontakty/` | 200 | PASS | no fatal |

Full CSV: `REPORTS/evidence/v9-06e50-route-smoke.csv`.

## 11. Source/runtime sync

| File | Source path | Runtime path | Hash match | Result | Notes |
|---|---|---|---|---|---|
| service-section-helpers.php | WORDPRESS/theme/... | wp-content/themes/... | yes | PASS | |
| nature/team-stats/stages/children/program/faq | WORDPRESS/theme/... | runtime | yes | PASS | |
| service-helpers.php | WORDPRESS/theme/... | runtime | yes | PASS | subnav |
| ServiceSectionParity.php | WORDPRESS/plugins/... | runtime | yes | PASS | wording |
| group_fp02_service_section_parity.json | WORDPRESS/acf-json/... | runtime | yes | PASS | |

## 12. Documentation/evidence

| File | Action | Result | Notes |
|---|---|---|---|
| REPORT-FP-0002-V9-06E50-service-sections-demo-acf-sot.md | created | PASS | this file |
| SERVICE-SECTION-ADMIN-PARITY-MODEL-v1.md | updated | PASS | E50 section |
| PROJECT-STATUS.md | updated | PASS | |
| SOURCE-AUTHORITY.md | updated | PASS | |
| evidence CSVs | created | PASS | v9-06e50-*.csv |

## 13. Git result

| Item | Value |
|---|---|
| Staged before | empty |
| Staged after | empty |
| Commit attempted | NO |
| Commit hash | NO |
| Commit skipped reason | Local section demo ACF SoT normalization; persistence handled separately |
| Push attempted | NO |

### Git classification (read-only)

- Intended E50: report/evidence/docs + section theme/plugin/ACF JSON + validation scripts
- DB section seeding: local `mars_wp_fp0002` only
- Existing uncommitted E46–E49 product WIP under FP-0002: present, not staged
- Foreign WIP: present (~821 short lines), untouched

## 14. Risk register

| Risk | Severity | Status | Recommended handling |
|---|---|---|---|
| Unseeded future Раздел pages show thinner chrome | Medium | Accepted | Seed ACF before publish; emergency helpers exist but not normal SoT |
| Home gallery residual non-deterministic order | Low | Known prior residual | No E50 Home write; ignore unless freeze reopen |
| Operator CSS dual-path drift vs git source | Low | Preserved | Runtime hash match vs E50 backup (`11A45ABE…`) |

## 15. Final verdict

PASS

V9-06E50 Service sections demo ACF SoT:
COMPLETE

Backup:
PASS

Hardcoded fallback audit:
PASS

Demo seeding:
PASS

Normal ACF source of truth:
PASS

Empty field behavior:
PASS

Admin validation:
PASS

Frontend validation:
PASS

Service pages preserved:
PASS

Home preserved:
PASS

Services hub preserved:
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

V9-06E50 Service sections demo ACF SoT performed:
YES

Home frozen state touched:
NO

Services hub frozen visual touched:
NO

Service pages touched:
NO

Section model touched:
YES_WITH_REGRESSION_PASS

DB writes:
21

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
