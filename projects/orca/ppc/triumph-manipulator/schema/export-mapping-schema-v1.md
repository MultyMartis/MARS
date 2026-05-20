# Export Mapping Schema v1

**Role:** Map internal PPC entities → Direct Commander Excel transport.  
**Exporter stance:** **Dumb transport only** — no semantic reasoning, no generation, no intent fixes.

---

## Principles

| # | Rule |
|---|------|
| 1 | Input = **validated** entity graph only |
| 2 | Output = Commander-compatible `.xlsx` per [template](../assets/direct-commander-template/) |
| 3 | Mapping is **field-for-field** + formatting |
| 4 | Excel is **not** source-of-truth |
| 5 | Draft vs active rows supported |

Reference: [direct-commander-foundation-v0.md](../export/direct-commander-foundation-v0.md).

---

## Export pipeline (future)

```
ValidatedPpcDocument
    → export-mapping (this doc)
    → xlsx writer
    → triumph-manipulator-commander-template-v0.xlsx shape
    → human import in Commander
```

---

## Sheet / section model (logical)

Template structure follows live Commander export (see template README). Logical sections:

| Section | Source entities |
|---------|-----------------|
| Campaign settings | `Campaign` |
| Ad groups | `Group` |
| Keywords | `Group.keyword_cluster` |
| Ads | `Group.ad_list` |
| Negatives | `Campaign.negatives` + `Group.negatives` |
| Extensions | `Campaign.extensions`, ad fastlinks/callouts |

**SAFE UNKNOWN:** Exact sheet names and column order — read from `triumph-manipulator-commander-template-v0.xlsx` at implementation time; table below uses **logical column keys**.

---

## Campaign mapping

| Internal field | Excel logical column | Transform |
|----------------|----------------------|-----------|
| `campaign_name` | `Campaign name` | copy |
| `campaign_type` | `Campaign type` | map `search` → template search value |
| `geo.primary_region` | `Region` / geo columns | copy; ID lookup future |
| `strategy.strategy_label` | Strategy columns | copy as text |
| `schedule.*` | Schedule columns | copy if enabled |
| `device_adjustments.*` | Device bid modifier columns | numeric copy |
| `extensions.sitelinks` | Campaign sitelink rows | row expand |
| `extensions.callouts` | Campaign callout rows | row expand |
| `negatives.keywords` | Campaign negative keywords | one row per keyword |

**Not exported from ORCA logic:** semantic labels like `intent_classification` — optional `Notes` column if template provides.

---

## Group mapping

| Internal field | Excel logical column | Transform |
|----------------|----------------------|-----------|
| `group_name` | `Ad group name` | copy |
| `landing_route.final_url` | Group default URL if template supports | copy |
| `semantic_intent` | — | **do not export** (internal) |
| `intent_purity_markers` | — | **do not export** |
| `entity_id` | — | optional hidden metadata column only if operator enables |

---

## Keyword mapping

One Excel row per `KeywordItem`:

| Internal field | Excel logical column | Transform |
|----------------|----------------------|-----------|
| `text` | `Keyword` | copy |
| `match_type` | `Match type` | enum map: `exact`→`Exact`, `phrase`→`Phrase`, `broad`→`Broad` |
| parent `group_name` | `Ad group` | FK join on export |
| parent `campaign_name` | `Campaign` | FK join on export |

---

## Ad mapping

| Internal field | Excel logical column | Transform |
|----------------|----------------------|-----------|
| `headline_1` | `Title 1` / `Headline 1` | copy verbatim |
| `headline_2` | `Title 2` / `Headline 2` | copy if present |
| `description` | `Text` / `Description` | copy verbatim |
| `display_url.domain` | `Display URL domain` | copy |
| `display_url.path_1` | `Path 1` | copy |
| `display_url.path_2` | `Path 2` | copy |
| `landing_url` | `Final URL` / `Link` | copy |
| `ad_status` | `Status` / draft flag | map `draft`→template draft value |
| `fastlinks[]` | Fast link extension rows | expand N rows |
| `callouts[]` | Callout extension rows | expand N rows |

**Forbidden exporter behaviors:**

- Truncate without validation report reference  
- Inject keywords into headlines  
- Change `landing_url` based on `landing_type`  
- Merge groups with different intents  

---

## Negative keyword mapping

| Source | Excel target |
|--------|--------------|
| `Campaign.negatives` | Campaign-level negative sheet/rows |
| `Group.negatives` | Group-level negative rows |

Match type: use `match_type_default` or per-item override when schema extended.

---

## Enum translation table (v1)

| Internal | Commander transport (placeholder) |
|----------|-----------------------------------|
| `campaign_type: search` | `Text & Image Ads` / search campaign type per template |
| `match_type: exact` | `Exact` |
| `match_type: phrase` | `Phrase` |
| `match_type: broad` | `Broad` |
| `ad_status: draft` | Template draft marker |
| `ad_status: active` | Template active marker |

**Implementer must** replace placeholders from template header row literals.

---

## Pre-export gate

Exporter **refuses** to run if:

- ValidationReport missing (future)  
- ValidationReport.passed = false  
- `schema_version` unsupported  

Today: human confirms validation manually.

---

## Idempotency and round-trip

| Concern | v1 policy |
|---------|-----------|
| Re-import Excel to entities | **Out of scope** — one-way export first |
| Stable row ordering | Sort by `group_name`, then `entity_id` |
| Character encoding | UTF-8 |

---

## Files and paths (future implementation)

| Artifact | Suggested path (not created in Phase 2) |
|----------|----------------------------------------|
| Mapping config | `tools/export-commander-v0/mapping-v1.yaml` |
| Template | `assets/direct-commander-template/triumph-manipulator-commander-template-v0.xlsx` |

---

## Testing export mapping (human)

1. Export one group with 1 ad + 2 keywords.  
2. Import in Commander test account.  
3. Verify limits, Cyrillic, draft flag, URL.  
4. Log discrepancies in pack notes — **not** in governance.

---

## SAFE UNKNOWN

- Exact column headers in xlsx — read from binary template.  
- Account-type-specific columns (brands, turbo pages) — human filter.  
- Whether Commander accepts all fastlink rows in one import batch — test operationally.
