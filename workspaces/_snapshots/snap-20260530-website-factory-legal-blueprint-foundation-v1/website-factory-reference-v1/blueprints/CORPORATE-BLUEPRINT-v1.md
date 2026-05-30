# Website Factory — CORPORATE Blueprint v1

**Blueprint ID:** `CORPORATE-BLUEPRINT-v1`  
**site_type_code:** `CORPORATE`  
**site_type_group:** CORE  
**Контракт:** [BLUEPRINT-CONTRACT-v1.md](BLUEPRINT-CONTRACT-v1.md)

---

## business_goal

**Primary:** Комплексное цифровое представление организации с **сегментированными аудиториями** (кliенты, партнёры, сотрудники, инвесторы).

**Direction:** Corporate structure · department/solution pages · custom functionality · partner areas · integrations · optional catalog/ecommerce subtrees.

**Hybrid by design:** primary `CORPORATE` Blueprint + **per-route-group** subtree Blueprints where applicable.

---

## typical_traffic_sources

| Источник | Приоритет |
|----------|-----------|
| Brand organic / direct | **Primary** |
| B2B research queries | High |
| PR / news | Medium |
| Partner referrals | Medium |
| Recruitment | Medium |
| PPC | Medium |

---

## page_structure

**Model:** Multi-audience hub-and-spoke with optional subtrees.

```
/                                    ← corporate home
/about/ · /company/                  ← corporate narrative
/solutions/ or /industries/          ← solution hubs
/solutions/{slug}/                   ← solution detail
/departments/ or /business-units/    ← optional org structure
/partners/                           ← partner area entry
/careers/                            ← recruitment
/newsroom/ or /press/                ← news / IR
/contacts/                           ← global contact
/catalog/ …                          ← optional CATALOG subtree
/shop/ …                             ← optional ECOMMERCE subtree
/portal/ …                           ← partner/employee entry (custom)
/privacy-policy/ …                   ← legal L1–L4
```

**Typical page count:** 30–500+ URL; several IA subtrees with different conversion models.

---

## required_pages

| Page role | URL pattern | Notes |
|-----------|-------------|-------|
| **Corporate home** | `/` | Brand + audience routing |
| **About / company** | `/about/` or `/company/` | Entity clarity |
| **Solutions hub** | `/solutions/` or `/industries/` | B2B intent pages |
| **Solution detail** | `/solutions/{slug}/` | ≥1 segment page |
| **Contacts** | `/contacts/` | Global contact |
| **Legal L1–L4** | Standard URLs | Production baseline |

**Recommended (context-dependent):**

| Page role | URL pattern |
|-----------|-------------|
| Partners | `/partners/` |
| Careers | `/careers/` |
| Newsroom / Press | `/newsroom/` |
| Investor relations | `/investors/` |
| Locations | `/locations/` |

**Subtree pages:** inherit [CATALOG-BLUEPRINT-v1.md](CATALOG-BLUEPRINT-v1.md) or [ECOMMERCE-BLUEPRINT-v1.md](ECOMMERCE-BLUEPRINT-v1.md) when present — document per route group.

---

## required_blocks

| Context | Required blocks |
|---------|-----------------|
| **Global** | Mega/primary nav · Legal footer |
| **Home** | Brand hero · Solutions/services hub teaser · Proof (logos/cases) · Segment CTAs · Contact |
| **Solution page** | Hero · Scope · Proof · Segment CTA · Contact |
| **About** | Story · Leadership (optional) · Proof |
| **Partners** | Partner value prop · Entry CTA · Contact |
| **Contacts** | Contact block · Locations (optional) |

**Custom functionality blocks:** per project charter — widgets, calculators, configurators, portal entry — **not** in Core block kit; document in project IA.

---

## optional_blocks

| Block role | When |
|------------|------|
| Industries verticals | Multi-vertical corp |
| Resource / blog teaser | Thought leadership |
| Careers entry + ATS embed | Hiring |
| Newsroom / press releases | IR / PR |
| Investor snippet | Public company |
| Employee portal entry | Internal audience |
| Catalog/ecommerce subtree blocks | Inherit from CATALOG/ECOMMERCE Blueprints |
| Integration showcases | CRM, SSO, API partners |

---

## conversion_requirements

| Requirement | Rule |
|-------------|------|
| **Primary conversion** | **Segmented** — demo/sales contact, partner apply, careers apply, investor contact |
| **CTA hierarchy** | Different primary CTA per audience segment; **HITL** when CTAs conflict |
| **Forms** | Consent Rule on all ПДn collection across subtrees |
| **Subtree conversion** | Catalog subtree → RFQ; ecommerce subtree → purchase; marketing → contact |

**Matrix alignment:** Custom logic **high**; integrations **high**; complexity **high**.

---

## legal_requirements

**Source:** [SITE-TYPE-LEGAL-MAPPING-v2.md](../legal/SITE-TYPE-LEGAL-MAPPING-v2.md) — CORPORATE

| Requirement | Detail |
|-------------|--------|
| **Core documents** | L1, L2, L3, L4 — baseline production |
| **Footer links** | Все 4 — production baseline |
| **Consent Rule** | All ПДn forms across subtrees |
| **Future legal expansion** | **CORPORATE CUSTOM:** partner agreements, portal terms, investor disclaimers, sector disclosures |
| **Subtree extensions** | ECOMMERCE / SAAS / MARKETPLACE legal extensions apply **per route group** |

**Hybrid rule:** legal mapping **per route group**; primary `CORPORATE` does not cancel subtree Extension requirements.

---

## seo_requirements

**Source:** [SITE-TYPE-SEO-MAPPING-v1.md](../registry/SITE-TYPE-SEO-MAPPING-v1.md) — CORPORATE

| Requirement | Detail |
|-------------|--------|
| **SEO priority** | **HIGH** |
| **Architecture** | Multi-audience IA; clear intent per URL |
| **Hubs** | Solutions, industries, careers (if indexable) |
| **Content** | Newsroom/blog for thought leadership |
| **Internal linking** | Strong cross-linking; avoid cannibalization |
| **Schema** | `Organization`, `WebSite`, `BreadcrumbList` |
| **Entity pages** | Brand query clarity |
| **Subtree SEO** | Apply CATALOG/ECOMMERCE SEO rules within subtrees |

---

## exclusions

| Excluded | Consequence if added |
|----------|---------------------|
| Full SaaS product surface (app dashboards as primary) | Subtree → `SAAS` or separate product property |
| Pure operational app without marketing shell | Reclassify → `WEB_APPLICATION` |
| Multi-sided marketplace core | Reclassify → `MARKETPLACE` |
| Single-page-only IA | Reclassify → `LANDING` |
| SMB promo-only scope (no custom/segments) | Reclassify → `PROMO` |

**Not excluded (by design):** optional catalog, ecommerce, partner portals — with subtree Blueprint + legal mapping.

---

## Integrations (documentation scope)

| Integration type | Blueprint note |
|------------------|----------------|
| CRM (lead routing) | Project charter; not Factory default |
| ATS (careers) | Embed or link; indexation policy per vendor |
| SSO (partner/employee) | Security charter; app routes often noindex |
| Analytics / CDP | Consent + L4 alignment |
| ERP / PIM (catalog) | Data source; not Blueprint content |

**SAFE UNKNOWN:** specific integration contracts — per project.

---

*Corporate Blueprint version: v1.*
