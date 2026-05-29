# Section — Hero (master hot zakaz)

**section_id:** `hero`  
**partial:** `workspaces/triumph-manipulator-landing-v5/src/partials/sections/v5-ppc/zakaz/screen-01-hero.html`  
**priority:** P0

## Final current hero (as-built G2)

### Structure

```text
.hero.hero--v5
  .hero__shell
    .hero__main [grid ~1.06fr | 420px]
      .hero__content — H1, lead, hero__specs ×5
      .hero__aside — inline form + tel outline
    .hero-proof.hero-proof--v5 — 4 operational items
    .hero__cargo — 6 cargo cards (modal CTA)
    .hero__notice — anti-junk qualification line
```

### Copy locks 🔒

| Element | Text |
|---------|------|
| **H1** | Аренда манипулятора **в Краснодаре** |
| **Lead** | Перевозка стройматериалов, бытовок, оборудования и тяжёлых грузов манипулятором **5 т**. Подача по Краснодару и краю. Без посредников. |
| **Specs** | Борт 5 т · Стрела 3 т · Вылет 14 м · Кузов 6.2×2.2 м · Мин. заказ 2 ч |
| **Form H2** | Рассчитать стоимость |
| **Form lead** | Оставьте имя и телефон — перезвоним и уточним задачу. |
| **Primary CTA** | Рассчитать стоимость (submit) |
| **Secondary CTA** | Позвонить `tel:+79004658331` |
| **Proof strip** | От 30 минут · Минимальный заказ · Опытные водители · Для юрлиц — безнал |
| **Cargo chips** | Бытовки · ФБС · Кирпич · Арматура · Оборудование · Контейнеры |
| **Notice** | Не работаем с эвакуацией легковых автомобилей и мелкими бытовыми перевозками. |

## Why hero evolved

| Generation | Problem | Fix |
|------------|---------|-----|
| **G0** (v4 index) | Fleet «5–10 т», fake «от XXXX ₽/час», «Свой автопарк» | Removed — MODE 1 violation |
| **G1** (v4 zakaz) | Better copy + form; still evolving layout | Stepping stone |
| **G2** (v5 zakaz) | Capability-first grid, lower-band zoning, ops proof | **Current canonical** |

## Why old hero failed

- Visual clutter — 6 feature paragraphs + rate before CTA
- Semantic overload — user could not extract 5 т / 3 т in 5 sec
- Fake pricing and fleet framing broke PPC honesty
- CTA buried — no inline form

## Visual zones

| Zone | Role | Scan priority |
|------|------|---------------|
| `hero__content` | Capability scan | P0 |
| `hero__aside` | Conversion (form) | P0 |
| `hero-proof--v5` | Operational trust | P1 |
| `hero__cargo` | Task qualification | P1 |
| `hero__notice` | Anti-junk filter | P1 |

## CTA hierarchy

1. **Primary:** form submit «Рассчитать стоимость»
2. **Secondary:** hero form call button; header tel (sticky — verify mobile)
3. **Tertiary:** cargo card modals (`data-cta-source=zakaz-hero-cargo-*`)
4. **Messengers:** footer/modal layer (MAX → TG → WA per doctrine)

**Tension:** PPC instance A1 `cta_semantics.primary_cta: call` vs pack `cta_priority: form` — document as ambiguous; mobile may need call-first order.

## Capability-first logic

Within 5–10 sec user must see: **one machine** parameters → **geo** → **fit** (cargo/tasks) → **how to price** (form) → **how to call**.

## Trust mode in hero

- **No** 4.9★ strip in hero (blueprint asked social strip)
- **Yes** operational proof strip — aligns with hot dispatch intent
- Social proof deferred to trust section (below fold)

## Density observations

- ~20+ distinct messages before scroll — `visual_density: high`
- Zoning (`hero__main` vs lower band) makes density **productive** vs G0 **destructive** overload
- Redundancy: «мин. заказ 2 ч» in specs and proof label

## Mobile risks

| Risk | Severity |
|------|----------|
| Form after 5 specs on stack | high |
| call-first not mirrored in hero | medium |
| 6 cargo tap targets | medium |
| Notice at bottom — may be below fold | medium — QA |

## Semantic locks 🔒

- One machine 5 т / 3 т / 14 m — no fleet
- No fake hero hourly rate
- Geo: Краснодар + край
- Qualification line required (hero notice + tasks denied block)

## Factory notes

- SCSS: `_v5-hero-extensions.scss`, page scope `body[data-page-type='ppc-zakaz-manip']`
- Background: `first-screen` + `hero-bg-final.jpg` + overlay (machine photo not competing with H1)
