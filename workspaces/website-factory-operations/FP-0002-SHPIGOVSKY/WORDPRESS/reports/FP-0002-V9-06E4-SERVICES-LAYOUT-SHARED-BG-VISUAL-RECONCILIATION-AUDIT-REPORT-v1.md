# REPORT — FP-0002 V9-06E4 SERVICES LAYOUT + SHARED BG VISUAL RECONCILIATION AUDIT

**Date:** 2026-07-06  
**Mode:** READ-ONLY VISUAL RECONCILIATION AUDIT  
**Baseline:** E3 @ `8c935957048c1f9b3d6ae1fee36ac3b5d2fcb222`  
**HEAD at audit:** `b545a1c3514bc88412c378e42ab69b3fcafa3d70`

---

## 1. Safety preflight

- Volume: X
- Label: AI WS
- Repository: X:\AI MARS
- Branch: mars/canonical-post-recovery
- Local HEAD: b545a1c3514bc88412c378e42ab69b3fcafa3d70
- Local short HEAD: b545a1c3
- Remote HEAD: b545a1c3514bc88412c378e42ab69b3fcafa3d70
- Remote short HEAD: b545a1c3
- Ahead: 0
- Behind: 0
- Foreign WIP: present (extensive unstaged M/??; not staged)
- Pre-existing staged files: none
- E3 ancestor check: YES (`8c935957` is ancestor of HEAD)
- Result: **PASS_WITH_HEAD_NOTE** (HEAD advanced past E3 commit; local/remote synced)

---

## 2. Authorization and scope

- Operator authorization: V9-06E4 Services Layout + Shared Background Visual Reconciliation Audit
- Task mode: READ-ONLY AUDIT
- DB writes: 0
- Source/theme changes: 0
- ACF JSON changes: 0
- Runtime delivery: NOT_PERFORMED
- ACF value writes: 0
- Native content writes: 0
- Media uploads: 0
- Options writes: 0
- Menu writes: 0
- Rewrite/permalink changes: 0
- Plugin install/update/delete: 0
- OCPilot writes: 0
- Documentation/evidence writes: YES (E4 scope only)
- Result: **PASS**

---

## 3. Runtime route visual audit

| Route | Runtime state | Operator finding | Result | Notes |
|---|---|---|---|---|
| `/uslugi/` | 200; page #5; `services-hub.php`; hero `hero--inner`; no hero image; main `page-uslugi` | Broken hero; Home hero design; missing image; main drift | **MISMATCH_CONFIRMED** | Template assigned correctly but hero partial wrong |
| `/uslugi/zavisimosti/` | 200; service #73; `services-inner-hero-v2`; no hero image; main matches static | Layout drift; correct hero type; missing image | **PARTIAL_MISMATCH** | `hero_media` ACF empty; stack incomplete vs static |

---

## 4. Static V9 route authority audit

| Route | Static source | Expected hero/main | Expected assets | Notes |
|---|---|---|---|---|
| `/uslugi/` | `src/pages/uslugi-v2.html` → `dist/uslugi/index.html` | `page-uslugi-v2__main`; `services-inner-hero-v2` | `services-hero.webp` | AUTHORITY_FOUND |
| `/uslugi/zavisimosti/` | `src/pages/usluga-podrazdel-v1.html` → `dist/uslugi/zavisimosti/index.html` | `page-service-subdivision-v1__main`; `services-inner-hero-v2` | `service-subdivision-hero.webp` | AUTHORITY_FOUND |

---

## 5. Services hub hero/main mismatch audit

| Check | Result | Notes |
|---|---|---|
| Template renders `/uslugi/` | PASS | `page-templates/services-hub.php` on page #5 |
| Why Home hero? | CONFIRMED | `template-parts/services-hub/hero.php` hardcodes `hero hero--inner` |
| ACF fallback cause? | NO | Not an ACF issue |
| Static hero type | `services-inner-hero-v2` | Per `uslugi-v2.html` |
| Hero asset in theme? | YES | `services-hero.webp` present; not referenced |
| Main wrapper drift? | CONFIRMED | `page-uslugi` vs `page-uslugi-v2__main` |
| Section stack drift? | CONFIRMED | `services-category-hub` vs `services-category-section-v2`; missing nav/founder/comfort |

---

## 6. Service subdivision layout/image audit

| Check | Result | Notes |
|---|---|---|
| Template | `subdivision-stack.php` | Correct variant routing |
| Hero type | PASS | `services-inner-hero-v2` |
| Hero image missing why? | ACF `hero_media` empty on #73 | Asset exists in theme |
| `service-subdivision-start-heading` | PRESENT | Via `program-cta-band-section` |
| Background on CTA band | MISSING visually | CSS `/assets/` 404 |
| Layout vs static | DRIFT | 7 sections vs 14 in static authority |

---

## 7. Shared background image blocks audit

| Block | Expected asset | Current runtime | Root cause | Notes |
|---|---|---|---|---|
| `final-form-heading` / `final-form__band` | home-final-form-background.webp | Markup OK; bg invisible | CSS_PATH | File in theme; CSS uses `/assets/...` |
| `service-subdivision-start-heading` | same | program-cta-band present | CSS_PATH | id `service-subdivision-start` |
| `home-rehabilitation-requirements__cta-band` | same | Used on home/stages | CSS_PATH | 4 root-absolute rules in v9-style.css |

---

## 8. Missing background asset inventory

| Asset | Static path | WP source path | Runtime path | Status | Notes |
|---|---|---|---|---|---|
| home-final-form-background.webp | dist/assets/... | theme/assets/... | runtime theme | PRESENT; CSS 404 | SHA256 match git=runtime=dist |
| services-hero.webp | dist/assets/... | theme/assets/... | runtime theme | PRESENT_NOT_WIRED | Hub hero omits img |
| service-subdivision-hero.webp | dist/assets/... | theme/assets/... | runtime theme | PRESENT_ACF_EMPTY | #73 hero_media unset |

---

## 9. Reconciliation matrix

| Issue | Static expected | WP current | Root cause | Proposed E5 repair |
|---|---|---|---|---|
| Hub hero type | services-inner-hero-v2 | hero--inner | TEMPLATE_WRAPPER | Replace services-hub/hero.php |
| Hub main layout | page-uslugi-v2 stack | simplified hub | TEMPLATE_WRAPPER | Align partials + classes |
| Hub hero image | services-hero.webp | none | TEMPLATE_WRAPPER | Wire theme default image |
| Subdivision hero image | service-subdivision-hero.webp | none | ACF/fallback | Fallback or seed hero_media |
| Subdivision layout | 14-section stack | 7-section stack | TEMPLATE_WRAPPER | Extend subdivision-stack |
| Shared backgrounds | visible ::before | 404 URL | CSS_PATH | Fix v9-style.css url() paths |

---

## 10. Future E5 repair plan

| Component | Planned repair | Safety |
|---|---|---|
| CSS backgrounds | Theme-relative urls in v9-style.css | Low risk; no DB |
| Services hub hero | services-inner-hero-v2 + image | Template delivery |
| Services hub layout | section-v2 + program-v2 + missing sections | Route-scoped smoke |
| Subdivision hero | Theme fallback or ACF seed | Optional DB |
| Subdivision stack | Add missing V9 sections | Incremental partials |
| Validation | Screenshot + route smoke | Read-only gate |

---

## 11. Screenshots

| Screenshot | Captured | Result |
|---|---:|---|
| runtime-uslugi-current-e4.png | YES | PASS |
| runtime-zavisimosti-current-e4.png | YES | PASS |
| static-v9-uslugi-reference-e4.png | YES | PASS |
| static-v9-zavisimosti-reference-e4.png | YES | PASS |

Path: `validation/v9-06e4-services-layout-shared-bg-visual-reconciliation-audit/screenshots/`

---

## 12. No-scope-drift

- DB writes: 0
- Source/theme changes: 0
- ACF JSON changes: 0
- ACF value writes: 0
- Native content writes: 0
- Media uploads: 0
- Options writes: 0
- Menu writes: 0
- Runtime delivery: NOT_PERFORMED
- Rewrite flush: NO
- Plugin install/update/delete: 0
- OCPilot writes: 0
- DB dumps staged: NO
- Runtime snapshots staged: NO
- Secrets/API keys: 0
- Result: **PASS**

---

## 13. Documentation changes

| File | Action | Reason |
|---|---|---|
| reports/FP-0002-V9-06E4-...-REPORT-v1.md | CREATE | E4 main report |
| architecture/FP-0002-V9-06E4-*.md (9 files) | CREATE | E4 audit pack |
| validation/v9-06e4-.../ (11 JSON + 4 PNG) | CREATE | E4 evidence |
| WORDPRESS/README.md | UPDATE | E4 status |
| WORDPRESS/SOURCE-AUTHORITY.md | UPDATE | E4 audit note |
| PROJECT-STATUS.md | UPDATE | E4 completion |

---

## 14. Git checkpoint

*(Completed after staging — see commit record)*

---

## 15. Final verdict

**PASS**

V9-06E4 Services Layout + Shared BG Visual Reconciliation Audit: **COMPLETE**

/services hub hero: **MISMATCH_CONFIRMED**

/services hub main layout: **MISMATCH_CONFIRMED**

/zavisimosti layout: **MISMATCH_CONFIRMED**

/zavisimosti hero image: **MISSING_CONFIRMED**

Shared background images: **MISSING_CONFIRMED**

Asset inventory: **COMPLETE**

E5 repair readiness: **READY**

No-scope-drift: **PASS**

Recommended next phase: **CREATE_V9_06E5_SERVICES_LAYOUT_SHARED_BG_REPAIR_TASK**

---

## 16. Recommended next action

**CREATE_V9_06E5_SERVICES_LAYOUT_SHARED_BG_REPAIR_TASK**

---

## 17. Final safety statement

Target folder: X:\AI MARS

V9-06E4 Services Layout + Shared BG Visual Reconciliation Audit performed: **YES**

DB writes: 0

Source/theme changes: 0

ACF JSON changes: 0

Runtime delivery: NO

ACF value writes: 0

Native content writes: 0

Media uploads: 0

Options writes: 0

Menu writes: 0

Rewrite flush performed: NO

OCPilot writes: 0

Production migration performed: NO

V9 source changed: NO

V9 dist changed: NO

DB dump committed: NO

Runtime snapshot committed: NO

Helper committed: NO

Secrets committed: 0
