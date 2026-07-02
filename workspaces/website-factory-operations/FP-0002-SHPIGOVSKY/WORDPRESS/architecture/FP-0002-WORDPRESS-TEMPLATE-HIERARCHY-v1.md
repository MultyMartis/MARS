# FP-0002 WordPress Template Hierarchy v1

**Task:** V9-06A | **Date:** 2026-07-03

---

## 1. Design principles

- One global header/footer via `header.php` / `footer.php` — never duplicated in page templates.
- Template parts carry section markup; templates orchestrate includes only.
- Prefer `single-service.php` + layout meta over per-slug PHP files.
- Page templates live in `page-templates/` with semantic names.

---

## 2. Root templates

| Template | Entity / family | Purpose | Required |
|----------|-----------------|---------|:--------:|
| `index.php` | fallback | Last-resort loop | yes |
| `front-page.php` | Home Page | V9 home sections | yes |
| `home.php` | Posts page | Blog archive `/blog/` | yes |
| `page.php` | generic Page | Safety fallback | yes |
| `single.php` | Post | Blog article | yes |
| `single-service.php` | `service` CPT | All service routes | yes |
| `404.php` | system | Not found | yes |
| `search.php` | system | Search (minimal) | defer |
| `archive.php` | fallback archive | Unused if archives disabled | optional |

**Not required:** `archive-service.php`, `taxonomy-service_category.php` (taxonomy rejected).

---

## 3. Page templates (`page-templates/`)

| File | Page family | Routes |
|------|-------------|--------|
| `services-hub.php` | Services hub | `/uslugi/` |
| `institutional.php` | O-centre | `/o-centre/` + children |
| `reviews.php` | Reviews | `/otzyvy/` |
| `contacts.php` | Contacts | `/kontakty/` |
| `legal.php` | Legal | 4 legal routes |

**Not separate files:** `page-about.php`, `page-contacts.php` as slug files — use semantic templates above.

---

## 4. Service template routing (`single-service.php`)

```text
single-service.php
  ├─ get_template_part by layout meta:
  │    subdivision → template-parts/service/subdivision-stack.php
  │    leaf        → template-parts/service/leaf-stack.php
  │    alcohol     → template-parts/service/alcohol-stack.php
  └─ placeholder variant when content_status=placeholder
```

| Layout meta | Variant | V9 reference |
|-------------|---------|--------------|
| `subdivision` | subdivision-stack | `usluga-podrazdel-v1.html` |
| `leaf` | leaf-stack | placeholder leaves |
| `alcohol-special` | alcohol-stack | `usluga-konechnaya-v1.html` |

---

## 5. Template-parts hierarchy

```text
template-parts/
  global/
    document-open.php
    document-close.php
  layout/
    head.php
    body-start.php
    header.php
    footer.php
    global-consultation-modal.php
  navigation/
    primary-desktop.php
    primary-mobile.php
    breadcrumbs.php
  components/
    scroll-to-top.php
    blog-archive-card.php
    review-archive-card.php
    program-cta-band.php
    internal-page-nav.php
  home/
    hero.php
    feature-grid.php
    treatment-prevention.php
    rehabilitation-program.php
    gallery.php
    articles-teaser.php
    faq.php
    final-form.php
  service/
    subdivision-stack.php
    leaf-stack.php
    alcohol-stack.php
    inner-hero.php
    intro.php
    signs.php
    approach.php
    stages.php
    program.php
    comfort.php
    faq.php
  page/
    placeholder-notice.php
    plain-content.php
  institutional/
    infrastructure-narrative.php
    institutional-narrative.php
  contacts/
    map-body.php
    rehabilitation-steps.php
  blog/
    archive-list.php
    article-content.php
    article-lower-stack.php
  legal/
    document-page.php
  reviews/
    archive-list.php
    reviews-section.php
```

---

## 6. Template selection matrix

| Condition | WordPress resolves |
|-----------|-------------------|
| `is_front_page()` | `front-page.php` |
| Posts page | `home.php` |
| `is_singular('post')` | `single.php` |
| `is_singular('service')` | `single-service.php` |
| Page with template `services-hub` | `page-templates/services-hub.php` |
| Page with template `institutional` | `page-templates/institutional.php` |
| Page with template `reviews` | `page-templates/reviews.php` |
| Page with template `contacts` | `page-templates/contacts.php` |
| Page with template `legal` | `page-templates/legal.php` |
| Other pages | `page.php` |

---

## 7. Shared includes (every public template)

1. `get_header()` → header.php → head + header partials  
2. Breadcrumbs (except home)  
3. Main content stack  
4. `get_footer()` → footer + modal + scroll-to-top  

---

## 8. Assets

Enqueued from `inc/assets.php` — V9 compiled CSS/JS from build pipeline, Swiper/Fancybox/Inputmask as V9 contract requires.

---

*Template files are not created in V9-06A.*
