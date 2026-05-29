# Scaling Rules for 11 Pages v2

**Source:** `calibration/.../next-evolution/scaling-rules-for-other-11-pages-v1.md`  
**Visual semantics layer:** per-route pack must set fields, not copy master hot defaults.

## Stable (all routes)

| Element | Visual semantics |
|---------|------------------|
| `hero_layout_mode` | `grid_form_aside` |
| Section skeleton | `frontend_priority` default stack |
| Trust sources | reviews section required |
| MODE 1 locks | `semantic_focus: one_machine`, no fake hero price |
| Form | short name + phone + consent |

## Vary per route (pack required)

| Element | Field |
|---------|-------|
| Hero H1 | `primary_ad_variant` — match **that** group's ad |
| Trust hero | `trust_mode` per intent tier |
| Cargo/chips | `cargo_cards_max`, list from use-case |
| Specs values | route machine locks (e.g. 6×6) |
| Density | use_case often `medium` vs master `high` |
| B2B | elevate `semantic_focus: b2b_payment` on yurlica |

## Route map

| # | Blueprint | Hero H1 emphasis |
|---|-----------|------------------|
| 1 | 02-bytovka | Бытовки |
| 2 | 03-stroymaterialy | Стройматериалы |
| 3 | 04-oborudovanie | Оборудование |
| 4 | 05-capability-5-ton | 5 тонн (handoff exists) |
| 5 | 06-b2b-yurlica | Юрлица |
| 6 | 07-capability-6x6 | 6×6 |
| 7 | 08-intercity-krai | По краю |
| 8 | 09-fbs-zhb | ФБС / ЖБИ |
| 9 | 10-konteynery | Контейнеры |
| 10 | 11-armatura | Арматура |
| 11 | 12-kirpich-bloki | Кирпич |

**01 master hot** = canonical visual semantics example.

## Anti-patterns

- Copy master hot H1 «Аренда» onto capability pages
- Import v4 index hero
- Skip visual semantics because 5-ton handoff exists
- Same `trust_mode` on all routes without review

## Per-route calibration

Each sibling: subfolder under `calibration/triumph-manipulator/<slug>/` **deferred** until operator reviews v0 loop.

## Pack checklist (before Factory)

- [ ] `group_id` + ads slice
- [ ] full `visual_semantics.fields`
- [ ] H1 ↔ ad table
- [ ] `drift_acceptance.destructive: []`
- [ ] `factory_hints.partial_paths`
- [ ] `approved_for_factory`
