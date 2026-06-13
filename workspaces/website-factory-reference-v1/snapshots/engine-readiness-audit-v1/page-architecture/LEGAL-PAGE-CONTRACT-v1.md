# Website Factory — Legal Page Contract v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/page-architecture/`  
**Статус:** специализация `LEGAL_PAGE` для Page Architecture layer — **documentation only**  
**Связь:** [LEGAL-IMPLEMENTATION-RULES.md](../legal/LEGAL-IMPLEMENTATION-RULES.md), [LEGAL-GENERATION-CONTRACT-v1.md](../legal/LEGAL-GENERATION-CONTRACT-v1.md), [LEGAL-PACK-v1-FREEZE.md](../legal/LEGAL-PACK-v1-FREEZE.md)

**Запрет:** не изменять Legal Pack templates, Legal Entity Discovery docs, Triumph workspace.

---

## Назначение

Формализует архитектурные уроки Triumph и Legal Pack v1 freeze на уровне **page contract** для `LEGAL_PAGE`. Юридические страницы — **часть проекта**, не отдельный микросайт.

---

## Page contract defaults (`LEGAL_PAGE`)

| Field | Value |
|-------|-------|
| `page_type` | `LEGAL_PAGE` |
| `page_role` | `LEGAL` |
| `page_goal` | Опубликовать один канонический legal document (L1–L4) с корректными URL, H1, переменными |
| `required_blocks` | **none** (marketing blocks forbidden on legal routes) |
| `optional_blocks` | Project shell only: site header nav, `FOOTER` with `LEGAL_LINKS` |
| `forbidden_blocks` | `HERO`, `LEAD_FORM`, `PRICING`, `CTA`, `PRODUCT_GRID`, `CART`, `CHECKOUT`, campaign blocks |
| `legal_requirements` | Legal Pack v1 + Generation Contract + Footer Rule |
| `seo_requirements` | Indexable utility/legal URLs; no duplicate H1 across L1–L4 |
| `conversion_requirements` | **none** — no primary CTA on legal body |
| `dependencies` | Legal Pack FROZEN; Entity Card READY; canonical URL slot |

---

## Design inheritance (Triumph / Legal Pack lessons)

Юридические страницы **наследуют дизайн проекта**. Отдельная legal design system **запрещена**.

| Principle | Rule |
|-----------|------|
| **Project design** | Legal pages use the same site shell, theme (light/dark), and nav patterns as marketing pages |
| **Content container** | Legal body in **project content container** (`section-shell` / page template) at **full working width** of that container |
| **Typography** | **Project content-page typography** — `.content-page` (or equivalent reusable layer) for semantic body tags |
| **No legal-only design language** | **Forbidden:** isolated legal font stack, legal-only `max-width` column, per-tag legal font-size overrides |
| **Content-page layer** | If project lacks `.content-page`, Factory **creates** reusable project-level typography **before** legal shell — **not** legal-only typography |
| **Semantic HTML** | Body: `h1`, `h2`, `h3`, `p`, `ul`, `ol`, `li`, `a`, `table`, `thead`, `tbody`, `tr`, `th`, `td` |
| **Shell scope** | Shell may set layout, spacing, nav, table overflow, theme **color** — **not** per-tag typography overrides in legal body |
| **Generator discipline** | No visual utility classes in legal body except project wrapper hooks (shell body, table overflow wrap) |

**Source of truth (unchanged):** [LEGAL-IMPLEMENTATION-RULES.md](../legal/LEGAL-IMPLEMENTATION-RULES.md) §9 Legal Content Layout Rule; [LEGAL-GENERATION-CONTRACT-v1.md](../legal/LEGAL-GENERATION-CONTRACT-v1.md) Phase 3 layout validation.

**Reference implementation (partial):** `src/scss/components/_content-page.scss`, `src/scss/sections/_legal-pages.scss` in `website-factory-reference-v1/`.

---

## Canonical URLs (immutable)

| Document | Canonical URL | H1 (link text = H1) |
|----------|---------------|---------------------|
| L1 Privacy | `/privacy-policy/` | Политика конфиденциальности |
| L2 Consent PD | `/consent-personal-data/` | Согласие на обработку персональных данных |
| L3 User Agreement | `/user-agreement/` | Пользовательское соглашение |
| L4 Cookie | `/cookie-files-policy/` | Политика Cookie-файлов |

**Rules:**

- URLs **не подлежат замене**
- Footer link text **must match** H1
- Content template **starts** with matching `#` H1 in Markdown source

---

## Per-slot page contracts

### L1 — Privacy Policy

| Attribute | Value |
|-----------|-------|
| `canonical_url` | `/privacy-policy/` |
| Template | `legal/privacy-policy-template.md` |
| Consent Rule | Linked from forms (not on this page body) |

### L2 — Consent Personal Data

| Attribute | Value |
|-----------|-------|
| `canonical_url` | `/consent-personal-data/` |
| Template | `legal/consent-personal-data-template.md` |
| Consent Rule | **Target** of form checkbox link |

### L3 — User Agreement

| Attribute | Value |
|-----------|-------|
| `canonical_url` | `/user-agreement/` |
| Template | `legal/user-agreement-template.md` |

### L4 — Cookie Policy

| Attribute | Value |
|-----------|-------|
| `canonical_url` | `/cookie-files-policy/` |
| Template | `legal/cookie-files-policy-template.md` |

---

## Generation gate (page-level)

| Check | FAIL if |
|-------|---------|
| Placeholders | Unresolved `{{company_name}}`, `{{domain}}`, etc. in published HTML |
| Entity | `legal_name` / `company_name` UNKNOWN per Legal Entity workflow |
| Layout | Legal-only typography or narrowed column violating §9 |
| URLs | Non-canonical paths |
| H1 | Mismatch with Footer Rule link text |

---

## Relationship to other page types

| Rule | Detail |
|------|--------|
| Money pages | Link **to** `LEGAL_PAGE` URLs via Consent Rule — do not embed full legal text |
| `LEGAL_PAGE` | Does not embed `LEAD_FORM` |
| Site matrix | [SITE-TYPE-PAGE-MATRIX-v1.md](SITE-TYPE-PAGE-MATRIX-v1.md) — production REQUIRED |

---

## SAFE UNKNOWN

- Extension Pack legal pages (ECOMMERCE offer/returns) — **NOT FROZEN**; separate future `LEGAL_PAGE` variants
- Automated layout CI — **FUTURE**

---

*Legal Page Contract version: v1. Lessons: Triumph Legal Pilot + Legal Pack v1 freeze.*
