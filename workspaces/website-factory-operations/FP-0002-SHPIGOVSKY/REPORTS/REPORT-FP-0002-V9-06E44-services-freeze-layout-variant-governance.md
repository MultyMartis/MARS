# REPORT — FP-0002 V9-06E44 SERVICES FREEZE AND LAYOUT VARIANT GOVERNANCE

## 1. Safety preflight

| Check | Value |
|---|---|
| Volume | `X:` |
| Label | `AI WS` |
| Repository | `X:\AI MARS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD | `8341f5690827df2c43d4f552132f9ca56426cfb7` (session end; diverges from `origin/mars/canonical-post-recovery` @ `8958e549…`) |
| Staged files before | empty |
| WIP count only | ~766 short-status lines (foreign WIP present; not touched) |
| Runtime/source canon detected | Runtime `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky`; source `...\FP-0002-SHPIGOVSKY\WORDPRESS` |
| Home frozen state untouched | YES |
| Services hub frozen state captured | YES |
| Commit allowed | NO |
| Result | PASS (proceed; no Git mutation) |

## 2. Services freeze backup

| Item | Value |
|---|---|
| Backup path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e44-services-hub-freeze-before-layout-governance-20260714-051559\` |
| DB dump | `mars_wp_fp0002.sql` (2 658 023 bytes; SHA256 `EF59E56EEF1885535C9A075CB8F10C03E847CB79B16C5E0EEC9E40FB448DCB90`; `--no-tablespaces`) |
| Theme backup/hash | `theme/shpigovsky` + `inventories/theme-sha256.txt` (633 files) |
| Plugin backup/hash | `plugin/shpigovsky-core` + `inventories/plugin-sha256.txt` (22 files) |
| ACF JSON backup/hash | `acf-json/` + `inventories/acf-json-sha256.txt` (10 files) |
| Uploads/media manifest/copy | `uploads-manifest/uploads-sha256.txt` (127 files; manifest only) |
| Services page meta export | `exports/uslugi-page-meta.json` (page `#5`) |
| Services hub ACF group export | `exports/acf-group-1628-services-hub.json` + admin inventory |
| Service layout ACF group export | `exports/acf-group-service-layout-hero.json` |
| Root service meta export | `exports/root-services-meta.json` (`#73/#77/#84`) |
| Services frontend snapshot | `snapshots/uslugi-freeze.html` (HTTP 200) |
| Route smoke | `inventories/route-smoke.csv` |
| Result | PASS |

## 3. Services freeze validation

| Check | Expected | Actual | Result |
|---|---|---|---|
| `/uslugi/` HTTP | 200 | 200 | PASS |
| Services hero | works | `services-inner-hero` / hero slider markers present | PASS |
| Root intro/lead fields | work | `__intro` + `__lead` present in HTML | PASS |
| Service sliders | work | category/swiper markers present | PASS |
| Home frozen untouched | yes | Home group `#1338`, 74 fields; `hero--home` present; home product files not edited | PASS |

## 4. Layout variant field discovery

| Area | Finding |
|---|---|
| Field name/key | `service_layout_variant` / `field_fp02_service_layout_variant` |
| ACF group | `group_fp02_service_layout_hero` («Service — Layout and Hero») |
| Current choices | `subdivision`, `standard`, `extended`, `alcohol_special`, `placeholder` |
| Current instructions | Was technical English enum note; E44 → clear RU instruction (choices unchanged) |
| Files referencing field | Theme map/loader/stacks/partials; plugin FieldGroups/RepeaterValidation/EditorRestrictions; ACF JSON |
| Conditional logic dependencies | `service_category_section_lead` visible iff `subdivision` |
| Frontend routing dependencies | `shpigovsky_map_acf_layout_to_variant` → stack `subdivision` / `leaf` / `alcohol-special` |

## 5. Layout values behavior

| Value | Label | Frontend effect | Admin effect | Current page count | Risk if removed | Recommendation |
|---|---|---|---|---:|---|---|
| subdivision | Подраздел | Distinct `subdivision-stack` | Shows hub category lead field | 3 | **High** — breaks roots + hub | Keep |
| standard | Стандартная услуга | Maps to `leaf` | Normal leaf fields | 0 | Low frontend (unused) | Keep as default leaf meaning |
| extended | Расширенная услуга | Maps to `leaf` (**same as standard**) | Same as leaf | 0 | Low today; reserved | Keep internal; hide later in Option B advanced |
| alcohol_special | Алкогольная зависимость | Distinct `alcohol-stack` | Special template semantics | 1 | **High** — breaks `#74` | Keep |
| placeholder | Заглушка | Maps to `leaf` (**same stack**) | List status «Заглушка» | 18 | Medium admin/semantics | Keep; editor-facing in Option B |

## 6. Service page inventory summary

| Role/depth | Count | Layout values found | Mismatches | Notes |
|---|---:|---|---|---|
| Root sections (depth 0 + children) | 3 | `subdivision` | 0 | `#73/#77/#84` correct |
| Alcohol special | 1 | `alcohol_special` | 0 | `#74` correct |
| Mid-section with children | 2 | `placeholder` | 2 | `#314/#316` — warn only; no auto-change |
| Leaves / placeholders | 16+ | mostly `placeholder` or empty | empty meta on some depth-2 | Inference covers empty |
| **Total services** | **29** | see counts above | **2** clear nesting mismatches | inventory CSV |

## 7. Admin help block

| Requirement | Implementation | Result | Notes |
|---|---|---|---|
| Help block added | `EditorRestrictions::render_service_layout_help` on `acf/render_field/name=service_layout_variant` | PASS | Russian, below selector |
| Text clear for Olga | Full choice explanations + rule-of-thumb | PASS | per charter text |
| i18n-ready | `__()` / `esc_html__()` domain `shpigovsky-core` | PASS | |
| Scoped styling | `.fp02-service-layout-help` in `admin-home-acf.css`; enqueued on service CPT | PASS | no global admin breakage |
| No frontend change | Admin-only hooks + CSS | PASS | regression routes unchanged |
| Mismatch warnings | Non-blocking `admin_notices` | PASS | no auto-migrate |

## 8. Governance recommendation

Option A — Keep selector, add help and warnings  
Option B — Simplified editor model + technical advanced override  
Option C — Automatic by nesting + placeholder flag

Recommended option:
**B**

Reason:
Internal values remain wired for frontend (`subdivision`, `alcohol_special`) and admin conditionals. `extended`/`placeholder`/`standard` are not three distinct frontend stacks today, so exposing all five technical labels confuses editors. Option B keeps compatibility, adds a clear editor role (`Раздел` / `Услуга` / `Заглушка`), and parks specials in advanced. Option C is unsafe until alcohol/extended semantics are fully derivable.

Next implementation step:
`CREATE_V9_06E45_SERVICE_LAYOUT_VARIANT_IMPLEMENTATION_TASK` — editor-facing role UI + advanced technical override; still no destructive migration.

## 9. Validation

| Check | Expected | Actual | Result |
|---|---|---|---|
| Service edit screen loads | yes | hooks registered (`has_action` true for help + mismatch); PHP loads | PASS (CLI cannot render admin HTML: `is_admin()` gate) |
| Help block visible | yes/if implemented | code + RU UTF-8 present; action registered | PASS |
| Selector still works | yes | choices unchanged | PASS |
| Save validation | no errors | enum validator unchanged | PASS |
| Frontend unchanged | yes | no theme frontend stack edits; routes 200 | PASS |
| Home unchanged | yes | 74 fields / `#1338` / `hero--home` | PASS |

## 10. Regression validation

| Route | HTTP | Result | Notes |
|---|---:|---|---|
| `/` | 200 | PASS | `hero--home` |
| `/uslugi/` | 200 | PASS | hero/intro/lead/slider |
| `/uslugi/zavisimosti/` | 200 | PASS | |
| `/uslugi/psihicheskoe-zdorovie/` | 200 | PASS | |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` | 200 | PASS | |
| `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | 200 | PASS | alcohol special |
| `/uslugi/psihicheskoe-zdorovie/depressiya/` | 200 | PASS | |
| `/blog/` | 200 | PASS | |
| `/specyalisty/` | 200 | PASS | |
| `/o-centre/` | 200 | PASS | |
| `/kontakty/` | 200 | PASS | |

Note: charter path `/uslugi/zavisimosti/alkogolnaya-zavisimost/` is **404** locally; canonical slug remains `lechenie-alkogolnoy-zavisimosti` (pre-existing; not introduced by E44).

## 11. Source/runtime sync

| File | Source path | Runtime path | Hash match | Result |
|---|---|---|---|---|
| EditorRestrictions.php | `WORDPRESS/plugins/.../EditorRestrictions.php` | `wp-content/plugins/.../EditorRestrictions.php` | YES | PASS |
| FieldGroups.php | `WORDPRESS/plugins/.../FieldGroups.php` | `wp-content/plugins/.../FieldGroups.php` | YES | PASS |
| group_fp02_service_layout_hero.json | `WORDPRESS/acf-json/...` | `wp-content/acf-json/...` (+ site `acf-json/`) | YES | PASS |
| admin-editor.php | `WORDPRESS/theme/.../admin-editor.php` | `wp-content/themes/.../admin-editor.php` | YES | PASS |
| admin-home-acf.css | `WORDPRESS/theme/.../admin-home-acf.css` | `wp-content/themes/.../admin-home-acf.css` | YES | PASS |

## 12. Documentation/evidence

| File | Action | Result | Notes |
|---|---|---|---|
| REPORT-FP-0002-V9-06E44-services-freeze-layout-variant-governance.md | created | PASS | this file |
| FREEZE-FP-0002-V9-06E44-SERVICES-HUB-ACCEPTED.md | created | PASS | |
| SERVICE-LAYOUT-VARIANT-GOVERNANCE-v1.md | created | PASS | Option B |
| v9-06e44-service-layout-variant-references.csv | created | PASS | |
| v9-06e44-service-layout-variant-inventory.csv | created | PASS | 29 rows |
| v9-06e44-service-layout-variant-admin-conditional-logic.csv | created | PASS | |
| v9-06e44-service-layout-variant-frontend-effect.csv | created | PASS | |
| v9-06e44-services-freeze-validation.csv | created | PASS | |
| PROJECT-STATUS.md | updated | PASS | |
| SOURCE-AUTHORITY.md | updated | PASS | |
| SERVICES-HUB-ADMIN-PARITY-MODEL-v1.md | updated | PASS | freeze + next scope |

## 13. Git result

| Item | Value |
|---|---|
| Staged before | empty |
| Staged after | empty |
| Commit attempted | NO |
| Commit hash | NO |
| Commit skipped reason | Services freeze/governance task; persistence handled separately |
| Push attempted | NO |

### Git classification (read-only)

- **Intended E44:** freeze/docs/report/evidence; plugin help/mismatch; FieldGroups instructions; ACF JSON instructions; theme admin CSS/enqueue.
- **Runtime-only:** backup under `X:\MARS-Localhost\backups\...`; temp audit scripts under `X:\MARS-Localhost\temp\`.
- **DB changes:** **0** product writes (dump/read-only audits only).
- **Media:** none.
- **Foreign WIP:** large unrelated dirty/untracked tree remains (including non-E44 FP-0002 and other projects) — **not** staged/restored/cleaned.

## 14. Risk register

| Risk | Severity | Status | Recommended handling |
|---|---|---|---|
| Editor still sees 5 technical values | Medium | Mitigated by help | E45 Option B UI |
| Mid-sections `#314/#316` as placeholder | Low/Med | Documented | Review in E45; no auto-migrate |
| `extended` unused / undifferentiated | Low | Documented | Advanced-only later |
| Empty layout meta on depth-2 leaves | Low | Inference works | Explicit set in cleanup wave |
| Admin help not browser-probed (no login session) | Low | Code+hook verified | Operator visual glance on service edit |
| HEAD ahead of origin with foreign commits | Medium | Pre-existing | Separate Git reconciliation — out of scope |

## 15. Final verdict

**PASS**

V9-06E44 Services freeze / layout variant governance:
**COMPLETE**

Services hub freeze:
**PASS**

Layout variant audit:
**PASS**

Admin help block:
**PASS**

Governance recommendation:
**PASS**

Home frozen state untouched:
**PASS**

Services frontend preserved:
**PASS**

Regression:
**PASS**

Source/runtime sync:
**PASS**

Operator CSS preserved:
**PASS**

Git commit:
**SKIPPED**

No foreign project work:
**PASS**

Recommended next phase:
**CREATE_V9_06E45_SERVICE_LAYOUT_VARIANT_IMPLEMENTATION_TASK**

## 16. Recommended next action

CREATE_V9_06E45_SERVICE_LAYOUT_VARIANT_IMPLEMENTATION_TASK

## 17. Final safety statement

Target folder:
X:\AI MARS

V9-06E44 Services freeze / layout variant governance performed:
YES

Services hub frozen:
YES

Home frozen state touched:
NO

DB writes:
0

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
