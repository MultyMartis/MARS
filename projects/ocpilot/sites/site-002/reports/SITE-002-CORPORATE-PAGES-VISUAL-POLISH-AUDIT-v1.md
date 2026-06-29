# SITE-002 — CORPORATE PAGES VISUAL POLISH AUDIT v1

**Program:** SITE-002 (BZPM / ЗПМ) — Corporate Pages Visual Polish Pass  
**Task ID:** SITE-002 — Home Page Design Language Alignment (STRICT HITL)  
**Mode:** Read-only audit — **no** code · **no** TEST deploy · **no** FTP · **no** git  
**Authority (visual):** Главная страница — https://zpm.new-site.space/  
**Scope (TEST):** M9.14 Delivery · M9.15 Payment · M9.16 Dealers · M9.17 Warranty · M9.18 Custom Manufacturing  
**Date:** 2026-06-28  
**Branch (context):** `mars/canonical-post-recovery`

---

## Методология

| Источник | Использование |
|----------|---------------|
| Live TEST HTML | HTTP 200 на `/`, `/delivery`, `/payment-methods`, `/guarantee`, `/dealers`, `/custom-equipment` (2026-06-28) |
| `assets/css/style.css` work copies | `reports/m9.14-work/` … `m9.18-work/` + merged state in `backups/style.css.pre-m9.18-custom.bak` |
| Implementation reports + QA captures | M9.14–M9.18 deployment reports, `qa-*.html` |
| Home baseline doc | `SITE-002-STABLE-M9.7E-HOMEPAGE-COMPLETE.md` |

**Не использовалось как authority:** PLP, PDP, каталог, фильтры, плотность таблиц каталога.

**Ограничение:** Pixel-level HITL (скриншотное сравнение) не выполнялось в этой сессии; выводы основаны на CSS-токенах, DOM-структуре live TEST и parity work copies. Для финальной полировки рекомендуется operator HITL по viewport 1440 / 1024 / 390.

---

## 1. Global consistency

**Оценка:** Corporate Pages **ощущаются одной внутренней системой** (общие `page-intro`, `zpm-*-section`, `zpm-corp-timeline`, `zpm-corp-faq`, `zpm-commercial-trust` CTA), но **не полностью совпадают с визуальным языком Главной**.

| Аспект | Статус относительно Home |
|--------|---------------------------|
| Типографические токены (`--Title-h*`, `--base-*`, `--mini-*`) | ✓ Те же CSS-переменные |
| Радиусы / цвета / кнопки | ✓ Не изобретены; reuse site tokens |
| Вертикальный ритм секций | ✗ **Переполнен** — двойной `padding-top` (см. §8) |
| Hero / page entry | ✗ Другой паттерн (ожидаемо для internal pages, но lead плотнее Home hero) |
| Карточки / иконки | ✗ Мельче и плотнее, чем `zpm-adv-card` / home benefit weight |
| CTA + форма | △ Reuse `zpm-commercial-trust`, но Home использует `zpm-dealers` + bare `zpm-form` |
| Таблицы / multi-col grids | △ Плотнее home-секций; ближе к catalog density (запрещённый ориентир) |
| Custom Manufacturing accents | ✗ Уникальные accent-borders — нет аналога на Home |

**Итог:** Пять страниц **согласованы между собой на ~75%**, с **Home — на ~55%**. Фаза visual polish **обоснована**.

---

## 2. Delivery (`/delivery`)

### Сравнение с Home

| Элемент | Home (authority) | Delivery (TEST) | Delta |
|---------|------------------|-----------------|-------|
| **Hero / entry** | Full `hero` slider, `section-title__like-h1`, lead `--Heading-*`, gap `--pad-y` / `--pad-gap` | `page-intro` + H1, lead в description; gap `--pad-gap-mini` (10px) | Lead block **плотнее** hero; нет визуального «воздуха» первого экрана |
| **H1 / Lead** | H1 40px; описание 20px/26px semibold | H1 через `page-intro__title`; body 16px/24px | Lead **легче и мельче**, чем hero description |
| **Section spacing** | `main > section`: `--pad-y` top+bottom (30px desktop) | + `.zpm-delivery-section { padding-top: var(--pad-y) }` | **+30px** лишнего top на каждую секцию |
| **Cards (points)** | `zpm-adv-card` min-height 220px, visual illustrations | `zpm-delivery-point-card`, icon 52px circle, `--pad-inner` | Карточки **компактнее**, иконки **в 2× меньше** home-weight |
| **Summary strip** | Нет 1:1; ближе — benefits grid с `--pad-y` gap | 4-col `zpm-delivery-summary`, gap `--pad-gap-line` (10px) | Плотная factual strip — **ок** по смыслу, **тесно** по воздуху |
| **Timeline** | Нет grid-step cards на Home | 7-col `zpm-corp-timeline`, step padding `--pad-inner` | Уникальный corp pattern; внутренний gap 8px **ниже** home card gaps |
| **Table (carriers)** | — | cell padding `12px 16px` | Плотнее card `--pad-inner` (30px) |
| **FAQ** | — | `zpm-corp-faq`, gap `--pad-gap-mini`, button `--pad-inner` | Единый corp pattern |
| **CTA / Form** | Home `zpm-dealers`: 2-col grid, form без cert column | `zpm-commercial-trust` + decor-logo + form-card | **Другой visual weight** vs home dealers block |
| **Footer transition** | `zpm-map` full-size → footer | Standard internal page flow | Без расхождения |

### Рекомендуемые корректировки (visual only)

1. **P1** — Убрать двойной section top padding (глобальный + `.zpm-delivery-section`).
2. **P1** — Увеличить gap `page-intro` container до `--pad-gap` (как hero `--pad-gap` между title и lead).
3. **P2** — Point-card icon 52px → ориентир **80px** (`--img-mini-width`) или увеличить internal gap до `--pad-gap`.
4. **P2** — Timeline step internal gap 8px → `--pad-gap-mini` minimum; между steps сохранить `--pad-gap-line` или поднять до `--pad-gap`.
5. **P3** — CTA actions: унифицировать с Delivery/Payment/Warranty token gaps (см. §7).

---

## 3. Payment (`/payment-methods`)

### Сравнение с Home

| Элемент | Home | Payment | Delta |
|---------|------|---------|-------|
| **Page intro** | — | 3 абзаца lead (плотный блок) | Lead **длиннее и тяжелее** первого экрана vs Delivery; тот же tight `page-intro` gap |
| **First section** | — | Timeline сразу после intro на `--main-light-color` | Первая секция **сразу tinted** — на Home tint через `section:nth-of-type(even)` |
| **Timeline** | — | 6-col grid | Аналог Delivery; те же spacing issues |
| **Proof cards** | `zpm-adv-cards` 2×2, min-height 220px | 5-col `zpm-payment-proof__grid`, gap `--pad-gap-line` | **Наиболее плотная** card grid в программе — catalog-like density |
| **Methods table** | — | Standard corp table 12×16 | Как Delivery |
| **Legal facts strip** | — | 3-col, как summary | Consistent with Delivery summary |
| **CTA** | — | `zpm-commercial-trust`, gaps `--pad-gap-line` / `--pad-gap` | Эталон для trio Delivery/Payment/Warranty |

### Рекомендуемые корректировки

1. **P1** — Double section padding (как Delivery).
2. **P1** — Proof grid: 5-col → **максимум 4-col** desktop (как `zpm-adv-cards__grid--row4` на Home) или увеличить gap до `--pad-gap`.
3. **P2** — Между H2 и intro сохранить `--pad-gap`; после длинного intro добавить **visual breathing** перед timeline (margin-bottom на intro block — без copy change).
4. **P3** — Выравнять tinted timeline section padding-bottom с Delivery/Warranty (`padding-bottom: var(--pad-y)` only, без лишнего global bottom если исправлен P1).

---

## 4. Warranty (`/guarantee`)

### Сравнение с Home

| Элемент | Home | Warranty | Delta |
|---------|------|----------|-------|
| **Coverage table + summary** | — | Table → 4-col summary | Table-to-summary transition **плотный** (`margin: var(--pad-gap) 0`) |
| **Process timeline** | — | 5-col, tinted section | Same corp timeline pattern |
| **Verification block** | — | `padding-top: calc(var(--pad-y) * 0.75)`; H2 downgraded to `--Title-h3-*` | **Subordinate weight** — ok по charter; **уникальный** top padding vs siblings |
| **Outcome cards** | 2-col adv-like | 2-col `zpm-warranty-outcome`, title margin 8px | Близко к home 2-col cards; title-to-text **8px** vs home card `--pad-gap-mini`/20px |
| **FAQ** | — | Shared `zpm-corp-faq` | — |
| **CTA** | — | Same as Delivery/Payment | — |

### Рекомендуемые корректировки

1. **P1** — Double section padding.
2. **P2** — Outcome card title margin 8px → `--pad-gap-mini` (10px) или `--pad-gap` для parity с home card text stacks.
3. **P2** — Verification `padding-top: 0.75` → **`var(--pad-y)`** или 0 если предыдущая секция уже tinted (единый section rhythm).
4. **P3** — Summary grid gap `--pad-gap-line` → `--pad-gap` на desktop ≥1025.

---

## 5. Dealers (`/dealers`)

### Сравнение с Home

| Элемент | Home | Dealers | Delta |
|---------|------|---------|-------|
| **Dealers block** | `zpm-dealers` + `zpm-universal__grid`, gap `--pad-inner`, bare form | Full corp page; CTA = `zpm-commercial-trust` | **Разный CTA visual language** с home dealers teaser |
| **Partner matrix tables** | — | 3 large tables | Highest table density in program |
| **OEM proof stack** | About/adv **large** media cards | White cards on `--main-light-color`, gap `--pad-gap-line` | Background tint ✓ (home even sections); card gap **тесный** |
| **OEM trust row** | — | `padding-top/bottom: calc(var(--pad-y) * 0.5)` | **Уникальный** half-padding — ломает canonical `--pad-y` |
| **Process timeline** | — | 5-col | Standard corp |
| **Supply chain diagram** | — | Vertical nodes, padding 14×16, connector 12px | **Нет home analog**; acceptable if kept internally consistent |
| **CTA actions** | Home: single `btn` + text | `gap: 12px 20px` hardcoded | **Не token-based** (vs `--pad-gap-line` на Delivery) |
| **CTA contacts** | — | `gap: 12px 24px` hardcoded | Same issue |

### Рекомендуемые корректировки

1. **P1** — Double section padding.
2. **P1** — CTA gaps: `12px 20px` / `12px 24px` → **`var(--pad-gap-line)` / `var(--pad-gap)`** (parity Delivery/Payment/Warranty).
3. **P2** — OEM row half-padding → full **`var(--pad-y)`** section rhythm или 0 если внутри tinted block.
4. **P2** — Proof stack gap `--pad-gap-line` → `--pad-gap`.
5. **P3** — Matrix table wrap margin — добавить `--pad-gap` после H2 перед table (если визуально тесно на HITL).

---

## 6. Custom Manufacturing (`/custom-equipment`)

### Сравнение с Home

| Элемент | Home | Custom | Delta |
|---------|------|--------|-------|
| **Page length / density** | Long scroll, но **крупные** section blocks | 4 tables + 8-step timeline + OEM + FAQ | **Самая высокая** information density в программе |
| **Process section** | — | `border-top/bottom: 2px solid accent`; steps `border-width: 2px`, `box-shadow` | **Accent framing нет на Home** — strongest visual outlier |
| **Timeline** | — | 8-col desktop | Ultra-wide grid → micro cards; **не home-like air** |
| **Approval gate** | — | `border: 2px solid accent-02`, badge block | Unique emphasis — charter-driven; polish = spacing only |
| **Outcomes section** | — | `border-top: 3px solid accent`; thead extra padding + accent bottom border | **Second accent outlier** |
| **OEM production image** | Home about: full image in grid | 16:9 bordered image max 920px | Acceptable; border matches site tokens |
| **CTA** | — | Same hardcoded gaps as Dealers | Same fix as Dealers |

### Рекомендуемые корректировки

1. **P1** — Double section padding.
2. **P1** — **Не добавлять** новые accent borders; polish pass may **only reduce** visual noise: рассмотреть ослабление `border-top/bottom 2–3px` до **1px `var(--border-color)`** *если operator подтвердит* — иначе оставить (charter emphasis). *Зафиксировать как HITL decision.*
3. **P1** — 8-col timeline → **max 4-col** desktop (CSS already breaks 1440→4); проверить min card width vs home adv card proportions.
4. **P2** — CTA token gaps (как Dealers).
5. **P2** — Scope groups / triggers list gap 10px → `--pad-gap-mini` / `--pad-gap` consistently.
6. **P3** — Outcomes thead `font-size: calc(* 1.05)` → base size (home tables N/A; avoid catalog-style emphasis).

---

## 7. Cross-page consistency

### Где страницы совпадают (оправдано)

| Pattern | Pages | Note |
|---------|-------|------|
| `page-intro` shell | All 5 | Internal page standard; Home uses hero instead |
| `zpm-*-section__title` + `--pad-gap` below H2 | All 5 | Matches `section .section-title__like-h2` |
| `max-width: 920px` prose | All 5 | Narrower than home `zpm-about__text` (740px mobile cap) — **corp wider** |
| `zpm-corp-timeline` base | Delivery, Payment, Warranty, Dealers, Custom | Shared component |
| `zpm-corp-faq` | Delivery, Warranty, Dealers, Custom | Payment — no FAQ (by IA) |
| Corp table styling | All with tables | Unified 12×16, striped rows |
| Summary / facts strips | Delivery, Payment, Warranty | Same label/value pattern |

### Где страницы расходятся

| Difference | Pages | Justified? | Polish action |
|------------|-------|------------|---------------|
| CTA action gaps: tokens vs hardcoded | Delivery/Payment/Warranty ✓ · Dealers/Custom ✗ | **No** | Unify to `--pad-gap-line` / `--pad-gap` |
| CTA `margin-top` vs `margin-bottom` on actions | Delivery trio `margin-top` · Dealers/Custom `margin-bottom` | **No** | Single direction + token |
| Tinted section padding | Various `-timeline-section`, `-proof`, `-oem`, `-process` | Partially (content hierarchy) | Unify top/bottom after fixing double pad |
| OEM row `0.5 * pad-y` | Dealers only | **No** | Normalize |
| Custom accent borders / shadows | Custom only | Charter emphasis — **maybe** | HITL |
| Proof card columns: 5 vs 2 vs 4 | Payment 5 · Delivery outcomes 2 · Warranty outcomes 2 | Content-driven | Visual gap harmonization only |
| Payment opens with timeline | Payment only | IA order — **yes** | Spacing only |
| FAQ presence | No FAQ on Payment | IA — **yes** | — |

---

## 8. Visual language inventory (authority: Home only)

Извлечено из live Home + `style.css` (M9.7E / manual UI baseline).

### Canonical hero rhythm (Home)

| Token / rule | Value |
|--------------|-------|
| Hero content min-height | `58vh` |
| Hero content padding | `calc(var(--pad-y) + 140px)` top · `calc(var(--pad-y) + 20px)` bottom |
| Title → description (inner) | `--pad-gap` (15px) in `--top` wrap |
| Info wrap → buttons | `--pad-y` (30px) |
| H1 | `--Title-h1-*` (40px/40px desktop) |
| Lead / description | `--Heading-*` (20px/26px, weight 500) |

**Corporate mapping:** `page-intro` ≠ hero; для corp pages polish target = **приблизить lead weight/spacing к hero**, не вводить hero slider.

### Canonical section spacing (Home)

| Rule | Value |
|------|-------|
| `main > section` | `padding-top + padding-bottom: var(--pad-y)` |
| Desktop `--pad-y` | 30px |
| Tablet/mobile `--pad-y` | 50px (≥1024 breakpoint) |
| Even sections | `background: var(--main-light-color)` (#F7F8FD) |
| `zpm-adv-bottom` exception | `80px 0 120px` — **не** применять к corp |

**Corporate drift:** `.zpm-*-section { padding-top: var(--pad-y) }` **дублирует** global top → effective inter-section **90px desktop** vs home **60px**.

### Canonical card padding (Home)

| Pattern | Padding / gap |
|---------|---------------|
| `zpm-adv-card__txt` | 30px top/left; internal gap 20px |
| `zpm-adv-cards__grid` | gap `--pad-gap` (15px) |
| `zpm-adv-card` min-height | 220px |
| `zpm-commercial-trust__benefit-icon` (site pattern) | 110×110 circle |
| `zpm-commercial-trust__service` | `--pad-inner` padding, gap `--pad-gap` |

**Corporate cards:** `--pad-inner` padding ✓; gaps often `--pad-gap-line` (10px) ✗; icons 52px ✗.

### Canonical heading spacing (Home)

| Level | margin-bottom |
|-------|---------------|
| H2 (`section-title__like-h2`) | `--pad-gap` (15px) |
| H3 (`section-title__like-h3`) | 10px (`--pad-box`) |
| `section .section-title__like-h1` | `--pad-inner` (30px) |

**Corporate:** `.zpm-*-section__title { margin: 0 0 var(--pad-gap) }` — **aligned ✓**.

### Canonical paragraph rhythm (Home)

| Context | Rule |
|---------|------|
| `page-intro > .container` | gap `--pad-gap-mini` (10px) |
| `zpm-dealers__text > p` | margin-bottom `--pad-box` (15px) |
| `zpm-about__text` | prose in universal grid |

**Corporate:** intro/body margin-bottom `--pad-gap`; lists gap 6–10px — **acceptable**, slightly tighter than home dealer text.

### Canonical CTA spacing (Home — `zpm-dealers` block)

| Element | Rule |
|---------|------|
| Grid | `zpm-universal__grid` — 2 columns, gap `--pad-inner` |
| Form | bare `zpm-form`, gap `--pad-gap` fields |
| Primary action | single `btn` below text |

**Corporate CTA:** `zpm-commercial-trust__wrap` gap `--pad-gap`; form-card `--pad-inner`; decor-logo — **heavier** than home dealers. Polish = spacing tokens, **not** structural revert.

### Canonical form spacing (Home)

| Element | Value |
|---------|-------|
| `zpm-form__grid` | gap `--pad-gap` |
| Inputs | line-height 48px, padding 0 15px |
| Submit | `btn` height 50px |

**Corporate:** reuse `zpm-commercial-trust__form-card` + `zpm-form` — **aligned** if card padding not compressed.

### Canonical FAQ spacing (Home)

**Прямого FAQ-accordion на Home нет.** Ближайший home pattern: `--pad-inner` clickable rows, `--pad-gap-mini` list gap (corp FAQ already close).

| Corp FAQ | Value |
|----------|-------|
| List gap | `--pad-gap-mini` |
| Button padding | `--pad-inner` |
| Toggle icon | 22px (corp) vs 24px (legacy delivery-faq in older CSS block) |

**Action:** ensure single `zpm-corp-faq` icon size **22px** everywhere; remove legacy duplicate rules if still loaded (dead CSS in `style.css` pre-M9.14 block — cleanup optional, not visual if unused).

### Canonical timeline spacing (Home)

**Нет grid timeline на Home.** Oриентир для polish: **`zpm-adv-cards__grid` gap `--pad-gap`** + card **`--pad-inner`** padding — не 7–8 columns of micro-cards.

| Corp timeline today | Value |
|---------------------|-------|
| Grid gap | `--pad-gap-line` (10px) |
| Step padding | `--pad-inner` |
| Step internal gap | 8px |
| Badge | 36×36 (Custom process: 44×44) |

---

## 9. Exact polish queue

Только визуальные CSS/spacing правки. Без copy, IA, Twig structure, новых компонентов.

### Priority 1 — Systemic (all corp pages)

| ID | Target | Change |
|----|--------|--------|
| **VP-01** | `.zpm-delivery-section`, `.zpm-payment-section`, `.zpm-warranty-section`, `.zpm-dealers-section`, `.zpm-custom-section` | Remove redundant `padding-top: var(--pad-y)` **or** reset `main.zpm-*-page > section` global padding to avoid double stack |
| **VP-02** | `.page-intro > .container` (corp routes only) | gap `var(--pad-gap-mini)` → **`var(--pad-gap)`**; optional lead `font-size/weight` toward hero description |
| **VP-03** | Dealers + Custom CTA | Replace hardcoded `12px 20px` / `12px 24px` with **`var(--pad-gap-line)` / `var(--pad-gap)`**; align margin direction with Delivery trio |
| **VP-04** | Payment proof grid | Reduce desktop columns or increase gap to **`var(--pad-gap)`** — target home `zpm-adv-cards` density |
| **VP-05** | Custom timeline desktop | Cap at **4 columns** ≥1440; increase step gap to **`var(--pad-gap)`** |

### Priority 2 — Per-page harmonization

| ID | Page | Change |
|----|------|--------|
| **VP-06** | Delivery | Point-card icon scale; timeline internal gap → `--pad-gap-mini` minimum |
| **VP-07** | Payment | Intro → timeline breathing room (margin only) |
| **VP-08** | Warranty | Outcome title spacing; verification section top padding normalize |
| **VP-09** | Dealers | OEM row half-padding; proof stack gap → `--pad-gap` |
| **VP-10** | Custom | Scope/triggers list gaps; process/outcomes accent borders — **HITL** (keep vs soften to 1px neutral) |
| **VP-11** | All summary/facts strips | gap `--pad-gap-line` → **`var(--pad-gap)`** on desktop |

### Priority 3 — Fine tuning (after HITL)

| ID | Target | Change |
|----|--------|--------|
| **VP-12** | Corp tables | cell padding `12px 16px` → **`14px 20px`** or `var(--pad-gap) var(--pad-inner)` fraction — if still feels catalog-dense |
| **VP-13** | `zpm-corp-faq__button::after` | Unify 22px across pages; verify reduced-motion |
| **VP-14** | CTA `zpm-commercial-trust__lead` max-width | Home lead max 730px; corp uses default — optional cap for line-length parity |
| **VP-15** | Footer transition | Ensure last section `padding-bottom` matches home last content section (`--pad-y` only, no double) |
| **VP-16** | Dead CSS | Remove orphaned pre-M9.14 `zpm-delivery-hero` / `zpm-delivery-faq` blocks from `style.css` if confirmed unused (**hygiene**, not user-visible unless conflict) |

---

## 10. Final verdict

### **READY FOR VISUAL POLISH**

**Обоснование:**

- Архитектура, copy и block order **не требуют изменений**.
- Визуальные токены **общие**, но **ритм и плотность** systematically drift от Home: двойной section padding, tighter grids, мельче icon weight, Dealers/Custom CTA hardcoded gaps, Custom accent framing.
- Cross-page corp consistency **хорошая**, но не достаточная для «один дизайнер» с Home без polish pass.

**Не является блокером:** отсутствие hero на corp pages (internal page pattern). **Является блокером polish-complete:** VP-01 + VP-03 без HITL на Custom accents (VP-10).

---

## Safety confirmation

| Rule | Status |
|------|--------|
| OpenCart / Twig / PHP / CSS / JS unchanged on TEST | ✓ |
| FTP not used | ✓ |
| Production not touched | ✓ |
| Git commit / push | ✓ None |
| Only deliverable created | `SITE-002-CORPORATE-PAGES-VISUAL-POLISH-AUDIT-v1.md` |

---

## UNKNOWN

| Item | Note |
|------|------|
| Pixel-perfect screenshot delta | QA PNG folders referenced in M9.14–M9.18 reports not present in repo workspace at audit time; operator HITL recommended |
| Live `style.css` post-M9.18 | Audit uses work copies + `pre-m9.18-custom.bak`; if operator edited TEST manually after M9.18, live may differ — verify against https://zpm.new-site.space/ |
| Custom accent borders | Charter vs Home conflict — requires **explicit operator HITL** before softening |

---

## SECURITY RISK

None identified (read-only analysis).

---

## Registration

| Field | Value |
|-------|--------|
| **Status** | **TRACKED** — Scope A documentation closeout (2026-06-30) |
| **Run** | OCPilot **4.169** |
| **Closeout report** | [SITE-002-DOCUMENTATION-CLOSEOUT-SCOPE-A.md](SITE-002-DOCUMENTATION-CLOSEOUT-SCOPE-A.md) |
| **Post-audit visual authority** | `SITE-002-STABLE-LIVE-OPERATOR-MANUAL-POLISH-01` (visual baseline retained under `SITE-002-STABLE-LIVE-LOCAL-FONTS-01`) |

Audit conclusions above are **unchanged** — historical input to Visual Polish Pass 1.x only.
