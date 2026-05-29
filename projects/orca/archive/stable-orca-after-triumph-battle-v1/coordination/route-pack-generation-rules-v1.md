# Route Pack Generation Rules v1

**Scope:** 11 remaining PPC routes (+ master hot pack completion) for Triumph Manipulator  
**Blueprint SoT:** `projects/orca/ppc/triumph-manipulator/landing-pages/`  
**V6 scaffold slugs:** `workspaces/triumph-manipulator-landing-v6/src/partials/sections/v5-ppc/<slug>/`  
**Stable shell:** `hero_layout_mode: grid_form_aside`, shared `v5-page01/*` trust blocks

For each route, ORCA pack **must** define all dimensions below before `approved_for_factory`.

---

## Global rules (all 11 routes)

| Rule | Requirement |
|------|-------------|
| V6 target | `factory/frontend-hints.md` points to V6 paths only |
| MODE 1 | No Factory work on paid route without pack + handoff |
| H1 | Matches **primary** ad variant for that `group_id` |
| Machine story | One machine unless blueprint explicitly allows alternate (vezdehod 6×6) |
| Denied tasks | Present — route-specific junk filters from blueprint |
| Visual semantics | Full `visual_semantics.fields` — no default-only bundle |
| Density | Apply tier from [semantic-density-control-v1.md](semantic-density-control-v1.md) |
| Registry | `route_id` aligns with `landing-route-registry.json` |

---

## Route generation matrix

### HIGH priority routes

#### `5-tonn` — capability (`05-capability-5-ton.md`)

| Dimension | Rule |
|-----------|------|
| **Hero adaptation** | H1 capability-first: «Манипулятор 5 тонн…»; instant 5/3/14 specs; no fleet |
| **Cargo adaptation** | Tasks aligned to 5 т limits — стройматериалы, ФБС, арматура in **scope** |
| **Tasks adaptation** | Allowed tasks from blueprint §ALLOWED; emphasize parameter fit |
| **Denied tasks** | No evacuation, no oversize beyond locks, no «любой вес» |
| **Pricing framing** | По задаче; min order 2 ч; **no** hero hourly fake rate |
| **FAQ strategy** | Capability + cost factors + timing; tonnage objections |
| **Trust emphasis** | `operational_proof` hero strip; reviews section required |
| **Qualification rules** | Fast parameter scan; anti-broad-rental |
| **Visual semantic profile** | `visual_density: medium-high`, `semantic_focus: [one_machine, capability_first]`, `cargo_cards_max: 4–6` |
| **Pack reference** | `triumph-manipulyator-5-tonn-pack-v0.md` + existing handoff (update for V6 paths) |
| **V6 slug** | `v5-ppc/5-tonn/` |

#### `bytovki` — use-case (`02-use-case-bytovka.md`)

| Dimension | Rule |
|-----------|------|
| **Hero adaptation** | H1: перевозка бытовок; lead = fit for вагончик/бытовка |
| **Cargo adaptation** | Cargo cards = бытовка types, access constraints — max 4–5 |
| **Tasks adaptation** | Install/delivery paths for modular buildings |
| **Denied tasks** | Not generic «аренда манипулятора»; no unrelated cargo |
| **Pricing framing** | Distance, access, weight of unit — no fixed lowball |
| **FAQ strategy** | Подъезд, габариты, сроки, что входит |
| **Trust emphasis** | Task-fit proof + reviews; optional case photo |
| **Qualification rules** | «Подходит ли под бытовку» in lead or hero lower |
| **Visual semantic profile** | `visual_density: medium`, `semantic_focus: [use_case_bytovka]` |
| **V6 slug** | `v5-ppc/bytovki/` |

#### `stroymaterialy` — use-case (`03-use-case-stroymaterialy.md`)

| Dimension | Rule |
|-----------|------|
| **Hero adaptation** | H1: доставка стройматериалов; bulk/pallet framing |
| **Cargo adaptation** | Cards: плиты, блоки, паллеты — within 5 т |
| **Tasks adaptation** | Unload + placement where blueprint allows |
| **Denied tasks** | No warehouse logistics promises without evidence |
| **Pricing framing** | Volume, distance, unload complexity |
| **FAQ strategy** | Вес, объём, разгрузка, срок подачи |
| **Trust emphasis** | Operational repeatability |
| **Qualification rules** | Weight/volume caps explicit |
| **Visual semantic profile** | `medium` density; cargo max 5 |
| **V6 slug** | `v5-ppc/stroymaterialy/` |

#### `vezdehod` — capability 6×6 (`07-capability-6x6-vezdekhod.md`)

| Dimension | Rule |
|-----------|------|
| **Hero adaptation** | H1: 6×6 / вездеход / бездорожье; **different** spec set |
| **Cargo adaptation** | Terrain-limited tasks — no urban-only claims |
| **Tasks adaptation** | Off-road access, стройка в поле |
| **Denied tasks** | No pretending standard 5т truck = 6×6 |
| **Pricing framing** | Route difficulty, mobilization |
| **FAQ strategy** | Грунт, проходимость, ограничения |
| **Trust emphasis** | Machine-specific proof; photo if available |
| **Qualification rules** | Geo + terrain qualification |
| **Visual semantic profile** | `semantic_focus: [one_machine, terrain_capability]` |
| **V6 slug** | `v5-ppc/vezdehod/` |

---

### MEDIUM priority routes

#### `armatura` (`11-use-case-armatura.md`)

| Dimension | Rule |
|-----------|------|
| Hero | Металлоконструкции / арматура H1 |
| Cargo | Long-load, bundle, crane reach |
| Denied | No «любой металл» without limits |
| Pricing | Length, weight, unload |
| FAQ | Длина, вес пачки, разгрузка |
| Trust | Safety + experience wording — evidence-backed only |
| Visual | `medium` density; cargo 4 |
| Slug | `armatura` |

#### `konteynery` (`10-use-case-konteynery.md`)

| Dimension | Rule |
|-----------|------|
| Hero | Контейнеры / блок-контейнеры |
| Cargo | Container sizes, crane pick points |
| Denied | No port/logistics claims without scope |
| Pricing | Container type, distance |
| FAQ | Габариты, доступ, фундамент |
| Trust | Operational |
| Visual | `medium`; watch hero height |
| Slug | `konteynery` |

#### `oborudovanie` (`04-use-case-oborudovanie.md`)

| Dimension | Rule |
|-----------|------|
| Hero | Оборудование / станки |
| Cargo | Industrial units, fragility notes |
| Denied | No precision engineering guarantees |
| Pricing | Rigging complexity |
| FAQ | Упаковка, крепление, страхование — SAFE UNKNOWN if not evidenced |
| Trust | Careful handling |
| Visual | `medium-high` if many cargo types — cap cards |
| Slug | `oborudovanie` |

#### `kirpich-bloki` (`12-use-case-kirpich-bloki.md`)

| Dimension | Rule |
|-----------|------|
| Hero | Кирпич / блоки / поддоны |
| Cargo | Palletized materials |
| Denied | No «весь склад» framing |
| Pricing | Weight, trips, unload |
| FAQ | Поддоны, этаж, разгрузка |
| Trust | Standard operational |
| Visual | `medium`; cargo 4–5 |
| Slug | `kirpich-bloki` |

---

### LOWER priority routes

#### `yurlic` — B2B (`06-b2b-yurlica.md`)

| Dimension | Rule |
|-----------|------|
| Hero | Юрлица / безнал / НДС / документы |
| Cargo | Contract objects, recurring supply — not consumer tasks |
| Tasks | Invoicing, acts, fleet **forbidden** |
| Denied | B2C shortcuts that weaken payment story |
| Pricing | Contract framing, not consumer «от 1000» |
| FAQ | Документы, НДС, сроки оплаты |
| Trust | `semantic_focus: [b2b_payment, documents]` |
| Qualification | Legal entity fit |
| Visual | Elevate B2B block priority in `frontend_priority` |
| Slug | `yurlic` |

#### `kray` — geo (`08-intercity-krai.md`)

| Dimension | Rule |
|-----------|------|
| Hero | По краю / межгород — geo explicit |
| Cargo | Distance bands, city pairs — no nationwide |
| Tasks | Intercity delivery, timing |
| Denied | Fake «вся Россия» |
| Pricing | Distance, mobilization, waiting |
| FAQ | Зоны, доплата за км |
| Trust | Geo operational proof |
| Qualification | Service area locks |
| Visual | `medium`; avoid hero clutter with many cities |
| Slug | `kray` |

#### `fbs-zhbi` (`09-use-case-fbs-zhb.md`)

| Dimension | Rule |
|-----------|------|
| Hero | ФБС / ЖБИ — heavy elements |
| Cargo | Element types within tonnage |
| Denied | No structural engineering certification claims |
| Pricing | Element weight, crane time |
| FAQ | Допуски, основание, согласование — mark UNKNOWN if needed |
| Trust | Heavy lift experience — evidenced |
| Visual | `medium-high`; strict cargo cap |
| Slug | `fbs-zhbi` |
| **URL note** | Registry: `/perevozka-fbs-zhbi/` — not `/fbs-zhbi/` |

---

## Master hot (`zakaz`) — pack completion (not in the 11)

| Dimension | Rule |
|-----------|------|
| Status | V6 `index.html` built; pack draft exists |
| Remaining ORCA work | Sign pack, formal handoff, resolve D1/D2 drift (qualification line, multi-ad H1) |
| Blueprint | `01-master-hot-general.md` |
| Do not | Re-implement frontend — semantic pack + approval trail |

---

## Per-route authoring checklist

- [ ] Blueprint read end-to-end
- [ ] `group_id` + ads from instance JSON
- [ ] `visual_semantics.fields` complete
- [ ] Hero + tasks + denied + FAQ slots drafted
- [ ] Density budget signed
- [ ] `factory/forbidden-drift.md` includes route-specific destructive patterns
- [ ] `frontend-hints.md` lists V6 partial paths
- [ ] Readiness checklist passed
- [ ] Matrix row updated

---

## Related

- [route-priority-roadmap-v1.md](route-priority-roadmap-v1.md)
- [remaining-routes-status-matrix-v1.md](remaining-routes-status-matrix-v1.md)
