# REPORT — FP-0002 GLOBAL OPEN GRAPH META 01

## 1. Verdict

**PASS_WITH_ATTENTION**

Open Graph is live on production via a single `shpigovsky-core` owner; all 12 sampled public surfaces pass raw-source QA; SEO title/description plumbing and JSON-LD remain healthy; robots/indexing unchanged. Attention: many inner pages omit `og:description` because Admin meta description is empty (correct per spec — not fabricated); authenticated Facebook/Meta OG debugger not run in this session.

---

## 2. Current-origin preflight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` on volume `X:` / `AI WS` |
| Worktree | `X:\AI MARS\worktrees\fp0002-open-graph-01` |
| Wave branch | `wave/fp0002-open-graph-01` |
| Remote SHA (preflight + post-fetch) | `d60e50725a76e45d07ff7d6959fc06501387dd8b` |
| Foreign WIP | Main repo dirty — bypassed via clean worktree |
| Staged pre-commit | Empty |

---

## 3. Fresh production / Olya intake

- **Core before:** `0.3.30-yandex-schema-org-01`
- **Core after:** `0.3.31-open-graph-01` (server probe)
- **Indexing:** `blog_public=1` — **OPEN**, unchanged
- **robots.txt** pre/post SHA256: `6157b0529c95ca6299bfd994c9f63c0b4f2b95a8cfa8cacbec81181723e981ff` — **unchanged**
- **Pre-deploy OG:** **0** `og:*` tags on homepage sample; no competing plugin/theme OG owner detected
- **Pre-deploy JSON-LD:** **1** script on homepage — preserved post-deploy
- **Homepage SEO:** Admin SEO title + meta description present and unchanged editorially

Evidence: `REPORTS/evidence/prod-open-graph-01/01-intake.json`, `04-post-deploy.json`

---

## 4. Existing Open Graph audit

Pre-deploy production `<head>` on `https://shpigovsky.ru/`:

| Owner | `<title>` | `<meta name="description">` | JSON-LD | OG | Twitter |
|-------|-----------|------------------------------|---------|-----|---------|
| Theme `seo-entity-meta.php` | yes | yes (`wp_head` @3) | — | — | — |
| Core `StructuredData` | — | — | yes (@6) | — | — |
| Core `OpenGraph` | — | — | — | **absent** | absent |

No Yoast/RankMath/social-plugin OG output found. Greenfield OG layer added without duplicate-owner conflict.

---

## 5. Open Graph architecture

```
WordPress request
  → RequestContext (URL, type, locale, emit gate)
  → TagBuilder (title, description, site_name, article times)
  → ImageResolver (page-aware image via theme helpers)
  → OpenGraph::render_meta_tags()
  → <meta property="og:*"> in wp_head @ priority 4
```

**Hook order:** SEO meta description @3 → **Open Graph @4** → JSON-LD @6.

Module id: `open-graph.meta` in `shpigovsky-core` `ModuleRegistry`.

---

## 6. Data ownership and precedence

| Field | Precedence |
|-------|------------|
| **og:title** | Admin SEO title (`fp02_seo_title`) → entity/page title → document title / org name (homepage) |
| **og:description** | Admin meta description (`fp02_seo_description`) only; **omit** if empty |
| **og:url** | Canonical permalink (`untrailingslashit`, absolute HTTPS); never deprecated `/specyalisty/` |
| **og:type** | `article` for `post`; `website` for all other public surfaces |
| **og:site_name** | `DataReaders::organization_name()` |
| **og:locale** | `get_locale()` mapped to OG locale (e.g. `ru_RU`) when available |
| **og:image** | Entity-aware resolver (see §8); omit rather than invent |

No manual OG textarea fields added. Olya continues editing existing SEO fields only.

---

## 7. Public entity/template coverage

| Type/template | og:type | title source | description source | image source | result |
|---------------|---------|--------------|-------------------|--------------|--------|
| Homepage | website | Admin SEO title | Admin meta description | home hero helper | PASS |
| Contacts | website | Admin SEO / page title | Admin meta description | institutional hero | PASS |
| Services hub | website | page title | omit (empty SEO desc) | services hub hero | PASS |
| Service single | website | service title | omit | service hero helper | PASS |
| Specialists hub | website | page title | omit | institutional hero fallback | PASS |
| Specialist single | website | specialist name | omit | featured portrait only | PASS |
| Article (post) | article | post title | omit | featured image only | PASS |
| About / institutional | website | page title | omit | institutional hero | PASS |
| Reviews | website | page title | omit | institutional hero | PASS |
| Legal (privacy) | website | page title | omit | institutional hero | PASS |
| Generic institutional | website | page title | omit | institutional hero | PASS |
| Deprecated `/specyalisty/` redirect | website | hub title | omit | hub image | PASS (og:url = `/specialisty`) |

---

## 8. Image selection architecture

`ImageResolver` routes by template/CPT using existing theme helpers:

1. Homepage → `shpigovsky_get_home_hero_image()` (or equivalent home hero owner)
2. Services hub / service single → services hero helpers
3. Specialist single → featured image thumbnail only (no placeholder SVG)
4. Article → featured image only (no blog fallback card)
5. Institutional/contacts/hub/legal/reviews → institutional hero when applicable
6. Otherwise → omit `og:image`

Dimensions/alt emitted only when WordPress attachment metadata provides them — not fabricated.

---

## 9. Article-specific Open Graph

For `post` type:

- `og:type=article`
- `article:published_time` and `article:modified_time` from actual WordPress post dates (GMT ISO-8601)
- No fabricated author/profile URLs; no category/tag article meta in this wave

Verified on `https://shpigovsky.ru/blog/nazvanie-stati/`: `article:published_time` present; `og:locale` present.

---

## 10. Implementation

**Plugin:** `shpigovsky-core` @ `0.3.31-open-graph-01`

| File | Role |
|------|------|
| `shpigovsky-core.php` | Version bump; module bootstrap |
| `src/ModuleRegistry.php` | Register `open-graph.meta` |
| `src/OpenGraph/OpenGraph.php` | `wp_head` renderer + escaping |
| `src/OpenGraph/TagBuilder.php` | Normalized OG model + precedence |
| `src/OpenGraph/ImageResolver.php` | Page-aware image selection |
| `src/OpenGraph/RequestContext.php` | URL/type/locale/canonical context |

**Not touched:** `src/StructuredData/*`, theme templates, robots, indexing modules, Yandex Maps embeds.

---

## 11. Live raw-source QA matrix

Evidence: `REPORTS/evidence/prod-open-graph-01/05-qa-matrix.json`

| URL | og:title | og:description | og:url | og:type | og:image | dupes | result |
|-----|----------|----------------|--------|---------|----------|-------|--------|
| `/` | Admin SEO title | Admin meta desc | `https://shpigovsky.ru` | website | uploads hero | all 1 | PASS |
| `/kontakty/` | Contacts SEO title | Admin meta desc | `.../kontakty` | website | o-centre hero | all 1 | PASS |
| `/uslugi/` | Услуги | *(omit)* | `.../uslugi` | website | services hero | all ≤1 | PASS |
| `/uslugi/.../lechenie-alkogolnoy-zavisimosti/` | service title | *(omit)* | canonical service URL | website | service hero | all ≤1 | PASS |
| `/specialisty/` | Специалисты | *(omit)* | `.../specialisty` | website | institutional hero | all ≤1 | PASS |
| `/specialisty/shpigovsky/` | specialist name | *(omit)* | canonical specialist URL | website | portrait webp | all ≤1 | PASS |
| `/blog/nazvanie-stati/` | post title | *(omit)* | canonical post URL | **article** | featured image | all ≤1 | PASS |
| `/o-centre/o-nas/` | О нас | *(omit)* | canonical | website | institutional hero | all ≤1 | PASS |
| `/otzyvy/` | Отзывы | *(omit)* | canonical | website | institutional hero | all ≤1 | PASS |
| `/privacy-policy/` | legal title | *(omit)* | canonical | website | institutional hero | all ≤1 | PASS |
| `/o-centre/programma-lecheniya/` | page title | *(omit)* | canonical | website | institutional hero | all ≤1 | PASS |
| `/specyalisty/` (301) | hub title | *(omit)* | **`/specialisty`** | website | hub image | all ≤1 | PASS |

**JSON-LD count:** 1 on every sampled URL. **No** `specyalisty` in any `og:url`.

---

## 12. Homepage SEO → OG verification

| Output | Value source | Match |
|--------|--------------|-------|
| `<title>` | Admin SEO title | yes |
| `<meta name="description">` | Admin meta description | yes |
| `og:title` | same SEO title pipeline | yes (semantic match after entity decode) |
| `og:description` | same meta description pipeline | yes |

---

## 13. Specialists URL verification

- Hub canonical: `https://shpigovsky.ru/specialisty/` → `og:url=https://shpigovsky.ru/specialisty`
- Single example: `https://shpigovsky.ru/specialisty/shpigovsky/`
- Deprecated `/specyalisty/` redirect final URL uses canonical `/specialisty/` in OG — **no deprecated spelling in og:url**

---

## 14. Schema.org separation/regression QA

- Module `structured-data.schema-org` unchanged
- Post-deploy: **1** JSON-LD script per sampled page
- No duplicate schema scripts
- OG module does not read or mutate JSON-LD graph
- Independent hook priorities and builders

---

## 15. Contacts/Yandex Maps regression QA

Spot-check on `/kontakty/`:

- Yandex map embed references present in HTML
- `scroll=false` behavior preserved (count 2 in source probe)
- JSON-LD count = 1
- OG tags added without layout/map regression

---

## 16. Robots / indexing safety

| Check | Result |
|-------|--------|
| robots.txt SHA pre | `6157b052...` |
| robots.txt SHA post | `6157b052...` (**unchanged**) |
| `blog_public` | 1 (OPEN) |
| P18G guard | not modified |
| Indexing close | **not performed** |

---

## 17. Production ↔ source parity

Deploy manifest: `REPORTS/evidence/prod-open-graph-01/03-deploy-manifest.json`

**6/6** deployed plugin files — local SHA256 = remote SHA256 after upload.

Layer B rollback: `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-open-graph-01\`

---

## 18. Backup / rollback

- Pre-deploy Layer B backup of exact touched plugin files under `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-open-graph-01\`
- Rollback: restore previous 6 files + revert `ModuleRegistry.php` / plugin version; disable module via registry if needed
- No DB migration; no editorial DB writes required

---

## 19. Files changed

**Core plugin (production-deployed):**

- `X:\AI MARS\worktrees\fp0002-open-graph-01\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\WORDPRESS\plugins\shpigovsky-core\shpigovsky-core.php`
- `...\src\ModuleRegistry.php`
- `...\src\OpenGraph\OpenGraph.php` *(new)*
- `...\src\OpenGraph\TagBuilder.php` *(new)*
- `...\src\OpenGraph\ImageResolver.php` *(new)*
- `...\src\OpenGraph\RequestContext.php` *(new)*

**Documentation / evidence:**

- `...\REPORTS\REPORT-FP-0002-GLOBAL-OPEN-GRAPH-META-01.md` *(this file)*
- `...\REPORTS\evidence\prod-open-graph-01\` *(intake, deploy, QA scripts + JSON)*
- `...\PROJECT-STATUS.md`
- `...\REPORTS\FP-0002-NEXT-WEBGPT-HANDOFF.md`

---

## 20. Core/version state

| | Version |
|---|---------|
| Before | `0.3.30-yandex-schema-org-01` |
| After (production) | `0.3.31-open-graph-01` |
| Schema module | enabled |
| OG module | enabled |

---

## 21. Git

- Branch pushed: `origin/mars/canonical-post-recovery`
- Base SHA: `d60e50725a76e45d07ff7d6959fc06501387dd8b`
- Commit: `9fe3790aceba040d8e0c0d307a65bd5980d87f01`
- Remote tip after push: `9fe3790aceba040d8e0c0d307a65bd5980d87f01`
- Worktree: `X:\AI MARS\worktrees\fp0002-open-graph-01` (wave branch `wave/fp0002-open-graph-01`; canonical checked out in main repo)

---

## 22. Residuals

1. **og:description sparse on inner pages** — many pages have no Admin meta description; OG correctly omits rather than fabricates. Operator may add SEO descriptions over time; OG will follow automatically.
2. **External OG debugger** — Facebook/Meta Sharing Debugger not run (auth/UI); authoritative check is server-rendered raw HTML (PASS).
3. **og:url trailing slash** — uses `untrailingslashit` pattern aligned with Schema.org canonical URLs (no trailing slash on non-home paths).

---

## 23. WP Forge harvesting

**NO NEW HARVEST REQUIRED.**

Pattern already established in Schema.org wave: single editorial SEO truth → separate output consumers (SEO meta, OG, JSON-LD). OG wave confirms the same architecture for social/link-preview layer.

---

## 24. Mutation statement

This wave **added** a new `open-graph.meta` module to `shpigovsky-core`, bumped plugin version to `0.3.31-open-graph-01`, and deployed **6 exact plugin files** to production. **No** robots, indexing, Schema.org logic, theme presentation, Yandex Maps, or editorial DB content was mutated. Olya production state preserved as truth.
