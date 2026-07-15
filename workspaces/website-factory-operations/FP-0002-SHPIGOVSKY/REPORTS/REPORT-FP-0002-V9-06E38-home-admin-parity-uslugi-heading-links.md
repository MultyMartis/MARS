# REPORT — FP-0002 V9-06E38 HOME ADMIN PARITY AND USLUGI CATEGORY LINKS

## 1. Safety preflight

| Check | Value |
|---|---|
| Volume | X: |
| Label | AI WS |
| Repository | X:\AI MARS |
| Branch | mars/canonical-post-recovery |
| HEAD | ee0c46532a5fbf41a3cfc9d7f755a1341f529a55 |
| Staged files before | (empty) |
| WIP count only | ~710–712 (foreign monorepo WIP; MetaBOT commits ahead of origin) |
| Runtime/source canon detected | YES — runtime theme CSS preflight MATCH with source before edits; runtime patched first, then synced |
| Commit allowed | NO |
| Result | PASS (local bounded writes only; commit skipped) |

## 2. Backup

| Item | Value |
|---|---|
| Backup path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e38-home-admin-parity-uslugi-links-before-20260713-190141` |
| DB dump | `mars_wp_fp0002.sql` (2 293 554 bytes; `--no-tablespaces`) |
| Theme backup/hash | theme / `df708fbe70f0ad3a` (631 files) |
| Plugin backup/hash | plugin / `f472b8162bea9535` (21 files) |
| ACF JSON backup/hash | acf-json / `dbe4eaabdd339ebf` (9 files) |
| Home meta export before | `exports/home-meta-before.tsv`, `exports/home-imsc42-meta-before.tsv` |
| Home ACF group export before | `exports/home-acf-fields-before.tsv`, `exports/group_fp02_page_home-before.json` |
| Home snapshot before | `snapshots/home-before.html` |
| `/uslugi/` snapshot before | `snapshots/uslugi-before.html` |
| Result | PASS |

## 3. `/uslugi/` category link audit

| Area | Finding |
|---|---|
| Render source | `template-parts/services-hub/service-group.php` (`.services-category-section-v2__marker` / `__heading`) |
| Category data source | `shpigovsky_get_services_hub_groups()` in `inc/services-hub-helpers.php` — root `service` CPT parents (`parent_id` already present) |
| Current marker logic | Sequential `shpigovsky_format_services_hub_group_marker($marker_index)` → `01`/`02`/`03` |
| Files to change | `services-hub-helpers.php` (add `url` = `get_permalink($parent)`), `service-group.php` (wrap marker/heading in `<a>`), `v9-style.css` (link styles) |

## 4. Home ACF/admin audit

| Area | Finding |
|---|---|
| Home page ID/template | Page `#4` (`glavnaya`); `show_on_front=page`; front-page ACF location |
| Field groups found | Canonical PHP `group_fp02_page_home` via `FieldGroups.php` + duplicate stale DB `acf-field` trees (pre-existing) |
| `imsc42` fields found | 47 Home `#4` text/meta values with leading `imsc42` (hero, advantages, intro bands, FAQ, CTA, legacy gallery titles); frontend showed 39 markers before cleanup |
| Legacy gallery/media band fields | `home_gallery_media` / label «Gallery / media bands (legacy; Home gallery now uses service CPT)» — not used by `gallery.php` |
| Automated blocks with legacy admin fields | Gallery (service CPT), services accordion (CPT, E32), specialists (child pages + options block), articles (WP posts) |
| Live editable fields | `hero_media`, `hero_cta_label`, `home_hero_slides`, `home_advantages`, `home_intro_bands`, `home_faq_items`, `home_cta_title`, `home_cta_text` |
| Dead legacy fields | `home_gallery_media` (removed), `home_reviews_teaser` (removed; already UI-hidden), `home_blog_teaser_enabled` (unused by theme; kept with instruction) |
| Unclear fields | Orphan live metas not in current `FieldGroups.php`: `home_faq_heading`, `home_recovery_intro_*`, `home_articles_heading`, `home_reviews_heading`, `home_comfort_*`, `home_specialists_heading` (fallback) — left intact |
| Classification artifact | `REPORTS/evidence/v9-06e38-home-acf-field-classification.csv` |

## 5. `/uslugi/` implementation

| Requirement | Implementation | Result | Notes |
|---|---|---|---|
| Marker links | `<a class="services-category-section-v2__marker-link">` inside marker; `tabindex="-1"` (decorative) | PASS | Numbering preserved |
| Heading links | `<a class="services-category-section-v2__heading-link">` wrapping title | PASS | Accessible primary link |
| Correct URLs | Parent service permalink | PASS | `/uslugi/zavisimosti/`, `/uslugi/psihicheskoe-zdorovie/`, `/uslugi/rasstroystva-pischevogo-povedeniya/` |
| Visual preserved | Inherit color; no underline; focus-visible outline | PASS | Additive CSS only |
| Slider unaffected | `data-services-category-gallery` + pagination still present | PASS | No arrow controls reintroduced |

## 6. Home admin cleanup implementation

| Field/group | Classification | Action | Result | Notes |
|---|---|---|---|---|
| Gallery / media bands legacy (`home_gallery_media`) | DEAD_LEGACY | Removed from `FieldGroups.php` + ACF JSON; trashed DB `acf-field` posts | PASS | Meta rows preserved; frontend gallery unchanged |
| Home gallery notice | AUTOMATED_NO_ADMIN_FIELD_NEEDED | Added message field `home_gallery_source_notice` | PASS | Explains CPT automation |
| Reviews teaser (`home_reviews_teaser`) | DEAD_LEGACY | Removed from PHP/JSON; trashed DB field posts | PASS | Theme hide filter left as safety |
| Blog teaser enabled | DEAD_LEGACY | Kept with instruction (unused by theme) | PASS | Conservative |
| Live text/repeater fields | LIVE_FRONTEND_EDITABLE | Kept; `imsc42` stripped | PASS | |
| Orphan heading metas | LIVE / UNCLEAR_REVIEW | Left intact | PARTIAL | Not re-registered into FieldGroups this wave |

## 7. `imsc42` cleanup

| Field | Before preview | After preview | Frontend affected | Result |
|---|---|---|---|---|
| `hero_cta_label` | `imsc42 Заказать звонок` | `Заказать звонок` | yes | PASS |
| `home_hero_slides_0_title` | `imsc42 Шпиговский дом` | `Шпиговский дом` | yes | PASS |
| `home_hero_slides_0_text` | `imsc42 Центр профилактики…` | cleaned | yes | PASS |
| `home_advantages_*` (12) | prefixed | cleaned | yes | PASS |
| `home_intro_bands_*` (12) | prefixed | cleaned | yes | PASS |
| `home_faq_items_*` (10) | prefixed | cleaned | yes | PASS |
| `home_cta_title` / `home_cta_text` | prefixed | cleaned | yes | PASS |
| `home_gallery_media_*` titles/texts | prefixed | cleaned (meta only) | no (legacy) | PASS |
| **Total stripped** | **47** | — | Home `imsc42` count **0** | PASS |

## 8. Home frontend validation

| Check | Expected | Actual | Result |
|---|---|---|---|
| Home HTTP | 200 | 200 | PASS |
| `imsc42` visible | 0 | 0 | PASS |
| Services accordion automated | yes | 3 CPT groups | PASS |
| Home gallery automated | yes | 18 service slides / links | PASS |
| Home articles real posts | yes | articles teaser present | PASS |
| Specialists child-page slider | yes | specialists block present | PASS |
| Visual preserved | yes | no redesign; marker cleanup only | PASS |

## 9. Home admin validation

| Check | Expected | Actual | Result |
|---|---|---|---|
| Legacy gallery/media block | absent | `acf_get_field(field_fp02_home_gallery_media)=GONE` | PASS |
| Live fields remain | yes | hero/advantages/intro/FAQ/CTA still registered | PASS |
| Automated dead repeaters removed | yes/partial | gallery + reviews teaser removed; blog toggle kept with note | PASS |
| Save validation | no errors | max-row map no longer references removed fields | PASS |
| Unclear fields documented | yes | CSV + section 4 | PASS |

## 10. `/uslugi/` validation

| Category | Marker link HTTP | Heading link HTTP | URL | Result |
|---|---:|---:|---|---|
| Зависимости | 200 | 200 | `/uslugi/zavisimosti/` | PASS |
| Психическое здоровье | 200 | 200 | `/uslugi/psihicheskoe-zdorovie/` | PASS |
| Расстройства пищевого поведения | 200 | 200 | `/uslugi/rasstroystva-pischevogo-povedeniya/` | PASS |

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
| `services-hub-helpers.php` | `WORDPRESS/theme/shpigovsky/inc/` | runtime theme | YES | PASS |
| `service-group.php` | `WORDPRESS/theme/.../services-hub/` | runtime theme | YES | PASS |
| `v9-style.css` | `WORDPRESS/theme/.../assets/css/` | runtime theme | YES | PASS |
| `FieldGroups.php` | `WORDPRESS/plugins/shpigovsky-core/src/Fields/` | runtime plugin | YES | PASS |
| `RepeaterValidation.php` | same | runtime plugin | YES | PASS |
| `group_fp02_page_home.json` | `WORDPRESS/acf-json/` | `wp-content/acf-json/` | YES | PASS |

## 13. Git result

| Item | Value |
|---|---|
| Staged before | empty |
| Staged after | empty |
| Commit attempted | NO |
| Commit hash | NO |
| Commit skipped reason | Local product/admin parity task; persistence handled separately |
| Push attempted | NO |

### Git classification (read-only)

- **Intended FP-0002 changes:** theme helpers/partial/CSS; `FieldGroups.php`; `RepeaterValidation.php`; `group_fp02_page_home.json`; E38 validation helpers/evidence; this report; classification CSV.
- **Runtime-only changes:** mirrored under `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky\` (theme/plugin/acf-json) — synced to source for changed files.
- **DB changes:** 69 writes (47 `imsc42` strips + 22 ACF field posts trashed); Home gallery/postmeta content otherwise preserved.
- **Foreign WIP:** ~712 unrelated monorepo paths; not touched.

## 14. Risk register

| Risk | Severity | Status | Recommended handling |
|---|---|---|---|
| Duplicate stale Home ACF DB field-group trees | Medium | Open (pre-existing) | Separate ACF DB hygiene wave |
| Orphan live heading metas not in FieldGroups UI | Medium | Documented | Operator decide: re-register into PHP or leave options-only |
| `home_blog_teaser_enabled` still visible but unused | Low | Mitigated (instruction added) | Retire in later wave if confirmed unused |
| ACF JSON regenerated from PHP shape may differ from older export style | Low | Mitigated | Local PHP registration remains authority |

## 15. Final verdict

PASS

Then state:

V9-06E38 Home admin parity / Uslugi category links:
COMPLETE

/uslugi marker+heading links:
PASS

Home ACF classification:
PASS

Legacy gallery/media block removal:
PASS

imsc42 cleanup:
PASS

Home frontend preserved:
PASS

Home admin parity:
PARTIAL

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

V9-06E38 Home admin parity / Uslugi category links performed:
YES

DB writes:
69

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
