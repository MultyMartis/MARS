# Website Factory — Content Signal Registry v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/content-contracts/`  
**Статус:** канонический словарь content signals — **architecture only**  
**Связь:** [CONTENT-CONTRACT-v1.md](CONTENT-CONTRACT-v1.md), [BLOCK-CONTENT-CONTRACTS-v1.md](BLOCK-CONTENT-CONTRACTS-v1.md)

**Не является:** copy bank, FAQ text library, objection scripts, SEO keyword list, prompt variables with example values.

---

## Назначение

**Content signal** — архитектурный класс информации, который **должен быть представлен** (или явно запрещён) в блоке/странице, без фиксации формулировки.

Signals описывают **что должно быть сказано по смыслу**, не **как** это написано.

---

## Field schema (per signal)

| Поле | Описание |
|------|----------|
| **signal_id** | Stable lowercase snake_case key |
| **signal_class** | `VALUE` · `PROOF` · `ACTION` · `ENTITY` · `COMMERCE` · `SUPPORT` · `RESTRICTION` |
| **definition** | Architectural meaning (1–3 sentences) |
| **evidence_rule** | `HITL_REQUIRED` · `SOURCE_DOCUMENTED` · `UGC_AUTHENTIC` · `LEGAL_PACK` · `NONE` |
| **typical_blocks** | Non-exhaustive `block_id` hints |
| **forbidden_without** | Preconditions (e.g. price requires offer context) |

---

## Registry

### VALUE class

#### `offer`

| Поле | Значение |
|------|----------|
| **signal_class** | VALUE |
| **definition** | Primary commercial proposition: what is sold, to whom, under what scope — one coherent value anchor per page/hero context. |
| **evidence_rule** | HITL_REQUIRED |
| **typical_blocks** | HERO, PRICING, PRODUCT_CARD |
| **forbidden_without** | Blueprint business goal documented |

#### `benefit`

| Поле | Значение |
|------|----------|
| **signal_class** | VALUE |
| **definition** | Outcome-oriented value articulation — results or advantages attributable to the offer. |
| **evidence_rule** | HITL_REQUIRED |
| **typical_blocks** | HERO, BENEFITS, FEATURES |
| **forbidden_without** | — |

#### `service_scope`

| Поле | Значение |
|------|----------|
| **signal_class** | VALUE |
| **definition** | Bounded description of service line, deliverable set, or catalog segment the user is viewing. |
| **evidence_rule** | HITL_REQUIRED |
| **typical_blocks** | SERVICES, SERVICE_PAGE context, CATEGORIES |
| **forbidden_without** | IA route matches scope |

#### `experience`

| Поле | Значение |
|------|----------|
| **signal_class** | VALUE |
| **definition** | Duration, scale, or depth of provider competence (years, projects, domains) — factual, verifiable. |
| **evidence_rule** | SOURCE_DOCUMENTED |
| **typical_blocks** | ABOUT, HERO, TRUST |
| **forbidden_without** | Verifiable source |

---

### PROOF class

#### `proof`

| Поле | Значение |
|------|----------|
| **signal_class** | PROOF |
| **definition** | Evidence that reduces perceived risk — outcomes, metrics, logos, third-party validation (generic proof slot). |
| **evidence_rule** | HITL_REQUIRED |
| **typical_blocks** | TRUST, CASES, TESTIMONIALS |
| **forbidden_without** | — |

#### `trust`

| Поле | Значение |
|------|----------|
| **signal_class** | PROOF |
| **definition** | Credibility markers: certifications, guarantees policy reference, security/compliance badges where applicable. |
| **evidence_rule** | HITL_REQUIRED or LEGAL_PACK |
| **typical_blocks** | TRUST, CERTIFICATES, PAYMENT |
| **forbidden_without** | — |

#### `review`

| Поле | Значение |
|------|----------|
| **signal_class** | PROOF |
| **definition** | Structured user review content: rating, author context, review body reference — **authentic UGC only**. |
| **evidence_rule** | UGC_AUTHENTIC |
| **typical_blocks** | REVIEWS, TESTIMONIALS |
| **forbidden_without** | Moderation/source policy |

#### `case`

| Поле | Значение |
|------|----------|
| **signal_class** | PROOF |
| **definition** | Project/client outcome narrative with identifiable context (industry, result type) — not anonymous praise. |
| **evidence_rule** | HITL_REQUIRED |
| **typical_blocks** | CASES |
| **forbidden_without** | Client permission where required |

#### `certificate`

| Поле | Значение |
|------|----------|
| **signal_class** | PROOF |
| **definition** | License, accreditation, award, or regulatory credential with issuer identity. |
| **evidence_rule** | SOURCE_DOCUMENTED |
| **typical_blocks** | CERTIFICATES, TRUST |
| **forbidden_without** | Valid credential |

#### `comparison`

| Поле | Значение |
|------|----------|
| **signal_class** | PROOF |
| **definition** | Structured differentiation vs alternatives, tiers, or SKUs — factual comparability only. |
| **evidence_rule** | HITL_REQUIRED |
| **typical_blocks** | PRICING, PRODUCT_CARD, FEATURES |
| **forbidden_without** | Comparable entities defined |

---

### ACTION class

#### `cta`

| Поле | Значение |
|------|----------|
| **signal_class** | ACTION |
| **definition** | Primary or secondary call-to-action intent: what happens next (submit, call, buy, request) — action type, not button label. |
| **evidence_rule** | NONE |
| **typical_blocks** | CTA, HERO, LEAD_FORM, PRODUCT_CARD, CHECKOUT |
| **forbidden_without** | Single primary per page (see CONTENT-RULES) |

#### `contact`

| Поле | Значение |
|------|----------|
| **signal_class** | ACTION |
| **definition** | Reachability: phone, email, messenger, hours — consistent with Legal Entity Card. |
| **evidence_rule** | SOURCE_DOCUMENTED |
| **typical_blocks** | CONTACTS, FOOTER, LEAD_FORM |
| **forbidden_without** | Legal Entity Card |

#### `location`

| Поле | Значение |
|------|----------|
| **signal_class** | ACTION |
| **definition** | Physical or service geography: address, region, delivery zone reference. |
| **evidence_rule** | SOURCE_DOCUMENTED |
| **typical_blocks** | CONTACTS, MAP, DELIVERY |
| **forbidden_without** | — |

---

### SUPPORT class

#### `faq`

| Поле | Значение |
|------|----------|
| **signal_class** | SUPPORT |
| **definition** | Question–answer pair slot for genuine support/objection topics — structure only. |
| **evidence_rule** | HITL_REQUIRED |
| **typical_blocks** | FAQ |
| **forbidden_without** | — |

#### `question`

| Поле | Значение |
|------|----------|
| **signal_class** | SUPPORT |
| **definition** | Interrogative slot in FAQ — topic label, not marketing headline. |
| **evidence_rule** | HITL_REQUIRED |
| **typical_blocks** | FAQ |
| **forbidden_without** | Paired with `answer` |

#### `answer`

| Поле | Значение |
|------|----------|
| **signal_class** | SUPPORT |
| **definition** | Response slot in FAQ — factual/support tone obligation. |
| **evidence_rule** | HITL_REQUIRED |
| **typical_blocks** | FAQ |
| **forbidden_without** | Paired with `question` |

#### `objection`

| Поле | Значение |
|------|----------|
| **signal_class** | SUPPORT |
| **definition** | Explicit friction point the content addresses (price, timing, risk, fit) — mapped to FAQ or proof, not manipulative framing. |
| **evidence_rule** | HITL_REQUIRED |
| **typical_blocks** | FAQ, BENEFITS, PROCESS |
| **forbidden_without** | — |

#### `process`

| Поле | Значение |
|------|----------|
| **signal_class** | SUPPORT |
| **definition** | Ordered steps of engagement, purchase, or delivery — step identity and sequence. |
| **evidence_rule** | HITL_REQUIRED |
| **typical_blocks** | PROCESS, CHECKOUT |
| **forbidden_without** | — |

---

### COMMERCE class

#### `price`

| Поле | Значение |
|------|----------|
| **signal_class** | COMMERCE |
| **definition** | Monetary amount, tier, or price-on-request stance — must match commerce model (RFQ vs listed price). |
| **evidence_rule** | HITL_REQUIRED |
| **typical_blocks** | PRICING, PRODUCT_CARD |
| **forbidden_without** | Site type commerce path |

#### `payment`

| Поле | Значение |
|------|----------|
| **signal_class** | COMMERCE |
| **definition** | Accepted payment methods and security reassurance at transaction surfaces. |
| **evidence_rule** | SOURCE_DOCUMENTED |
| **typical_blocks** | PAYMENT, CHECKOUT |
| **forbidden_without** | ECOMMERCE / checkout context |

#### `delivery`

| Поле | Значение |
|------|----------|
| **signal_class** | COMMERCE |
| **definition** | Shipping, pickup, or fulfillment options, timelines, and geographic limits. |
| **evidence_rule** | SOURCE_DOCUMENTED |
| **typical_blocks** | DELIVERY, CHECKOUT, PRODUCT_CARD |
| **forbidden_without** | — |

#### `availability`

| Поле | Значение |
|------|----------|
| **signal_class** | COMMERCE |
| **definition** | Stock, lead time, or service slot availability — factual status only. |
| **evidence_rule** | SOURCE_DOCUMENTED |
| **typical_blocks** | PRODUCT_CARD |
| **forbidden_without** | Live inventory source or HITL |

#### `guarantee`

| Поле | Значение |
|------|----------|
| **signal_class** | COMMERCE |
| **definition** | Warranty, return, or service guarantee terms reference — must align with legal policies when published. |
| **evidence_rule** | LEGAL_PACK or HITL_REQUIRED |
| **typical_blocks** | TRUST, PRODUCT_CARD, PRICING |
| **forbidden_without** | Policy document when claim is binding |

---

### ENTITY class

#### `entity_identity`

| Поле | Значение |
|------|----------|
| **signal_class** | ENTITY |
| **definition** | Legal entity name, identifiers, and official representation — from Legal Entity Discovery. |
| **evidence_rule** | SOURCE_DOCUMENTED |
| **typical_blocks** | FOOTER, ABOUT, LEGAL_PAGE |
| **forbidden_without** | Legal Entity Card |

#### `brand_narrative`

| Поле | Значение |
|------|----------|
| **signal_class** | ENTITY |
| **definition** | Company history, mission, positioning — non-promotional factual narrative on about surfaces. |
| **evidence_rule** | HITL_REQUIRED |
| **typical_blocks** | ABOUT, TEAM |
| **forbidden_without** | — |

---

### RESTRICTION class

#### `urgency`

| Поле | Значение |
|------|----------|
| **signal_class** | RESTRICTION |
| **definition** | Time-bound scarcity or deadline — **only** when factually true and documented; high misuse risk. |
| **evidence_rule** | SOURCE_DOCUMENTED |
| **typical_blocks** | HERO, CTA, PRICING |
| **forbidden_without** | Verifiable deadline/stock rule |

#### `legal_disclosure`

| Поле | Значение |
|------|----------|
| **signal_class** | RESTRICTION |
| **definition** | Mandatory legal text slot per Legal Pack document type — structure and document binding, not marketing. |
| **evidence_rule** | LEGAL_PACK |
| **typical_blocks** | LEGAL_PAGE (route body), LEGAL_LINKS |
| **forbidden_without** | Legal Pack gate |

#### `consent`

| Поле | Значение |
|------|----------|
| **signal_class** | RESTRICTION |
| **definition** | Personal data processing consent capture adjacent to forms — rule reference, not checkbox label text. |
| **evidence_rule** | LEGAL_PACK |
| **typical_blocks** | LEAD_FORM, CHECKOUT |
| **forbidden_without** | Consent Rule + Legal Pack |

---

## Signal count summary

| Class | Count (v1) |
|-------|------------|
| VALUE | 4 |
| PROOF | 6 |
| ACTION | 3 |
| SUPPORT | 5 |
| COMMERCE | 5 |
| ENTITY | 2 |
| RESTRICTION | 3 |
| **Total** | **28** |

New `signal_id` — **forbidden** in v1 without Content Layer charter + CONTENT-GAPS review.

---

## SAFE UNKNOWN

- Industry-specific signal packs (medical, finance) — **FUTURE**
- Signal ↔ CMS field mapping — **FUTURE**
- Automated signal presence detection — **FUTURE**

---

*Content Signal Registry version: v1.*
