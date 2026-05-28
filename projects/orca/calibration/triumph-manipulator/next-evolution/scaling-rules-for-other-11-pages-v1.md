# Scaling Rules for Other 11 Pages v1

**Source:** Triumph 12-group Full Cycle v1.1 structure + calibration on master hot.

## Stable across all routes (do not vary)

| Element | Rule |
|---------|------|
| **Section skeleton** | Hero → specs → tasks (allowed/denied) → order steps → pricing factors → trust → B2B → proof strip → FAQ → contact |
| **CTA system** | Primary расчёт + tel; messengers secondary in footer/modal |
| **Trust sources** | Яндекс + Авито only |
| **Specs table shape** | dl/grid with icons — same component |
| **B2B logic** | Withoutнал block where applicable |
| **FAQ pattern** | Route-tuned Q&A; accordion component |
| **Semantic locks** | No fleet, no fake price, anti-evacuation, one-machine per route |
| **PPC robots default** | noindex,nofollow |
| **Factory workspace pattern** | `v5-ppc/<slug>/` partials + shared `v5-page01` shell |
| **`hero--v5` layout** | Grid + inline form — reuse SCSS |
| **Price framing** | По задаче + factors block |
| **Form fields** | Имя + телефон (+ consent) unless B2B charter says more |

## Vary per route (pack must specify)

| Element | Variation |
|---------|-----------|
| **Hero H1** | Match **that** group’s primary ad (аренда / 5 т / бытовки / …) |
| **Hero scenario** | Background crop; optional task image on use-case |
| **Cargo / fastlink chips** | 4–6 items from use-case set |
| **Proofs** | Ops vs social mix per intent tier |
| **Task blocks** | Allowed list = route-specific; denied = route-tuned |
| **Specs values** | 5 т default; **6×6 route** uses its machine locks |
| **Pricing framing emphasis** | Price-intent groups stress factors + FAQ price Q |
| **Visual scene** | `second-screen-<slug>.jpg` per route |
| **Denied tasks** | Evacuation always; add route junk (e.g. мелкие перевозки) |
| **Lead copy** | Use-case verb in lead |
| **B2B prominence** | Higher on `06-b2b-yurlica` route |
| **Intercity geo** | Край route expands geo copy |

## Route map (11 siblings — from landing-pages INDEX)

| # | Blueprint file | Vary hero H1 toward |
|---|----------------|---------------------|
| 1 | `02-use-case-bytovka.md` | Бытовки |
| 2 | `03-use-case-stroymaterialy.md` | Стройматериалы |
| 3 | `04-use-case-oborudovanie.md` | Оборудование |
| 4 | `05-capability-5-ton.md` | 5 тонн (handoff exists) |
| 5 | `06-b2b-yurlica.md` | Юрлица / безнал |
| 6 | `07-capability-6x6-vezdekhod.md` | 6×6 вездеход |
| 7 | `08-intercity-krai.md` | По краю |
| 8 | `09-use-case-fbs-zhb.md` | ФБС / ЖБИ |
| 9 | `10-use-case-konteynery.md` | Контейнеры |
| 10 | `11-use-case-armatura.md` | Арматура |
| 11 | `12-use-case-kirpich-bloki.md` | Кирпич / блоки |

**Master hot (`01`)** = this calibration case.

## Per-route pack checklist (copy before Factory)

- [ ] `group_id` + ads JSON slice attached
- [ ] H1 ↔ primary ad continuity table
- [ ] `hero_layout` + `trust_hero_mode`
- [ ] `cargo_cards[]` or chips list
- [ ] `denied_tasks[]`
- [ ] `factory_notes` with `v5-ppc/<slug>/` paths
- [ ] `approved_for_factory` gate

## Anti-patterns when scaling

- Copying master hot H1 «Аренда» onto capability pages
- Sharing denied tasks list unchanged across use-cases
- Importing v4 index hero partial on any route
- Skipping handoff because 5-ton exists

## Calibration reuse

Each new route: **one calibration loop folder** under `triumph-manipulator/<slug>/` OR subfolder — **deferred** until v0 loop reviewed by operator.
