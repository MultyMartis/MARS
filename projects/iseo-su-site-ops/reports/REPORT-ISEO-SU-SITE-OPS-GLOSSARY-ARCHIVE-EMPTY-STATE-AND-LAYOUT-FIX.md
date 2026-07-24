# REPORT — ISEO-SU SITE OPS GLOSSARY ARCHIVE EMPTY-STATE AND LAYOUT FIX

**Task ID:** ISEO-SU-SITE-OPS-GLOSSARY-ARCHIVE-EMPTY-STATE-AND-LAYOUT-FIX  
**Date:** 2026-07-24  
**Final status:** **COMPLETE — GLOSSARY ARCHIVE LAYOUT FIXED / DRAFT PREVIEW WORKING**

---

## 1. Execution Summary

Fixed the authenticated glossary archive empty layout: the main WP archive query reported 241 found posts but left `$wp_query->posts` empty, so the template loop rendered 241 nulls as an orphan `#` group of empty anchors (yellow bullet column). Replaced loop collection with a dedicated archive query, skipped empty groups, reused privacy-style plain `h2` headings, and wired draft terms to capability-gated preview links. Anonymous closed behavior preserved. No new CSS. No terms published.

---

## 2. Environment Preflight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Drive / volume | `X:` / **AI WS** |
| Branch | `mars/canonical-post-recovery` |
| Staged index at start | empty |
| HEAD (pre-commit) | `5f46c3df…` (local ahead of origin — unrelated unpushed history preserved) |
| Foreign WIP | present across other projects — **not touched** |

---

## 3. Defect Baseline

Authenticated `/glossary/`:

- `# (241)` alphabet chip only
- `#` heading + 241× `<a href=""></a>`
- Tall yellow list-marker column; scrollHeight ≈ 11385
- Drafts in admin: **241**; published: **0**
- Anonymous `/glossary/`: **404**

Evidence: `_glossary-scratch/layout-fix/baseline-receipt.json`, `baseline-auth-archive.html/.png`

---

## 4. Root Cause

Main query SQL selected 241 glossary drafts (`found_posts=241`, `post_count=241`) but **`count($wp_query->posts)=0`**. `have_posts()` still iterated 241 times, `get_post()` returned null, grouping mapped empty titles to `#`, and empty `<li>` bullets produced the giant yellow dotted line. Not a CSS/`min-height` issue.

---

## 5. Source Changes

| File | Change |
|------|--------|
| `wordpress/iseoblog-glossary/inc/glossary-helpers.php` | Dedicated `iseo_glossary_get_archive_posts()`, raw titles, preview URLs, safer grouping |
| `wordpress/iseoblog-glossary/archive-glossary.php` | Use dedicated query; plain `h2` groups; empty-state copy; no empty wrappers |
| `wordpress/iseoblog-glossary/inc/glossary-cpt.php` | Align `pre_get_posts` statuses with helper; document main-query limitation |

Deployed to production theme `iseoblog` with scoped `*.bak-glossary-layoutfix-20260724T064614Z` backups.

---

## 6. Draft Preview Behavior

Editors with `edit_posts` see drafts on the archive via the dedicated query. Each term links to `get_preview_post_link()` when `edit_post` is allowed. Anonymous users still receive 404. Private posts remain capability-gated. No public draft permalinks invented.

---

## 7. Alphabet Grouping

- Cyrillic / Latin / `0–9` from first character
- `#` only for real symbol titles; never for empty dataset
- Post-fix: **47** populated groups; **no** `#` group; **241** terms listed

---

## 8. Empty State

Copy when no groups: `Термины пока не добавлены.` (search miss: `По запросу ничего не найдено.`). No alphabet chips or letter lists in that case.

---

## 9. No-new-style Validation

No stylesheet added; no new selectors; no inline styles in glossary templates. Letter groups dropped `content_block__title` in favor of privacy-style plain `h2` inside `content_block`. Residual `content_block__title` on the page comes from pre-existing Telegram/audit chrome only.

---

## 10. Production Deployment

SFTP upload of three theme files after scoped bak copies. Receipt: `_glossary-scratch/layout-fix/deploy-layout-fix-receipt.json`. Import tool remains disabled. Exposure gate remains false.

---

## 11. Authenticated Preview Validation

| Metric | Result |
|--------|--------|
| Terms listed | 241 |
| Empty anchors | 0 |
| Letter groups | 47 |
| Orphan `#` | absent |
| Preview notice | present |
| Single draft preview | OK |
| PHP fatal | none |

---

## 12. Anonymous Boundary Validation

`/glossary/` → **404**. Noindex/sitemap-exclude/menu policies unchanged. Draft count still 241; published still 0.

---

## 13. Regression Validation

Anonymous: `/`, `/privacy-policy.html`, `/blog/`, `/tariff-calc`, `/offers` → **200**. No form/mail triggers. WPilot untouched.

---

## 14. Rollback Readiness

Restore `archive-glossary.php`, `inc/glossary-helpers.php`, `inc/glossary-cpt.php` from `*.bak-glossary-layoutfix-20260724T064614Z`. Re-check auth preview + anon 404. Full Beget only if scoped restore fails.

---

## 15. Files Created or Updated

**Created:**

- `ISEO-SU-GLOSSARY-ARCHIVE-LAYOUT-FIX-EVIDENCE-v1.md`
- `reports/REPORT-ISEO-SU-SITE-OPS-GLOSSARY-ARCHIVE-EMPTY-STATE-AND-LAYOUT-FIX.md`

**Updated:**

- `wordpress/iseoblog-glossary/archive-glossary.php`
- `wordpress/iseoblog-glossary/inc/glossary-helpers.php`
- `wordpress/iseoblog-glossary/inc/glossary-cpt.php`
- `ISEO-SU-GLOSSARY-TEMPLATE-COMPONENT-MAP-v1.md`
- `ISEO-SU-GLOSSARY-ARCHITECTURE-AND-CONTENT-MODEL-v1.md`
- `ISEO-SU-SITE-OPS-ARTIFACT-REGISTER-v1.md`
- `OPERATIONAL-INDEX.md`

**Local evidence (untracked scratch):** `_glossary-scratch/layout-fix/**`

---

## 16. Git and Foreign WIP

Scoped commit created (no push). Foreign WIP left untouched. Scratch evidence not staged.

---

## 17. Final Decision

**COMPLETE — GLOSSARY ARCHIVE LAYOUT FIXED / DRAFT PREVIEW WORKING**

---

## 18. Operator Review

Please confirm authenticated `/glossary/` shows populated alphabet groups and that anonymous `/glossary/` remains 404. Editorial publish gate remains operator-controlled.

---

## 19. Stop Condition

- No glossary term published
- Public exposure closed
- Authenticated draft preview working
- No giant empty `#` bullet column
- No new CSS
- Existing baseline routes unchanged
- No push
- Waiting for operator review

---

*REPORT · GLOSSARY ARCHIVE EMPTY-STATE AND LAYOUT FIX · 2026-07-24.*
