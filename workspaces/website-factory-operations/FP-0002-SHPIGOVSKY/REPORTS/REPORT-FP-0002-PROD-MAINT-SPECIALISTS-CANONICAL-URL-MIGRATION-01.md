# REPORT — FP-0002 SPECIALISTS CANONICAL URL MIGRATION 01

**Date (UTC):** 2026-08-24  
**Production:** https://shpigovsky.ru/  
**Page:** #1030 (same object)  
**Core:** `0.3.28-specialists-canonical-url`

## 1. Verdict

**PASS**

## 2. Current-origin preflight

- Workspace `X:\AI MARS`, volume `X:` / `AI WS`
- Fetched `origin/mars/canonical-post-recovery`
- Initial implementation base SHA: `9c669a70752d3013b344426dfcbcd7bdb06ea61c`
- Replayed onto advanced origin tip before commit: `b14c99084840fe9e05d26c90bea0e40b6d7d3a65`
- Clean worktree: `X:\AI MARS\worktrees\fp0002-specialists-canonical-url-migration-01`
- Branch: `agent/fp0002-specialists-canonical-url-migration-01`
- Shared dirty main foreign WIP **not** used

## 3. Fresh production/editorial intake

Evidence: `REPORTS/evidence/prod-maint-specialists-canonical-url-migration-01/01-prod-intake.json`

| Item | Before |
|------|--------|
| Page #1030 slug | `specyalisty` |
| Template | `page-templates/specialists-hub.php` |
| Reusable | enabled; `rehab_requirements`, `about_home` |
| CPT rewrite | `specyalisty`, `has_archive=false` |
| Published specialists | 9 |
| Menu Primary item | page object #1030 → `/specyalisty/` |
| Option all-link | `http://shpigovsky.beget.tech/specyalisty/` |
| `blog_public` | `1` |
| Core | `0.3.27-specialists-hub-admin-ux` |

## 4. URL ownership before migration

| Owner | Value |
|-------|--------|
| Hub Page | #1030 slug `specyalisty` |
| CPT | `Specialist::REWRITE_SLUG = specyalisty` |
| Helpers | `get_page_by_path('specyalisty')` + hardcoded `/specyalisty/` fallback |
| Menu | post_type page #1030 |
| Sitemap | native WP sitemap with old paths |
| Canonicals | old paths |
| Redirects | none for this family |

## 5. Migration implementation

1. CPT rewrite → `specialisty` + one-time flush flag `fp02_specialist_cpt_rewrite_flushed_specialisty_v1`
2. Page #1030 slug → `specialisty` (same ID)
3. Helpers resolve hub by ID `#1030` / path `specialisty`
4. `SpecialistLegacyRedirect` module (template_redirect 301)
5. `.htaccess` fragment + production custom block (HTTPS host to avoid SSL-proxy chain)
6. Cleared stale ACF option `fp02-block-specialists_specialists_all_link_url`
7. ACF JSON / FieldGroups admin copy updated
8. Core version `0.3.28-specialists-canonical-url`

## 6. Page #1030

Same object. Slug `specialisty`. Template + reusable + title preserved.

## 7. Specialist CPT routing

Rewrite `specialisty`, `has_archive=false`. Nine published slugs unchanged.

## 8. Internal link migration

| Owner | Change |
|-------|--------|
| CPT permalinks | auto via rewrite |
| Page #1030 permalink / menu | auto via slug |
| `shpigovsky_get_specialists_*` helpers | new path / ID 1030 |
| ACF all-link option | cleared (empty → generated permalink) |
| ACF JSON / FieldGroups notices | new spelling |

## 9. Redirect implementation

- **Primary:** production `.htaccess` custom block from `DOCS/PRODUCTION/fp-0002-legacy-redirects.htaccess.fragment`
- **Companion:** `Shpigovsky\Core\Permalinks\SpecialistLegacyRedirect`
- Rules: hub + path-preserving singles; HTTPS `HTTP_HOST` targets (no HTTP→HTTPS chain)

## 10. Complete redirect matrix

| OLD | status | NEW | final |
|-----|--------|-----|-------|
| `/specyalisty/` | 301 | `/specialisty/` | 200 |
| `/specyalisty/shpigovsky/` | 301 | `/specialisty/shpigovsky/` | 200 |
| `/specyalisty/kazakov/` | 301 | `/specialisty/kazakov/` | 200 |
| `/specyalisty/kostyuk/` | 301 | `/specialisty/kostyuk/` | 200 |
| `/specyalisty/hanikova/` | 301 | `/specialisty/hanikova/` | 200 |
| `/specyalisty/shapiguzova/` | 301 | `/specialisty/shapiguzova/` | 200 |
| `/specyalisty/litvinov/` | 301 | `/specialisty/litvinov/` | 200 |
| `/specyalisty/poverinov/` | 301 | `/specialisty/poverinov/` | 200 |
| `/specyalisty/filippov/` | 301 | `/specialisty/filippov/` | 200 |
| `/specyalisty/filippova/` | 301 | `/specialisty/filippova/` | 200 |

Evidence: `05-live-qa.json`

## 11. New URL QA

Hub 200; H1 «Специалисты»; cards intact; no `internal-page-nav`; all 9 singles 200 + correct canonicals.

## 12. Old URL QA

Exactly one 301 → new URL → 200. No chains/loops/302/404 after HTTPS Location fix.

## 13. Internal old-URL audit after migration

**LIVE INTERNAL LINKS TO `/specyalisty/`: 0**

Checked: home, hub, `/uslugi/`, sample single. Menu/home use `/specialisty/`.

## 14. Sitemap / canonical / SEO

- Hub canonical: `https://shpigovsky.ru/specialisty/`
- Singles: `https://shpigovsky.ru/specialisty/{slug}/`
- Pages sitemap: new hub only (no old)
- Specialists sitemap: 9 new URLs, 0 old

## 15. Admin/editorial preservation

Template, reusable selection/enable, specialist IDs/slugs/`menu_order`/content preserved.

## 16. Indexing / robots safety

`blog_public=1` OPEN. Robots unchanged (no specialist path rules). Indexing not closed.

## 17. Production ↔ source parity

`06-parity.json`: **14/14 exact MATCH** + htaccess fragment MATCH.

## 18. Backup / rollback

- Operator full Beget backup acknowledged
- Layer-B: `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-maint-specialists-canonical-url-migration-01\`
- Rollback: restore Layer-B files + page slug `specyalisty` + CPT rewrite constant + prior htaccess block + clear flush flag / re-flush

## 19. Files / DB/config changed

**Source/runtime files:** core plugin (5), theme (7), ACF JSON (2), htaccess fragment + production `.htaccess`.

**DB:** page #1030 `post_name`; option all-link cleared; rewrite flush + flush flag.

## 20. Git

Commit: `00ce9196e1157cbb0930cd2332f9b771ea7c91e3`.
Push to `origin/mars/canonical-post-recovery` (this wave).

## 21. Current canonical URL truth

Hub canonical: `https://shpigovsky.ru/specialisty/`  
Specialist canonical pattern: `https://shpigovsky.ru/specialisty/{slug}/`  
Old `specyalisty`: **DEPRECATED — REDIRECT-ONLY / HISTORICAL EVIDENCE.**

## 22. Residuals

None blocking. Historical reports/evidence retain old URLs by design.

## 23. Mutation statement

Bounded production URL migration only: Page #1030 slug, CPT rewrite base, helpers/ACF copy, redirects, stale option clear, rewrite flush. No robots/indexing/SMTP/forms/Metrika/layout/editorial specialist content changes. WPilot writes OFF.
