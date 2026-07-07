# REPORT — FP-0002 V9-06E22 REMOVE GLOBAL HEROES SETTINGS FROM SITE SETTINGS

## 1. Safety preflight

- Volume: X
- Label: AI WS
- Repository: X:\AI MARS
- Branch: mars/canonical-post-recovery
- Local HEAD: bfa0f620a6e0ed8f4dfd6aa0c8b17282a3ffb855
- Local short HEAD: bfa0f620
- Remote HEAD: bfa0f620a6e0ed8f4dfd6aa0c8b17282a3ffb855
- Remote short HEAD: bfa0f620
- Ahead: 0
- Behind: 0
- Foreign WIP: extensive outside FP-0002 WORDPRESS E22 scope — preserved unstaged
- Pre-existing staged files: none
- E21 ancestor check: PASS (`a99e77bd` ancestor of HEAD; HEAD note: tip advanced to `bfa0f620`)
- Result: **PASS**

## 2. Authorization and scope

- Operator authorization: V9-06E22 Remove Global Heroes Settings — GRANTED
- Task mode: CORRECTIVE REPAIR / E21 operator QA rejection follow-up
- DB checkpoint: YES
- Fresh DB dump: YES
- DB writes: 1 (ACF global hero field group delete only)
- Source/theme changes: 2 files
- Project plugin changes: 2 files
- Third-party plugin changes: 0
- ACF JSON changes: 1 (delete `group_fp02_block_hero_fallbacks.json`)
- Runtime delivery: YES (4 source files + delete runtime ACF JSON)
- Page delete/trash/draft changes: 0
- Service clone implementation: NO
- Obsolete page cleanup: NO
- Batch 3 implementation: NO
- Global heroes settings removed: YES
- Local hero fields preserved: YES
- Reviews alias restore: NO
- Reviews data writes: 0
- Legal text writes: 0
- WP nav menu DB writes: 0
- Privacy setting writes: 0
- Rewrite/permalink changes: NO
- Plugin install/update/delete: 0
- OCPilot writes: 0
- Documentation/evidence writes: YES
- Result: **PASS**

## 3. DB checkpoint

| Item | Result | Path/notes |
|---|---|---|
| Fresh mysqldump | PASS | `v9-06e22-remove-global-heroes-settings-pre-20260708-034456/mars_wp_fp0002.sql` |
| SHA256 | PASS | 5FBB2EB8BD98C769945CA564EE84F9D3506DDC46D8E0FACA6DB1DD0EBD815506 |
| Options snapshots | PASS | batch2, global-hero, reviews, local-hero meta/groups |
| Restore instructions | PASS | `validation/v9-06e22-remove-global-heroes-settings/db-checkpoint.json` |
| Committed dump | NO | per charter |

## 4. Baseline global heroes audit

| Area | Before | Risk | Notes |
|---|---|---|---|
| `Герои` under Site Settings | present | must_remove | E21 Batch 2 direct child |
| Global hero field group | `group_fp02_block_hero_fallbacks` | must_remove | 13 option fields |
| E21 global hero option fields | 6 contexts × image/asset | must_remove | seeded theme assets |
| Local hero architecture | page/service `hero_media` | must_preserve | E7B authority |
| E21 frontend global hero reads | `shpigovsky_get_block_hero_fallback_image` | must_remove | inserted before theme fallback |

## 5. Repair plan

| Component | Planned repair | Safety |
|---|---|---|
| Admin IA | Remove `Герои` from Site Settings + fielded slugs | PASS |
| ACF | Remove global hero group registration/JSON/DB | PASS |
| Frontend | Restore local → theme fallback chain | PASS |
| Data | Orphan global options OK; no local hero writes | PASS |

## 6. Global heroes removal

| Item | Before | After | Result |
|---|---|---|---|
| Site Settings `Герои` | present | absent | PASS |
| `fp02-block-hero-fallbacks` fielded slug | present | absent | PASS |
| `group_fp02_block_hero_fallbacks` | active | deleted | PASS |
| ACF JSON source | present | deleted | PASS |
| Frontend block hero read layer | active | removed | PASS |
| Local hero field groups | present | preserved | PASS |

## 7. ACF global heroes location / sync

| Item | Before | After | DB write | Result |
|---|---|---|---|---|
| `group_fp02_block_hero_fallbacks` | present | deleted | 1 | PASS |
| Local hero groups | 4 present | 4 present | 0 | PASS |

## 8. Runtime delivery

| File | Delivered | Result | Notes |
|---|---:|---|---|
| OptionsPage.php | YES | PASS | remove Герои |
| FieldGroups.php | YES | PASS | remove block_hero_fallbacks |
| reusable-blocks-helpers.php | YES | PASS | remove block hero helpers |
| hero-helpers.php | YES | PASS | restore theme-only fallback |
| group_fp02_block_hero_fallbacks.json | deleted | PASS | runtime + source |

## 9. Post-repair admin validation

| Admin item | Result | Notes |
|---|---|---|
| No `Герои` under Site Settings | PASS | source `OptionsPage` probe |
| Шапка / Подвал / Комфорт | PASS | fielded slugs + ACF groups |
| Batch 1 preserved | PASS | final-form, specialists, cta-bands |
| Top-level Отзывы | PASS | ACF option page `fp02-reviews` |
| Local hero groups | PASS | service/home/hub/institutional |
| Screenshots | PARTIAL | HTTP/source evidence only |

## 10. Post-repair frontend regression validation

| Route/check | Result | Notes |
|---|---|---|
| `/` | PASS | HTTP 200; header/footer/comfort/rehab |
| `/uslugi/` | PASS | HTTP 200; hero marker |
| `/uslugi/zavisimosti/` | PASS | HTTP 200 |
| `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | PASS | HTTP 200 |
| `/kontakty/` | PASS | HTTP 200 |
| `/otzyvy/` | PASS | HTTP 200; reviews |
| `/privacy-policy/` | PASS | HTTP 200 |
| `/o-centre/specialistam/` | PASS | HTTP 200 |
| `/o-centre/` | PASS | HTTP 200 |

## 11. Screenshots / evidence

| Evidence | Captured | Result | Notes |
|---|:---:|---|---|
| Admin menu no heroes | 0 | PARTIAL | source/ACF probe |
| Admin header/footer/comfort | 0 | PARTIAL | ACF group probe |
| Local hero admin fields | 0 | PARTIAL | local hero groups present |
| Frontend route markers | 9 | PASS | HTTP curl validation |

## 12. Final E22 admin / hero architecture contract

| Item | Final state | Notes |
|---|---|---|
| Site Settings children | 8 items (no Герои) | see contract JSON |
| Global hero settings | not used | read layer removed |
| Local hero authority | active | E7B + page/service fields |
| Fallback chain | local → theme asset | no global options |
| E21 preserved blocks | Шапка, Подвал, Комфорт | PASS |

## 13. No-scope-drift

- DB writes: 1
- Local hero field value writes: 0
- Page/service content writes: 0
- Source/theme changes: 2
- Project plugin changes: 2
- Third-party plugin changes: 0
- ACF JSON changes: 1
- Runtime delivery: YES
- Page delete/trash/draft changes: 0
- Service clone implementation: NO
- Obsolete page cleanup: NO
- Batch 3 implementation: NO
- Reviews alias restore: NO
- Reviews data writes: 0
- Legal text writes: 0
- WP nav menu DB writes: 0
- Privacy setting writes: 0
- Rewrite flush: NO
- Plugin install/update/delete: 0
- OCPilot writes: 0
- Production migration: NO
- V9 src/dist changes: 0
- DB dumps staged: NO
- Backup payload staged: NO
- Runtime snapshots staged: NO
- Helpers/temp staged: NO
- Secrets/API keys: 0
- Result: **PASS**

## 14. Documentation changes

| File | Action | Reason |
|---|---|---|
| `reports/FP-0002-V9-06E22-...-REPORT-v1.md` | created | wave report |
| `architecture/FP-0002-V9-06E22-*.md` | created | checkpoint, audit, plan, removal, contract, next step |
| `validation/v9-06e22-remove-global-heroes-settings/*.json` | created | evidence pack |
| `WORDPRESS/README.md` | updated | E22 status |
| `WORDPRESS/SOURCE-AUTHORITY.md` | updated | E22 entry |
| `PROJECT-STATUS.md` | updated | E22 status |

## 15. Git checkpoint

- Exact staged files: E22 plugin/theme/ACF JSON delete + docs/evidence only
- Staged list inspected: YES
- Theme source files staged: YES (2)
- Project plugin files staged: YES (2)
- Third-party plugin files staged: NO
- ACF JSON staged: YES (deletion)
- Runtime files staged: NO
- OCPilot files staged: NO
- DB dumps staged: NO
- Backup payload staged: NO
- Runtime snapshots staged: NO
- Uploaded media files staged: NO
- Helper/temp files staged: NO
- Secrets staged: NO
- Commit: FP-0002: remove global hero settings
- Commit hash: (see post-commit)
- Push: normal (no force)
- Result: pending operator git wave

## 16. Final verdict

**PASS**

V9-06E22 Remove Global Heroes Settings: **COMPLETE**

DB checkpoint: **PASS**

Fresh DB dump: **PASS**

Operator E21 global heroes rejection: **ADDRESSED**

`Герои` removed from Site Settings: **PASS**

Global hero option field group removed/deactivated: **PASS**

Global hero frontend read layer removed: **PASS**

Local hero fields preserved: **PASS**

Hero frontend regression: **PASS**

E21 Header/Footer/Comfort preserved: **PASS**

Batch 1 preserved: **PASS**

Reviews alias remains removed: **PASS**

Top-level Reviews preserved: **PASS**

No-scope-drift: **PASS**

Recommended next phase: **CREATE_V9_06E23_OPERATOR_ADMIN_HERO_QA_TASK**

## 17. Recommended next action

**CREATE_V9_06E23_OPERATOR_ADMIN_HERO_QA_TASK**

## 18. Final safety statement

Target folder:
X:\AI MARS

V9-06E22 Remove Global Heroes Settings performed:
YES

DB checkpoint:
YES

Fresh DB dump:
YES

DB writes:
1

Local hero field value writes:
0

Page/service content writes:
0

Source/theme changes:
2

Project plugin changes:
2

Third-party plugin changes:
0

ACF JSON changes:
1

Runtime delivery:
YES

Page delete/trash/draft changes:
0

Service clone implementation:
NO

Obsolete page cleanup:
NO

Batch 3 implementation:
NO

Reviews alias restore:
NO

Reviews data writes:
0

Legal text writes:
0

WP nav menu DB writes:
0

Privacy setting writes:
0

Rewrite flush performed:
NO

OCPilot writes:
0

Production migration performed:
NO

V9 source changed:
NO

V9 dist changed:
NO

DB dump committed:
NO

Backup payload committed:
NO

Runtime snapshot committed:
NO

Helper/temp committed:
NO

Secrets committed:
0
