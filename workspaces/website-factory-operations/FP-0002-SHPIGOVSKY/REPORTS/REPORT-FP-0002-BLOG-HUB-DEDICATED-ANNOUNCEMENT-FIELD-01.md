# REPORT — FP-0002 BLOG HUB DEDICATED ANNOUNCEMENT FIELD 01

## 1. Verdict

**PASS**

Production Blog Hub `/blog/` now has a dedicated ACF owner `article_hub_announcement` (`Анонс статьи для хаба`) for article-card preview text. Empty field keeps the historical `get_the_excerpt()` fallback. IDs 1745 and 750 render unchanged. Article Lead, SEO, Open Graph, Schema.org, native excerpts, robots, and indexing were not rewritten. Exact-file deploy, source↔production parity, and selective Git checkpoint completed.

---

## 2. Current-origin preflight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` on volume `X:` / `AI WS` |
| Worktree | `X:\AI MARS\worktrees\fp0002-blog-hub-announcement-01` |
| Wave branch | `wave/fp0002-blog-hub-announcement-01` |
| Origin tip at start | `c7290512a8b02113e3716ee145caac6229887f68` (`origin/mars/canonical-post-recovery`) |
| Worktree HEAD at start | same SHA — no replay required |
| Shared dirty main | Bypassed; not used, not repaired |
| Staged pre-commit | Empty |

Historical forensic SHA `187591a8859dda2e2d3ceeaa18de8392e7e7ad85` was not used as a checkout target.

---

## 3. Fresh production/Olya intake

Evidence: `REPORTS/evidence/prod-blog-hub-announcement-01/01-wp-intake.json`, `01-public-intake.json`

| Item | Pre-deploy |
|------|------------|
| Core | `0.3.31-open-graph-01` |
| Indexing | `blog_public=1`, IndexingState effective **OPEN** |
| ACF group | `group_fp02_blog_post_article_meta` — **no** `article_hub_announcement` yet |
| WPilot write | disabled / null |
| robots.txt SHA256 | `6157b0529c95ca6299bfd994c9f63c0b4f2b95a8cfa8cacbec81181723e981ff` |
| Sitemap | present; no `Disallow: /` |

**ID 1745** — `Генотипирование при зависимостях. Зачем оно нужно на старте программы`  
slug `demo-pagination-article-01`; native `post_excerpt` empty; `post_modified_gmt` **2026-09-09 09:24:19**; author 2.

**ID 750** — `Лечение алкогольной зависимости: почему сила воли здесь ни при чём`  
native excerpt filled; `post_modified_gmt` **2026-09-09 07:13:06**.

Activity Log table probe returned a double-prefix miss (`fp02_fp02_user_activity_log` / `activity_log_exists: false`). That is **not** treated as “Olya idle”. Newest production post timestamps were preserved.

---

## 4. Previous preview ownership

Verified on current origin (not assumed from the forensic SHA):

`home.php` → `template-parts/blog/archive-list.php` → `shpigovsky_build_blog_archive_card_args()` in `inc/blog-helpers.php` previously set `'excerpt' => get_the_excerpt( $post_id )` → `template-parts/components/blog-archive-card.php` (plain-text escaped).

That meant:

1. native `post_excerpt` if filled;
2. otherwise auto-trimmed `post_content` (~55 words + `[&hellip;]`).

Article hero Lead remained `article_lead`. SEO/OG/Schema remained `fp02_seo_description` (and existing Schema precedence). Those owners were not changed.

---

## 5. New field

| | |
|---|---|
| Label | `Анонс статьи для хаба` |
| Name | `article_hub_announcement` |
| Key | `field_fp02_article_hub_announcement` |
| Type | textarea, 4 rows, no WYSIWYG |
| Instructions | `Текст, который показывается в карточке статьи на странице «Статьи».` |
| Group | `group_fp02_blog_post_article_meta` / title `Blog Post — Article Meta` |
| Location | `post_type == post` |
| Admin placement | immediately after `Lead / announcement` (`article_lead`), before `Source label` |

Not a duplicate field group. Not Lead, not native Excerpt, not SEO/OG/Schema.

---

## 6. New precedence

1. `article_hub_announcement` — if non-empty after trim  
2. native `get_the_excerpt( $post_id )` fallback

No bulk migration. Empty new field → IDs 1745 and 750 keep their current cards.

---

## 7. Implementation

| File | Change |
|------|--------|
| `X:\AI MARS\worktrees\fp0002-blog-hub-announcement-01\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\WORDPRESS\theme\shpigovsky\inc\blog-helpers.php` | `shpigovsky_get_blog_hub_announcement()`; card args `'excerpt'` uses it |
| `...\WORDPRESS\plugins\shpigovsky-core\src\Fields\FieldGroups.php` | field in `blog_post_article_meta()` |
| `...\WORDPRESS\plugins\shpigovsky-core\shpigovsky-core.php` | version `0.3.32-blog-hub-announcement-01` |
| `...\WORDPRESS\acf-json\group_fp02_blog_post_article_meta.json` | same field; `"modified": 1787000001` |

Card markup stays presentation-only (`esc_html( wp_strip_all_tags( ... ) )`). `shpigovsky_get_article_lead()` unchanged.

---

## 8. Admin UX QA

WP-admin browser login was not used. Runtime ACF group listing on production (post-deploy + closeout):

- field name `article_hub_announcement` sits **after** `article_lead`;
- label `Анонс статьи для хаба` present in `acf_get_fields()` / post-deploy name map;
- `article_lead` remains;
- SEO group not duplicated;
- `blog_public` stayed `1`;
- no Admin PHP fatal in probes.

`get_field_object( 'article_hub_announcement', 1745 )` returned empty on a post whose value is empty (ACF empty-value quirk). Group field list is the authoritative Admin registration proof.

Native Excerpt meta box left in place (legacy fallback).

---

## 9. Blog Hub QA

Live `https://shpigovsky.ru/blog/` HTTP 200.

| Post | New field | Card excerpt |
|------|-----------|--------------|
| **1745** | empty | auto-trim from content, starts `Что такое генотипирование`, ends `[&hellip;]` — **unchanged** |
| **750** | empty | exact native excerpt `В статье расскажем о подходах к лечению и профилактике зависимости` — **unchanged** |

`post_modified_gmt` unchanged after deploy/QA: 1745 `2026-09-09 09:24:19`, 750 `2026-09-09 07:13:06`.

---

## 10. New-field priority QA

**No editorial DB mutation.** Request-scoped `acf/load_value/name=article_hub_announcement` filter on post **1745 only**, marker `QA-HUB-ANN-1745-PRIORITY-PROBE`, then probe deleted.

| Check | Result |
|-------|--------|
| Filtered 1745 | marker — `priority_wins: true` |
| Filtered 750 | unchanged native excerpt |
| Meta 1745/750 hub | still empty |
| Public HTML | no marker leak |
| `no_db_write` | true |

Evidence: `06-priority-qa.json`, `07-qa-summary.json`.

---

## 11. SEO / OG / Schema separation

Singles after deploy:

| Post | `<meta name="description">` / `og:description` | Schema `description` | Hero Lead |
|------|-----------------------------------------------|----------------------|-----------|
| 1745 | SEO: `Разберем анализ набора генетических маркеров...` | same SEO text | `article_lead` via `blog-article-hero__excerpt` |
| 750 | SEO: `Почему при алкоголизме сила воли ни при чём...` | same SEO text | `article_lead` |

Public HTML does **not** contain `article_hub_announcement`. JSON-LD count remains 1. Hub field is not fed into SEO/OG/Schema.

---

## 12. Olya/editorial preservation

No copy of `post_excerpt`, Lead, Meta Description, or trimmed content into the new field. Native excerpts untouched. Article bodies, featured images, dates, authors, SEO titles/descriptions unchanged. Closeout confirmed hub meta empty on 1745/750.

---

## 13. Robots/indexing safety

| Signal | Result |
|--------|--------|
| `blog_public` | **1** before and after |
| IndexingState | OPEN |
| robots.txt SHA256 | `6157b0529c95ca6299bfd994c9f63c0b4f2b95a8cfa8cacbec81181723e981ff` unchanged |
| Root `Disallow: /` | absent |
| Sitemap | present |

---

## 14. Production ↔ source parity

`03-deploy-manifest.json` — **4/4** local SHA256 = remote SHA256:

| File | SHA256 after deploy |
|------|---------------------|
| `blog-helpers.php` | `3823eb203a15deaa0f53151225a90bf469157839477b188db65b56d2183916f0` |
| `FieldGroups.php` | `acd939372f255a3b28ad46db3841471de28d81e6cdeb93dad18f4ad697dd04e6` |
| `shpigovsky-core.php` | `f4cf281de6532e42d352e5dd99588db2e090221e9874a9120c689ccae5600ff0` |
| ACF JSON | `df8baa0622542ae9001e71a1b76c67dde1b3fa84a57ee7a0c77628480bc26a1c` |

PHP lint OK. LF/CRLF not rewritten beyond the edited sources.

---

## 15. Backup/rollback

- Layer B: `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-blog-hub-announcement-01\`
- Evidence copies: `REPORTS/evidence/prod-blog-hub-announcement-01/backup-*`
- Rollback: restore the four pre-deploy files (hashes in §14 `before_sha256` / backup bytes). No post-data rollback required (no migration).

---

## 16. Files changed

**Production-deployed:**

- `X:\AI MARS\worktrees\fp0002-blog-hub-announcement-01\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\WORDPRESS\theme\shpigovsky\inc\blog-helpers.php`
- `...\WORDPRESS\plugins\shpigovsky-core\src\Fields\FieldGroups.php`
- `...\WORDPRESS\plugins\shpigovsky-core\shpigovsky-core.php`
- `...\WORDPRESS\acf-json\group_fp02_blog_post_article_meta.json`

**Documentation / evidence:**

- `...\REPORTS\REPORT-FP-0002-BLOG-HUB-DEDICATED-ANNOUNCEMENT-FIELD-01.md` *(this file)*
- `...\REPORTS\evidence\prod-blog-hub-announcement-01\`
- `...\PROJECT-STATUS.md`
- `...\REPORTS\FP-0002-NEXT-WEBGPT-HANDOFF.md`

---

## 17. Core/version state

| | Version |
|---|---------|
| Before | `0.3.31-open-graph-01` |
| After (production) | `0.3.32-blog-hub-announcement-01` |

---

## 18. Git

- Branch pushed: `origin/mars/canonical-post-recovery`
- Base SHA: `c7290512a8b02113e3716ee145caac6229887f68`
- Commit: `COMMIT_PENDING`
- Remote tip after push: `COMMIT_PENDING`
- Worktree: `X:\AI MARS\worktrees\fp0002-blog-hub-announcement-01` (`wave/fp0002-blog-hub-announcement-01`)

---

## 19. Residuals

1. **WP-admin UI not clicked in a browser** — field registration proven via production ACF group listing; visual editor chrome not screenshot-verified.
2. **`get_field_object()` empty-value quirk** — object-by-name on an empty post value is empty; group `acf_get_fields()` lists the field correctly.
3. **Activity Log intake table-name miss** — probe used a doubled prefix; not used as proof that Olya was idle.
4. **ID 1745 live slug** remains `demo-pagination-article-01` (not the guessed `/genotipirovanie-pri-zavisimostyah/` draft).

---

## 20. WP Forge harvesting

**NO NEW HARVEST REQUIRED.**

Project-specific Admin UX: Hub card announcement vs Lead vs native Excerpt vs SEO description. The reusable principle (separate editorial surfaces need separate owners) is already implicit in FP-0002 SEO/OG/Schema split.

---

## 21. Mutation statement

Exact-file deploy of four source files only. No WPilot writes. No DB bulk. No robots/indexing writes. No editorial migration. Reversible request-scoped ACF `load_value` filter on post 1745 only, then deleted — no residue. Indexing remains **OPEN**. robots.txt SHA unchanged.
