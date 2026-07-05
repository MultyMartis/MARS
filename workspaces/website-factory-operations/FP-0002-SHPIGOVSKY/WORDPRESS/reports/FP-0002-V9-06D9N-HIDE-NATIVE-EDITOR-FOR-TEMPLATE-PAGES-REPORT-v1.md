# REPORT — FP-0002 V9-06D9-N HIDE NATIVE EDITOR FOR TEMPLATE-MANAGED PAGES

**Date:** 2026-07-05  
**Base HEAD:** 367c41945c30e98f4719bca06c4e8eb3a4f51df6 (D9-M)

---

## 1. Safety preflight

- Volume: X
- Label: AI WS
- Repository: X:\AI MARS
- Branch: mars/canonical-post-recovery
- Local HEAD: 367c41945c30e98f4719bca06c4e8eb3a4f51df6
- Local short HEAD: 367c4194
- Remote HEAD: 367c41945c30e98f4719bca06c4e8eb3a4f51df6
- Remote short HEAD: 367c4194
- Ahead: 0
- Behind: 0
- Foreign WIP: present (unstaged; not staged)
- Pre-existing staged files: none
- Strict HEAD gate: PASS
- Result: **PASS**

---

## 2. Authorization and scope

- Operator authorization: V9-06D9-N Hide Native Editor for Template-Managed Pages
- Task mode: ADMIN UX REPAIR — code-based allowlist policy
- DB writes: 0
- Source/theme changes: 2 files (admin-editor.php created; functions.php require added)
- Runtime delivery: bounded copy of 2 theme files
- ACF JSON changes: 0
- ACF value writes: 0
- Native post_content writes: 0
- Media uploads: 0
- Attachment creation: 0
- Options writes: 0
- Menu writes: 0
- Rewrite/permalink changes: 0
- Plugin install/update/delete: 0
- V9 src/dist changes: 0
- Documentation/evidence writes: YES (approved paths)
- Result: **PASS**

---

## 3. Baseline admin UX audit

| Page ID | Title | Template-managed | Native editor before | ACF visible before | Recommended action |
|---:|---|---|---|---|---|
| 4 | Главная | YES | YES | YES | HIDE_NATIVE_EDITOR |
| 5 | Услуги | YES | YES | YES | HIDE_NATIVE_EDITOR |
| 20 | Контакты | YES | YES | YES | HIDE_NATIVE_EDITOR |
| 11 | О центре | YES | YES | N/A | HIDE_NATIVE_EDITOR |
| 6 | Зависимости | NO | YES | N/A | OPERATOR_REVIEW_REQUIRED |
| 3 | Политика конфиденциальности | YES | YES | N/A | OPERATOR_REVIEW_REQUIRED |

Evidence: `validation/v9-06d9n-hide-native-editor-template-pages/baseline-admin-ux-audit.json`

---

## 4. Implementation plan

| Item | Decision | Reason |
|---|---|---|
| Pattern | Allowlist metabox removal + admin_init editor support removal | Non-template/legal pages need native editor |
| Location | `theme/shpigovsky/inc/admin-editor.php` | Matches project theme admin hook convention |
| Allowlist | 13 D9-M cleaned page IDs | Documented in helper constant |
| Retain editor | IDs 3, 6–10, 17, 19, 21, 25 | Operator-review / legal content |
| Global removal | NO | Would hide editor on privacy policy #3 |
| DB writes | NO | Code-only admin UX |
| ACF visibility | Preserve all metaboxes | Task requirement |

Evidence: `validation/v9-06d9n-hide-native-editor-template-pages/implementation-plan.json`

---

## 5. Source implementation

| File | Change | Result |
|---|---|---|
| `theme/shpigovsky/inc/admin-editor.php` | Created allowlist admin UX helper | PASS |
| `theme/shpigovsky/functions.php` | Added `require_once` for admin-editor.php | PASS |

Evidence: `validation/v9-06d9n-hide-native-editor-template-pages/source-implementation-result.json`

---

## 6. Runtime delivery

- Delivery mode: bounded_file_copy
- Runtime target: `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky\wp-content\themes\shpigovsky\`
- Files copied: `inc/admin-editor.php`, `functions.php`
- Deletes: 0
- Mirror/purge: NO
- Checksum/source-target verification: SHA256 match on both files
- Result: **PASS**

Evidence: `validation/v9-06d9n-hide-native-editor-template-pages/runtime-delivery-plan.json`, `runtime-delivery-result.json`

---

## 7. Post-implementation admin validation

| Page ID | Title | Native editor after | ACF visible after | Result | Notes |
|---:|---|---|---|---|---|
| 4 | Главная | hidden | YES | PASS | hide policy active; ACF group registered |
| 5 | Услуги | hidden | N/A | PASS | hide policy active |
| 20 | Контакты | hidden | N/A | PASS | hide policy active |
| 3 | Политика конфиденциальности | visible | N/A | PASS | 20k legal content retained |
| 6 | Зависимости | visible | N/A | PASS | operator-review page |
| 11 | О центре | hidden | N/A | PASS | D9-M cleaned institutional |

Classic Editor active; Gutenberg disabled; Home ACF values intact (hero #89, gallery 4 rows).

Evidence: `validation/v9-06d9n-hide-native-editor-template-pages/post-implementation-admin-validation.json`

---

## 8. Frontend regression validation

| Check | Result | Notes |
|---|---|---|
| Route smoke (7 routes) | PASS | ALL_200 |
| Home 19 sections | PASS | 19/19 |
| Hero/gallery uploads | PASS | `/uploads/` URLs |
| CTA | PASS | «Записаться на консультацию» |
| FAQ heading | PASS | «Нас часто спрашивают» |
| Specialists heading | PASS | «Специалисты центра» |
| Footer | PASS | site-footer present |
| Admin-only code frontend impact | PASS | no regression |

Evidence: `validation/v9-06d9n-hide-native-editor-template-pages/frontend-regression-validation.json`

---

## 9. Screenshots

| Screenshot | Captured | Result |
|---|---:|---|
| wp-admin-home-editor-before-d9n.png | YES | PARTIAL (login screen) |
| wp-admin-home-editor-after-d9n.png | YES | PARTIAL (login screen) |
| wp-admin-home-acf-fields-after-d9n.png | YES | PARTIAL (login screen) |
| wp-admin-services-editor-after-d9n.png | YES | PARTIAL (login screen) |
| wp-admin-contacts-editor-after-d9n.png | YES | PARTIAL (login screen) |
| wp-admin-privacy-policy-editor-retained-d9n.png | YES | PARTIAL (login screen) |
| runtime-home-full-desktop-after-d9n.png | YES | PASS |
| runtime-home-full-mobile-after-d9n.png | YES | PASS |
| runtime-service-74-after-d9n.png | YES | PASS |
| runtime-contacts-after-d9n.png | YES | PASS |

Evidence: `validation/v9-06d9n-hide-native-editor-template-pages/screenshot-manifest.json`, `visual-result.json`

---

## 10. No-scope-drift

- DB writes: 0
- Source/theme changes: 2 files only
- Runtime delivery: 2 files copied
- ACF JSON changes: 0
- ACF value writes: 0
- Native post_content writes: 0
- Media uploads: 0
- Attachment creation: 0
- Options writes: 0
- Menu writes: 0
- Rewrite flush: NO
- Plugin install/update/delete: 0
- V9 src/dist changes: 0
- Runtime deletes: 0
- DB dumps staged: NO
- Runtime snapshots staged: NO
- Plugin files staged: NO
- Secrets/API keys: NO
- Result: **PASS**

Evidence: `validation/v9-06d9n-hide-native-editor-template-pages/no-scope-drift-validation.json`

---

## 11. Documentation changes

| File | Action | Reason |
|---|---|---|
| `reports/FP-0002-V9-06D9N-HIDE-NATIVE-EDITOR-FOR-TEMPLATE-PAGES-REPORT-v1.md` | Created | Phase report |
| `architecture/FP-0002-V9-06D9N-*.md` | Created | Audit, plan, implementation, validation, next-step |
| `validation/v9-06d9n-hide-native-editor-template-pages/*.json` | Created | Evidence pack |
| `validation/v9-06d9n-hide-native-editor-template-pages/screenshots/*` | Created | Visual evidence |
| `WORDPRESS/README.md` | Updated | D9-N status |
| `WORDPRESS/SOURCE-AUTHORITY.md` | Updated | D9-N authority line |
| `FP-0002-SHPIGOVSKY/PROJECT-STATUS.md` | Updated | Current phase |

---

## 12. Git checkpoint

*(Updated after commit — see task closeout)*

---

## 13. Final verdict

**PASS**

V9-06D9-N Hide Native Editor for Template-Managed Pages: **COMPLETE**

DB writes: 0  
Source/theme changes: 2  
Runtime delivery: PERFORMED  
ACF JSON changes: 0  
ACF value writes: 0  
Native post_content writes: 0  
Options writes: 0  
Native editor hidden on allowlisted pages: PASS  
ACF visibility preserved: PASS  
Operator-review/legal pages preserved: PASS  
Frontend regression: PASS  
Route smoke: ALL_200  
No-scope-drift: PASS  
Admin screenshots: PARTIAL (unauthenticated headless)

Recommended next phase: **CREATE_V9_06D9O_ADMIN_UX_QA_TASK**

---

## 14. Recommended next action

**CREATE_V9_06D9O_ADMIN_UX_QA_TASK**

Operator in-browser confirmation that Home #4, Services #5, and Contacts #20 show ACF fields without the empty native editor box.

---

## 15. Final safety statement

Target folder: X:\AI MARS  
Volume: AI WS / X:  
Runtime: X:\MARS-Localhost\sites\wordpress\projects\shpigovsky  
V9-06D9-N Hide Native Editor for Template-Managed Pages performed: YES  
Database writes: 0  
Source/theme changes: 2  
Runtime delivery performed: YES  
ACF JSON changes: 0  
ACF value writes: 0  
Native post_content writes: 0  
Native title/slug/status/template writes: 0  
Media uploads: 0  
Attachment creation: 0  
Options writes: 0  
Menu writes: 0  
Service writes: 0  
Services Hub writes: 0  
Contacts writes: 0  
Rewrite flush performed: NO  
Permalink/rewrite changed: NO  
Menus changed: 0  
Redirects created: 0  
External API/API keys added: NO  
Production migration performed: NO  
V9 source changed: NO  
V9 dist changed: NO  
Plugin source changed in Git: NO  
Plugin installs/updates/deletes: 0  
DB dump committed: NO  
Runtime snapshot committed: NO  
Uploaded media files committed: NO  
Plugin files committed: NO  
Helper committed: NO  
Secrets committed: 0
