# FP-0002 Static Demo — Scale & Risk v1

## Scale

| Template type | Page count |
| --- | --- |
| HOME_PAGE_TEMPLATE | 1 |
| SERVICES_HUB_INTERNAL_PAGE | 1 |
| SERVICE_SUBDIVISION_INTERNAL_PAGE | 6 |
| SERVICE_LEAF_INTERNAL_PAGE | 18 |
| PLACEHOLDER_PAGE | 30 |
| TOTAL | 56 |

| Metric | Value |
| ------ | ----: |
| Maximum hierarchy depth | 4 |
| Menu pages | 8 |
| Footer-only pages | 4 |
| Unresolved parents | 0 |
| Duplicate URLs | 0 |
| Duplicate titles | 0 |
| Duplicate H1 | 0 |

## Main risks

1. **Excel placeholder slots** (`Название`) — final service list incomplete.
2. **Blog duplicate slug** in Excel — demo uses generated suffix slugs.
3. **Hyperlink targets in Excel** stale — registry uses display URLs only.
4. **Nested dist output** may require Gulp architecture extension (technical risk — document in PASS 2).
5. **URL typos** (`specyalisty`, `pilzovatelyu`) preserved per Excel authority for demo.
