# Campaign Entity Schema v1

**Entity:** `Campaign`  
**Role:** Semantic container for a Yandex **Search** campaign — not a keyword dump.  
**Parent:** PPC project document · **Children:** `Group[]`

---

## Design rules

1. **Campaign = container** — intent separation happens primarily at **group** level unless psychology/landing differ at campaign scale ([doctrine](../doctrine/generation-logic-v0.md)).  
2. **Search-only** — v1 forbids RSYA / retargeting / master campaign fields.  
3. **Human-readable naming** — Russian, numbered groups downstream; campaign name must be operable in Commander UI.  
4. **Negatives at campaign level** — global junk protection; group-level negatives refine.

---

## Field specification

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `entity_id` | string | yes | Stable internal ID |
| `campaign_name` | string | yes | Commander-visible name; human-readable RU |
| `campaign_type` | enum | yes | v1: `search` only |
| `search_only_scope` | boolean | yes | Must be `true` in v1 |
| `geo` | GeoBlock | yes | Target geography for Triumph (Krasnodar + policy) |
| `strategy` | StrategyBlock | yes | Bidding/strategy **intent** — human executes in Direct |
| `negatives` | NegativeList | yes | Campaign-level minus-words |
| `schedule` | ScheduleBlock | no | Day/time intent — may be empty = platform default |
| `device_adjustments` | DeviceAdjustments | no | Desktop/tablet/mobile bid modifiers (human applies) |
| `extensions` | ExtensionsBlock | no | Sitelinks, callouts at campaign level if used |
| `intent_classification` | IntentClass | yes | Dominant campaign intent family |
| `routing_role` | RoutingRole | yes | How this campaign fits landing/campaign split architecture |
| `groups` | Group[] | yes | ≥1 group |
| `notes` | string | no | Operator notes — not exported |

---

## `campaign_type` (v1 enum)

| Value | Allowed v1 | Notes |
|-------|------------|-------|
| `search` | **yes** | Only production type in Phase 2 |
| `rsya` | **no** | Document only — do not instantiate |
| `master` | **no** | Out of scope |
| `retargeting` | **no** | Out of scope |

---

## `GeoBlock`

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `primary_region` | string | yes | e.g. `Краснодар` |
| `region_ids` | string[] | no | Future: Direct region IDs — **SAFE UNKNOWN** until mapped |
| `geo_notes` | string | no | Intercity groups may still use campaign geo with group-level messaging |

**Triumph default:** Krasnodar operational zone; intercity handled via dedicated groups + [landing-routing](landing-routing-schema-v1.md).

---

## `StrategyBlock`

Documents **intent for humans** — ORCA does not autobid.

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `strategy_label` | string | yes | e.g. `manual_cpc`, `search_coverage` |
| `bid_intent` | string | no | Operator description |
| `budget_intent` | string | no | Daily/monthly intent — not autonomous |
| `priority_tier` | enum | no | Aligns with research: `S` \| `A` \| `B` \| `X` |

---

## `NegativeList`

| Field | Type | Required |
|-------|------|----------|
| `keywords` | string[] | yes (may be empty only if documented) |
| `match_type_default` | enum | no — default `phrase` |

**Campaign-global examples** (from doctrine): `вакансии`, `работа`, `купить`, `ремонт`, `эвакуатор`.

**Conditional negatives** (e.g. `дешево`, `бесплатно`) — flag in `negatives.conditional[]` with `reason` for human review.

---

## `ScheduleBlock`

| Field | Type | Required |
|-------|------|----------|
| `enabled` | boolean | yes |
| `schedule_notes` | string | no |
| `hours_matrix` | object | no — future exporter detail |

---

## `DeviceAdjustments`

| Field | Type | Notes |
|-------|------|-------|
| `desktop_modifier` | number \| null | % adjustment intent |
| `tablet_modifier` | number \| null | |
| `mobile_modifier` | number \| null | Mobile-first ads still required at Ad layer |

---

## `ExtensionsBlock` (campaign-level)

Optional sitelink/callout **campaign** extensions when not ad-specific.

| Field | Type |
|-------|------|
| `sitelinks` | SitelinkItem[] |
| `callouts` | string[] |

Ad-level fastlinks/callouts remain on [Ad](ad-entity-schema-v1.md).

---

## `intent_classification` (enum)

Campaign-level **dominant** intent family (groups may refine):

| Value | When to use |
|-------|-------------|
| `hot_general` | Master commercial entry |
| `use_case` | Task-specific segments (бытовка, стройматериалы, …) |
| `capability` | Tonage, boom, 6×6, machine spec |
| `b2b` | Юрлица, безнал, документы |
| `intercity` | По краю / межгород |
| `mixed_container` | **Discouraged** — prefer split campaigns |

If `mixed_container` → validation should **warn** ([validation-schema-v1.md](validation-schema-v1.md)).

---

## `routing_role` (enum)

Describes why this campaign exists in the **landing/campaign split** architecture:

| Value | Meaning |
|-------|---------|
| `primary_search` | Main commercial search container |
| `capability_split` | Separated capability-heavy psychology |
| `b2b_split` | B2B/document psychology separated |
| `use_case_split` | Use-case family separated from hot general |
| `intercity_split` | Regional/long-haul separated |
| `experimental` | Human-flagged test — extra validation scrutiny |

---

## Campaign split doctrine (operational)

**Split into separate campaigns** when:

- Landing psychology differs at scale (e.g. B2B vs hot general)
- Intent classification would be `mixed_container` without split
- Operator needs independent budgets/negatives

**Keep one campaign** when:

- Intents differ only at group granularity
- Same geo, same core commercial stage

---

## Minimal valid example (logical)

```yaml
entity_id: camp_triumph_search_main_v1
campaign_name: "Триумф — Поиск — Краснодар"
campaign_type: search
search_only_scope: true
geo:
  primary_region: Краснодар
strategy:
  strategy_label: manual_cpc
  priority_tier: S
negatives:
  keywords: [вакансии, работа, купить, ремонт, эвакуатор]
schedule:
  enabled: false
device_adjustments: {}
extensions: {}
intent_classification: hot_general
routing_role: primary_search
groups: []   # populated with Group entities
```

---

## Validation touchpoints

| Check | Schema |
|-------|--------|
| Required fields | [validation-schema-v1.md](validation-schema-v1.md) § structural |
| `search_only_scope` | Must be true |
| Empty `groups` | Fail |
| Global negatives present for launch-ready | Warn if empty |

---

## Export touchpoints

Campaign-level rows map via [export-mapping-schema-v1.md](export-mapping-schema-v1.md) — campaign sheet / campaign block in Commander template.

---

## SAFE UNKNOWN

- Exact Yandex Direct campaign settings keys for API/automation — not in repo.  
- Region ID table for Krasnodar — confirm against live Direct + template at export time.
