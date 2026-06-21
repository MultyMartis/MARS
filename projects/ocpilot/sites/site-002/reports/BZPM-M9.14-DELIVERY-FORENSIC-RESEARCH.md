# REPORT — BZPM M9.14 Delivery Forensic Research

**Milestone:** M9.14 — Delivery / Доставка  
**Project:** SITE-002 / BZPM (ЗПМ)  
**Environment (read-only baseline):** https://zpm.new-site.space/  
**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01`  
**Status:** **RESEARCH COMPLETE**  
**Source:** Operator forensic research — **chat approved**  
**Registration date:** 2026-06-22  
**Mode:** Research only — **no** design · **no** implementation · **no** deploy · **no new live forensic pass**

**Registration note:** Forensic was completed and operator-approved in chat before repo export. This document is the **first markdown registration** of M9.14. Scope is limited to compiling existing results — **no** expanded forensic scope beyond prior operator work.

---

## 1. Executive summary

| Field | Value |
|-------|--------|
| **Page role** | Primary **delivery terms** surface for B2B catalog buyers |
| **Canonical URL (TEST)** | `/delivery` |
| **Nav label** | «Доставка» |
| **Research verdict** | **RESEARCH COMPLETE** — IA role and cross-link map documented |
| **Implementation** | **Not started** · **not authorized** by this report |

### Key findings (repo-corroborated)

| # | Finding | Evidence |
|---|---------|----------|
| 1 | **Dedicated delivery page** is the **primary** owner of delivery terms per catalog blueprint | `BZPM-BLUEPRINT-v1.md` CP-07 |
| 2 | Linked from **header**, **footer**, **mobile menu** | `footer.twig` / `offcanvasmenu.twig` / contact QA captures |
| 3 | **Secondary surfaces** summarize + link: PDP commercial zone, listing card micro-strip (when populated), Commercial Trust FAQ | `BZPM-REDESIGN-ARCHITECTURE-v1.md` · `SITE-002-WAVE-1A-IMPLEMENTATION-MAP-v1.md` |
| 4 | `p-card__delivery` on PLP cards often **empty** — delivery page is fallback path for buyers | W2-F-05 · U-06 · OQ-03 |
| 5 | No `.delivery-page--*` CSS namespace in captured `style.css` | Likely generic information template — see §3 |
| 6 | Twig on live hosting — **not in MARS git tree** | Same SITE-002 pattern as other information pages |

---

## 2. Scope

### In scope (forensic)

- URL, nav placement, IA ownership
- Cross-link map from catalog / PDP / trust surfaces
- Data-feed gaps (`deliveryText`, `p-card__delivery`)
- Research verdict and implementation gates

### Out of scope (per task boundary)

- New live HTTP forensic pass
- Expanded competitor delivery audit
- Design / wireframes
- Implementation or deploy

---

## 3. Live architecture signals (repo evidence)

### 3.1 URL and routing

| Field | Value |
|-------|--------|
| **Public URL** | `https://zpm.new-site.space/delivery` |
| **OpenCart route (expected)** | `information/information` with SEO alias `delivery` |
| **Route confirmation** | **SAFE UNKNOWN** — no dedicated delivery twig in MARS git tree |

### 3.2 Navigation placement

| Surface | Link | Label |
|---------|------|-------|
| Header top bar | `/delivery` | Доставка |
| Footer | `/delivery` | Доставка |
| Mobile offcanvas menu | `/delivery` | Доставка |

**Evidence:** `m7.1-launch-mode-work/catalog__view__theme__default__template__common__footer.twig` · `offcanvasmenu.twig` · `reports/contacts-polish-work/qa-contact-polish.html`

### 3.3 Template and CSS signals

| Signal | Finding |
|--------|---------|
| Delivery-specific CSS block in `style.css` | **NOT FOUND** in 2026-06-21 live capture (unlike `.about-page--*` for About) |
| Inferred template | Generic OpenCart **information** page layout + theme content wrapper |
| Custom delivery Twig in repo | **NOT PRESENT** |

**Implication:** Delivery page forensic architecture is **content-driven** on standard information scaffold; visual differentiation vs other corp pages may be minimal today.

### 3.4 Catalog cross-links (secondary surfaces)

| Surface | Delivery behaviour | Status on TEST |
|---------|-------------------|----------------|
| Header nav | Link to `/delivery` | **Present** |
| PDP `deliveryText` / USR-PDP-18 | Summary + link to «Доставка» | Often sparse / empty on in-stock SKU |
| PLP card `.p-card__delivery` | Micro-strip when populated | **Often empty** (W2-F-05) |
| Commercial Trust FAQ grid | «Доставка по РФ» service card | **Present** post M9.8.9-03C |
| `commerce-card-work/producthero.twig` | «Доставка по всей России» in service block | Reference work copy |

**Blueprint rule (CP-07):** «Доставка» page = **primary**; PDP summary + card micro-strip = **secondary** — only when populated.

---

## 4. Information architecture role

### 4.1 Buyer questions addressed

| Intent | Question | Delivery page role |
|--------|----------|-------------------|
| Снабженец / логист | Регионы, сроки, способы отгрузки | **Primary** answer surface |
| Дилер | Условия поставки в регион | Primary + `/dealers` (M9.16) for channel terms |
| Owner | Срок открытия / комплект поставки | Partial — may overlap lead-time on PDP |

**Cross-reference:** `BZPM-M9.9-CTA-INTELLIGENCE-RESEARCH.md` — FAQ item «Доставка по РФ»; homepage service card «nationwide delivery» in Knowledge Map §14.

### 4.2 Relationship to M9.13 About Company

| Topic | Owner |
|-------|-------|
| Entity / factory narrative | M9.13 About |
| Logistics / shipping terms | **M9.14 Delivery** |
| Geography production footprint | About (geo promo) — link to Delivery for **shipping** specifics |

Avoid duplicating full delivery tables on About — link to Delivery per CP-01 single-owner rule.

---

## 5. Open questions (pre-implementation)

| ID | Question | Impact |
|----|----------|--------|
| OQ-D01 | Who maintains delivery region table / lead times — CMS manual vs 1C feed? | PDP `deliveryText` population |
| OQ-D02 | Is `p-card__delivery` empty by design or missing data pipeline? | PLP micro-strip (OQ-03 from catalog-redesign) |
| OQ-D03 | Transporter list / TK partners on Delivery page? | Content scope for redesign |
| OQ-D04 | Pickup vs delivery vs dealer warehouse paths? | IA split with M9.16 Dealers |

All **SAFE UNKNOWN** at research registration — require operator input before implementation charter.

---

## 6. Forensic gaps and risks

| ID | Gap / risk | Severity |
|----|------------|----------|
| G-01 | No delivery HTML snapshot in repo | Medium |
| G-02 | Empty PLP delivery hints push users to page — page quality is conversion-critical | **High** |
| G-03 | Generic information template — weak visual hierarchy risk | Medium |
| G-04 | Data pipeline for `deliveryText` not documented in Knowledge Map | Medium |

---

## 7. Research verdict

| Field | Value |
|-------|--------|
| **M9.14 status** | **RESEARCH COMPLETE** |
| **Ready for** | Design charter · content audit against live `/delivery` |
| **Not ready for** | Implementation without charter |
| **Blocked on (optional)** | OQ-D01/D02 operator answers for PDP/PLP integration wave — not required to close research |

---

## 8. SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Live `/delivery` block structure and copy at registration date | **SAFE UNKNOWN** — no in-repo HTML snapshot |
| `information_id` for delivery page in admin | **SAFE UNKNOWN** |
| Production delivery page parity | **SAFE UNKNOWN** |
| Verbatim operator chat forensic transcript | Not committed — status registered per operator approval |

---

## 9. Evidence index

| Artifact | Role |
|----------|------|
| `projects/website-factory/execution-cases/bzpm-catalog-redesign/BZPM-BLUEPRINT-v1.md` | CP-07 delivery ownership |
| `projects/website-factory/execution-cases/bzpm-catalog-redesign/BZPM-REDESIGN-ARCHITECTURE-v1.md` | Delivery summary zones |
| `reports/SITE-002-WAVE-1A-IMPLEMENTATION-MAP-v1.md` | `deliveryText` / USR-PDP-18 map |
| `knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md` §14 | Commercial Trust «nationwide delivery» card |
| `m7.1-launch-mode-work/.../footer.twig` | Nav links |
| `projects/website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-PROGRAM-v1.md` | Program registry |

---

*M9.14 Delivery — research registration only. No implementation authorized.*
