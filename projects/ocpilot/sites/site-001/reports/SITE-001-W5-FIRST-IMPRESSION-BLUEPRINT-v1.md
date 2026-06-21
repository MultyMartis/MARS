# SITE-001 — W5 First Impression Blueprint v1

**Type:** Design architecture blueprint — documentation only  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Checkpoint:** `site-001-phase1-stable-2026-06`  
**Design owner:** Website Factory  
**Direction:** **Concept B — «Современный Дилер 2026»** (approved target; implementation **NOT** authorized)

**Mode:** **DESIGN BLUEPRINT ONLY** — no FTP · no CSS · no Twig · no PHP · no JS · no DB · no execution

**Explicit exclusions:** No color proposals · no shadows · no gradients · no border radius · no token systems · no atmosphere tweaks. Problem = **first impression architecture**, not styling.

**Inputs:**

- [SITE-001-WEBSITE-FACTORY-CONCEPT-WORKSHOP-v1.md](SITE-001-WEBSITE-FACTORY-CONCEPT-WORKSHOP-v1.md)
- [SITE-001-WEBSITE-FACTORY-CONCEPT-DECISION-v1.md](SITE-001-WEBSITE-FACTORY-CONCEPT-DECISION-v1.md)
- [SITE-001-VISUAL-CHANGE-FAILURE-AUDIT-v1.md](SITE-001-VISUAL-CHANGE-FAILURE-AUDIT-v1.md)
- [SITE-001-W4-1-VISUAL-PROOF-PACK-v1.md](SITE-001-W4-1-VISUAL-PROOF-PACK-v1.md)
- [SITE-001-W4-USED-PDP-DESIGN-PLAN-v1.md](SITE-001-W4-USED-PDP-DESIGN-PLAN-v1.md)
- [SITE-001-W4-1-HEADER-HERO-DESIGN-PLAN-v1.md](SITE-001-W4-1-HEADER-HERO-DESIGN-PLAN-v1.md)
- QA evidence: `sites/site-001/qa/w4-1-header-hero-screenshots/`

---

## Blueprint mandate

Translate **Concept B** from workshop decision into an **implementation-ready architecture** for three first-impression zones:

1. Header  
2. Homepage first screen  
3. Used PDP first screen  

**Success criterion:** A visitor recognizes the site as a **modern dealership within 3 seconds** — without logo, without A/B comparison.

**Baseline perception score:** **3/10** (workshop + W4.1 proof pack)  
**Target perception score:** **7/10+** (Concept B mandate)

---

# SECTION 1 — CURRENT STATE ANALYSIS

Evidence: W4.1 Visual Proof Pack (1440×900, 2026-06-09) · Visual Change Failure Audit · W4 Used PDP design plan · Phase 1 acceptance.

---

## 1.1 HEADER

### A. Current structure

```
┌─────────────────────────────────────────────────────────────────┐
│ TIER 1 — Utility toolbar (.singe_bar__wrap)                     │
│ [LOGO+tagline] [address] ············· [hours] [phone] [WA] [☰] │
├─────────────────────────────────────────────────────────────────┤
│ TIER 2 — Primary nav (<nav>)                                    │
│ [logo repeat mobile] · [5 nav items left-aligned] · [callback][ph]│
├─────────────────────────────────────────────────────────────────┤
│ TIER 3 — Promo strip (.lcd_display.header) — separate band      │
│ «TRADE-IN 98% · 300 000 ₽ · …» marquee                          │
└─────────────────────────────────────────────────────────────────┘
```

**DOM reality (post-W4.1):** Three stacked horizontal bands remain. W4.1 added shell classes (`w4-1-header`, gradient nav, red discipline) but **did not recompose** tiers into one block. Promo is still a **third strip** below nav (graphite CAPS after W4.1, but same position). Desktop sticky behaviour deployed in W4.1 — **rejected** for Concept B.

**Functional elements present:** Logo · 5 menu items · phone pill · WhatsApp · callback CTA · hours · address · promo marquee.

### B. Current weaknesses

| ID | Weakness | Evidence |
|----|----------|----------|
| H-W1 | **Three-band OC-dealer silhouette** — instant template recognition | Workshop §Shared diagnosis; W4.1 header crop: anatomy unchanged |
| H-W2 | **Left-aligned nav** — classic OpenCart sidebar-dealer pattern, not centered dealership shell | W4.1 proof: menu order/position unchanged |
| H-W3 | **Competing contact surfaces** — phone in toolbar AND nav; callback AND WhatsApp both shout | W4.1 design plan §1 competing red zones (partially fixed, hierarchy not reordered) |
| H-W4 | **Promo as third horizontal layer** — adds vertical chrome before any content | W4.1 promo score 8/10 for *styling* change, but **structural third band** persists |
| H-W5 | **Logo role diluted** — appears in toolbar with tagline border; competes with nav items | Phase 1 branding map; header crop |
| H-W6 | **W4.1 polish insufficient** — header score **5/10** in proof pack; visitor notice **MAYBE** | [SITE-001-W4-1-VISUAL-PROOF-PACK-v1.md](SITE-001-W4-1-VISUAL-PROOF-PACK-v1.md) |

### C. Why it still feels like an old dealership template

The header communicates **«stacked legacy auto-theme»** because:

1. **Vertical rhythm** = utility bar + dark nav + promo = three horizontal slices — the canonical OpenCart `auto` theme dealer layout since Phase 0.  
2. **Navigation geometry** = logo left, links left-clustered — not a unified dealership shell with centered wayfinding.  
3. **Promo separation** = marketing message lives outside the nav frame as its own band — discount-dealer ticker grammar even after graphite restyle.  
4. **No single primary action** — callback, phone, WhatsApp, and nav items share one visual plane; visitor cannot read «what do I do first?» in 3 seconds.

W4.1 proved that **surface polish on this anatomy** does not change first-impression class (header 5/10, homepage 3/10).

---

## 1.2 HOMEPAGE FIRST SCREEN

### A. Current structure

```
┌─────────────────────────────────────────────────────────────────┐
│ HEADER (3 bands — see 1.1)                                        │
├─────────────────────────────────────────────────────────────────┤
│ HERO — Full-width image carousel (Swiper)                       │
│ [small promo headline text] [small subtext] [red CTA button]    │
│ (vehicle photo background, rotating slides)                     │
├─────────────────────────────────────────────────────────────────┤
│ BELOW HERO — «СИБКАР — авто с пробегом» + four_blocks grid       │
│ [icon block] [icon block] [icon block] [icon block]               │
├─────────────────────────────────────────────────────────────────┤
│ (fold edge) catalog teasers / sliders — not search-first        │
└─────────────────────────────────────────────────────────────────┘
```

**Search placement:** Catalog search exists on `/cars/` but **not** on homepage first screen as primary entry. Homepage first screen = **promotional carousel**, not inventory discovery.

**Post-W4.1:** Slider content, CTA placement, hero typography scale, four_blocks — **unchanged**. Homepage first screen score **3/10**; visitor notice **NO**.

### B. Current weaknesses

| ID | Weakness | Evidence |
|----|----------|----------|
| HP-W1 | **Carousel-first grammar** — visitor reads «discount banner rotation», not «digital showroom» | W4.1 proof §1: slider/texts/CTA unchanged |
| HP-W2 | **Micro typography in hero** — promo copy smaller than nav; no dominant value proposition | Workshop: «мелкий текст акции» |
| HP-W3 | **No search anchor on first screen** — primary user job (find a car) deferred to catalog navigation | W3ATMOSPHERE audit: `.search_form` MISS on homepage |
| HP-W4 | **four_blocks as disconnected trust grid** — four equal icons below hero, not integrated into hero journey | W4.1 proof: four_blocks unchanged |
| HP-W5 | **Red CTA on slide competes with header CTAs** — three layers of conversion noise in first 900px | Visual failure audit: expectation mismatch |
| HP-W6 | **W3 waves invisible here** — CSS atmosphere does not alter hero **composition** | Visual Change Failure Audit: composition frozen |

### C. Why it still feels like an old dealership template

Homepage first screen = **«full-width promo carousel + icon strip»** — the default regional OC-dealer homepage pattern:

1. Visitor eye hits **rotating offer text**, not a stable dealership proposition.  
2. No **inventory entry point** in the hero viewport — modern dealers lead with search/filter; this site leads with seasonal promo.  
3. Hero **reading path** is horizontal bands (header → slider → icons) — template stack, not showroom entry.  
4. W3COLOR / W3ATMOSPHERE / W3WF changed **finish** on elements that do not dominate first screen — failure audit confirmed weak delta.

---

## 1.3 USED PDP FIRST SCREEN

### A. Current structure (post-W4 + W4.1)

```
┌─────────────────────────────────────────────────────────────────┐
│ HEADER (3 bands)                                                  │
├─────────────────────────────────────────────────────────────────┤
│ PROMO strip (W4.1 graphite CAPS)                                  │
├─────────────────────────────────────────────────────────────────┤
│ w4-1-pdp-top — breadcrumbs + H1 (editorial band, light canvas)  │
├─────────────────────────────────────────────────────────────────┤
│ short_btns — status badges (loose row)                            │
├─────────────────────────────────────────────────────────────────┤
│ w4-used-hero — unified card (W4 structural win)                   │
│ ┌──────────────────┬──────────────────┐                           │
│ │ GALLERY 50%      │ PANEL 50%        │                           │
│ │ (photos)         │ price            │                           │
│ │                  │ credit line      │                           │
│ │                  │ discount toggles │                           │
│ │                  │ spec grid        │                           │
│ │                  │ 3 CTA buttons    │                           │
│ └──────────────────┴──────────────────┘                           │
├─────────────────────────────────────────────────────────────────┤
│ w4-used-trust-strip (VIN check — light band)                      │
└─────────────────────────────────────────────────────────────────┘
```

**W4 achievement:** Hero unified into `w4-used-hero` card — first structural improvement. **W4.1 achievement:** Promo strip restyle (8/10 visibility). **Remaining gap:** Top of screen still reads **catalog page with title block**, then 50/50 OC columns inside card.

**Used PDP first screen score:** **6/10** (W4.1 proof pack) — promo pulls up; hero anatomy still two-column commerce grid.

### B. Current weaknesses

| ID | Weakness | Evidence |
|----|----------|----------|
| PDP-W1 | **H1 above hero** — title block separated from vehicle imagery; «catalog heading» not «vehicle on stage» | W4.1 PDP hero crop: H1 unchanged, notice **NO** |
| PDP-W2 | **50/50 gallery/panel split** — OpenCart product template geometry preserved inside W4 card | W4 design plan §2 current anatomy |
| PDP-W3 | **Price competes with discount toggles and 3 CTAs** — commercial hierarchy flat inside right column | W4 design plan: four competing objects |
| PDP-W4 | **Gallery not edge-dominant** — photos padded inside card; vehicle not «exhibition» scale | W4 design plan: pad 10, no edge bleed |
| PDP-W5 | **Financing/credit buried in panel stack** — not a single offer moment | W4 `w4-used-hero__offer` groups but no floating offer architecture |
| PDP-W6 | **Header + promo + breadcrumbs** consume ~200px before vehicle — slow path to «the car» | W4.1 crops; three bands + pdp-top |

### C. Why it still feels like an old dealership template

Even with W4 card wrapper:

1. **Vertical stack** = chrome → title → badges → two-column product layout = OC product page, not magazine PDP.  
2. **H1 placement** outside gallery = visitor reads **category semantics** before **vehicle presence**.  
3. **Gallery share** = half width — template default, not showroom stage (70%+ vehicle dominance).  
4. **Offer panel** inline, not overlapping stage — no «single vehicle + floating deal» modern dealer pattern.  
5. Promo strip (visible win) cannot compensate for **hero composition class** alone.

---

# SECTION 2 — CONCEPT B BLUEPRINT

Architecture for **Concept B — Modern Dealer 2026**. Describes **zones, hierarchy, and reading paths** — not visual finish.

---

## 2.1 HEADER BLUEPRINT

### Current → Target

| Aspect | Current | Target (Concept B) |
|--------|---------|-------------------|
| Band count | 3 separate horizontal strips | **2 logical zones** in **1 dealership shell** (contact rail + primary band with inset promo) |
| Nav alignment | Left-clustered items | **Centered nav** in primary band |
| Promo position | Third strip below nav | **Inset row inside** primary band (bottom edge of shell) |
| Scroll behaviour | Sticky on desktop (W4.1) | **Static** — header scrolls away |
| Logo zone | Toolbar left with tagline | **Primary band left** — identity anchor, tagline demoted or removed from header |
| Contact cluster | Split across toolbar + nav | **Unified right cluster** in primary band |
| Primary CTA | Callback competes with phone/WA | **One primary CTA** (callback); phone/WA supportive |

### Visual hierarchy (roles)

| Role | Elements | Purpose |
|------|----------|---------|
| **PRIMARY** | Centered navigation (5 items) | Wayfinding — «this is a real dealership with clear departments» |
| **SECONDARY** | Callback CTA (pill) · Phone number (click-to-call) | Conversion — «talk to us now» |
| **SUPPORTIVE** | Logo (left anchor) · WhatsApp icon · Hours (muted, contact rail) · Promo inset (single rotating message) | Identity · alternate channel · context · offer awareness without third band |

### Zone map

```
TARGET HEADER — «Dealer shell»

┌─────────────────────────────────────────────────────────────────┐
│ CONTACT RAIL (ultra-compact, single line)                       │
│ ········································· [hours muted] [ph][WA] │
├─────────────────────────────────────────────────────────────────┤
│ PRIMARY BAND (immersive single block)                           │
│ [LOGO] ······ [NAV · NAV · NAV · NAV · NAV] ······ [CALLBACK][PH]│
│ ─────────────────────────────────────────────────────────────── │
│ INSET PROMO (inside band, not separate strip)                   │
│ «single rotating offer message»                                   │
└─────────────────────────────────────────────────────────────────┘
```

### CTA hierarchy

| Tier | Element | Behaviour |
|------|---------|-----------|
| 1 — Primary | **Обратный звонок** (callback) | Single conversion button in nav band right |
| 2 — Secondary | **Phone** (formatted number) | Click-to-call; visible text + icon |
| 3 — Supportive | **WhatsApp** | Icon/link; no equal weight to callback |
| 4 — Passive | Nav items | Browse intent, not conversion |

### Menu hierarchy

| Priority | Items | Rationale |
|----------|-------|-----------|
| Core | Каталог / Авто с пробегом | Inventory — primary visitor job |
| Core | Trade-in / Кредит | Dealer services — revenue paths |
| Trust | Об автосалоне | Credibility |
| Contact | Контакты | Fallback conversion |

Centered placement signals **balanced dealership** — not sidebar catalog template.

### Logo role

- **Anchor left** in primary band only (remove duplicate from contact rail on desktop).  
- Size: dominant enough for recognition, **subordinate to centered nav** in visual weight.  
- Tagline: **not** in header chrome — footer or about only (reduces toolbar noise).

### Phone role

- **Secondary CTA** — always visible in primary band right cluster.  
- Duplicate in contact rail **allowed** on desktop for thumb-zone reach; mobile collapses to burger context.

### WhatsApp role

- **Supportive channel** — icon + link in contact rail and/or nav cluster.  
- Never primary button weight.

### Callback role

- **Primary header CTA** — only element with «button» prominence in nav band.  
- One per viewport — no duplicate callback in hero on same screen.

### Answers

| Question | Answer |
|----------|--------|
| What is **primary**? | Centered navigation + Callback CTA |
| What is **secondary**? | Phone · Logo identity |
| What is **supportive**? | WhatsApp · Hours · Inset promo message |

---

## 2.2 HOMEPAGE FIRST SCREEN BLUEPRINT

### Current → Target

| Aspect | Current | Target (Concept B) |
|--------|---------|-------------------|
| Hero type | Full-width rotating promo carousel | **Showroom entry** — stable hero frame with dominant headline + vehicle visual |
| Headline | Small rotating promo copy | **Large stable headline** — «Авто с пробегом в [город]» (2 lines max) |
| Primary action | Red button on slide | **Floating search card** — «Показать N авто» |
| Search | Absent on first screen | **Overlapping hero bottom** — mark · model · price from |
| Trust | four_blocks grid below hero | **Integrated chips** flanking search card OR inline in search card footer |
| Below fold edge | four_blocks + catalog sliders | **Horizontal featured vehicles** (3-card peek scroll) |
| Reading path | Header → tiny promo text → icons | Header → headline → search card → featured peek |

### Hero composition

```
TARGET HOMEPAGE FIRST SCREEN — «Showroom entry»

┌─────────────────────────────────────────────────────────────────┐
│ HEADER (dealer shell — static)                                  │
├─────────────────────────────────────────────────────────────────┤
│ HERO STAGE (~85vh max viewport)                                 │
│                                                                 │
│  [LARGE HEADLINE          ]              [VEHICLE IMAGE         ]│
│  [subline muted           ]              [dominant right 60%  ]│
│  [optional ghost CTA      ]              [or full-bleed photo ]│
│                                                                 │
│         ┌─────────────────────────────────────────┐             │
│         │ FLOATING SEARCH CARD (overlaps hero)    │             │
│         │ [mark] [model] [price from] [SEARCH CTA]│             │
│         │ [trust chips: N cars · warranty · etc.] │             │
│         └─────────────────────────────────────────┘             │
├─────────────────────────────────────────────────────────────────┤
│ FEATURED VEHICLES — horizontal scroll peek (3 cards)            │
│ [card◄] [card] [card►]                                          │
└─────────────────────────────────────────────────────────────────┘
```

### Element roles

| Element | Role | Priority |
|---------|------|----------|
| Large headline | Value proposition — **what this site is** | PRIMARY |
| Floating search card | Inventory entry — **what visitor does first** | PRIMARY |
| Vehicle imagery | Emotional proof — **showroom, not banner** | SECONDARY |
| Search CTA button | Conversion to catalog | SECONDARY |
| Trust chips | Credibility without four_blocks grid | SUPPORTIVE |
| Featured scroll | Proof of inventory depth | SUPPORTIVE |
| Carousel rotation | **Demoted** — single hero frame or slow hero; promo text not hero headline | REMOVED from dominance |

### User eye path (explicit)

| Step | Zone | What visitor reads |
|------|------|-------------------|
| **1** | Primary nav band (centered) | «Organized dealership» — not template stack |
| **2** | Hero headline (large, left) | «Авто с пробегом в [город]» — stable proposition |
| **3** | Floating search card | «I can find a car right here» — primary job |
| **4** | Vehicle image (right) | «They have real cars» — showroom signal |
| **5** | Featured vehicles peek | «There's inventory to browse» — depth proof |

**3-second outcome:** Visitor answers **«modern car search site / dealership»** — not **«rotating promo banner»**.

---

## 2.3 USED PDP FIRST SCREEN BLUEPRINT

### Current → Target

| Aspect | Current | Target (Concept B) |
|--------|---------|-------------------|
| H1 position | Above hero in `w4-1-pdp-top` band | **On gallery overlay** — vehicle name + year as stage title |
| Top chrome | Header + promo + breadcrumbs + H1 band | **Minimal breadcrumb strip** only above stage |
| Hero layout | 50/50 card columns | **Stage band** — gallery 70% edge-dominant + floating offer card |
| Offer | Stacked in right column | **Floating card** overlapping gallery right edge |
| Trust | `w4-used-trust-strip` below hero | **Light strip below stage** — unchanged position, simplified chrome above |
| W4 asset | `w4-used-hero` wrappers | **Preserved inside stage** — re-grouped spatially, not deleted |
| CTA count in hero | 3 equal buttons | **One primary** «Забронировать просмотр» + secondary collapsed |

### Zone architecture

```
TARGET USED PDP FIRST SCREEN — «Magazine PDP»

┌─────────────────────────────────────────────────────────────────┐
│ HEADER (dealer shell)                                           │
├─────────────────────────────────────────────────────────────────┤
│ BREADCRUMB STRIP (minimal, single line, no H1)                    │
├─────────────────────────────────────────────────────────────────┤
│ STAGE BAND (full-width dark canvas)                               │
│ ┌────────────────────────────────────────┐ ┌──────────────────┐ │
│ │ GALLERY 70% — edge-bleed photos        │ │ FLOATING OFFER   │ │
│ │ [H1 vehicle name + year ON gallery]    │ │ CARD (overlap)   │ │
│ │ [status badges on gallery corner]      │ │ PRICE (large)    │ │
│ │                                        │ │ credit line      │ │
│ │                                        │ │ 3 spec chips     │ │
│ │                                        │ │ [PRIMARY CTA]    │ │
│ └────────────────────────────────────────┘ └──────────────────┘ │
├─────────────────────────────────────────────────────────────────┤
│ TRUST STRIP (light) — «Проверено СИБКАР» + icons                │
└─────────────────────────────────────────────────────────────────┘
```

### Element roles

| Element | Role | Priority |
|---------|------|----------|
| Gallery (70%, edge-bleed) | **Vehicle as hero** — exhibition | PRIMARY |
| H1 on gallery | Vehicle identity — **not catalog title** | PRIMARY |
| Floating offer card | Price + deal moment | PRIMARY |
| Primary CTA | «Забронировать просмотр» | SECONDARY |
| Credit line | Financing hook | SECONDARY |
| Spec chips (3) | Key facts — year/km/owners | SUPPORTIVE |
| Breadcrumbs | Orientation | SUPPORTIVE |
| Discount toggles | **Demoted** below fold or inside offer card collapsed | SUPPORTIVE |
| Trust strip | Post-hero credibility | SUPPORTIVE |

### User eye path (explicit)

| Step | Zone | What visitor reads |
|------|------|-------------------|
| **1** | Stage band (full-width dark canvas) | «This is a vehicle showcase» — not catalog page |
| **2** | Gallery + H1 overlay | «This specific car» — name, year, photos |
| **3** | Floating offer card — price | «What it costs» — commercial clarity |
| **4** | Primary CTA | «I can book a viewing» — single action |
| **5** | Trust strip below | «Dealer verified this car» — confidence |

**3-second outcome:** Visitor answers **«modern single-vehicle showroom page»** — not **«OpenCart product with two columns»**.

---

# SECTION 3 — BLOCK SCHEMAS (TEXT WIREFRAMES)

## 3.1 HEADER

```
┌──────────────────────────────────────────────────────────────────────────┐
│ CONTACT RAIL                                                             │
│                              [HOURS quiet]              [PHONE] [WA]     │
├──────────────────────────────────────────────────────────────────────────┤
│ PRIMARY BAND                                                             │
│                                                                          │
│  [LOGO]     [MENU1] [MENU2] [MENU3] [MENU4] [MENU5]     [CALLBACK][PH] │
│                                                                          │
│  ┌────────────────────────────────────────────────────────────────────┐  │
│  │ INSET PROMO: «single offer line»                                  │  │
│  └────────────────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────────────┘

MOBILE (conceptual):
┌────────────────────────┐
│ [LOGO]    [PH][WA][☰]  │
├────────────────────────┤
│ [CALLBACK full width]  │
├────────────────────────┤
│ INSET PROMO (1 line)   │
└────────────────────────┘
(burger → offcanvas nav; contact rail hours hidden)
```

## 3.2 HOMEPAGE FIRST SCREEN

```
┌──────────────────────────────────────────────────────────────────────────┐
│ HEADER (dealer shell)                                                    │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  HERO STAGE                                                              │
│                                                                          │
│  ┌─────────────────────┐              ┌─────────────────────────────┐    │
│  │ HEADLINE LINE 1     │              │                             │    │
│  │ HEADLINE LINE 2     │              │     VEHICLE PHOTO           │    │
│  │ subline             │              │     (dominant)              │    │
│  └─────────────────────┘              └─────────────────────────────┘    │
│                                                                          │
│           ┌─────────────────────────────────────────────────┐            │
│           │ SEARCH CARD                                     │            │
│           │ [MARK ▼] [MODEL ▼] [PRICE FROM ▼] [SHOW N CARS] │            │
│           │ [chip: stock] [chip: warranty] [chip: trade-in] │            │
│           └─────────────────────────────────────────────────┘            │
│                                                                          │
├──────────────────────────────────────────────────────────────────────────┤
│ FEATURED ROW                                                             │
│  ◄  [CAR CARD]  [CAR CARD]  [CAR CARD]  ►                               │
└──────────────────────────────────────────────────────────────────────────┘
```

## 3.3 USED PDP FIRST SCREEN

```
┌──────────────────────────────────────────────────────────────────────────┐
│ HEADER (dealer shell)                                                    │
├──────────────────────────────────────────────────────────────────────────┤
│ crumbs: Home > Cars > Brand > Model                                      │
├──────────────────────────────────────────────────────────────────────────┤
│ STAGE                                                                    │
│ ┌────────────────────────────────────────────────┐  ┌─────────────────┐  │
│ │ [badge] [badge]                                │  │ OFFER CARD      │  │
│ │                                                │  │                 │  │
│ │   GALLERY                                      │  │ PRICE           │  │
│ │   [main photo edge-bleed]                      │  │ credit/mo       │  │
│ │                                                │  │ [year|km|owner] │  │
│ │   H1: Vehicle Name Year                        │  │                 │  │
│ │                                                │  │ [BOOK VIEWING]  │  │
│ │   [thumb][thumb][thumb][thumb]                 │  │                 │  │
│ └────────────────────────────────────────────────┘  └─────────────────┘  │
│                                          (card overlaps gallery edge ──►)│
├──────────────────────────────────────────────────────────────────────────┤
│ TRUST: [icon check] [icon shield] [icon doc] «Проверено СИБКАР»         │
└──────────────────────────────────────────────────────────────────────────┘
```

---

# SECTION 4 — VISUAL IMPACT MAP

Per-change impact on **3-second modern dealership perception** (not CSS polish).

| # | Proposed architectural change | Zone | Impact | Why |
|---|------------------------------|------|--------|-----|
| 1 | Collapse 3 header bands → 1 shell + inset promo | Header | **VERY HIGH** | Eliminates #1 OC-template silhouette signal (three horizontal strips) |
| 2 | Center primary navigation | Header | **HIGH** | Breaks left-clustered OC-dealer nav pattern; instant layout novelty |
| 3 | Demote promo from third strip to inset row | Header | **HIGH** | Removes ~24px chrome layer; reduces «discount ticker site» read |
| 4 | Static header (remove sticky) | Header | **MEDIUM** | Aligns with Concept B; reduces «sticky widget bar» feel; lower than band collapse |
| 5 | Single primary CTA hierarchy (callback > phone > WA) | Header | **MEDIUM** | Clarifies intent; visible only after band collapse reduces noise |
| 6 | Replace carousel-first hero with stable headline + dominant vehicle | Homepage | **VERY HIGH** | Changes homepage **grammar** from promo rotation to showroom entry |
| 7 | Floating search card overlapping hero | Homepage | **VERY HIGH** | Modern dealer signal #1 — «search inventory here»; absent today |
| 8 | Large headline typography scale (architectural size, not style) | Homepage | **HIGH** | First readable element becomes proposition, not promo fine print |
| 9 | Featured vehicles horizontal peek (replaces four_blocks dominance) | Homepage | **MEDIUM** | Proves inventory; below search — supportive not primary |
| 10 | Demote/remove carousel as hero headline source | Homepage | **HIGH** | Stops discount-banner first impression |
| 11 | Move H1 from above-hero band onto gallery overlay | Used PDP | **VERY HIGH** | Shifts page class from «catalog title» to «vehicle on stage» |
| 12 | Full-width stage band with gallery 70% edge-dominant | Used PDP | **VERY HIGH** | Breaks 50/50 OC product column geometry |
| 13 | Floating offer card overlapping gallery | Used PDP | **HIGH** | Modern commerce pattern — single deal moment |
| 14 | Reduce hero CTA to one primary + demoted secondaries | Used PDP | **MEDIUM** | Commercial clarity; depends on stage layout first |
| 15 | Minimal breadcrumb strip (no H1 band) | Used PDP | **MEDIUM** | Reduces chrome stack before vehicle |
| 16 | Re-skin W4 `w4-used-*` inside stage (preserve wrappers) | Used PDP | **HIGH** | Leverages accepted W4 work; spatial regroup not rewrite |
| 17 | Trust strip below stage only (simplify above-fold chrome) | Used PDP | **LOW** | W4 already delivered; position unchanged |

**Cumulative thesis:** Items **1, 6, 7, 11, 12** are the **minimum architectural set** for 3-second class change. Items with **LOW** impact alone (W4.1-style polish, atmosphere, tokens) **cannot** reach 7/10 — confirmed by Visual Change Failure Audit and W4.1 proof pack.

---

# SECTION 5 — IMPLEMENTATION PHASES

**Planning only.** No code. No CSS. No execution. Sequenced for post-blueprint charter authorization.

| Phase | Name | Scope | Depends on | Gate |
|-------|------|-------|------------|------|
| **W5-A** | **Header Shell Recomposition** | `header.twig` DOM regroup: contact rail + primary band + inset promo; remove third strip; centered nav; static scroll; CTA hierarchy; **revert W4.1 sticky** | Blueprint approval | 3-sec test: header silhouette without logo |
| **W5-B** | **Homepage Showroom Entry** | `home.twig` hero restructure: stable headline zone, floating search card mount, featured horizontal row; demote carousel dominance | W5-A (shared header shell live) | 3-sec test: homepage without logo |
| **W5-C** | **Used PDP Magazine Stage** | `product.twig` stage band: H1 on gallery, floating offer card, 70% gallery; re-group `w4-used-*` inside stage; minimal breadcrumb strip | W5-A | 3-sec test: used PDP without logo |
| **W5-D** | **First Impression Integration & Verification** | Cross-page consistency check; mobile shell variants; W4.1/W4 marker preservation audit; hard-refresh QA protocol; operator 3-second HITL scoring; rollback decision | W5-A + W5-B + W5-C | All three zones ≥7/10 operator score |

### Phase rationale

1. **W5-A first** — header appears on all three zones; shell change is highest cross-page leverage.  
2. **W5-B and W5-C** may proceed in parallel after W5-A — independent templates, shared header.  
3. **W5-D last** — integration verification; no new architecture, only proof that 3-second test passes sitewide.

### Explicitly NOT in W5 phases

- W3COLOR / W3ATMOSPHERE / W3WF token waves  
- Catalog density (W3UX-C1) — preserve below first screen  
- Footer, forms, credit calculator logic, SEO, PHP/JS/DB  
- Production deployment

---

# SECTION 6 — 3 SECOND TEST

**Method:** Logo hidden. User sees only structure, zone geometry, typography **scale hierarchy**, and content placement. No A/B with previous version.

### Current site (structure only)

| Zone | What user thinks (3 sec) |
|------|--------------------------|
| Header | «Три полоски сверху — типичный шаблон автосалона» |
| Homepage | «Крутится баннер с акцией и красной кнопкой» |
| Used PDP | «Страница товара каталога: заголовок, потом картинка слева и цена справа» |
| **Overall** | **Old OpenCart regional dealer template** — score **3/10** |

### Blueprint Concept B (structure only)

| Zone | What user thinks (3 sec) |
|------|--------------------------|
| Header | «Один блок навигации по центру — как у нормального современного дилера» |
| Homepage | «Сайт чтобы найти машину — большой заголовок и поиск прямо на экране» |
| Used PDP | «Витрина одной машины — фото большое, цена отдельной карточкой» |
| **Overall** | **Modern dealership / digital showroom** — target **7/10+** |

### Delta summary

| Signal | Current | Concept B |
|--------|---------|-----------|
| Header silhouette | 3-band stack | 1 shell + inset |
| Homepage job | Promo carousel | Search-first entry |
| PDP geometry | 50/50 catalog | Stage + floating offer |
| 3-sec class | OC template | Modern dealer |

---

## Blueprint dependencies & preservation

| Asset | Treatment in W5 |
|-------|-----------------|
| Phase 1 copy, URLs, phone, menu items | **Frozen** — reposition only |
| W3UX-C1 catalog density | **Preserve** — below first screen on `/cars/` |
| W4 `w4-used-*` twig wrappers | **Preserve** — spatial re-group inside W5-C stage |
| W4.1 promo graphite styling | **Superseded structurally** — inset promo replaces third strip; styling deferred to implementation charter |
| W4.1 sticky header | **Revert** — Concept B static header |

---

## Evidence index

| Source | Path |
|--------|------|
| W4.1 screenshots | `projects/ocpilot/sites/site-001/qa/w4-1-header-hero-screenshots/` |
| Concept workshop | [SITE-001-WEBSITE-FACTORY-CONCEPT-WORKSHOP-v1.md](SITE-001-WEBSITE-FACTORY-CONCEPT-WORKSHOP-v1.md) |
| Concept decision | [SITE-001-WEBSITE-FACTORY-CONCEPT-DECISION-v1.md](SITE-001-WEBSITE-FACTORY-CONCEPT-DECISION-v1.md) |
| Failure audit | [SITE-001-VISUAL-CHANGE-FAILURE-AUDIT-v1.md](SITE-001-VISUAL-CHANGE-FAILURE-AUDIT-v1.md) |
| W4 PDP plan | [SITE-001-W4-USED-PDP-DESIGN-PLAN-v1.md](SITE-001-W4-USED-PDP-DESIGN-PLAN-v1.md) |

---

## Next artifact

[SITE-001-W5-FIRST-IMPRESSION-DECISION-v1.md](SITE-001-W5-FIRST-IMPRESSION-DECISION-v1.md) — operator gate + final YES/NO verdict.

*SITE-001 W5 First Impression Blueprint v1 — design architecture only; no implementation.*
