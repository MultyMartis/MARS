# FP-0002 WordPress Admin UX Model v1

**Task:** V9-06A | **Date:** 2026-07-03

---

## 1. Admin navigation map

| Admin section | Content | Editor persona |
|---------------|---------|----------------|
| **Консоль** | Dashboard | Admin |
| **Страницы** | Home (as front), hub, institutional, contacts, reviews, legal | Content editor |
| **Услуги** | Service catalogue (CPT) | Content editor |
| **Записи** | Blog articles | Content editor |
| **Медиафайлы** | Images, PDFs | Content editor |
| **Внешний вид → Меню** | Primary, footer columns, legal | Admin |
| **Настройки → Общие** | Site title (native) | Admin |
| **Настройки → Чтение** | Front page, posts page | Admin |
| **Настройки сайта** (ACF options) | Phones, address, socials, modal defaults | Admin |

**Hidden / restricted:** Comments, Tools clutter, block editor flexible layouts, unrelated post formats.

---

## 2. Page workflows

### Home (front page)

| Field | Visible | Required |
|-------|:-------:|:--------:|
| Title | yes | yes |
| Slug | admin only | yes (`glavnaya`) |
| Block editor | **hidden** | — |
| Home ACF groups | yes | partial |
| Featured image | no | — |

Sections: hero slides, grids, FAQ, CTA — bounded fields only.

### Services hub (`/uslugi/`)

| Field | Visible |
|-------|:-------:|
| Title | yes |
| Parent | no |
| Services hub ACF | yes |
| Native editor | hidden |

### Institutional pages

| Page | Template | Editor |
|------|----------|--------|
| O-centre hub | institutional | Full ACF G0–G5 |
| Children | institutional | Placeholder notice + minimal fields until content |

### Contacts

| Field | Visible |
|-------|:-------:|
| Contacts ACF (map, methods, steps) | yes |
| Native editor | hidden |

### Reviews

| Field | Visible |
|-------|:-------:|
| Reviews repeater | yes |
| Requirements band | yes |

### Legal

| Field | Visible |
|-------|:-------:|
| Native content | yes (controlled HTML) |
| Legal meta (version, date) | yes |
| DEMO banner | code-owned notice in admin |

---

## 3. Service workflow (`Услуги`)

| Field | Visible | Notes |
|-------|:-------:|-------|
| Title | yes | H1 source |
| Slug | yes | Must match V9 path segment |
| Parent | yes | Hierarchy |
| Order | optional | Menu order fallback only |
| Layout meta | yes | subdivision / leaf / alcohol-special |
| Excerpt | yes | Cards, teasers |
| Featured image | yes | Hero fallback |
| Native editor | **hidden** for structured layouts | Placeholder may allow minimal |
| Service ACF groups | yes | By layout |

**Editorial flow:**

1. Create subdivision service (parent = none).
2. Create leaf services under subdivision.
3. Assign layout variant; fill bounded sections.
4. Publish when content approved (placeholders may remain draft).

---

## 4. Blog workflow

| Field | Visible |
|-------|:-------:|
| Title, slug | yes |
| Content | yes — primary article body |
| Excerpt | yes |
| Featured image | yes |
| Categories | optional (defer) |
| Tags | **hidden** (default off) |
| Author/date | configurable visibility |
| Blog post ACF | sources, related, quote |

Posts page (`blog`): title only; archive layout from theme.

---

## 5. Global settings

**ACF Options page «Настройки сайта»:**

- Phones, email, address, hours
- Social links
- Modal default labels
- Footer legal entity (DEMO flagged)

**Not in options:** page bodies, service copy, secrets, analytics IDs (env).

---

## 6. Hidden / restricted controls

| Control | Action |
|---------|--------|
| Gutenberg block library on structured pages | Remove editor support |
| Custom fields meta box (native) | Hide when ACF active |
| Tags | Disable |
| Service CPT archive UI | N/A — no archive |
| Flexible content | Not registered |

---

## 7. Validation behavior

- Required: title, slug, parent (for child services), layout meta.
- Placeholder services: allow publish with notice meta for staging.
- Legal pages: block publish to production index until operator clears DEMO tokens.
- Phone/email in options: format validation in ACF.

---

*Admin customizations not implemented in V9-06A.*
