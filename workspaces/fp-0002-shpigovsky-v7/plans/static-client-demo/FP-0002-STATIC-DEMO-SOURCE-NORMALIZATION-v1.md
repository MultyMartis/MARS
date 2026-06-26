# FP-0002 Static Demo — Source Normalization v1

## Summary

| Metric | Value |
| ------ | ----: |
| Total source rows (sheet) | 53 |
| Empty/separator rows | 0 |
| Page rows (registry) | 56 |
| Explicit hierarchy | 48 |
| Inferred hierarchy / URL | 12 |
| Unresolved parent rows | 0 |
| Duplicate raw names (`Название`) | 5 (disambiguated in registry) |

## Normalization rules applied

- URL from column A display text (not hyperlink target)
- Trailing spaces and `//` normalized
- Parent resolved by URL prefix walk
- Excel duplicate `/blog/nazvanie-stati/` → demo slugs `-1`, `-2` suffix (**DEMO_GENERATED_SLUG**)
- Rows without URL → inferred slug under resolved parent (**LOW** confidence)
- Footer legal pages from runtime footer.html (**INFERRED**, not in Excel)

## Full intermediate registry

See `data/demo-page-registry.draft.json` → `pages[]` fields: `source_row`, `raw_name`, `normalized_name`, `hierarchy_level`, `parent_raw`, `parent_resolved`, `raw_url`, `source_notes`, `confidence`.
