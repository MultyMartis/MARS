# REPORT — M9.8.9-03 CERTIFICATES DEALERS MERGE FORENSIC AND DESIGN

**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** TEST — https://zpm.new-site.space/  
**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01`  
**Task:** M9.8.9-03 — forensic audit + design variants (no implementation)  
**Date:** 2026-06-19  
**Mode:** Research and design only — **no** code changes · **no** deploy · **no** FTP · **no** commit

**PRE-TASK RULE:** Knowledge Map + Stable Checkpoint + site-passport + README — read and applied.

---

## 1. Current Architecture

### 1.1 Template locations (live OpenCart paths)

| Block | Twig template (canonical live path) | Root markup |
|-------|-------------------------------------|-------------|
| Certificates | `catalog/view/theme/default/template/sections/certificates.twig` | `<section class="certificates">` |
| Dealers + form | `catalog/view/theme/default/template/sections/blockdealersform.twig` | `<section class="zpm-dealers" data-dealers>` |

**Repo evidence:** Controllers consistently load these views; live HTML snapshots match. **Source `.twig` files are not present in the MARS git tree** — they live on TEST hosting / bulk storage (`C:\AI MARS STORAGE\ocpilot\project-sites\site-002\`). Forensic markup taken from:

- `projects/ocpilot/sites/site-002/category-audit-v1-work/category-live.html` (2026-06 capture)
- `projects/ocpilot/sites/site-002/reports/m9.8.9-06d-work/plp-stoly-after.html`
- Live fetch https://zpm.new-site.space/stoly-serii-premium/stoly/ (2026-06-19)

### 1.2 Controller wiring

Views are rendered in PHP controllers via `$this->load->view('sections/…')` and passed as string variables to parent Twig.

| Controller | Variables loaded |
|------------|------------------|
| `catalog/controller/product/category.php` | `certificates`, `blockdealersform`, also `blockadvantagestop`, `blockadvantagesbottom`, `aboutteaser` (**advantages loaded but not output on category PLP**) |
| `catalog/controller/common/home.php` | `certificates`, `blockadvantagestop`, `blockdealersform`, `blockadvantagesbottom` |
| `catalog/controller/product/katalog.php` | same full stack as home (below grid) |

**Evidence:** `m9.8.5-products-per-page-work/category.php` L587–591; `m7.1-launch-mode-work/patch/catalog/controller/common/home.php`; `m7.1-launch-mode-work/catalog__controller__product__katalog.php`.

### 1.3 Parent template insertion

| Parent Twig | Order of commercial blocks |
|-------------|---------------------------|
| `product/category.twig` | `{{ seotext }}` → `{{ certificates }}` → `{{ blockdealersform }}` |
| `common/home.twig` | `{{ certificates }}` → `{{ blockadvantagestop }}` → `{{ blockdealersform }}` → `{{ blockadvantagesbottom }}` |
| `product/katalog.twig` | certificates → blockadvantagestop → blockdealersform → blockadvantagesbottom |

**Includes:** No `{% include %}` between sections — each block is a **pre-rendered HTML string** from the controller.

### 1.4 Certificates block — structure

```
section.certificates
└── .container
    ├── .zpm-slider__head
    │   ├── .section-title__like-h2  «Наши / сертификаты»
    │   └── .certificates__nav--desktop → prev/next (.certificates__btn--*)
    └── .swiper.js-certificates-slider
        └── .swiper-slide × N
            └── a.certificates__card[href=full JPG][data-fancybox=certificates]
                └── img.certificates__img[src=thumb PNG]
```

**Assets (live):** `/assets/img/certificates/certificat_00.jpg`, `certificat_01.jpg`, thumbs `thumb_00.png`, `thumb_01.png`.

**Data quality (forensic):** Snapshot shows **4 slides** but only **2 unique certificate files** — slides 2–4 duplicate `certificat_01.jpg` / `thumb_01.png`. **SAFE UNKNOWN:** whether live Twig was updated since capture; operator should confirm real certificate inventory.

### 1.5 Dealers block — structure

```
section.zpm-dealers[data-dealers]
└── .container
    └── .zpm-universal__grid
        ├── .zpm-universal__grid-First
        │   ├── H2 «Дилерам / и оптовикам»
        │   ├── .zpm-dealers__text (long paragraph)
        │   └── a.btn «Подробнее» → /dealers
        └── .zpm-universal__grid-Second
            └── form.zpm-form
                ├── hidden dialog=7
                ├── name, phone, email, message
                ├── agree checkbox + legal links
                └── submit «Отправить»
```

### 1.6 Shared CSS (`assets/css/style.css`)

| Area | Key selectors | Notes |
|------|---------------|-------|
| Certificates | `.certificates__head`, `__nav`, `__btn`, `__slider`, `__card`, `__img` | No root `.certificates { padding }` — height driven by title + swiper + image aspect |
| Slider chrome | `.zpm-slider__head`, `.zpm-slider__btn` | Shared with other sliders (hero, rel-articles) |
| Dealers | `.zpm-dealers { padding: 120px 0 }` | **Major vertical cost**; 80px @ ≤1024 |
| Grid | `.zpm-universal__grid` (2 col), `.zpm-dealers .zpm-universal__grid` | Dealers: 2 col desktop → 1 col @ ≤1024 |
| Form | `.zpm-form__*` | Shared form system site-wide |
| Typography | `.zpm-dealers__text { max-width: 540px }` | Long prose column |

**Evidence:** `m9.8.5-products-per-page-work/style.css` L1514–1516, 5519–5542, 6764–6798, 10595–10710.

### 1.7 JavaScript (`assets/js/main.js`)

| Feature | Implementation | Scope |
|---------|----------------|-------|
| **Certificates slider** | IIFE `initCertificatesSlider()` — Swiper on `.js-certificates-slider` | `slidesPerView`: 1.15 → 2 @660 → **4 @1025**; nav buttons scoped to `.certificates` root |
| **Lightbox** | `data-fancybox="certificates"` on `<a>` | Fancybox (global init elsewhere in `main.js`) |
| **Dealer form** | IIFE «ISOLATED HANDLER FOR DEALER FORM» | `formSelector: '.zpm-dealers[data-dealers] .zpm-form'`; **`document.querySelector` — only first form on page** |
| **Endpoint** | `POST /index.php?route=checkout/anketa` | `dialog=7`; optional reCAPTCHA + CSRF meta |
| **Validation** | Inputmask phone; custom email rules; agree checkbox gate | Bound per form instance when found |

**Form dependency chain:** Block **depends on** this JS handler + backend `checkout/anketa` route + `dialog=7` semantics. No separate PHP controller in repo for the section itself.

### 1.8 PDP / product pages

**No** `certificates` or `blockdealersform` on PDP templates/controllers in repo evidence. Problem is concentrated on **catalog surfaces** (category PLP, hub, `/katalog`, homepage).

---

## 2. Usage Map

| Surface | Certificates | Dealers form | Advantages top/bottom | Notes |
|---------|:------------:|:------------:|:---------------------:|-------|
| **Category PLP** (all levels, incl. hub `category--hub`) | ✅ | ✅ | ❌ (loaded in PHP, **not rendered**) | Primary operator pain point |
| **Homepage** `/` | ✅ | ✅ | ✅ (between certs and dealers) | Different vertical rhythm |
| **`/katalog`** | ✅ | ✅ | ✅ | Full marketing stack below type grid |
| **PDP** | ❌ | ❌ | ❌ | Aligns with BZPM redesign «suppress on deep pages» |
| **Other pages** | **SAFE UNKNOWN** | **SAFE UNKNOWN** | — | Not exhaustively probed; dedicated `/dealers` page exists (linked from block) |

**Live confirmation (2026-06-19):** Category «Столы» shows both blocks sequentially after pagination — «Наши сертификаты» then «Дилерам и оптовикам» + form.

---

## 3. Current Problems

### 3.1 Layout / UX

| # | Problem | Evidence |
|---|---------|----------|
| 1 | **~2 viewport heights** for trust + B2B on catalog pages | `.zpm-dealers` padding 120px×2 + full-width cert slider (4-up desktop) + large dual H2s |
| 2 | **Weak visual connection** | Separate `<section>` roots, no shared container/grid; cert block reads as «gallery», dealers as «landing» |
| 3 | **Certificates visually dominate** | Large `section-title__like-h2`, 4 visible slides, 56px nav buttons; form is below fold on many viewports |
| 4 | **Information spread** | Trust (certs) disconnected from procurement story (dealer copy + CTA) |
| 5 | **Heavy on deep PLP** | Same wallpaper on leaf categories with 15+ SKU grid — aligns with W2-F-07 «repeated blocks» critique in BZPM redesign docs |
| 6 | **Gap after grid** | Category audit: «large vertical gap between grid and certificates/dealers» |

### 3.2 Content / data

| # | Problem | Evidence |
|---|---------|----------|
| 7 | **Duplicate certificate slides** | 4 slides, 2 unique files in HTML capture |
| 8 | **Dealer copy too long** for secondary placement | Single dense paragraph before form |
| 9 | **No commercial micro-signals** | No response time, volume, warranty, «производство РФ» near form |

### 3.3 Technical

| # | Problem | Evidence |
|---|---------|----------|
| 10 | **Wasted controller work** on category | `blockadvantagestop/bottom` loaded but unused in `category.twig` |
| 11 | **Dealer JS single-instance** | `querySelector` — risk if multiple `.zpm-dealers` on one page after merge/home variants |
| 12 | **Live Twig not in repo** | Implementation must live-capture before deploy (SITE-002 working rules) |

---

## 4. Commercial Analysis

### 4.1 What the dealer needs at this scroll position

On category pages the user has **already evaluated products**. The merged block should answer:

| Question | Current state | Target signal (short) |
|----------|---------------|------------------------|
| Why trust this manufacturer? | Certs slider (strong but oversized) | 2–3 proofs + «производство в РФ» |
| Why partner vs one-off buy? | Buried in long paragraph | 3–5 bullets: прайс, отгрузки, стабильность |
| What do I do next? | Form exists but below cert screen | Form visible in same viewport as trust |
| How fast will you respond? | Not stated | «Ответ в течение 1 рабочего дня» (**operator to confirm**) |
| Scale / logistics | Mentioned vaguely | «Поставки по РФ», «склад / производство» (**confirm facts**) |

### 4.2 Certificates — forensic UX verdict

| Question | Recommendation |
|----------|----------------|
| Reduce certificate size? | **Yes** — treat as **trust chips**, not hero gallery |
| How many to show? | **2–3 visible** on desktop; rest via «Все сертификаты» or lightbox group |
| Slider needed? | **Optional** — if >3 docs; else static row is simpler and shorter |
| Lightbox needed? | **Yes** — keep `data-fancybox` for readable PDF/JPG proof (tender use case) |
| CTA near certs? | **Light link** «Смотреть все» / icon zoom — **not** competing with form submit |

### 4.3 Copy pillars for center column (no long prose)

Suggested **5 micro-lines** (implementation phase — operator copy edit):

1. **ЗПМ** — производитель нейтрального оборудования для общепита  
2. **Производство** — Россия (**verify claim**)  
3. **Качество** — сертифицированная продукция  
4. **Гарантия** — от производителя (**term — confirm**)  
5. **Поставка** — по всей РФ  

Optional trust row above form: **«Прайс и КП после заявки»** · **«Ответ: N часов»**.

### 4.4 Alignment with BZPM redesign strategy

`BZPM-REDESIGN-ARCHITECTURE-v1.md` (documented/planned, not implemented) recommends:

- Tier-1 trust **once** at catalog entry — compact summary, not full slider on every deep page  
- Full dealer form **suppressed** on deep PLP in favour of link to `/dealers`

**Tension:** Operator request (M9.8.9-03) is **merge + keep form** on category pages. **Mitigation:** compact merged section now; optional **phase 2** contextual suppression on leaf PLP only.

---

## 5. Variant A — «Classic 3-column» (operator brief)

### Structure (desktop ≥1025)

```
section.zpm-commercial-trust[data-commercial-trust]
└── .container
    └── .zpm-commercial-trust__grid (3 cols: 28% | 32% | 40%)
        ├── COL-L: certs
        │   ├── mini H3 «Сертификаты»
        │   ├── 2–3 thumbs in row (fixed height ~120–140px)
        │   └── link «Все сертификаты» → lightbox group
        ├── COL-C: value props
        │   ├── H3 «Сотрудничество с ЗПМ»
        │   └── ul.zpm-commercial-trust__bullets (5 lines + icons)
        └── COL-R: form
            ├── H3 «Заявка дилерам»
            ├── 2 trust chips (срок ответа · поставки РФ)
            └── existing .zpm-form (compact: 4 fields + submit)
```

### Mobile (≤1024)

1. Bullets (collapsed to 3 + «ещё»)  
2. Certificate row (horizontal scroll, 2 visible)  
3. Form (full width)

### Pros

- Direct match to operator layout brief  
- Clear scanning: trust → why → action  
- Reuses existing form markup/endpoints

### Cons

- Tight at 1024–1280 — form may still wrap tall  
- Swiper in narrow left col fiddly  
- Homepage has advantages **between** old blocks — needs separate integration rule

### Implementation risk

**Medium** — new grid CSS + Twig composition; Swiper breakpoints need retuning.

### Mobile behaviour

Single column stack; cert row swipe or 2-up static; form unchanged functionally.

---

## 6. Variant B — «Trust strip + split» (compact)

### Structure (desktop)

```
section.zpm-commercial-trust
└── .container
    ├── ROW-1: .zpm-commercial-trust__strip (full width, ~160px)
    │   ├── 3 cert thumbs + «Сделано в РФ» badge
    │   └── text link «Все документы»
    └── ROW-2: .zpm-commercial-trust__split (55% / 45%)
        ├── copy: H2 + 4 icon bullets (no long paragraph)
        └── form card (.zpm-commercial-trust__form-card with subtle border/bg)
```

### Mobile

- Strip becomes horizontal scroll  
- Form immediately after bullets (form before strip if conversion priority — **A/B decision**)

### Pros

- **Best chance to fit one desktop viewport** (~900–1000px total height with compact padding 48–64px)  
- Reduces cert visual dominance without losing lightbox  
- Form in «card» gains focus vs gallery

### Cons

- Less literal «left / center / right» — operator may need visual mockup approval  
- Strip + split = two layout modes to maintain

### Implementation risk

**Low–medium** — mostly CSS; can drop Swiper if ≤3 certs static.

### Mobile behaviour

Strip + bullets + form; estimated **1.2–1.5 screens** (acceptable).

---

## 7. Variant C — «Contextual tier» (catalog-aware)

### Structure

**Hub / parent category / homepage:** full Variant B.

**Leaf category PLP (depth ≥ N or product count > 0):** collapsed mode:

```
section.zpm-commercial-trust.is-compact
└── single row: [cert icon stack] [3 bullets inline] [btn «Стать дилером»] [link form ▾]
    └── expandable panel OR modal with full form (click)
```

Certificates: **no slider** — icon + count «4 сертификата».

### Pros

- Aligns with BZPM W2-F-07 «no wallpaper on deep pages»  
- Strongest catalog UX on product-heavy pages  
- Reduces scroll fatigue where operator complaint is loudest

### Cons

- **Higher logic scope** — PHP/Twig context flags (`category_display_mode`, depth, hub vs leaf)  
- Hidden form may reduce conversion if users don’t expand — needs analytics  
- Operator asked for visible form — **conflict** unless compact mode still shows mini-form

### Implementation risk

**High** — conditional rendering + JS for expand/modal + QA matrix across category types.

### Mobile behaviour

Compact bar fixed height; form in drawer/modal — best for scroll, worst for immediate conversion.

---

## 8. Recommended Variant

**Primary: Variant B (Trust strip + split)** with **certificate count = 2–3 visible**, lightbox retained, slider **removed or optional only if >3**.

**Rationale:**

| Criterion | B wins because |
|---------|----------------|
| Operator goals (compact, one screen) | Lowest vertical padding budget |
| Cert vs form balance | Strip demotes gallery; form in dedicated card |
| Implementation risk | No 3-column squeeze; reuses `zpm-form` |
| Commercial strength | Bullets + 2 trust chips directly above submit |
| Live evidence | Current 4-up slider + 120px dealers padding is the main height driver |

**Secondary path:** If operator insists on literal 3 columns → **Variant A** with **no Swiper** (static 2 thumbs) and reduced section padding `48px 0`.

**Defer:** Variant C as **M9.8.9-03b** or roadmap item unless operator explicitly wants leaf-page suppression.

### Homepage / katalog scope note

Merge target for **category PLP** is clear. For **homepage** and **`/katalog`**, advantages blocks sit between certificates and dealers today — implementation should either:

1. Replace only the **pair** `certificates + blockdealersform` and leave advantages unchanged, or  
2. Define a **second combined template** for home/katalog including advantages — **out of scope unless chartered**.

**Recommendation:** Scope M9.8.9-03 implementation to **category.twig** first; home/katalog follow-up pass.

---

## 9. Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| Live Twig differs from repo snapshots | High | Mandatory FTP capture + SHA256 before edit |
| Dealer form `querySelector` single bind | Medium | Refactor to `querySelectorAll` or scope init to `[data-commercial-trust]` |
| Duplicate cert assets | Low | Operator supplies final cert list before implementation |
| Fancybox + compact thumbs | Low | Test zoom on mobile; min touch target 44px |
| ID collision (`dealerName` etc.) | Medium | Only one form per page, or suffix IDs in merged template |
| Operator manual CSS overrides | Medium | Diff live `style.css` after deploy |
| Conflict with BZPM redesign suppression policy | Low (doc) | Document as conscious operator override |
| Twig cache | Low | Clear cache post-deploy (standard SITE-002 rule) |
| reCAPTCHA / anketa backend | Low | Do not change `dialog=7` or endpoint without backend audit |

---

## 10. Implementation Estimate

**Phase:** Implementation **not authorized** by this task — estimate for planning only.

| Work package | Effort | Files (expected) |
|--------------|--------|------------------|
| Live capture (twig ×2, category.twig, style.css, main.js) | 0.5 h | — |
| New `sections/blockcommercialtrust.twig` (or similar) composing cert partial + copy + form partial | 2–3 h | 1 new twig; optional 2 partials |
| Controller: category.php swap to single view load | 0.5 h | 1 php |
| category.twig: replace two variables with one | 0.25 h | 1 twig |
| CSS: new block + responsive | 2–3 h | style.css |
| JS: cert init scope; optional remove slider; form init all instances | 1 h | main.js |
| QA: desktop 1440/1280/1024, mobile 390, hub + leaf PLP, form submit | 1–2 h | — |
| Deploy + cache + rollback doc | 0.5 h | backup .bak |

**Total:** **~8–11 hours** (1–1.5 agent deploy passes), assuming no homepage/katalog in same pass.

**Out of scope add-ons:** homepage/katalog (+3–4 h); Variant C contextual logic (+4–6 h); new copywriting/photography; `/dealers` page redesign.

---

## Evidence index

| Artifact | Path |
|----------|------|
| Category live HTML | `category-audit-v1-work/category-live.html` L4121–4293 |
| Category twig hook | `m9.8.5-products-per-page-work/category.twig` L145–147 |
| Category controller | `m9.8.5-products-per-page-work/category.php` L587–591 |
| Home twig order | `m7.1-launch-mode-work/catalog__view__theme__default__template__common__home.twig` |
| Certificates JS | `m9.8.5-products-per-page-work/main.js` L135–169 |
| Dealers form JS | `m9.8.5-products-per-page-work/main.js` L2678–2795 |
| Dealers CSS padding | `m9.8.5-products-per-page-work/style.css` L5519–5521 |
| M9.8.9 pack charter | `reports/SITE-002-M9.8.9-MINOR-FIXES-PACK-01-REGISTRATION.md` |
| BZPM redesign policy | `projects/website-factory/execution-cases/bzpm-catalog-redesign/BZPM-REDESIGN-ARCHITECTURE-v1.md` |
| Root hub block audit | `projects/website-factory/execution-cases/bzpm-roadmap/BZPM-M9.5-NEUTRAL-ROOT-UX-v1.md` §11–12 |

---

## UNKNOWN

| Item | What would verify |
|------|-------------------|
| Exact current live `certificates.twig` / `blockdealersform.twig` source | FTP capture from TEST |
| Real unique certificate count on production assets | `/assets/img/certificates/` listing |
| Guaranteed response-time SLA for dealer leads | Operator / CRM policy |
| Whether `checkout/anketa` `dialog=7` routing unchanged | Backend controller on live |
| Full page inventory using these blocks | Site crawl beyond category/home/katalog |

---

## Git status (this task)

| Item | Value |
|------|-------|
| Code changes | **None** |
| Report file added | `reports/SITE-002-M9.8.9-03-CERTIFICATES-DEALERS-MERGE-FORENSIC-AND-DESIGN.md` |
| Commit | **Not performed** (per task charter) |

---

*Forensic + design pass complete. Awaiting operator approval on recommended variant (B) and scope (category PLP first) before implementation pass.*
