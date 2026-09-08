# SITE-002-SEO-BLOG-CANONICAL-SITEMAP-GO1-PLAN-TO-BUILD-01

## 1. Scope

Build-only GO1 for SITE-002 (bzpm.ru) blog SEO:

- Add self-canonicals for blog hubs (`/blog`, `/blog/news`) and post pages.
- Add blog hub/theme/post URLs to `extension/feed/google_sitemap`.
- No production deploy, no Git commit/push, dirty main untouched.
- Category canonical/sitemap architecture deferred.
- Robots, header/footer.twig, pagination redesign out of scope.

## 2. Model routing

Composer / Grok only (as authorized). No premium/deep-reasoning model switch.

## 3. Operator GO

Operator authorized GO1 plan-to-build only:

- Clean worktree from remote tip `575a9c08c8f6563105aaae28a638821c020e84d7`
- Patch + local validation + deploy/git plans
- Explicitly **not** authorized: FTP PUT, DB write, cache clear, deploy, git add/commit/push, dirty-main mutation

## 4. No-deploy boundary

| Flag | Value |
|------|-------|
| production_write_allowed | false |
| db_write_allowed | false |
| ftp_write_allowed | false |
| cache_clear_allowed | false |
| deploy_allowed | false |
| git_commit_allowed | false |
| git_push_allowed | false |
| dirty_main_mutation_allowed | false |
| category_canonical_sitemap_architecture_allowed | false |
| robots_edit_allowed | false |
| header_footer_edit_allowed | false |

Evidence: Storage `manifests/operation.json`, `preflight/no-mutation-boundary.md`.

## 5. Deferred category canonical/sitemap architecture

Intentionally **not** touched:

- sitemap short URLs vs `/katalog/...` category canonical
- category canonical alignment
- catalog / blog pagination redesign
- robots.txt
- header.twig / footer.twig

## 6. Worktree

| Item | Value |
|------|-------|
| Path | `X:\AI MARS STORAGE\git-sync-site002-blog-seo-20260909-001235\repo` |
| Base | `origin/mars/canonical-post-recovery` @ `575a9c08c8f6563105aaae28a638821c020e84d7` |
| Mode | detached HEAD, clean at create |
| Dirty main | `X:\AI MARS` @ `75d8dbee…` — **untouched for this GO** |

## 7. Source discovery

No classic `.../patch/catalog/controller/blog/` tree on tip. Live-equivalent baselines are under `projects/ocpilot/sites/site-002/tools/`:

| Role | Tools baseline | Production path |
|------|----------------|-----------------|
| Blog category | `catalog_controller_blog_category-SITE-002-PROD-BRAND-CAPS-AND-BLOG-SLIDER-ORDER-01.php` | `/public_html/catalog/controller/blog/category.php` |
| Blog post | `catalog_controller_blog_post-SITE-002-PROD-BRAND-CAPS-AND-BLOG-SLIDER-ORDER-01.php` | `/public_html/catalog/controller/blog/post.php` |
| Google sitemap | `google_sitemap-site-002-prod-audit-wave-b-seo-foundation-01.php` | `/public_html/catalog/controller/extension/feed/google_sitemap.php` |
| Blog model (read-only) | `catalog_model_blog_blog-SITE-002-PROD-BRAND-CAPS-AND-BLOG-SLIDER-ORDER-01.php` | `catalog/model/blog/blog.php` |

Canonical via `$this->document->addLink(..., 'canonical')` — **no header.twig change required**.

Model filters: `active='1'` and `date_added <= NOW()` via `getCategories()` / `getPosts()`.

## 8. Baseline HTTP

### Hubs / non-routes

| URL | Status | Canonical | Robots |
|-----|--------|-----------|--------|
| `https://bzpm.ru/blog` | 200 | MISSING | index, follow |
| `https://bzpm.ru/blog/news` | 200 | MISSING | index, follow |
| `https://bzpm.ru/news` | 404 | — | — |
| `https://bzpm.ru/stati` | 404 | — | — |
| `https://bzpm.ru/articles` | 404 | — | — |

### Posts (6)

All HTTP 200, content present, `index, follow`, canonical **MISSING**, absent from sitemap:

1. `/blog/news/proizvoditelnost-truda-rck-altayskiy-kray-2026`
2. `/blog/news/oborudovanie-dlya-restoranov-kak-proektiruyut-kukhni-pod-format-zavedeniya`
3. `/blog/news/produkciya-zpm-podtverzhdena-sertifikatom-sdelano-v-rossii`
4. `/blog/news/obnovili-sajt-zpm-katalog-lichnyj-kabinet-poisk-i-oformlenie-zakaza-stali-udobnee`
5. `/blog/news/oborudovanie-dlya-obshchepita-kak-podobrat-osnashchenie-pod-zadachi-kukhni`
6. `/blog/news/oborudovanie-dlya-pishchevykh-proizvodstv-kak-podbirayut-resheniya-pod-processy-predpriyatiya`

### Sitemap

- `https://bzpm.ru/sitemap.xml` — 200
- total locs: **1861**
- blog locs: **0**
- hubs and 0/6 posts absent

## 9. Patch summary

Packaged under clean worktree:

`projects/ocpilot/sites/site-002/seo-blog-canonical-sitemap-go1-work/`

| File | Change |
|------|--------|
| `patch/catalog/controller/blog/category.php` | Theme + hub `addLink` self-canonical (no `?page=`) |
| `patch/catalog/controller/blog/post.php` | Post self-canonical via `blog/post` + `blog_post_id` |
| `patch/catalog/controller/extension/feed/google_sitemap.php` | Blog hub + `getCategories()` themes + `getPosts()` posts before `</urlset>` |

Tools GO1 mirrors (same content):

- `tools/catalog_controller_blog_category-SITE-002-SEO-BLOG-CANONICAL-SITEMAP-GO1-PLAN-TO-BUILD-01.php`
- `tools/catalog_controller_blog_post-SITE-002-SEO-BLOG-CANONICAL-SITEMAP-GO1-PLAN-TO-BUILD-01.php`
- `tools/google_sitemap-SITE-002-SEO-BLOG-CANONICAL-SITEMAP-GO1-PLAN-TO-BUILD-01.php`

Marker: `SITE-002-SEO-BLOG-CANONICAL-SITEMAP-GO1`

Canonical targets:

- Hub: `$this->url->link('blog/category')` → `/blog`
- Theme: `$this->url->link('blog/category', 'blog_category_id=' . $id)` → `/blog/news` (etc.)
- Post: `$this->url->link('blog/post', 'blog_post_id=' . $id)` → `/blog/news/{slug}`

Sitemap: no `/news|/stati|/articles`, no `?page=`, product/category branches preserved.

## 10. Validation

| Check | Result |
|-------|--------|
| PHP lint | **PHP_BINARY_UNAVAILABLE** — documented; no deploy in this GO |
| `addLink` canonical in category | PASS |
| `addLink` canonical in post | PASS |
| sitemap blog model + hub/theme/post | PASS |
| no `/news` `/stati` `/articles` in sitemap branch | PASS |
| no `/blog?page=` in sitemap | PASS |
| no robots/header/footer edits | PASS |
| git status | untracked GO1 work + 3 tools only; tracked tree clean |
| unexpected tracked diffs | none |

## 11. Later deploy plan

See Storage `deploy-plan/`:

1. Backup live: `category.php`, `post.php`, `google_sitemap.php` under `/public_html/catalog/controller/...`
2. FTP PUT the three patched files only
3. Prefer **no** cache clear first; OCMOD/mod cache only if proven necessary
4. Verify hubs, 6 posts, sitemap blog locs, product/category samples, no PHP warnings, no public «БЗПМ»
5. Rollback = restore three backups only

**Not executed in this GO.**

## 12. Later Git plan

Suggested message: `ocpilot: add SITE-002 blog canonical and sitemap URLs`

- Stage only allowlisted GO1 paths from clean worktree (never dirty main)
- Commit after deploy PASS (or per operator sequence)
- Push as separate wave

**Not executed in this GO.**

## 13. Risks

- Custom blog module (not PavBlog/Journal)
- Sitemap loc count will increase after deploy (~+1 hub + themes + published posts)
- Category canonical/sitemap architecture still deferred
- Phantom `?page=2` remains robots-only
- header/footer.twig protected
- robots.txt must not be edited in this wave
- PHP binary unavailable locally — lint deferred to deploy host or CI
- Dirty main diverged — commits must use clean worktree only

## 14. Storage artifacts

Root:

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-SEO-BLOG-CANONICAL-SITEMAP-GO1-PLAN-TO-BUILD-01\`

Subfolders populated: preflight, worktree, source-discovery, baseline-http, patch, validation, diff-review, deploy-plan, git-plan, risk-register, manifests, logs; this report under `reports/`.

## 15. Final verdict

**SITE-002 SEO BLOG CANONICAL SITEMAP GO1 BUILD COMPLETE — READY FOR DEPLOY DECISION**

- Patch built and statically validated in clean worktree
- Production untouched
- No Git commit/push
- Deploy and Git require separate operator GO
- Category canonical/sitemap architecture remains deferred
