# Website Factory — PROMO Blueprint v1

**Blueprint ID:** `PROMO-BLUEPRINT-v1`  
**site_type_code:** `PROMO`  
**site_type_group:** CORE  
**Контракт:** [BLUEPRINT-CONTRACT-v1.md](BLUEPRINT-CONTRACT-v1.md)

---

## business_goal

**Primary:** Узнаваемость бренда, построение доверия, навигация к ключевым услугам и контактным точкам.

Многостраничное представление компании без полноценной e-commerce или кастомной enterprise-логики. SEO-capable IA для органического привлечения.

**Direction:** Multi-page structure · trust-building · SEO importance **high**.

---

## typical_traffic_sources

| Источник | Приоритет |
|----------|-----------|
| Organic search | **Primary** |
| Brand queries / direct | High |
| Local SEO | High (if local business) |
| Referrals | Medium |
| Contextual ads to hub pages | Medium |
| PPC to home/services | Medium |

---

## page_structure

**Model:** Hub-and-spoke multi-page IA.

```
/                          ← home hub
/services/                 ← services index
/services/{slug}/          ← service money pages
/about/                    ← company story
/cases/ or /portfolio/     ← proof (optional section)
/contacts/                 ← contact hub
/blog/ or /news/           ← optional content hub
/privacy-policy/ …         ← legal L1–L4
```

**Typical page count:** 5–15 pages (+ legal).

---

## required_pages

| Page role | URL pattern | Notes |
|-----------|-------------|-------|
| **Home** | `/` | Brand + services teaser + proof + CTA |
| **Services index** | `/services/` | Overview of offerings |
| **Service detail** | `/services/{slug}/` | ≥1 money page; multi-service = multiple slugs |
| **About** | `/about/` | Company story, team optional |
| **Contacts** | `/contacts/` | Contact block, map optional |
| **Legal L1–L4** | `/privacy-policy/` … `/cookie-files-policy/` | Production baseline |

**Recommended (not blocking v1 classification):**

| Page role | URL pattern |
|-----------|-------------|
| Cases / Portfolio | `/cases/` or `/portfolio/` |
| Blog / News | `/blog/` or `/news/` |

---

## required_blocks

**Per-page minimums:**

| Page | Required blocks |
|------|-----------------|
| **Global** | Header/nav · Legal footer |
| **Home** | Hero (brand/service) · Services overview · Social proof · CTA band · Contact teaser |
| **Service** | Hero · Scope/description · Process · FAQ (recommended) · Lead form (contextual) · Contact |
| **About** | Hero · Story · Team (optional) · Proof |
| **Contacts** | Contact block · Map/locations (recommended) · FAQ (optional) |

---

## optional_blocks

| Block role | When |
|------------|------|
| Cases / portfolio grid | Proof on home or dedicated page |
| Team | About page |
| Blog/news teaser | Content marketing |
| Pricing ballpark | Transparent service pricing |
| Careers entry | Hiring signal |
| Map / locations | Local business |
| Lead form | Per service page beyond contact |

---

## conversion_requirements

| Requirement | Rule |
|-------------|------|
| **Primary conversion** | Soft + contextual — contact, lead form, click-to-call |
| **CTA model** | «Узнать больше» on hub; stronger CTA on service money pages |
| **Forms** | On money pages and contacts; Consent Rule required |
| **No single sticky PPC funnel** | Unlike LANDING — navigation serves discovery |

**Matrix alignment:** Lead generation **high**; SEO **high**; PPC **medium**.

---

## legal_requirements

**Source:** [SITE-TYPE-LEGAL-MAPPING-v2.md](../legal/SITE-TYPE-LEGAL-MAPPING-v2.md) — PROMO

| Requirement | Detail |
|-------------|--------|
| **Required documents** | L1, L2, L3, L4 — full site + production |
| **Footer links** | Все 4 — production |
| **Consent Rule** | Contact / lead forms on any page |
| **Cookie banner** | Links to L4 |
| **Future expansion** | — |

---

## seo_requirements

**Source:** [SITE-TYPE-SEO-MAPPING-v2.md](../seo-architecture/SITE-TYPE-SEO-MAPPING-v2.md) — PROMO (derived from v1 hints)

| Requirement | Detail |
|-------------|--------|
| **SEO priority** | **HIGH** |
| **Architecture** | Hub-and-spoke: home → services → cases → contacts |
| **Per-page** | Unique H1/title per page |
| **Internal linking** | To money pages and contacts |
| **Technical** | XML sitemap; breadcrumbs |
| **Schema** | `Organization`, `LocalBusiness` (if local), `Service` on service pages |
| **Content hub** | Blog/news optional for long-tail |
| **Local SEO** | NAP, geo pages if applicable |
| **Robots** | Index key pages; noindex thin/duplicate utility |

---

## exclusions

| Excluded | Consequence if added |
|----------|---------------------|
| **Cart** | Reclassify → `ECOMMERCE` |
| **Checkout** | Reclassify → `ECOMMERCE` |
| **Online payment** | Reclassify → `ECOMMERCE` |
| Product catalog at scale (PLP/PDP tree) | Reclassify → `CATALOG` |
| Filters / faceted catalog | Reclassify → `CATALOG` |
| Subscriptions / billing UI | Reclassify → `SAAS` |
| Partner portals / SSO / enterprise integrations | Reclassify → `CORPORATE` |
| Single-page-only PPC funnel | Reclassify → `LANDING` |
| Sticky conversion CTA site-wide | LANDING pattern — avoid unless specific money page |

---

*Promo Blueprint version: v1.*
