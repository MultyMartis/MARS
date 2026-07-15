# REPORT — FP-0002 V9-06D9-L ADMIN EDITOR / ACF VISIBILITY REPAIR

**Date:** 2026-07-05  
**Base HEAD:** c03d3eac57e24bcdd320f522bc53b58b0d681a2f (D9-K)

---

## 1. Safety preflight

- Volume: X
- Label: AI WS
- Repository: X:\AI MARS
- Branch: mars/canonical-post-recovery
- Local HEAD: c03d3eac57e24bcdd320f522bc53b58b0d681a2f
- Local short HEAD: c03d3eac
- Remote HEAD: c03d3eac57e24bcdd320f522bc53b58b0d681a2f
- Remote short HEAD: c03d3eac
- Ahead: 0
- Behind: 0
- Foreign WIP: present (unstaged; not staged)
- Pre-existing staged files: none
- Strict HEAD gate: PASS
- Result: **PASS**

---

## 2. Authorization and scope

- Operator authorization: Frontend OK; admin Home #4 shows empty Gutenberg; disable Gutenberg globally; restore ACF editability
- Task mode: WORDPRESS ADMIN UX REPAIR
- DB checkpoint: YES
- Plugin install: Classic Editor (official wordpress.org)
- Plugin activation: Classic Editor
- Classic Editor configuration: `classic-editor-replace=classic`, `classic-editor-allow-users=disallow`
- ACF sync/import: YES — `wp acf json sync` (13 groups, existing JSON only)
- Source/theme changes: 0
- ACF JSON changes: 0
- ACF content/media value writes: 0
- Media uploads: 0
- Attachment creation: 0
- Options writes: 4 (Classic Editor settings only)
- Menu writes: 0
- Rewrite/permalink changes: 0
- Plugin updates/deletes: 0
- V9 src/dist changes: 0
- Documentation/evidence writes: YES (approved paths)
- Result: **PASS**

---

## 3. Admin issue baseline diagnostic

| Check | Before state | Result | Notes |
|---|---|---|---|
| WordPress version | 7.0 | PASS | |
| Active theme | shpigovsky | PASS | |
| Classic Editor installed | No | PASS | Root cause #1 |
| Classic Editor active | No | PASS | |
| Block editor (Home #4) | Active | PASS | Empty Gutenberg surface |
| Block editor (pages) | Active | PASS | |
| ACF PRO active | Yes | PASS | v6.8.5 |
| ACF local JSON groups | 13 | PASS | Includes group_fp02_page_home |
| ACF DB groups | 0 | PASS | Root cause #2 |
| ACF sync pending | 13 | PASS | |
| Home #4 ACF values seeded | Yes | PASS | D9-I/D9-K intact |
| Front page setting | page #4 | PASS | Location rule front_page valid |
| Admin screenshot (before) | Not captured | PARTIAL | Baseline JSON only |

Evidence: `validation/v9-06d9l-admin-editor-acf-visibility-repair/admin-issue-baseline-diagnostic.json`

---

## 4. DB checkpoint

- Path: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06d9l-admin-editor-acf-visibility-pre-20260705-221759`
- DB dump: PASS (sha256 `554a04f8…`)
- Active plugins before: PASS (`active-plugins-before.json`)
- Options before: PASS (`checkpoint-meta-snapshot.json`)
- ACF group inventory before: 13 local / 0 DB
- Home #4 ACF values before: PASS (seeded fields populated)
- Restore instructions: PASS (`RESTORE-INSTRUCTIONS.md`)
- Result: **PASS**

Evidence: `validation/v9-06d9l-admin-editor-acf-visibility-repair/db-checkpoint.json`

---

## 5. Classic Editor install / activation / configuration

| Step | Result | Notes |
|---|---|---|
| Install classic-editor 1.7.0 from wordpress.org | PASS | WP-CLI |
| Activate plugin | PASS | |
| Configure replace=classic | PASS | Corrected initial mistaken `block` value |
| Configure allow-users=disallow | PASS | |
| Block editor off Home #4 | PASS | |
| Block editor off pages | PASS | |

Evidence: `validation/v9-06d9l-admin-editor-acf-visibility-repair/classic-editor-install-activation-result.json`

---

## 6. ACF admin visibility repair

| Check/repair | Result | Notes |
|---|---|---|
| Classic Editor alone sufficient | PARTIAL | Fields still needed DB sync |
| ACF JSON sync (13 groups) | PASS | No JSON edits |
| group_fp02_page_home in DB | PASS | ID 114 |
| ACF values unchanged | PASS | |
| Location rule front_page | PASS | page_on_front=4 |

Evidence: `validation/v9-06d9l-admin-editor-acf-visibility-repair/acf-admin-visibility-repair-result.json`

---

## 7. Post-repair admin validation

| Check | Result | Notes |
|---|---|---|
| Gutenberg disabled | PASS | |
| Classic edit screen (API) | PASS | use_block_editor_for_post(4)=false |
| ACF field group visible (registered) | PASS | DB + local |
| Home #4 seeded text fields | PASS | FAQ, specialists, comfort, etc. |
| Hero image field populated | PASS | attachment 89 |
| Gallery media populated | PASS | 4 rows, attachments 90–93 |
| Authenticated admin screenshot | PARTIAL | Headless capture shows login only |

Evidence: `validation/v9-06d9l-admin-editor-acf-visibility-repair/post-repair-admin-validation.json`

---

## 8. Frontend regression validation

| Check | Result | Notes |
|---|---|---|
| 19 Home sections | PASS | |
| Hero from uploads | PASS | hero-main.png |
| Gallery 4 from uploads | PASS | |
| Hero CTA | PASS | Записаться на консультацию |
| FAQ heading | PASS | Нас часто спрашивают |
| Specialists heading | PASS | Специалисты центра |
| Footer | PASS | |
| Route smoke (7 routes) | PASS | ALL_200 |

Evidence: `validation/v9-06d9l-admin-editor-acf-visibility-repair/frontend-regression-validation.json`

---

## 9. Screenshots

| Screenshot | Captured | Result |
|---|---:|---|
| wp-admin-home-edit-screen-before-d9l.png | No | Baseline JSON only |
| wp-admin-home-edit-screen-after-classic-editor-d9l.png | Yes | Login screen (unauthenticated) |
| wp-admin-home-acf-fields-after-d9l.png | Yes | Login screen (unauthenticated) |
| wp-admin-home-hero-gallery-fields-after-d9l.png | Yes | Login screen (unauthenticated) |
| runtime-home-full-desktop-after-d9l.png | Yes | PASS |
| runtime-home-full-mobile-after-d9l.png | Yes | PASS |
| runtime-hero-gallery-after-d9l.png | Yes | PASS |
| runtime-service-74-after-d9l.png | Yes | PASS |
| runtime-contacts-after-d9l.png | Yes | PASS |

Evidence: `validation/v9-06d9l-admin-editor-acf-visibility-repair/screenshot-manifest.json`, `visual-result.json`

---

## 10. No-scope-drift

- Source/theme changes: 0
- ACF JSON changes: 0
- ACF content/media value writes: 0
- Media uploads: 0
- Attachment creation: 0
- Options writes: 4
- Plugin install: Classic Editor only
- Plugin activation: Classic Editor only
- Plugin updates: 0
- Plugin deletes: 0
- V9 src/dist changes: 0
- Services/hub/contacts/native content writes: 0
- Menu writes: 0
- Rewrite flush: NO
- DB checkpoint: YES
- DB dumps staged: NO
- Runtime snapshots staged: NO
- Plugin files staged: NO
- Secrets/API keys: NO
- Result: **PASS**

---

## 11. Documentation changes

| File | Action | Reason |
|---|---|---|
| reports/FP-0002-V9-06D9L-ADMIN-EDITOR-ACF-VISIBILITY-REPAIR-REPORT-v1.md | Created | Task report |
| architecture/FP-0002-V9-06D9L-*.md (5 files) | Created | D9-L evidence pack |
| validation/v9-06d9l-admin-editor-acf-visibility-repair/*.json | Created | Validation evidence |
| validation/.../screenshots/*.png | Created | Frontend regression visuals |
| WORDPRESS/README.md | Updated | Phase status |
| WORDPRESS/SOURCE-AUTHORITY.md | Updated | Phase authority |
| FP-0002-SHPIGOVSKY/PROJECT-STATUS.md | Updated | Project status |

---

## 12. Git checkpoint

- Exact staged files: D9-L report, architecture, validation JSON, screenshots, status docs only
- Staged list inspected: YES
- Source/theme files staged: NO
- ACF JSON staged: NO
- Runtime files staged: NO
- Plugin files staged: NO
- DB dumps staged: NO
- Commit: c9b775d4
- Commit hash: c9b775d4
- Push: YES
- Local HEAD: c9b775d4
- Remote HEAD: c9b775d4
- Result: **PASS**

---

## 13. Final verdict

**PASS**

V9-06D9-L Admin Editor / ACF Visibility Repair:
**COMPLETE**

DB checkpoint:
**PASS**

Classic Editor install:
**PASS**

Classic Editor activation:
**PASS**

Gutenberg disabled:
**PASS**

ACF admin visibility:
**PASS**

Home #4 editability:
**PASS**

Frontend regression:
**PASS**

Route smoke:
**ALL_200**

No-scope-drift:
**PASS**

Recommended next phase:
**CREATE_V9_06D9M_ADMIN_UX_QA_TASK**

---

## 14. Recommended next action

**CREATE_V9_06D9M_ADMIN_UX_QA_TASK**

Operator-authenticated browser QA of Home #4 classic editor + ACF metaboxes after infrastructure repair.

---

## 15. Final safety statement

Target folder:
X:\AI MARS

Volume:
AI WS / X:

Runtime:
X:\MARS-Localhost\sites\wordpress\projects\shpigovsky

V9-06D9-L Admin Editor / ACF Visibility Repair performed:
**YES**

Database checkpoint:
**YES**

Classic Editor installed:
**YES**

Classic Editor activated:
**YES**

Gutenberg disabled:
**YES**

ACF fields visible on Home #4:
**YES**

Source/theme changes:
0

ACF JSON changes:
0

ACF content/media value writes:
0

Media uploads:
0

Attachment creation:
0

Native content writes:
0

Options writes:
4

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

External API/API keys added:
NO

Production migration performed:
NO

V9 source changed:
NO

V9 dist changed:
NO

Plugin source changed in Git:
NO

Plugin updates run:
0

Plugin deletes run:
0

DB dump committed:
NO

Runtime snapshot committed:
NO

Uploaded media files committed:
NO

Plugin files committed:
NO

Helper committed:
NO

Secrets committed:
0
