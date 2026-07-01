# FP-0002 V8 — Blog Architecture v1

**Date:** 2026-07-01  
**Baseline:** `eb47ebb`  
**Fixture article:** `src/pages/blog/nazvanie-stati.html`

---

## 1. Overview

| Surface | Source page | Route (static) | Canonical URL |
|---------|-------------|----------------|---------------|
| Blog archive | `src/pages/blog.html` | `/blog.html` | `https://shpigovsky.ru/blog/` |
| Blog article | `src/pages/blog/nazvanie-stati.html` | `/blog/nazvanie-stati.html` | `https://shpigovsky.ru/blog/nazvanie-stati/` |

Both use one DOM for desktop and mobile; responsive behavior is SCSS-only.

---

## 2. Blog archive

### Structure

1. Breadcrumbs (Главная → Статьи)  
2. `blog-archive-list` — card grid  
3. `blog-lower-stack` — expert quote + program CTA  

### Card anatomy (`blog-archive-card.html`)

| Field | Source | WP |
|-------|--------|-----|
| Thumbnail | Param `imageSrc` | Featured image |
| Title | Param | Post title |
| Date | Param | Post date |
| Reading time | Param | Computed |
| Excerpt | Param | Post excerpt |
| Link | `articleHref` | Permalink |

### Desktop / mobile

- Desktop: multi-column grid  
- Mobile: stacked cards — same markup  

### Placeholder behavior

- Some card excerpts use **temporary placeholder copy** (acceptable for demo).  
- Pagination: **not implemented** — future WP query + paged archive.

### Relationship to home

- `home-articles.html` uses **similar card anatomy** but is a **separate section** — not the same partial file.  
- Teaser links may point at fixture slug.

### Shared vs not shared

| Shared | Not shared with article |
|--------|-------------------------|
| Header, footer, modal, CTA band | Article hero, TOC, body stream |
| Card visual language | `blog-expert-quote` (archive lower stack only) |

---

## 3. Blog article

### Page composition

```text
blog-article-content.html
  └── hero (breadcrumbs, layout, excerpt)
  └── blog-article-body (single content stream)
blog-article-lower-stack.html
  └── conclusion heading
  └── blog-article-founder-quote
  └── sources (8 items)
  └── related (3 cards)
  └── program-cta-band
```

### Unified hero

| Block | Class / element | WP ownership |
|-------|-----------------|--------------|
| Breadcrumbs | in hero | Template |
| Layout | `.blog-article-hero__layout` | Template shell |
| H1 | `.blog-article-hero__title` | Post title |
| Meta | date, reading time, author | Post fields |
| Featured image | `.blog-article-hero__media` | Post thumbnail |
| TOC | `.blog-article-hero__toc` | **Auto-generated from H2** |
| Excerpt | `.blog-article-hero__excerpt` | **Post excerpt — not body** |

### Mobile hero order

1. Featured image  
2. H1  
3. Meta (date · reading time · author)  
4. TOC  
5. Excerpt  

Implemented via CSS reordering on shared DOM.

### Fixture metadata

| Field | Value |
|-------|-------|
| Title | Лечение алкогольной зависимости: почему сила воли здесь ни при чём |
| Date | 05.05.2026 |
| Author | Шпиговский С.Ю. |
| Reading time | 5 минут на чтение |
| Slug | `nazvanie-stati` (demo placeholder) |

### Semantic TOC

**5 H2 anchors** (matches body):

1. `#alkogolizm-kak-bolezn-mozga`  
2. `#kto-na-samom-dele-pyuet`  
3. `#psihologicheskie-mehanizmy-zavisimosti`  
4. `#neyrobiologiya-i-psihologiya`  
5. `#statsionarnoe-lechenie`  

**WordPress rule:** Generate TOC from H2 in `the_content()` on save/render — editors must not maintain TOC manually.

### Body stream

| Metric | Count | Evidence |
|--------|-------|----------|
| H2 | 5 | `blog-article-content.html` |
| H3 | 12 | same |
| Inline images | 4 | `<figure><img>` in body |
| Streams | 1 | `.blog-article-body__content` |

**WordPress:** Entire hierarchy inside single `the_content()` — no chapter partials.

### Excerpt

Separate block with `.block-whith-red-line` — **not** part of `the_content()`.

### Conclusion + founder quote

- H2 «Заключение» in lower stack  
- `blog-article-founder-quote` — variant B anatomy  
- `.blog-article-conclusion-label` **absent** (by design)

### Sources

**8 source paragraphs** in `blog-article-sources` — template-managed / custom field; outside body stream.

### Related articles

**3 cards** (yoga, BOS, alcohol) — all link to placeholder `/blog/nazvanie-stati/`.

Query-driven in WordPress; exclude current post.

### CTA / footer

- `program-cta-band` with `ctaSource: blog-article-cta-01`  
- Shared site footer  

---

## 4. WordPress boundaries (summary)

| In `the_content()` | Outside body stream |
|--------------------|---------------------|
| H2, H3, paragraphs, inline figures | TOC shell (auto-filled) |
| | Excerpt block |
| | Founder quote block |
| | Sources |
| | Related posts |
| | CTA band |

**No** mobile-specific article content in editor.  
**No** chapter partial architecture in WordPress.

---

## 5. Deferred / placeholder

| Item | Status |
|------|--------|
| Related permalinks | Placeholder slug |
| Internal links in excerpt/body | Operator-noted TODOs |
| Pagination on archive | DEFERRED |
| Search | DEFERRED |
| Multiple live articles | Only one fixture in V8 |

---

## 6. Related documents

- [FP-0002-V8-WORDPRESS-READY-BASELINE-v1.md](FP-0002-V8-WORDPRESS-READY-BASELINE-v1.md)  
- [FP-0002-V8-FORGE-WORDPRESS-HANDOFF-MAP-v1.md](FP-0002-V8-FORGE-WORDPRESS-HANDOFF-MAP-v1.md)

---

*Blog architecture — reconciled to V8 source.*
