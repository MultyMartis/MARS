# REPORT — FP-0002 V9-06D9-J MEDIA SELECTION / UPLOAD PLAN

**Date:** 2026-07-05  
**Mode:** READ_ONLY + PLANNING ONLY  
**Base HEAD:** `3d34449a315e060bbb2ad328ba4a71810b785c6b` (D9-I)

---

## 1. Safety preflight

- Volume: X
- Label: AI WS
- Repository: X:\AI MARS
- Branch: mars/canonical-post-recovery
- Local HEAD: 3d34449a315e060bbb2ad328ba4a71810b785c6b
- Local short HEAD: 3d34449a
- Remote HEAD: 3d34449a315e060bbb2ad328ba4a71810b785c6b
- Remote short HEAD: 3d34449a
- Ahead: 0
- Behind: 0
- Foreign WIP: present (unstaged; not staged)
- Pre-existing staged files: none
- Strict HEAD gate: PASS
- Result: PASS

---

## 2. Authorization and scope

- Operator authorization: V9-06D9-J Media Selection / Upload Plan
- Task mode: READ_ONLY MEDIA INVENTORY + UPLOAD PLAN ONLY
- Runtime delivery: NOT_PERFORMED
- Source/theme changes: 0
- ACF JSON changes: 0
- Runtime file writes: 0
- DB writes: 0
- ACF value writes: 0
- Media uploads: 0
- Attachment creation: 0
- Options writes: 0
- Menu writes: 0
- Rewrite/permalink changes: 0
- Plugin source changes: 0
- V9 src/dist changes: 0
- Documentation/evidence writes: YES (approved paths only)
- Result: PASS

---

## 3. Runtime / media read-only gate

| Check | Result | Notes |
|---|---|---|
| runtime HTTP 200 | PASS | `/` verified |
| DB connection | PASS | mars_wp_fp0002 via wp-load.php |
| home page #4 | PASS | publish |
| ACF PRO active | PASS | get_field available |
| D9-H field group | PASS | group_fp02_page_home |
| D9-I seeded fields readable | PASS | home_recovery_intro_heading populated |
| uploads directory | PASS | wp-content/uploads exists |
| attachment inventory | PASS | 0 attachments |
| frontend inspectable | PASS | route smoke + DOM checks |

Evidence: `validation/v9-06d9j-media-selection-upload-plan/runtime-media-readonly-gate.json`

---

## 4. Static V9 media inventory

| Section | Static/source asset | Theme fallback | Runtime current | Classification |
|---|---|---|---|---|
| hero | v9/src/img/hero/hero-main.png | assets/img/hero/hero-main.png | theme URL active | UPLOAD_AND_SEED_D9K |
| gallery ×4 | v9/src/img/content/gallery/shpigovsky-gallery-0N.webp | theme gallery webp | theme URL active | UPLOAD_AND_SEED_D9K |
| founder-quote | founder-sergey-shpigovsky.png | theme content | theme URL | OPERATOR_REVIEW_REQUIRED |
| specialists ×4 | home-specialists/*.webp | theme content | theme URL | OPERATOR_REVIEW_REQUIRED |
| comfort ×6+logo | home-comfort/*.webp | theme content | theme URL | KEEP_THEME_FALLBACK |
| clinic/staff/pre-reviews | pre-reviews/*.webp | theme content | theme URL | KEEP_THEME_FALLBACK |
| rehabilitation-program ×4 | program-*.webp | theme content | theme URL | KEEP_THEME_FALLBACK |
| articles ×3 | home-articles/*.webp | theme content | theme URL | KEEP_THEME_FALLBACK |
| videos | posters + mp4 | theme assets | theme URL | DEFER (mp4) / KEEP (posters) |
| footer/logo/social | logo.svg, social SVGs | theme branding | theme URL | DO_NOT_UPLOAD_VENDOR_OR_ICON |
| ui icons | external-link.svg | theme svg | theme URL | DO_NOT_UPLOAD_VENDOR_OR_ICON |

Full JSON: 40 assets — `static-v9-media-inventory.json`  
Architecture: `architecture/FP-0002-V9-06D9J-STATIC-V9-MEDIA-INVENTORY-v1.md`

---

## 5. Current WP Media Library inventory

| Attachment | File | Matches static/theme asset | Candidate use | Notes |
|---|---|---|---|---|
| — | — | — | — | **attachment_count: 0** |

Uploads directory exists; no media library entries. All Home imagery from theme fallbacks.

Evidence: `current-wp-media-library-inventory.json`

---

## 6. ACF media field gap analysis

| Field | Current value | Fallback used | Upload needed | Seed needed | Risk |
|---|---|---|---|---|---|
| home_hero_slides.image | empty (text row present) | hero-main.png | YES | YES | MEDIUM |
| home_gallery_media | empty repeater | 4 gallery webp fallbacks | YES | YES | MEDIUM |
| home_reviews_teaser | empty | static review cards | NO | OPERATOR_DECISION | HIGH |

Evidence: `acf-media-field-gap-analysis.json`, `home-page-media-acf-snapshot.json`

---

## 7. Media classification

| Asset | Section | Classification | Reason |
|---|---|---|---|
| hero-main.png | hero | UPLOAD_AND_SEED_D9K | ACF image subfield wired, empty |
| shpigovsky-gallery-01..04.webp | gallery | UPLOAD_AND_SEED_D9K | home_gallery_media repeater empty |
| founder + 4 specialist photos | people | OPERATOR_REVIEW_REQUIRED | Portrait/licensing sensitivity |
| comfort/program/articles/etc. | sections | KEEP_THEME_FALLBACK | No ACF media field yet |
| logo, social, external-link SVG | chrome | DO_NOT_UPLOAD_VENDOR_OR_ICON | Stable theme chrome |
| interview/center.mp4 | videos | DEFER_UNTIL_CONTENT_REVIEW | Video hosting separate wave |

Summary counts: UPLOAD_AND_SEED_D9K=5, KEEP_THEME_FALLBACK=21, OPERATOR_REVIEW_REQUIRED=5, DO_NOT_UPLOAD=7, DEFER=2

---

## 8. D9-K media upload/seed plan

| Phase | Action | Target | Safety requirement | Result |
|---|---|---|---|---|
| K1 | DB checkpoint + dry-run manifest | mars_wp_fp0002 | mysqldump + pre-values JSON | PLANNED |
| K2 | Upload 5 images | hero + 4 gallery | checksum manifest; no overwrite | PLANNED |
| K3 | Seed ACF media fields | page #4 | attachment IDs only; preserve hero text | PLANNED |
| K4 | Visual regression QA | Home `/` | vs D9-J screenshots | PLANNED |
| K5 | Admin media UX QA | page #4 edit | image pickers populated | PLANNED |

Evidence: `d9k-media-upload-seed-plan.json`

---

## 9. D9-K risk / rollback plan

| Risk | Prevention | Rollback |
|---|---|---|
| Wrong hero image | SHA256 verify V9 src | DB checkpoint restore |
| Gallery order drift | Seed order = fallback order | DB restore |
| Orphan attachments | Manifest all new IDs | Delete manifest IDs only (operator-approved) |
| ACF partial seed | Pre-values JSON | DB restore |

Evidence: `d9k-risk-rollback-plan.json`

---

## 10. Frontend current-state validation

| Check | Result | Notes |
|---|---|---|
| 19 Home sections | PASS | all IDs found |
| hero image present | PASS | theme fallback URL |
| gallery fallback | PASS | shpigovsky-gallery assets |
| broken images | PASS | 0 empty src |
| footer | PASS | site-footer present |
| routes smoke | PASS | `/`, `/uslugi/`, service-74, `/kontakty/` ALL 200 |
| PHP fatal | PASS | none detected |

Evidence: `current-frontend-media-validation.json`

---

## 11. Screenshots

| Screenshot | Captured | Result |
|---|---:|---|
| runtime-home-full-desktop-d9j-current.png | yes | PASS |
| runtime-home-full-mobile-d9j-current.png | yes | PASS |
| runtime-hero-media-d9j-current.png | yes | PASS |
| runtime-gallery-media-d9j-current.png | yes | PASS |
| runtime-comfort-media-d9j-current.png | yes | PASS |
| runtime-specialists-media-d9j-current.png | yes | PASS |
| runtime-footer-d9j-current.png | yes | PASS |
| runtime-service-74-d9j-current.png | yes | PASS |
| runtime-contacts-d9j-current.png | yes | PASS |
| wp-admin-media-library-d9j-current.png | no | SKIPPED (auth required) |
| wp-admin-home-media-fields-d9j-current.png | no | SKIPPED (auth required) |

Evidence: `screenshot-manifest.json`, `visual-result.json`, `screenshots/`

---

## 12. No-scope-drift

- DB writes: 0
- ACF value writes: 0
- Source/theme changes: 0
- ACF JSON changes: 0
- Runtime delivery: NOT_PERFORMED
- Runtime file writes: 0
- Media uploads: 0
- Attachment creation: 0
- Object create/delete: 0
- Options writes: 0
- Menu writes: 0
- Services writes: 0
- Hub writes: 0
- Contacts writes: 0
- Native post content writes: 0
- Rewrite flush: NO
- Plugin changes: 0
- V9 src/dist changes: 0
- DB dumps staged: 0
- Runtime snapshots staged: 0
- Secrets/API keys: 0
- Result: PASS

Evidence: `no-scope-drift-validation.json`

---

## 13. Documentation changes

| File | Action | Reason |
|---|---|---|
| reports/FP-0002-V9-06D9J-MEDIA-SELECTION-UPLOAD-PLAN-REPORT-v1.md | created | Task report |
| architecture/FP-0002-V9-06D9J-*.md (7 files) | created | Planning pack |
| validation/v9-06d9j-media-selection-upload-plan/*.json | created | Evidence |
| validation/.../screenshots/*.png | created | Baseline captures |
| WORDPRESS/README.md | updated | Phase pointer |
| WORDPRESS/SOURCE-AUTHORITY.md | updated | D9-J note |
| FP-0002-SHPIGOVSKY/PROJECT-STATUS.md | updated | Status |

---

## 14. Git checkpoint

- Exact staged files: D9-J report, architecture, validation JSON, screenshots, status docs only
- Staged list inspected: required before commit
- Source/theme files staged: NO
- ACF JSON staged: NO
- Runtime files staged: NO
- Uploads/media files staged: NO
- Helper scripts (_d9j_*.php/.py/.mjs): NOT STAGED
- Commit: pending operator push wave
- Result: pending

---

## 15. Final verdict

**PASS**

V9-06D9-J Media Selection / Upload Plan: **COMPLETE**

Runtime delivery: NOT_PERFORMED  
Source/theme changes: 0  
ACF JSON changes: 0  
Runtime file writes: 0  
DB writes: 0  
ACF value writes: 0  
Media uploads: 0  
Attachment creation: 0  

Static media inventory: PASS  
WP media library inventory: PASS  
ACF media gap analysis: PASS  
D9-K upload plan: PASS  
Frontend current-state validation: PASS  
No-scope-drift: PASS  

Recommended next phase: **D9-K Controlled Media Upload + ACF Seed**

---

## 16. Recommended next action

**CREATE_V9_06D9K_CONTROLLED_MEDIA_UPLOAD_AND_ACF_SEED_TASK**

---

## 17. Final safety statement

Target folder: X:\AI MARS  
Volume: AI WS / X:  
Runtime: X:\MARS-Localhost\sites\wordpress\projects\shpigovsky  

V9-06D9-J Media Selection / Upload Plan performed: **YES**  
Runtime delivery performed: **NO**  
Source/theme changes: **0**  
ACF JSON changes: **0**  
Runtime file writes: **0**  
Database writes: **0**  
ACF value writes: **0**  
Media uploads: **0**  
Attachment creation: **0**  
Object create/delete: **0**  
Native content writes: **0**  
Options writes: **0**  
Menu writes: **0**  
Service writes: **0**  
Services Hub writes: **0**  
Contacts writes: **0**  
Rewrite flush performed: **NO**  
Permalink/rewrite changed: **NO**  
Menus changed: **0**  
Redirects created: **0**  
External API/API keys added: **NO**  
Production migration performed: **NO**  
V9 source changed: **NO**  
V9 dist changed: **NO**  
Plugin source changed: **NO**  
Plugin updates run: **0**  
Plugin installs run: **0**  
Plugin deletes run: **0**  
DB dump committed: **NO**  
Runtime snapshot committed: **NO**  
Helper committed: **NO**  
Secrets committed: **0**
