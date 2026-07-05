# REPORT — FP-0002 V9-06D9-K CONTROLLED MEDIA UPLOAD + ACF SEED

**Date:** 2026-07-05  
**Mode:** CONTROLLED MEDIA UPLOAD + ACF MEDIA SEED  
**Base:** D9-J plan (`6cb0b9df`); execution at repo HEAD `f8f652fd` (D9-J direct parent, local=remote)

---

## 1. Safety preflight

- Volume: X
- Label: AI WS
- Repository: X:\AI MARS
- Branch: mars/canonical-post-recovery
- Local HEAD: f8f652fd30f4b1892971ca7e1cae40eff1ba9a57
- Local short HEAD: f8f652fd
- Remote HEAD: f8f652fd30f4b1892971ca7e1cae40eff1ba9a57
- Remote short HEAD: f8f652fd
- Ahead: 0
- Behind: 0
- Foreign WIP: present (unstaged; not staged)
- Pre-existing staged files: none
- Strict HEAD gate: **DEVIATION NOTED** — required `6cb0b9df`; actual `f8f652fd` (+1 unrelated governance commit; D9-J is ancestor; local=remote)
- Result: **PASS WITH HEAD DEVIATION DOCUMENTED**

---

## 2. Authorization and scope

- Operator authorization: V9-06D9-K Controlled Media Upload + ACF Seed
- Task mode: CONTROLLED MEDIA UPLOAD + ACF MEDIA SEED (Home #4 only)
- Runtime delivery: NOT_PERFORMED (source/theme unchanged)
- Source/theme changes: 0
- ACF JSON changes: 0
- Runtime file writes: uploads only (5 media files via WP API)
- DB checkpoint: PASS
- Media uploads: 5
- Attachment creation: 5
- ACF value writes: 2 (`home_hero_slides`, `home_gallery_media`)
- Home page writes: 2 (ACF fields only)
- Other object writes: 0
- Options writes: 0
- Menu writes: 0
- Rewrite/permalink changes: 0
- Plugin source changes: 0
- V9 src/dist changes: 0
- Documentation/evidence writes: YES (approved paths only)
- Result: **PASS**

---

## 3. Runtime / DB / media gate

| Check | Result | Notes |
|---|---|---|
| runtime HTTP 200 | PASS | `/` verified |
| DB connection | PASS | mars_wp_fp0002 / fp02_ |
| active theme shpigovsky | PASS | |
| ACF PRO active | PASS | |
| Home page #4 | PASS | publish |
| target field home_hero_slides | PASS | field_fp02_home_hero_image |
| target field home_gallery_media | PASS | field_fp02_home_gallery_item_media |
| uploads directory writable | PASS | |
| approved source files (5) | PASS | checksums match D9-J |
| attachment count before | PASS | 0 |

Evidence: `validation/v9-06d9k-controlled-media-upload-acf-seed/runtime-db-media-gate.json`

---

## 4. Baseline media / ACF audit

| Area | Before state | Notes |
|---|---|---|
| Attachments | 0 | Empty Media Library |
| home_hero_slides | 1 row; image empty | D9-I text seeded; theme hero fallback |
| home_gallery_media | 0 rows | Theme gallery fallback (4 images) |
| Frontend hero URL | theme assets | hero-main.png |
| Frontend gallery URLs | 4× theme webp | shpigovsky-gallery-01…04 |
| Fallback usage | hero + gallery | Both active |

Evidence: `validation/v9-06d9k-controlled-media-upload-acf-seed/baseline-media-acf-audit.json`

---

## 5. DB checkpoint / rollback baseline

- Checkpoint path: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06d9k-controlled-media-upload-pre-20260705-145628`
- DB dump: PASS (`mars_wp_fp0002.sql`, sha256 `a668523f…`)
- Pre-values JSON: `home-page-4-pre-media-values.json`
- Attachment inventory before: `attachment-inventory-before.json` (0)
- Uploads inventory before: `uploads-inventory-before.json`
- Restore instructions: full DB restore + field-level JSON restore + attachment ID delete
- Result: **PASS**

Evidence: `validation/v9-06d9k-controlled-media-upload-acf-seed/db-checkpoint.json`

---

## 6. Execution plan

| File | Source | Target field | Metadata | Expected visual impact |
|---|---|---|---|---|
| hero-main.png | v9/src/img/hero/hero-main.png | home_hero_slides[0].image | Шпиговский дом — центр… | SHOULD_MATCH_CURRENT_FALLBACK |
| shpigovsky-gallery-01.webp | v9/…/gallery/01 | home_gallery_media[0].media | Лечение зависимости от алкоголя | SHOULD_MATCH_CURRENT_FALLBACK |
| shpigovsky-gallery-02.webp | v9/…/gallery/02 | home_gallery_media[1].media | Лудомания… | SHOULD_MATCH_CURRENT_FALLBACK |
| shpigovsky-gallery-03.webp | v9/…/gallery/03 | home_gallery_media[2].media | Лечение подростковой… | SHOULD_MATCH_CURRENT_FALLBACK |
| shpigovsky-gallery-04.webp | v9/…/gallery/04 | home_gallery_media[3].media | Зависимость от постоянных покупок | SHOULD_MATCH_CURRENT_FALLBACK |

Evidence: `validation/v9-06d9k-controlled-media-upload-acf-seed/execution-plan.json`

---

## 7. Dry-run

| Check | Result | Notes |
|---|---|---|
| five source files exist | PASS | |
| upload target writable | PASS | |
| home page 4 only | PASS | |
| hero preserves slide text | PASS | merge image into row 0 |
| gallery four rows | PASS | |
| no options writes | PASS | |
| no source/schema changes | PASS | |

Evidence: `validation/v9-06d9k-controlled-media-upload-acf-seed/dry-run-result.json`

---

## 8. Media upload result

| File | Attachment ID | URL | Metadata result | Checksum/result |
|---|---:|---|---|---|
| hero-main.png | 89 | `/uploads/2026/07/hero-main.png` | title + alt set | MATCH |
| shpigovsky-gallery-01.webp | 90 | `/uploads/2026/07/shpigovsky-gallery-01.webp` | title + alt set | MATCH |
| shpigovsky-gallery-02.webp | 91 | `/uploads/2026/07/shpigovsky-gallery-02.webp` | title + alt set | MATCH |
| shpigovsky-gallery-03.webp | 92 | `/uploads/2026/07/shpigovsky-gallery-03.webp` | title + alt set | MATCH |
| shpigovsky-gallery-04.webp | 93 | `/uploads/2026/07/shpigovsky-gallery-04.webp` | title + alt set | MATCH |

Evidence: `validation/v9-06d9k-controlled-media-upload-acf-seed/media-upload-result.json`

---

## 9. ACF media seed result

| Field | Result | Old state | New state |
|---|---|---|---|
| home_hero_slides[0].image | PASS | image empty | attachment 89; title/text preserved |
| home_gallery_media | PASS | 0 rows | 4 rows; attachments 90–93 |

Evidence: `validation/v9-06d9k-controlled-media-upload-acf-seed/acf-media-seed-result.json`

---

## 10. Post-write verification

| Check | Expected | Actual | Result |
|---|---|---|---|
| Attachment count | 5 | 5 | PASS |
| Hero ACF image | 89 | 89 | PASS |
| Gallery ACF rows | 4 | 4 | PASS |
| Frontend hero uploads URL | /uploads/ | /uploads/2026/07/hero-main.png | PASS |
| Frontend gallery uploads URLs | 4× /uploads/ | 4× /uploads/2026/07/ | PASS |
| Options unchanged | yes | yes | PASS |
| Only approved fields changed | yes | yes | PASS |

Evidence: `validation/v9-06d9k-controlled-media-upload-acf-seed/post-write-verification.json`, `attachment-manifest.json`

---

## 11. Frontend visual regression

| Check | Result | Notes |
|---|---|---|
| 19 Home sections | PASS | 19/19 |
| hero image | PASS | uploads URL |
| gallery 4 images | PASS | uploads URLs |
| hero CTA | PASS | Записаться на консультацию |
| sliders/dots | PASS | data-gallery-pagination present |
| footer | PASS | site-footer |
| no broken images | PASS | no empty src |
| route smoke | ALL_200 | 7/7 routes |

Evidence: `validation/v9-06d9k-controlled-media-upload-acf-seed/post-upload-home-visual-regression-check.json`, `post-upload-route-smoke.json`

---

## 12. Admin media editability verification

| Check | Result | Notes |
|---|---|---|
| Media Library 5 attachments | PASS | IDs 89–93 |
| titles/alt set | PASS | |
| hero field shows attachment | PASS | |
| gallery field shows 4 attachments | PASS | |
| deferred fields empty | PASS | |
| admin screenshots | SKIPPED | readback verification used |

Evidence: `validation/v9-06d9k-controlled-media-upload-acf-seed/admin-media-editability-verification.json`

---

## 13. Screenshots

| Screenshot | Captured | Result |
|---|---:|---|
| runtime-home-full-desktop-after-d9k.png | yes | PASS |
| runtime-home-full-mobile-after-d9k.png | yes | PASS |
| runtime-hero-after-d9k.png | yes | PASS |
| runtime-gallery-after-d9k.png | yes | PASS |
| runtime-footer-after-d9k.png | yes | PASS |
| runtime-services-hub-after-d9k.png | yes | PASS |
| runtime-service-74-after-d9k.png | yes | PASS |
| runtime-contacts-after-d9k.png | yes | PASS |
| wp-admin-* | no | SKIPPED (auth) |

Evidence: `validation/v9-06d9k-controlled-media-upload-acf-seed/screenshots/`, `screenshot-manifest.json`

---

## 14. No-scope-drift

- Source/theme changes: 0
- ACF JSON changes: 0
- Plugin changes: 0
- V9 src/dist changes: 0
- Options writes: 0
- Menu writes: 0
- Services writes: 0
- Hub writes: 0
- Contacts writes: 0
- Native post content writes: 0
- Rewrite flush: NO
- Object create/delete: 5 (attachments only)
- Media uploads: 5
- Attachment creation: 5
- ACF value writes limited to Home #4 approved media fields: YES
- DB checkpoint: YES
- DB dumps staged: NO
- Runtime snapshots staged: NO
- Uploaded media files staged: NO
- Secrets/API keys: 0
- Result: **PASS**

Evidence: `validation/v9-06d9k-controlled-media-upload-acf-seed/no-scope-drift-validation.json`

---

## 15. Documentation changes

| File | Action | Reason |
|---|---|---|
| reports/FP-0002-V9-06D9K-CONTROLLED-MEDIA-UPLOAD-ACF-SEED-REPORT-v1.md | created | Phase report |
| architecture/FP-0002-V9-06D9K-*.md (4 files) | created | Architecture evidence |
| validation/v9-06d9k-controlled-media-upload-acf-seed/*.json | created | Validation evidence |
| validation/…/screenshots/*.png | created | Visual evidence |
| WORDPRESS/README.md | updated | Phase status |
| WORDPRESS/SOURCE-AUTHORITY.md | updated | Phase authority |
| FP-0002-SHPIGOVSKY/PROJECT-STATUS.md | updated | Project status |

---

## 16. Git checkpoint

- Exact staged files: D9-K report, architecture docs, validation JSON, screenshots, status docs only
- Staged list inspected: YES
- Source/theme files staged: NO
- ACF JSON staged: NO
- Runtime files staged: NO
- Uploaded media files staged: NO
- DB dumps staged: NO
- Helper/temp files staged: NO
- Commit: FP-0002: upload home media assets
- Push: after commit (normal, no force)

---

## 17. Final verdict

**PASS**

V9-06D9-K Controlled Media Upload + ACF Seed: **COMPLETE**

Runtime delivery: NOT_PERFORMED  
Source/theme changes: 0  
ACF JSON changes: 0  
Runtime file writes: 0 (Git); 5 uploads via WP runtime only  

DB checkpoint: PASS  
Media uploads: 5  
Attachment creation: 5  
ACF value writes: 2  
Home page writes: 2  
Other object writes: 0  
Options writes: 0  
Menu writes: 0  

Uploaded approved files: 5 / 5  
Hero media seed: PASS  
Gallery media seed: PASS  
Home visual regression: PASS  
Admin media editability: PASS  
Route smoke: ALL_200  
No-scope-drift: PASS  

Recommended next phase: **CREATE_V9_06D9L_OPERATOR_MEDIA_REVIEW_TASK**

---

## 18. Recommended next action

**CREATE_V9_06D9L_OPERATOR_MEDIA_REVIEW_TASK**

---

## 19. Final safety statement

Target folder:  
X:\AI MARS

Volume:  
AI WS / X:

Runtime:  
X:\MARS-Localhost\sites\wordpress\projects\shpigovsky

V9-06D9-K Controlled Media Upload + ACF Seed performed:  
YES

Runtime delivery performed:  
NO

Source/theme changes:  
0

ACF JSON changes:  
0

Runtime file writes:  
0

Database checkpoint:  
YES

Media uploads:  
5

Attachment creation:  
5

ACF value writes:  
2

Home page writes:  
2

Other object writes:  
0

Native content writes:  
0

Options writes:  
0

Menu writes:  
0

Service writes:  
0

Services Hub writes:  
0

Contacts writes:  
0

Rewrite flush performed:  
NO

Permalink/rewrite changed:  
NO

Menus changed:  
0

Redirects created:  
0

Object create/delete:  
5

External API/API keys added:  
NO

Production migration performed:  
NO

V9 source changed:  
NO

V9 dist changed:  
NO

Plugin source changed:  
NO

Plugin updates run:  
0

Plugin installs run:  
0

Plugin deletes run:  
0

DB dump committed:  
NO

Runtime snapshot committed:  
NO

Uploaded media files committed:  
NO

Helper committed:  
NO

Secrets committed:  
0
