# FP-0002 V9 — href="#" Allowlist v1

## Allowed social/messenger placeholders

| Component | Label | Why | Future replacement | Forge |
|-----------|-------|-----|-------------------|-------|
| `site-header__messenger-link` | Telegram | No verified URL | Operator supplies messenger URL | Theme options / menu |
| `site-header__messenger-link` | WhatsApp | No verified URL | Operator supplies messenger URL | Theme options / menu |
| `offcanvas__messenger-link` | Telegram/WhatsApp/Max | No verified URL | Operator supplies URLs | Mobile menu config |
| `site-footer__social-link` | Telegram/WhatsApp/Max/YouTube | No verified URL | Operator supplies social URLs | Footer widget/options |
| `contacts-body__messenger-link` | Telegram/WhatsApp/Max | No verified URL | Operator supplies URLs | Contacts block |

## Allowed same-page anchors

| Component | Example | Classification |
|-----------|---------|----------------|
| `blog-article-content` TOC | `#alkogolizm-kak-bolezn-mozga` | SAME_PAGE_ANCHOR |

## Converted away from href="#" in V9-02

| Action | Final target |
|--------|--------------|
| Все статьи (home) | `/blog/` |
| Blog cards (home) | `/blog/nazvanie-stati/` |
| Все отзывы | `/otzyvy/` |
| Читать весь отзыв (home/archive) | non-link text (no detail route) |
| подробнее о доме | `/o-centre/galereya-o-dome/` |
| подробнее (program) | `/o-centre/programma-lecheniya/` |
| все специалисты | `/o-centre/` |
| Blog/reviews pagination | `<span>` prototype controls |

## Non-allowlisted href="#"

**Count after V9-02:** 0 navigation blockers (social/messenger + anchors only)
