# REPORT — FP-0002 PROD-P13-FU01 Native Slug UX

**Date:** 2026-08-16  
**Host:** `http://shpigovsky.beget.tech/`  
**Docroot:** `/home/s/shpigovsky/shpigovsky.ru/public_html`  
**Evidence:** `REPORTS/evidence/prod-p13-fu01-native-slug-ux/`

## 1. Status

- **PASS**
- Production file writes: **2** exact plugin files
- DB QA writes: reversible drafts only (created + force-deleted); lasting product URL writes **0**
- WPilot writes: **0** (`write_enabled=false`)
- Commit/push: **none**

Required closeout: `PROD-P13-FU01 NATIVE SLUG UX TECHNICAL CLOSEOUT COMPLETE — OPERATOR VISUAL ACCEPTANCE PENDING`

## 2. Root Cause

**SLUG UX DUPLICATION ROOT CAUSE IDENTIFIED**

- Duplicate UI owner: WordPress core `#edit-slug-box` **plus** `PermalinkSlugUX::render_native_permalink_box` (`edit_form_after_title`) printing a second `get_sample_permalink_html()` row labeled **Постоянная ссылка**. Side metabox `fp02_permalink_slug` (**URL / ярлык** / `fp02_post_name`) was a third control.
- Persistence conflict owner: `wp_insert_post_data` preferred `fp02_post_name` over native `post_name`; empty custom field regenerated from title even when the native slug was present.
- Service native **Изменить** was missing because `ServicePermalinks::filter_service_permalink` always returned a fully resolved URL (no `%postname%` for sample permalink HTML). Specialist already had native Edit.

Details: `REPORTS/evidence/prod-p13-fu01-native-slug-ux/ROOT-CAUSE.md`

## 3. Final Architecture

**CUSTOM ENTITY PERMALINK UX MATCHES STANDARD WORDPRESS PAGE UX**

- Canonical Admin UX: one native WordPress permalink row for public singles.
- Applicable CPTs (class A): `service`, `specialist`. Pages/posts already native (class C). Reviews are not a public CPT (class B).
- Custom UI removed: metabox, second `#edit-slug-box`, `fp02_post_name`, admin CSS/JS.
- Module `admin.permalink-slug-ux` retained as **data-layer only** (`wp_insert_post_data` + `wp_unique_post_slug`).
- Service `post_type_link` now honors `$leavename` so core can render **Изменить**. Frontend permalinks stay fully resolved. Canonical data owner: `wp_posts.post_name`.

## 4. Service QA

| Check | Result |
|-------|--------|
| One permalink row | PASS (`Постоянная ссылка` ×1, `#edit-slug-box` ×1, no `fp02_*`) |
| Native **Изменить** | PASS (`editable-post-name` = `zavisimosti`) |
| HTTP Update + reload | PASS draft `#2028` slug `fp02-fu01-http-service-saved` then deleted |
| PHP native `$_POST['post_name']` persist | PASS |
| Frontend existing URL | PASS `/uslugi/zavisimosti/` HTTP 200 |

## 5. Specialist QA

| Check | Result |
|-------|--------|
| One permalink row | PASS |
| Native **Изменить** | PASS (`kostyuk`) |
| HTTP Update + reload | PASS draft `#2029` slug `fp02-fu01-http-spec-saved` then deleted |
| PHP persist | PASS |
| Published rewrite | PASS `/specyalisty/kostyuk/` HTTP 200 |

Draft `get_permalink()` for unpublished specialists remains the core query URL (`?post_type=specialist&p=ID`). Pretty `/specyalisty/{slug}/` applies when published.

## 6. Clear / Regenerate

Native slug submitted empty → regenerate from current title (same save). Unrelated title edit without `$_POST['post_name']` does **not** regenerate.

- Service: `fp02-fu01-qa-service-native` → clear → `fp02-fu01-qa-service-regen-title` PASS
- Specialist: `fp02-fu01-qa-spec-native` → clear → `fp02-fu01-qa-specialist-regen-title` PASS

## 7. Collision

Data-layer uniqueness, no custom UI. Suffix `-copy-01`, `-copy-02` (drafts included; core skips draft uniquify).

- Service: `fp02-fu01-qa-collision` / `-copy-01` / `-copy-02` PASS
- Specialist: `fp02-fu01-qa-spec-collision` / `-copy-01` PASS

## 8. Existing URL Safety

**EXISTING PRODUCTION URLS UNCHANGED**

- Services checked: **31** before = **31** after
- Specialists checked: **9** before = **9** after
- Accidental `post_name` / permalink changes: **0**

## 9. Exact Files Changed

Source + production:

1. `WORDPRESS/plugins/shpigovsky-core/src/Admin/PermalinkSlugUX.php`
2. `WORDPRESS/plugins/shpigovsky-core/src/Permalinks/ServicePermalinks.php`

Docs: `PROJECT-STATUS.md`, this report, `WORDPRESS/architecture/FP-0002-PROD-P13-OWNERSHIP-NOTES-v1.md`, evidence pack.

Intake of CSS (`v9-style.css`, `fp02-specialist-profile.css`) was **MATCH** — no operator CSS canonize required. OPERATOR CURRENT PRODUCTION STATE PRESERVED.

## 10. Exact DB QA Objects

All force-deleted after QA. No public QA leftovers.

| ID | Type | Purpose |
|----|------|---------|
| 2015 | service draft | persist / clear |
| 2019 | specialist draft | persist / clear |
| 2020–2022 | service drafts | collision |
| 2023–2024 | specialist drafts | collision |
| 2028 | service draft | HTTP native Update |
| 2029 | specialist draft | HTTP native Update |

Activity log rows titled `FP02 FU01 QA%`: 9 deleted.

## 11. Source / Production Parity

**2/2 SOURCE ↔ PRODUCTION MATCH**

See `EXACT-FILE-HASHES.md`. Rollback: `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p13-fu01-layer-b-pre\`.

## 12. Regression

PASS: home, `/uslugi/`, `/uslugi/zavisimosti/` + child hierarchy, `/specyalisty/`, `/specyalisty/kostyuk/`, sitemap, Smart Search markers, Service SEO metabox, no duplicate Admin permalink UI. Unrelated P13 features not deployed.

## 13. WPilot

`write_enabled=false`  
Business writes: **0**

## 14. Git

- Commit: none
- Push: none
- Foreign WIP: untouched (existing staged client-ops index left as-is; no `git add` / reset / stash)

## 15. Acceptance

`PROD-P13-FU01 NATIVE SLUG UX TECHNICAL CLOSEOUT COMPLETE — OPERATOR VISUAL ACCEPTANCE PENDING`

Desired state:

FP-0002 PROD-P13-FU01 COMPLETE — CUSTOM PUBLIC ENTITIES USE ONE NATIVE WORDPRESS PERMALINK EDITOR — NO DUPLICATE URL UI — MANUAL SLUG EDIT PERSISTS AFTER UPDATE/RELOAD — CLEAR REGENERATES SAFELY — COLLISIONS REMAIN UNIQUE — EXISTING PRODUCTION URLS UNCHANGED — SOURCE/PRODUCTION PARITY MAINTAINED
