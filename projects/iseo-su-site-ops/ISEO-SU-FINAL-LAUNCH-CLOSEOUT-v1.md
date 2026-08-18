# ISEO-SU FINAL LAUNCH CLOSEOUT v1

**Programme:** ISEO-SU-SITE-OPS  
**Task ID:** ISEO-SU-SITE-OPS-FINAL-POST-LAUNCH-AND-GIT-SYNC-CLOSEOUT  
**Date:** 2026-08-18  
**Status:** **COMPLETE — ISEO-SU POST-LAUNCH VERIFIED / CANONICAL REMOTE SYNCED / SITE OPS CLOSEOUT COMPLETE**

---

## 1. Status

Glossary production is healthy. Post-launch overflow was real, then fixed with a glossary-scoped CSS block. SEO/indexability smoke passed. Custom `sitemap.xml` unchanged. MERGED / DEFERRED / EXCLUDED untouched. Mobile offcanvas unchanged by operator order. Accepted i-seo.su site-ops history restored to `origin/mars/canonical-post-recovery` via a clean worktree.

## 2. Glossary Production State

| Field | Value |
|-------|-------|
| `/glossary/` | HTTP 200 |
| Published eligible canonical articles | **184** |
| Archive unique term links | **184** |
| MERGED / DEFERRED / EXCLUDED | 30 / 14 / 13 — non-public |
| Related-term block | live; public targets only |
| Archive title | `Глоссарий - INTLSEO Studio` |
| Desktop submenu | `Глоссарий` immediately after calculator |
| Hero | services-style `page_scene`; no rates |
| Production CSS SHA-256 | `4a1202b6b122230eba2edb4c559b03198ac9bfba221a39b561f7c78bca7e453f` |
| CSS deploy stamp | `20260818T101846Z` |

## 3. Mobile Overflow Verification

Historical hero-align evidence: 390px glossary `scrollWidth` 395 vs 390 (**+5px**). Current production (before this closeout fix) still reproduced real overflow:

| Viewport | Archive/singles `scrollWidth` | `clientWidth` | Delta | Actually scrollable |
|----------|-------------------------------|---------------|------:|---------------------|
| 320 | 395 | 320 | 75 | yes |
| 360 | 395 | 360 | 35 | yes |
| 375 | 395 | 375 | 20 | yes |
| 390 | 395 | 390 | 5 | yes |
| 414 | 395 | 414 | 0 | no |

Constant min content width **395px**. Deepest leaf: `.two_common_col__title` (shared Telegram CTA inside `#SecondScreen`), compounded by theme `.row` `box-sizing: content-box` + 15px padding and `.two_common_col` negative side margins. Not breadcrumbs, not alphabet, not `html`/`body`.

## 4. CSS Action

**MOBILE OVERFLOW — FIXED / PRODUCTION AND SOURCE ALIGNED**

- No `overflow-x: hidden` on `html`/`body`.
- Glossary-scoped `@media (max-width: 490px)` rules in `css/main.css` / `production-source/css/main.css`.
- Operator manual hunks preserved (breadcrumbs, archive search label, `.info_span`, list-margin split).
- Before SHA: `8e1774ba8996ed3f8be33c6c9750c5db2db4752ff9c93bb54a46b0a5860f2580`
- After SHA: `4a1202b6b122230eba2edb4c559b03198ac9bfba221a39b561f7c78bca7e453f`
- Remote backup: `css/main.css.bak-glossary-overflow-20260818T101846Z`
- Post-fix: `scrollWidth == clientWidth` (delta 0) at 320 / 360 / 375 / 390 / 414; desktop 1440 unaffected.

## 5. Sitemap State

**NO CHANGE — CUSTOM sitemap.xml REMAINS UNCHANGED**

| Source | Result |
|--------|--------|
| `https://i-seo.su/wp-sitemap-posts-glossary-1.xml` | HTTP 200, **184** URLs |
| `https://i-seo.su/wp-sitemap.xml` | glossary child present |
| `https://i-seo.su/sitemap.xml` | HTTP 200; **0** glossary URLs (intentional) |
| Draft / MERGED / DEFERRED / EXCLUDED leakage | **0** (`kontent-marketing` is a published eligible term, not the DEFERRED `Контент` record) |

## 6. SEO / Indexability Smoke

Archive and representative singles (Nofollow, GEO, E-E-A-T, Core Web Vitals, Канонический URL, АГС, Частотность запроса, BERT, SEO-аудит): HTTP 200; expected titles; canonical `/glossary…`; robots `index, follow` (no accidental `noindex`); singles have meta description; related links are public canonical terms.

Archive has **no Yoast meta description / og:description** (on-page hero description is present). Not treated as a glossary indexer blocker. Optional later Yoast archive-description work only.

`robots.txt` read-only: no glossary `Disallow`.

## 7. Non-Public Corpus

Sampled MERGED (ids 2447, 2674; slug `/glossary/ssl`), DEFERRED (2669 `/sandbox`, 2509), EXCLUDED (2464, 2483): HTTP **404**, not exposed as term pages. No publish / trash / redirect / metadata mutation.

## 8. Mobile Menu Deferred

**MOBILE OFFCANVAS PARITY — DEFERRED BY OPERATOR / OUT OF SCOPE**

`content-mobilemenu.php` / `#offcanvas-MENU` not modified. Offcanvas still has no `Глоссарий` / calculator titles. Desktop submenu unchanged and healthy.

## 9. Site Regression

`/`, `/services.html`, `/blog/`, `/tariff-calc`, `/offers`, `/privacy-policy.html`, `/glossary/`, representative singles: expected HTTP; no PHP fatal; no maintenance; desktop calculator→glossary adjacency intact; services page unchanged; article corpus unchanged; sitemap healthy. `/tariff-calc` and `/offers` remain `noindex, follow` (pre-existing private surfaces).

## 10. Git Remote Sync

Dirty main was **not** used for push. Histories had diverged (`merge-base` `2145935c`; local +70 / remote +310). `origin` lacked `projects/iseo-su-site-ops` after scoped client-ops tree integration `edee6fec`. Report-hub local commits were **not** included.

Clean worktree: `X:\AI MARS STORAGE\git-sync-iseo-su-final-closeout\repo`

Accepted range restored onto current `origin/mars/canonical-post-recovery`:

1. programme tree restore from `f8126b03^`
2. cherry-pick `f8126b03` hero alignment
3. cherry-pick `ff8af69c` final integration
4. cherry-pick closeout commit (overflow CSS + this evidence)

## 11. Remote Canonical Tip

Recorded after push in the companion REPORT §15. Original local SHAs `f8126b03` / `ff8af69c` remain on dirty-main history; equivalent cherry-picks are on the canonical remote (original SHAs cannot be DAG-ancestors of origin without merging 68 `iseo-report-hub` commits).

## 12. Remaining Non-Blocking Items

Optional, separate charters only:

- mobile offcanvas `Глоссарий` parity
- custom `sitemap.xml` glossary duplication (Yoast already lists 184)
- MERGED alias search polish
- archive Yoast meta description

No new programme phase.

## 13. Final Decision

**COMPLETE — ISEO-SU POST-LAUNCH VERIFIED / CANONICAL REMOTE SYNCED / SITE OPS CLOSEOUT COMPLETE**

**MOBILE OVERFLOW — FIXED / PRODUCTION AND SOURCE ALIGNED**

Stop.

---

*ISEO-SU final launch closeout v1 · 2026-08-18.*
