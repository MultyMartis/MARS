# REPORT — SITE-002 Blog Publish Datetime Readtime 01

**Operation ID:** `SITE-002-PROD-BLOG-PUBLISH-DATETIME-READTIME-01`  
**OCPilot Run:** **4.272**  
**Date:** 2026-07-16 (UTC evening 2026-07-15)  
**Environment:** PRODUCTION (`https://bzpm.ru/`)  
**Authority worktree:** `X:\AI MARS STORAGE\git-sync-e01\repo` @ `5727a8f3`  
**Dirty main:** untouched  

**Verdict:** `SITE-002 BLOG PUBLISH DATETIME READTIME COMPLETE — ADMIN DATETIME AND READING TIME LIVE`

---

## 1. Scope

Admin publish datetime UI + automatic reading-time storage/display for custom blog, without changing post 13 content/images/slug/schedule or autopublish gate semantics.

## 2. Operator request

1. Admin date+time picker for article publish datetime (not date-only text).
2. Keep `date_added <= NOW()` autopublish model.
3. Keep post 13 at Barnaul `16.07.2026 07:00` / MySQL `2026-07-16 03:00:00`.
4. Auto-calc reading time on save.
5. Show reading time in `.blog-list__item__meta` and `.blog-item__meta`.
6. Russian pluralization: `Время на чтение: N минут.`

## 3. Preflight

| Check | Result |
|-------|--------|
| Volume `X:` label | `AI WS` |
| Authority HEAD | `5727a8f3` = `origin/mars/canonical-post-recovery` |
| Dirty main | diverged foreign WIP — **no mutation** |
| Storage operation root | created |

Artifacts: `preflight/authority-git.txt`, `preflight/dirty-main-readonly.txt`, `manifests/operation.json`.

## 4. Blog admin discovery

| Role | Path |
|------|------|
| Controller | `admin/controller/blog/posts.php` |
| Model | `admin/model/blog/blog.php` |
| Form | `admin/view/template/blog/posts_form.twig` |
| List | `admin/view/template/blog/posts_list.twig` |
| Language | `admin/language/ru-ru/blog/posts.php` |

Before: field `modified` was plain text date `d.m.Y` (time truncated on edit display). Save already used `strtotime` → `Y-m-d H:i:s`.

Datetime convention taken from product form: `.datetime` + `YYYY-MM-DD HH:mm` + bootstrap-datetimepicker.

## 5. Blog frontend discovery

| Role | Path |
|------|------|
| List controller/template | `catalog/controller/blog/category.php` + `.../blog/category.twig` |
| Detail controller/template | `catalog/controller/blog/post.php` + `.../blog/post.twig` |
| Autopublish model | `catalog/model/blog/blog.php` (`active=1 AND date_added <= NOW()`) — **unchanged** |

Meta before: Rubric / Date / Views only.

## 6. DB schema before

`oc_blog_posts` columns: id, category_id, title, short_description, content, image, views, active, meta_*, date_added.  
No reading_time field.  
`date_added` type: `datetime`.  
Post 13 before: `date_added=2026-07-16 03:00:00`, image `catalog/blog/rck-productivity-hero-zpm-2026.jpg`.

## 7. Publish datetime UI decision

- Keep DB field `date_added`.
- Keep POST name `modified` for compatibility.
- Admin UI format: `YYYY-MM-DD HH:mm` (seconds forced to `:00` on save).
- Label/help: site/MySQL time; used for deferred publish.
- No Barnaul auto-conversion in admin (storage remains site/Moscow).

## 8. Reading time decision and formula

- Column: `reading_time_minutes TINYINT UNSIGNED NOT NULL DEFAULT 1`
- Constant: **1500** Unicode characters / minute
- Algorithm: strip HTML/scripts/styles → decode entities → normalize whitespace → `mb_strlen` → `max(1, ceil(chars/1500))`
- Store on save; frontend uses stored value + pluralization helper

## 9. DB migration/backfill

```sql
ALTER TABLE oc_blog_posts
  ADD COLUMN reading_time_minutes TINYINT UNSIGNED NOT NULL DEFAULT 1
  AFTER content;
```

Backfill: 6 posts (ids 8–13). Post 13 → **2** minutes. Date guard preserved.

## 10. Admin source patch

Patched/uploaded:

1. `admin/controller/blog/posts.php` — datetimepicker assets; `Y-m-d H:i` display; reading_time for form
2. `admin/model/blog/blog.php` — normalize datetime + calculate/store reading_time
3. `admin/view/template/blog/posts_form.twig` — datetime UI + help + read-only minutes
4. `admin/language/ru-ru/blog/posts.php` — language keys

## 11. Frontend source patch

1. `catalog/controller/blog/category.php` — `reading_time_text`
2. `catalog/controller/blog/post.php` — `reading_time_text`
3. `catalog/view/theme/default/template/blog/category.twig` — meta reading-time block
4. `catalog/view/theme/default/template/blog/post.twig` — meta reading-time block

Autopublish model file **not** changed in this run.

## 12. Production apply

- FTP uploads: **8** exact blog source files (controller/model/twig/language), all sha256-verified; admin controller re-upload after `$post_info` init fix
- DB schema: **1** column add
- DB row updates: **6** reading_time backfills (post 13 date-guarded)
- Cache: cleared `storage/cache` files under `/home/a/assum/bzpm.ru/storage/cache` (98 → 0)

## 13. Admin verification

| Check | Result |
|-------|--------|
| Post 13 `date_added` | `2026-07-16 03:00:00` unchanged |
| Hero image | `catalog/blog/rck-productivity-hero-zpm-2026.jpg` |
| Logo in content | present (`rck-logo-altay-2026.png`) |
| `reading_time_minutes` | `2` |
| Admin UI save | not required (backfill + source patch); form source verified deployed |

## 14. Frontend verification

| URL | Status | Reading time |
|-----|--------|--------------|
| `/blog` | 200 | `Время на чтение: 4 минуты.` |
| `/blog/news` | 200 | `Время на чтение: 4 минуты.` |
| post 13 SEO URL | **404** | hidden (pre-publish) |
| published detail sample | 200 | `Время на чтение: 4 минуты.` |

Post 13 gate: `date_added <= NOW()` = **0** (not published early).

## 15. Regression check

`/`, `/contact`, premium shelving PLP, `/sitemap.xml` → 200; public `БЗПМ` = 0; no HTTP 500.

## 16. Production mutation summary

| Channel | Count / note |
|---------|----------------|
| FTP files changed | **8** blog admin/catalog source files |
| DB schema changes | **1** (`reading_time_minutes`) |
| DB row updates | **6** reading_time backfill |
| Admin saves | **0** |
| Import runs | **0** |
| Scheduler changes | **0** |
| Monitor changes | **0** |
| Form/mail changes | **0** |
| Recipient changes | **0** |
| Dirty main mutation | **0** |

## 17. DB mutation summary

- `ALTER TABLE oc_blog_posts ADD COLUMN reading_time_minutes ...`
- `UPDATE oc_blog_posts SET reading_time_minutes=N` for ids 8–13
- Post 13 date/image/content/slug: **unchanged**

## 18. FTP mutation summary

Exact paths under `/public_html/`:

- `admin/controller/blog/posts.php`
- `admin/model/blog/blog.php`
- `admin/view/template/blog/posts_form.twig`
- `admin/language/ru-ru/blog/posts.php`
- `catalog/controller/blog/category.php`
- `catalog/controller/blog/post.php`
- `catalog/view/theme/default/template/blog/category.twig`
- `catalog/view/theme/default/template/blog/post.twig`

## 19. Git/worktree summary

- Authority worktree used for docs/mirrors/commit
- Dirty main ignored
- Repo mirrors under `projects/ocpilot/sites/site-002/tools/`

## 20. Storage artifacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-BLOG-PUBLISH-DATETIME-READTIME-01\`

## 21. SAFE UNKNOWN / blockers

- Full browser login to OpenCart admin form not executed in this run; datetime UI verified via deployed source + product-form convention. Operator visual confirm of post 13 edit screen recommended.
- Home page does not use `.blog-list__item__meta` cards (reading time N/A there).

## 22. Final verdict

`SITE-002 BLOG PUBLISH DATETIME READTIME COMPLETE — ADMIN DATETIME AND READING TIME LIVE`

## 23. Next recommendation

After Barnaul **2026-07-16 07:00**, verify post 13 becomes 200 and shows `Время на чтение: 2 минуты.` in list + detail. Optionally open admin edit of post 13 and confirm datetime picker shows `2026-07-16 03:00` without saving unless needed.
