# Website Factory — Block Registry Gaps v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/block-registry/`  
**Статус:** documented remaining gaps after Block Registry Alignment v1  
**Связь:** [BLOCK-REGISTRY-v1.md](BLOCK-REGISTRY-v1.md), [BLOCK-REGISTRY-GAPS-v1.md](BLOCK-REGISTRY-GAPS-v1.md), [../blueprints/BLUEPRINT-GAPS-v1.md](../blueprints/BLUEPRINT-GAPS-v1.md)

---

## Назначение

Block Registry v1 делает Blueprints **operational** для planning (Site Type → Blocks). Этот документ фиксирует, что **ещё не существует** — без претензии на implementation.

---

## 1. Design mapping

| Gap | Status | Notes |
|-----|--------|-------|
| Block → design token mapping | **NOT DEFINED** | Priority 4 in [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](../WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md) |
| Block → component in visual contract | **PARTIAL** | `projects/orca/visual-semantics/contracts/website-factory-visual-contract-v0.md` — manual |
| Per-block design complexity tiers | **NOT DEFINED** | v0 had guidance; v1 registry omits |
| Responsive variants per block | **NOT CATALOGED** | |

---

## 2. Section variants

| Gap | Status | Notes |
|-----|--------|-------|
| Hero variants (brand vs conversion vs catalog) | **NOT IN REGISTRY** | Single `HERO` block_id |
| CTA variants (band vs sticky vs inline) | **PARTIAL** | One `CTA` id; reference has band + sticky partials |
| Trust vs TESTIMONIALS split | **IMPLEMENTED** | `testimonials.html` + narrowed `trust.html` — WF-R01.3.2 Wave A3 |
| Modal callback | **NOT block_id** | `modal_callback.html` in layout — recommend future `CALLBACK_MODAL` or CTA variant |
| Breadcrumbs | **NOT block_id** · **PARTIAL** | Tier B layout-component; `components/breadcrumbs.html` — WF-R01.3.3 Wave S2; required in CATALOG/ECOMMERCE Blueprints |
| Filters / search UI | **PARTIAL** | `FILTERS` — `components/filters.html` **PARTIAL** (WF-R01.3.4 Wave C2); `SEARCH` block_id — WF-R01.2 Gate 2; partial **OPEN** → WF-R01.3.4 Wave C3 |
| Header / primary nav | **IMPLEMENTED** | `header-nav.html` — WF-R01.3.2 Wave C2 |
| Pagination | **NOT block_id** · **PARTIAL** | Tier B layout-component; `components/pagination.html` — WF-R01.3.3 Wave S3; PLP requirement |
| Add-to-cart (PDP micro-block) | **NOT separate id** | Part of PRODUCT_CARD on ECOMMERCE |
| Order confirmation | **NOT block_id** | Post-checkout page block |
| Blog / news teaser | **NOT block_id** | PROMO optional page type |

---

## 3. Visual systems

| Gap | Status | Notes |
|-----|--------|-------|
| Reference SCSS coverage | **PARTIAL** | hero, header-nav, benefits, process, testimonials, trust, pricing, lead_form, cta_band, contact_block, sticky_cta, faq, cases, footer, legal-links, breadcrumbs, pagination, filters |
| Motion / interaction per block | **NOT DEFINED** | `_motion.scss` exists; no block binding |
| Dark/light theme per block | **NOT DEFINED** | |

---

## 4. Conversion patterns

| Gap | Status | Notes |
|-----|--------|-------|
| Thank-you page blocks | **NOT IN REGISTRY** | Blueprint mentions `/thank-you/` |
| Abandoned cart | **INTEGRATION** | Not a block — email/CRM |
| Segment-specific CTA (CORPORATE) | **PROCESS ONLY** | No `SEGMENT_CTA` block_id |
| RFQ vs lead form distinction | **SAME block_id** | `LEAD_FORM` covers both — variant gap |
| Sticky add-to-cart (mobile ECOMMERCE) | **NOT block_id** | Blueprint recommended |

---

## 5. Component contracts

| Gap | Status | Notes |
|-----|--------|-------|
| HTML partial contract per block_id | **PARTIAL** | 14 section partials + 4 compositional components (`legal-links`, `breadcrumbs`, `pagination` Tier B, `filters` Tier A); 12 blocks without partial |
| Props / content slots schema | **NOT DEFINED** | v0 noted SAFE UNKNOWN |
| Form field schemas (LEAD_FORM vs CHECKOUT) | **NOT DEFINED** | Consent Rule HTML only for consent |
| Accessibility checklist per block | **NOT DEFINED** | |

---

## 6. JSON schema / machine-readable export

| Gap | Status | Notes |
|-----|--------|-------|
| block_id JSON Schema | **NOT CREATED** | Markdown canonical in v1 |
| Matrix v2 machine validation | **NOT IMPLEMENTED** | |
| Blueprint ↔ block_id sync tool | **NOT IMPLEMENTED** | |
| Registry diff vs block-registry-v0 | **MANUAL** | Different ID conventions |

---

## 7. Cross-system alignment gaps

| Gap | Status | Notes |
|-----|--------|-------|
| SITE-TYPE-BLOCK-MAPPING-v1 update | **CLOSED** (2026-06-01) | [HYGIENE-PASS-v1.md](../HYGIENE-PASS-v1.md) — superseded banner |
| Cross-layer alignment (page ↔ block) | **DOCUMENTED** | [BLOCK-REGISTRY-GAPS-v1.md](BLOCK-REGISTRY-GAPS-v1.md) |
| FEATURES, CATEGORY_GRID, REVIEWS | **ADDED** | Registry alignment 2026-05-31; no reference partials |
| SITE-TYPE-SEO-MAPPING block awareness | **WEAK** | SEO v2 priority queued |
| ECOMMERCE Legal Extension blocks | **FUTURE** | E1–E4 not in Core Pack v1 |
| Extended Type block libraries | **NOT STARTED** | SAAS, WEB_APPLICATION, MARKETPLACE |

---

## 8. Reference workspace implementation gaps

| block_id | Reference partial | Gap |
|----------|-------------------|-----|
| BENEFITS | `benefits.html` | **Implemented** — WF-R01.3.2 Wave A1 |
| PROCESS | `process.html` | **Implemented** — WF-R01.3.2 Wave A2 |
| SERVICES | — | Not implemented |
| CATEGORIES | — | Not implemented |
| PRODUCT_GRID | — | Not implemented |
| PRODUCT_CARD | — | Not implemented |
| TESTIMONIALS | `testimonials.html` | **Implemented** — WF-R01.3.2 Wave A3 |
| TRUST | `trust.html` | **Implemented, narrowed** — WF-R01.3.2 Wave A3 |
| CERTIFICATES | — | Not implemented |
| TEAM | — | Not implemented |
| ABOUT | — | Not implemented |
| MAP | — | Not implemented |
| PARTNERS | — | Not implemented |
| DELIVERY | — | Not implemented |
| PAYMENT | — | Not implemented |
| CHECKOUT | — | Not implemented |
| CART | — | Not implemented |
| LEGAL_LINKS | `components/legal-links.html` | **PARTIAL** — WF-R01.3.2 Wave B2 |
| FOOTER | `footer.html` | **PARTIAL** — WF-R01.3.2 Wave B1 |

---

## 9. Validation & automation gaps

| Gap | Status |
|-----|--------|
| CI: FORBIDDEN block detection | **NOT IMPLEMENTED** |
| CI: dependency graph check | **NOT IMPLEMENTED** |
| CI: Consent Rule on LEAD_FORM partials | **MANUAL QA** |
| Operator drift warnings for block-before-blueprint | **DOCUMENTATION ONLY** |

---

## Recommended next steps (documentation queue)

| Priority | Item | Owner lane |
|----------|------|------------|
| 1 | Update SITE-TYPE-BLOCK-MAPPING-v1 → v2 pointer | **DONE** — Hygiene Pass v1 (2026-06-01) |
| 2 | DESIGN SYSTEM MAPPING (Priority 4) | Design |
| 3 | Header/nav + filters as block_id charter | **DONE** — WF-R01.2 Gate 2 (2026-06-19) |
| 4 | Partial implementation roadmap for catalog/commerce blocks | Frontend — **separate charter** |
| 5 | JSON Schema export | Tooling — S5 boundary |

---

## SAFE UNKNOWN

- Timeline for reference workspace partial expansion — **not scheduled**
- Whether modal callback becomes block_id or CTA sub-variant — **requires operator decision**
- Triumph / other workspace retrofits — **out of scope** for this alignment pass

---

*Gaps document version: v1.*
