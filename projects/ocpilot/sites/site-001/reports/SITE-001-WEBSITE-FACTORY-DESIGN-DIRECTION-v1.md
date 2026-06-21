# SITE-001 — Website Factory Design Direction v1

**Type:** Design direction — visual director / UX strategist output (documentation only)  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Checkpoint:** `site-001-phase1-stable-2026-06`  
**Design owner:** Website Factory  
**Implementation owner:** OCPilot (execution only — not design invention)

**Inputs reviewed:**

- [SITE-001-PHASE1-STABLE-CHECKPOINT-v1.md](SITE-001-PHASE1-STABLE-CHECKPOINT-v1.md)
- [SITE-001-W2-VISUAL-REFRESH-DISCOVERY-v1.md](SITE-001-W2-VISUAL-REFRESH-DISCOVERY-v1.md)
- [SITE-001-W2-VISUAL-SPECIFICATION-v1.md](SITE-001-W2-VISUAL-SPECIFICATION-v1.md)
- [SITE-001-W2-IMPLEMENTATION-ROADMAP-v1.md](SITE-001-W2-IMPLEMENTATION-ROADMAP-v1.md)
- W3-V · W3V2 · W3UX-C1 · W3COLOR-01 · W3ATMOSPHERE-01A/01 · W3VIS rollback · W3-C rollback reports
- QA screenshots (local): `projects/ocpilot/sites/site-001/qa/w3v2-screenshots/`, `w3ux-c1-screenshots/`, `w3atmosphere-01-screenshots/`, `w3vis-01a-screenshots/` (rolled-back reference)

**Explicit exclusions:** No site modifications in this document. No FTP · No CSS/Twig/PHP/JS/DB edits.

---

## Executive summary

Website Factory выбирает **одно** визуальное направление для SITE-001: **«Graphite Salon»** (графитовый автосалон на прохладном stone-canvas).

Цель — изменить **ощущение сайта**, **тональность** и **раскраску** без смены структуры, текстов и коммерческой логики. Красный и тёмные тона из логотипа **сохраняются**; меняется **окружение** — canvas, graphite, глубина, единый язык карточек.

OCPilot уже частично реализовал это направление в **W3ATMOSPHERE-01** (PASS WITH NOTES). Website Factory **не отменяет** успешные элементы, но **заменяет** фрагментированную самодеятельность OCPilot единой авторитетной спецификацией. Следующая волна **W3WF-01** — реализация по этому документу.

---

## Part 1 — Design diagnosis

### 1.1 Почему сайт всё ещё выглядит как OpenCart-шаблон

| Причина | Описание (язык оператора) |
|---------|---------------------------|
| **Белый лист вместо интерьера** | Canvas `#F7F8FA` почти не отличим от карточек `#FFFFFF` — страница = «листы A4 на белом столе», нет **глубины** и **атмосферы**. |
| **Триада white / red / black** | Палитра бинарна: белые прямоугольники, плоский charcoal nav/footer, агрессивный красный `#AA0303`. Нет **благородных нейтралей** между уровнями — ощущение discount-retail, не премиального салона. |
| **Коллаж поверхностей** | Карточки каталога, `four_blocks`, банки, фильтры, формы — один рецепт «белый + серая рамка», но часть блоков осталась в legacy (4px radius, `rgb(208,208,208)`). Сайт читается как **склейка эпох OC**, не единая **раскраска**. |
| **Резкие швы** | Near-black borders `rgb(14,15,16)` / `rgb(16,18,21)` между header и nav, в footer — «дешёвый рез», ломает **тональность** premium shell. |
| **Двойной CSS-слой** | W3-V + W3V2 + override-блоки поверх 6k+ строк legacy literals (56× red, 48× dark, 24× grey border). Cascade непредсказуем — часть страницы «до токенов», часть «после». |
| **Плоские тёмные band** | Nav, footer, `.fancy_form_block`, credit/VIN — один flat `#21242B` без градиента и inner highlight. Тёмное = «второй footer», не **графитовая отделка**. |
| **Чужой hover** | Catalog hover с blue-grey shadow `rgba(55,76,96,0.4)` — конфликтует с graphite depth system. |
| **Neon accents** | Red focus glow `0 0 10px rgb(170,3,3)`, stock green `rgb(0,170,0)` — кричат против спокойной **дорогой** тональности. |

**Вывод:** проблема не в отсутствии брендового красного, а в **неполной атмосферной системе** — слабая **раскраска** уровней, фрагментированная реализация, отсутствие единого визуального языка.

### 1.2 Какие попытки OCPilot провалились и почему

| Wave | Verdict | Почему провал / откат |
|------|---------|----------------------|
| **W3-C Footer Reduction** | **ROLLED BACK** | Оператор отклонил **визуальное направление** (сжатие footer, structural Twig + spacing). Урок: не трогать структуру footer и не менять spacing без явного UX-запроса. |
| **W3VIS-01A** PDP hero surface | **ROLLED BACK** | **Task drift** — OCPilot перегруппировал PDP hero без запроса. Оператор просил site-wide **тональность**, не hero redesign. |
| **W3VIS-01B** CTA hierarchy | **ROLLED BACK** | Изменение commercial hierarchy / flex order — **запрещено** без отдельного charter. |
| **W3-V** (tokens only) | PASS WITH NOTES, **недостаточно** | Radius/shadow tokens без canvas и surface system — оператор: «почти не видно». Косметика без **атмосферы**. |
| **W3V2** (partial identity) | PASS WITH NOTES, **недостаточно** | Override ~272 строк на 7k+ legacy — **слабая палитра**, dual layer. Улучшение есть, но сайт остаётся template-like. |
| **OCPilot self-direction** | **REJECTED pattern** | Волны без Website Factory spec — оператор явно запретил «OCPilot inventing design direction». |

### 1.3 Что сохранить из предыдущих попыток

| Layer | Preserve | Reason |
|-------|----------|--------|
| **Phase 1 branding** | Logo, copy, meta, СИБКАР identity | ACCEPTED checkpoint — immutable |
| **W3UX-C1** `.used_catalog` density | Spacing/height rules on `/cars/*` | PASS WITH NOTES — единственная UX-плотность, явно одобренная |
| **W3-V token bridge** | `--w3v-radius-*`, `--w3v-shadow-*` where compatible | Reuse in WF block; do not delete |
| **W3V2 brand red shift** | `#9E0202` / `#BA0000` | Richer red — aligned with logo, less aggressive than `#AA0303` |
| **W3ATMOSPHERE-01 direction** | Canvas `#EEF1F5`, graphite gradients, unified card recipe, focus ring | Technical PASS — direction matches WF «Graphite Salon»; refine, do not reinvent |
| **W3VIS rollback boundaries** | No PDP hero wrapper, no CTA reorder | Operator hard constraint |
| **W3-C rollback lesson** | No footer structure/spacing collapse | Operator hard constraint |

### 1.4 Что категорически избегать

1. **PDP hero redesign** — никаких unified hero wrappers, flex regroup, CTA tier changes.
2. **Структурные изменения** — Twig, block order, navigation items, footer columns, form fields.
3. **Spacing/density waves** в том же charter — margin/padding/flex/display запрещены (кроме W3UX-C1 preserve).
4. **Слабые token-only patches** — изменение 2–3 переменных без full surface pass = «invisible improvement».
5. **OCPilot design invention** — любое визуальное решение вне [SITE-001-WEBSITE-FACTORY-IMPLEMENTATION-BRIEF-v1.md](SITE-001-WEBSITE-FACTORY-IMPLEMENTATION-BRIEF-v1.md).
6. **Footer reduction / legal collapse** — повтор W3-C.
7. **Neon focus / blue-grey hover** — legacy cheap cues.
8. **Типографическая иерархия** — размеры price/H1/CTA не менять.

### 1.5 Слой с максимальным impact без layout changes

**Приоритет 1 — Canvas + surface levels (раскраска):**

- Body canvas → cool stone `#EEF1F5` (~5% luminance Δ vs cards).
- L2 cards / L2-alt tool panels / L1 graphite bands — чёткая **иерархия уровней**.

**Приоритет 2 — Header + footer atmosphere:**

- Premium shell: white top bar + graphite gradient nav; footer gradient + muted legal.

**Приоритет 3 — Unified card language:**

- Catalog, `four_blocks`, banks, reviews, service cards — один рецепт (12px, graphite border, shadow stack).

**Приоритет 4 — Forms + dark bands:**

- Raised filter panel, calm focus ring, graphite lead bands (не flat black slab).

**Низкий solo-impact:** PDP-only polish без canvas+cards — риск «не видно» (урок W3VIS).

---

## Part 2 — Selected visual direction: «Graphite Salon»

**Одно направление. Без альтернатив.**

Концепция: автосалон на **прохладном stone-полу** с **графитовыми** стенами (nav/footer/dark bands) и **белыми витринами** (карточки авто). Красный — **брендовый акцент**, не агрессивный фон. Ощущение: **дороже**, **современнее**, **не как OpenCart-шаблон**.

### 2.1 Palette

| Role | Token | Value | Usage rule |
|------|-------|-------|------------|
| **Canvas** | `--wf-canvas` | `#EEF1F5` | `body` background — «пол салона» |
| **Section tint** | `--wf-surface-tint` | `#F4F6F9` | Optional homepage section bands — same DOM |
| **Card surface** | `--wf-surface-card` | `#FFFFFF` | Catalog, banks, reviews, four_blocks, bonus |
| **Raised tool** | `--wf-surface-raised` | `#FAFBFC` | Filters, search panels — NOT merchandise |
| **Sunken** | `--wf-surface-sunken` | `#E4E8ED` | Tags, chips, inner strips |
| **Graphite main** | `--wf-graphite-main` | `#2F343E` | Nav, footer base, dark band fill |
| **Graphite secondary** | `--wf-graphite-secondary` | `#3A404C` | Elevated dark panels |
| **Graphite deep** | `--wf-graphite-deep` | `#1A1D24` | Seam accents only — replaces near-black |
| **Gradient top** | `--wf-graphite-gradient-top` | `#353A45` | Header nav / footer gradient start |
| **Gradient bottom** | `--wf-graphite-gradient-bottom` | `#272B33` | Header nav / footer gradient end |
| **Brand red** | `--wf-brand-red` | `#9E0202` | Primary CTA, swiper, key accents — logo-aligned |
| **Brand red hover** | `--wf-brand-red-hover` | `#BA0000` | Hover — no neon outer glow |
| **Brand red soft** | `--wf-brand-red-soft` | `rgba(158,2,2,0.08)` | Tint bands |
| **Brand red muted** | `--wf-brand-red-muted` | `#B82424` | Large price text — desaturated vs CTA |
| **Border default** | `--wf-border` | `rgba(47,52,62,0.10)` | Card outlines |
| **Border hover** | `--wf-border-hover` | `rgba(47,52,62,0.16)` | Card hover |
| **Border on dark** | `--wf-border-on-dark` | `rgba(236,238,242,0.10)` | Footer/header dividers |
| **Text main** | `--wf-text-main` | `#2A2F38` | Body |
| **Text secondary** | `--wf-text-secondary` | `#5A6270` | Labels, logo subtitle |
| **Text on dark** | `--wf-text-on-dark` | `#EDEFF3` | Nav/footer primary |
| **Text on dark muted** | `--wf-text-on-dark-muted` | `#A8AEB8` | Footer legal |
| **Success** | `--wf-success` | `#1F8A4C` | Stock badges — replaces neon green |
| **WhatsApp** | `--wf-whatsapp` | `#25A244` | Distinct — do not merge with brand red |

**Bridge:** map existing `--w3color-*` / `--w3v2-*` to `--wf-*` aliases in one `:root` block — no competing namespaces after W3WF-01.

### 2.2 Graphite / dark tones

- Nav: `linear-gradient(180deg, var(--wf-graphite-gradient-top) 0%, var(--wf-graphite-main) 100%)`.
- Footer: `linear-gradient(180deg, var(--wf-graphite-gradient-top) 0%, var(--wf-graphite-gradient-bottom) 100%)`.
- Dark content bands (`.fancy_form_block`, `.used_car__credit`, slider overlay): same graphite family + optional `rgba(255,255,255,0.04)` inset top highlight.
- **Forbidden:** flat `#000`, `rgb(14,15,16)` 10px seams, `rgb(16,18,21)` hard cuts.

### 2.3 Red usage rules

| Use | Rule |
|-----|------|
| Primary CTA buttons | Fill `--wf-brand-red`; hover `--wf-brand-red-hover` + `--wf-shadow-cta` |
| Price emphasis | `--wf-brand-red-muted` on large price — not full saturation |
| Footer accent | 2px × 40px decorative line under logo zone (CSS pseudo) — accent only |
| Focus ring | `0 0 0 3px rgba(158,2,2,0.18)` — **no** `0 0 10px` neon |
| Background fills | Red only on CTAs and thin accents — **never** large red panels |
| Swiper/pagination | Brand red dots/arrows — consistent token |

### 2.4 Canvas background

```css
body {
  background-color: var(--wf-canvas);
}
```

Optional (homepage only, same blocks):

```css
.home_section--tinted { background-color: var(--wf-surface-tint); }
```

Only if selector already exists — **no new markup**.

### 2.5 Card surfaces

**L2 recipe (all card families):**

- `background: var(--wf-surface-card)`
- `border: 1px solid var(--wf-border)`
- `border-radius: 12px`
- `box-shadow: var(--wf-shadow-sm)`
- Optional: `box-shadow: var(--wf-shadow-sm), var(--wf-shadow-inset-highlight)`

**Hover:** `--wf-shadow-md` + `--wf-border-hover` — **no** blue-grey legacy shadow.

**Families:** `.catalog_item > a/div`, `.partner_banks__item`, `.reviews__item > .inner`, `.four_blocks > div`, `.fancy_two_blocks__item`, `.new_car_bonus__item`, `.contacts_info_block > div`, `.newcar_config__item_inner`.

### 2.6 Borders

- Default: `--wf-border` (translucent graphite).
- Strong emphasis: `#CDD3DC` only where existing strong border used.
- On dark: `--wf-border-on-dark` — 1px, never 10px near-black.

### 2.7 Shadows

| Token | Value |
|-------|-------|
| `--wf-shadow-sm` | `0 1px 2px rgba(42,47,56,0.05), 0 2px 6px rgba(42,47,56,0.04)` |
| `--wf-shadow-md` | `0 2px 8px rgba(42,47,56,0.07), 0 6px 20px rgba(42,47,56,0.05)` |
| `--wf-shadow-lg` | `0 4px 14px rgba(42,47,56,0.08), 0 12px 32px rgba(42,47,56,0.06)` |
| `--wf-shadow-inset-highlight` | `inset 0 1px 0 rgba(255,255,255,0.60)` |
| `--wf-shadow-header` | `0 2px 8px rgba(42,47,56,0.06), 0 1px 0 rgba(42,47,56,0.04)` |
| `--wf-shadow-cta` | `0 4px 14px rgba(158,2,2,0.20)` |
| `--wf-shadow-focus` | `0 0 0 3px rgba(158,2,2,0.18)` |

Policy: graphite-only depth stack; no glassmorphism; no red outer glow on inputs.

### 2.8 Header atmosphere

| Element | Treatment |
|---------|-----------|
| `.singe_bar__wrap` | White L2; `--wf-shadow-header` + `inset 0 1px 0 rgba(255,255,255,0.8)` hairline |
| `nav`, `.offcanvas_nav` | Graphite gradient; top seam `rgba(255,255,255,0.05)` |
| Logo subtitle | `--wf-text-secondary` |
| Scroll duplicate bars | Same tokens |
| CTA buttons | Position/fill unchanged; hover `--wf-shadow-cta` only |

**Frozen:** DOM, CTA count, menu items, sticky behavior.

### 2.9 Footer atmosphere

| Element | Treatment |
|---------|-----------|
| `footer`, `.footer_top` | Vertical graphite gradient |
| Top/bottom seams | 1px `--wf-border-on-dark` — purge 10px near-black |
| Section title dividers | `rgba(237,239,243,0.12)` |
| Legal text | `--wf-text-on-dark-muted` |
| Logo zone | Optional 2px `--wf-brand-red` accent line (pseudo) |
| Footer CTAs | `--wf-shadow-cta` on red buttons |

**Frozen:** columns, links, legal content, forms, height structure.

### 2.10 Form atmosphere

| Element | Treatment |
|---------|-----------|
| Inputs | White or `--wf-surface-raised` fill; `--wf-border`; focus `--wf-shadow-focus` |
| `.search_form`, filter panels | L2-alt raised surface — distinct from product cards |
| `.fancy_form_block`, dark popups | Graphite gradient overlay; not flat `#21242B` |
| Primary submit | `--wf-brand-red` + `--wf-shadow-cta` |

**Frozen:** field count, labels, validation, placement.

### 2.11 Catalog card atmosphere

- White offer card on stone canvas.
- 12px radius unified (override legacy 4px on card group selectors).
- Image area neutral tone — no yellow cast via `background-color` on image wrapper if present.
- Price: `--wf-brand-red-muted`; stock: `--wf-success`.
- **W3UX-C1:** do not alter `.used_catalog` margin/padding/height rules.

### 2.12 PDP widget atmosphere

- **No hero redesign.** Same columns, same CTA order.
- Photo/info columns: subtle L2 border/shadow where selectors exist — atmosphere only.
- Discount widget, credit, VIN: align dark bands to graphite gradient family.
- Canvas uplift makes white widgets read as **panels on stone floor**.

Expected impact: **5/10** on PDP vs **8/10** on catalog — acceptable per operator constraints.

### 2.13 Banks / reviews / four_blocks atmosphere

| Block | Treatment |
|-------|-----------|
| `.partner_banks__item` | L2 card frame — logo centered in defined card, not empty white pad |
| `.reviews__item > .inner` | L2 recipe |
| `.four_blocks > div` | **Migrate from legacy** — highest ROI on `/` and `/about` |
| `.fancy_two_blocks__item` | L2 recipe |

---

## Part 3 — Relationship to live TEST state

| Layer | Status (2026-06-09) | WF action |
|-------|---------------------|-----------|
| W3ATMOSPHERE-01 | **ACTIVE** — PASS WITH NOTES | W3WF-01 **aligns** to this direction; closes gaps (legacy literal purge in override scope) |
| W3-V · W3V2 · W3UX-C1 | **ACTIVE** | Bridge tokens; preserve W3UX-C1 block verbatim |
| W3VIS · W3-C | **ROLLED BACK** | Boundaries remain OUT OF SCOPE |

**W3WF-01 is not a new design experiment** — it is the **authoritative Website Factory implementation** of «Graphite Salon», consolidating fragmented OCPilot layers into one governed CSS wave.

---

## Part 4 — Evidence references

| Evidence | Path |
|----------|------|
| W3V2 before/after | `projects/ocpilot/sites/site-001/qa/w3v2-screenshots/` |
| W3UX-C1 before/after | `projects/ocpilot/sites/site-001/qa/w3ux-c1-screenshots/` |
| W3ATMOSPHERE before/after | `projects/ocpilot/sites/site-001/qa/w3atmosphere-01-screenshots/` |
| W3VIS (reference — rolled back) | `projects/ocpilot/sites/site-001/qa/w3vis-01a-screenshots/` |
| Execution JSON | `.recovery-temp/site-001-w3atmosphere-01-result.json` |

**Note:** QA screenshots are local artefacts; may be gitignored.

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-09 | **CREATED** — Website Factory design direction «Graphite Salon» v1 |

*SITE-001 Website Factory Design Direction v1 — documentation only; no site modifications.*
