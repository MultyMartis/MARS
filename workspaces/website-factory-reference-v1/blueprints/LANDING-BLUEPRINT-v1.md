# Website Factory — LANDING Blueprint v1

**Blueprint ID:** `LANDING-BLUEPRINT-v1`  
**site_type_code:** `LANDING`  
**site_type_group:** CORE  
**Reference workspace:** `workspaces/website-factory-reference-v1/`  
**Контракт:** [BLUEPRINT-CONTRACT-v1.md](BLUEPRINT-CONTRACT-v1.md)

---

## business_goal

**Primary:** Генерация лидов или одно целевое действие (заявка, звонок, регистрация) с **одного URL**.

**Direction:** Single primary conversion · lead generation · PPC-friendly.

Одностраничный коммерческий актив с линейной структурой повествования и минимальной навигацией. Качество трафика и conversion rate важнее organic scale.

---

## typical_traffic_sources

| Источник | Приоритет |
|----------|-----------|
| PPC (Яндекс.Директ, Google Ads) | **Primary** |
| Ретаргетинг | High |
| Email / SMS campaigns | Medium |
| Партнёрские ссылки | Medium |
| Organic search | **Low** |

---

## page_structure

**Model:** Single conversion page (+ utility/legal).

```
/                          ← primary conversion page (all blocks)
/thank-you/                ← optional post-submit
/privacy-policy/           ← legal (production)
/consent-personal-data/    ← legal (production)
/user-agreement/           ← legal (production)
/cookie-files-policy/      ← legal (production)
```

**Typical page count:** 1 основная + 0–1 thank-you + 4 legal (production).

---

## required_pages

| Page role | URL | Notes |
|-----------|-----|-------|
| **Primary landing** | `/` | Единственная conversion page; все mandatory blocks |
| **Privacy policy** | `/privacy-policy/` | L1 — production + сбор ПДн |
| **Consent PD** | `/consent-personal-data/` | L2 |
| **User agreement** | `/user-agreement/` | L3 |
| **Cookie policy** | `/cookie-files-policy/` | L4 |

**Conditional:** `/thank-you/` — recommended при form submit redirect.

**Legal note:** PPC landing без форм и без production — legal pages не обязательны (LEGAL-IMPLEMENTATION-RULES §2).

---

## required_blocks

**Global stack (primary page `/`):**

| Order | Block role | Reference partial |
|-------|------------|-------------------|
| 1 | Hero | `hero` |
| 2 | Benefits (value props) | inline / hero-adjacent |
| 3 | Process (how it works) | — |
| 4 | Social proof / Trust | `social_proof` |
| 5 | FAQ | `faq` |
| 6 | Lead form | `lead_form` |
| 7 | CTA band | `cta_band` |
| 8 | Contact block | `contact_block` |
| 9 | Sticky CTA (mobile) | `sticky_cta` |
| 10 | Legal footer | `footer` |

**Layout:** Header (minimal) · Modal callback hook (recommended wiring)

**Typical stack:** Hero → Benefits → Process → Social proof → FAQ → Lead form → CTA band → Contact → Sticky CTA

---

## optional_blocks

| Block role | When |
|------------|------|
| Pricing | Offer has tiers / packages |
| Cases | Social proof extension |
| Modal callback | Phone-first conversion |
| Logo strip | Brand trust |
| Risk reversal | Guarantee / warranty messaging |
| Countdown | Time-limited campaign |

---

## conversion_requirements

| Requirement | Rule |
|-------------|------|
| **Primary conversion** | **One** — form submit, callback, or click-to-call |
| **CTA hierarchy** | Single primary CTA repeated; sticky on mobile |
| **Form** | Lead form with Consent Rule HTML |
| **PPC alignment** | H1/title aligned with ad offer; fast LCP; minimal nav distraction |
| **Secondary actions** | Phone, messenger — subordinate to primary |
| **Thank-you** | Post-conversion confirmation page optional |

**Matrix alignment:** Lead generation **critical**; PPC importance **critical** ([SITE-TYPE-MATRIX-v1](../registry/SITE-TYPE-MATRIX-v1.md)).

---

## legal_requirements

**Source:** [SITE-TYPE-LEGAL-MAPPING-v2.md](../legal/SITE-TYPE-LEGAL-MAPPING-v2.md) — LANDING

| Requirement | Detail |
|-------------|--------|
| **Required documents** | L1, L2, L3, L4 — при full landing + production + сбор ПДн |
| **Footer links** | Все 4 canonical links — production |
| **Consent Rule** | На каждой форме сбора ПДн (lead form, callback modal) |
| **Future expansion** | — |

---

## seo_requirements

**Source:** [SITE-TYPE-SEO-MAPPING-v1.md](../registry/SITE-TYPE-SEO-MAPPING-v1.md) — LANDING

| Requirement | Detail |
|-------------|--------|
| **SEO priority** | **LOW** |
| **Indexation** | Single URL; self-canonical; `noindex` optional for pure PPC clones |
| **Meta** | Lightweight title/description (brand + offer) — **strategy only**, not generated here |
| **Internal linking** | Minimal |
| **Schema** | `Organization` / `LocalBusiness` — optional; FAQ schema only if genuine FAQ block |
| **Sitemap** | No multi-page sitemap program |

**Principle:** Quality score and conversion > organic scale.

---

## exclusions

| Excluded | Consequence if added |
|----------|---------------------|
| Multi-page IA (services, blog hub) | Reclassify → `PROMO` |
| Category grid / catalog / PLP / PDP | Reclassify → `CATALOG` |
| Filters / search at catalog scale | Reclassify → `CATALOG` |
| **Cart** | Reclassify → `ECOMMERCE` |
| **Checkout** | Reclassify → `ECOMMERCE` |
| **Online payment** | Reclassify → `ECOMMERCE` |
| User account / dashboard | Reclassify → `SAAS` / `WEB_APPLICATION` |
| Marketplace / multi-vendor | Reclassify → `MARKETPLACE` |
| Full mega-nav corporate IA | Reclassify → `CORPORATE` / `PROMO` |

---

*Landing Blueprint version: v1. Golden reference: `workspaces/website-factory-reference-v1/`.*
