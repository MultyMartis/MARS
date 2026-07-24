# REPORT — ISEO-SU SITE OPS GLOSSARY ARCHITECTURE TEMPLATE AND CONTENT INTAKE

**Task ID:** ISEO-SU-SITE-OPS-GLOSSARY-ARCHITECTURE-TEMPLATE-AND-CONTENT-INTAKE  
**Date:** 2026-07-24  
**Final status:** **COMPLETE — GLOSSARY FOUNDATION READY / TERMS IMPORTED AS DRAFTS**

---

## 1. Execution Summary

Designed and deployed a WordPress `glossary` CPT with archive/single templates that reuse only existing i-seo.su classes, imported **241** workbook terms as **drafts** (no definitions invented), and left public exposure closed (anonymous `/glossary/` → 404, sitemap excluded, no menu link).

---

## 2. Environment Preflight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Drive / volume | `X:` / **AI WS** |
| Branch | `mars/canonical-post-recovery` |
| Staged index | empty at start |
| HEAD | `39b01a19…` (local ahead of origin — foreign/unrelated unpushed history preserved) |
| Foreign WIP | present across other projects — **not touched** |
| Access files | present under `local/sites/iseo-su-production/` and Git-ignored |

---

## 3. Backup Confirmation

Operator confirmed a fresh full Beget backup before this task. Theme file backups created as `*.bak-glossary-20260724T054207Z` on overwrite; baseline `functions.php` also retained under `_glossary-scratch/pre-deploy-backup/`.

---

## 4. Workbook Analysis

| Metric | Count |
|--------|-------|
| Raw rows | 266 |
| Header repeats | 13 |
| Blank separators | 12 |
| Valid unique terms | **241** |
| Duplicates | 0 |
| Definitions in workbook | none |

Sanitized inventory: `data/glossary-intake/glossary-terms-inventory-v1.json` / `.csv`.

---

## 5. Architecture Decision

- CPT `glossary` in theme `iseoblog` (`inc/glossary-*.php`) — mirrors CPT `offer` modularity.  
- URLs: `/glossary/` + `/glossary/{slug}/` (`with_front => false`).  
- ACF PHP fields for synonyms/keywords/LSI/notes; letter derived from title.  
- Publication gate `ISEO_GLOSSARY_PUBLIC_EXPOSURE = false`.  
- No child theme, no glossary plugin, no shared CSS/JS edits.

---

## 6. Reference Template Analysis

Public privacy route: **`/privacy-policy.html`** — static PHP-capable HTML using theme parts for topbar/mobile menu; main structure `page_scene` + `content_block`. Not modified. Blog `blog_filter` reused for alphabet chips. Blog single patterns deliberately avoided (stats/authors/ratings).

---

## 7. Existing Style Reuse

Mapped in `ISEO-SU-GLOSSARY-TEMPLATE-COMPONENT-MAP-v1.md`. No new stylesheet/selectors/inline styles in glossary templates.

---

## 8. CPT and ACF Implementation

Deployed to `wp-content/themes/iseoblog/`:

- `functions.php` (require bootstrap only)  
- `inc/glossary-bootstrap.php`, `glossary-cpt.php`, `glossary-acf.php`, `glossary-helpers.php`, `glossary-import-admin.php`  
- `archive-glossary.php`, `single-glossary.php`  
- `inc/data/glossary-terms-inventory-v1.json`  

Admin: CPT menu «Глоссарий»; ACF group visible on term edit.

---

## 9. URL and Indexation Model

| Control | Result |
|---------|--------|
| Anonymous archive/single | 404 while gate closed |
| `wp_robots` | noindex/nofollow while gate closed |
| Yoast sitemap | post type excluded while gate closed |
| REST publish probe | `[]` |
| Menu | not added |

---

## 10. Import Execution

Admin Tools import (then disabled):

- Dry-run: 241 would_create  
- Run: **241 created**, 0 skipped, 0 errors  
- Status forced: draft  
- Idempotent title map for re-runs  

---

## 11. Draft Content State

241 glossary drafts; empty content/excerpt; ACF metadata from workbook; no published empties.

---

## 12. Archive Template

Editor preview: H1 «Глоссарий», `page_scene`, alphabet `blog_filter`, grouped lists. Anonymous: 404.

---

## 13. Single Template

Preview OK: `page_scene`, breadcrumbs, content block, back link; no fake meta.

---

## 14. Admin Validation

CPT list OK; ACF fields OK; draft count 241; import page worked then disabled.

---

## 15. Frontend Preview Validation

Logged-in archive preview OK. Anonymous `/glossary/` 404. No public menu entry.

---

## 16. No-new-style Validation

No new CSS files/selectors added. Glossary templates contain no inline `style=`. One `style=` observed in logged archive HTML originates from pre-existing theme chrome inside footer/main, not glossary markup.

---

## 17. Regression Validation

Anonymous checks (`post-import-anon-checks.json`): `/`, `/privacy-policy.html`, `/blog/`, `/user-agreement.html`, `/tariff-calc`, `/offers` → 200; `/glossary/` → 404. No form submits; WPilot bridge/REST not used.

---

## 18. Rollback Readiness

Exact file rollback via SFTP bak copies + remove glossary includes/templates; delete only `glossary` drafts; flush rewrites; verify baselines. Full Beget restore only if scoped rollback fails.

---

## 19. Files Created or Updated

**Created (project):**

- `wordpress/iseoblog-glossary/**` (theme package)  
- `data/glossary-intake/glossary-terms-inventory-v1.json`  
- `data/glossary-intake/glossary-terms-inventory-v1.csv`  
- `ISEO-SU-GLOSSARY-ARCHITECTURE-AND-CONTENT-MODEL-v1.md`  
- `ISEO-SU-GLOSSARY-TERM-INTAKE-REGISTER-v1.md`  
- `ISEO-SU-GLOSSARY-TEMPLATE-COMPONENT-MAP-v1.md`  
- `reports/REPORT-ISEO-SU-SITE-OPS-GLOSSARY-ARCHITECTURE-TEMPLATE-AND-CONTENT-INTAKE.md`  

**Updated:** task routing guide, route matrix, WP object map, protected zones, artifact register, SAFE UNKNOWN register, OPERATIONAL-INDEX.

**Production:** theme files listed in §8 (+ bak copies).

---

## 20. Production Changes

Theme-only glossary foundation + 241 draft CPT posts + ACF values. No core/plugin/.htaccess/wp-config/css/js/home/privacy edits. WPilot untouched.

---

## 21. Risks

Empty public index risk mitigated by 404/noindex/sitemap exclude. Accidental mass publish remains an editorial risk until gate opens. Server still holds inventory JSON with import UI disabled (G-U-004).

---

## 22. SAFE UNKNOWN

See architecture model §19 (Yoast workflow preference; optional `.html` singles; related terms; inventory retention on server).

---

## 23. Git Persistence

Scoped commit planned: glossary package + intake data + docs/register updates. No push.

---

## 24. Operator Review

Review draft terms, approve definition-writing process, then decide publication gate + menu/sitemap.

---

## 25. Next Task

**Suggested:** ISEO-SU glossary editorial content wave (definitions/excerpts) under separate charter — still no mass publish until QA.

---

## 26. Stop Condition

- No glossary term published  
- No public menu link  
- No empty thin pages indexed  
- No new CSS introduced  
- Existing pages unchanged (privacy untouched)  
- Foundation + draft intake ready  
- No push  
- Waiting for operator review before definitions/publication  

---

*REPORT complete · 2026-07-24.*
