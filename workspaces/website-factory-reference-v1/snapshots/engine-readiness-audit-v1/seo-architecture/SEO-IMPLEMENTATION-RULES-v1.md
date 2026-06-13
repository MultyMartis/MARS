# Website Factory — SEO Implementation Rules v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/seo-architecture/`  
**Статус:** human-operated production rules — **documentation only**  
**Связь:** [SEO-ARCHITECTURE-SYSTEM-v2.md](SEO-ARCHITECTURE-SYSTEM-v2.md), [SITE-TYPE-SEO-MAPPING-v2.md](SITE-TYPE-SEO-MAPPING-v2.md)

**Не является:** automated linter, SEO audit tool, content generator.

---

## Global rules (all Core types)

| # | Rule | Halt if violated |
|---|------|------------------|
| G1 | SEO Architecture frozen **before** Design / Frontend on money/catalog routes | Design start without Page SEO Contracts |
| G2 | No new `site_type_code` or Blueprint in SEO workstream | Architecture drift |
| G3 | No keyword/meta/article generation under SEO layer | Scope creep |
| G4 | Page SEO Contract required for each indexable production route in `priority_pages` | Incomplete gate |
| G5 | `intent_type` must match SEARCH-INTENT-MODEL-v1 | Invalid taxonomy |
| G6 | Legal Pack v1 **FROZEN** — trust signals reference legal mapping only | Legal Pack mutation |
| G7 | Page Block Validation PASS before Design (upstream) | Block architecture fail |
| G8 | No MIG / ORCA / runtime SEO validator claimed | False implementation claims |

---

## LANDING

| Rule | Detail |
|------|--------|
| **L1 PPC-first** | Primary traffic = PPC per Blueprint; organic is secondary or optional |
| **L2 Lead generation** | Architecture optimizes single conversion path, not organic scale |
| **L3 SEO secondary** | `seo_depth` = MINIMAL; do not invest multi-page organic IA |
| **L4 No blog-first** | No content hub / blog as primary site architecture |
| **L5 Single surface** | `LANDING_PAGE` on `/`; `HOME_PAGE` forbidden |
| **L6 Campaign duplicates** | A/B or clone landings require canonical / noindex policy in SEO Strategy Contract |
| **L7 Legal** | Production + PII → legal routes; SEO navigational only on `LEGAL_PAGE` |
| **L8 Exclusions** | No catalog pages, no SERVICE_PAGE, no reviews hub as SEO program |

---

## PROMO

| Rule | Detail |
|------|--------|
| **P1 Hub-and-spoke** | `HOME_PAGE` links to money pages (`SERVICE_PAGE`, `CONTACT_PAGE`) |
| **P2 Service SEO** | ≥1 `SERVICE_PAGE` with unique intent per URL — no cannibalization |
| **P3 Local optional** | If local business: `LOCAL` intent on CONTACT + NAP signals |
| **P4 Trust support** | `ABOUT_PAGE`, optional `REVIEWS_PAGE` / `FAQ_PAGE` support money pages |
| **P5 No catalog SEO** | No PLP/PDP program — reclassify to CATALOG/ECOMMERCE |
| **P6 No checkout SEO** | No cart/checkout architecture |
| **P7 Campaign landings** | Optional `LANDING_PAGE` — separate Page SEO Contract; do not replace HOME SEO hub |

---

## CATALOG

| Rule | Detail |
|------|--------|
| **C1 Category SEO** | `CATEGORY_PAGE` required; category tree drives internal linking |
| **C2 Product visibility** | `PRODUCT_PAGE` required; PDP = primary long-tail target |
| **C3 No checkout strategy** | Cart/checkout page types forbidden; no transactional funnel SEO |
| **C4 RFQ conversion** | PDP conversion = RFQ/contact — not ATC |
| **C5 Facet discipline** | Document facet indexation policy in SEO Strategy Contract; no infinite thin URLs |
| **C5 Pagination** | PLP pagination architecture documented (prev/next intent) — not implementation |
| **C6 No blog-first** | Blog cannot replace catalog IA as primary organic strategy |
| **C7 Contact** | `CONTACT_PAGE` required for support/RFQ trust |

---

## ECOMMERCE

| Rule | Detail |
|------|--------|
| **E1 Commercial SEO** | Same catalog discipline as CATALOG for PLP/PDP |
| **E2 Category + product** | Both page types REQUIRED in SEO priority set |
| **E3 Checkout excluded** | Cart, checkout, order confirmation — **not** SEO targets; default **noindex** intent |
| **E4 Transactional on PDP only** | `TRANSACTIONAL` intent on `PRODUCT_PAGE`; not on utility funnel |
| **E5 No SERVICE_PAGE** | B2B services hub → PROMO hybrid reclassification |
| **E6 No LANDING-only** | Single-page model → site type LANDING |
| **E7 Product schema intent** | Honest offer/inventory only — documented in Page SEO Contract |
| **E8 Performance** | CWV critical on PLP/PDP — note in strategy; not audit in v2 |

---

## CORPORATE

| Rule | Detail |
|------|--------|
| **R1 Brand-first home** | `HOME_PAGE` primary `BRAND` + `NAVIGATIONAL` |
| **R2 Multi-audience IA** | Distinct intent per solutions/industries URL |
| **R3 Cannibalization guard** | No duplicate solution URLs competing for same intent |
| **R4 Subtree discipline** | Catalog/ecommerce pages only when subtree declared in Blueprint |
| **R5 About required** | `ABOUT_PAGE` enterprise trust |
| **R6 Thought leadership optional** | Blog/news — optional; must link to hubs, not replace entity clarity |
| **R7 Careers** | Index only if project/ATS policy allows |
| **R8 Legal** | `LEGAL_PAGE` navigational; production L1–L4 |

---

## Production flow (mandatory order)

```text
1. site_type_code + Blueprint
2. SEO Strategy Contract (site-level)
3. Page Architecture + Page Contracts (all routes)
4. Page SEO Contracts (priority + indexable routes)
5. SEO Architecture Matrix review
6. Page Block Validation PASS
7. Design (FUTURE)
8. Frontend
```

---

## Anti-patterns (halt)

| Anti-pattern | Affected types |
|--------------|----------------|
| Blog-first site without money/catalog IA | LANDING, CATALOG, ECOMMERCE |
| Indexing checkout steps | ECOMMERCE |
| SEO-heavy facet URLs without policy | CATALOG, ECOMMERCE |
| Multi-page organic program on LANDING | LANDING |
| SERVICE_PAGE as primary on pure catalog | CATALOG, ECOMMERCE |
| Missing Page SEO Contract on priority page | All |
| Claiming automated SEO validation exists | All |

---

## SAFE UNKNOWN

- Operator tooling for SEO contract templates — **FUTURE**.
- Integration with future Metadata Contract — **not defined** in v2.

---

*SEO Implementation Rules version: v1.*
