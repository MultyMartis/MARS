# Row Generation Rules v1

**Role:** Deterministic rules for expanding entities into Commander Excel rows.  
**Goal:** Stable, human-readable workbooks that import cleanly.

---

## Global ordering (deterministic)

Within one export run, emit rows in this **strict order**:

```
1. Campaign rows          (sort: campaign_name ASC)
2. Group rows             (per campaign: group_name ASC)
3. Keyword rows           (per group: is_primary DESC, phrase ASC)
4. Ad rows                (per group: status active first, ad_id ASC)
5. Group negative rows    (per group: phrase ASC)
6. Campaign negative rows (per campaign: phrase ASC)
7. Fastlink rows          (per ad: array order preserved)
8. Callout rows           (per ad: array order preserved)
9. Campaign extension rows (if any)
```

**Rationale:** Commander and operators expect parent before children; stable sort enables diff-friendly golden exports.

---

## Parent-child relationships

Every child row carries join keys:

| Child row | Required parent keys |
|-----------|---------------------|
| Group | `Campaign name` |
| Keyword | `Campaign name`, `Ad group name` |
| Ad | `Campaign name`, `Ad group name` |
| Group negative | `Campaign name`, `Ad group name` |
| Campaign negative | `Campaign name` |
| Fastlink / Callout | `Campaign name`, `Ad group name`, + ad identifier per template |

**Ad identifier:** Prefer `ad_id` in optional metadata column; if template uses row order only, ads must be emitted in fixed order within group.

---

## Entity references (traceability)

Optional column **ORCA Entity ID** (operator-enabled):

| Row type | Value |
|----------|-------|
| Campaign | `campaign_id` |
| Group | `group_id` |
| Ad | `ad_id` |
| Keyword | `{group_id}:{phrase_hash}` synthetic stable id |

Purpose: map Commander import errors back to JSON without opening governance systems.

---

## Duplicate prevention

| Duplicate type | Policy |
|----------------|--------|
| Same keyword `phrase` twice in one group | **Block** export — `DUPLICATE_KEYWORD_ROW` |
| Same negative phrase twice at same level | Dedup keep first, log manifest warning |
| Same `ad_id` twice | **Block** — graph error |
| Identical ad copy rows (H1+H2+desc) | **Allow** but manifest warns — validation SE-08 should have caught |

Keyword dedup normalization for duplicate check only: trim, lowercase, ё→е — **does not** change exported text ([field-normalization-rules-v1.md](field-normalization-rules-v1.md)).

---

## Extension attachment logic

1. Emit parent **ad row** first (or per template: extensions interleaved — **verify xlsx**).  
2. For each `fastlinks[]` item → one extension row linked to parent ad keys.  
3. For each `callouts[]` item → one callout row.  
4. Do **not** synthesize fastlinks from landing sitemap — only entity array contents.  
5. Do **not** drop fastlinks because “decorative” — validation should have failed SE-11 already.

**SAFE UNKNOWN:** Whether Commander expects extensions on separate sheet vs inline — follow template structure.

---

## Row counts and survivability

| Guard | Action |
|-------|--------|
| >500 keywords in one group | Block — `ROW_EXPLOSION` (validation should warn SE-13) |
| >20 ads in one group | Block — `AD_ROW_EXPLOSION` |
| Empty group (no keywords, no ads) | Block — ST-04/05 |

Preserves anti-chaos doctrine without semantic rewriting.

---

## Human readability after import

| Practice | Rule |
|----------|------|
| Group names | Copy `group_name` verbatim — no auto-slug |
| Campaign name | Copy `campaign_name` verbatim |
| Tier prefixes | Keep `01 — …` numbering from draft fixture |
| Notes column | Optional `validation_notes` / blueprint id for operator |

Commander UI should read naturally in Russian without ORCA internal codes in primary columns.

---

## Workbook generation (logical)

```
load template clone
for campaign in sorted(campaigns):
  write campaign row
  for group in sorted(campaign.groups):
    write group row
    for kw in sorted(keywords): write keyword row
    for ad in sorted(ads): write ad row
    for neg in sorted(group_negatives): write neg row
    for ad in ads:
      for fl in ad.fastlinks: write fastlink row
      for co in ad.callouts: write callout row
  for neg in sorted(campaign_negatives): write campaign neg row
save xlsx
```

No parallel sheet writes that reorder parents after children.

---

## Related

- [draft-export-rules-v1.md](draft-export-rules-v1.md)  
- [entity-to-commander-mapping-v1.md](entity-to-commander-mapping-v1.md)
