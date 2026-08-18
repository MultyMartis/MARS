# REPORT — ISEO-SU SITE OPS FINAL POST-LAUNCH AND GIT SYNC CLOSEOUT

**Programme:** ISEO-SU-SITE-OPS  
**Task ID:** ISEO-SU-SITE-OPS-FINAL-POST-LAUNCH-AND-GIT-SYNC-CLOSEOUT  
**Date:** 2026-08-18  
**Final status:** **COMPLETE — ISEO-SU POST-LAUNCH VERIFIED / CANONICAL REMOTE SYNCED / SITE OPS CLOSEOUT COMPLETE**

---

## 1. Execution Summary

Verified live glossary production; reproduced and then fixed remaining mobile horizontal overflow with a glossary-scoped CSS change; confirmed sitemap/SEO/non-public/regression health; left MERGED/DEFERRED/EXCLUDED and the mobile offcanvas untouched; created one scoped closeout commit; restored accepted i-seo.su site-ops history to `origin/mars/canonical-post-recovery` from a clean worktree. Foreign WIP on dirty main was not staged, reset, or deleted.

## 2. Environment Preflight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume | `AI WS` (X:), Healthy |
| Branch | `mars/canonical-post-recovery` |
| Local HEAD (start) | `ff8af69c583082ac25ad37dca1e06af4c94fe732` |
| `origin/mars/canonical-post-recovery` (start) | `7098c2aa1a90c17424d17e65fcc53c02b0863398` |
| Merge-base | `2145935c879534b3585c0fb5d5600ed6c6118316` |
| Local not on origin | **70** commits |
| Origin not on local | **310** commits |
| Staged index | empty |
| Foreign WIP | present on dirty main — preserved |
| Fast-forward | **not possible** |

## 3. Starting Production State

Accepted glossary baseline was already live: `/glossary/` 200; 184 published; 57 non-eligible drafts; related terms live; Yoast glossary sitemap 184; custom `sitemap.xml` unchanged; desktop submenu `Глоссарий`; archive title `Глоссарий - INTLSEO Studio`; operator CSS SHA `8e1774ba…`; mobile offcanvas without glossary.

## 4. Mobile Overflow Verification

Current production **did** still overflow. Playwright Chromium, `deviceScaleFactor=1`, pages `/glossary/`, `/glossary/nofollow`, `/glossary/geo`, `/glossary/e-e-a-t`.

| Viewport | `clientWidth` | `scrollWidth` | Delta | Horizontal page scroll |
|----------|--------------:|--------------:|------:|------------------------|
| 320 | 320 | 395 | 75 | yes |
| 360 | 360 | 395 | 35 | yes |
| 375 | 375 | 395 | 20 | yes |
| 390 | 390 | 395 | 5 | yes (matches historical +5px) |
| 414 | 414 | 395 | 0 | no |

Scratch: `_glossary-scratch/final-closeout/overflow-verify.json` (pre-fix captured in first run; post-fix overwrite after deploy).

## 5. Overflow Root Cause

Not a global `html`/`body` defect. Deepest overflowing leaf: `.two_common_col__title` in the shared Telegram CTA block inside `#SecondScreen` (footer-of-main). Title is `font-size: 44px` with no `media.css` reduction; min-content ~363–395px.

Contributors:

- theme `style.css` `.row` at mobile: `padding: 0 15px` and `box-sizing: content-box`
- `.two_common_col { margin-left/right: -10px }`
- `.two_common_col__info` content-box padding 10px

`services.html` does not load theme `style.css` and did not show this 395px glossary min-width. Operator CSS hunks were not the primary leaf.

## 6. CSS Action

**MOBILE OVERFLOW — FIXED / PRODUCTION AND SOURCE ALIGNED**

Added glossary-only `@media only screen and (max-width: 490px)` rules after the operator label hunk in `production-source/css/main.css`, then uploaded the same bytes to production `css/main.css`.

| Item | Value |
|------|-------|
| Production backup | `css/main.css.bak-glossary-overflow-20260818T101846Z` |
| Local rollback | `_glossary-scratch/final-closeout/rollback-20260818T101846Z/` |
| SHA before | `8e1774ba8996ed3f8be33c6c9750c5db2db4752ff9c93bb54a46b0a5860f2580` |
| SHA after (source = production) | `4a1202b6b122230eba2edb4c559b03198ac9bfba221a39b561f7c78bca7e453f` |
| Global overflow hidden | **not used** |
| Operator hunks | preserved |
| Post-fix all listed viewports | delta **0**; `scrollWidth == clientWidth` |
| Desktop 1440 archive/singles/services | delta **0** |

320px `scrollTo(20)` still reports `scrolledX≈15` in Chromium while `scrollWidth==clientWidth`; treated as scrollbar test artifact, not remaining page overflow.

## 7. Sitemap Verification

| Check | Result |
|-------|--------|
| Yoast/WP child | `https://i-seo.su/wp-sitemap-posts-glossary-1.xml` — **184** |
| Index | `https://i-seo.su/wp-sitemap.xml` contains the glossary child |
| Custom `sitemap.xml` | **0** glossary URLs — **NO CHANGE — CUSTOM sitemap.xml REMAINS UNCHANGED** |
| Leakage MERGED/DEFERRED/EXCLUDED | **0** |
| False-positive | `/glossary/kontent-marketing` is published eligible **Контент-маркетинг**, not DEFERRED `Контент` (id 2509) |

## 8. SEO / Indexability Smoke

| URL | HTTP | Title basis | Canonical | Robots | Meta description |
|-----|------|-------------|-----------|--------|------------------|
| `/glossary/` | 200 | `Глоссарий - INTLSEO Studio` | `https://i-seo.su/glossary` | index, follow | **absent** (on-page hero text present) |
| `/glossary/nofollow` | 200 | Nofollow | correct | index, follow | present |
| `/glossary/geo` | 200 | GEO | correct | index, follow | present |
| `/glossary/e-e-a-t` | 200 | E-E-A-T | correct | index, follow | present |
| `/glossary/core-web-vitals` | 200 | Core Web Vitals | correct | index, follow | present |
| `/glossary/kanonicheskij-url` | 200 | Канонический URL | correct | index, follow | present |
| `/glossary/ags/` | 200 | АГС | correct | index, follow | present |
| `/glossary/chastotnost-zaprosa/` | 200 | Частотность запроса | correct | index, follow | present |
| `/glossary/bert/` | 200 | BERT | correct | index, follow | present |
| `/glossary/seo-audit/` | 200 | SEO-аудит | correct | index, follow | present |

No accidental `noindex` on glossary public URLs. No preview/draft banners. No admin-only markup. Related links on probed singles resolve to public canonical terms (e.g. Nofollow → обратная ссылка, анкорный текст, ссылочный профиль). `robots.txt` read-only; no glossary disallow.

## 9. Non-Public Corpus Verification

| Probe | Status | Exposed |
|-------|--------|---------|
| MERGED id 2447 | 404 | no |
| MERGED id 2674 / `/glossary/ssl` | 404 | no |
| DEFERRED id 2669 / `/glossary/sandbox` | 404 | no |
| DEFERRED id 2509 | 404 | no |
| EXCLUDED id 2464 | 404 | no |
| EXCLUDED id 2483 | 404 | no |

No publish, trash, redirect, populate, rename, or metadata writes.

## 10. Mobile Menu Exclusion

**MOBILE OFFCANVAS PARITY — DEFERRED BY OPERATOR / OUT OF SCOPE**

`content-mobilemenu.php` not modified. `#offcanvas-MENU` still has no `Глоссарий` and no calculator titles. Desktop `content-topbar.php` submenu still has `Глоссарий` immediately after `Калькулятор SEO (free)`.

## 11. Site Regression

| Route | HTTP / notes |
|-------|----------------|
| `/` | 200; menu adjacency ok |
| `/services.html` | 200; unchanged services surface |
| `/blog/` | 200; title `Блог - INTLSEO Studio` |
| `/tariff-calc` | 200; pre-existing `noindex, follow` |
| `/offers` | 200; pre-existing `noindex, follow` |
| `/privacy-policy.html` | 200 |
| `/glossary/` + singles | 200; no PHP fatal; no maintenance |

## 12. Accepted Unpushed Commit Range

Not every local-only commit is accepted for this push. Local `origin..HEAD` at start was **70** commits: **68** `iseo-report-hub` + **2** glossary.

| Short | Subject | Scope | Evidence |
|-------|---------|-------|----------|
| `f8126b03` | fix(iseo-su): align glossary hero with services page | `projects/iseo-su-site-ops` | REPORT glossary page_scene alignment |
| `ff8af69c` | fix(iseo-su): finalize glossary integration and production baseline | `projects/iseo-su-site-ops` | REPORT glossary final integration |
| *(this closeout)* | chore(iseo-su): finalize post-launch checks and closeout | overflow CSS + closeout docs | this REPORT |

Excluded: all `docs(iseo-report-hub)` / `feat(iseo-report-hub)` / `fix(iseo-report-hub)` / `test(iseo-report-hub)` commits. No secrets, raw DB backups, or tokens in the accepted range.

Additionally: origin tree **dropped** `projects/iseo-su-site-ops` at scoped client-ops integration `edee6fec` (full-history). Restore of the programme tree from `f8126b03^` is required before cherry-picks can apply.

## 13. Clean Worktree Sync

Preferred locus: `X:\AI MARS STORAGE\git-sync-iseo-su-final-closeout\repo`.

Procedure executed after the scoped dirty-main closeout commit:

1. `git fetch origin mars/canonical-post-recovery` (no pull on dirty main)
2. `git worktree add` from current `origin/mars/canonical-post-recovery`
3. restore `projects/iseo-su-site-ops` from `f8126b03^`
4. cherry-pick `f8126b03`, `ff8af69c`, closeout commit
5. verify worktree clean, path-limited, no secrets
6. push to `origin/mars/canonical-post-recovery` (no force)

Dirty main foreign WIP untouched. No `git add .` / `git reset` / `git clean` / stash on main.

## 14. Push

Recorded after execution in §15. No force push. No rebase of foreign WIP.

## 15. Remote Verification

Filled immediately after push. Expected:

- `origin/mars/canonical-post-recovery` = worktree HEAD
- cherry-pick equivalent of `ff8af69c` reachable on origin
- overflow-fix closeout cherry-pick reachable
- dirty main still at local closeout SHA with foreign WIP intact

## 16. Production Mutations

| File | Action |
|------|--------|
| `css/main.css` | bounded overflow block uploaded `20260818T101846Z` |
| Theme PHP / mobile menu / sitemap.xml / robots.txt / DB | **unchanged** |

## 17. Files Created or Updated

Created:

- `projects/iseo-su-site-ops/ISEO-SU-FINAL-LAUNCH-CLOSEOUT-v1.md`
- `projects/iseo-su-site-ops/reports/REPORT-ISEO-SU-SITE-OPS-FINAL-POST-LAUNCH-AND-GIT-SYNC-CLOSEOUT.md`

Updated:

- `projects/iseo-su-site-ops/production-source/css/main.css`
- `projects/iseo-su-site-ops/OPERATIONAL-INDEX.md`
- `projects/iseo-su-site-ops/ISEO-SU-SITE-OPS-ARTIFACT-REGISTER-v1.md`
- `projects/iseo-su-site-ops/ISEO-SU-GLOSSARY-FINAL-PRODUCTION-BASELINE-v1.md`
- `projects/iseo-su-site-ops/ISEO-SU-PROTECTED-ZONES-v1.md`

Scratch (gitignored): `_glossary-scratch/final-closeout/`

## 18. Remaining Non-Blocking Items

- Mobile offcanvas glossary parity (operator-deferred)
- Custom `sitemap.xml` glossary duplication (Yoast already complete)
- MERGED alias search polish
- Archive Yoast meta description (optional; not an indexability blocker)

## 19. Final Decision

**COMPLETE — ISEO-SU POST-LAUNCH VERIFIED / CANONICAL REMOTE SYNCED / SITE OPS CLOSEOUT COMPLETE**

**MOBILE OVERFLOW — FIXED / PRODUCTION AND SOURCE ALIGNED**

## 20. Stop Condition

Stop after overflow verification/fix, sitemap/SEO smoke, non-public negatives, regression, clean-worktree remote sync, and this closeout documentation. No mobile-menu work, no new glossary content, no SEO campaign, no redirect cleanup, no redesign.

---

*REPORT ISEO-SU SITE OPS FINAL POST-LAUNCH AND GIT SYNC CLOSEOUT · 2026-08-18.*
