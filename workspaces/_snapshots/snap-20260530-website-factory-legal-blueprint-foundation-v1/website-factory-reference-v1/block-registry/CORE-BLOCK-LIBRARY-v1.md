# Website Factory — Core Block Library v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/block-registry/`  
**Статус:** первый канонический library overview  
**Связь:** [BLOCK-REGISTRY-v1.md](BLOCK-REGISTRY-v1.md), [SITE-TYPE-BLOCK-MATRIX-v2.md](SITE-TYPE-BLOCK-MATRIX-v2.md)

**Reference workspace sections:** `workspaces/website-factory-reference-v1/src/partials/sections/`

---

## Назначение

Core Block Library v1 — **human-readable catalog** всех canonical blocks с фокусом на placement и conversion value. Детальные поля registry — в [BLOCK-REGISTRY-v1.md](BLOCK-REGISTRY-v1.md).

**Site type compatibility legend:**

| Marker | Meaning |
|--------|---------|
| ● | Primary / required context |
| ○ | Optional / recommended |
| — | Forbidden or N/A for type |

Full matrix: [SITE-TYPE-BLOCK-MATRIX-v2.md](SITE-TYPE-BLOCK-MATRIX-v2.md).

---

## Library entries

### HERO

| Aspect | Detail |
|--------|--------|
| **Purpose** | Above-the-fold offer, audience fit, orientation |
| **Typical placement** | Top of page — first viewport; home, landing, PLP intro, PDP header zone |
| **Conversion value** | High orientation; secondary CTA or scroll-to-convert |
| **Site type compatibility** | LANDING ● · PROMO ● · CATALOG ○ · ECOMMERCE ○ · CORPORATE ● |
| **Reference** | `hero.html` |

---

### BENEFITS

| Aspect | Detail |
|--------|--------|
| **Purpose** | Value props, outcomes, differentiators |
| **Typical placement** | Immediately below hero on single-page stacks |
| **Conversion value** | Medium — supports decision before form/CTA |
| **Site type compatibility** | LANDING ● · PROMO ○ · CATALOG — · ECOMMERCE — · CORPORATE ○ |

---

### SERVICES

| Aspect | Detail |
|--------|--------|
| **Purpose** | Service lines with links to money pages |
| **Typical placement** | Home hub; `/services/` index |
| **Conversion value** | Medium — discovery → service page conversion |
| **Site type compatibility** | LANDING — · PROMO ● · CATALOG — · ECOMMERCE — · CORPORATE ● |

---

### CATEGORIES

| Aspect | Detail |
|--------|--------|
| **Purpose** | Category taxonomy entry and navigation |
| **Typical placement** | Catalog home; mega-menu; PLP breadcrumbs context |
| **Conversion value** | Medium — discovery path |
| **Site type compatibility** | LANDING — · PROMO — · CATALOG ● · ECOMMERCE ● · CORPORATE ○ |

---

### PRODUCT_GRID

| Aspect | Detail |
|--------|--------|
| **Purpose** | Filterable PLP grid |
| **Typical placement** | Category pages; search results |
| **Conversion value** | Medium — browse → PDP |
| **Site type compatibility** | LANDING — · PROMO — · CATALOG ● · ECOMMERCE ● · CORPORATE ○ |

---

### PRODUCT_CARD

| Aspect | Detail |
|--------|--------|
| **Purpose** | Single item — card in grid or PDP body |
| **Typical placement** | Inside PRODUCT_GRID; PDP main column |
| **Conversion value** | High on PDP — RFQ or add-to-cart |
| **Site type compatibility** | LANDING — · PROMO — · CATALOG ● · ECOMMERCE ● · CORPORATE ○ |

---

### PRICING

| Aspect | Detail |
|--------|--------|
| **Purpose** | Tiers, packages, transparent ballpark |
| **Typical placement** | Mid-page on landing; service pages; shop promos |
| **Conversion value** | High when offer has tiers — drives form/checkout |
| **Site type compatibility** | LANDING ○ · PROMO ○ · CATALOG — · ECOMMERCE ○ · CORPORATE ○ |
| **Reference** | `pricing.html` |

---

### PROCESS

| Aspect | Detail |
|--------|--------|
| **Purpose** | Steps — how engagement or purchase works |
| **Typical placement** | Mid-stack after benefits |
| **Conversion value** | Medium — reduces uncertainty |
| **Site type compatibility** | LANDING ● · PROMO ○ · CATALOG — · ECOMMERCE — · CORPORATE ○ |

---

### CASES

| Aspect | Detail |
|--------|--------|
| **Purpose** | Portfolio / case studies |
| **Typical placement** | Home proof section; `/cases/` page |
| **Conversion value** | Medium trust lift |
| **Site type compatibility** | LANDING ○ · PROMO ○ · CATALOG — · ECOMMERCE — · CORPORATE ○ |
| **Reference** | `cases.html` |

---

### TESTIMONIALS

| Aspect | Detail |
|--------|--------|
| **Purpose** | Quotes; product reviews |
| **Typical placement** | Near trust zone or PDP |
| **Conversion value** | Medium–high trust |
| **Site type compatibility** | LANDING ○ · PROMO ○ · CATALOG ○ · ECOMMERCE ○ · CORPORATE ○ |

---

### TRUST

| Aspect | Detail |
|--------|--------|
| **Purpose** | Logos, metrics, badges |
| **Typical placement** | After value props; before FAQ/form |
| **Conversion value** | Medium — risk reduction |
| **Site type compatibility** | LANDING ● · PROMO ○ · CATALOG ○ · ECOMMERCE ○ · CORPORATE ● |
| **Reference** | `social_proof.html` |

---

### CERTIFICATES

| Aspect | Detail |
|--------|--------|
| **Purpose** | Licenses, ISO, industry awards |
| **Typical placement** | Trust zone; about; PDP (regulated products) |
| **Conversion value** | High in regulated verticals |
| **Site type compatibility** | LANDING ○ · PROMO ○ · CATALOG ○ · ECOMMERCE ○ · CORPORATE ○ |

---

### TEAM

| Aspect | Detail |
|--------|--------|
| **Purpose** | People behind the brand |
| **Typical placement** | About page |
| **Conversion value** | Low–medium trust |
| **Site type compatibility** | LANDING — · PROMO ○ · CATALOG — · ECOMMERCE — · CORPORATE ○ |

---

### ABOUT

| Aspect | Detail |
|--------|--------|
| **Purpose** | Company story |
| **Typical placement** | `/about/` dedicated page |
| **Conversion value** | Low direct; supports brand queries |
| **Site type compatibility** | LANDING — · PROMO ● · CATALOG — · ECOMMERCE — · CORPORATE ● |

---

### FAQ

| Aspect | Detail |
|--------|--------|
| **Purpose** | Objection handling |
| **Typical placement** | Pre-form on landing; support pages |
| **Conversion value** | Medium — removes friction |
| **Site type compatibility** | LANDING ● · PROMO ○ · CATALOG ○ · ECOMMERCE ○ · CORPORATE ○ |
| **Reference** | `faq.html` |

---

### CTA

| Aspect | Detail |
|--------|--------|
| **Purpose** | CTA band + sticky mobile |
| **Typical placement** | Mid/end of page; fixed mobile bar |
| **Conversion value** | **Critical** on LANDING |
| **Site type compatibility** | LANDING ● · PROMO ○ · CATALOG — · ECOMMERCE ○ · CORPORATE ○ |
| **Reference** | `cta_band.html`, `sticky_cta.html` |

---

### LEAD_FORM

| Aspect | Detail |
|--------|--------|
| **Purpose** | Lead capture, RFQ, price request |
| **Typical placement** | Primary conversion zone; PDP RFQ; service money pages |
| **Conversion value** | **Critical** on LANDING |
| **Site type compatibility** | LANDING ● · PROMO ○ · CATALOG ○ · ECOMMERCE — · CORPORATE ○ |
| **Reference** | `lead_form.html` |

---

### CONTACTS

| Aspect | Detail |
|--------|--------|
| **Purpose** | Phones, email, address, messengers |
| **Typical placement** | Page footer zone; `/contacts/` hub |
| **Conversion value** | High secondary (call, email) |
| **Site type compatibility** | LANDING ● · PROMO ● · CATALOG ● · ECOMMERCE ● · CORPORATE ● |
| **Reference** | `contact_block.html` |

---

### MAP

| Aspect | Detail |
|--------|--------|
| **Purpose** | Office/dealer map |
| **Typical placement** | Contacts page; local business pages |
| **Conversion value** | Medium — local intent |
| **Site type compatibility** | LANDING ○ · PROMO ○ · CATALOG ○ · ECOMMERCE ○ · CORPORATE ○ |

---

### PARTNERS

| Aspect | Detail |
|--------|--------|
| **Purpose** | Partner program presentation |
| **Typical placement** | `/partners/`; corporate home segment |
| **Conversion value** | Segment-specific B2B |
| **Site type compatibility** | LANDING — · PROMO — · CATALOG — · ECOMMERCE — · CORPORATE ○ |

---

### DELIVERY

| Aspect | Detail |
|--------|--------|
| **Purpose** | Shipping options and policy summary |
| **Typical placement** | Checkout; `/delivery/` policy page |
| **Conversion value** | Medium — checkout reassurance |
| **Site type compatibility** | LANDING — · PROMO — · CATALOG — · ECOMMERCE ○ · CORPORATE ○ |

---

### PAYMENT

| Aspect | Detail |
|--------|--------|
| **Purpose** | Payment methods, security badges |
| **Typical placement** | Checkout; PDP trust row |
| **Conversion value** | High at payment step |
| **Site type compatibility** | LANDING — · PROMO — · CATALOG — · ECOMMERCE ● · CORPORATE ○ |

---

### CHECKOUT

| Aspect | Detail |
|--------|--------|
| **Purpose** | Order completion flow |
| **Typical placement** | `/checkout/` |
| **Conversion value** | **Critical** — primary ECOMMERCE conversion |
| **Site type compatibility** | LANDING — · PROMO — · CATALOG — · ECOMMERCE ● · CORPORATE ○ |

---

### CART

| Aspect | Detail |
|--------|--------|
| **Purpose** | Cart review |
| **Typical placement** | `/cart/`; mini-cart in header (GAP) |
| **Conversion value** | High — funnel bridge |
| **Site type compatibility** | LANDING — · PROMO — · CATALOG — · ECOMMERCE ● · CORPORATE ○ |

---

### LEGAL_LINKS

| Aspect | Detail |
|--------|--------|
| **Purpose** | L1–L4 canonical URLs |
| **Typical placement** | Inside FOOTER |
| **Conversion value** | Compliance — not commercial |
| **Site type compatibility** | All Core ● (production) |

---

### FOOTER

| Aspect | Detail |
|--------|--------|
| **Purpose** | Global footer shell |
| **Typical placement** | Page bottom — all marketing pages |
| **Conversion value** | System — NAP + legal |
| **Site type compatibility** | All Core ● |

---

## Reference workspace coverage

| block_id | Implemented partial | Status |
|----------|---------------------|--------|
| HERO | hero.html | ✓ |
| TRUST | social_proof.html | ✓ |
| PRICING | pricing.html | ✓ |
| LEAD_FORM | lead_form.html | ✓ |
| CTA | cta_band.html, sticky_cta.html | ✓ |
| CONTACTS | contact_block.html | ✓ |
| FAQ | faq.html | ✓ |
| CASES | cases.html | ✓ |
| BENEFITS, PROCESS, SERVICES, … | — | **Not implemented** — registry-only v1 |

Modal callback: layout partial `modal_callback.html` — **not** separate block_id in v1 (see GAPS).

---

## SAFE UNKNOWN

- Variant library (hero v2, form compact) — **not cataloged**
- Block instance props schema — **FUTURE**

---

*Core library version: v1.*
