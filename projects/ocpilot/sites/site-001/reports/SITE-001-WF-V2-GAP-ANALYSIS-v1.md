# REPORT — SITE-001 WF V2 GAP ANALYSIS

**Type:** Comparative visual audit — documentation only  
**Date:** 2026-06-10  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Baseline:** **Visual Baseline V1** (Phase 1 + W3-V/V2/UX-C1/ATMOSPHERE + W4/W4.1 + W5-A/S + W5-C)  
**Target:** **WF V2 Concept** — `projects/ocpilot/sites/site-001/design/wf-v2-concept/`

**Design authority reviewed:**

| File | Role |
|------|------|
| `01-sibcar-v2-concept.png` | Целевая композиция (header + used PDP + контентные зоны) |
| `02-sibcar-v2-specification.png` | Техническая спецификация «Clean Header» + принципы минимализма |

**Evidence (live, 2026-06-10):**

- HTTP fetch: `/`, `/cars/`, used PDP `/audi-a1-2012-s-probegom-149-000-km-799`
- Live `/css/main.css` — **173 031 bytes** (W3ATMOSPHERE + W4.1 + W5-A + W5-A-S + W5-C markers confirmed)
- Execution reports: W5-A, W5-A-S, W5-C
- **No FTP · No CSS · No Twig · No implementation**

**Spec note:** В референсах есть расхождение по тону header: mock `01` показывает тёмный header, spec `02` задаёт **светлый** contact rail `#F7F8FA` + **белый** primary band `#FFFFFF`. Для аудита header **приоритет у spec `02`** (явные токены и anti-pattern list). Mock `01` используется для композиции PDP и общего «clean showroom» ритма.

---

## Executive summary

| Dimension | Current state (V1) | Target state (WF V2) | Gap severity |
|-----------|-------------------|----------------------|--------------|
| **Visual class** | «Стилизованный OpenCart-шаблон автосалона» — многослойные override-волны, тёмный dealer chrome, card-in-card | «Light clean modern showroom» — flat surfaces, thin dividers, один контейнер на зону, минимум теней | **CRITICAL** |
| **Header** | W5-A shell live: contact rail белый, primary band **graphite gradient**, promo **dark inset**, phone/WA **дублируются** | Светлый rail + белый band + светлый promo; контакты **только** в rail; один red CTA | **HIGH** |
| **Homepage hero** | Swiper carousel + мелкий promo copy + four_blocks — **без изменений** W5-B | Stable headline + floating search card + featured peek | **CRITICAL** (not started) |
| **Used PDP** | W5-C commercial stage — **nested cards + shadows**; H1 **над** hero; 50/50 columns | Flat offer scene; H1 интегрирован; меньше контейнеров; clean spec sheet | **HIGH** |
| **Catalog / forms / footer** | Legacy OC patterns + W3 atmosphere patches | Clean cards без `#d0d0d0` borders; light modals sitewide; simplified footer chrome | **MEDIUM–HIGH** |
| **Estimated implementation impact** | — | Full WF V2 alignment | **VERY HIGH** — частичный **reversal** W5-A/C surface direction + новая W5-B homepage + sitewide de-noising pass |

**Overall alignment score:** **~25–30 / 100** vs WF V2 Concept  
**Perception delta vs operator 3-second test:** Current ≈ **4/10** modern clean dealer · Target ≈ **8/10**

**Key paradox:** Последние волны W5-A/S/C двигали сайт к **«Modern Dealer / Graphite Salon»** (тёмный shell, raised panels, shadows). WF V2 Concept — **противоположный вектор**: **subtractive** design (убрать рамки, тени, вложенные карточки). Текущий TEST **активно противоречит** новому target по surface system, хотя **структурно** (centered nav, commercial stage wrapper, static header) частично совпадает.

---

## Methodology

Для каждой зоны:

1. **Совпадает** — уже близко к WF V2  
2. **Противоречит** — прямой конфликт с concept/spec  
3. **Удалить** — visual noise / legacy, не нужен в target  
4. **Перестроить** — сохранить функцию, сменить архитектуру/поверхность  
5. **Сохранить** — можно оставить с минимальной адаптацией

---

## 1. Header

### Current (live)

```
CONTACT RAIL — white #fff, thin dark border-bottom
  address · hours · phone · WhatsApp
PRIMARY BAND — graphite gradient #22252d → #1a1d24
  logo (inverted white) · centered nav (5+dropdowns) · callback + phone + WA
PROMO — sibling .lcd_display.header, dark #1a1d24, marquee CAPS inset
```

DOM: `w5a-header-shell` + W4.1 legacy classes. Static scroll (**OK**). Nav centered (**OK**).

### Target (WF V2 spec `02`)

```
CONTACT RAIL — #F7F8FA, text #6B7280, dividers #E5E7EB, h=44px
  address · hours · WhatsApp · phone (ONLY here)
PRIMARY BAND — #FFFFFF, h=72px
  logo · centered nav #111827 · ONE red CTA #E60000 «Перезвоните мне»
PROMO STRIP — #F3F4F6, h=40px, red «+» + trade-in message
```

**No** phone/WA in primary band. **No** shadows. **No** dark gradients.

| Category | Assessment |
|----------|------------|
| **Совпадает** | Трёхзонная семантика (rail / band / promo) · centered navigation · static header (W4.1 sticky reverted) · один primary callback CTA по weight · logo left anchor · menu items frozen · «Ещё» dropdown для density (W5-A-S) |
| **Противоречит** | Primary band **тёмный graphite** vs target **white** · contact rail **white** vs target **#F7F8FA** · promo **dark inset** vs target **light #F3F4F6 strip** · phone + WhatsApp **дублируются** в CTA cluster (spec: remove from primary) · logo `filter: invert(1)` — artifact тёмного band · W5-A-S dropdown `box-shadow: 0 12px 28px` — spec forbids decorative shadows · nav text white-on-dark vs #111827 on white |
| **Удалить** | Graphite gradient backgrounds on header zones · inverted logo filter · duplicate phone/WA in `.w5a-header__cta-cluster` (desktop) · dark promo marquee fade masks · legacy `w4-1-header` gradient rules where they fight clean spec · red glow/shadow on callback if present from base theme |
| **Перестроить** | Promo from **inset dark footer of shell** → **separate light strip** below header (spec DOM: promo outside `<header>` acceptable) · Contact rail palette + typography (14–15px / 500) · Primary band to flat white with 1px `#E5E7EB` bottom divider only · CTA cluster → **callback only** |
| **Сохранить** | `w5a-header-shell` DOM grouping · W5-A-S nav density (5 top + dropdowns) · tel:/wa.me links · offcanvas mobile menu · callback modal hook `#callback__FORM_popup` |

**Zone impact:** HIGH — header visible on every page; color/system mismatch = instant «not WF V2» signal.

---

## 2. Contact rail

| Category | Assessment |
|----------|------------|
| **Совпадает** | Address + hours left · channels right · compact single-line desktop layout · icons muted · semantic split meta/channels |
| **Противоречит** | Background `#ffffff` not `#F7F8FA` · text rgba(26,29,36,0.78) not `#6B7280` · border `rgba(26,29,36,0.08)` — OK direction but spec wants `#E5E7EB` system · hours format «c 9:00-21:00» vs spec «с 9:00 до 21:00» (copy, not visual — frozen) |
| **Удалить** | Extra contrast from adjacent dark primary band (creates harsh jump) · `duble_line_btns` hover animations if they add visual noise |
| **Перестроить** | Full token alignment to WF V2 rail · mobile wrap behavior per spec (single line collapse) |
| **Сохранить** | Twig structure `w5a-contact-rail__inner` · both channels in rail (correct per spec) |

**Zone impact:** MEDIUM alone · HIGH as part of header read.

---

## 3. Navigation

| Category | Assessment |
|----------|------------|
| **Совпадает** | Centered desktop nav · core items visible (Главная, Новые, Пробег, Услуги, Контакты) · dropdown pattern for overflow · hover red accent aligned with brand · no sticky |
| **Противоречит** | Nav rendered **white text on graphite** vs dark text on white · dropdown panel heavy shadow · split across two `<ul class="desck_menu">` — visual OK but legacy DOM · mobile duplicates phone/WA inside nav (`mobile_adaptive`) — acceptable for mobile but adds noise on tablet breakpoints |
| **Удалить** | Shadowed dropdown cards (replace with flat panel + 1px border) · legacy `w4-1-header__nav` gradient remnants |
| **Перестроить** | Nav typography to 15px / weight 500 / `#111827` · hover `#E60000` · simplify dropdown to flat list |
| **Сохранить** | Menu URLs and labels · W5-A-S «Ещё» grouping · offcanvas full list · services sub-menu |

**Zone impact:** MEDIUM.

---

## 4. Promo strip

| Category | Assessment |
|----------|------------|
| **Совпадает** | Trade-in message content · always visible below header · single message line · red accent on offer keywords (concept) |
| **Противоречит** | **Dark `#1a1d24` background** vs target **`#F3F4F6`** · CAPS marquee animation vs calm static strip in spec · inset inside graphite shell vs independent light band · white text on dark vs dark text on light · `margin`/`border-top` inset styling from W5-A-S |
| **Удалить** | Marquee ping-pong motion (spec shows static line) · dark fade `::before/::after` on marquee · graphite shared background with header |
| **Перестроить** | Standalone 40px light strip · red «+» icon prefix · typographic hierarchy 14px · optional: slow single-line scroll only if operator insists — not in static spec |
| **Сохранить** | `.lcd_display.header` DOM node (CSS-only re-skin possible) · promo copy · placement immediately below header |

**Zone impact:** HIGH — promo is first content-adjacent band; dark strip reinforces «old dealer ticker» not «clean 2026».

---

## 5. Homepage hero

| Category | Assessment |
|----------|------------|
| **Совпадает** | Full-width imagery · brand red CTA exists · vehicle photography quality · `header_cup` inside header (post W5-A fix) |
| **Противоречит** | **Swiper carousel-first** — WF V2 / prior Concept B both reject this · **No floating search card** · **No large stable headline** · micro promo text in slides · `four_blocks` icon grid immediately below · multiple competing CTAs (slide + header + hidden slider btn) · hero not 85vh showroom entry |
| **Удалить** | Carousel-as-primary-grammar (or demote to secondary) · decorative `home_slider_decor` elements · redundant callback on slides · four_blocks as dominant trust pattern below fold edge |
| **Перестроить** | Entire first screen architecture (W5-B never executed): headline zone + overlapping search + featured horizontal peek · stone/light canvas continuity with WF V2 |
| **Сохранить** | Slide photography assets (reusable as static hero background) · Swiper library (for featured row) · container grid system |

**Zone impact:** CRITICAL — homepage unchanged by W5; largest structural gap.

---

## 6. Used PDP

### Current (live + W5-C)

```
w4-1-pdp-top: breadcrumbs + H1 (above stage)
w5c-commercial-stage: gradient shell + border + shadow
  badges → w4-used-hero (card + shadow) → trust strip (nested status cards)
below: equipment card (shadow) · credit panel (dark + white inset) · bank logos
```

Gallery ~50% width inside card; offer column stacked: price · credit mini-card · 3 discount mini-cards · spec cells · 3 CTAs.

### Target (WF V2 concept `01` + clean principles `02`)

Flat light canvas · minimal outer containers · price as typographic anchor · specs as simple grid **without nested boxed cells** · trust as inline strip · credit form clean white · **reduce card-in-card** · H1 integrated with product area · fewer shadows/borders.

| Category | Assessment |
|----------|------------|
| **Совпадает** | Commercial content set (price, credit/mo, discounts, specs, CTAs, VIN trust, equipment, credit form) · W4 grouping preserved · gallery + thumbs · modal forms functional · badges for stock/state · brand red for primary actions · W5-C improved price typography (52px) |
| **Противоречит** | **`w5c-commercial-stage` outer shell**: border + `box-shadow: 0 20px 56px` + gradient — direct violation of «no shadows / no extra containers» · **`car_main_info` inner card** shadow `0 12px 40px` — card-in-card · **H1 in `w4-1-pdp-top` above stage** — catalog title pattern · **50/50 column split** not edge-dominant gallery · **3 discount mini-cards** each bordered+shadowed · **spec cells** individual white boxes with shadow · **credit price side-card** bordered+shadowed · **trust strip** 4 boxed pills · **equipment grid** bordered cells + outer card shadow · **credit panel** dark wrapper + nested white card + car image duplicate · **3 equal CTAs** — flat hierarchy |
| **Удалить** | Stage wrapper shadow/border/gradient (keep semantic grouping via spacing only) · nested shadows on hero/trust/equipment · discount as 3 separate cards → inline list or single row · duplicate car image in credit panel · heavy VIN button shadow · `w4-1-pdp-top` H1 band chrome |
| **Перестроить** | Hero to single flat surface: gallery dominant + offer column without nested card · H1 into gallery/product header zone · trust to simple inline status row · specs to borderless grid with dividers only · credit form to flat section (concept shows cleaner block) · reduce vertical chrome before vehicle |
| **Сохранить** | `w4-used-*` twig markers and JS hooks · Swiper/Fancybox · form POST endpoints · `#toggleConfigBtn` · W5-C modal light-theme pass on used PDP (direction OK, may simplify further) · price anchor sizing intent |

**Zone impact:** HIGH — W5-C moved opposite to WF V2 subtractive goal.

---

## 7. Catalog cards

Live `/cars/`: `.catalog_item` — `border: 1px solid rgb(208,208,208)`, `border-radius: 4px`, hover shadow; tags as mini boxed pills; nested price/old price; carousel per card.

| Category | Assessment |
|----------|------------|
| **Совпадает** | Card grid density (W3UX-C1) · photo-first · price prominent · in-stock tags · responsive 4-col |
| **Противоречит** | **#d0d0d0 borders** on every card · hover drop shadow · **tags as boxed chips** · **catalog_item__face** bottom border · legacy 4px radius · carousel arrows/pagination OC chrome · white card on `#EEF1F5` canvas = floating widget look |
| **Удалить** | Per-card borders (replace with gap-only grid or hairline divider) · hover shadow elevation · boxed tag backgrounds |
| **Перестроить** | Flat listing: image → title → meta → price flow on unified surface · align tag typography inline · match WF V2 catalog feel from concept (clean rows/cards without double frames) |
| **Сохранить** | Grid width system · swiper per card (functional) · price semantics · link structure |

**Zone impact:** MEDIUM–HIGH on catalog surfaces (high traffic).

---

## 8. Forms

**Inline:** credit panel on PDP — dark `#used_car__credit` shell, white inset, slider, inputs 52px (W5-C).  
**Modals:** used PDP modals light-themed (W5-C-I); **homepage/other pages** still default `.popup__FORM_wrap` — dark `#0e0f10`, `padding: 70px`, heavy shadow.

| Category | Assessment |
|----------|------------|
| **Совпадает** | Used PDP modal refresh (light shell, structured padding) · input heights · submit red · legal checkbox readable on used PDP |
| **Противorечит** | **Global modals dark** (callback/credit/trade-in on homepage/catalog) · excessive padding 70px · dark popup on light site · credit panel **dark band + nested white card** · base input borders `#d0d0d0` · legacy `border-radius: 4px` |
| **Удалить** | Dark modal theme sitewide · nested card in credit panel · thick popup shadows |
| **Перестроить** | All forms to light flat modal · inline credit to single-surface section · uniform 8–12px radius per WF V2 · focus rings not glow shadows |
| **Сохранить** | Fancybox integration · form field names/POST · success states · phone mask scripts |

**Zone impact:** MEDIUM (modals episodic) · HIGH on PDP credit section.

---

## 9. Modals

(See Forms.) Additional: `#VIN_report_popup.popup__big_FORM_wrap` — large dark report view; partner bank modals if any.

| Category | Assessment |
|----------|------------|
| **Совпадает** | W5-C scoped used-car lead modals |
| **Противorечит** | **Dual modal theme** (light on used PDP only vs dark everywhere else) · big VIN report popup legacy styling · inconsistent close button styling |
| **Удалить** | Dark theme split · 70px uniform padding legacy |
| **Перестроить** | Single WF V2 modal system across all `#*_FORM_popup` |
| **Сохранить** | Modal IDs and triggers (data-fancybox) |

**Zone impact:** MEDIUM.

---

## 10. Footer

Live: dark `#212429`, `box-shadow`, **10px top/bottom borders** `#0e0f10`, multi-column menus, duplicate CTAs, legal notice.

| Category | Assessment |
|----------|------------|
| **Совпадает** | Dark footer acceptable for closure (concept focuses header/PDP; spec header task excludes footer) · contact duplication for conversion · legal links present |
| **Противorечит** | Heavy **10px border slabs** · footer shadow · boxed partner bank carousel on homepage/PDP (not footer but related) · visual weight conflicts with WF V2 «light clean» body · `duble_line_btns row-reverse` legacy |
| **Удалить** | 10px border-top/bottom bands · footer box-shadow (if WF V2 extends to footer flattening) |
| **Перестроить** | Softer footer transition from light body · simplify columns spacing · align typography to WF V2 scale |
| **Сохранить** | Menu links · phone/address · legal copy · Phase 1 brand text |

**Zone impact:** LOW–MEDIUM (out of spec scope but contributes to overall noise).

---

## Cross-cutting visual noise audit

| Pattern | Current V1 | WF V2 target | Severity |
|---------|------------|--------------|----------|
| **Лишние borders** | `#d0d0d0` / `rgb(208,208,208)` on catalog cards, four_blocks, spec cells, discount cards, equipment cells, inputs | Thin `#E5E7EB` dividers only; no box borders on cards | **CRITICAL** |
| **Cards inside cards** | `w5c-commercial-stage` → `car_main_info` → offer/spec/discount cells; credit dark→white; catalog card→tags | Single surface per zone; spacing not nesting | **CRITICAL** |
| **Лишние shadows** | W5-C stage/hero/equipment; W3V2 shadow tokens; catalog hover; footer; dropdown; modals | **No decorative shadows** (spec explicit) | **CRITICAL** |
| **Visual noise** | 6+ override CSS layers (W3-V/V2/UX/ATMOSPHERE/W4.1/W5-A/S/C); competing reds; graphite + light canvas mix | Single `--wf-v2-*` clean system | **HIGH** |
| **Повторяющиеся контainers** | `.container>.row` + card wrappers at every section; PDP triple chrome (header+promo+pdp-top) | Flat sections with whitespace | **HIGH** |
| **OC template patterns** | Carousel homepage; 50/50 PDP; bordered catalog grid; dark popups; three-band header **dark variant** | Clean dealership 2026 | **HIGH** |

**CSS layer debt (live main.css):** Base theme (~7k lines) + W3-V + W3V2 + W3UX-C1 + W3ATMOSPHERE + W4 + W4.1 + W5-A + W5-A-S + W5-C ≈ **173 KB**. WF V2 implies **consolidation and subtraction**, not another append-only block.

---

## TOP-20 elements blocking WF V2 look

| Rank | Element | Zone | Why it blocks | Est. impact if fixed |
|------|---------|------|---------------|----------------------|
| **1** | Graphite dark primary header band (`#22252d` gradient) | Header | Instant «old dark dealer» vs WF V2 light shell | **VERY HIGH** |
| **2** | Dark promo strip `#1a1d24` marquee | Promo | Third dark band; ticker grammar | **VERY HIGH** |
| **3** | `w5c-commercial-stage` outer border + 20px shadow + gradient | Used PDP | Defines «card stack» aesthetic WF V2 forbids | **VERY HIGH** |
| **4** | Homepage Swiper promo carousel as first screen | Homepage | Core grammar mismatch; no search-first | **VERY HIGH** |
| **5** | H1 above hero (`w4-1-pdp-top`) | Used PDP | OC catalog page read | **HIGH** |
| **6** | `car_main_info` inner hero shadow card | Used PDP | Card-in-card | **HIGH** |
| **7** | Catalog `.catalog_item` `#d0d0d0` borders + hover shadow | Catalog | OC grid template signal | **HIGH** |
| **8** | Phone + WhatsApp duplicated in primary CTA cluster | Header | Violates spec; contact noise | **HIGH** |
| **9** | 3× discount mini-cards with borders/shadows | Used PDP | Offer block visual clutter | **HIGH** |
| **10** | Spec grid cells as individual boxed tiles | Used PDP | Cards-in-card in offer column | **HIGH** |
| **11** | Trust strip 4 boxed status cards | Used PDP | CRM table look | **MEDIUM–HIGH** |
| **12** | Dark `#0e0f10` global modals (non-PDP pages) | Modals | 2014 popup aesthetic | **MEDIUM–HIGH** |
| **13** | Credit panel dark wrapper + nested white inset + car image | Used PDP | Repeated container | **MEDIUM–HIGH** |
| **14** | `four_blocks` bordered icon grid on homepage | Homepage | Template trust grid below hero | **MEDIUM–HIGH** |
| **15** | Equipment grid bordered cells + outer shadow card | Used PDP | Spec sheet noise | **MEDIUM** |
| **16** | 50/50 gallery/offer column split | Used PDP | Not edge-dominant showroom | **MEDIUM** |
| **17** | Three equal-weight CTAs (credit/trade-in/installment) | Used PDP | Flat commercial hierarchy | **MEDIUM** |
| **18** | Footer 10px border slabs + shadow | Footer | Heavy chrome | **MEDIUM** |
| **19** | Partner bank logo boxes with borders | Homepage/PDP | Card-in-card micro-pattern | **MEDIUM** |
| **20** | Accumulated W3/W4/W5 conflicting surface tokens | Global | Unpredictable overrides; blocks clean system | **HIGH** (enabler) |

---

## Preservation map (do not discard blindly)

| Asset | Reason |
|-------|--------|
| W5-A DOM shell (rail / band / nav grouping) | Re-skin to light WF V2, not full DOM revert |
| W5-A-S nav density + «Ещё» | UX win; keep structure |
| W4 `w4-used-*` twig grouping | Content architecture; flatten surfaces |
| Phase 1 copy, URLs, phones, menu labels | Frozen |
| W3UX-C1 catalog density | Keep grid; change card surface |
| Static header (no sticky) | Matches WF V2 |
| W5-C modal light pass on used PDP | Extend sitewide |

---

## Estimated impact summary

| Workstream | Scope | Effort | Visual payoff |
|------------|-------|--------|---------------|
| **WF V2 Header** (rail + band + promo light system) | header.twig CSS | M | **VERY HIGH** |
| **WF V2 De-noising pass** (remove borders/shadows/nesting sitewide) | main.css consolidation | L | **VERY HIGH** |
| **WF V2 Homepage** (hero + search card) | home.twig + CSS | L | **VERY HIGH** |
| **WF V2 Used PDP flatten** (reverse W5-C surface excess) | product.twig CSS | L | **HIGH** |
| **WF V2 Catalog cards** | CSS (+ optional twig) | M | **HIGH** |
| **WF V2 Forms/modals unified** | CSS | M | **MEDIUM** |
| **CSS layer consolidation** (retire conflicting W3/W5 tokens) | governance | L | **HIGH** (maintainability) |

**Total estimated impact:** Aligning TEST to WF V2 is **not a tweak** — it is a **direction correction** from «Graphite Modern Dealer embellishment» to «Clean Minimal Showroom subtraction», plus **unfinished homepage architecture**.

---

## UNKNOWN / risks

| Item | Status |
|------|--------|
| Operator preference between mock `01` dark header vs spec `02` light header | **UNKNOWN** — recommend HITL pick before implementation |
| W5-B homepage charter status | **NOT EXECUTED** — scope gap confirmed |
| Browser cache (`max-age=604800`) masking future changes | **KNOWN RISK** from prior audits |
| Production deployment | **NOT IN SCOPE** |

---

## Authorization status

| Action | Status |
|--------|--------|
| WF V2 Gap Analysis | **COMPLETE** |
| Implementation | **NOT AUTHORIZED** (per audit mandate) |
| FTP / CSS / charter | **NOT AUTHORIZED** |
| Commit / push | **NOT AUTHORIZED** |

---

## Evidence index

| Source | Location |
|--------|----------|
| WF V2 concept mock | `projects/ocpilot/sites/site-001/design/wf-v2-concept/01-sibcar-v2-concept.png` |
| WF V2 header spec | `projects/ocpilot/sites/site-001/design/wf-v2-concept/02-sibcar-v2-specification.png` |
| Live HTML snapshots | `.recovery-temp/wf-v2-audit-home.html`, `wf-v2-audit-pdp.html`, `wf-v2-audit-catalog.html` |
| Live CSS | `.recovery-temp/wf-v2-audit-main.css` (173 031 bytes) |
| W5-A execution | [SITE-001-W5A-HEADER-SHELL-EXECUTION-v1.md](SITE-001-W5A-HEADER-SHELL-EXECUTION-v1.md) |
| W5-A-S execution | [SITE-001-W5A-STABILIZATION-EXECUTION-v1.md](SITE-001-W5A-STABILIZATION-EXECUTION-v1.md) |
| W5-C execution | [SITE-001-W5C-USED-PDP-EXECUTION-v1.md](SITE-001-W5C-USED-PDP-EXECUTION-v1.md) |
| Prior direction (superseded by WF V2 for audit) | [SITE-001-WEBSITE-FACTORY-CONCEPT-DECISION-v1.md](SITE-001-WEBSITE-FACTORY-CONCEPT-DECISION-v1.md) |

*SITE-001 WF V2 Gap Analysis v1 — audit documentation only; no implementation.*
