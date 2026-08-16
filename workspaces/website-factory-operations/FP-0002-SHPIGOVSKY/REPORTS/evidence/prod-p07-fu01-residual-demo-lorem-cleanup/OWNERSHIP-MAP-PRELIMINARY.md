# PROD-P07-FU01 — Preliminary Ownership Map (read-only)

**Status:** PRELIMINARY — mutations blocked by backup gate  
**Date:** 2026-08-14  
**Sources:** live public HTML, local canonical theme source, P07 probe `prod-readonly-db-fs-probe.json`

---

## A. `/uslugi/` hub short descriptions

### Frontend surface

* Template class: `.services-category-section-v2__service-text`
* Live 2026-08-14: **no visible `DEMO —` prefix**
* Live residual in the same card-description slot: **`Lorem ipsum…`** (multiple category child cards)
* Charter class A covers `DEMO —` **or equivalent** technical/demo text in hub short descriptions → live Lorem in this slot is in-scope equivalent residue

### Resolution chain (source)

Owner helper: `shpigovsky_get_service_mini_description()` in `WORDPRESS/theme/shpigovsky/inc/services-hub-helpers.php`

Priority:

1. ACF / post meta `service_short_description` (Admin SoT when non-empty)
2. V9 static map `shpigovsky_get_v9_services_hub_child_copy( $slug )` in `inc/v9-static-content.php`
3. PHP DEMO fallback `shpigovsky_get_service_demo_mini_description_fallback()` (hardcoded `DEMO — …`)

### Live classification (FE)

| Observation | Likely owner |
|-------------|--------------|
| Visible Lorem in hub child cards | V9 static `$demo_lorem` entries for several child slugs (e.g. `depressiya`, `ptrs`, eating-disorder leaves) **or** empty ACF causing that V9 path |
| No visible `DEMO —` on hub now | Either DEMO ACF rows are not currently rendered in hub category lists, or not winning over V9/real text for visible cards |
| Historical P07 DB probe | Many posts (`#1047+#` etc.) still recorded `service_short_description = DEMO — краткое описание…` and/or `content_source=demo_placeholder` — **DB reconfirm required after backup gate** before mutation |

### Planned action classes (after gate; not executed)

| Case | Action |
|------|--------|
| ACF = `DEMO — <real>` | Strip prefix only |
| ACF = entire demo filler | Clear / hide if template allows; do not invent |
| Visible Lorem from V9 static map | Disable/replace technical fallback with empty/omit or existing real copy; no invented clinical text |
| PHP DEMO fallback emits residue | Change fallback to empty/omit only if proven owner |

---

## B. Alcohol leaf FAQ / signs Lorem

**Route:** `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/`  
**Known object:** service `#74` (P07 deferred note)

### Live FE residues

| Section / class | Placeholder type |
|-----------------|------------------|
| `.service-leaf-signs-v1__editorial` | Lorem ipsum editorial paragraph |
| Program chrome `.services-program-v2__lead` / `__intro` | Lorem ipsum |
| FAQ accordion answers (alcohol leaf FAQ) | Lorem / temporary technical answers in static FAQ map |

### Owners (source)

| Block | Admin/ACF candidate | Fallback owner when empty |
|-------|---------------------|---------------------------|
| Signs | `service_general_signs_*` via `shpigovsky_get_general_signs_copy()` | `shpigovsky_get_v9_alcohol_signs_copy()` — **editorial is Lorem**; items/intro are real RU |
| FAQ | `service_general_faq_items` via `shpigovsky_get_general_faq_items()` | `shpigovsky_get_v9_alcohol_leaf_faq_items()` — **answers include Lorem / temporary technical text** |
| Program demo chrome | general/section program fields | `shpigovsky_get_v9_alcohol_leaf_program_demo_copy()` — **all Lorem** |

### Planned action classes (after gate; not executed)

1. Prefer real Admin-owned content if present  
2. Else omit placeholder row / hide optional empty section  
3. Fix PHP emergency Lorem fallbacks to omit rather than invent clinical copy  
4. Do **not** fabricate medical statements

---

## C. Explicitly out of scope (observed but not FU01 mutation targets)

* Home blog URLs containing `demo-pagination-article-*` (slug/path, not hub short-desc)
* Broader `.test` URLs, `blogname`, `WP_DEBUG`, `WP_ENVIRONMENT_TYPE`, `home`/`siteurl`, HTTPS, DNS
* Accepted P07 UX/Admin architecture (cards, Guest Visit CTA, approach parity, reusable blocks, Generic Content)

---

## D. Mutation status

**None.** Backup gate blocked DB/file writes. This map is preparatory only.
