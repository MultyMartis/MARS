# Website Factory — Site Type SEO Mapping v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/registry/`  
**Связь:** [SITE-TYPE-REGISTRY-v1.md](SITE-TYPE-REGISTRY-v1.md), [SITE-TYPE-MATRIX-v1.md](SITE-TYPE-MATRIX-v1.md)

**Статус:** documentation only — **не** SEO-аудит, **не** автоматическая генерация мета-тегов.

> **Superseded:** Canonical SEO site-type mapping is [seo-architecture/SITE-TYPE-SEO-MAPPING-v2.md](../seo-architecture/SITE-TYPE-SEO-MAPPING-v2.md) (SEO Architecture Layer v2). This v1 file is retained for historical priority hints only — **do not delete**; content is not rewritten here.

---

## Легенда SEO priority

| Priority | Значение |
|----------|----------|
| **LOW** | SEO вторичен; минимальная техническая база; organic не primary channel. |
| **MEDIUM** | SEO поддерживает бизнес, но не доминирует; selective indexing. |
| **HIGH** | SEO — существенный канал; полноценная IA и content strategy. |
| **CRITICAL** | SEO — primary или co-primary acquisition; architecture driven by search intent. |

---

## LANDING

| Поле | Значение |
|------|----------|
| **SEO priority** | **LOW** |
| **Typical SEO architecture** | Single URL; one H1 aligned with offer; minimal internal linking; `noindex` optional for pure PPC clones; canonical self; lightweight meta (title/description for brand + offer); schema: `Organization` or `LocalBusiness` (if applicable) — **optional**; FAQ schema only if genuine FAQ block present; **no** multi-page sitemap program. |

**Примечания:** quality score и conversion > organic scale. Duplicate landings for A/B — canonical/HITL policy required.

---

## PROMO

| Поле | Значение |
|------|----------|
| **SEO priority** | **HIGH** |
| **Typical SEO architecture** | Hub-and-spoke: home → services → cases → contacts; unique H1/title per page; internal linking to money pages; XML sitemap; breadcrumbs; schema: `Organization`, `LocalBusiness` (if local), `Service` on service pages; blog/news hub optional; local SEO (NAP, geo pages) if business is local; robots: index key pages, noindex thin/duplicate utility. |

---

## CATALOG

| Поле | Значение |
|------|----------|
| **SEO priority** | **HIGH** |
| **Typical SEO architecture** | Category tree (PLP) + PDP long-tail; faceted navigation with **controlled** indexation policy; canonical rules for filters; pagination rel prev/next; structured data: `Product` / `ItemList` where honest; spec-rich PDP content; internal linking category ↔ PDP; XML sitemap segmented (categories, products); search console monitoring for crawl budget; **no** infinite thin facet URLs. |

**FUTURE:** dedicated faceted SEO addendum — not part of v1 registry execution.

---

## ECOMMERCE

| Поле | Значение |
|------|----------|
| **SEO priority** | **HIGH** |
| **Typical SEO architecture** | Full catalog SEO (as CATALOG) plus transactional intent on PDP; `Product` schema with offer (price/stock when truthful); review markup when authentic; cart/checkout typically **noindex**; policy pages indexable; site search optional; performance (CWV) critical on PLP/PDP; hreflang if multi-locale; duplicate PDP control (variants, parameters). |

---

## CORPORATE

| Поле | Значение |
|------|----------|
| **SEO priority** | **HIGH** |
| **Typical SEO architecture** | Multi-audience IA with clear intent per URL; solutions/industries hubs; careers (index if ATS allows); newsroom/blog for thought leadership; strong internal linking; schema: `Organization`, `WebSite`, `BreadcrumbList`; avoid cannibalization between similar solution pages; subtree rules when hybrid (catalog/ecommerce/blog); entity clarity pages for brand queries. |

---

## SAAS

| Поле | Значение |
|------|----------|
| **SEO priority** | **MEDIUM** |
| **Typical SEO architecture** | Marketing site: product/pricing/features/docs/blog; PLG pages indexable; **app routes** (login, dashboard, billing) → **noindex**; docs/help center as SEO asset (informational + commercial support); schema: `SoftwareApplication` (careful — no false claims); comparison/alternative pages (ethical); changelog/status for trust; separate subdomain policy (docs.app.com) — document in project charter. |

---

## WEB_APPLICATION

| Поле | Значение |
|------|----------|
| **SEO priority** | **LOW** |
| **Typical SEO architecture** | Minimal public indexable surface: login, maybe landing/login marketing shell; **default noindex** on app routes; sitemap tiny or absent; SEO **not** primary; if public marketing exists — classify subtree as `PROMO` or `LANDING` for SEO rules; focus on performance and auth, not rankings. |

---

## MARKETPLACE

| Поле | Значение |
|------|----------|
| **SEO priority** | **HIGH** |
| **Typical SEO architecture** | Listing long-tail at scale; seller store pages; category taxonomy; duplicate/thin listing control; canonical for similar listings; `Product` / `Offer` schema where accurate; user-generated content moderation for SEO quality; pagination and crawl budget management; platform brand pages + transactional category pages; checkout/account noindex; seller onboarding pages typically noindex until published inventory. |

---

## Сводная таблица

| site_type_code | SEO priority | Primary SEO mode |
|----------------|--------------|------------------|
| **LANDING** | LOW | Single-page / PPC alignment |
| **PROMO** | HIGH | Brand + service intent pages |
| **CATALOG** | HIGH | Category + PDP long-tail |
| **ECOMMERCE** | HIGH | Transactional catalog + PDP |
| **CORPORATE** | HIGH | Multi-audience hub-and-spoke |
| **SAAS** | MEDIUM | Product marketing + docs |
| **WEB_APPLICATION** | LOW | Minimal public / noindex app |
| **MARKETPLACE** | HIGH | Listing long-tail + categories |

---

## SAFE UNKNOWN

- Exact schema templates and validator rules — **future** SEO Pack artefact.
- AI visibility / entity pages — **not** separate site type in v1; may live under CORPORATE/PROMO subtree.
- Regional search engines beyond RU defaults — project-specific.

---

*SEO mapping version: v1.*
