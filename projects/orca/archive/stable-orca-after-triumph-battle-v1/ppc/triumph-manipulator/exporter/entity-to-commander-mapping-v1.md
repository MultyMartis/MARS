# Entity-to-Commander Mapping v1

**Role:** Conceptual mapping from `OrcaPpcDocument` entities → Commander Excel transport rows.  
**Stance:** Field-for-field copy + enum translation — **no** semantic inference.

**Column names:** **Logical keys** below. Exact header literals in `.xlsx` must be read from [triumph-manipulator-commander-template-v0.xlsx](../assets/direct-commander-template/triumph-manipulator-commander-template-v0.xlsx) at implementation — **SAFE UNKNOWN** until verified.

---

## Field name alignment (JSON instance)

Triumph draft JSON uses:

| Document path | Notes |
|---------------|-------|
| `ads[].status` | `draft` \| `active` (maps to logical `ad_status`) |
| `keyword_cluster.keywords[].phrase` | Keyword text |
| `keyword_cluster.keywords[].match_policy` | `exact` \| `phrase` \| `broad` |
| `keyword_cluster.keywords[].status` | Keyword row active/paused (future) |

Markdown entity docs may say `ad_status` / `text` — exporter normalizes to JSON instance paths.

---

## Logical workbook sections

| Section | Entity source | Row pattern |
|---------|---------------|-------------|
| Campaign settings | `campaigns[]` | One row per campaign (settings block) |
| Ad groups | `campaigns[].groups[]` | One row per group |
| Keywords | `groups[].keyword_cluster.keywords[]` | One row per keyword |
| Ads | `groups[].ads[]` | One row per ad |
| Campaign negatives | `campaigns[].campaign_negatives.keywords[]` | One row per negative phrase |
| Group negatives | `groups[].group_negatives.keywords[]` | One row per negative phrase |
| Fastlinks | `ads[].fastlinks[]` | One row per fastlink (extension block) |
| Callouts | `ads[].callouts[]` | One row per callout |
| Campaign extensions | `campaigns[].extensions.*` (if present) | Expand per template |

Sheet boundaries follow template — may be one sheet or multiple (**verify from xlsx**).

---

## Campaign → campaign row

| Internal field | Logical column | Transform |
|----------------|----------------|-----------|
| `campaign_name` | Campaign name | verbatim copy |
| `campaign_type` | Campaign type | map `search` → template search literal |
| `search_only_scope` | — | **not exported** (internal guard) |
| `geo.primary_region` | Region / geo text | verbatim; region ID lookup **SAFE UNKNOWN** |
| `geo.geo_notes` | Notes (if column exists) | optional copy |
| `strategy.strategy_label` | Strategy | verbatim |
| `strategy.bid_intent` | Notes | optional |
| `strategy.priority_tier` | — | **do not export** (internal) |
| `schedule.*` | Schedule columns | copy if `schedule.enabled` |
| `device_adjustments.*` | Device modifiers | numeric copy or empty |
| `intent_classification` | — | **do not export** |
| `routing_role` | — | **do not export** |
| `campaign_id` | ORCA Entity ID (optional) | only if operator enables metadata column |

---

## Group → group row

| Internal field | Logical column | Transform |
|----------------|----------------|-----------|
| `group_name` | Ad group name | verbatim |
| `landing_route.final_url` | Group default URL | copy if template supports group-level URL |
| `group_id` | ORCA Entity ID (optional) | traceability |
| `semantic_intent` | — | **do not export** |
| `intent_tier` | — | **do not export** |
| `intent_type` | — | **do not export** |
| `intent_purity_markers` | — | **do not export** |
| `landing_route.blueprint_id` | Notes (optional) | operator diagnostic only |
| `keyword_cluster.intent_summary` | Notes (optional) | not required for import |

Parent linkage: each group row carries **Campaign name** (join key) = parent `campaign_name`.

---

## Keyword → keyword row

One transport row per `keyword_cluster.keywords[]` item where export policy includes it (default: `status: active`).

| Internal field | Logical column | Transform |
|----------------|----------------|-----------|
| `phrase` | Keyword | verbatim |
| `match_policy` | Match type | enum map (see below) |
| `is_primary` | — | **do not export** (internal) |
| `status` | Keyword status | map if template supports paused rows |
| parent `group_name` | Ad group | FK join |
| parent `campaign_name` | Campaign | FK join |

### Match type enum map

| `match_policy` | Logical Commander value |
|----------------|-------------------------|
| `exact` | Exact |
| `phrase` | Phrase |
| `broad` | Broad |

Replace literals from template header row at implementation.

---

## Ad → ad row

| Internal field | Logical column | Transform |
|----------------|----------------|-----------|
| `headline_1` | Title 1 / Headline 1 | verbatim — **no truncation** |
| `headline_2` | Title 2 / Headline 2 | copy if non-empty |
| `description` | Text / Description | verbatim |
| `display_url.domain` | Display URL domain | verbatim |
| `display_url.path_1` | Path 1 | verbatim |
| `display_url.path_2` | Path 2 | verbatim if present |
| `landing_url` | Final URL / Link | verbatim URL |
| `status` | Ad status / State | map `draft` / `active` → template markers |
| `ad_id` | ORCA Entity ID (optional) | traceability |
| `keyword_alignment.*` | — | **do not export** |
| `yandex_bold_highlight.*` | — | **do not export** |
| `mobile_first_readability.*` | — | **do not export** |
| `validation_notes` | Notes (optional) | operator only |

Parent linkage: **Campaign name** + **Ad group name**.

---

## Fastlink → extension row

| Internal field | Logical column | Transform |
|----------------|----------------|-----------|
| `title` | Sitelink title / Fast link title | verbatim |
| `url` | Sitelink URL | verbatim if present |
| `description_1` | Description line 1 | if template has |
| `intent_role` | Notes (optional) | **do not export** by default |
| parent ad keys | Campaign + Ad group + Ad ref | attach per template extension model |

Attachment: extensions link to parent **ad** or **group** per Commander rules — follow template examples (**SAFE UNKNOWN** for exact attachment column).

---

## Callout → extension row

| Internal field | Logical column | Transform |
|----------------|----------------|-----------|
| `text` | Callout text | verbatim |
| `intent_role` | — | **do not export** |
| parent ad keys | Campaign + Ad group | attach per template |

---

## Negatives → negative rows

### Campaign-level

Source: `campaigns[].campaign_negatives.keywords[]` (string list or objects per schema).

| Internal | Logical column |
|----------|----------------|
| negative phrase | Negative keyword |
| `campaign_negatives.match_type_default` | Match type default for rows |
| parent `campaign_name` | Campaign |

### Group-level

Source: `groups[].group_negatives.keywords[]`

| Internal | Logical column |
|----------|----------------|
| negative phrase | Negative keyword |
| `group_negatives.match_type_default` | Match type |
| parent `group_name` | Ad group |
| parent `campaign_name` | Campaign |

---

## Fields never exported (internal-only)

| Field family | Reason |
|--------------|--------|
| Intent purity / tier / classification | Semantic — not Commander columns |
| Landing blueprint ids (default) | Internal routing; optional Notes only |
| Validation markers | Already in ValidationReport |
| `source_pack`, `project_id` (default) | Manifest only, not campaign sheet |

---

## Export manifest mapping (future, not Commander sheet)

| Manifest field | Source |
|----------------|--------|
| `document_id` | `project_id` |
| `validation_report_timestamp` | report |
| `template_version` | contract |
| `row_counts` | per section |
| `exported_entity_ids` | campaigns, groups, ads |

---

## Testing mapping (human)

1. Export single group: 2 keywords, 1 active ad, 2 callouts.  
2. Import to test Commander account.  
3. Compare field-by-field to document JSON.  
4. Log header literal mismatches in pack notes.

---

## Related

- [row-generation-rules-v1.md](row-generation-rules-v1.md)  
- [field-normalization-rules-v1.md](field-normalization-rules-v1.md)  
- [schema/export-mapping-schema-v1.md](../schema/export-mapping-schema-v1.md)
