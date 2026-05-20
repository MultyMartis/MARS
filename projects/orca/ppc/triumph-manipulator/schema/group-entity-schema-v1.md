# Group Entity Schema v1

**Entity:** `Group`  
**Role:** **One semantic intent** + keyword cluster + landing route + ads.  
**Parent:** `Campaign` · **Children:** `Ad[]`

---

## Core rule

> **One group = one semantic intent.**

Forbidden: mixed employment / buy / repair / generic rent chaos in a single group ([doctrine](../doctrine/generation-logic-v0.md), [intent-groups](../research/intent-groups-v1.md)).

---

## Field specification

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `entity_id` | string | yes | Stable internal ID |
| `parent_campaign_id` | string | yes | FK to campaign |
| `group_name` | string | yes | Human-readable RU; sequential numbering recommended |
| `semantic_intent` | string | yes | Short intent label (operator language) |
| `keyword_cluster` | KeywordCluster | yes | Keywords sharing commercial meaning |
| `negatives` | NegativeList | yes | Group-level minus-words |
| `landing_route` | LandingRoute | yes | See [landing-routing-schema-v1.md](landing-routing-schema-v1.md) |
| `ad_list` | Ad[] | yes | ≥1 ad |
| `intent_purity_markers` | IntentPurityMarkers | yes | Machine-checkable purity signals |
| `use_case_classification` | UseCaseClass \| null | conditional | Required when intent family is use-case |
| `capability_classification` | CapabilityClass \| null | conditional | Required when intent family is capability |
| `intent_tier` | enum | no | `S` \| `A` \| `B` \| `X` from research |
| `draft_status` | enum | no | `draft` \| `review` \| `approved_for_export` |
| `notes` | string | no | Operator notes |

---

## `group_name` conventions

| Pattern | Example |
|---------|---------|
| Numbered prefix | `03 — Манипулятор 5 тонн` |
| Intent-visible | `07 — Перевозка бытовок` |
| Avoid | Generic `Группа 1`, `Новая группа` |

Survivability: names are debugged in Commander months later.

---

## `semantic_intent`

Free-text **operator label** that must match:

- `keyword_cluster.intent_summary`
- Ad keyword alignment primary phrase
- Landing route intent

Example: `Перевозка бытовки — exact use-case`.

---

## `KeywordCluster`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `intent_summary` | string | yes | One-line commercial meaning |
| `keywords` | KeywordItem[] | yes | ≥1 keyword |
| `cluster_rules_ack` | boolean | yes | Operator/assist confirms semantic clustering doctrine |

### `KeywordItem`

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `text` | string | yes | Lowercase normalization recommended |
| `match_type` | enum | yes | `exact` \| `phrase` \| `broad` — Triumph search prefers `phrase`/`exact` |
| `is_primary` | boolean | no | Primary phrase for ad alignment |

**Good cluster:**

- заказать манипулятор  
- вызвать манипулятор  

**Bad cluster (reject at validation):**

- заказать манипулятор + работа манипулятор + ремонт + купить

---

## `NegativeList` (group-level)

Refines campaign negatives for this intent.

| Field | Type |
|-------|------|
| `keywords` | string[] |
| `match_type_default` | enum |

Example: capability group may add negatives blocking wrong tonnage queries.

---

## `IntentPurityMarkers`

Checklist-backed fields for validation engine / human QA:

| Field | Type | Required | Meaning |
|-------|------|----------|---------|
| `single_intent_confirmed` | boolean | yes | Human or assist attests one intent |
| `reject_list_checked` | boolean | yes | Checked against tier X / junk list in research |
| `no_employment_intent` | boolean | yes | No job-seeker semantics |
| `no_purchase_asset_intent` | boolean | yes | No «купить манипулятор» |
| `no_repair_intent` | boolean | yes | No repair semantics |
| `cross_intent_risk` | enum | yes | `none` \| `low` \| `high` |

If `cross_intent_risk` = `high` → validation **fail** until split.

---

## `use_case_classification` (enum)

Required when group maps to use-case landing family:

| Value | Blueprint ref (typical) |
|-------|-------------------------|
| `bytovka` | `landing-pages/02-use-case-bytovka.md` |
| `stroymaterialy` | `03-use-case-stroymaterialy.md` |
| `oborudovanie` | `04-use-case-oborudovanie.md` |
| `fbs_zhb` | `09-use-case-fbs-zhb.md` |
| `konteynery` | `10-use-case-konteynery.md` |
| `armatura` | `11-use-case-armatura.md` |
| `kirpich_bloki` | `12-use-case-kirpich-bloki.md` |
| `other_use_case` | Custom — requires `notes` + human approval |

---

## `capability_classification` (enum)

Required when group maps to capability landing family:

| Value | Blueprint ref (typical) |
|-------|-------------------------|
| `tonnage_5t` | `05-capability-5-ton.md` |
| `vezdekhod_6x6` | `07-capability-6x6-vezdekhod.md` |
| `boom_reach` | Capability emphasis — human specifies in `notes` |
| `brand_chassis` | e.g. КАМАЗ — ensure machine truth |
| `other_capability` | Custom — human approval |

---

## Relationship to ads

| Rule | Detail |
|------|--------|
| Min ads | ≥1 per group |
| Max ads | Operator-defined; avoid uncontrolled variation spam |
| Alignment | Each ad must declare `keyword_alignment` → [ad schema](ad-entity-schema-v1.md) |
| Landing | Ads inherit group `landing_route.final_url` unless explicitly overridden with justification |

---

## Minimal valid example (logical)

```yaml
entity_id: grp_03_bytovka_v1
parent_campaign_id: camp_triumph_search_main_v1
group_name: "04 — Перевозка бытовок"
semantic_intent: Перевозка бытовки — exact use-case
keyword_cluster:
  intent_summary: Пользователь ищет перевозку/установку бытовки манипулятором
  keywords:
    - { text: перевозка бытовки краснодар, match_type: phrase, is_primary: true }
    - { text: манипулятор для бытовки, match_type: phrase }
  cluster_rules_ack: true
negatives:
  keywords: [купить бытовку, аренда бытовки]
landing_route:
  landing_type: use_case
  blueprint_id: "02-use-case-bytovka"
  final_url: "https://example.ru/bytovka"
  intent_continuity_ack: true
ad_list: []
intent_purity_markers:
  single_intent_confirmed: true
  reject_list_checked: true
  no_employment_intent: true
  no_purchase_asset_intent: true
  no_repair_intent: true
  cross_intent_risk: none
use_case_classification: bytovka
capability_classification: null
intent_tier: S
```

---

## Validation touchpoints

| Check | Reference |
|-------|-----------|
| Single intent | [validation-schema-v1.md](validation-schema-v1.md) § semantic |
| Keyword cluster coherence | § semantic |
| Landing match | § semantic + continuation |
| Non-empty `ad_list` | § structural |
| Classification vs landing_type | § structural |

---

## Export touchpoints

Group maps to Commander **ad group** rows + keyword rows + shared negatives — [export-mapping-schema-v1.md](export-mapping-schema-v1.md).
