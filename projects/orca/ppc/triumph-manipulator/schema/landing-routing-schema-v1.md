# Landing Routing Schema v1

**Entity fragment:** `LandingRoute` (embedded on `Group`)  
**Role:** Bind group intent → best-fit landing blueprint + URL + fallback policy.

---

## Principles

1. **Intent continuity** — ad promise must match page hero and qualification ([doctrine](../doctrine/generation-logic-v0.md)).  
2. **No single universal landing** — route by intent family.  
3. **Blueprint ref is SoT for meaning** — URL is deploy target; blueprint is qualification spec.  
4. **Fallback is explicit** — never silent misroute to master page without flag.

---

## `LandingRoute` field specification

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `landing_type` | enum | yes | Routing family |
| `blueprint_id` | string | yes | Maps to `landing-pages/*.md` |
| `blueprint_path` | string | no | Repo-relative path for operators |
| `final_url` | string | yes | Live or staging URL |
| `use_case_route` | UseCaseRoute \| null | conditional | When `landing_type` = use_case |
| `capability_route` | CapabilityRoute \| null | conditional | When `landing_type` = capability |
| `b2b_route` | B2bRoute \| null | conditional | When `landing_type` = b2b |
| `intercity_route` | IntercityRoute \| null | conditional | When `landing_type` = intercity |
| `fallback_route` | FallbackRoute | yes | Degradation policy |
| `intent_continuity_ack` | boolean | yes | Human/assist confirms ad↔landing match |

---

## `landing_type` (enum)

| Value | Purpose |
|-------|---------|
| `master_hot` | General hot commercial entry |
| `use_case` | Task-specific qualification page |
| `capability` | Machine spec / tonnage / reach |
| `b2b` | Юрлица, documents, безнал |
| `intercity` | Regional / межгород logistics |
| `fallback` | Controlled degradation only |

---

## Blueprint registry (v1)

| `blueprint_id` | File | Intent |
|----------------|------|--------|
| `01-master-hot-general` | [01-master-hot-general.md](../landing-pages/01-master-hot-general.md) | Hot general |
| `02-use-case-bytovka` | [02-use-case-bytovka.md](../landing-pages/02-use-case-bytovka.md) | Бытовка |
| `03-use-case-stroymaterialy` | [03](../landing-pages/03-use-case-stroymaterialy.md) | Стройматериалы |
| `04-use-case-oborudovanie` | [04](../landing-pages/04-use-case-oborudovanie.md) | Оборудование |
| `05-capability-5-ton` | [05](../landing-pages/05-capability-5-ton.md) | 5 т |
| `06-b2b-yurlica` | [06](../landing-pages/06-b2b-yurlica.md) | B2B |
| `07-capability-6x6-vezdekhod` | [07](../landing-pages/07-capability-6x6-vezdekhod.md) | 6×6 |
| `08-intercity-krai` | [08](../landing-pages/08-intercity-krai.md) | Межгород/край |
| `09-use-case-fbs-zhb` | [09](../landing-pages/09-use-case-fbs-zhb.md) | ФБС/ЖБИ |
| `10-use-case-konteynery` | [10](../landing-pages/10-use-case-konteynery.md) | Контейнеры |
| `11-use-case-armatura` | [11](../landing-pages/11-use-case-armatura.md) | Арматура |
| `12-use-case-kirpich-bloki` | [12](../landing-pages/12-use-case-kirpich-bloki.md) | Кирпич/блоки |

---

## `UseCaseRoute`

| Field | Type | Required |
|-------|------|----------|
| `use_case_class` | enum | yes — mirrors [group schema](group-entity-schema-v1.md) |
| `cargo_semantics` | string | no | What is being moved/lifted |
| `hero_must_show` | string[] | no | e.g. `бытовка на борту` |

---

## `CapabilityRoute`

| Field | Type | Required |
|-------|------|----------|
| `capability_class` | enum | yes |
| `tonnage_claim` | string | no | Must match real machine |
| `boom_claim` | string | no | |
| `terrain_claim` | string | no | e.g. `6x6`, `вездеход` |

**Rule:** Claims in ads must be supportable on capability landing hero.

---

## `B2bRoute`

| Field | Type | Required |
|-------|------|----------|
| `payment_semantics` | string[] | no | `безнал`, `НДС`, `договор` |
| `document_trust_elements` | string[] | no | |
| `object_scale_hint` | string | no | стройка, склад, … |

---

## `IntercityRoute`

| Field | Type | Required |
|-------|------|----------|
| `distance_semantics` | string | yes | e.g. `по краю`, `межгород` |
| `origin_region` | string | yes | Краснодар |
| `destination_policy` | string | no | Human-defined service area |

---

## `FallbackRoute`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `allowed` | boolean | yes | If false, missing page = validation fail |
| `fallback_blueprint_id` | string | conditional | Usually `01-master-hot-general` |
| `fallback_url` | string | conditional | |
| `fallback_reason` | enum | yes | `staging` \| `url_not_live` \| `temporary` \| `none` |

**Policy:**

| Situation | Allowed fallback |
|-----------|------------------|
| Exact blueprint live | **No** fallback needed |
| Staging URL | `allowed=true`, reason `staging`, document in notes |
| Intent-specific group | **Discouraged** fallback to master — warn at validation |
| Wrong intent on master | **Fail** — do not use fallback to hide mismatch |

---

## Routing decision matrix (operator)

| Group intent signal | `landing_type` | Typical blueprint |
|--------------------|----------------|-------------------|
| «заказать/вызвать манипулятор» general | `master_hot` | 01 |
| «для бытовки», «перевозка бытовки» | `use_case` | 02 |
| «5 тонн», «стрела», «6x6» | `capability` | 05 / 07 |
| «юрлицо», «безнал», «НДС» | `b2b` | 06 |
| «по краю», «межгород» | `intercity` | 08 |

Tier priority: [intent-groups-v1.md](../research/intent-groups-v1.md).

---

## Intent continuity checklist

Before `intent_continuity_ack: true`:

- [ ] Primary keyword phrase reflected in landing hero (blueprint)  
- [ ] CTA type compatible (call / calculate)  
- [ ] Capability claims in ad ≤ capability on page  
- [ ] Use-case cargo matches page section focus  
- [ ] B2B payment language present on B2B page when promised in ad  

---

## Validation touchpoints

| Failure | Severity |
|---------|----------|
| `landing_type` vs `blueprint_id` mismatch | error |
| `final_url` empty | error |
| Use-case group without `use_case_route` | error |
| Specific intent + master fallback without reason | warn |
| Ad `landing_url` ≠ group `final_url` without override note | warn/error |

---

## Export touchpoints

`final_url` maps to Commander ad/group URL columns — [export-mapping-schema-v1.md](export-mapping-schema-v1.md). Exporter copies URL only; does not pick blueprint.

---

## Production domain (v0.2 — operator-confirmed)

**Canonical host:** `https://manipulator-triumph.ru`  
**Policy:** SEO-safe slugs; trailing slash on path segments below is **recommended** but not enforced by exporter.

| Route role | `final_url` (production) | Typical `blueprint_id` |
|------------|--------------------------|-------------------------|
| Master hot | `https://manipulator-triumph.ru/` | `01-master-hot-general` |
| 5 t capability | `https://manipulator-triumph.ru/manipulyator-5-tonn/` | `05-capability-5-ton` |
| Бытовка use-case | `https://manipulator-triumph.ru/perevozka-bytovok/` | `02-use-case-bytovka` |
| B2B / юрлица | `https://manipulator-triumph.ru/manipulyator-dlya-yurlic/` | `06-b2b-yurlica` |
| Вездеход 6×6 | `https://manipulator-triumph.ru/manipulyator-vezdehod/` | `07-capability-6x6-vezdekhod` |
| Стройматериалы | `https://manipulator-triumph.ru/dostavka-stroymaterialov/` | `03-use-case-stroymaterialy` |

**Display URL vs landing URL (v0.3):**

| Field | Role | Example |
|-------|------|---------|
| `landing_url` / `landing_route.final_url` | Full HTTPS click target | `https://manipulator-triumph.ru/manipulyator-5-tonn/` |
| `display_url.path_1` | Short **Commander display path** (CTR artifact) | `manip-5-tonn` |
| `display_url.domain` | Document host coherence (SY-12) | `manipulator-triumph.ru` |

**Commander transport:** Exporter writes **path only** to col 49 — no domain, no slash (SY-17). Max **20** chars, `[a-z0-9-]` (SY-18). UTF-8 source → deterministic ASCII normalization.

**Sitelink routing:** `fastlinks[].url` must use slugs from production table above — reinforces group intent; duplicate URLs per ad = validation error (SY-14, CM-11).

**Deprecated placeholder:** `triumph-krd.ru` — replace in fixtures and drafts; validation SY-12 warns on host mismatch.

---

## SAFE UNKNOWN

- Future URL revisions (pricing page, `/tarify/`, regional subpaths) — confirm with site operator before changing `final_url` registry.  
- UTM / tracking parameter standard — not defined in v1.  
- Whether Commander normalizes trailing slashes on import — **human-verify** per import session.
