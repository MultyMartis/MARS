# BZPM M9.13 — About Company — Design Charter v1

**Milestone:** M9.13 — About Company / О компании  
**URL (TEST):** `/about`  
**Program:** BZPM Corporate Pages Program  
**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01`  
**Policy:** MANUAL UI REFINEMENTS ARE CANONICAL  
**Version:** v1  
**Status:** **DESIGN CHARTER — PENDING OPERATOR APPROVAL**  
**Date:** 2026-06-22  

**Boundary:** Design planning and visual-commitment rules only. This document does **not** authorize wireframes, mockups, HTML/CSS/JS, deploy, or TEST writes.

**Sources of truth:**

| Artefact | Path |
|----------|------|
| Design Program | [BZPM-CORPORATE-PAGES-DESIGN-PROGRAM-v1.md](../BZPM-CORPORATE-PAGES-DESIGN-PROGRAM-v1.md) |
| IA Map | [BZPM-CORPORATE-PAGES-IA-MAP-v1.md](../BZPM-CORPORATE-PAGES-IA-MAP-v1.md) § M9.13 |
| Approved copy | [BZPM-M9.13-ABOUT-COMPANY-PAGE-COPY-v1.1.md](../../../ocpilot/sites/site-002/copy/BZPM-M9.13-ABOUT-COMPANY-PAGE-COPY-v1.1.md) |
| Forensic research | [BZPM-M9.13-ABOUT-COMPANY-FORENSIC-RESEARCH.md](../../../ocpilot/sites/site-002/reports/BZPM-M9.13-ABOUT-COMPANY-FORENSIC-RESEARCH.md) |
| Contacts reference surface | [SITE-002-CONTACTS-PAGE-MAIN-REDESIGN-IMPLEMENTATION.md](../../../ocpilot/sites/site-002/reports/SITE-002-CONTACTS-PAGE-MAIN-REDESIGN-IMPLEMENTATION.md) · [SITE-002-CONTACTS-PAGE-POLISH-V1.md](../../../ocpilot/sites/site-002/reports/SITE-002-CONTACTS-PAGE-POLISH-V1.md) |

**Primary design question:** *Почему этой компании можно доверить закупку оборудования?*

---

## 1. Purpose

### 1.1 Page mission

M9.13 `/about` is the **primary trust anchor** for SITE-002 — not a corporate presentation, not a company-history article, not an SEO landing.

The page must answer vendor-legitimacy objections for B2B buyers **before** they enter Payment, Delivery, or catalog evaluation. It owns **entity narrative** and **OEM proof** per IA CP-01.

### 1.2 What this page is NOT

| Anti-goal | Reason |
|-----------|--------|
| Corporate anniversary / «история с 2010» showcase | History is supporting context only — not the visual story |
| Long-form article for search engines | Copy is structured for procurement verification, not keyword density |
| Factory marketing brochure | No stock photography, no vanity metrics, no unlabeled badges |
| Duplicate of homepage advantages | Visual and rhetorical dedup required vs homepage trust blocks |
| Substitute for Payment / Delivery / Warranty / Dealers / Custom / Contacts | One-line summaries + links only (CP-01) |

### 1.3 What this page IS

The **strongest trust page** on SITE-002: a scannable evidence stack that proves ЗПМ is a **real manufacturer** with **verifiable facts**, **documented conformity path**, and **clear escalation to a human**.

---

## 2. Audience

| Segment | Priority | What they need from design |
|---------|----------|----------------------------|
| **Владелец бизнеса** | Primary | Fast OEM legitimacy — «не перекуп» before first deal |
| **Снабженец / закупщик** | Primary | Checkable facts: ИНН, адрес цеха, документы, тендерная пригодность |
| **Проектировщик / инженер** | Secondary | Production capability, geography, custom path pointer |
| **Дилер / оптовик** | Tertiary | Factory-vs-intermediary proof — channel terms deferred to `/dealers` |

**Design implication:** Layout must reward **scan-and-verify** behaviour (labels, facts, links to proof), not emotional brand storytelling.

---

## 3. Conversion goals

### 3.1 Primary

**Reduce skepticism about manufacturer legitimacy** → visitor accepts ЗПМ as credible OEM → **submits «Задать вопрос» form** or initiates contact via phone/email from BLOCK 11.

Success signal: user reaches form with trust objections already resolved by on-page evidence.

### 3.2 Secondary

**Catalog exploration** — visitor proceeds to neutral equipment evaluation via «Перейти в каталог» when trust is established but SKU selection is the next step.

### 3.3 Tertiary

**Contacts / requisites verification** — visitor jumps to `/contact/` for ИНН/КПП/address confirmation or general inquiry when form is not the preferred channel.

**Rule:** Tertiary must remain visible in CTA band but must **not** compete visually with primary form submit.

---

## 4. Trust goals

| # | Trust goal | Design must deliver |
|---|------------|---------------------|
| T1 | **Manufacturer, not reseller** | ИНН, ОГРН, production address scannable without scroll hunt |
| T2 | **Real production footprint** | Барнаул site + factory media (photo or video fallback) |
| T3 | **Procurement-ready documentation** | Cert types + «Сделано в России» **labeled** with disclaimer |
| T4 | **National supply credibility** | Russia coverage without duplicating Delivery tables |
| T5 | **Human escalation path** | Form + phone + email — same discipline as Contacts delivered page |
| T6 | **Honest boundaries** | No fake SLA, no warranty months, no ПП №719 universal claim |

---

## 5. Page role in buyer journey

### 5.1 Journey position

```
Catalog doubt / Commercial Trust «кто вы?»
        │
        ▼
   ┌─────────┐
   │  ABOUT  │  ◄── trust anchor (this page)
   └────┬────┘
        │
   ┌────┴────────────────────────────┐
   │                                 │
   ▼                                 ▼
Payment + Delivery              Catalog / Custom
(transaction path)              (product path)
        │
        ▼
   Contacts (requisites fallback)
```

### 5.2 Typical entry paths

| Entry | User state | Page must do |
|-------|------------|--------------|
| Header «О компании» | Exploratory | Establish OEM in first screen |
| Commercial Trust FAQ | Skeptical | Match FAQ themes — no dead-end |
| Post-catalog hesitation | Evaluating vendor | Proof layer before returning to PLP |
| Dealer candidate | Channel check | Confirm factory; pointer to `/dealers` only |

### 5.3 Exit paths (intended)

| Exit | When |
|------|------|
| Form submit | Trust + specific question |
| `/` catalog | Trust + ready to browse SKUs |
| `/contact/` | Need requisites / map / callback |
| `/payment-methods`, `/delivery`, `/guarantee`, `/custom-equipment`, `/dealers` | Need policy depth — **link only** |
| `/our-certification` | Need cert document depth |

---

## 6. Relationship with sibling pages

CP-01 rule: **one primary owner per topic**. About may show **one-line summary + text link** — never embedded foreign page body.

| Page | URL | About relationship | Allowed on About | Forbidden on About |
|------|-----|-------------------|------------------|-------------------|
| **Payment** | `/payment-methods` | Process step 3 in BLOCK 06; FAQ 4 | «Счёт, КП, закрывающие» summary + link | VAT %, bank table, methods matrix |
| **Delivery** | `/delivery` | BLOCK 06 step 5; BLOCK 08 geo; FAQ 2 | Shipment points (region level); «самовывоз / ТК» summary + link | TK pricing, lead times, МО street address |
| **Warranty** | `/guarantee` | BLOCK 02 H3; BLOCK 06 step 6; FAQ implicit | «Гарантия производителя» — **no term badge** | Months chip, RMA process, SLA |
| **Dealers** | `/dealers` | BLOCK 06 audience note; BLOCK 09 seg. 6; optional teaser strip | «Партнёрская программа» one line + link | Discounts, territory, MOQ, partner logos |
| **Custom** | `/custom-equipment` | BLOCK 02, 05, FAQ 8 | «Изготовление на заказ» summary + link | TZ checklist, parameter matrix, upload form |
| **Contacts** | `/contact/` | Trust row, BLOCK 01, 04, 07, CTA tertiary | ИНН/ОГРН summary + link for full requisites | Full requisites panel, map embed, contact card grid |
| **Certification** | `/our-certification` | BLOCK 07, BLOCK 04 fact, FAQ 5 | Cert type labels + deep link | PDF wall, full cert gallery |

**Contacts alignment:** Form field set, consent pattern, success microcopy, and phone/email presentation must **match** delivered Contacts page (`zpm-contact-*` / `blockanyquestionsform` discipline) — adapted to About form copy (extra `question` field).

---

## 7. Required evidence hierarchy

Evidence is ranked by **procurement decision weight** — what a закупщик checks first.

### Level 1 — Must be visible without deep scroll (first ~2 viewports)

| Evidence | Copy source | Visual commitment |
|----------|-------------|-------------------|
| Legal entity + ИНН + ОГРН | BLOCK 01 body, trust row | SC-03 trust row — **dominant micro-scan strip** |
| «Производитель, не перекуп» | BLOCK 01 H2 + lead | H1 zone + lead — typographic clarity |
| Production location (Барнаул, Калинина 15в) | BLOCK 01 trust row; BLOCK 03 | Trust row + factory media |
| Factory / workshop media | Hero + BLOCK 03 | **Static photo required**; video optional overlay (see §15) |

### Level 2 — Core proof stack (mid-page, scroll expected)

| Evidence | Copy source | Visual commitment |
|----------|-------------|-------------------|
| Trust facts table (7 rows) | BLOCK 04 | Proof card / fact row — **dense but scannable** |
| «Сделано в России» + СС.002662 | BLOCK 04; BLOCK 07 | Labeled fact + cert promo block — **not hero badge** |
| Capability cards (4) | BLOCK 03 | Equal-weight card grid |
| Document framework | BLOCK 07 | SC-14 cert promo — structured, link-out |
| Process overview (6 steps) | BLOCK 06 | SC-04 timeline — informational, not checkout UX |

### Level 3 — Supporting context (lower visual weight)

| Evidence | Copy source | Visual commitment |
|----------|-------------|-------------------|
| «Почему выбирают» H3 stack (7) | BLOCK 02 | Segment list — **below** Level 1–2 proof |
| Product scope prose | BLOCK 05 | Text block — no SKU grid |
| Audience segments (6) | BLOCK 09 | SC-13 matrix — 2–4 col grid |
| Geography Russia + 2 points | BLOCK 08 | SC-15 — list prose default; map only if operator asset |
| FAQ (8) | BLOCK 10 | SC-08 accordion — objection cleanup |
| Founded 2010 | BLOCK 01, 03 | Inline prose — **no anniversary timeline** |

---

## 8. Visual narrative

Narrative arc is **verification**, not storytelling.

### Beginning — «Кто вы и можно ли проверить?» (Utility → BLOCK 01)

| Beat | Content | Emphasis |
|------|---------|----------|
| Orient | Breadcrumb, H1, lead | Clean internal-page rhythm — align Contacts shell (SC-01) |
| Identity | BLOCK 01 «Кто мы» + trust row + main image | **Trust row + legal facts dominate** |
| First impression media | Hero / BLOCK 01 image | Real factory — not stock; caption attested |

**Beginning must answer Q1 (производитель или перекуп?) in <5 seconds of scan.**

### Middle — «Докажите производство и документы» (BLOCK 02 → BLOCK 08)

| Beat | Content | Emphasis |
|------|---------|----------|
| Rationale | BLOCK 02 advantages | Supporting — buyer-benefit framing after identity lock |
| Production proof | BLOCK 03 + optional video | Workshop credibility — capability cards |
| Fact layer | BLOCK 04 trust facts | **Peak proof density** — visual anchor of middle |
| Scope + process | BLOCK 05, 06 | Operational clarity — links to sibling pages |
| Compliance | BLOCK 07 cert promo | SC-14 — structured; disclaimer visible |
| Reach | BLOCK 08 geography | Russia supply — defer logistics detail to Delivery |

**Middle must answer Q2–Q5 from IA without leaving page (except cert depth link).**

### End — «Снимите оставшиеся возражения и дайте контакт» (BLOCK 09 → FORM)

| Beat | Content | Emphasis |
|------|---------|----------|
| Fit | BLOCK 09 audience | Segmentation — who this factory serves |
| Objections | BLOCK 10 FAQ | Compact accordion — not article body |
| Action | BLOCK 11 CTA + FORM | **Primary conversion zone** — form is visual endpoint |

**End must make escalation obvious: form primary, phone/email support, catalog secondary.**

---

## 9. Content hierarchy — copy blocks

Ranking for **all approved v1.1 blocks** (Critical / Important / Supporting).

| Block | Title | Rank | Rationale |
|-------|-------|------|-----------|
| Utility | Meta, breadcrumb | Supporting | Required shell — no visual competition |
| — | H1 + Lead | **Critical** | First trust statement |
| **01** | Кто мы | **Critical** | Identity + SC-03 trust row |
| **02** | Почему компании выбирают ЗПМ | Important | Benefit framing — after proof hooks |
| **03** | Производство и возможности | **Critical** | Factory evidence + capability cards + video slot |
| **04** | Почему нам доверяют | **Critical** | Dense verifiable facts — peak trust |
| **05** | Что производим | Important | Scope boundary — not catalog |
| **06** | Как работаем с заказчиками | Important | Journey map — links out |
| **07** | Документы и соответствие | **Critical** | Cert + compliance — procurement gate |
| **08** | География поставок | Important | Supply reach — Delivery link |
| **09** | Для кого работаем | Supporting | Audience matrix — segmentation |
| **10** | FAQ | Important | Objection resolver — pre-CTA |
| **11** | CTA | **Critical** | Conversion band |
| FORM | Задать вопрос | **Critical** | Primary conversion instrument |

---

## 10. Block importance map

Visual weight budget (relative — not pixel spec).

| Block | Importance tier | Visual weight (1–5) | Notes |
|-------|-----------------|---------------------|-------|
| **01** | Tier 1 — Anchor | **5** | Trust row must be most scannable element after H1 |
| **04** | Tier 1 — Anchor | **5** | Fact layer — equal prominence to BLOCK 01 proof |
| **03** | Tier 1 — Anchor | **4** | Factory media + 4 capability cards |
| **07** | Tier 1 — Anchor | **4** | Cert promo — structured block, not banner |
| **11 + FORM** | Tier 1 — Anchor | **4** | CTA band + form — page endpoint |
| **02** | Tier 2 — Support | **3** | Seven H3s — readable list, not hero cards |
| **06** | Tier 2 — Support | **3** | SC-04 timeline — shared corp pattern |
| **08** | Tier 2 — Support | **2** | Geo — prose/list default |
| **10** | Tier 2 — Support | **3** | FAQ — full width accordion |
| **05** | Tier 3 — Context | **2** | Prose — no product cards |
| **09** | Tier 3 — Context | **2** | Segment grid — lighter than BLOCK 02 |
| Hero media (pre-01 or in 01) | Tier 1 | **4** | Static-first; see §15 |

**Section rhythm:** Tier 1 blocks need **clear vertical separation** (consistent corp section spacing — lock with Contacts internal-page rhythm). Avoid 11 equal-weight sections — prevents scroll fatigue.

---

## 11. Visual emphasis strategy

### 11.1 What MUST dominate visually

| Element | Why |
|---------|-----|
| SC-03 trust row (BLOCK 01) | Fast OEM scan |
| BLOCK 04 trust facts | Verifiable procurement checklist |
| Factory photo (hero / BLOCK 01 / BLOCK 03) | «Real place» evidence |
| BLOCK 07 cert block + disclaimer | Compliance without overclaim |
| BLOCK 11 + form | Conversion |
| Inline links to Contacts for verification | «Проверьте сами» pattern |

### 11.2 What must NOT dominate visually

| Element | Why |
|---------|-----|
| «Основаны в 2010» | Supporting fact — not anniversary hero |
| BLOCK 02 seven H3 advantages | Risk duplicating homepage — keep subordinate |
| BLOCK 09 audience grid | Segmentation — not primary proof |
| «Сделано в России» badge alone | Must not float as unlabeled legal proof |
| Video player chrome | Enhancement only — must not block static fallback |
| Dealer teaser | One line — not partner marketing block |
| Product category names | No pseudo-catalog |
| Numeric metrics (5×, 15×, warranty months) | Not in copy — forbidden |

### 11.3 Contacts reference surface — reuse rules

From delivered Contacts page — **patterns to inherit**, not duplicate content:

| Pattern | Contacts evidence | About use |
|---------|-------------------|-----------|
| Internal-page rhythm | Breadcrumb → H1 → sections | SC-01 shell |
| Card grid discipline | `zpm-contact-cards` 4-col | Adapt for capability cards (BLOCK 03) and trust facts (BLOCK 04) — **not** contact cards |
| Summary card | Logo + compact facts | BLOCK 01 image + trust row — richer proof |
| Form card | Center column form | SC-10 — same consent/field hooks |
| Icon language | FA5 Pro Duotone (`fad`) | Consistent icon weight for trust row / facts |
| Mobile stack ≤1024px | Single column order | Mandatory for 11-block page |

**Do not embed:** Yandex map, requisites panel, messenger row, contact card grid — those remain Contacts-owned.

---

## 12. CTA strategy

### 12.1 Hierarchy (locked)

| Priority | Element | Placement |
|----------|---------|-----------|
| **Primary** | «Отправить вопрос» → form submit | BLOCK 11 + FORM only |
| **Secondary** | «Перейти в каталог» | BLOCK 11 text/button — subordinate |
| **Tertiary** | «Контакты и реквизиты» | BLOCK 11 link |
| **Support** | Phone `8 (3852) 72-18-90` · `info@bzpm.ru` | BLOCK 11 inline — always visible in CTA zone |

### 12.2 CTA frequency — charter decision

| Zone | Buttons | Links |
|------|---------|-------|
| Hero / BLOCK 01 | **None** | Contacts link in body only |
| BLOCK 02 proof strip | **None** | 3 text links (catalog, custom, contacts) |
| BLOCK 03 video | **Optional** «Смотреть дальше» scroll — **not** conversion CTA | — |
| BLOCK 04–09 | **None** | Inline cross-links per copy |
| BLOCK 10 FAQ | **None** | Links inside answers |
| BLOCK 11 + FORM | **Primary button** + secondary/tertiary | — |

**Rule:** **One primary button CTA zone** per page (BLOCK 11). No mid-page «Отправить» buttons — reduces trust-education interruption.

### 12.3 CTA appearance timing

CTA band appears **after** FAQ (BLOCK 10) — user has consumed evidence stack. Form immediately follows CTA band (or integrated in same visual zone per SC-09).

---

## 13. FAQ strategy

### 13.1 Role

FAQ is an **objection resolver**, not primary content. It catches residual doubts after BLOCK 01–09.

### 13.2 Depth — charter decision

| Parameter | Decision |
|-----------|----------|
| Count | **8 items** — per approved copy; do not expand |
| Pattern | SC-08 single-open accordion |
| Position | After BLOCK 09, before BLOCK 11 |
| Visual weight | Important but **subordinate** to BLOCK 04 and BLOCK 07 |
| SEO posture | Not optimized as article — no FAQ schema over-design in charter phase |

### 13.3 Priority FAQ items (if space constrained on mobile)

| Priority | FAQ | Why |
|----------|-----|-----|
| 1 | Производитель или перекупщик? | Core Q1 |
| 2 | Где производство? | Core Q2 |
| 3 | Что означает «Сделано в России»? | Cert boundary |
| 4 | Какие документы при закупке? | Procurement |
| 5–8 | Remaining | Standard depth |

### 13.4 Overlap discipline

FAQ answers must **not repeat** full BLOCK 04 fact table — accordion gives short confirmatory answers with links to owners (Delivery, Payment, etc.).

---

## 14. Certificate strategy

Research and copy attestation:

| Item | Value |
|------|-------|
| Program | «Сделано в России» — добровольная сертификация РЭЦ |
| Registration | **СС.002662** |
| Validity | 20.10.2025 – 19.10.2028 |
| Deep link | `/our-certification` |

### 14.1 Importance

| Level | Treatment |
|-------|-----------|
| Strategic | **High** — key differentiator for Russian procurement |
| Legal | **Bounded** — disclaimer mandatory; not ПП №719 substitute |
| Visual | **Medium-high** in BLOCK 07; **medium** as fact row in BLOCK 04 |

### 14.2 Visibility rules

| Surface | Rule |
|---------|------|
| Trust row (BLOCK 01) | **Exclude** «Сделано в России» from SC-03 four labels — keep row for entity/geo/specialization |
| BLOCK 04 fact table | **Include** as one labeled row with registration number |
| BLOCK 07 | **Primary cert surface** — SC-14 promo: type labels, number, dates, disclaimer, link |
| Hero / page top | **No** large floating badge |
| Header site badge | If site header already shows badge — page block **references** it in BLOCK 07, does not duplicate giant badge |
| FAQ 5 | Text confirmation — links to BLOCK 07 anchor conceptually |

### 14.3 Position philosophy

**Certificate narrative belongs in the compliance chapter (BLOCK 07), not the identity chapter (BLOCK 01).**

Flow: identity (who) → production (where/how) → facts (BLOCK 04 includes cert as checkable row) → **documents deep block (BLOCK 07)** with disclaimer → FAQ reinforces.

**Forbidden:** Cert promo as first screen; PDF thumbnails without operator assets; ПП №719 badge; «госзакупка guaranteed» visuals.

---

## 15. Video strategy

### 15.1 Forensic context

Live TEST has `.about-page-video` + `[data-scroll-next]` scroll interaction. Video file and poster frame: **SAFE UNKNOWN**.

### 15.2 Charter decision — Video vs Static Hero

| Mode | Status |
|------|--------|
| **Static factory photo** | **REQUIRED** — default hero and BLOCK 03 media |
| **Video** | **OPTIONAL ENHANCEMENT** — only if operator supplies attested file + poster |
| **Video-only hero** | **FORBIDDEN** without static fallback |

### 15.3 Implementation rules (for future design pass)

| Rule | Detail |
|------|--------|
| Fallback | Same frame as poster image — always visible without JS |
| Placement | BLOCK 03 video slot — **not** replacing BLOCK 01 trust scan |
| Scroll button | «Смотреть дальше» — navigation enhancement only; `prefers-reduced-motion` disables auto-motion |
| Dominance | Video container ≤ BLOCK 03 weight — subordinate to trust row and BLOCK 04 |
| Missing asset | Ship static photo + caption; hide empty video element |

### 15.4 Hero structure decision

**Split hero model:**

1. **Above fold:** H1 + lead + BLOCK 01 trust row + supporting factory still (BLOCK 01 image) — **static-first**.
2. **BLOCK 03:** Optional video embed with static poster parity.

**Reject:** Full-viewport autoplay video hero that delays trust row scan.

---

## 16. Proof strategy

### 16.1 Facts deserving visual emphasis

| Fact | Emphasis treatment |
|------|-------------------|
| ИНН 2221237587, ОГРН 1172225049787 | Trust row + BLOCK 04 row — monospace or tabular scan |
| Барнаул, пр. Калинина, 15в | Trust row + BLOCK 03 + BLOCK 04 |
| Собственное производство | Trust row label + BLOCK 04 + capability card |
| СС.002662 + dates | BLOCK 04 row + BLOCK 07 promo |
| Direct factory (not reseller) | BLOCK 01 lead + BLOCK 04 row |
| Russia supply | BLOCK 04 + BLOCK 08 |

### 16.2 Facts that stay text-only (no badge/chip)

| Fact | Why |
|------|-----|
| Founded 2010 | Context — no «15 лет» hero stat |
| СНГ supply | FAQ/geo prose — individual conditions |
| Warehouse stock | FAQ 7 — links to catalog |
| Partner МО warehouse | Region only — address on Delivery |
| Manager response time | SAFE UNKNOWN — no SLA chip |

### 16.3 Proof card strategy — charter decision

| Block | Pattern | Card count |
|-------|---------|------------|
| BLOCK 03 | SC-05 variant — **capability cards** | 4 equal cards |
| BLOCK 04 | **Trust fact rows** — not marketing cards | 7 rows — icon + label + statement |
| BLOCK 02 | **No cards** — H3 list | 0 |
| BLOCK 09 | SC-13 segment matrix | 6 segments — lighter cards |

**BLOCK 04 vs BLOCK 03:** BLOCK 04 is **checklist semantics** (verify); BLOCK 03 is **capability semantics** (how). Visual language may share card grid component but BLOCK 04 must read denser and more «audit-like».

---

## 17. Special requirement resolutions

### 17.1 Trust row strategy (SC-03)

| Decision | Detail |
|----------|--------|
| Placement | Immediately under BLOCK 01 body — **before** long prose scroll |
| Labels | 4 locked: Юридическое лицо · Бренд · Производство · Специализация |
| Icons | Icon + short label — FA duotone parity with Contacts |
| Tooltips | Optional for legal name expansion — not required in v1 |
| Exclusions | No warranty months, no VAT, no «Сделано в России» in this row |

### 17.2 Dealer teaser — include or exclude?

| Decision | **INCLUDE minimal — EXCLUDE as block** |
|----------|----------------------------------------|
| Rationale | Dealer audience is tertiary; full teaser strip competes with trust endpoint |
| Implementation | Use **copy-existing** pointer in BLOCK 06 audience note + BLOCK 09 segment 6 |
| Optional strip | **One line** SC-12 between BLOCK 10 and BLOCK 11: «Работаете с общепитом в регионе?» + link — **text only**, no logo row |
| Forbidden | Partner logos, territory map, discount hints, duplicate `/dealers` body |

### 17.3 Shared components instantiated on About

| ID | Component | About blocks |
|----|-----------|--------------|
| SC-01 | Corp page shell | All |
| SC-02 | Hero / media | BLOCK 01 image; BLOCK 03 video |
| SC-03 | Trust row | BLOCK 01 |
| SC-04 | Process timeline | BLOCK 06 |
| SC-05 | Proof / fact cards | BLOCK 03, BLOCK 04 |
| SC-08 | FAQ accordion | BLOCK 10 |
| SC-09 | CTA band | BLOCK 11 |
| SC-10 | Corp inquiry form | FORM |
| SC-12 | Cross-link inline | Body links + optional dealer strip |
| SC-13 | Partner / segment matrix | BLOCK 09 |
| SC-14 | Cert promo | BLOCK 07 |
| SC-15 | Geography | BLOCK 08 |

---

## 18. Design risks

| ID | Risk | Severity | Mitigation |
|----|------|----------|------------|
| R1 | Video asset missing → placeholder drift | **High** | Static-first mandate (§15) |
| R2 | 11 blocks → scroll fatigue | **High** | Tier 1/2/3 weight map (§10); section spacing |
| R3 | Duplicate homepage advantages | **Medium** | BLOCK 02 subordinate; visual dedup review in design pass |
| R4 | Legacy `.about-page--*` CSS conflicts | **Medium** | Reconcile or namespace in implementation charter — not hybrid |
| R5 | Cert block duplicates PLP Commercial Trust | **Medium** | SC-14 summary only; link `/our-certification` |
| R6 | «Сделано в России» overclaim | **High** | Disclaimer always visible in BLOCK 07 |
| R7 | Long page mobile form abandonment | **Medium** | CTA only at end; phone visible in BLOCK 11 |
| R8 | МО warehouse address conflict | **Low on About** | Region-only per copy; defer street to M9.14 charter |
| R9 | Live content drift (5×/15× metrics) | **Medium** | Copy v1.1 excludes — design must not reintroduce |
| R10 | Form backend UNKNOWN (Contacts pattern) | **Medium** | Same `action="#"` posture until implementation charter |

---

## 19. Forbidden patterns

| Pattern | Why forbidden |
|---------|---------------|
| Company anniversary / «юбилей» hero | Shifts focus from procurement trust |
| History timeline with year milestones | Corporate presentation anti-goal |
| Giant management portrait / team gallery | No copy support; vanity |
| Corporate stock photography | Asset rule — real factory only |
| SEO article layout (long prose columns, TOC) | Anti-goal |
| Banner carousel | No attested content slides |
| Vanity metrics without proof (5×, 15×, «N клиентов») | Not in approved copy |
| ПП №719 universal compliance badge | Legal overclaim |
| Unlabeled «Сделано в России» as tender guarantee | Disclaimer required |
| Warranty term chip («12 мес») | Owner: M9.17 — OQ locked |
| VAT / bank requisites panel | Owner: Payment / Contacts |
| SKU grid / price cards | Owner: Catalog |
| TK freight tables / delivery calculator | Owner: Delivery |
| Dealer discount tiers / territory map | Owner: Dealers |
| Full cert PDF wall | Owner: `/our-certification` |
| Multiple competing primary CTAs mid-page | §12 frequency rule |
| Fake client logos | Operator asset required |
| Autoplay sound video | UX + no asset |

---

## 20. Success criteria

Operator judges About design **successful** when:

| # | Criterion | Verification method |
|---|-----------|---------------------|
| S1 | Visitor answers IA Q1–Q5 on-page (except cert doc depth) | Copy coverage audit vs IA map |
| S2 | Trust row scannable in **<5 seconds** at desktop and mobile | Operator scan test |
| S3 | BLOCK 04 + BLOCK 07 readable as «procurement checklist» | Operator review |
| S4 | No CP-01 violations — sibling topics are links only | Cross-link audit |
| S5 | Form matches Contacts consent/field discipline | Side-by-side with `/contact/` |
| S6 | Static factory media works with JS disabled | Progressive enhancement check |
| S7 | «Сделано в России» shows number + disclaimer — no ПП №719 implication | Copy fidelity check |
| S8 | One primary CTA zone — no mid-page submit buttons | Design review |
| S9 | Page does not feel like homepage duplicate | Operator visual compare |
| S10 | Mobile ≤1024px — no horizontal scroll trap on fact rows | Responsive check |
| S11 | `prefers-reduced-motion` respected on video scroll | Accessibility check |
| S12 | Design charter approved **before** any wireframe/mockup work | Phase gate |

---

## 21. Open questions (operator lock)

| ID | Question | Impact | Default if unresolved |
|----|----------|--------|----------------------|
| OQ-DC01 | Factory photo asset — operator-provided or live capture? | Hero + BLOCK 03 | Static capture from production — **no** stock |
| OQ-DC02 | Video file + poster — supply or omit? | BLOCK 03 | **Omit video** — static only |
| OQ-DC03 | Geography map image for BLOCK 08? | SC-15 | **List prose only** |
| OQ-DC04 | Catalog CTA URL — `/` vs neutral hub | BLOCK 11 secondary | `/` per copy note |
| OQ-DC05 | Optional dealer strip before CTA — include? | SC-12 | **Include** one-line strip per copy microcopy |
| OQ-DC06 | Legacy `.about-page--*` — refactor vs new `zpm-about-*` namespace? | Implementation | Defer to implementation charter |
| OQ-DC07 | BLOCK 01 image vs separate hero media block? | SC-02 layout | **Combined** — image in BLOCK 01 zone, no extra hero |
| OQ-DC08 | Client / project logos — any operator assets? | Social proof | **Exclude** — none attested |
| OQ-DC09 | Privacy policy route `/privacy-policy` | Form consent | Verify at implementation — assumed per copy |

---

## 22. Design readiness verdict

| Dimension | Status | Notes |
|-----------|--------|-------|
| Copy | **READY** | v1.1 complete — operator approval header pending |
| IA | **READY** | CP-01 boundaries locked |
| Charter | **READY FOR OPERATOR REVIEW** | This document |
| Assets | **PARTIAL** | Factory photo required; video optional; map optional |
| OQ | **PARTIAL** | §21 deferrals — none block charter approval |
| Visual design | **NOT READY** | Awaits operator charter approval |
| Implementation | **NOT READY** | Awaits design approval + implementation charter |

**Verdict:** M9.13 About Company is **PARTIAL DESIGN READY** — charter pass complete; operator may approve charter and authorize **visual design phase** with explicit asset deferrals (static-first hero, no video until supplied).

**Explicit stop:** No wireframes · no mockups · no Twig/CSS/JS · no deploy.

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-22 | **CREATED** — Design Charter v1; resolves video/static, cert placement, dealer teaser, trust row, proof cards, FAQ depth, CTA frequency |

---

*BZPM M9.13 About Company Design Charter v1 — documentation only. No design, wireframes, mockups, or implementation authorized.*
