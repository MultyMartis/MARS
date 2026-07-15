# REPORT — FP-0002 V9-06E39 HOME ADMIN ORDER AND LOCALIZATION FOUNDATION

## 1. Safety preflight

| Check | Value |
|---|---|
| Volume | X: |
| Label | AI WS |
| Repository | X:\AI MARS |
| Branch | mars/canonical-post-recovery |
| HEAD | 1b7cda593165eb4a7b8b745d6b416b18fcbcc7f2 |
| Staged files before | (empty) |
| WIP count only | ~717–720 (foreign monorepo WIP; MetaBOT commits ahead of origin) |
| Runtime/source canon detected | YES — `WORDPRESS/` source → runtime `shpigovsky` / `shpigovsky-core` / `acf-json` |
| Commit allowed | NO |
| Result | PASS (local bounded writes only; commit skipped) |

## 2. Backup

| Item | Value |
|---|---|
| Backup path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e39-home-admin-order-localization-before-20260714-001557` |
| DB dump | `mars_wp_fp0002.sql` (1 542 361 bytes; `--no-tablespaces`) |
| Theme backup/hash | theme / `cf85cd6ec2a80961` (631 files) |
| Plugin backup/hash | plugin / `3103ccaaa0c1d1ba` (21 files) |
| ACF JSON backup/hash | acf-json / `b73428bf6bd6bbe5` (9 files) |
| Home meta export before | `exports/home-meta-before.tsv` |
| Home ACF group export before | `exports/home-acf-groups-before.tsv` (+ fields/all-groups) |
| Home admin inventory before | `exports/home-admin-inventory-before.txt` |
| Home frontend snapshot before | `snapshots/home-before.html` (HTTP 200, 186 111 bytes) |
| Home section order before | rebuilt from snapshot in evidence CSV (20 sections) |
| Result | PASS |

## 3. Home frontend order audit

| Artifact | Path | Rows | Result |
|---|---|---:|---|
| Frontend section order | `REPORTS/evidence/v9-06e39-home-frontend-section-order.csv` | 20 | PASS — grounded in `front-page.php` + live HTML |
| Admin field order before/after | `REPORTS/evidence/v9-06e39-home-admin-field-order-before-after.csv` | 20 field rows | PASS |
| Localization audit | `REPORTS/evidence/v9-06e39-localization-audit.csv` | 14 | PASS |

## 4. Home admin order implementation

| Frontend order | Frontend block | Admin section after | Editable/automated | Result | Notes |
|---:|---|---|---|---|---|
| 1 | hero | hero_media, hero_cta_label, home_hero_slides | editable | PASS | |
| 2 | recovery-intro | recovery heading/leads + home_intro_bands | editable | PASS | intro_bands moved with recovery |
| 3 | founder-quote | home_founder_quote_source_notice | automated | PASS | new notice |
| 4 | treatment-prevention | home_treatment_source_notice | automated | PASS | new notice |
| 5 | gallery | home_gallery_source_notice | automated | PASS | |
| 6–7 | why-us / staff-photo | (absent) | static | PASS | accepted absent |
| 8 | feature-grid | home_advantages | editable | PASS | moved from early position |
| 9–10 | clinic / recovery-life | (absent) | static | PASS | |
| 11 | reviews | home_reviews_source_notice | automated | PASS | |
| 12–14 | rehab / genotyping | (absent) | static | PASS | |
| 15 | comfort | home_comfort_source_notice | automated | PASS | |
| 16 | videos | (absent) | static | PASS | |
| 17 | specialists | home_specialists_source_notice | automated | PASS | |
| 18 | articles | home_articles_heading + notice | editable+auto | PASS | |
| 19 | faq | home_faq_heading + home_faq_items | editable | PASS | |
| 20 | final-form | home_cta_title / home_cta_text | editable fallback | PASS | |

## 5. Localization foundation

| Area | Implementation | Result | Notes |
|---|---|---|---|
| Theme text domain | `shpigovsky` in `style.css`; `load_theme_textdomain` in `inc/setup.php` | PASS | Already present |
| Plugin/field text domain | `shpigovsky-core`; added `load_plugin_textdomain` on `init` | PASS | Decision: Home ACF in plugin uses `shpigovsky-core` (matches existing admin i18n) |
| Home ACF labels | Russian originals wrapped in `__()` | PASS | Admin shows RU (`get_locale()` = `ru_RU`) |
| Home ACF instructions/notices | Russian originals wrapped in `__()` | PASS | |
| POT/language files | `languages/shpigovsky-core.pot` + `languages/shpigovsky.pot` | PASS | Manual foundation POT; no `.mo` fabricated |
| Comments/helper notes | Brief EN bilingual comments on `page_home` | PASS | No mass comment rewrite |

**Decision:** Source strings are Russian + i18n-wrapped so current admin displays Russian without needing `ru_RU.mo`. English is extractable via POT → future `en_US.po`.

## 6. ACF/DB changes

| Item | Before | After | Result | Notes |
|---|---|---|---|---|
| Home ACF group order | Mixed (advantages early; specialists early) | Frontend-aligned 20 fields | PASS | PHP + JSON |
| Home ACF DB group | `#639` publish (1); stale fields incomplete | `#639` publish; 20 fields ordered RU | PASS | Transient duplicates during sync trashed; final VERIFY_COUNT=20 |
| ACF JSON | Mixed EN/RU labels | RU resolved export | PASS | source + runtime hash match |
| Field keys/meta values | Existing meta keys | Preserved | PASS | Spot-check: FAQ/articles/recovery/CTA/advantages intact |

## 7. Home admin validation

| Check | Expected | Actual | Result |
|---|---|---|---|
| Home edit loads | yes | wp-admin edit `#4` → HTTP 302 when logged out (auth gate OK); ACF API loads 1 Home group | PASS |
| One Home ACF group | yes | 1 publish `group_fp02_page_home` | PASS |
| Admin order matches frontend | yes | 20 fields via `acf_get_fields` match frontend sequence | PASS |
| Labels in Russian current admin | yes | RU labels from PHP/DB; locale `ru_RU` | PASS |
| Strings localization-ready | yes | `__()` + POT | PASS |
| Automated notices positioned | yes | founder/treatment/gallery/reviews/comfort/specialists/articles | PASS |
| Save validation | no errors | no required blockers; meta keys preserved | PASS |

## 8. Home frontend validation

| Check | Expected | Actual | Result |
|---|---|---|---|
| Home HTTP | 200 | 200 | PASS |
| Frontend order unchanged | yes | before=after 20 sections | PASS |
| Visible text unchanged | yes | snapshot length 186 111 unchanged | PASS |
| `imsc42` visible | 0 | 0 | PASS |
| Automated blocks work | yes | gallery/treatment/articles/specialists still present in HTML | PASS |
| Visual preserved | yes | no theme CSS/template content edits | PASS |

## 9. Localization validation

| Check | Expected | Actual | Result |
|---|---|---|---|
| Text domain present | yes | theme + plugin headers | PASS |
| Text domain loaded | yes | theme already; plugin loader added | PASS (`is_textdomain_loaded` false without `.mo` — expected) |
| Changed labels wrapped | yes | Home `page_home` + shared subfield helpers | PASS |
| POT/language artifact | exists | both POTs created + runtime synced | PASS |
| PHP syntax | ok | `php -l` clean | PASS |

## 10. Regression validation

| Route | HTTP | Result | Notes |
|---|---:|---|---|
| `/` | 200 | PASS | imsc42=0 |
| `/uslugi/` | 200 | PASS | |
| `/blog/` | 200 | PASS | |
| `/specyalisty/` | 200 | PASS | |
| `/o-centre/` | 200 | PASS | |
| `/kontakty/` | 200 | PASS | |

## 11. Source/runtime sync

| File | Source path | Runtime path | Hash match | Result |
|---|---|---|---|---|
| FieldGroups.php | `WORDPRESS/plugins/shpigovsky-core/src/Fields/FieldGroups.php` | `wp-content/plugins/shpigovsky-core/src/Fields/FieldGroups.php` | YES | PASS |
| shpigovsky-core.php | `WORDPRESS/plugins/.../shpigovsky-core.php` | runtime plugin bootstrap | YES | PASS |
| group_fp02_page_home.json | `WORDPRESS/acf-json/` | `wp-content/acf-json/` | YES | PASS |
| shpigovsky-core.pot | `WORDPRESS/plugins/.../languages/` | runtime plugin languages | YES | PASS |
| shpigovsky.pot | `WORDPRESS/theme/shpigovsky/languages/` | runtime theme languages | YES | PASS |
| v9-style.css (operator) | n/a (unchanged) | runtime vs E39 backup | YES | PASS |

## 12. Git result

| Item | Value |
|---|---|
| Staged before | empty |
| Staged after | empty |
| Commit attempted | NO |
| Commit hash | NO |
| Commit skipped reason | Local admin order/localization task; persistence handled separately |
| Push attempted | NO |

### Git classification (read-only)

| Class | Paths |
|---|---|
| Intended FP-0002 | `FieldGroups.php`, `shpigovsky-core.php`, `languages/*.pot`, `acf-json/group_fp02_page_home.json`, E39 report/evidence CSVs, `PROJECT-STATUS.md`, `SOURCE-AUTHORITY.md` |
| Runtime-only | runtime plugin/theme/acf-json copies under `X:\MARS-Localhost\...` |
| DB changes | `mars_wp_fp0002` Home ACF field posts under group `#639` |
| Foreign WIP | ~700+ other monorepo paths untouched |

## 13. Risk register

| Risk | Severity | Status | Recommended handling |
|---|---|---|---|
| ACF message fields may expose empty `name` in some ACF reads | low | accepted | Keys/labels intact; message type often nameless; JSON/PHP keep names |
| Transient DB field duplicates during sync | medium | mitigated | Deduped to 20 publish fields; trash retained for rollback |
| No `.mo` yet for EN locale switch | low | documented | Compile EN PO from POT when needed |
| Main worktree foreign WIP / remote divergence | medium | unchanged | No git reconciliation; selective persistence later |

## 14. Final verdict

PASS

V9-06E39 Home admin order / localization foundation:
COMPLETE

Home admin order:
PASS

Localization foundation:
PASS

Home labels/instructions localization-ready:
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

(After operator accepts local admin UX, consider `CREATE_V9_06E38_E39_PERSISTENCE_TASK` for selective Git persistence.)

## 16. Final safety statement

Target folder:
X:\AI MARS

V9-06E39 Home admin order / localization foundation performed:
YES

DB writes:
1 (Home ACF field tree sync/reorder/dedupe under group `#639`; meta values preserved)

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
