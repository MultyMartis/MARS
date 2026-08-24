# REPORT — FP-0002 PROD-MAINT SPECIALISTS NAV + SEO + MAPS 01

**Date (UTC):** 2026-08-24  
**Production:** https://shpigovsky.ru/  
**Core:** `0.3.29-specialists-nav-seo-maps-01` (was `0.3.28-specialists-canonical-url`)

## 1. Verdict

**PASS_WITH_ATTENTION**

Wave objectives met on production. Residual ATTENTION items are QA-script URL samples and strict string-compare noise (typography / HTML entities), not functional regressions.

## 2. Current-origin preflight

- Workspace `X:\AI MARS`, volume `X:` / `AI WS`
- Implementation worktree: `X:\AI MARS\worktrees\fp0002-specialists-nav-seo-maps-01`
- Branch: `wave/fp0002-specialists-nav-seo-maps-01` @ `16a14050f27bcb49dce54857122c55b975004216`
- Remote advanced during wave: `origin/mars/canonical-post-recovery` = `b0447bc82a05c385d69b78c4e8666fa4331e5a84` (`ocpilot: apply SITE-002 catalog normalization`)
- Rebase onto remote tip before push (shared dirty main foreign WIP **not** used)

## 3. Fresh production/editorial intake

Evidence: `REPORTS/evidence/prod-maint-specialists-nav-seo-maps-01/01-prod-intake.json`

| Item | Value |
|------|--------|
| `blog_public` | `1` (OPEN) |
| Core (pre-wave) | `0.3.28-specialists-canonical-url` |
| Homepage #4 | `fp02_seo_title` + `fp02_seo_description` populated (Olya) |
| Contacts #20 | SEO fields populated; 2 map rows with constructor embed |
| Map rows `map_scroll` | `false` (legacy default) |
| Specialists hub #1030 | `/specialisty/`, template `specialists-hub.php` |
| Robots SHA (pre-wave) | `2594093919d01f067bcd3776d50d973cfa20a1faf4a6d63fc23f21367d08529e` |

## 4. Task 01 — Specialists hub navigation

**Requirement:** Remove breadcrumb/navigation output **completely** on `/specialisty/` (not CSS hide).

**Root cause:** Prior layout-polish wave used `shpigovsky_render_breadcrumbs( array( 'wrap' => 'none' ) )`, which removed `.internal-page-nav` wrapper but still emitted breadcrumb markup.

**Fix:** Removed breadcrumb renderer call entirely from `page-templates/specialists-hub.php`. `template-parts/specialist/hub-content.php` does not render breadcrumbs.

**Live QA:** No `internal-page-nav`, no breadcrumb nav on hub — **PASS**. Breadcrumb regression on `/o-centre/` — **PASS**.

## 5. Task 02 — Global SEO meta (Admin → frontend)

**Owner:** `WORDPRESS/theme/shpigovsky/inc/seo-entity-meta.php`  
**ACF fields:** `fp02_seo_title`, `fp02_seo_description` (`plugins/shpigovsky-core/src/Fields/SeoEntityMeta.php`; post types: page, post, service, specialist)

**Root cause:** Context resolution explicitly excluded `is_front_page()` and `is_home()`, so static front page and posts page never received Admin SEO values.

**Fix:**

- Refactored context via `shpigovsky_seo_get_context_post_id()` for singular entities, `page_on_front`, `page_for_posts`
- Excluded search / 404 / pagination-owned contexts
- When custom SEO title is set, unset `site` / `tagline` title parts (full SEO title convention)

**Live QA:**

| Page | Admin SEO populated | Frontend title | Meta description | Result |
|------|---------------------|----------------|------------------|--------|
| Homepage `/` | yes | present | present, matches admin | **PASS** |
| Contacts `/kontakty/` | yes | present | present, matches admin | **PASS** |
| Hub, singles, hubs without admin SEO | empty | WP default title | none (expected) | **PASS** |

**ATTENTION:** `title_matches_admin: false` on homepage/contacts in automated QA — typography normalizes nbsp/dash variants and `<title>` uses HTML entities; semantic content matches in source.

## 6. Task 03 — Contacts Yandex Maps

**Root cause:** `location-card.php` showed privacy fallback card even when valid Yandex Constructor embed existed in Admin.

**Fix:**

- Render live constructor embed when sanitized; fallback only for invalid/missing embed or legacy iframe URL path
- Added per-map-row ACF `map_scroll` (`true_false`, default **OFF**) in `FieldGroups.php` + `acf-json/group_fp02_page_contacts.json`
- Passed through `contacts-helpers.php`; normalized in `yandex-map-embed.php` via `shpigovsky_set_yandex_constructor_scroll_param()` / `shpigovsky_normalize_yandex_constructor_embed()`
- Excluded `map_embed_code` from typography pipeline (`TypographyFilters.php`)

**Live QA:** 2 Yandex constructor scripts render on `/kontakty/` — **PASS**. Manual verify (`_04_verify_live.py`): script URLs contain `scroll=false` (WordPress emits `&#038;` in HTML — QA regex reported `missing`; functional output correct).

**Scroll ON path:** Not live-tested (would require reversible Admin toggle); implementation forces `scroll=true` when row toggle ON.

## 7. Scope boundaries (unchanged)

- Specialist URL migration / redirects — **not touched**
- Forms, SMTP, Metrika, anti-spam, indexing guard — **not touched**
- Robots.txt — **preserved** (SHA unchanged post-deploy)
- `blog_public=1` — **preserved**

## 8. Production deploy

Evidence: `03-deploy-manifest.json`, `04-post-deploy.json`, `02-php-lint.json`

| Metric | Value |
|--------|--------|
| Files deployed | 9 |
| Parity | **9/9** `parity_ok: true` |
| PHP lint | all **PASS** (on production host) |
| Post-deploy core | `0.3.29-specialists-nav-seo-maps-01` |
| Post-deploy `blog_public` | `1` |
| Cache | flushed |

Layer-B backups: `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-maint-specialists-nav-seo-maps-01\`

## 9. Live QA matrix

Evidence: `05-live-qa.json`

| Check | Result |
|-------|--------|
| Specialists hub — no breadcrumbs | **PASS** |
| `/o-centre/` — breadcrumbs present | **PASS** |
| Homepage SEO in source | **PASS** |
| Contacts SEO + maps | **PASS** |
| `/specyalisty/` → 301 `/specialisty/` | **PASS** |
| Robots preserved | **PASS** |
| Indexing OPEN | **PASS** |
| QA sample `/uslugi/lechenie-alkogolizma/` | **404** — wrong URL in script (intake sample: ID 1011 nested path) |
| QA sample `/politika-konfidencialnosti/` | **404** — privacy page null in intake |

## 10. Files changed (source)

| Path | Change |
|------|--------|
| `WORDPRESS/theme/shpigovsky/page-templates/specialists-hub.php` | Remove breadcrumbs call |
| `WORDPRESS/theme/shpigovsky/inc/seo-entity-meta.php` | Front/posts page SEO context |
| `WORDPRESS/theme/shpigovsky/inc/yandex-map-embed.php` | Scroll param normalization |
| `WORDPRESS/theme/shpigovsky/template-parts/contacts/location-card.php` | Live constructor embed |
| `WORDPRESS/theme/shpigovsky/inc/contacts-helpers.php` | Pass `map_scroll` |
| `WORDPRESS/plugins/shpigovsky-core/shpigovsky-core.php` | Version `0.3.29-specialists-nav-seo-maps-01` |
| `WORDPRESS/plugins/shpigovsky-core/src/Fields/FieldGroups.php` | `map_scroll` field |
| `WORDPRESS/plugins/shpigovsky-core/src/Typography/TypographyFilters.php` | Exclude embed code |
| `WORDPRESS/acf-json/group_fp02_page_contacts.json` | `map_scroll` JSON |

**DB:** No schema migration. Existing contacts map rows default `map_scroll=false` until Olya toggles in Admin.

## 11. Rollback

1. Restore Layer-B files from `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-maint-specialists-nav-seo-maps-01\`
2. Flush caches on production
3. ACF JSON sync if FieldGroups reverted (optional `map_scroll` column harmless if unused)

## 12. Git

Commit on `wave/fp0002-specialists-nav-seo-maps-01`, rebased onto `origin/mars/canonical-post-recovery`, pushed to `origin/mars/canonical-post-recovery` (selective staging only).

## 13. Residuals / follow-ups (non-blocking)

1. Update `_03_live_qa.py` service/legal URLs to intake-correct paths; handle `&#038;` in scroll param check
2. Optional: live verify `map_scroll=ON` with reversible Admin test
3. Olya may set SEO title/description on additional entity types now that front page path is fixed

## 14. Mutation statement

Bounded production maintenance only: specialists hub breadcrumb removal, SEO meta context fix for front/posts pages, contacts Yandex map embed restore + scroll toggle. No robots/indexing/SMTP/forms/Metrika/URL migration changes. WPilot writes OFF.
